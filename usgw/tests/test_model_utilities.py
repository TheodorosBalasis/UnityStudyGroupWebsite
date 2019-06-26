import unittest
import json
from usgw.models.model_utilities import to_json_response, from_dict, from_json
from usgw.models.model_utilities import is_dict_instance, is_dict_instance_strict
from usgw.models.model_utilities import get_invalid_field, get_fields, get_methods
from usgw.models.model_utilities import filter_dunder
from usgw.tests.mocks import TestType, TestEmptyType


class TestFromDict(unittest.TestCase):
    def test_errors(self):
        with self.assertRaises(TypeError):
            from_dict('Not a dictionary', TestType)
        with self.assertRaises(TypeError):
            from_dict({}, 'Not a type.')
        with self.assertRaises(ValueError):
            from_dict({'invalid_field': None}, TestType)

    def test_output(self):
        test_instance = TestType('test')
        output_instance = from_dict(test_instance.__dict__, TestType)
        self.assertEqual(test_instance, output_instance)
        try:
            output_instance.instance_method()
        except:
            self.fail('Instance method was not bound to object!')


class TestFromJSON(unittest.TestCase):
    def test_errors(self):
        test_instance = TestType('test')
        valid_json = json.dumps(test_instance.__dict__)
        with self.assertRaises(TypeError):
            from_json(0, TestType)
        with self.assertRaises(TypeError):
            from_json(valid_json, 'Not a type.')
        with self.assertRaises(ValueError):
            from_json('String but invalid JSON.', TestType)

    def test_output(self):
        test_instance = TestType('test')
        valid_json = json.dumps(test_instance.__dict__)
        output_instance = from_json(valid_json, TestType)
        self.assertEquals(test_instance, output_instance)


class TestIsDictInstance(unittest.TestCase):
    def test_errors(self):
        with self.assertRaises(TypeError):
            is_dict_instance('Not a dictionary', TestType)
        with self.assertRaises(TypeError):
            is_dict_instance({}, 'Not a type')

    def test_output(self):
        test_dict = {}
        self.assertTrue(is_dict_instance(test_dict, TestType))
        test_dict['test_field'] = None
        self.assertTrue(is_dict_instance(test_dict, TestType))
        test_dict['invalid_field'] = None
        self.assertFalse(is_dict_instance(test_dict, TestType))


class TestIsDictInstanceStrict(unittest.TestCase):
    def test_output(self):
        test_dict = {}
        self.assertFalse(is_dict_instance_strict(test_dict, TestType))
        test_dict['invalid_field'] = None
        test_dict.pop('invalid_field')
        test_dict['test_field'] = None
        self.assertTrue(is_dict_instance_strict(test_dict, TestType))


class TestGetInvalidField(unittest.TestCase):
    def test_errors(self):
        with self.assertRaises(TypeError):
            get_invalid_field('Not a dictionary', TestType)
        with self.assertRaises(TypeError):
            get_invalid_field({}, 'Not a type')

    def test_output(self):
        test_dict = {'test_field': None}
        self.assertEquals(get_invalid_field(test_dict, TestType), None)
        test_dict['invalid_field'] = None
        self.assertEquals(get_invalid_field(test_dict, TestType), 'invalid_field')


class TestTypeGets(unittest.TestCase):
    def test_get_fields_errors(self):
        with self.assertRaises(TypeError):
            get_fields(list)
        with self.assertRaises(AttributeError):
            get_fields(TestEmptyType)

    def test_get_fields_output(self):
        self.assertEqual(get_fields(TestType)[0], 'test_field')

    def test_get_methods_errors(self):
        with self.assertRaises(TypeError):
            get_methods('This is not a type.')

    def test_get_methods_output(self):
        output = get_methods(TestType)
        self.assertEqual(output[0][0], '__eq__')


class TestFilterDunder(unittest.TestCase):
    def test_errors(self):
        with self.assertRaises(TypeError):
            filter_dunder('Not a list')

    def test_output(self):
        output = filter_dunder(get_methods(TestType))
        self.assertEquals(output[0][0], 'instance_method')
