from fastapi import FastAPI

app = FastAPI()

@app.get("/user")
def get_user():
    return {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "roles": ["admin", "editor", "viewer"],  # Array of items
        "profile": {  # Nested JSON
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "New York",
                "zip": "10001"
            }
        },
        "is_active": True  # Single item
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
