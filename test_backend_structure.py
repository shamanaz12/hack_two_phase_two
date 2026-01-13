#!/usr/bin/env python3
"""
Test script to verify the backend application structure
"""

import sys
import os
import subprocess

def test_imports():
    """Test that all modules can be imported without errors"""
    print("Testing module imports...")
    
    # Add the backend directory to the Python path
    backend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend')
    sys.path.insert(0, os.path.dirname(backend_dir))
    
    try:
        # Test importing the main app
        from backend.main import app
        print("✓ Main app imported successfully")
        
        # Test importing other modules
        from backend import database
        print("✓ Database module imported successfully")
        
        from backend import models
        print("✓ Models module imported successfully")
        
        from backend import dependencies
        print("✓ Dependencies module imported successfully")
        
        from backend.routes import tasks, updates
        print("✓ Routes modules imported successfully")
        
        from backend.services import update_service
        print("✓ Services module imported successfully")
        
        from backend import lifespan
        print("✓ Lifespan module imported successfully")
        
        from backend import exception_handlers
        print("✓ Exception handlers module imported successfully")
        
        print("\n✓ All modules imported successfully!")
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def test_environment():
    """Test that environment setup is correct"""
    print("\nTesting environment setup...")
    
    # Check if .env file exists
    env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend', '.env')
    if os.path.exists(env_file):
        print("✓ .env file exists")
    else:
        print("✗ .env file does not exist")
        return False
    
    # Check if .env is in .gitignore
    gitignore_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.gitignore')
    if os.path.exists(gitignore_file):
        with open(gitignore_file, 'r') as f:
            gitignore_content = f.read()
            if '.env' in gitignore_content:
                print("✓ .env is in .gitignore")
            else:
                print("✗ .env is not in .gitignore")
                return False
    else:
        print("✗ .gitignore file does not exist")
        return False
    
    print("✓ Environment setup is correct!")
    return True

def main():
    print("Running backend application verification tests...\n")
    
    import_success = test_imports()
    env_success = test_environment()
    
    if import_success and env_success:
        print("\n🎉 All tests passed! The backend application structure is correct.")
        print("\nTo start the server, run:")
        print("cd backend && uvicorn main:app --reload --port 8000")
        return True
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)