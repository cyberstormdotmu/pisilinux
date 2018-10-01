#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    kde4.configure("-DCMAKE_BUILD_TYPE=Release -DCMAKE_VERBOSE_MAKEFILE=ON")

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dodoc("LICENCE", "README.md")
