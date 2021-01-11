Hello

This code was created by Jatin Khurana for the interview of BlueStacks

Requirements:
    Role Based Access Control:
        Implement a role based auth system. System should be able to assign a role to a user and remove a role from a user.
        Entities are USER, ACTION TYPE, RESOURCE, ROLE
        ACTION TYPE defines the access level (Ex: READ, WRITE, DELETE)
        Access to resources for users are controlled strictly by the role. One user can have multiple roles. Given a user, action type and resource, the system should be able to tell whether user has access or not.


Steps to execute:
    The project can be opened in pycharm (or any other python IDE), where the entry point will be main.py
    The project can be run directly from terminals as well

    a) Change directory to where main.py is residing
    b) activate the virtual environment (venv) (Different commands for different OS)
    c) run command < python main.py > or right click file in IDE and press green play button(depends on the IDE)

    The rest of the menu is self explanatory and one just needs to follow the instructions


Features and Assumptions:
    The resource can be interacted in three ways, Reading, Writing and Deleting
    False inputs are handled for each functions keeping in mind the extensibility of the codes
    My CLI Interaction class won't be following Single Responsibility Principle as this is just to showcase the system functions rather than OOP


Prerequisites:
    The system has been initialized with 3 resources, 6 roles and 3 users (The initializations are in main.py, the entry point of the code)
    System is designed in such a fashion that New users, roles and resources can be created during runtime as well
    No external RABC system, or cloud/APIs are used, the system is purely designed to showcase OOP skills
    The project was built on python 3.9 but is backwards compatible upto python 3.0

