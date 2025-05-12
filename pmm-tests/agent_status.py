def verify_command(command):
    """
    Executes shell specified command and return the console output.
    If the exit code was non-zero it raises a CalledProcessError.

    :param  command:    shell command string to execute
    :type   command:    str
    :return:            command console output
    :rtype:             str
    :raises:            a CalledProcessError if the exit code was non-zero.
    """
    from tempfile import TemporaryFile
    with TemporaryFile() as output:
        return subprocess.check_output(command, shell=True, universal_newlines=True, stderr=output).rstrip()

if __name__ == '__main__':
    print(verify_command('pmm-admin list'))