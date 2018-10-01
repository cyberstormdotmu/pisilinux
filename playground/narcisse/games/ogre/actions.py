#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("--enable-cg --disable-devil --enable-openexr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("Docs/*.html")
    pisitools.dohtml("Docs/*.gif")

    for dirs in ("Docs/api", "Docs/manual",  "Docs/vbo-update"):
        shelltools.copytree(dirs, "%s/%s/%s/html" % (get.installDIR(), get.docDIR(), get.srcNAME()))

    pisitools.dodoc("AUTHORS", "BUGS", "COPYING", \
                    "README", "Docs/shadows/OgreShadows.pdf", \
                    "Docs/licenses/*.txt")
