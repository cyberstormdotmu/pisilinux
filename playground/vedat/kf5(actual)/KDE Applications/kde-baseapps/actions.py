#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # pisitools.ldflags.add("-Wl,-rpath")
    
    shelltools.system("sed -i -e 's|add_subdirectory(dolphin)|#add_subdirectory(dolphin)|' CMakeLists.txt")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DQT_PLUGIN_INSTALL_DIR=lib/qt5/plugins \
                          -DLOCALE_INSTALL_DIR=/usr/share/locale \
                          -DLIB_INSTALL_DIR=lib \
                          -DPYTHON_EXECUTABLE=/usr/bin/python3 \
                          -DBUILD_TESTING=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.install()
    
    pisitools.dodoc("README", "COPYING.LIB")
