from task import Task

class ToDoList():
    def __init__(self):
        self.tasks = []
        
    def add_task(self, name, description, priority): 
        self.tasks.append(Task(name, description, priority))

    def show_tasks(self):
        pass

    def remove_task(self):
        pass

    def save_to_csv(self): 
        pass

    def load_from_csv(self):
        pass