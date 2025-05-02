class OutreachAgent:
    def send_emails(self, patient_list):
        for patient in patient_list:
            email_body = f"Dear {patient['name']}, we recommend scheduling your colonoscopy."
            print(f"Sending email to {patient['email']}: {email_body}")