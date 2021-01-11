from ActionType import ActionType
from Resource import Resource
import warnings


class Role:
    def __init__(self, name):
        self.__resource_privileges = {}
        self.__name = name

    @property
    def name(self):
        return self.__name

    def add_resource_privileges(self, resource, privileges):
        if not isinstance(privileges, list):
            raise (ValueError(f"privileges should be a list of action types"))

        if not isinstance(resource, Resource):
            raise (ValueError(f"resource should be of type Resource"))

        if resource not in self.__resource_privileges:
            self.__resource_privileges[resource] = []

        for action_type in privileges:
            if not isinstance(action_type, ActionType):
                warnings.warn(f"action_type is not of type ActionType and will be skipped")
                continue

            if action_type not in self.__resource_privileges[resource]:
                self.__resource_privileges[resource].append(action_type)

        return self

    def has_resource_access(self, resource, action_type):
        if not isinstance(action_type, ActionType):
            raise (ValueError(f"action_type should be of type ActionType"))

        if not isinstance(resource, Resource):
            raise (ValueError(f"resource should be of type Resource"))

        if resource not in self.__resource_privileges:
            return False

        if action_type in self.__resource_privileges[resource]:
            return True
        else:
            return False

