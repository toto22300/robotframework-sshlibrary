import unittest

from SSHLibrary import SSHLibrary


HOSTNAME = 'localhost'


class TestSSHLibraryConfiguration(unittest.TestCase):

    def test_default_confguration(self):
        self._assert_config(SSHLibrary()._config)

    def test_setting_configruation_values(self):
        cfg = SSHLibrary(newline='CRLF', prompt='$')._config
        self._assert_config(cfg, newline='\r\n', prompt='$')

    def test_set_default_confguarition(self):
        timeout, newline, prompt, level = 1, '\r\n', '>', 'DEBUG'
        lib = SSHLibrary()
        lib.set_default_configuration('timeout=%s' % timeout,
                                      'newline=%s' % newline,
                                      'prompt=%s' % prompt,
                                      'log_level=%s' % level)
        self._assert_config(lib._config, timeout, newline, prompt, level)

    def _assert_config(self, cfg, timeout=3, newline='\n', prompt=None,
                       log_level='INFO'):
        self.assertEquals(cfg.timeout, timeout)
        self.assertEquals(cfg.newline, newline)
        self.assertEquals(cfg.prompt, prompt)
        self.assertEquals(cfg.log_level, log_level)


class TestSSHClientConfiguration(unittest.TestCase):

    def test_default_client_configuration(self):
        lib = SSHLibrary()
        lib.open_connection(HOSTNAME)
        self._assert_config(lib.ssh_client.config)

    def test_overriding_client_configuration(self):
        lib = SSHLibrary(timeout=4)
        lib.open_connection(HOSTNAME, timeout=5)
        self._assert_config(lib.ssh_client.config, timeout=5)

    def test_set_client_confguration(self):
        port, term_type = 23, 'ansi'
        lib = SSHLibrary()
        lib.open_connection(HOSTNAME)
        lib.set_client_configuration('port=%d' % port,
                                     'term_type=%s' % term_type)
        self._assert_config(lib.ssh_client.config, port=port,
                            term_type=term_type)


    def _assert_config(self, cfg, host=HOSTNAME, timeout=3, newline='\n',
                       prompt=None, port=22, term_type='vt100'):
        self.assertEquals(cfg.host, host)
        self.assertEquals(cfg.timeout, timeout)
        self.assertEquals(cfg.newline, newline)
        self.assertEquals(cfg.prompt, prompt)
        self.assertEquals(cfg.term_type, term_type)
        self.assertEquals(cfg.port, port)


if __name__ == '__main__':
    unittest.main()
