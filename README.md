# Time-Sheet-Inputter
Automatically enters my timesheet for the past two weeks. Uses PyAutoGui since I use the same screen every week.

## How It's Made

Python Standard Library. External libraries: pyautogui

Used pyautogui to find the necessary text boxes in the timesheet software, then iterated over a range() for the number of days worked (always 5, in my case). The sleep() function was used to account for some delay on the timesheet system's side for autocompleting the correct response.
