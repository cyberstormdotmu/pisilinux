#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
	autotools.make()
		
def install():
	pisitools.insinto("/usr/bin", "greed")
	pisitools.doman("greed.6")
	pisitools.dodoc ("COPYING", "README")
	shelltools.makedirs("%s/var/games/greed" % get.installDIR())
