#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import kde4

import os

WorkDir = "qt-everywhere-opensource-src-%s" % get.srcVERSION()
absoluteWorkDir = "%s/%s" % (get.workDIR(), WorkDir)

bindirQt5="/usr/lib/qt5/bin"

def setup():
    checkdeletepath="%s/qtbase/src/3rdparty"  % absoluteWorkDir
    for dir in ('libjpeg', 'freetype', 'libpng', 'zlib', "xcb", "sqlite"):
        if os.path.exists(checkdeletepath+dir):
            shelltools.unlinkDir(checkdeletepath+dir)

    filteredCFLAGS = get.CFLAGS().replace("-g3", "-g")
    filteredCXXFLAGS = get.CXXFLAGS().replace("-g3", "-g")

    vars = {"PISILINUX_CC" :       get.CC() + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "PISILINUX_CXX":       get.CXX() + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "PISILINUX_CFLAGS":    filteredCFLAGS + (" -m32" if get.buildTYPE() == "emul32" else ""),
            "PISILINUX_LDFLAGS":   get.LDFLAGS() + (" -m32" if get.buildTYPE() == "emul32" else "")}

    shelltools.export("CFLAGS", filteredCFLAGS)
    shelltools.export("CXXFLAGS", filteredCXXFLAGS)
    #check that dosed commands without releated patches

    if not get.buildTYPE() == "emul32":
        #-no-pch makes build ccache-friendly
        options = "-v \
                   -prefix /usr \
                   -libdir /usr/lib \
                   -bindir /usr/bin \
                   -headerdir /usr/include \
                   -plugindir /usr/lib/qt5/plugins \
                   -importdir /usr/lib/qt5/imports \
                   -datadir /usr/share/qt5 \
                   -docdir /usr/share/doc/qt5 \
                   -libexecdir /usr/libexec \
                   -translationdir /usr/share/qt5/translations \
                   -sysconfdir /etc \
                   -archdatadir /usr/lib/qt5 \
                   -confirm-license \
                   -opensource \
                   -optimized-qmake \
                   -nomake tests \
                   -release \
                   -shared \
                   -accessibility \
                   -dbus-linked \
                   -fontconfig \
                   -glib \
                   -gtkstyle \
                   -icu \
                   -c++11 \
                   -system-harfbuzz \
                   -openssl-linked \
                   -system-libjpeg \
                   -system-libpng \
                   -system-sqlite \
                   -system-zlib \
                   -plugin-sql-sqlite \
                   -plugin-sql-odbc \
                   -plugin-sql-psql \
                   -no-sql-ibase \
                   -no-sql-tds \
                   -no-rpath \
                   -no-mtdev \
                   -no-sql-db2 \
                   -no-sql-oci \
                   -no-pch \
                   -I/usr/include/firebird/ \
                   -I/usr/include/postgresql/server/ \
                   -no-separate-debug-info \
                   -no-strip " 
                   
                   
    else:
        pisitools.dosed("qtbase/mkspecs/linux-g++-64/qmake.conf", "-m64", "-m32")
        shelltools.export("LDFLAGS", "-m32 %s" % get.LDFLAGS())
        options = "-no-pch \
                   -v \
                   -prefix /usr \
                   -libdir /usr/lib32 \
                   -plugindir /usr/lib32/qt5/plugins \
                   -importdir /usr/lib32/qt5/imports \
                   -datadir /usr/share/qt5 \
                   -translationdir /usr/share/qt5/translations \
                   -sysconfdir /etc \
                   -system-sqlite \
                   -system-harfbuzz \
                   -system-libjpeg \
                   -system-libpng \
                   -system-zlib \
                   -nomake tests \
                   -openssl-linked \
                   -nomake examples \
                   -nomake tools \
                   -optimized-qmake \
                   -no-rpath \
                   -no-strip \
                   -no-mtdev \
                   -no-sql-db2 \
                   -no-sql-oci \
                   -no-sql-odbc \
                   -no-sql-ibase \
                   -no-sql-psql \
                   -no-sql-sqlite \
                   -no-sql-sqlite2 \
                   -no-sql-tds \
                   -no-sql-mysql \
                   -dbus-linked \
                   -no-openvg \
                   -confirm-license \
                   -reduce-relocations  \
                   -opensource "

    autotools.rawConfigure(options)

def build():
    shelltools.export("LD_LIBRARY_PATH", "%s/lib:%s" % (get.curDIR(), get.ENV("LD_LIBRARY_PATH")))
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    
    shelltools.export("LD_LIBRARY_PATH", "%s/usr/lib" % get.installDIR())
    mkspecPath = "/usr/lib/qt5/mkspecs"

    for root, dirs, files in os.walk("%s/usr/lib/qt5" % get.installDIR()):
        # Remove unnecessary spec files..
        if root.endswith(mkspecPath):
            for dir in dirs:
                if not dir.startswith("linux") and dir not in ["common","qws","features","default"]:
                    pisitools.removeDir(os.path.join(mkspecPath,dir))
        for name in files:
            if name.endswith(".prl"):
                pisitools.dosed(os.path.join(root, name), "^QMAKE_PRL_BUILD_DIR.*", "")

    
    pisitools.dodoc("LGPL_EXCEPTION.txt", "LICENSE.*")





