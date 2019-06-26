class TestType(object):
    '''Basic class with one field, an instance method, and a static method.'''
    def __init__(self, test_field):
        self.test_field = test_field

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def instance_method(self):
        pass

    @staticmethod
    def static_method():
        pass

    test_attr = None


class TestEmptyType():
    '''Empty class.'''
    pass
