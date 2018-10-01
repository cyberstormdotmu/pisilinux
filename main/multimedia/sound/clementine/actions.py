#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("sed -i 's|lastfm5/ws.h|lastfm/ws.h|g' CMakeLists.txt")
    shelltools.system("sed -i 's|lastfm5/Track.h|lastfm/Track.h|g' CMakeLists.txt")
    shelltools.system("sed -i 's|<lastfm5/|<lastfm/|g' src/internet/lastfm/lastfmcompat.h")
    shelltools.system("sed -i 's|<lastfm5/|<lastfm/|g' src/internet/lastfm/lastfmservice.cpp")
    shelltools.system("sed -i 's|<lastfm5/|<lastfm/|g' src/internet/lastfm/lastfmsettingspage.cpp")
    shelltools.system("sed -i 's|<lastfm5/Track.h>|<lastfm/Track.h>|g' src/core/song.cpp")
    shelltools.system("sed -i 's|Exec=clementine %U|Exec=clementine|g' dist/clementine.desktop")
    cmaketools.configure(" \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DENABLE_VK=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("Changelog", "COPYING")
