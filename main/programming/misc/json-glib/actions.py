#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def setup():
    options = "-Ddocs=false \
               -Dintrospection=true \
              "
               
    if get.buildTYPE() == "_emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/usr/lib32/bin \
                     --sbindir=/usr/lib32/sbin \
                     --datadir=/usr/lib32/share \
                     --datarootdir=/usr/lib32/share \
                     --libexecdir=/usr/lib32/libexec \
                     --localedir=/usr/lib32/share/locale \
                   "
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("CXX", "%s -m32" % get.CXX())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    
    
    if get.buildTYPE() == "_emul32":
        pisitools.removeDir("usr/lib32/bin")
        pisitools.removeDir("usr/lib32/libexec")
        pisitools.removeDir("usr/lib32/share")
        #pisitools.removeDir("usr/libexec")
        
        #pisitools.removeDir("/usr/share/gtk-doc")

        pisitools.dodoc("README.md", "NEWS")
