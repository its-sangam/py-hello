# main.py
from tasks.send_mail import SendMail
from tasks.push_notification import PushNotificationTask
from tasks.check_subscription import CheckSubscriptionStatus

def main():
    tasks = [
        SendMail(),
        PushNotificationTask(),
        CheckSubscriptionStatus(),
    ]

    for task in tasks:
        print(f"Executing task: {task}")
        task.execute()

if __name__ == "__main__":
    main()
