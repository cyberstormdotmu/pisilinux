#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools

def setup():
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DECM_MKSPECS_INSTALL_DIR=/usr/lib/qt5/mkspecs/modules \
                          -DLIB_INSTALL_DIR=lib \
                          -DPYTHON_EXECUTABLE=/usr/bin/python3 \
                          -DBUSMENUQT_INCLUDE_DIR=/usr/include/dbusmenu-qt5 \
                          -DBUILD_TESTING=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.dodoc("README.md", "COPYING.LIB", "COPYING-CMAKE-SCRIPTS")
