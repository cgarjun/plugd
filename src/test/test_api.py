import unittest
import os
from plugd import api
from example import simple_example

class TestApi(unittest.TestCase):

    def setUp(self):
        """
        docstring
        """
        self.config_path = os.path.join(os.getcwd(), 'config.json')
        self.plugd_ins = api.Plugd(self.config_path)
        self.plugin_ins = simple_example.PlugdPlugin()

    def test_init(self):
        """
        docstring
        """
        self.assertTrue(self.plugd_ins)

    def test_is_valid_plugin(self):
        """
        docstring
        """
        self.assertTrue(self.plugd_ins.is_valid_plugin(self.plugin_ins))

    def test_get_plugin_module(self):
        """
        docstring
        """
        self.assertEqual(self.plugd_ins.get_plugin_module('example.simple_example'), simple_example)

    def test_run_plugin(self):
        """
        docstring
        """
        self.assertIsInstance(self.plugd_ins.run_plugin('simple_example'), simple_example.PlugdPlugin)

    def test_list_plugins(self):
        """
        docstring
        """
        self.assertEqual(self.plugd_ins.list_plugins(), self.plugd_ins.config['plugins'])
        

if __name__ == '__main':
    unittest.main()