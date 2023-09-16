import pyautogui
import keyboard
corners = []

def getPosWithSpace():
    while len(corners)<4:
        keyboard.wait('space')
        x,y = pyautogui.position()
        corners.append((x,y))
        print('space pressed! Waiting on it again...')

    print(corners)

def click():
    print("clicking")
    for i in range(150,2350,50):
        for j in range(150,1450,50):
            pyautogui.moveTo(i,j,_pause =False)
            pyautogui.click(_pause=False)

if __name__ == "__main__":
    while True:
        print('Press space when ready...')
        keyboard.wait('space')
        click()
