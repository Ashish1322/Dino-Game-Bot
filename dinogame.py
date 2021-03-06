import pyautogui
from PIL import Image, ImageGrab
import time

# Function for press key to jump
def hit(key):
    pyautogui.keyDown(key)

# Function for detecting the cactus
def iscollide(data):
    for i in range(500,570):
        for j in range(275,285):
           if  data[i,j] < 100:
               hit('up')
               return
    return 
  
if __name__ == "__main__":
    
    time.sleep(2)
    while True:
        Image = ImageGrab.grab().convert('L')
        data = Image.load()
        iscollide(data)
        for i in range(500, 570):
            for j in range(250, 290):
                data[i,j] = 0
       



        