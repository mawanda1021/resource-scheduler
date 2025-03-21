
# resource-scheduler
project:
  name: "📊 Resource Scheduler (Bank Teller/Call Center)"
  course: "CSC 2101 - Operating Systems | Task 2"
  description: |
    This project is a **Resource Scheduler** that dynamically assigns **bank tellers/call center agents** 
    to customer requests based on different scheduling algorithms.
    The goal is to **minimize wait time**, **maximize resource utilization**, and **ensure fairness**.


---
# 📊 Resource Scheduler (Bank Teller/Call Center)

project:
  course: "CSC 2101 - Operating Systems | Task 2"
  description: |
    This project is a **Resource Scheduler** that dynamically assigns **bank tellers/call center agents** to customer requests based on different scheduling algorithms.
    The goal is to **minimize wait time**, **maximize resource utilization**, and **ensure fairness**.

# 🧩 Features

  - "✅ Simulates customer arrivals with **random priority & service time**"
  - "✅ Assigns agents dynamically based on **Round Robin, Priority, or Shortest Job Next** scheduling"
  - "✅ **Real-time monitoring** of agent workload & customer queue"
  - "✅ **Web-based dashboard (React.js)** for visualizing agent status"
  - "✅ **Containerized with Docker & deployed via GitHub Actions**"

  - "✅ **Automated deployment using Render**"



# 🛠 Tech Stack

tech_stack:
  backend:
    - "Python (Flask)"
    - "Flask-SocketIO"
  frontend:
    - "React.js"
  database:
    - "PostgreSQL (or SQLite for testing)"
  deployment:
    - "Docker"
    - "GitHub Actions"

    - "Render (instead of AWS/Heroku)"


installation:
=======
    - "AWS/Heroku"

# 📂 Project Structure
project_structure: |
  resource-scheduler/
  ├── backend/               # Backend (Flask API)
  │   ├── main.py            # Main Flask server
  │   ├── scheduler.py       # Scheduling algorithms
  │   ├── models.py          # Agent & Customer classes
  │   ├── requirements.txt   # Dependencies
  ├── frontend/              # Frontend (React.js)
  │   ├── src/
  │   │   ├── components/    # React Components
  │   │   ├── services/      # API Calls & WebSocket Connection
  ├── docker-compose.yml     # Docker for multi-container setup
  ├── Dockerfile             # Backend containerization
  ├── .github/workflows/     # GitHub Actions CI/CD
  ├── README.md              # Documentation
  ├── SRS_Document.md        # Software Requirements Specification

# 🚀 Installation & Setup
installation_setup:

  steps:
    - description: "🔹 **Clone the Repository**"
      command: |
        git clone https://github.com/mawanda1021/resource-scheduler.git
        cd resource-scheduler

    - description: "🔹 **Set Up Backend**"
<<<<<<< HEAD
      options:
        python:
          command: |
            cd backend
            pip install -r requirements.txt
            python main.py
        docker:
          command: |
            docker build -t resource-scheduler .
            docker run -p 5000:5000 resource-scheduler

      using_python:
        command: |
          cd backend
          pip install -r requirements.txt
          python main.py
      using_docker:
        command: |
          docker build -t resource-scheduler .
          docker run -p 5000:5000 resource-scheduler

    - description: "🔹 **Set Up Frontend**"
      command: |
        cd frontend
        npm install
        npm start
      note: "The frontend will run at http://localhost:3000"

# 📌 API Endpoints

api_endpoints:
  - method: "POST"
    endpoint: "/add_customer"
    description: "Add a customer to the queue"
  - method: "POST"
    endpoint: "/start_scheduling"
    description: "Start a scheduling algorithm"
  - method: "GET"
    endpoint: "/agents"
    description: "Get agent status"
  - method: "GET"
    endpoint: "/queue"
    description: "Get customer queue"


docker:
  compose_command: "docker-compose up --build"

ci_cd_pipeline:
  description: |
    This project uses **GitHub Actions** to:
    ✅ **Run tests automatically**
    ✅ **Build and push Docker images to Docker Hub**
    ✅ **Deploy automatically to Render**

deployment:
  backend_url: "🔗 **Backend API**: [Render Backend URL](#) (Replace with actual URL)"
  frontend_url: "🔗 **Frontend**: [Render Frontend URL](#) (Replace with actual URL)"


# 📦 Docker Compose
docker_compose:
  command: |
    docker-compose up --build

# ⚡️ CI/CD Pipeline (GitHub Actions)
ci_cd_pipeline:
  description: |
    This project uses GitHub Actions to:
    - Run tests automatically
    - Build and push Docker images to Docker Hub
    - Deploy to AWS or Heroku

# 🌍 Deployment
deployment:
  live_demo_link: "🔗 **Live Demo Link** (Replace with actual deployment link)"

# 👥 Contributors

contributors:
  - name: "MAWANDA ROBERT"
    github: "@mawanda1021"
  - name: "Team Member 2"
    github: "@teammember"
  - name: "Team Member 3"
    github: "@teammember"


future_improvements:
  - "🔹 Add **AI-based scheduling** for workload optimization"
  - "🔹 Store **historical data** for analysis"
  - "🔹 Implement **role-based authentication**"

license:
  type: "MIT License"
  description: "This project is licensed under the MIT License."

final_notes:
  - "📌 Ensure **the backend is running before starting the frontend**"
  - "📌 Use **Postman** to test API endpoints."
  - "📌 If you have any issues, please open an **[issue](https://github.com/mawanda1021/resource-scheduler/issues)** on GitHub. 🚀"

# 📌 Future Improvements
future_improvements:
  - "Add AI-based scheduling for workload optimization"
  - "Store historical data for analysis"
  - "Implement role-based authentication"

# 📝 License
license: "This project is licensed under the MIT License."

# 🔥 Final Notes
final_notes:
  - "📌 Make sure your backend is running before starting the frontend"
  - "📌 Use Postman to test API endpoints."

