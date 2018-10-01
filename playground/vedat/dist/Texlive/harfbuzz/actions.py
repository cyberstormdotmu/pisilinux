#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    options = "\
               --prefix=/usr \
               --includedir=/usr/include \
               --disable-static \
               --disable-silent-rules \
               --with-graphite2=yes \
               --enable-dependency-tracking \
              "
    if get.buildTYPE() == "emul32":
        options += "\
                    --with-graphite2=no \
                    --without-cairo \
                   "
    autotools.configure(options)
    
    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")