#Maze 2020 aufgaben stack

class Stack:
    def __init__(self):
        self.storage = list()

    def add(self, excercise):
        self.storage.append(excercise)

    def get(self):
        last = self.storage[-1]
        self.storage.pop()
        return last
    
    def __str__(self):
        return "Stackobject holding " + str(len(self.storage)) + " tasks."

    def __repr__(self):
        return "Stackobject holding " + str(len(self.storage)) + " tasks."

    def all(self):
        return self.storage
