import React, { createContext, useContext, useEffect, useState } from "react";
import { User, AuthState, LoginCredentials, RegisterData } from "../types/auth";
import { authAPI } from "../services/api";

interface AuthContextType extends AuthState {
  login: (credentials: LoginCredentials) => Promise<void>;
  register: (data: RegisterData) => Promise<void>;
  logout: () => Promise<void>;
  updateProfile: (data: Partial<User>) => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [state, setState] = useState<AuthState>({
    user: null,
    token: localStorage.getItem("token"),
    refreshToken: localStorage.getItem("refreshToken"),
    isAuthenticated: false,
    loading: true,
    error: null,
  });

  useEffect(() => {
    const loadUser = async () => {
      if (state.token) {
        try {
          const user = await authAPI.getCurrentUser();
          setState((prev) => ({
            ...prev,
            user,
            isAuthenticated: true,
            loading: false,
          }));
        } catch (error) {
          setState((prev) => ({
            ...prev,
            user: null,
            token: null,
            refreshToken: null,
            isAuthenticated: false,
            loading: false,
          }));
        }
      } else {
        setState((prev) => ({ ...prev, loading: false }));
      }
    };

    loadUser();
  }, [state.token]);

  const login = async (credentials: LoginCredentials) => {
    try {
      const { access, refresh } = await authAPI.login(credentials);
      localStorage.setItem("token", access);
      localStorage.setItem("refreshToken", refresh);
      const user = await authAPI.getCurrentUser();
      setState((prev) => ({
        ...prev,
        user,
        token: access,
        refreshToken: refresh,
        isAuthenticated: true,
        error: null,
      }));
    } catch (error: any) {
      setState((prev) => ({
        ...prev,
        error: error.response?.data?.detail || "Login failed",
      }));
      throw error;
    }
  };

  const register = async (data: RegisterData) => {
    try {
      await authAPI.register(data);
      await login({ username: data.username, password: data.password });
    } catch (error: any) {
      setState((prev) => ({
        ...prev,
        error: error.response?.data?.detail || "Registration failed",
      }));
      throw error;
    }
  };

  const logout = async () => {
    try {
      await authAPI.logout();
      setState({
        user: null,
        token: null,
        refreshToken: null,
        isAuthenticated: false,
        loading: false,
        error: null,
      });
    } catch (error: any) {
      setState((prev) => ({
        ...prev,
        error: error.response?.data?.detail || "Logout failed",
      }));
    }
  };

  const updateProfile = async (data: Partial<User>) => {
    try {
      if (!state.user?.id) throw new Error("User not found");
      const updatedUser = await authAPI.updateUser(state.user.id, data);
      setState((prev) => ({
        ...prev,
        user: updatedUser,
        error: null,
      }));
    } catch (error: any) {
      setState((prev) => ({
        ...prev,
        error: error.response?.data?.detail || "Profile update failed",
      }));
      throw error;
    }
  };

  return (
    <AuthContext.Provider
      value={{
        ...state,
        login,
        register,
        logout,
        updateProfile,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};
