'use client';

import { useState } from 'react';
import { Task } from '../types';
import ErrorDisplay from './ErrorDisplay';

interface TaskFormProps {
  userId: string;
  onCreateTask: (task: Task) => void;
}

const TaskForm = ({ userId, onCreateTask }: TaskFormProps) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!title.trim()) {
      setError('Title is required');
      return;
    }

    try {
      // In a real implementation, this would call the API to create a task
      // For demo purposes, we'll simulate the creation
      await new Promise(resolve => setTimeout(resolve, 500));

      const newTask: Task = {
        id: Date.now().toString(), // In a real app, this would come from the backend
        title: title.trim(),
        description: description.trim(),
        completed: false,
        userId,
        createdAt: new Date(),
        updatedAt: new Date()
      };

      // Reset form
      setTitle('');
      setDescription('');
      setError('');

      // Notify parent component
      onCreateTask(newTask);
    } catch (err: any) {
      setError(err.message || 'Failed to create task');
    }
  };

  return (
    <div className="mb-8">
      <h2 className="text-xl font-semibold mb-4">Create New Task</h2>
      {error && (
        <ErrorDisplay error={error} onRetry={() => setError('')} />
      )}
      <form onSubmit={handleSubmit} className="bg-white shadow rounded-lg p-6">
        <div className="mb-4">
          <label htmlFor="title" className="block text-sm font-medium text-gray-700 mb-1">
            Title *
          </label>
          <input
            type="text"
            id="title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            placeholder="Enter task title"
            required
          />
        </div>
        <div className="mb-4">
          <label htmlFor="description" className="block text-sm font-medium text-gray-700 mb-1">
            Description
          </label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            rows={3}
            className="w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
            placeholder="Enter task description (optional)"
          ></textarea>
        </div>
        <div className="flex justify-end">
          <button
            type="submit"
            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
          >
            Create Task
          </button>
        </div>
      </form>
    </div>
  );
};

export default TaskForm;