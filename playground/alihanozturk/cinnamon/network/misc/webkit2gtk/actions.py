#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

paths = ["JavaScriptCore", "WebCore", "WebKit", "WebKit2"]
docs = ["AUTHORS", "COPYING.LIB", "THANKS", \
        "LICENSE-LGPL-2", "LICENSE-LGPL-2.1", "LICENSE"]

def setup():
    shelltools.system("rm -r Source/ThirdParty/gtest/")
    shelltools.system("rm -r Source/ThirdParty/qunit/")
    cmaketools.configure("-DPORT=GTK \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DCMAKE_INSTALL_PREFIX=/usr \
                          -DLIB_INSTALL_DIR=/usr/lib \
                          -DLIBEXEC_INSTALL_DIR=/usr/lib/webkit2gtk-4.0 \
                          -DUSE_LIBHYPHEN=OFF         \
                          -DENABLE_MINIBROWSER=ON")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("NEWS")
    shelltools.cd("Source")
    for path in paths:
        for doc in docs:
            if shelltools.isFile("%s/%s" % (path, doc)):
                pisitools.insinto("%s/%s/%s" % (get.docDIR(), get.srcNAME(), path),
                                  "%s/%s" % (path, doc))
