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


# Multi-Agent Healthcare System

## **Overview**
The Multi-Agent Healthcare System is a modular and intelligent framework designed to automate healthcare workflows. It employs multiple specialized agents that collaborate to achieve specific goals, such as sending outreach emails for patient health screenings. This project demonstrates how multi-agent systems can streamline healthcare operations by automating repetitive and time-consuming tasks.

---

## **Key Features**
- Modular architecture with distinct responsibilities for each agent.
- Seamless coordination between planning, data retrieval, and communication.
- Fully automated workflow execution with clear debugging and logging outputs.
- Scalable design to accommodate additional workflows and agents.

---

## **Workflow**
The system follows a well-defined workflow to achieve its goals:
1. **Goal Definition**: The user specifies a goal (e.g., "Send outreach emails for colonoscopy screenings").
2. **Plan Generation**: The `PlannerAgent` creates a structured plan with a `query_code` and `description`.
3. **Data Retrieval**: The `ExecutorAgent` fetches the required data (e.g., a patient list) using the `query_code`.
4. **Action Execution**: The `OutreachAgent` performs the required actions (e.g., sending emails) based on the retrieved data.

---

## **Architecture**
The project consists of the following agents:

### **1. ManagerAgent**
- The central coordinator responsible for orchestrating the workflow.
- Initializes other agents and ensures smooth execution of the workflow.

### **2. PlannerAgent**
- Generates a structured plan to achieve the specified goal.
- Outputs a `query_code` and a `description` for the goal.

### **3. ExecutorAgent**
- Executes the `query_code` from the plan to fetch the required data.
- Returns structured data (e.g., a list of patients with names and email addresses).

### **4. OutreachAgent**
- Uses the data fetched by the `ExecutorAgent` to perform the required actions.
- Sends emails to patients and logs the details.

---

