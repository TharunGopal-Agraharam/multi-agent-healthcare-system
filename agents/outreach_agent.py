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
