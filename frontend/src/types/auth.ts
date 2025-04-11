export interface User {
  id: number;
  username: string;
  email: string;
  role: "ADMIN" | "SUPER_ADMIN";
  first_name: string;
  last_name: string;
  is_active: boolean;
  date_joined: string;
  created_at: string;
}

export interface LoginData {
  username: string;
  password: string;
}

export interface RegisterData {
  username: string;
  email: string;
  password: string;
  confirmPassword: string;
  role: "ADMIN" | "SUPER_ADMIN";
}

export interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  loading: boolean;
  error: string | null;
}

export interface AuthContextType extends AuthState {
  login: (username: string, password: string) => Promise<User>;
  register: (data: RegisterData) => Promise<void>;
  logout: () => Promise<void>;
  clearError: () => void;
}
