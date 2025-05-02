class OutreachAgent:
    def send_emails(self, patient_list):
        print(f"Patient list received for outreach: {patient_list}")
        with open("outreach.log", "w") as log_file:
            for patient in patient_list:
                email_body = f"Dear {patient['name']}, we recommend scheduling your colonoscopy."
                log_file.write(f"Sending email to {patient['email']}: {email_body}\n")
                print(f"Sending email to {patient['email']}: {email_body}")
