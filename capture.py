import datetime
import os
import time

import img2pdf
import pyautogui
from natsort import natsorted
from PIL import Image


# function to make output folder
def make_folder():
    # make folder name
    foldername = FOLDERNAME + "_" + now.strftime("%Y%m%d%H%M%S")
    # make folder
    os.mkdir(foldername)
    # return folder name
    return foldername

# function to capture screen
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

# function to convert png to jpg
def convert(foldername):
    # get file list
    files = os.listdir(foldername)
    # sort file list
    files = natsorted(files)
    print(files)
    # set extension
    ext = ".png"
    # convert
    with open(PDFNAME,"wb") as f:
        f.write(img2pdf.convert([Image.open(foldername + "/" + file).filename for file in files if file.endswith(ext)]))

if __name__ == "__main__":
    # number of pages
    PAGES = int(input("Enter number of pages: "))
    # interval (sec)
    SPAN = 1
    # initials of output folder
    FOLDERNAME = "output"
    # initials of output file
    FILENAME = "capture"
    # get current time
    now = datetime.datetime.now()
    # PDF file name
    PDFNAME = FOLDERNAME + now.strftime("%Y%m%d%H%M%S") + ".pdf"

    # make folder
    foldername = make_folder()
    # time to move screen
    time.sleep(5)
    # capture
    capture(foldername)
    # convert to pdf
    convert(foldername)