![image](https://github.com/user-attachments/assets/16d716f1-be94-42d5-84a2-227b5ca3812b)


## **Email Content**
The email sent to patients contains the following details:

- **Subject**: Outreach for Colonoscopy Screenings
- **Body**:
  ```
  Dear [Patient's Name],

  We hope this message finds you well. As part of our healthcare initiative, we are reaching out to encourage you to schedule a colonoscopy screening. Regular screenings are vital for early detection and prevention of colorectal issues.

  Please contact us or visit our website to learn more and schedule your appointment.

  Best regards,  
  [Your Healthcare Team Name]  
  [Contact Information]  
  ```

This email is dynamically personalized for each patient using their name and other relevant details.

---

## **Code Explanation**

### **ManagerAgent**
The `ManagerAgent` coordinates the workflow by invoking the appropriate methods in other agents.

```python name=manager_agent.py
class ManagerAgent:
    def __init__(self):
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

        # Step 3: Perform outreach
        self.outreach_agent.send_emails(patient_list)
        print("Emails have been sent.")
```

---

### **PlannerAgent**
The `PlannerAgent` generates a structured plan for the specified goal.

```python name=planner_agent.py
class PlannerAgent:
    def create_plan(self, goal):
        """
        Generates a plan to achieve the specified goal.

        Example Plan:
        {
            "query_code": "QUERY_CODE_FOR_PATIENTS",
            "description": "Outreach for colonoscopy screenings"
        }
        """
        print(f"Creating plan for goal: {goal}")
        plan = {
            "query_code": "QUERY_CODE_FOR_PATIENTS",
            "description": "Outreach for colonoscopy screenings"
        }
        print(f"Plan created: {plan}")
        return plan
```

---

### **ExecutorAgent**
The `ExecutorAgent` fetches the required data based on the `query_code`.

```python name=executor_agent.py
class ExecutorAgent:
    def run_query(self, query_code):
        """
        Executes the query code to fetch the required data.
        Returns a list of patients.
        """
        print(f"Running query with code: {query_code}")
        patient_list = [
            {"name": "John Doe", "email": "john@example.com"},
            {"name": "Jane Smith", "email": "jane@example.com"}
        ]
        print(f"Query result: {patient_list}")
        return patient_list
```

---

### **OutreachAgent**
The `OutreachAgent` sends emails to the patients in the list.

```python name=outreach_agent.py
class OutreachAgent:
    def send_emails(self, patient_list):
        """
        Sends personalized emails to the provided list of patients.
        """
        print(f"Sending emails to patients: {patient_list}")
        
        for patient in patient_list:
            # Construct the email content
            subject = "Important: Schedule Your Colonoscopy Screening"
            body = f"""
            Dear {patient['name']},

            We hope this message finds you well. As part of our healthcare initiative, we are reaching out to encourage you 
            to schedule a colonoscopy screening. Regular screenings are vital for early detection and prevention of 
            colorectal issues.

            Please contact us or visit our website to learn more and schedule your appointment.

            Best regards,
            Your Healthcare Team
            """
            
            # Log the email being sent
            print(f"Sending email to {patient['name']} at {patient['email']}")
            print(f"Subject: {subject}")
            print(f"Body: {body}")
```

---

## **Sample Execution**
### **Command**
```bash
python manager_agent.py
```

### **Output**
```plaintext
Starting ManagerAgent script...
Initializing ManagerAgent...
Initializing agents...
Initiating workflow...
Workflow 'Send outreach emails for colonoscopy screenings' started.
Creating plan for goal: Send outreach emails for colonoscopy screenings
Plan created: {'query_code': 'QUERY_CODE_FOR_PATIENTS', 'description': 'Outreach for colonoscopy screenings'}
Plan generated: {'query_code': 'QUERY_CODE_FOR_PATIENTS', 'description': 'Outreach for colonoscopy screenings'}
Running query with code: QUERY_CODE_FOR_PATIENTS
Query result: [{'name': 'John Doe', 'email': 'john@example.com'}, {'name': 'Jane Smith', 'email': 'jane@example.com'}]
Patient list fetched: [{'name': 'John Doe', 'email': 'john@example.com'}, {'name': 'Jane Smith', 'email': 'jane@example.com'}]
Sending emails to patients: [{'name': 'John Doe', 'email': 'john@example.com'}, {'name': 'Jane Smith', 'email': 'jane@example.com'}]
Sending email to John Doe at john@example.com
Subject: Important: Schedule Your Colonoscopy Screening
Body:
    Dear John Doe,

    We hope this message finds you well. As part of our healthcare initiative, we are reaching out to encourage you 
    to schedule a colonoscopy screening. Regular screenings are vital for early detection and prevention of 
    colorectal issues.

    Please contact us or visit our website to learn more and schedule your appointment.

    Best regards,
    Your Healthcare Team
Sending email to Jane Smith at jane@example.com
Subject: Important: Schedule Your Colonoscopy Screening
Body:
    Dear Jane Smith,

    We hope this message finds you well. As part of our healthcare initiative, we are reaching out to encourage you 
    to schedule a colonoscopy screening. Regular screenings are vital for early detection and prevention of 
    colorectal issues.

    Please contact us or visit our website to learn more and schedule your appointment.

    Best regards,
    Your Healthcare Team
Emails have been sent.
```

---

## **Future Enhancements**
1. **Integration with Real APIs**:
   - Replace the mock patient list with real data from healthcare APIs like FHIR.

2. **Email Service Integration**:
   - Use an email delivery service (e.g., SMTP, SendGrid) to send real emails.

3. **Error Handling**:
   - Add robust error-handling mechanisms for network issues, invalid data, etc.

4. **Logging**:
   - Implement a logging system to save outputs and errors to a file for better traceability.

5. **Additional Workflows**:
   - Enhance the system to include workflows for appointment scheduling, reminders, and follow-ups.

---

## **License**
This project is open-source and available under the [MIT License](LICENSE).

---

## **Contributors**
- **Tharun Gopal Agraharam** (Project Creator)
