#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get


def setup():
    libtools.libtoolize()
    autotools.aclocal("-I m4")
    #autotools.autoreconf("-vi")
    autotools.configure()

def build():
    autotools.make()

#def check():
#    autotools.make("-j1 test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS","INSTALL","NEWS","README","THANKS" )
