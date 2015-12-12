#!usr/bin/python
# Berekening gezeilde tijd met omrekening met behulp van de SW waarde
# Inputs:
# Gezeilde tijd in hh:mm:ss
# SW in float
# Output: Berekende tijd
# BerekendeTijd == GezeildeTijd * 100 / SW
# print(BerekendeTijd("01:32:56",103.5))

import datetime

def BerekendeSec(GezeildeTijd, SW):
    TinSec = get_sec(GezeildeTijd) * 100 / SW
    return TinSec

def TimeFromSec(TinSec):
    return datetime.timedelta(seconds = TinSec)

def get_sec(t):
    l = t.split(':')
    return int(l[0]) * 3600 + int(l[1]) * 60 + int(l[2])

#main()
#GezeildeTijd = input("Geef gezeilde tijd: ")
#SW = input("Geef SW: ")

GezeildeTijd = "1:00:00"
SW = 110

s = BerekendeSec(GezeildeTijd, SW)
t = TimeFromSec(s)

print("Berekende tijd: " + str(t))
print("Berekende tijd in seconden: " + str(s))
