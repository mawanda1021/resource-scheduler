import time
import threading
from models import Customer, Agent

class Scheduler:
    def __init__(self, agents):
        self.agents = agents
        self.queue = []

    def add_customer(self, customer):
        self.queue.append(customer)

    def round_robin(self):
        while True:
            if self.queue:
                customer = self.queue.pop(0)
                for agent in self.agents:
                    if agent.assign_task(customer):
                        threading.Thread(target=self.process_task, args=(agent, customer)).start()
                        break
            time.sleep(2)

    def priority_scheduling(self):
        while True:
            if self.queue:
                self.queue.sort(key=lambda x: x.priority, reverse=True)  # Sort by priority (VIP first)
                customer = self.queue.pop(0)
                for agent in self.agents:
                    if agent.assign_task(customer):
                        threading.Thread(target=self.process_task, args=(agent, customer)).start()
                        break
            time.sleep(2)

    def shortest_job_next(self):
        while True:
            if self.queue:
                self.queue.sort(key=lambda x: x.service_time)  # Sort by shortest job first
                customer = self.queue.pop(0)
                for agent in self.agents:
                    if agent.assign_task(customer):
                        threading.Thread(target=self.process_task, args=(agent, customer)).start()
                        break
            time.sleep(2)

    def process_task(self, agent, customer):
        print(f"Agent {agent.agent_id} serving Customer {customer.customer_id} (Priority: {customer.priority})")
        time.sleep(customer.service_time)  # Simulate service time
        agent.release_task(customer)
        print(f"Customer {customer.customer_id} served by Agent {agent.agent_id}.")
