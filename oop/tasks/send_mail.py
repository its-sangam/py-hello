# tasks/send_mail.py
from .task import Task

class SendMail(Task):

    def execute(self):
        self.log_task("Starting to send email...")
        # Here would be the implementation for sending an email.
        print("Email sent successfully.")

    def __repr__(self):
        return f"SendMail()"