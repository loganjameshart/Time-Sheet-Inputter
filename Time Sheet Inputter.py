import pyautogui as pag
import time


time.sleep(3)

pag.click(272,476)

for days in range(0,5):
    pag.write("time")
    time.sleep(.5)
    pag.press("enter")
    pag.press("tab")
    pag.write("7.5")
    pag.press("tab")
    pag.press("tab")

pag.click(272,782)

for days in range(0,5):
    pag.write("time")
    time.sleep(.5)
    pag.press("enter")
    pag.press("tab")
    pag.write("7.5")
    pag.press("tab")
    pag.press("tab")