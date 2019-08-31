from echo import actions
from protocol import make_response
import unittest
from datetime import datetime


class TestGetEcho(unittest.TestCase):
    
    
    request = {
                'action': 'some_action',
                }
    def test_get_echo_timestamp(self):
        req1 = TestGetEcho.request
        self.assertAlmostEqual(actions.get_echo(req1).get('time'), make_response(req1, 200).get('time'), 1)


    def test_get_echo_action_and_data(self):
        req2 = TestGetEcho.request
        self.assertEqual(actions.get_echo(req2).get('action', 'data'), make_response(req2, 200).get('action', 'data'))

if __name__ == '__main__':
    unittest.main()
