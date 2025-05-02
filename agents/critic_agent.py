class CriticAgent:
    def review_plan(self, plan):
        # Review the plan for coherence and completeness
        if "step1" not in plan or "step2" not in plan:
            raise ValueError("Plan is incomplete")
        return plan