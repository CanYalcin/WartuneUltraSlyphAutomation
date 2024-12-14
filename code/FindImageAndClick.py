import time
import pyautogui
import threading
from PIL import Image
import os

allImages = ([Image.open("Images/Iris0.png"),Image.open("Images/Iris1.png"),Image.open("Images/Iris2.png")],
[Image.open("Images/Pan0.png"),Image.open("Images/Pan1.png"),Image.open("Images/Pan2.png")],
[Image.open("Images/Amazon0.png"),Image.open("Images/Amazon1.png"),Image.open("Images/Amazon2.png")],
[Image.open("Images/Eve0.png"),Image.open("Images/Eve1.png"),Image.open("Images/Eve2.png")])

input1 = int(input("Press 1 for Iris\nPress 2 for Pan\nPress 3 for Amazon\nPress 4 for Eve\n"))

while input1<1 or input1>4:
    print("Wrong input")
    input1 = int(input("Press 1 for Iris\nPress 2 for Pan\nPress 3 for Amazon\nPress 4 for Eve\n"))


def findImageThenClick(img, ConfidLvL=.75):
    try:
        x, y = pyautogui.locateCenterOnScreen(img, confidence=ConfidLvL, grayscale=True)
        print("Found it!")
        pyautogui.click(x,y)
        pyautogui.PAUSE = 9
    except:
        pass

args = None

def inputForExit():
    global args
    args = input()

inputStrs = ["Iris","Pan","Amazon","Eve"]
imagePngs = allImages[input1-1]
print("To close the app, input anything")
print("Search will start in 3 sec for " + inputStrs[input1-1])

try:
    threading.Thread(target=inputForExit).start()
    time.sleep(3)
    while args==None:
        for x in range(0,3):
            findImageThenClick(imagePngs[x])
        pass;
except:
    print("something went wrong")