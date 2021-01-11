from ActionType import ActionType
from Resource import Resource
from GenericSystem import GenericSystem
from Role import Role
from User import User


class RABCSystem(GenericSystem):

    def __init__(self, users, resources, roles):
        super().__init__(users, resources)
        self.__roles = roles

    def has_permissions(self, user, resource, action_type):
        if not isinstance(user, User):
            raise (ValueError(f"user is not of type User"))

        if not isinstance(resource, Resource):
            raise (ValueError(f"resource is not of type Resource"))

        if not isinstance(action_type, ActionType):
            raise (ValueError(f"action_type is not of type ActionType"))

        user_roles = user.roles
        for role in user_roles:
            if role.has_resource_access(resource, action_type):
                return True

        return False

    @property
    def roles(self):
        return self.__roles

    def assign_role_to_user(self, user, role):
        if not isinstance(user, User):
            raise (ValueError("user should be of type User"))

        if not isinstance(role, Role):
            raise (ValueError("role should be of type Role"))

        user.add_role(role)

