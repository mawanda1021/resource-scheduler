project:
  name: "📊 Resource Scheduler (Bank Teller/Call Center)"
  course: "CSC 2101 - Operating Systems | Task 2"
  description: |
    This project is a **Resource Scheduler** that dynamically assigns **bank tellers/call center agents** 
    to customer requests based on different scheduling algorithms.
    The goal is to **minimize wait time**, **maximize resource utilization**, and **ensure fairness**.

objectives:
  - "✅ Minimize **customer waiting times**."
  - "✅ Balance **workload among agents** efficiently."
  - "✅ Provide **real-time status tracking** of customer queue and agent availability."
  - "✅ Ensure **fairness in task assignment**."

scope:
  - "🔹 Simulates real-world **bank/call center** environments."
  - "🔹 Implements **Round Robin, Priority Scheduling, and Shortest Job Next**."
  - "🔹 Provides **real-time monitoring** of agent workload and queue status."
  - "🔹 Includes **web-based dashboard** for tracking and control."
  - "🔹 Supports **containerized deployment** using **Docker**."
  - "🔹 Uses **GitHub Actions** for **CI/CD automation**."
  - "🔹 Deployed on **Render** for scalability."

system_overview:
  backend: "Flask API to handle scheduling, task assignments, and queue management."
  frontend: "React.js Dashboard for real-time monitoring of agents and customers."
  database: "PostgreSQL (or SQLite for local testing)."

functional_requirements:
  - id: "FR-01"
    description: "System shall allow customers to enter a queue with **random service time & priority**."
  - id: "FR-02"
    description: "System shall assign customers to available agents **dynamically**."
  - id: "FR-03"
    description: "System shall implement **Round Robin, Priority Scheduling, and Shortest Job Next**."
  - id: "FR-04"
    description: "System shall update **agent and customer queue status** every 5 seconds."
  - id: "FR-05"
    description: "Frontend shall display a **real-time dashboard** of queue & agent workloads."
  - id: "FR-06"
    description: "System shall support **containerized deployment (Docker)**."
  - id: "FR-07"
    description: "System shall be deployed on **Render using GitHub Actions**."

non_functional_requirements:
  - id: "NFR-01"
    description: "The system shall be available **99.9% of the time**."
  - id: "NFR-02"
    description: "The backend shall respond to requests within **<1 second**."
  - id: "NFR-03"
    description: "The system shall support **at least 100 concurrent customer requests**."
  - id: "NFR-04"
    description: "The frontend shall be **mobile responsive**."

system_architecture:
  components:
    - "Frontend (React.js): Real-time monitoring & control"
    - "Backend (Flask API): Scheduling logic & task management"
    - "Database (PostgreSQL/SQLite): Stores customer & agent data"
  deployment_model:
    - backend: "Render Web Service"
    - frontend: "Render Static Site"
    - database: "PostgreSQL (Optional)"

scheduling_algorithms:
  round_robin: "Each agent gets assigned a task in a rotating order."
  priority_scheduling: "VIP/Corporate customers are served first."
  shortest_job_next: "Tasks with shorter service times are prioritized."

api_endpoints:
  - method: "POST"
    endpoint: "/add_customer"
    description: "Adds a customer to the queue."
  - method: "POST"
    endpoint: "/start_scheduling"
    description: "Starts a scheduling algorithm."
  - method: "GET"
    endpoint: "/agents"
    description: "Retrieves agent workload status."
  - method: "GET"
    endpoint: "/queue"
    description: "Retrieves current customer queue."

deployment_plan:
  steps:
    - "✅ Push code to GitHub."
    - "✅ Connect GitHub repo to Render."
    - "✅ Deploy backend using **Gunicorn & Flask**."
    - "✅ Deploy frontend as a **React static site**."
    - "✅ Monitor deployment logs for any errors."

ci_cd_pipeline:
  - "✅ Runs **tests automatically**."
  - "✅ Builds & pushes **Docker images** to Docker Hub."
  - "✅ Deploys **backend & frontend** to Render."

risks_and_mitigations:
  - risk: "System crashes under heavy load."
    mitigation: "Implement **load balancing**."
  - risk: "Long customer wait times."
    mitigation: "Optimize **scheduling algorithms**."
  - risk: "Deployment issues on Render."
    mitigation: "Debug logs & use **GitHub Actions automation**."

future_improvements:
  - "🔹 Add **AI-based scheduling** for better optimization."
  - "🔹 Store **historical data analytics** for performance tracking."
  - "🔹 Implement **role-based authentication** for security."

references:
  - "📚 Operating Systems Concepts – Silberschatz, Galvin"
  - "📚 Render Documentation – [https://render.com/docs](https://render.com/docs)"
  - "📚 Flask Documentation – [https://flask.palletsprojects.com](https://flask.palletsprojects.com)"

conclusion: |
  This **Resource Scheduler** optimizes **bank/call center operations** by efficiently assigning tasks to agents.
  With **real-time monitoring**, **multiple scheduling algorithms**, and **automated deployment**, 
  it ensures a **seamless customer service experience**.

  🚀 **Ready for deployment on Render!**
