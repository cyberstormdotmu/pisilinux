#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
  
    #shelltools.cd("%s/" % get.workDIR())
    #pisitools.dosym("./Makefile", "Makefile")
    autotools.make("V=1 CC=%s CFLAGS=\"%s\"" % (get.CC(), get.CFLAGS()))
    autotools.make("V=1 CC=%s CFLAGS=\"%s\" btrfs-select-super" % (get.CC(), get.CFLAGS()))

def install():
  
    #shelltools.cd("%s/" % get.workDIR())
    autotools.rawInstall("prefix=/usr DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/lib/*.a")

    pisitools.insinto("/usr/bin", "bcp", "btrfs-bcp")
    pisitools.insinto("/usr/bin", "show-blocks", "btrfs-show-blocks")
    
    pisitools.dodoc("COPYING")
   