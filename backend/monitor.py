import time

def monitor_agents(agents):
    while True:
        print("\nAgent Status:")
        for agent in agents:
            print(f"Agent {agent.agent_id}: {len(agent.tasks)} tasks assigned.")
        time.sleep(5)
