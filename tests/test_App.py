import unittest
from unittest.mock import mock_open, Mock, create_autospec, patch
from src.App import App

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = App()

    def test_app_readcontent(self):
        with patch('builtins.open', mock_open(read_data="test\ndata\n")) as mockfile:
            self.assertEqual(self.app.readcontent('fakefile.txt'), "test\ndata\n")
            mockfile.assert_called_with('fakefile.txt', 'r')

    def test_app_readline(self):
        with patch('builtins.open', mock_open(read_data="line1\nline2\nline3\n")) as mockfile:
            self.assertEqual(self.app.readline("fakefile.txt"), "line1\n")
            mockfile.assert_called_once_with("fakefile.txt", "r")

    def test_app_appendfile(self):
        with patch('builtins.open', mock_open(read_data="line1\n")) as mockfile:
            self.app.appendfile("fakefile.txt", "line2")
            mockfile.assert_called_once_with("fakefile.txt", "a")
            h = mockfile()
            h.write.assert_called_once_with("line2")

    def test_app_writefile(self):
        with patch('builtins.open', mock_open(read_data="line1\n")) as mockfile:
            self.app.writefile("fakefile.txt", "line2")
            mockfile.assert_called_once_with("fakefile.txt", "w")
            h = mockfile()
            h.write.assert_called_once_with("line2")

    def test_app_deletefile(self):
        spec = create_autospec(self.app)
        spec.deletefile("fakefile.txt")
        spec.deletefile.assert_called_once_with("fakefile.txt")

    def tearDown(self):
        self.app = None


if __name__ == "__main__":
    unittest.main()