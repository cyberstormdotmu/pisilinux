#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kde4

def setup():
    shelltools.system("./initrepo.sh") 
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()
