# DNS Server Project

## Overview
This project implements a DNS server using Python for the backend and JavaScript for the frontend. The backend is built with FastAPI and handles DNS record management, while the frontend provides a user interface for interacting with the DNS server.

## Project Structure
```
dns-server-project
├── backend                # Backend application
│   ├── app                # Application package
│   │   ├── api            # API package
│   │   ├── core           # Core functionalities
│   │   ├── models         # Data models
│   │   └── services       # Business logic services
│   ├── main.py            # Entry point for the backend
│   ├── requirements.txt    # Backend dependencies
│   └── tests              # Test suite
├── frontend               # Frontend application
│   ├── public             # Public assets
│   ├── src                # Source files
│   ├── .gitignore         # Git ignore for frontend
│   ├── package.json       # Frontend dependencies and scripts
│   └── vite.config.js     # Vite configuration
├── .gitignore             # Git ignore for the entire project
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile.backend      # Dockerfile for backend
└── Dockerfile.frontend     # Dockerfile for frontend
```

## Backend
- **main.py**: The entry point for the backend application, starting the DNS server and FastAPI application.
- **app**: Contains the core application logic, including API routes, models, and services for managing DNS records and zones.
- **requirements.txt**: Lists the dependencies required for the backend application.

## Frontend
- **public**: Contains static assets like the favicon and main HTML file.
- **src**: Contains the React components and services for the frontend application.
- **package.json**: Manages frontend dependencies and scripts for building and running the application.

## Getting Started
1. Clone the repository:
   ```
   git clone <repository-url>
   cd dns-server-project
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```

3. Run the backend:
   ```
   python main.py
   ```

4. Set up the frontend:
   - Navigate to the `frontend` directory.
   - Install dependencies:
     ```
     npm install
     ```

5. Run the frontend:
   ```
   npm run dev
   ```

## Docker
To run the project using Docker, use the provided `docker-compose.yml` file:
```
docker-compose up
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.