'use client';

import { useState, useEffect } from 'react';
import { Task } from '../types';
import Header from '../components/Header';
import TaskList from '../components/TaskList';
import TaskForm from '../components/TaskForm';

const DashboardPage = () => {
  const [userId, setUserId] = useState<string | null>(null);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  // Check if user is logged in
  useEffect(() => {
    // In a real implementation, this would check for auth tokens
    const token = localStorage.getItem('auth-token');
    if (token) {
      setIsLoggedIn(true);
      // In a real app, you might fetch user details here
      setUserId(localStorage.getItem('user-id') || 'demo-user');
    } else {
      // Redirect to login if not authenticated
      window.location.href = '/login';
    }
  }, []);

  const handleCreateTask = (task: Task) => {
    // In a real implementation, this would update the task list from the API
    // For demo purposes, we'll just show an alert
    alert(`Task "${task.title}" created successfully!`);
  };

  if (!isLoggedIn) {
    return null; // Redirect happens in useEffect
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      <main className="container mx-auto py-6 px-4 sm:px-6 lg:px-8">
        <div className="lg:flex lg:items-center lg:justify-between mb-8">
          <div className="min-w-0 flex-1">
            <h1 className="text-2xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">
              Task Dashboard
            </h1>
            <p className="mt-2 text-sm text-gray-500">
              Manage your tasks efficiently
            </p>
          </div>
        </div>

        <div className="mt-8">
          {userId ? (
            <>
              <TaskForm userId={userId} onCreateTask={handleCreateTask} />
              <TaskList userId={userId} />
            </>
          ) : (
            <div className="text-center py-8">
              <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500 mx-auto"></div>
              <p className="mt-4 text-gray-500">Loading your tasks...</p>
            </div>
          )}
        </div>
      </main>
    </div>
  );
};

export default DashboardPage;