class PlannerAgent:
    def create_plan(self, goal):
        # Break down high-level goal into steps
        plan = {
            "step1": "Define patient cohort criteria",
            "step2": "Fetch patient data from FHIR API",
            "step3": "Send outreach emails"
        }
        return plan