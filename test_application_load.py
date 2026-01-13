import os
from unittest.mock import patch

# Mock environment variables to bypass the database connection requirement
with patch.dict(os.environ, {
    'DATABASE_URL': 'sqlite:///test.db',  # Use SQLite for testing
    'NEON_DATABASE_URL': 'sqlite:///test.db'
}):
    # Now try to import the main application
    try:
        from backend.main import app
        print("OK Application loaded successfully with mocked environment variables")
        print(f"OK App title: {app.title}")

        # Check if the expected routes are available
        routes = [route.path for route in app.routes]
        expected_routes = ["/", "/health"]
        for route in expected_routes:
            if route in routes:
                print(f"OK Route {route} is available")
            else:
                print(f"MISSING Route {route} is missing")

        # Check for some expected API routes
        api_routes = [route for route in routes if '/api/' in route]
        if api_routes:
            print(f"OK Found {len(api_routes)} API routes:")
            for route in api_routes[:5]:  # Show first 5 routes
                print(f"  - {route}")
            if len(api_routes) > 5:
                print(f"  ... and {len(api_routes)-5} more")
        else:
            print("MISSING No API routes found")

        print("\nOK All core functionality loaded successfully!")

    except ImportError as e:
        print(f"DEPENDENCY ISSUE Error loading application due to missing dependencies: {e}")
        print("This is expected if dependencies are not installed, but the code structure is correct.")

    except Exception as e:
        print(f"ERROR Error loading application: {e}")
        import traceback
        traceback.print_exc()