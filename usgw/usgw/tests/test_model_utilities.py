import unittest
import json
from usgw.models.model_utilities import to_json_response, from_dict, from_json
from usgw.tests.mocks import TestType, TestEmptyType


class TestFromDict(unittest.TestCase):
    def test_errors(self):
        with self.assertRaises(TypeError):
            from_dict('Not a dictionary', TestType)
        with self.assertRaises(TypeError):
            from_dict({}, 'Not a type.')
        with self.assertRaises(TypeError):
            from_dict({}, list)
        with self.assertRaises(TypeError):
            from_dict({}, int)
        with self.assertRaises(AttributeError):
            from_dict({}, TestEmptyType)
        with self.assertRaises(ValueError):
            from_dict({'invalid_field': None}, TestType)

    def test_output(self):
        test_instance = TestType('test')
        output_instance = from_dict(test_instance.__dict__, TestType)
        self.assertEqual(test_instance, output_instance)


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
