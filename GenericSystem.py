from abc import ABC, abstractmethod

from User import User


class GenericSystem(ABC):

    def __init__(self, users, resources):
        self.__users = users
        self.__resources = resources

    @abstractmethod
    def has_permissions(self):
        pass

    @property
    def users(self):
        return self.__users

    @property
    def resources(self):
        return self.__resources

    def create_user(self, name):
        new_user = User(name)
        self.__users.append(new_user)

