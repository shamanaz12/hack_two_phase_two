'use client';

import { useState, useEffect } from 'react';
import TaskItem from './TaskItem';
import { Task } from '../types';
import ErrorDisplay from './ErrorDisplay';
import LoadingSpinner from './LoadingSpinner';

interface TaskListProps {
  userId: string;
}

const TaskList = ({ userId }: TaskListProps) => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Fetch tasks for the user
  useEffect(() => {
    const fetchTasks = async () => {
      try {
        // In a real implementation, this would call the API to get tasks
        // For demo purposes, we'll simulate the data
        await new Promise(resolve => setTimeout(resolve, 500));

        // Mock tasks data
        const mockTasks: Task[] = [
          {
            id: '1',
            title: 'Sample Task 1',
            description: 'This is a sample task description',
            completed: false,
            userId: userId,
            createdAt: new Date(),
            updatedAt: new Date()
          },
          {
            id: '2',
            title: 'Completed Task',
            description: 'This task is already completed',
            completed: true,
            userId: userId,
            createdAt: new Date(),
            updatedAt: new Date()
          },
          {
            id: '3',
            title: 'Another Sample Task',
            description: 'This is another sample task',
            completed: false,
            userId: userId,
            createdAt: new Date(),
            updatedAt: new Date()
          }
        ];

        setTasks(mockTasks);
      } catch (err: any) {
        setError(err.message || 'Failed to load tasks');
      } finally {
        setLoading(false);
      }
    };

    if (userId) {
      fetchTasks();
    }
  }, [userId]);

  const handleToggleTask = async (task: Task) => {
    try {
      // In a real implementation, this would call the API to toggle task completion
      // For demo purposes, we'll update the local state
      await new Promise(resolve => setTimeout(resolve, 300));

      const updatedTasks = tasks.map(t =>
        t.id === task.id ? { ...t, completed: !t.completed, updatedAt: new Date() } : t
      );

      setTasks(updatedTasks);
    } catch (err: any) {
      setError(err.message || 'Failed to update task');
    }
  };

  const handleDeleteTask = async (taskId: string) => {
    if (!window.confirm('Are you sure you want to delete this task?')) {
      return;
    }

    try {
      // In a real implementation, this would call the API to delete the task
      // For demo purposes, we'll update the local state
      await new Promise(resolve => setTimeout(resolve, 300));

      const updatedTasks = tasks.filter(t => t.id !== taskId);
      setTasks(updatedTasks);
    } catch (err: any) {
      setError(err.message || 'Failed to delete task');
    }
  };

  if (loading) {
    return <LoadingSpinner message="Loading your tasks..." />;
  }

  if (error) {
    return (
      <ErrorDisplay
        error={error}
        onRetry={() => {
          setError('');
          // Re-fetch tasks when retry is clicked
          const fetchTasks = async () => {
            try {
              setLoading(true);
              // Mock API call
              await new Promise(resolve => setTimeout(resolve, 500));

              const mockTasks: Task[] = [
                {
                  id: '1',
                  title: 'Sample Task 1',
                  description: 'This is a sample task description',
                  completed: false,
                  userId: userId,
                  createdAt: new Date(),
                  updatedAt: new Date()
                },
                {
                  id: '2',
                  title: 'Completed Task',
                  description: 'This task is already completed',
                  completed: true,
                  userId: userId,
                  createdAt: new Date(),
                  updatedAt: new Date()
                },
                {
                  id: '3',
                  title: 'Another Sample Task',
                  description: 'This is another sample task',
                  completed: false,
                  userId: userId,
                  createdAt: new Date(),
                  updatedAt: new Date()
                }
              ];

              setTasks(mockTasks);
            } catch (err: any) {
              setError(err.message || 'Failed to load tasks');
            } finally {
              setLoading(false);
            }
          };
          fetchTasks();
        }}
      />
    );
  }

  const handleUpdateTask = async (taskId: string, updatedTask: Partial<Task>) => {
    try {
      // In a real implementation, this would call the API to update the task
      // For demo purposes, we'll update the local state
      await new Promise(resolve => setTimeout(resolve, 300));

      const updatedTasks = tasks.map(task =>
        task.id === taskId
          ? { ...task, ...updatedTask, updatedAt: new Date() }
          : task
      );

      setTasks(updatedTasks);
    } catch (err: any) {
      setError(err.message || 'Failed to update task');
    }
  };

  return (
    <div>
      <h2 className="text-xl font-semibold mb-4">Your Tasks</h2>
      {tasks.length === 0 ? (
        <div className="text-center py-8">
          <p className="text-gray-500">No tasks yet. Create your first task!</p>
        </div>
      ) : (
        <div>
          {tasks.map((task) => (
            <TaskItem
              key={task.id}
              task={task}
              onToggle={handleToggleTask}
              onDelete={handleDeleteTask}
              onUpdate={handleUpdateTask}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default TaskList;