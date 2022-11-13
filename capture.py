import datetime
import os
import time

import pyautogui

# number of pages
PAGES = int(input("Enter number of pages: "))
# interval (sec)
SPAN = 1
# Initials of output folder
FOLDERNAME = "output"
# Initials of output file
FILENAME = "capture"

# make output folder
def make_folder():
    # get current time
    now = datetime.datetime.now()
    # make folder name
    foldername = FOLDERNAME + "_" + now.strftime("%Y%m%d%H%M%S")
    # make folder
    os.mkdir(foldername)
    # return folder name
    return foldername

def capture(foldername):
    for p in range(PAGES):
        # make file name
        filename = FILENAME + "_" + str(p+1).zfill(4) + ".png"
        # capture
        pyautogui.screenshot().save(os.path.join(foldername, filename))
        # move to next page
        pyautogui.press("right")
        # interval
        time.sleep(SPAN)

if __name__ == "__main__":
    # make folder
    foldername = make_folder()
    # time to move screen
    time.sleep(5)
    # capture
    capture(foldername)
