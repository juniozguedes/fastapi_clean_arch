import uvicorn
from src.main.server.server import app
from src.main.routes.router import generate_routes


if __name__ == "__main__":
    generate_routes(app)
    uvicorn.run(app, host="0.0.0.0", port=8000)
