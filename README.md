# Technical Lesson: Inheritance, Class Attributions, and Class Methods

In this lesson, we will explore how to apply inheritance as well as class attributes and methods.

## Scenario

Imagine you are working for a school administration. You are updating their system to create a student and teacher portal. They will need a couple of class methods and attributes as well as classes themselves to allow for clean interaction.

* Create User super class
* Create Teacher and Student sub classes
* Create class attribute to track all users
* Create class methods to add users and to see all students.

## Resources & Tools

* [GitHub Repo](https://github.com/learn-co-curriculum/python-inheritence-class-methods-technical-lesson)

## Instructions

### Setup

Before we begin coding, let's complete the initial setup for this lesson: 
* Fork and Clone 
  * Go to the provided GitHub repository link.
  * Fork the repository to your GitHub account.
  * Clone the forked repository to your local machine.
* Open and Run File
  * Open the project in VSCode.
  * Run `pipenv install` to install all necessary dependencies.
  * Run `pipenv shell` to enter the virtual environment.

### Task 1: Define the Problem

You need to create several related classes, some with shared attributes. You will be tasked with:
* Create User super class
* Create Teacher and Student sub classes
* Create class attribute to track all users names
* Create class methods to add users and to find a specific user.

### Task 2: Determine the Design

Determine the design based on the account types:
* User
  * Attributes
    * First Name
    * Last Name
    * Email
    * Methods
    * send_email
  * Class Attributes
    *  all_names
  * Class Methods
    * add_name_to_all
    * user_exists
* Teacher
  * Attributes
    * First Name
    * Last Name
    * Email
    * Knowledge
  * Methods
    * teach
* Student
  * Attributes
    * First Name
    * Last Name
    * Email
    * GPA
  * Methods
    * learn

### Task 3: Develop, Test, and Refine the Code

#### Step 1: Create a Feature Branch

```bash
git checkout -b school_model
```

#### Step 2: Set up parent class

When we are building classes and determining when to use a parent class our mind must first go to what are shared values. In this case we want to make a distinction between student and teacher, however they will have many shared attributes and methods as we want to use the same school portal for both. Because of this that is telling us we want to build a parent class to host those shared attributes
<br />
All code changes will happen in lib/schoolportal.py

```python
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
```

We set up our user class to init with all of the shared attributes, the name and email.

#### Step 3: Set up child methods

Now that the parent class is built we can build our two child classes and pass into them the inherited parent class. Then when we want to access our parent class we would use the keyword ```super()```.

```python
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

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

class Student(User):
    def __init__(self, first_name, last_name, email,gpa):
        super().__init__(first_name, last_name,email)
        self.gpa = gpa
        self.knowledge = []
```

We pass into our class name the parent class, that will allow the child classes of teacher and student to access anything the user class has. Then we call ```super().__init__()``` in order to set up the initial shared variables. 

#### Step 4: Child methods

We can now build separate methods for our children, giving us access to different features if you are a student or teacher.

```python
import random
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

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
```

We have added a teach and learn method to the teacher and student respectively. Each method is only accessible within the relevant child class.

#### Step 5: Create parent methods

Any method we have that we would like to access throughout all of our children should be added to our parent class.

```python
import random
class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    def send_email(self,receiver,message):
        print(f"{self.email} to {receiver}: {message}") 

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
```

We have built a send email method that while not actually sending an email uses the users current email to simulate a sent email. This is a feature accessible to both students and teachers, and now both types of instances can call the parent method.

#### Step 6: Adding class methods and attributes

Switching topics to class methods and attributes, these are methods accessible to classes as opposed to instances. In this case we are adding two class methods and one attribute to our parent user class.

```python
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
        return [True for user in cls.all_names if user == fullname]


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
```

We have built an ```all_names``` list to be accessible outside of the ```__init__```, this means it is accessible to the class itself as opposed to a specific instance. We then create two class methods using the ```@classmethod``` decorator. All of these class specific features can be accessed by using ```User.all_names``` and ```User.user_exists(“Some Name”)``` for example. This can be seen in use within the init when we call ```add_name_to_all```.
<br />
Test to ensure we can create and call all these methods by creating instances of students and teachers
<br />
After verifying that the classes work commit changes.

```bash
git commit -am "Completed User,Teacher, and Student model"
```

#### Step 7: Push changes to GitHub and Merge Branches

* Push the branch to GitHub:

```bash
git push origin school_model
```

* Create a Pull Request (PR) on GitHub.
* Merge the PR into main after review.
* Pull the new merged main branch locally and delete merged feature branch (optional):

```bash
git checkout main
git pull origin main

git branch -d school_model
```

If the last command doesn’t delete the branch, it’s likely git is not recognizing the branch as having been merged. Verify you do have the merged code in your main branch, then you can run the same command but with a capital D to ignore the warning and delete the branch anyway. 

```bash
git branch -D school_model
```

### Task 4: Document and Maintain

Best Practice documentation steps:

* Add comments to code to explain purpose and logic
* Clarify intent / functionality of code to other developers
* Add screenshot of completed work included in Markdown in README.
* Update README text to reflect the functionality of the application following https://makeareadme.com. 
* Delete any stale branches on GitHub
* Remove unnecessary/commented out code
* If needed, update git ignore to remove sensitive data

### Considerations
* Super
  * If you ever need to access a feature of the parent class within a child class you need to start with ```Super()```, if you have a method within the child that uses a parent method you can call that parent method with ```Super().method()```
* cls
  * For any class method you will see that cls is added within the inputs similarly to self. This is also an implicit variable that is passed in similar to self representing the class as a whole.
