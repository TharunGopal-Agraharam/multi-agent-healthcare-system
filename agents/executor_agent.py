class ExecutorAgent:
    def run_query(self, query_code):
        patient_list = [
            {"name": "John Doe", "email": "john@example.com"},
            {"name": "Jane Smith", "email": "jane@example.com"}
        ]
        print(f"ExecutorAgent generated patient list: {patient_list}")
        return patient_list
