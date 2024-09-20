#!/usr/bin/env python3
# Detect OS/distro ID or name

import os

def get_distro_id(path_prepend: str = "") -> str:
    """
    Detect OS/distro ID.

    :param str path_prepend: The root folder prefix. Defaults to None.
    :return: The ID of the OS or distro.
    """
    distro_id: str | None = None
    while distro_id == None:
        if os.path.exists(f"{path_prepend}/etc/lsb-release"):
            with open(f"{path_prepend}/etc/lsb-release", "r") as temp:
                for line in temp.readlines():
                    if line.startswith("DISTRIB_ID="):
                        distro_id = line.split('=')[1].lower().strip()
                        break
        if os.path.exists(f"{path_prepend}/etc/os-release"):
            with open(f"{path_prepend}/etc/os-release", "r") as temp:
                for line in temp.readlines():
                    if line.startswith("ID="):
                        distro_id = line.split('=')[1].lower().strip()
                        break
        # otherwise loop through all files in /etc and check for "-release"
        for etcf in os.listdir("/etc"): # depth=1, hopefully just 1 file matches
            if etcf.endswith("-release") and etcf not in ("os-release", "lsb-release"):
                distro_id = etcf.split('-')[0]
                break
    return distro_id

def get_distro_name(path_prepend: str = "") -> str:
    """
    Detect OS/distro name.

    :param str path_prepend: The root folder prefix. Defaults to None.
    :return str distro_name: The name of the OS or distro.
    """
    distro_name: str | None = None
    while distro_name == None:
        if os.path.exists(f"{path_prepend}/etc/lsb-release"):
            with open(f"{path_prepend}/etc/lsb-release", "r") as temp:
                for line in temp.readlines():
                    if line.startswith("DISTRIB_DESCRIPTION="):
                        distro_name = line.split('=')[1].strip()
                        break
        if os.path.exists(f"{path_prepend}/etc/os-release"):
            with open(f"{path_prepend}/etc/os-release", "r") as temp:
                for line in temp.readlines():
                    if line.startswith("NAME="):
                        distro_name = line.split('=')[1].strip()
                        break
        # Last resort loop through all files in /etc and check for "-release"
        for etcf in os.listdir("/etc"):
            if etcf.endswith("-release") and etcf not in ("os-release", "lsb-release"):
                distro_name = etcf.split('-')[0].capitalize()
                break
    return distro_name
