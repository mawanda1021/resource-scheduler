from flask import Flask, request, jsonify
from flask_socketio import SocketIO
import threading
from models import Customer, Agent
from scheduler import Scheduler

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

agents = [Agent(i) for i in range(3)]
scheduler = Scheduler(agents)

@app.route('/')
def home():
    return jsonify({"message": "Resource Scheduler API is running on Render!"})

@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.json
    customer = Customer(data['customer_id'], data['priority'])
    scheduler.add_customer(customer)
    socketio.emit("customer_queue", [{"customer_id": c.customer_id, "priority": c.priority} for c in scheduler.queue])
    return jsonify({"message": "Customer added"}), 200

@app.route('/start_scheduling', methods=['POST'])
def start_scheduling():
    scheduling_type = request.json.get("type", "round_robin")

    def run_scheduler():
        while True:
            socketio.emit("agent_status", [{"id": a.agent_id, "tasks": a.tasks} for a in agents])
            socketio.emit("assignments", [{"agent_id": a.agent_id, "customer_id": t.customer_id} for a in agents for t in a.tasks])
            socketio.sleep(5)

    threading.Thread(target=run_scheduler, daemon=True).start()

    if scheduling_type == "priority":
        threading.Thread(target=scheduler.priority_scheduling, daemon=True).start()
    elif scheduling_type == "shortest_job_next":
        threading.Thread(target=scheduler.shortest_job_next, daemon=True).start()
    else:
        threading.Thread(target=scheduler.round_robin, daemon=True).start()

    return jsonify({"message": f"{scheduling_type} scheduling started"}), 200

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=10000)  # Render uses dynamic ports
