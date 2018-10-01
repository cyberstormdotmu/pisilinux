#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure(" --disable-static \
                          --enable-shared \
                          --with-libguile=/usr/lib/guile/ \
                          --with-guile-ver=2.0.11")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("usr/share/pkgconfig/", "/usr/lib/")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "THANKS", "TODO", "VERSION")
