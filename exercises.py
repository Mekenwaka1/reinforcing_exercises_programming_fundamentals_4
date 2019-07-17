emotions = { 
    'happiness': 3, 
    'stress': 2, 
    'fear': 1 
}

class Person:
    def __init__(self, name, emotions):
        self.name = name
        self.emotions = emotions

    def feeling(self):
        message = ""
        for key, value in self.emotions.items():
            if value == 1:
                level = "high"
            elif value == 2:
                level = "medium"
            elif value == 3:
                level = "low"
            message += "I am feeling a {} amount of {}.\n".format(level, key)
        return message

meke = Person("Meke", emotions)
print(meke.name)
print(meke.feeling())