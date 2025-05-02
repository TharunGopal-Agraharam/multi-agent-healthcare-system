# Multi-Agent Healthcare System

This repository contains a multi-agent system designed to assist healthcare organizations in proactive outreach for high-risk patient populations. The system leverages collaborative agents to perform tasks like patient cohort selection, data querying, and personalized outreach.

## Features
- **Manager Agent**: Orchestrates the workflow.
- **Planner Agent**: Translates high-level goals into actionable plans.
- **Critic Agent**: Reviews and refines plans.
- **Epidemiologist Agent**: Defines criteria for patient cohort selection.
- **Data Analyst Agent**: Writes queries to fetch data.
- **Executor Agent**: Runs queries and retrieves data.
- **Outreach Agent**: Sends personalized emails to patients.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/TharunGopal-Agraharam/multi-agent-healthcare-system.git
   ```
2. Navigate to the repository directory:
   ```bash
   cd multi-agent-healthcare-system
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Start by initiating the workflow through the **Manager Agent**:
```python
from manager_agent import ManagerAgent

manager = ManagerAgent()
manager.initiate_workflow("Send outreach emails for colonoscopy screenings")
```

## License
This project is licensed under the MIT License.