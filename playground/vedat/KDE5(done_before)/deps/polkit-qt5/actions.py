#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir = "polkit-qt-1-%s" % (get.srcVERSION())

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
                          -DUSE_QT5=ON \
                          -DUSE_QT4=OFF")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "README*", "TODO")
