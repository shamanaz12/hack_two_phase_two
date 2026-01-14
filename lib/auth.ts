import { createAuthClient } from "better-auth/react";

// Initialize Better Auth client
export const authClient = createAuthClient({
  baseURL: process.env.NEXT_PUBLIC_BETTER_AUTH_URL || "http://localhost:3000",
  fetchOptions: {
    cache: "no-store",
  },
});

// Export signIn and signOut functions to be used in the app
export const signIn = authClient.signIn;
export const signOut = authClient.signOut;

// Function to get the current user's session
export const getCurrentUser = async () => {
  try {
    const response = await fetch(`${process.env.NEXT_PUBLIC_BETTER_AUTH_URL || "http://localhost:3000"}/api/auth/session`, {
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
      },
    });
    
    if (!response.ok) {
      return null;
    }
    
    const data = await response.json();
    return data.session ? data.session.user : null;
  } catch (error) {
    console.error("Error getting current user:", error);
    return null;
  }
};

// Function to get the JWT token from Better Auth
export const getJwtToken = async (): Promise<string | null> => {
  try {
    // In a real Better Auth implementation, you would get the JWT token
    // For now, we'll look for it in localStorage where it might be stored
    if (typeof window !== 'undefined') {
      const token = localStorage.getItem('better-auth-session');
      return token;
    }
    return null;
  } catch (error) {
    console.error("Error getting JWT token:", error);
    return null;
  }
};