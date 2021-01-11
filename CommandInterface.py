import sys

from ActionType import ActionType


class CommandInterface:
    def __init__(self, rabc_system):
        self.__system = rabc_system

        self.__current_user = None
        self.__current_action_type = None
        self.__current_resource = None
        self.__current_role = None

    def execute_cli(self):
        while True:
            print("######     Main Menu   ########")
            print("1. Check for permissions")
            print("2. Create User")
            print("3. Assign Roles to User")
            print("4. Exit")
            option = input()
            if option == '1':
                self.__check_permissions()
            elif option == '2':
                self.__create_user()
            elif option == '3':
                self.__assign_roles()
            elif option == '4':
                sys.exit()
            else:
                print("Please choose a valid option")
                continue

    def __create_user(self):
        while True:
            print("Enter User Name")
            name = input()
            self.__system.create_user(name)

            print("Create More Users? Press 1 for Yes")
            if input() != '1':
                break

    def __assign_roles(self):
        while True:
            self.__select_user()
            self.__select_role()
            self.__system.assign_role_to_user(self.__current_user, self.__current_role)

            print("Assign More Roles? Press 1 for Yes")
            if input() != '1':
                break

    def __select_role(self):
        print("Please select Role")
        roles = self.__system.roles
        for role in roles:
            print(f"{roles.index(role)}. {role.name}")
        while True:
            try:
                option = int(input())
                self.__current_role = self.__system.roles[option]
                break
            except (ValueError, IndexError):
                print("Please choose a correct option for Roles")
                continue

    def __check_permissions(self):
        while True:
            self.__select_user()
            self.__select_resource()
            self.__select_action()

            if self.__system.has_permissions(user=self.__current_user, resource=self.__current_resource,
                                             action_type=self.__current_action_type):
                print(
                    f"{self.__current_user.name} has permissions to {self.__current_action_type.name} {self.__current_resource.name}")
            else:
                print(
                    f"{self.__current_user.name} doesn't have permissions to {self.__current_action_type.name} {self.__current_resource.name}")

            print("Press 1 to test again")
            if input() != '1':
                break

    def __select_user(self):
        print("Please select User")
        users = self.__system.users
        for user in users:
            print(f"{users.index(user)}. {user.name}")
        while True:
            try:
                option = int(input())
                self.__current_user = self.__system.users[option]
                break
            except (ValueError, IndexError):
                print("Please choose a correct option for User")
                continue

    def __select_resource(self):
        print("Select resource to access")
        resources = self.__system.resources
        for resource in resources:
            print(f"{resources.index(resource)}. {resource.name}")
        while True:
            try:
                option = int(input())
                self.__current_resource = self.__system.resources[option]
                break
            except (ValueError, IndexError):
                print("Please choose a correct option for Resource")
                continue

    def __select_action(self):
        print("Select action to perform")
        print(f"0. READ")
        print("1. WRITE")
        print("2. DELETE")
        while True:
            action = input()
            if action == '0':
                self.__current_action_type = ActionType.READ
                break
            elif action == '1':
                self.__current_action_type = ActionType.WRITE
                break
            elif action == '2':
                self.__current_action_type = ActionType.DELETE
                break
            else:
                print("Please choose a correct option for action")
                continue
