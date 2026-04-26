# Multi-Service Docker Application To-Do List

## Project Setup

- [ ] Create the root project structure.
- [ ] Add a `README.md` with setup, build, run, and troubleshooting instructions.
- [ ] Add a `.gitignore` for Node.js, React, Docker, logs, local environment files, and build artifacts.
- [ ] Add example environment documentation, such as `.env.example`, without committing real secrets.

## Web Application

- [ ] Create a basic React frontend application.
- [ ] Add a page or component that can call the backend API.
- [ ] Configure the frontend to use the reverse proxy or API service URL.
- [ ] Add a `Dockerfile` for the web application.
- [ ] Create a custom base image for the web application.
- [ ] Implement a multi-stage build for the web application.
- [ ] Serve the optimized production frontend build with a lightweight web server.
- [ ] Optimize the frontend Docker image size and build cache usage.
- [ ] Add a health check for the web application container.

## API Service

- [ ] Create a Node.js Express backend API.
- [ ] Add basic routes, such as health, status, and data endpoints.
- [ ] Connect the API service to MongoDB.
- [ ] Connect the API service to Redis.
- [ ] Configure the API service to read sensitive values from Docker secrets.
- [ ] Add a `Dockerfile` for the API service.
- [ ] Create a custom base image for the API service.
- [ ] Optimize the API Docker image size and dependency installation.
- [ ] Add a health check for the API service container.

## Database

- [ ] Add a MongoDB service to Docker Compose.
- [ ] Configure MongoDB authentication.
- [ ] Store MongoDB credentials using Docker secrets.
- [ ] Add a Docker volume for persistent MongoDB data.
- [ ] Add a MongoDB health check.
- [ ] Configure MongoDB logging and log rotation.

## Cache

- [ ] Add a Redis service to Docker Compose.
- [ ] Configure Redis persistence if required.
- [ ] Add a Docker volume for persistent Redis data.
- [ ] Configure Redis authentication if required.
- [ ] Store Redis credentials using Docker secrets if authentication is enabled.
- [ ] Add a Redis health check.
- [ ] Configure Redis logging and log rotation.

## Reverse Proxy

- [ ] Add an Nginx reverse proxy service.
- [ ] Configure Nginx to route frontend requests.
- [ ] Configure Nginx to route API requests.
- [ ] Add an Nginx configuration file.
- [ ] Add a health check for the Nginx service.
- [ ] Configure Nginx logging and log rotation.

## Docker Compose

- [ ] Create a `docker-compose.yml` file.
- [ ] Define services for web, API, MongoDB, Redis, and Nginx.
- [ ] Define a custom Docker network for service communication.
- [ ] Configure service dependencies with health check conditions where appropriate.
- [ ] Configure Docker volumes for MongoDB and Redis persistence.
- [ ] Configure Docker secrets for sensitive values.
- [ ] Configure restart policies for all services.
- [ ] Configure logging and log rotation for all services.
- [ ] Expose only the ports required for external access.

## Docker Best Practices

- [ ] Use `.dockerignore` files for the web and API services.
- [ ] Pin base image versions where practical.
- [ ] Use small production images, such as Alpine or slim variants where appropriate.
- [ ] Install only production dependencies in final images.
- [ ] Run application containers as non-root users where practical.
- [ ] Keep Docker layers cache-friendly by copying dependency manifests before source files.
- [ ] Avoid committing real credentials, generated secrets, or local data volumes.
- [ ] Verify image sizes after builds and remove unnecessary files from final images.

## Validation

- [ ] Build all custom images successfully.
- [ ] Start the full stack with Docker Compose.
- [ ] Confirm the frontend is reachable through Nginx.
- [ ] Confirm the API is reachable through Nginx.
- [ ] Confirm the API can read and write data in MongoDB.
- [ ] Confirm the API can use Redis cache.
- [ ] Confirm all health checks report healthy.
- [ ] Confirm persistent data survives container restarts.
- [ ] Confirm logs are generated and log rotation is active.
- [ ] Confirm secrets are mounted securely and are not exposed in logs or source files.

