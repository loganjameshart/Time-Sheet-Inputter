import pyautogui as pag
import time

#sleep for a few seconds to give time to switch windows, if necessary
time.sleep(3)

#clicks in the first text box
pag.click(272,476)

#inputs my standard work hours, tabbing over to get to each new day. Pauses inbetween are used to account for the system's delay in populating drop-down choices.
for days in range(0,5):
    pag.write("time")
    time.sleep(.5)
    pag.press("enter")
    pag.press("tab")
    pag.write("7.5")
    pag.press("tab")
    pag.press("tab")

#click on the text box for the next week.     
pag.click(272,782)

for days in range(0,5):
    pag.write("time")
    time.sleep(.5)
    pag.press("enter")
    pag.press("tab")
    pag.write("7.5")
    pag.press("tab")
    pag.press("tab")
