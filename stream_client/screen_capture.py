""" proprietary two pc streaming setup on the same network """
import numpy
import time
import d3dshot
import socket
import mss.tools as mss_tools
from mss import mss
from win32api import GetSystemMetrics
from utils import checksum

class StreamServer:
    def __init__(self):
        self.w = GetSystemMetrics(0)
        self.h = GetSystemMetrics(1)
        self.stream_server_address_port = ('192.168.4.1', 1935)
        self.udp_client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    def update_checksum(self, t):
        z = bytearray([t[0], t[1]&0xFF,(t[1]&0xFF00)>>8, t[2]&0xFF, (t[2]&0xFF00)>>8])
        self.udp_client.sendto(z, self.stream_server_address_port)

    def setup(self, x=500, y=50):
        start = time.time()
        last = 0
        count = 0
        a = self.w//2 - x//2
        b = self.h//2 - y//2
        with mss() as sct:
            while True:
                shot = sct.grab((a, b, a+x, b+y))                
                count += 1
                c = checksum(shot.rgb)
                if c:
                    self.update_checksum(c)

                dt = time.time() - start
                dt_int = int(dt)
                if dt_int > last:
                    last = dt_int
                    print('%.2f FPS' % (count/dt))

if __name__ == "__main__":
    server = StreamServer()
    server.setup()
