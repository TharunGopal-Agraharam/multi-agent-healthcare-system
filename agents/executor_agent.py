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
