#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2016 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#shelltools.export("GOPATH", "%s" % get.curDIR())
shelltools.export("DOCKER_BUILDTAGS","seccomp")
shelltools.export("COMMIT","4fc53a8")
shelltools.export("BINDIR","/usr/bin")

def setup():
    shelltools.cd("%s" % get.workDIR())
    shelltools.move("runc-*", "runc")
    
    shelltools.cd("runc")
    shelltools.move("vendor", "src")
    
    shelltools.makedirs("src/github.com/opencontainers")
    shelltools.cd("src/github.com/opencontainers")
    
    shelltools.system("ln -rsf %s/runc ./runc" % get.workDIR())
    
def build():
    shelltools.cd("%s/runc/src/github.com/opencontainers/runc" % get.workDIR())
    
    build_runc = "GOPATH=%s/runc make COMMIT=4fc53a8" % get.workDIR()

    shelltools.system(build_runc)

def install():
    pisitools.dobin("runc")
    
    # symlink containerd/run (nice integration with docker)
    pisitools.dosym("/usr/bin/runc", "/usr/bin/docker-runc")
    
    #insert completions in doc
    #pisitools.insinto("/usr/share/doc/runc", "contrib")
     
    pisitools.dodoc("MAINTAINERS", "README*")
