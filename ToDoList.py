import Task

class ToDoList:
    tasks = []

    def add_task(self, title, description, priority):
        self.tasks.append(Task(title,description,priority))

    def remove_task(self, title):
        temp = 0
        for i in range(len(self.tasks)):
            if self.tasks[i].title == title:
                temp = i
        del self.tasks[temp]

    def view_sorted_tasks(self):
        print(self.tasks.sort())

    def mark_as_completed(self, title):
        temp = 0
        for i in range(len(self.tasks)):
            if self.tasks[i].title == title:
                temp = i
        self.tasks[temp].is_completed = True




