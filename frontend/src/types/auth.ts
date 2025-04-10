export interface User {
  id: number;
  username: string;
  email: string;
  role: "SUPER_ADMIN" | "ADMIN";
  first_name: string;
  last_name: string;
  created_at: string;
  updated_at: string;
}

export interface LoginCredentials {
  username: string;
  password: string;
}

export interface RegisterData {
  username: string;
  email: string;
  password: string;
  password2: string;
  role: "SUPER_ADMIN" | "ADMIN";
  first_name: string;
  last_name: string;
}

export interface AuthState {
  user: User | null;
  token: string | null;
  refreshToken: string | null;
  isAuthenticated: boolean;
  loading: boolean;
  error: string | null;
}
