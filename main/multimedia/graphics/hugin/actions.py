#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build") 
    
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
                          -DENABLE_LAPACK=yes", sourceDir="..")

def build():
    shelltools.makedirs("build")
    shelltools.cd("build") 
    
    cmaketools.make()

def install():
    shelltools.makedirs("build")
    shelltools.cd("build") 
    
    cmaketools.rawInstall('DESTDIR="%s"' % get.installDIR())
    
    shelltools.cd("..")

    pisitools.dodoc("AUTHORS", "README", "TODO")
