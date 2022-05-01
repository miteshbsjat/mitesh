import unittest
from subprocess import CalledProcessError
from mitesh import MiteSh
from os import environ


class TestMiteSh(unittest.TestCase):

    def test_simple_echo(self):
        mitesh = MiteSh("echo -n Hello")
        expected = "Hello"
        for first_line in mitesh.execute():
            self.assertEqual(expected, first_line)


    def test_multiline_echos(self):
        mitesh = MiteSh("echo Hello; echo World")
        expected = [ "Hello", "World" ]
        index = 0
        for line in mitesh.execute():
            self.assertEqual(expected[index], line)
            index += 1


    def test_pipe(self):
        mitesh = MiteSh("echo Hello World | grep \"Hello World\"")
        expected = [ "Hello World" ]
        index = 0
        for line in mitesh.execute():
            self.assertEqual(expected[index], line)
            index += 1


    def test_awk(self):
        mitesh = MiteSh("echo \"Namaste Venkatesh\" | awk '{print NF}'")
        expected = [ "2" ]
        index = 0
        for line in mitesh.execute():
            self.assertEqual(expected[index], line)
            index += 1


    def test_subshell(self):
        mitesh = MiteSh("(echo \"Shree Ganeshay Namah\"; echo \"Namaste Venkatesh\") | awk '{print NF}'")
        expected = [ "3", "2" ]
        index = 0
        for line in mitesh.execute():
            self.assertEqual(expected[index], line)
            index += 1


    def test_command_not_present(self):
        mitesh = MiteSh("no-such-command >/dev/null 2>&1")
        expected = [ "no output" ]
        index = 0
        with self.assertRaises(CalledProcessError):
            for line in mitesh.execute():
                self.assertEqual(expected[index], line)
                index += 1


    def test_command_error(self):
        mitesh = MiteSh("echo Hello; exit -1")
        expected = [ "Hello" ]
        index = 0
        with self.assertRaises(CalledProcessError):
            for line in mitesh.execute():
                self.assertEqual(expected[index], line)
                index += 1


    def test_2_commands_for_same_output(self):
        mitesh = MiteSh('if [ -e "/etc/passwd" ]; then wc -l /etc/passwd | awk \'{print $1}\'; fi')
        expected = []
        for line in mitesh.execute():
            expected.append(line)
        mitesh = MiteSh('if [ -e "/etc/passwd" ]; then cat /etc/passwd | awk \'{print NR}\' | tail -1; fi')
        index = 0
        for line in mitesh.execute():
            expected.append(line)
            self.assertEqual(expected[index], line)
            index += 1


    def test_for_loop(self):
        mitesh = MiteSh("for i in $(seq 0 1000); do echo $i; done")
        index = 0
        for line in mitesh.execute():
            self.assertEqual(str(index), line)
            index += 1


    def test_shell_env(self):
        mitesh = MiteSh("echo $HOME")
        expected = [ environ.get("HOME") ]
        index = 0
        for line in mitesh.execute():
            self.assertEqual(expected[index], line)
            index += 1


    def test_dir_permission(self):
        with self.assertRaises(PermissionError):
            mitesh = MiteSh("echo Hello", sh_tmp_base='/root/mitesh')
            expected = [ "Hello" ]
            index = 0
            for line in mitesh.execute():
                self.assertEqual(expected[index], line)
                index += 1


if __name__ == '__main__':
    unittest.main()

