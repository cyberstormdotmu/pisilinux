from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Bluetooth Service",
                 "tr": "Bluetooth Hizmeti"})
serviceDefault = "on"

PIDFILE="/run/bluez.pid"
DAEMON ="/usr/libexec/bluetooth/bluetoothd"

@synchronized
def start():
  
    startService(command=DAEMON,
                 pidfile=PIDFILE,
                 detach=True,
                 donotify=True)
    
    os.system("pidof bluez + /usr/libexec/bluetooth/bluetoothd > /run/bluez.pid")
    
@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except:
        pass

def status():
    return isServiceRunning(pidfile=PIDFILE)
