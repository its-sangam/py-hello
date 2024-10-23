# tasks/task.py
from abc import ABC, abstractmethod

class Task(ABC):
    @abstractmethod
    def execute(self):
        """Method to be implemented by subclasses."""
        pass

    @staticmethod
    def log_task(message):
        """Static method to log messages."""
        print(f"[LOG] {message}")

    def __str__(self):
        return self.__class__.__name__
