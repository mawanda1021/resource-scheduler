import random
import time
from threading import Lock

class Customer:
    def __init__(self, customer_id, priority):
        self.customer_id = customer_id
        self.priority = priority
        self.service_time = random.randint(2, 10)  # Random service time (2-10 sec)
        self.arrival_time = time.time()  # Timestamp of arrival

class Agent:
    def __init__(self, agent_id, workload_limit=3):
        self.agent_id = agent_id
        self.workload_limit = workload_limit
        self.tasks = []
        self.lock = Lock()  # Prevents race conditions in multi-threading
    
    def assign_task(self, customer):
        with self.lock:
            if len(self.tasks) < self.workload_limit:
                self.tasks.append(customer)
                return True
        return False
    
    def release_task(self, customer):
        with self.lock:
            self.tasks.remove(customer)

    def is_available(self):
        return len(self.tasks) < self.workload_limit
