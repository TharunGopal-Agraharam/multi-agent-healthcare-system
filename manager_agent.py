print("Starting ManagerAgent script...")
from agents import PlannerAgent, CriticAgent, EpidemiologistAgent, DataAnalystAgent, ExecutorAgent, OutreachAgent
print("Initializing ManagerAgent...")
manager = ManagerAgent()
class ManagerAgent:
    def initiate_workflow(self, workflow_name):
        print(f"Workflow '{workflow_name}' started.")

        # Step 1: Create a plan
        plan = self.planner_agent.create_plan(workflow_name)
        print(f"Plan generated: {plan}")

        # Step 2: Fetch patient list
        patient_list = self.executor_agent.run_query(plan['query_code'])
        print(f"Patient list fetched: {patient_list}")

        # Step 3: Send outreach emails
        self.outreach_agent.send_emails(patient_list)
        print("Emails have been sent.")
        
        # Step 3: Outreach
        self.outreach.send_emails(patient_list)
