import React, { createContext, useContext, useState, useEffect } from "react";
import { authAPI } from "../services/api";
import { AuthContextType, AuthState, User, RegisterData } from "../types/auth";

const initialState: AuthState = {
  user: null,
  token: localStorage.getItem("token"),
  isAuthenticated: false,
  loading: true,
  error: null,
};

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [state, setState] = useState<AuthState>(initialState);

  useEffect(() => {
    const initializeAuth = async () => {
      const token = localStorage.getItem("token");
      if (token) {
        try {
          const user = await authAPI.getCurrentUser();
          setState({
            user,
            token,
            isAuthenticated: true,
            loading: false,
            error: null,
          });
        } catch (error) {
          localStorage.removeItem("token");
          localStorage.removeItem("refreshToken");
          setState({
            ...initialState,
            loading: false,
          });
        }
      } else {
        setState({
          ...initialState,
          loading: false,
        });
      }
    };

    initializeAuth();
  }, []);

  const login = async (username: string, password: string): Promise<User> => {
    try {
      const { access, refresh } = await authAPI.login(username, password);
      localStorage.setItem("token", access);
      localStorage.setItem("refreshToken", refresh);
      const user = await authAPI.getCurrentUser();
      setState({
        user,
        token: access,
        isAuthenticated: true,
        loading: false,
        error: null,
      });
      return user;
    } catch (error: any) {
      const errorMessage = error.response?.data?.detail || "Login failed";
      setState((prev) => ({
        ...prev,
        error: errorMessage,
      }));
      throw new Error(errorMessage);
    }
  };

  const register = async (data: RegisterData): Promise<void> => {
    try {
      await authAPI.register(data);
      setState((prev) => ({
        ...prev,
        error: null,
      }));
    } catch (error: any) {
      const errorMessage =
        error.response?.data?.detail || "Registration failed";
      setState((prev) => ({
        ...prev,
        error: errorMessage,
      }));
      throw new Error(errorMessage);
    }
  };

  const logout = async () => {
    try {
      await authAPI.logout();
    } catch (error) {
      console.error("Logout error:", error);
    } finally {
      localStorage.removeItem("token");
      localStorage.removeItem("refreshToken");
      setState({
        ...initialState,
        loading: false,
      });
    }
  };

  const clearError = () => {
    setState((prev) => ({
      ...prev,
      error: null,
    }));
  };

  return (
    <AuthContext.Provider
      value={{
        ...state,
        login,
        register,
        logout,
        clearError,
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

export default AuthContext;
