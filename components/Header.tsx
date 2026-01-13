'use client';

import Link from 'next/link';
import { useState, useEffect } from 'react';

const Header = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [userName, setUserName] = useState('');

  // Check if user is logged in (this would typically check for auth tokens)
  useEffect(() => {
    // In a real implementation, this would check for auth tokens in cookies/localStorage
    const token = localStorage.getItem('auth-token');
    if (token) {
      setIsLoggedIn(true);
      // In a real app, you might fetch user details here
      setUserName(localStorage.getItem('user-name') || '');
    }
  }, []);

  const handleLogout = () => {
    // In a real implementation, this would clear auth tokens
    localStorage.removeItem('auth-token');
    localStorage.removeItem('user-name');
    setIsLoggedIn(false);
    window.location.href = '/login';
  };

  return (
    <header className="bg-blue-600 text-white p-4">
      <div className="container mx-auto flex justify-between items-center">
        <div className="flex items-center space-x-2">
          <Link href="/" className="text-xl font-bold">Todo App</Link>
        </div>
        
        <nav>
          <ul className="flex space-x-6">
            {isLoggedIn ? (
              <>
                <li className="inline">Welcome, {userName || 'User'}!</li>
                <li className="inline">
                  <button 
                    onClick={handleLogout}
                    className="bg-red-500 hover:bg-red-700 text-white py-1 px-3 rounded"
                  >
                    Logout
                  </button>
                </li>
              </>
            ) : (
              <>
                <li className="inline">
                  <Link href="/login" className="hover:underline">Login</Link>
                </li>
                <li className="inline">
                  <Link href="/signup" className="hover:underline">Sign Up</Link>
                </li>
              </>
            )}
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;