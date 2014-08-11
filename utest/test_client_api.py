import unittest

from SSHLibrary import SSHClient


class TestClienAPI(unittest.TestCase):

    def test_login_close_and_login_again(self):
        s = SSHClient('localhost', prompt='$ ')
        s.login('test', 'test')
        s.execute_command('ls')
        s.close()
        s.login('test', 'test')
        s.execute_command('ls')
