#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import kde5

def setup():
    cmaketools.configure("-DKDE_INSTALL_USE_QT_SYS_PATHS=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.install()

    pisitools.dodoc("COPYING", "INSTALL", "README")
