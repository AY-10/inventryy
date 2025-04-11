import axios from "axios";
import { LoginData, RegisterData, User } from "../types/auth";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000/api";

// Create axios instance with default config
const api = axios.create({
  baseURL: API_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

// Add token to requests if it exists
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
    if (error.response?.status === 401 && !originalRequest._retry) {
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
  setAuthToken: (token: string) => {
    api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  },

  login: async (username: string, password: string) => {
    const response = await api.post("/token/", { username, password });
    return response.data;
  },

  register: async (data: RegisterData) => {
    const response = await api.post("/users/", data);
    return response.data;
  },

  logout: async () => {
    const refreshToken = localStorage.getItem("refreshToken");
    if (refreshToken) {
      await api.post("/token/blacklist/", { refresh: refreshToken });
    }
  },

  getCurrentUser: async () => {
    const response = await api.get("/users/me/");
    return response.data;
  },

  getUsers: async () => {
    const response = await api.get("/users/");
    return response.data;
  },

  updateUser: async (userId: number, data: Partial<User>) => {
    const response = await api.patch(`/users/${userId}/`, data);
    return response.data;
  },

  deleteUser: async (userId: number): Promise<void> => {
    await api.delete(`/users/${userId}/`);
  },
};

export const userAPI = {
  getUsers: async () => {
    const response = await api.get("/users/");
    return response.data;
  },

  getUser: async (id: number) => {
    const response = await api.get(`/users/${id}/`);
    return response.data;
  },

  updateUser: async (id: number, data: Partial<User>) => {
    const response = await api.patch(`/users/${id}/`, data);
    return response.data;
  },

  deleteUser: async (id: number): Promise<void> => {
    await api.delete(`/users/${id}/`);
  },
};

export const storeAPI = {
  getStores: async () => {
    const response = await api.get("/stores/");
    return response.data;
  },

  getStore: async (id: number) => {
    const response = await api.get(`/stores/${id}/`);
    return response.data;
  },

  createStore: async (data: any) => {
    const response = await api.post("/stores/", data);
    return response.data;
  },

  updateStore: async (id: number, data: any) => {
    const response = await api.patch(`/stores/${id}/`, data);
    return response.data;
  },

  deleteStore: async (id: number) => {
    await api.delete(`/stores/${id}/`);
  },
};

export const inventoryAPI = {
  getItems: async () => {
    const response = await api.get("/inventory/");
    return response.data;
  },

  getItem: async (id: number) => {
    const response = await api.get(`/inventory/${id}/`);
    return response.data;
  },

  createItem: async (data: any) => {
    const response = await api.post("/inventory/", data);
    return response.data;
  },

  updateItem: async (id: number, data: any) => {
    const response = await api.patch(`/inventory/${id}/`, data);
    return response.data;
  },

  deleteItem: async (id: number) => {
    await api.delete(`/inventory/${id}/`);
  },
};

export const salesAPI = {
  getSales: async () => {
    const response = await api.get("/sales/");
    return response.data;
  },

  getSale: async (id: number) => {
    const response = await api.get(`/sales/${id}/`);
    return response.data;
  },

  createSale: async (data: any) => {
    const response = await api.post("/sales/", data);
    return response.data;
  },

  updateSale: async (id: number, data: any) => {
    const response = await api.patch(`/sales/${id}/`, data);
    return response.data;
  },

  deleteSale: async (id: number) => {
    await api.delete(`/sales/${id}/`);
  },
};

export default api;
