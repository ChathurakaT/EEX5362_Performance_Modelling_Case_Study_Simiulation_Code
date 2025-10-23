import random
import simpy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# ------------------------------
# 1️⃣  Simulation Configuration
# ------------------------------
RANDOM_SEED = 42
SIM_TIME = 8 * 60  # minutes (8 hours)
ARRIVAL_RATE = 3   # calls per minute (λ)
SERVICE_RATE = 2   # calls per minute per agent (μ)

random.seed(RANDOM_SEED)


# ------------------------------
# 2️⃣  Call Center Environment
# ------------------------------
class CallCenter:
    def __init__(self, env, num_agents, service_rate):
        self.env = env
        self.agents = simpy.Resource(env, num_agents)
        self.service_rate = service_rate
        self.wait_times = []
        self.queue_lengths = []
        self.busy_times = [0.0 for _ in range(num_agents)]

    def handle_call(self, agent_id):
        service_time = random.expovariate(self.service_rate)
        yield self.env.timeout(service_time)
        self.busy_times[agent_id] += service_time

    def call_process(self, caller_id):
        arrival_time = self.env.now
        with self.agents.request() as request:
            yield request
            wait = self.env.now - arrival_time
            self.wait_times.append(wait)
            self.queue_lengths.append(len(self.agents.queue))
            agent_id = random.randint(0, len(self.busy_times) - 1)
            yield self.env.process(self.handle_call(agent_id))


# ------------------------------
# 3️⃣  Arrival Generator
# ------------------------------
def arrival_generator(env, call_center, arrival_rate):
    caller_id = 0
    while True:
        yield env.timeout(random.expovariate(arrival_rate))
        caller_id += 1
        env.process(call_center.call_process(caller_id))


# ------------------------------
# 4️⃣  Run Simulation Function
# ------------------------------
def run_simulation(num_agents, service_rate):
    env = simpy.Environment()
    call_center = CallCenter(env, num_agents, service_rate)
    env.process(arrival_generator(env, call_center, ARRIVAL_RATE))
    env.run(until=SIM_TIME)

    avg_wait = np.mean(call_center.wait_times)
    avg_queue = np.mean(call_center.queue_lengths)
    util = sum(call_center.busy_times) / (len(call_center.busy_times) * SIM_TIME)
    throughput = len(call_center.wait_times) / (SIM_TIME / 60)

    return {
        "Agents": num_agents,
        "ServiceRate": service_rate,
        "AvgWait(s)": round(avg_wait * 60, 2),
        "AvgQueue": round(avg_queue, 2),
        "Utilization": round(util, 2),
        "Throughput(hr)": round(throughput, 2)
    }


# ------------------------------
# 5️⃣  Run Experiments
# ------------------------------
results = []
results.append(run_simulation(2, SERVICE_RATE))          # Scenario A
results.append(run_simulation(3, SERVICE_RATE))          # Scenario B
results.append(run_simulation(2, SERVICE_RATE * 1.3))    # Scenario C

df = pd.DataFrame(results)
scenarios = ['A: 2 agents', 'B: 3 agents', 'C: 2 agents (faster)']
df["Scenario"] = scenarios
print(df)
df.to_csv("call_center_results.csv", index=False)


# ------------------------------
# 6️⃣  Visualization (3 Different Chart Types)
# ------------------------------

# Chart 1 – Bar Chart (Average Waiting Time)
plt.figure(figsize=(8, 5))
plt.bar(df["Scenario"], df["AvgWait(s)"], color='skyblue', edgecolor='black')
plt.title("Average Waiting Time by Scenario", fontsize=14)
plt.ylabel("Avg Wait (seconds)")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# Chart 2 – Line Chart (Average Queue Length)
plt.figure(figsize=(8, 5))
plt.plot(df["Scenario"], df["AvgQueue"], marker='o', color='green', linewidth=2)
plt.title("Average Queue Length by Scenario", fontsize=14)
plt.ylabel("Avg Queue Length")
plt.xlabel("Scenario")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# Chart 3 – Pie Chart (Agent Utilization)
plt.figure(figsize=(7, 7))
plt.pie(df["Utilization"], labels=df["Scenario"], autopct='%1.1f%%',
        colors=['orange', 'lightcoral', 'gold'], startangle=140)
plt.title("Agent Utilization Comparison", fontsize=14)
plt.tight_layout()
plt.show()

print("\n✅ Results saved to call_center_results.csv")
