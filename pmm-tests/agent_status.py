import argparse
import os
import subprocess
import sys
import unittest

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
    errors = []
    listResponse = verify_command("pmm-admin list")
    for line in listResponse.split("Port")[1].strip().splitlines():
        if "pmm_agent" in line:
            if "connected" not in line.lower():
                errors.append(f"pmm_agent status should be 'Connected' but is: {line}")
        else:
            if "running" not in line.lower():
                errors.append(f"pmm_agent status should be 'Running' but is: {line}")

    if errors:
        raise ValueError('\n'.join(errors))

