#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

def setup():
    qt5.configure("librecad.pro")

def build():
    qt5.make()

    shelltools.cd("plugins")
    qt5.configure("plugins.pro")
    qt5.make("-j4")

def install():
    pisitools.dobin("unix/librecad")
     
    pisitools.insinto("/usr/share/librecad/fonts/", "unix/resources/fonts/*")
    pisitools.insinto("/usr/share/librecad/library/", "unix/resources/library/*")
    pisitools.insinto("/usr/share/librecad/patterns/", "unix/resources/patterns/*")
    pisitools.insinto("/usr/share/librecad/qm/", "unix/resources/qm")
    pisitools.insinto("/usr/share/librecad/plugins/", "unix/resources/plugins/*")
    pisitools.dodoc("README.md", "gpl-2.0.txt")
     
     

