# tasks/push_notification.py
from .task import Task

class PushNotificationTask(Task):
    def execute(self):
        self.log_task("Starting to send push notification...")
        # Here would be the implementation for sending a push notification.
        print("Push notification sent successfully.")

    def __repr__(self):
        return f"PushNotificationTask()"
