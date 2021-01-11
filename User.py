from Role import Role


class User:
    def __init__(self, name):
        self.__roles = []
        self.__name = name

    def add_role(self, role):
        if not isinstance(role, Role):
            raise (ValueError(f"role is not of type Role"))
        self.__roles.append(role)
        return self

    def remove_role(self, role):
        if not isinstance(role, Role):
            raise (ValueError(f"role is not of type Role"))
        if self.__roles.__contains__(role):
            self.__roles.remove(role)
        else:
            raise (ValueError(f"User doesn't has {role} role"))

    # def add_multiple_roles(self, roles):
    #     for role in roles:
    #         self.add_role(role)

    @property
    def roles(self):
        return self.__roles

    @property
    def name(self):
        return self.__name
