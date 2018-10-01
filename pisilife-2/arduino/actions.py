#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools


def install():
    pisitools.insinto("/usr/share/arduino-1.8.1", "*") 
    pisitools.dosym("/usr/share/arduino-1.8.1/arduino", "/usr/bin/arduino")
