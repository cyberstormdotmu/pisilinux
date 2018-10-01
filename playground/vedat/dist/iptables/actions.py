#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--prefix=/usr \
                         --sbindir=/usr/sbin \
                         --libexecdir=/usr/libexec \
                         --enable-devel \
                         --without-kernel \
                         --enable-libipq \
                         --enable-shared ")

def build():
    autotools.make("V=1")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.insinto("/usr/include", "include/iptables.h")
    pisitools.insinto("/usr/include", "include/ip6tables.h")
    pisitools.insinto("/usr/include/libiptc", "include/libiptc/*.h")

    pisitools.dodir("/var/lib/iptables")
    pisitools.dodir("/etc/iptables")
    