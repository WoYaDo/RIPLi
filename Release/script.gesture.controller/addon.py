import time
import struct
import myo as libmyo; libmyo.init()
import time
import sys
import urllib2
import Queue
import threading

import xbmc, xbmcgui, xmbcaddon

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
 


# Send commands to Kodi
def executeCommand(method):
    start = 'http://localhost:8080/jsonrpc?request={"jsonrpc":%20"2.0",%20"id":%201,%20"method":%20"'
    end = '"}'
    url = start + method + end
    response = urllib2.urlopen(url)
    html = response.read()
    #print(html)
#-------------------------------------------------------------------------------
# Event handlers + dispatchers etc.
AdminMode = False
def SwitchAdminMonde():
    global AdminMode
    AdminMode = not(AdminMode)

def DoubleTap():
    q.put("DoubleTap")
def WaveIn():
    q.put("WaveIn")
def WaveOut():
    q.put("WaveOut")
def FingersSpread():
    q.put("FingersSpread")

def WaveRight():
    q.put("WaveRight")
def WaveLeft():
    q.put("WaveLeft")
def SwipeLeft():
    q.put("SwipeLeft")
def SwipeRight():
    q.put("SwipeRight")
def Menu():
    q.put("Menu")

def MyoDispatcher(pose):
    global AdminMode
    if(pose == libmyo.Pose.fist):
        print "fist"
        SwitchAdminMonde()
    elif(not(AdminMode)):
        pass
    elif(pose == libmyo.Pose.double_tap):
        DoubleTap()
    elif(pose == libmyo.Pose.wave_in):
        WaveIn()
    elif(pose == libmyo.Pose.wave_out):
        WaveOut()
    elif(pose == libmyo.Pose.fingers_spread):
        FingersSpread()

def GestureDispatcher(gesture):
    if AdminMode:
        pass
    elif gesture == 'Waved with right hand': WaveRight()
    elif gesture == 'Waved with left hand': WaveLeft()
    elif gesture == 'Swiped left': SwipeLeft()
    elif gesture =='Swiped right': SwipeRight()
    elif gesture == 'Menu': Menu()
#-------------------------------------------------------------------------------
class Listener(libmyo.DeviceListener):
    """
    Listener implementation. Return False from any function to
    stop the Hub.
    """

    interval = 0.05  # Output only 0.05 seconds

    def __init__(self):
        super(Listener, self).__init__()
        self.orientation = None
        self.pose = libmyo.Pose.rest
        self.emg_enabled = False
        self.locked = False
        self.rssi = None
        self.emg = None
        self.last_time = 0
        self.pose_lock = False

    def output(self):
        ctime = time.time()
        if (ctime - self.last_time) < self.interval:
            return
        self.last_time = ctime

        parts = []
        if self.orientation:
            for comp in self.orientation:
                parts.append(str(comp).ljust(15))
        parts.append(str(self.pose).ljust(10))
        parts.append('E' if self.emg_enabled else ' ')
        parts.append('L' if self.locked else ' ')
        parts.append(self.rssi or 'NORSSI')
        if self.emg:
            for comp in self.emg:
                parts.append(str(comp).ljust(5))
        sys.stdout.flush()

    def on_connect(self, myo, timestamp, firmware_version):
        myo.vibrate('short')
        myo.vibrate('short')
        myo.request_rssi()
        myo.request_battery_level()

    def on_rssi(self, myo, timestamp, rssi):
        self.rssi = rssi
        self.output()

    def on_pose(self, myo, timestamp, pose):
        if(not self.pose_lock):
            self.pose = pose
            if pose != libmyo.Pose.rest:
                MyoDispatcher(pose)
                self.pose_lock = True
            self.output()
        elif(pose == libmyo.Pose.rest):
            self.pose_lock = False
            self.pose = pose

    def on_orientation_data(self, myo, timestamp, orientation):
        pass
        #self.orientation = orientation
        #self.output()

    def on_accelerometor_data(self, myo, timestamp, acceleration):
        pass

    def on_gyroscope_data(self, myo, timestamp, gyroscope):
        pass

    def on_emg_data(self, myo, timestamp, emg):
        self.emg = emg
        self.output()

    def on_unlock(self, myo, timestamp):
        self.locked = False
        self.output()

    def on_lock(self, myo, timestamp):
        self.locked = True
        self.output()

    def on_event(self, kind, event):
        """
        Called before any of the event callbacks.
        """

    def on_event_finished(self, kind, event):
        """
        Called after the respective event callbacks have been
        invoked. This method is *always* triggered, even if one of
        the callbacks requested the stop of the Hub.
        """

    def on_pair(self, myo, timestamp, firmware_version):
        """
        Called when a Myo armband is paired.
        """

    def on_unpair(self, myo, timestamp):
        """
        Called when a Myo armband is unpaired.
        """

    def on_disconnect(self, myo, timestamp):
        """
        Called when a Myo is disconnected.
        """

        line1 = "Myo disconnected!!!!"
        time = 5000 #in miliseconds
 
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))

    def on_arm_sync(self, myo, timestamp, arm, x_direction, rotation,
                    warmup_state):
        """
        Called when a Myo armband and an arm is synced.
        """

    def on_arm_unsync(self, myo, timestamp):
        """
        Called when a Myo armband and an arm is unsynced.
        """

        line1 = "Myo unsynced!!!!"
        time = 5000 #in miliseconds
 
        xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time, __icon__))

    def on_battery_level_received(self, myo, timestamp, level):
        """
        Called when the requested battery level received.
        """

    def on_warmup_completed(self, myo, timestamp, warmup_result):
        """
        Called when the warmup completed.
        """


def mainMyo():
    print("Connecting to Myo ... Use CTRL^C to exit.")
    try:
        hub = libmyo.Hub()
    except MemoryError:
        print("Myo Hub could not be created. Make sure Myo Connect is running.")
        return

    hub.set_locking_policy(libmyo.LockingPolicy.none)
    hub.run(1000, Listener())

    # Listen to keyboard interrupts and stop the hub in that case.
    try:
        while hub.running:
            time.sleep(0.25)
    except KeyboardInterrupt:
        print("\nQuitting ...")
    finally:
        print("Shutting down hub...")
        hub.shutdown()

kinectConnected = False
try:
    time.sleep(2)
    f = open(r'\\.\pipe\NPtest', 'r+b', 0)
    i = 1
    kinectConnected = True
except(IOError):
    print "Running in myo only mode"

def mainKinect():
    while kinectConnected:
        global i
        s = 'Message[{0}]'.format(i)
        i += 1
        n = struct.unpack('I', f.read(4))[0]    # Read str length
        s = f.read(n)                           # Read str
        f.seek(0)                               # Important!!!
        GestureDispatcher(s)
   
#-------------------------------------------------------------------------------
q = Queue.Queue()
t1 = threading.Thread(target=mainMyo)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=mainKinect)
t2.daemon = True
t2.start()

def quitController():
    t1.stop()
    t2.stop()

while True:
    s = q.get()
    if(s == "FingersSpread" or s == "WaveLeft"):
        executeCommand("Input.Back")
    elif(s == "DoubleTap" or s ==  "WaveRight"):
        executeCommand("Input.Select")
    elif(s == "WaveIn" or s == "SwipeLeft"):
        executeCommand("Input.Left")
    elif(s == "WaveOut" or s == "SwipeRight"):
        executeCommand("Input.Right")
