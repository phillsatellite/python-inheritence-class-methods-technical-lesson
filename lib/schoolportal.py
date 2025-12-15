import random
class User:
    all_names = []

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        User.add_name_to_all(first_name, last_name)

    def send_email(self,receiver,message):
        print(f"{self.email} to {receiver}: {message}")

    @classmethod
    def add_name_to_all(cls,first,last):
        fullname = first + " " + last
        cls.all_names.append(fullname)

    @classmethod
    def user_exists(cls,fullname):
        return fullname in cls.all_names

class Teacher(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name,email)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]

    def teach(self):
        return self.knowledge[random.randint(0, len(self.knowledge) - 1)]

class Student(User):
    def __init__(self, first_name, last_name, email,gpa):
        super().__init__(first_name, last_name,email)
        self.gpa = gpa
        self.knowledge = []

    def learn(self,knowledge_string):
        self.knowledge.append(knowledge_string)