from time import localtime
from socket import socket, getaddrinfo, AF_INET, SOCK_DGRAM
from struct import unpack
from errno import ETIMEDOUT
from machine import RTC

NTP_DELTA = 3155673600
host = "pool.ntp.org"

def getntp():
    print('Get UTC time from NTP server...')
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1b
    try:
        addr = getaddrinfo(host, 123)[0][-1]
    except OSError: # as exc:
        #if exc.args[0] == -2:
            print('Connect NTP Server: Error resolving pool NTP')
            return 0
    s = socket(AF_INET, SOCK_DGRAM)
    s.settimeout(1)
    res = s.sendto(NTP_QUERY, addr)

    try:
        msg = s.recv(48)
    except OSError as exc:
        if exc.args[0] == ETIMEDOUT:
            print('Connect NTP Server: Request Timeout')
            s.close()
            return 0
    s.close()
    val = unpack("!I", msg[40:44])[0]
    return val - NTP_DELTA

def settime():
   RTC().datetime(localtime(getntp()))
   print(time.localtime())
