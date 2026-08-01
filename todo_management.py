from task import Task
import csv

class ToDoList():
    def __init__(self):
        self.tasks = []
        
    def add_task(self, name, description, priority): 
        self.tasks.append(Task(name, description, priority))
        print(f'{name} added to tasks correctly.')
        self.save_to_csv()

    def show_tasks(self):
        i=0
        if len(self.tasks) == 0 :
            print("There is no tasks.")
        else :
            for t in self.tasks:
                i+=1
                print(f'{i}: {t.name} \ndescription: {t.description} \npriority: {t.priority}\n')

        
        

    def remove_task(self, name):
        for t in self.tasks:
            if t.name == name :
                self.tasks.remove(t)
                print(f'{name} removed from tasks.')
                self.save_to_csv()
                return
             
        print("Not found in tasks.")

       

    def save_to_csv(self): 
        with open("tasks.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "description", "priority"])

            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority]) 

    

    def load_from_csv(self):
        try:
            self.tasks.clear()
            with open("tasks.csv" , "r") as f:
                reader = csv.reader(f)
                next(reader)


                for r in reader :
                    task = Task(r[0], r[1], r[2])
                    self.tasks.append(task)

        except FileNotFoundError:
            print("Starting with empty list.")
        