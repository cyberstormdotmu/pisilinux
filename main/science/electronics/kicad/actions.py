#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("Release")
    shelltools.cd("Release") 
    cmaketools.configure("-DKICAD_STABLE_VERSION=ON     \
                          -DKICAD_REPO_NAME=stable      \
                          -DCMAKE_BUILD_TYPE=Release    \
                          -DCMAKE_INSTALL_PREFIX=/usr   \
                          -DKICAD_SKIP_BOOST=ON         \
                          -DKICAD_SCRIPTING=ON          \
                          -DKICAD_SCRIPTING_MODULES=ON  \
                          -DBUILD_GITHUB_PLUGIN=ON", sourceDir="..")
    
    shelltools.cd("..")
    shelltools.cd("kicad-i18n-4.0.7")
    shelltools.makedirs("Release")
    shelltools.cd("Release")
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr \
                          -DKICAD_I18N_UNIX_STRICT_PATH=ON", sourceDir="..")
    shelltools.cd("..")

def build():
    shelltools.cd("Release")
    cmaketools.make()
    shelltools.cd("..")
    shelltools.cd("kicad-i18n-4.0.7")
    shelltools.cd("Release")
    cmaketools.make()
    shelltools.cd("..")

def install():
    shelltools.cd("Release")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    shelltools.cd("kicad-i18n-4.0.7")
    shelltools.cd("Release")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #shelltools.cd("..")

    #pisitools.dodoc("AUTHORS*", "CHANGELOG*", "README*")
