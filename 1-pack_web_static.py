#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    must return the archive path if the archive has been correctly
    generated. Otherwise, it should return None
    """
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        rout = "versions/web_static_{}.tgz".format(date)
        _gzip = local("tar -cvzf {} web_static".format(rout))
        return rout
    except Exception:
        return None
