#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""

from fabric.api import *
import os.path import exists

env.hosts = ['54.234.97.54', '100.25.190.116']
env.user = "ubuntu"


def do_deploy(archive_path):
    """
        Distribute archive.
    """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))
        return True
    except:
        return False
