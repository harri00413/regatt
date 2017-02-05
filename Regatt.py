# UI deel van Regatt using standard UI stuff

from time import time, strftime, gmtime
from console import hud_alert
from calc_time import berekendetijd


# Some vars
tStartTijd = 0.0
tStopTijd = 0.0
tTimer = 0.0
bRunning = False

def button_tapped(sender: object):
  """

  :type sender: object
  """
  global bRunning
  global tTimer
  global tStartTijd
  global tStopTijd
  t = sender.title
  if t == "Start":
    sender.title = "Stop"
    btnStartStop.tint_color = 1.00, 0.00, 0.00
    tStartTijd = time()
    swLock.enabled = True
    bRunning = True

  else:
    if swLock.value:
      hud_alert('Stop button is locked. Unlock to use stop.')
      else:
        tStopTijd = time()
        tTimer = strftime("%H:%M:%S", gmtime(tStoptijd - tStartTijd))
        sender.title = "Start"
        btnStartStop.tint_color = 0.00, 1.00, 0.00
        labTijd.text = str(tTimer)


# Main program
v = ui.load_view('TestUI')
labTijd = v['lbltijd']
labTijd.text = "00:00:00"
swLock = v['swLock']
btnStartStop = v['btnStart']

if ui.get_screen_size()[1] >= 768:
  # iPad & larger
  v.present('popover')
else:
  # iPhone
  v.present(orientations=['portrait'])
