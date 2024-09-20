#!/usr/bin/env python3

import os.path
import subprocess as sp
import sys
from src import detect_os

INSTALLER_DIR: str = os.path.dirname(os.path.abspath(__file__))
IS_EFI: bool = os.path.exists("/sys/firmware/efi")
USE_OTHER_ISO:str = "" # e.g. "arch" if using Arch iso to install different OS like Fedora # TODO remove

try: # if using iso to install another OS, two extra args should be passed
    if IS_EFI:
        args:list[str] = list(sys.argv[0:4]) # just first 3 arguments (exclude distro arguments)
        distro:str = sys.argv[4]
        distro_name:str = sys.argv[5]
    else:
        args: list[str] = list(sys.argv[0:3]) # just first 2 arguments (exclude distro arguments)
        distro: str = sys.argv[3]
        distro_name:str = sys.argv[4]
except IndexError:
    distro:str = detect_os.get_distro_id()
    distro_name:str = detect_os.get_distro_name()

if distro:
    if USE_OTHER_ISO != "":
        distro_for_prep: str = USE_OTHER_ISO
    else:
        distro_for_prep: str = distro
#    try: # CAUTION: comment lines 30-37 & unindent line 38 if prepared manually
#        if IS_EFI:
#            sp.check_output([f'./src/prep/{distro_for_prep}_live.sh', f'{args[1]}', f'{args[2]}', f'{args[3]}']) # type: ignore
#        else:
#            sp.check_output([f'./src/prep/{distro_for_prep}_live.sh', f'{args[1]}', f'{args[2]}']) # type: ignore
#    except sp.CalledProcessError as e:
#        print(f"F: There was an error in prep steps! {e.output.decode('utf-8')}")
#    else:
    __import__(f"src.distros.{distro}.installer")
else:
    print("F: Distribution could not be detected!")

