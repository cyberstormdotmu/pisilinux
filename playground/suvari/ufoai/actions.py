#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ufoai-%s-source" % get.srcVERSION()
datadir = "/usr/share/ufoai"
exefiles = ["ufo", "ufo2map", "ufoded"]

def setup():
    shelltools.export("CFLAGS", "%s -lpthread -mmmx -msse" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -lpthread -mmmx -msse" % get.CXXFLAGS())
    shelltools.export("LDFLAGS", "%s -lpthread -mmmx -msse" % get.LDFLAGS())

    shelltools.makedirs("base")
    shelltools.system("./configure --prefix=/usr \
                       --bindir=/usr/bin \
                       --datadir=/usr/share/ufoai \
                       --localedir=/usr/share/locale \
                       --enable-release \
                       --enable-sse \
                       --enable-cgame-campaign \
                       --enable-cgame-multiplayer \
                       --enable-cgame-skirmish \
                       --enable-game \
                       --enable-memory \
                       --enable-testall \
                       --enable-ufo2map \
                       --enable-ufoded \
                       --enable-ufo \
                       --enable-ufomodel \
                       --disable-uforadiant \
                       --enable-ufoslicer")

def build():
    autotools.make()
    autotools.make("lang")

def install():
    pisitools.insinto(datadir, "base")

    for f in exefiles:
        pisitools.dobin(f)

    pisitools.dodoc("COPYING", "README")

