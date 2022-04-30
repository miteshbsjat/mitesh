## !! Shree Ganeshay Namah !! ##

# MITESH => Modestly Integrated To Every SHell #
# __all__ = ['MiteSh']

from os import environ, path, makedirs, chmod, stat, linesep
from hashlib import sha256
from stat import S_IEXEC
from subprocess import Popen, PIPE, CalledProcessError


class MiteSh:
    """
    A class used to run a single line shell script and yield its output 
    line by line.


    Attributes
    ----------
    command : str
        a shell script one line command or one line group of commands
    sh_tmp_base : str
        the temporary base directory to hold several command files [/tmp/mitesh]
    sh_type : str
        the type of shell script given in command [bash]
    command_file_overwrite : bool
        the flag for shell script file overwrite (set False for performaance) [True]

    Methods
    -------
    execute()
        Execute the given command and yields its output line by line
    """

    gsh_tmp_base = environ.get('MITESH_TMP_BASE', '/tmp/mitesh')
    gsh_lines = {
            "bash": {
                "entrypoint": '#!/usr/bin/env bash',
                "exit": 'exit $?'
            },
            "sh": {
                "entrypoint": '#!/usr/bin/env sh',
                "exit": 'exit $?'
            },
            "zsh": {
                "entrypoint": '#!/usr/bin/env zsh',
                "exit": 'exit $?'
            }
        }
    gsh_type = "bash"
    gcommand_file_overwrite = True


    def __init__(self, command:str, sh_tmp_base=gsh_tmp_base, 
            sh_type=gsh_type, command_file_overwrite=gcommand_file_overwrite):
        """
        Parameters
        ----------
        command : str
            a shell script one line command or one line group of commands
        sh_tmp_base : str
            the temporary base directory to hold several command files [/tmp/mitesh]
        sh_type : str
            the type of shell script given in command [bash]
        command_file_overwrite : bool
            the flag for shell script file overwrite (set False for performaance) [True]

        Raises
        ------
        PermissionError
            When there is permission denied on sh_tmp_base
        """

        self.command = command
        self.sh_tmp_base = sh_tmp_base
        self.sh_type = sh_type
        self.command_file_overwrite = command_file_overwrite
        #self.check_and_create_dir(self.sh_tmp_base)
        self.command_hash = self.get_command_hash()
        try:
            self.command_file = self.check_and_create_command_file()
            self.pipe = self._run()
        except PermissionError as e:
            raise PermissionError(e)
        except Exception as e:
            raise Exception(e)

    def check_and_create_dir(self, dir):
        try:
            if not path.isdir(dir):
                makedirs(dir, exist_ok=True)
        except PermissionError as e:
            raise PermissionError(e, f"Please check write permissions of dir {dir}")


    def get_command_hash(self):
        return sha256(self.command.encode('utf-8')).hexdigest()


    def check_and_create_command_file(self):
        command_dir = path.sep.join([self.sh_tmp_base, self.command_hash[0:2]])
        command_file = path.sep.join([command_dir, self.command_hash[2:]]) + ".sh"
        try:
            self.check_and_create_dir(command_dir)
            if not self.command_file_overwrite and path.isfile(command_file):
                print(f"Ignoring already created command_file {command_file}")
                return command_file

            with open(command_file, "w") as cfh:
                cfh.write(MiteSh.gsh_lines[self.sh_type]['entrypoint'])
                cfh.write(linesep)
                cfh.write(self.command)
                cfh.write(linesep)
                cfh.write(MiteSh.gsh_lines[self.sh_type]['exit'])
                cfh.write(linesep)
            st = stat(command_file)
            chmod(command_file, st.st_mode | S_IEXEC)
            return command_file
        except PermissionError as e:
            raise PermissionError(e, f"Please check write permissions of file {command_file}")


    def _run(self):
        return Popen([str(self.command_file)], stdout=PIPE, universal_newlines=True)


    def execute(self):
        """Executes the given command and yields its output line by line


        Parameters
        ----------

        Raises
        ------
        CalledProcessError
            If any error (shell exit_code != 0) occurred during execution of the 
            command.
        """
        #return self.pipe.communicate()[0].decode('utf-8').split(linesep)[:-1]
        for stdout_line in iter(self.pipe.stdout.readline, ""):
            yield stdout_line.rstrip()
        self.pipe.stdout.close()
        return_code = self.pipe.wait()
        if return_code:
            raise CalledProcessError(return_code, self.command)




if __name__ == '__main__':
    #mitesh = MiteSh("cat /proc/cpuinfo | grep -c processor", sh_tmp_base='/tmp/mitesh')
    try:
        mitesh = MiteSh("echo 1; sleep 1; echo1 2; sleep 1; echo 3; exit -1", sh_tmp_base='/tmp/mitesh')
        for x in mitesh.execute():
            print(f"GOT {x}")
    except PermissionError as e:
        print(f"Permission Error: {e}")
    except CalledProcessError as e:
        print(f"Execution Error: {e}")
    except Exception as e:
        print(f"Some other exception occurred: {e}")

