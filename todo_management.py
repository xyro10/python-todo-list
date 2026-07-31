from task import Task

class ToDoList():
    def __init__(self):
        self.tasks = []
        
    def add_task(self, name, description, priority): 
        self.tasks.append(Task(name, description, priority))
        print(f'{name} added to tasks correctly.')

    def show_tasks(self):
        pass

    def remove_task(self, name):
        for t in self.tasks:
            if t.name == name :
                self.tasks.remove(t)
                print(f'{name} removed from tasks.')
                return
             
        print("Not found in tasks.")

       

    def save_to_csv(self): 
        pass

    def load_from_csv(self):
        pass