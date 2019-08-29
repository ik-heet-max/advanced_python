from echo import actions
from protocol import make_response
import unittest


class TestGetEcho(unittest.TestCase):
    
    def test_get_echo_(self):
        request = {
                'data': None,
                'time': 'some',
                }
        self.assertEqual(actions.get_echo(request), make_response(request, 200, request.get('data')))


if __name__ == '__main__':
    unittest.main()
