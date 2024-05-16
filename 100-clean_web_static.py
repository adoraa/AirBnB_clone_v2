#!/usr/bin/python3
"""
Fabric script that cleans up the local archives and the web servers
"""
import os
from fabric.api import env, sudo, local
env.hosts = ['54.234.97.54', '100.25.190.116']


def do_clean(number=0):
    """Function to clean up archives"""
    number = int(number)
    if number == 0:
        number = 1
    number += 1
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
