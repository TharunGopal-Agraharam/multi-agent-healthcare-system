print("Starting ManagerAgent script...")

class ManagerAgent:
    def __init__(self):
        print("Initializing agents...")
        self.planner_agent = PlannerAgent()
        self.executor_agent = ExecutorAgent()
        self.outreach_agent = OutreachAgent()

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


class PlannerAgent:
    def create_plan(self, goal):
        print(f"Creating plan for goal: {goal}")
        # Example plan
        plan = {
            "query_code": "QUERY_CODE_FOR_PATIENTS",
            "description": "Outreach for colonoscopy screenings"
        }
        print(f"Plan created: {plan}")
        return plan


class ExecutorAgent:
    def run_query(self, query_code):
        print(f"Running query with code: {query_code}")
        # Mock patient list
        patient_list = [
            {"name": "John Doe", "email": "john@example.com"},
            {"name": "Jane Smith", "email": "jane@example.com"}
        ]
        print(f"Query result: {patient_list}")
        return patient_list


class OutreachAgent:
    def send_emails(self, patient_list):
        print(f"Sending emails to patients: {patient_list}")
        for patient in patient_list:
            print(f"Sending email to {patient['name']} at {patient['email']}")


# Main script execution
print("Initializing ManagerAgent...")
manager = ManagerAgent()
print("Initiating workflow...")
manager.initiate_workflow("Send outreach emails for colonoscopy screenings")
