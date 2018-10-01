# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("pyqt5")

    shelltools.system("python config.py")

    

def build():
    shelltools.cd("pyqt5")
    autotools.make()

def install():
    shelltools.cd("pyqt5")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README.md")

 
