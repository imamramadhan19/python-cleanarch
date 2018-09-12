from abc import ABC, abstractmethod


class Validator(ABC, object):

    @abstractmethod
    def is_valid(self): pass

    @abstractmethod
    def get_errors(self): pass

    @abstractmethod
    def get_valid_data(self): pass
