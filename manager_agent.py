from agents import PlannerAgent, CriticAgent, EpidemiologistAgent, DataAnalystAgent, ExecutorAgent, OutreachAgent

class ManagerAgent:
    def __init__(self):
        self.planner = PlannerAgent()
        self.critic = CriticAgent()
        self.epidemiologist = EpidemiologistAgent()
        self.data_analyst = DataAnalystAgent()
        self.executor = ExecutorAgent()
        self.outreach = OutreachAgent()

    def initiate_workflow(self, goal):
        # Step 1: Planning
        plan = self.planner.create_plan(goal)
        refined_plan = self.critic.review_plan(plan)
        
        # Step 2: Patient Cohort Selection
        criteria = self.epidemiologist.define_criteria()
        query_code = self.data_analyst.write_query(criteria)
        patient_list = self.executor.run_query(query_code)
        
        # Step 3: Outreach
        self.outreach.send_emails(patient_list)
