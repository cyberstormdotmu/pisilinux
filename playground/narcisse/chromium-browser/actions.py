#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

pisitools.flags.add("-fno-stack-protector")
pisitools.flags.remove("-fstack-protector")
pisitools.cxxflags.add("-std=gnu++14 -fpermissive")

def setup():

    shelltools.export("LC_ALL", "C")
    shelltools.system("sed -i 's|icu)|icu-i18n)|g' build/linux/system.gyp")
    shelltools.system("export -n CFLAGS CXXFLAGS")
    #shelltools.touch(get.workDIR() + "/chromium-48.0.2564.97/chrome/test/data/webui/i18n_process_css_test.html")
    
    options = "\
               -Drelease_extra_cflags='%s' \
               -Duse_system_expat=1 \
               -Duse_system_flac=1 \
               -Duse_system_ffmpeg=0 \
               -Duse_system_fontconfig=1 \
               -Duse_system_harfbuzz=1 \
               -Duse_system_icu=0 \
               -Duse_system_jsoncpp=1 \
               -Duse_system_libevent=1 \
               -Duse_system_libjpeg=0 \
               -Duse_system_libpng=0 \
               -Duse_system_libsrtp=0 \
               -Duse_system_libusb=0 \
               -Duse_system_libxnvctrl=0 \
               -Duse_system_libxslt=1 \
               -Duse_system_libvpx=0 \
               -Duse_system_libwebp=1 \
               -Duse_system_libwebm=0 \
               -Duse_system_minizip=1 \
               -Duse_system_opus=1 \
               -Duse_system_snappy=1 \
               -Duse_system_speex=1 \
               -Duse_system_zlib=1 \
               -Duse_system_bzip2=1 \
               -Duse_system_nspr=1 \
               -Duse_system_ssl=0 \
               -Duse_system_yasm=1 \
               -Duse_system_libva=0 \
               -Duse_gtk3=1 \
               -Duse_gconf=0 \
               -Duse_sysroot=0 \
               -Denable_hangout_services_extension=1 \
               -Dlogging_like_official_build=1 \
               -Dtracing_like_official_build=1 \
               -Dfieldtrial_testing_like_official_build=1 \
               -Dremove_webcore_debug_symbols=1 \
               -Dffmpeg_branding=Chrome \
               -Dproprietary_codecs=1 \
               -Denable_widevine=1 \
               -Denable_pepper_cdms=1 \
               -Dclang=0 \
               -Dhost_clang=0 \
               -Duse_bundled_clang=0 \
               -Dclang_use_chrome_plugins=0 \
               -Duse_ccache=0 \
               -Dlinux_use_bundled_gold=0 \
               -Dlinux_use_bundled_binutils=0 \
               -Dlinux_use_gold_flags=0 \
               -Dlinux_link_gsettings=1 \
               -Dlinux_link_kerberos=1 \
               -Dlinux_link_libbrlapi=1 \
               -Dlinux_link_libgps=1 \
               -Dlinux_link_libpci=1 \
               -Dlinux_link_libspeechd=1 \
               -Dlinux_link_pulseaudio=1 \
               -Dlibspeechd_h_prefix=speech-dispatcher/ \
               -Dwerror= \
               -Ddisable_fatal_linker_warnings=1 \
               -Ddisable_nacl=0 \
               -Ddisable_newlib_untar=0 \
               -Ddisable_pnacl=0 \
               -Ddisable_sse2=1 \
               -Ddisable_glibc=1 \
               -Dtarget_arch=x64 \
               -Dpython_arch=x64 \
               -Dlinux_sandbox_chrome_path=/usr/lib/chromium-browser/chromium-browser \
               -Dlinux_sandbox_path=/usr/lib/chromium-browser/chromium-sandbox \
               -Dusb_ids_path=/usr/share/misc/usb.ids \
               -Dgoogle_api_key=AIzaSyBINKL31ZYd8W5byPuwTXYK6cEyoceGh6Y \
               -Dgoogle_default_client_id=879512332529.apps.googleusercontent.com \
               -Dgoogle_default_client_secret=RmQPJJeL1cNJ8iETnoVD4X17 " %(get.CFLAGS())
   
    shelltools.system("build/linux/unbundle/replace_gyp_files.py  %s" % options)
   
    shelltools.export("GYP_GENERATORS","ninja")
    shelltools.system("build/gyp_chromium build/all.gyp --depth=. %s" % options)
    
    shelltools.system("python build/download_nacl_toolchains.py --packages nacl_x86_newlib,pnacl_newlib,pnacl_translator sync --extract")
    
  
def build():
    
    shelltools.system("ninja -C out/Release chrome")
    shelltools.system("ninja -C out/Release chrome_sandbox")
    shelltools.system("ninja -C out/Release chromedriver")
    shelltools.system("ninja -j8 -C out/Release widevinecdmadapter")
    shelltools.system("ninja -j8 -C out/Release clearkeycdm")
    
def install():
	
    pisitools.dosed("out/Release/xdg-settings", "xdg-mime", "/usr/lib/chromium-chromium-browser/xdg-mime")
    shelltools.makedirs("%s/usr/lib/chromium-browser" % get.installDIR())
  
    shelltools.cd("out/Release")
    
    binaries_for_inst=["chrome", "chrome_sandbox", "chromedriver", "natives_blob.bin", "snapshot_blob.bin", "nacl_helper", "nacl_helper_nonsfi", "nacl_helper_bootstrap", "nacl_irt_x86_64.nexe", "icudtl.dat", "bro", "chrome-wrapper", "tls_edit"]
    
    libraries_for_inst=["libclearkeycdm.so", "libwidevinecdmadapter.so", "libwidevinecdm.so", "libyuv.a", "xdg-mime", "xdg-settings"]

   
    # install and strip binaries
    for mybin in binaries_for_inst:
        pisitools.insinto("/usr/lib/chromium-browser", mybin)
       
    # install and strip shared libs  
    for mylib in libraries_for_inst:
        pisitools.insinto("/usr/lib/chromium-browser", mylib)
         
    pisitools.dosym("/usr/lib/chromium-browser/chrome", "/usr/lib/chromium-browser/chromium-browser")
    pisitools.rename("/usr/lib/chromium-browser/chrome_sandbox", "chrome-sandbox")
    shelltools.chmod("%s/usr/lib/chromium-browser/chrome-sandbox" % get.installDIR(), 04755)
    
     # install rest of needed files
    pisitools.insinto("/usr/lib/chromium-browser", "*.pak")
    pisitools.insinto("/usr/lib/chromium-browser", "*.json")
    pisitools.insinto("/usr/lib/chromium-browser", "locales")
    pisitools.insinto("/usr/lib/chromium-browser", "pseudo_locales")
    pisitools.insinto("/usr/lib/chromium-browser", "resources")
    
    pisitools.newman("chrome.1", "chromium-browser.1")
    
    shelltools.cd("../..")
    for size in ["22", "24", "48", "64", "128", "256"]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" %(size, size), "chrome/app/theme/chromium/product_logo_%s.png" % size, "chromium-browser.png")
   		
    pisitools.dosym("/usr/share/icons/hicolor/256x256/apps/chromium-browser.png", "/usr/share/pixmaps/chromium-browser.png")
    
    pisitools.dodoc("LICENSE")


    
