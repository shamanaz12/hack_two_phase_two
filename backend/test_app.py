from fastapi import FastAPI

app = FastAPI(
    title="Todo App with Update Management API",
    description="API for managing todos with update capabilities",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo App with Update Management API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

print("Application loaded successfully")