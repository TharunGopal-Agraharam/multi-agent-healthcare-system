class DataAnalystAgent:
    def write_query(self, criteria):
        # Write query for FHIR API
        return f"SELECT * FROM Patients WHERE age BETWEEN {criteria['age_range'][0]} AND {criteria['age_range'][1]} AND condition = '{criteria['condition']}'"