import cerberus

from src.shared.validator.abc_validator import Validator


class ValidatorCerberus(Validator):

    def __init__(self):
        self.__validator = cerberus.Validator()
        super(ValidatorCerberus, self).__init__()

    def is_valid(self, adict, schema):
        return self.__validator.validate(adict, schema)

    def get_errors(self):
        return self.__validator.errors

    def get_valid_data(self):
        return self.__validator.document
