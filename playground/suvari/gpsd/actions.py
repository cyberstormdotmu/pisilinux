#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import scons
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())
    shelltools.export("CPPFLAGS", get.CXXFLAGS())
    shelltools.export("CXXFLAGS", get.CXXFLAGS())
    shelltools.export("CFLAGS",  get.CFLAGS())
    shelltools.export("LDFLAGS", get.LDFLAGS())

def build():
    scons.make("\
                systemd=no \
                dbus_export=yes \
                debug=yes \
                python=False \
                libQgpsmm=no \
                nostrip=True \
                gpsd_user=gpsd \
                gpsd_group=dialout")

    shelltools.system("sed -i 's/sbin/bin/g' comar/*.service")


def install():
    shelltools.system("sed -i 's|.so gps.1|.so man1/gps.1|' cgps.1 lcdgps.1 xgps.1 xgpsspeed.1")
    scons.install()

    # We're using conf.d instead of sysconfig
    pisitools.dosed("gpsd.hotplug.wrapper", "sysconfig\/", "conf.d/")

    # Install UDEV files
    pisitools.insinto("/lib/udev/rules.d", "gpsd.rules", "99-gpsd.rules")
    pisitools.dobin("gpsd.hotplug", "/lib/udev")
    pisitools.dobin("gpsd.hotplug.wrapper", "/lib/udev")

    # Fix permissions
    shelltools.chmod("%s/usr/lib/%s/site-packages/gps/gps.py" % (get.installDIR(), get.curPYTHON()))

    pisitools.dodoc("README", "TODO", "AUTHORS", "COPYING")
