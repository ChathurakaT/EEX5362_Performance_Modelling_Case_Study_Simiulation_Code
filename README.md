📞 Call Center Queue Simulation – Case Study
🎯 Project Overview

This project simulates a Customer Service Queue System to analyze how different agent configurations affect system performance.
The goal is to compare the impact of varying numbers of agents and service rates on key metrics such as:

Average waiting time

Average queue length

Agent utilization

Three scenarios were evaluated using a Python-based discrete event simulation.

| Scenario | Description     | Agents | Service Rate (calls/minute) |
| -------- | --------------- | ------ | --------------------------- |
| A        | Base Case       | 2      | 2.0                         |
| B        | Increased Staff | 3      | 2.0                         |
| C        | Faster Agents   | 2      | 2.6                         |

⚙️ Simulation Details

Simulation Duration: 1000 minutes

Arrival Rate (λ): 3 customers per minute

Queue Discipline: First Come, First Served (FCFS)

Service Model: M/M/c (Poisson arrivals, exponential service, c servers)

Libraries Used: simpy, numpy, matplotlib

🧠 Key Metrics

During each simulation, the following performance measures were collected:

Average Waiting Time (seconds)

Average Queue Length (customers)

Agent Utilization (%)

These values were plotted to visually compare the performance across the three scenarios.

📊 Results and Visualizations

The simulation results were visualized using Matplotlib:

Figure	Description
Figure 1	Average Waiting Time by Scenario
Figure 2	Average Queue Length by Scenario
Figure 3	Agent Utilization Comparison
