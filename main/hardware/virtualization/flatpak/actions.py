#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2018 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.system("NOCONFIGURE=1 ./autogen.sh")
    
    autotools.configure("--with-priv-mode=setuid \
                         --enable-xauth \
                         --with-system-bubblewrap \
                         --enable-docbook-docs \
                         --disable-static \
                         --enable-sandboxed-triggers")
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.dodoc("AUTHORS", "ChangeLog", "README*", "NEWS")
