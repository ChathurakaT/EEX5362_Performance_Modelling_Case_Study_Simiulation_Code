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

| Figure       | Description                      |
| ------------ | -------------------------------- |
| **Figure 1** | Average Waiting Time by Scenario |
| **Figure 2** | Average Queue Length by Scenario |
| **Figure 3** | Agent Utilization Comparison     |


📈 Example Output

Scenario A (2 agents): Avg Wait ≈ 67s, Queue ≈ 3.3

Scenario B (3 agents): Avg Wait ≈ 2.6s, Queue ≈ 0.1

Scenario C (2 agents, faster): Avg Wait ≈ 9.6s, Queue ≈ 0.45

These outcomes show that adding more agents or improving their service rate drastically reduces both waiting time and queue buildup.


💡 Insights & Recommendations

Adding one more agent greatly reduces customer waiting time.

Increasing service rate also helps, though to a lesser extent.

Trade-off: More agents mean lower utilization, so cost vs. performance must be balanced.

Recommendation: Implement dynamic staffing or AI-based automation to handle peak loads efficiently.


🧰 Code Usage
1️⃣ Install Dependencies
pip install simpy numpy matplotlib

2️⃣ Run the Simulation
python call_center_simulation.py


3️⃣ Output

The program generates:

Average waiting time

Average queue length

Agent utilization
and automatically plots all charts for comparison.


🧩 Technologies Used

Python 3.9+

SimPy – for discrete event simulation

NumPy – for statistical calculations

Matplotlib – for visualization


✍️ Author

D.W.C. Tharushan

Final Year BSE (Hons) Student

The Open University of Sri Lanka

📧 s92069979@ousl.lk
