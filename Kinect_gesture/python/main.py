import time
import struct

import myo

# Connection to the pipe --> http://jonathonreinhart.blogspot.be/2012/12/named-pipes-between-c-and-python.html
f = open(r'\\.\pipe\NPtest', 'r+b', 0)
i = 1

while True:
    s = 'Message[{0}]'.format(i)
    i += 1

    n = struct.unpack('I', f.read(4))[0]    # Read str length
    s = f.read(n)                           # Read str
    f.seek(0)                               # Important!!!
    print 'Read:', s

    GestureDispatcher(s);

    time.sleep(2)
#-------------------------------------------------------------------------------

# Send commands to Kodi
def executeCommand(method):
    start = 'http://localhost:8080/jsonrpc?request={"jsonrpc":%20"2.0",%20"id":%201,%20"method":%20"'
    end = '"}'
    url = start + method + end
    response = urllib2.urlopen(url)
    html = response.read()
    #print(html)
#-------------------------------------------------------------------------------

AdminMode = false

def SwitchAdminMonde():
    AdminMode = not(AdminMode)


def MyoDispatcher(pose):
    if(pose == libmyo.Pose.fist):
        SwitchAdminMonde()
    elif(AdminMode):
        pass
    elif(pose == libmyo.Pose.double_tap):
        DoubleTap()
    elif(pose == libmyo.Pose.wave_in):
        WaveIn()
    elif(pose == libmyo.Pose.wave_out):
        WaveOut


def GestureDispatcher(gesture):
    return {
        'Waved with right hand': WaveRight(),
        'Waved with left hand': WaveLeft(),
        'Swiped left': SwipeLeft(),
        'Swiped right': SwipeRight(),
        'Menu': Menu()
    }

def WaveRight():
    pass
def WaveLeft():
    pass
def SwipeLeft():
    pass
def SwipeRight():
    pass
def Menu():
    pass
