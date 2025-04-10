import axios from "axios";
import { LoginCredentials, RegisterData, User } from "../types/auth";

const API_URL = "http://localhost:8000/api";

// Create axios instance with default config
const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Add token to requests if available
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle token refresh
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const refreshToken = localStorage.getItem("refreshToken");
      try {
        const { data } = await axios.post(`${API_URL}/token/refresh/`, {
          refresh: refreshToken,
        });
        localStorage.setItem("token", data.access);
        api.defaults.headers.common["Authorization"] = `Bearer ${data.access}`;
        return api(originalRequest);
      } catch (error) {
        localStorage.removeItem("token");
        localStorage.removeItem("refreshToken");
        window.location.href = "/login";
      }
    }
    return Promise.reject(error);
  }
);

export const authAPI = {
  login: async (credentials: LoginCredentials) => {
    const { data } = await api.post("/token/", credentials);
    return data;
  },

  register: async (userData: RegisterData) => {
    const { data } = await api.post("/users/", userData);
    return data;
  },

  logout: async () => {
    const refreshToken = localStorage.getItem("refreshToken");
    if (refreshToken) {
      await api.post("/token/blacklist/", { refresh: refreshToken });
    }
    localStorage.removeItem("token");
    localStorage.removeItem("refreshToken");
  },

  getCurrentUser: async (): Promise<User> => {
    const { data } = await api.get("/users/me/");
    return data;
  },

  getUsers: async (): Promise<User[]> => {
    const { data } = await api.get("/users/");
    return data;
  },

  updateUser: async (userId: number, userData: Partial<User>) => {
    const { data } = await api.patch(`/users/${userId}/`, userData);
    return data;
  },

  deleteUser: async (userId: number): Promise<void> => {
    await api.delete(`/users/${userId}/`);
  },

  changePassword: async (oldPassword: string, newPassword: string) => {
    const { data } = await api.post("/users/change_password/", {
      old_password: oldPassword,
      new_password: newPassword,
    });
    return data;
  },
};

export default api;
