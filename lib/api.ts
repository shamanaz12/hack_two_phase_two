import { Task } from "../types";

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

// Helper function to get auth token from wherever it's stored
const getAuthToken = (): string | null => {
  // Retrieve the token from localStorage where Better Auth stores it
  if (typeof window !== 'undefined') {
    // Better Auth typically stores the token in localStorage with a specific key
    return localStorage.getItem('better-auth-session') || localStorage.getItem('auth-token');
  }
  return null;
};

// Helper function to set auth token
const setAuthToken = (token: string): void => {
  if (typeof window !== 'undefined') {
    localStorage.setItem('better-auth-session', token);
  }
};

// Generic request function with error handling
const request = async (endpoint: string, options: RequestInit = {}) => {
  const url = `${API_BASE_URL}${endpoint}`;
  const headers = {
    "Content-Type": "application/json",
    ...(getAuthToken() ? { Authorization: `Bearer ${getAuthToken()}` } : {}),
    ...options.headers,
  };

  try {
    const response = await fetch(url, {
      ...options,
      headers,
    });

    if (!response.ok) {
      // Handle unauthorized access
      if (response.status === 401) {
        // Clear the invalid token
        if (typeof window !== 'undefined') {
          localStorage.removeItem('better-auth-session');
          localStorage.removeItem('auth-token');
        }
        throw new Error('Unauthorized: Invalid or expired token');
      }
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    // Handle responses that might not have JSON content
    const contentType = response.headers.get("content-type");
    if (contentType && contentType.includes("application/json")) {
      return await response.json();
    } else {
      // For responses like DELETE that return empty body
      return {};
    }
  } catch (error) {
    console.error(`API request failed: ${url}`, error);
    throw error;
  }
};

// User API functions
export const userAPI = {
  // Login function to get and store the JWT token
  login: async (email: string, password: string): Promise<any> => {
    const response = await fetch(`${API_BASE_URL}/auth/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) {
      throw new Error(`Login failed: ${response.status}`);
    }

    const data = await response.json();

    // Store the token for future requests
    if (data.access_token) {
      setAuthToken(data.access_token);
    }

    return data;
  },

  // Registration function
  register: async (email: string, username: string, password: string): Promise<any> => {
    const response = await fetch(`${API_BASE_URL}/auth/register`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, username, password }),
    });

    if (!response.ok) {
      throw new Error(`Registration failed: ${response.status}`);
    }

    const data = await response.json();

    // Store the token for future requests
    if (data.access_token) {
      setAuthToken(data.access_token);
    }

    return data;
  },
};

// Task API functions
export const taskAPI = {
  // GET /api/{user_id}/tasks
  getTasks: async (userId: string): Promise<Task[]> => {
    return request(`/api/${userId}/tasks`);
  },

  // POST /api/{user_id}/tasks
  createTask: async (userId: string, taskData: Omit<Task, 'id' | 'userId' | 'createdAt' | 'updatedAt'>): Promise<Task> => {
    return request(`/api/${userId}/tasks`, {
      method: "POST",
      body: JSON.stringify(taskData),
    });
  },

  // GET /api/{user_id}/tasks/{id}
  getTaskById: async (userId: string, taskId: string): Promise<Task> => {
    return request(`/api/${userId}/tasks/${taskId}`);
  },

  // PUT /api/{user_id}/tasks/{id}
  updateTask: async (userId: string, taskId: string, taskData: Partial<Task>): Promise<Task> => {
    return request(`/api/${userId}/tasks/${taskId}`, {
      method: "PUT",
      body: JSON.stringify(taskData),
    });
  },

  // DELETE /api/{user_id}/tasks/{id}
  deleteTask: async (userId: string, taskId: string): Promise<void> => {
    await request(`/api/${userId}/tasks/${taskId}`, {
      method: "DELETE",
    });
  },

  // PATCH /api/{user_id}/tasks/{id}/complete
  toggleTaskCompletion: async (userId: string, taskId: string): Promise<Task> => {
    return request(`/api/${userId}/tasks/${taskId}/complete`, {
      method: "PATCH",
    });
  },
};