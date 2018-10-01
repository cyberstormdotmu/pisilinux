#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.insinto("%s/share/proj" % get.defaultprefixDIR(), "nad/test*")
    #pisitools.insinto("%s/share/proj" % get.defaultprefixDIR(), "nad/pj_out*.dist")

    #pisitools.dodoc("nad/README.NAD", "nad/README.NADUS")
