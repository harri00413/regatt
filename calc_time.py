#!usr/bin/python3
# Berekening gezeilde tijd met omrekening met behulp van de SW waarde
# Inputs:
# Gezeilde uren, minuten en seconden in uren, minuten en seconden en SW
# SW in float
# Output: Berekende tijd als string
# BerekendeTijd = GezeildeTijd * 100 / SW
# print(BerekendeTijd("01:32:56",103.5))

import datetime


# noinspection PyShadowingNames
def berekendetijd(gezeildeuren, gezeildeminuten, gezeildeseconden, sw):
    tinsec = get_sec(gezeildeuren, gezeildeminuten, gezeildeseconden) * 100 / sw
    return datetime.timedelta(seconds=round(tinsec), microseconds=0)


def get_sec(u, m, s):
    return u * 3600 + m * 60 + s


# main()
# igezeildeuren = int(input("Geef gezeilde uren: "))
# igezeildeminuten = int(input("Geef gezeilde minuten: "))
# igezeildeseconden = int(input("Geef gezeilde seconden: "))
# sw = int(input("Geef SW: "))

# print("Berekende tijd: " + str(berekendetijd(igezeildeuren, igezeildeminuten, igezeildeseconden, sw)))
