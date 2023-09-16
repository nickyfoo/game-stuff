import pyautogui
import keyboard
import time
from PIL import ImageGrab

positions = [(539, 459), (716, 459), (894, 457), (1069, 457), (1247, 459), (1242, 749), (1070, 750), (885, 745), (717, 745), (534, 752), (536, 1041), (716, 1040), (885, 1038), (1068, 1042), (1245, 1043)]
inventorypositions = [(1001, 903), (1136, 900), (1273, 897), (1422, 905), (1553, 904), (1693, 901), (1833, 898), (1954, 904), (2110, 901), (2233, 897), (1006, 1025), (1142, 1043), (1273, 1039), (1396, 1032), (1545, 1036), (1697, 1045), (1849, 1041), (1944, 1036), (2103, 1036), (2219, 1039), (998, 1164), (1147, 1187), (1291, 1185), (1418, 1174), (1558, 1175), (1693, 1185), (1833, 1182), (1978, 1163), (2063, 1154), (2236, 1166)]
checkpos = (1788, 124)
startbuttonpos = (852, 1325)
exitbuttonpos = (404, 1322)
inventorybuttonpos = (364, 1295)
ratingcheckpos = (1566, 214)
recycleAllPos = (2399, 922)
inventoryPagePositions = [(829, 901), (842, 1042), (836, 1173)]

colors = [(209, 150, 74), (253, 192, 17)]
mainmenucolor = (195,189,22)
whackmenucolor = (202,18,0)
inventorynotfullcolor = (213,214,213)
inventoryFullColors = [(145, 140, 130),(136, 131, 120),(201, 199, 196),(156, 151, 142),(172, 168, 161),(132, 126, 115),(181, 178, 172),(147, 142, 132),(177, 173, 167),(135, 130, 119),(159, 155, 146),(211, 209, 207),(139, 133, 122),(142, 137, 126),(141, 136, 125),(151, 146, 137),(157, 153, 144),(133, 127, 116),(171, 167, 160),(156, 152, 143),(138, 132, 121),(141, 136, 125),(189, 186, 181),(144, 139, 129)]
inventoryGreenRating = (0,255,0)



print(positions)
print(colors)

def matches(x,y):
    for i in range(-5,5):
        for j in range(-5,5):
            for color in colors:
                if pyautogui.pixelMatchesColor(x+i,y+j,color):
                    return True
    return False

def match(x,y):
    for color in colors:
        if pyautogui.pixelMatchesColor(x,y,color,10):
            return True

def slowloop():
    while(True):
        for x,y in positions:
            if match(x,y):
                pyautogui.moveTo(x,y)
                pyautogui.click()
    

def fastmatch(rgb):
    r,g,b = rgb
    tolerance = 10
    ans = False
    for er,eg,eb in colors:
        ans |= abs(r-er) <= tolerance and abs(g-eg) <= tolerance and abs(b-eb) <= tolerance
    return ans

def fastloop():
    timeoutstart = time.time()
    timeouttime = timeoutstart + 65
    while time.time() < timeouttime:
        img = ImageGrab.grab()
        for x,y in positions:
            if(fastmatch(img.getpixel((x,y)))):
                pyautogui.moveTo(x,y)
                pyautogui.click()
                break

def getpos():
    while True:
        pos= pyautogui.position()
        img = ImageGrab.grab()
        print(pos,img.getpixel(pos))

def isReady():
    img = ImageGrab.grab()
    print("checking whack a potato")
    return img.getpixel(checkpos)==mainmenucolor

def inventoryIsFull():
    img = ImageGrab.grab()
    print("checking inventory full", img.getpixel(inventorybuttonpos),inventorynotfullcolor)
    return img.getpixel(inventorybuttonpos) in inventoryFullColors
##    return img.getpixel(inventorybuttonpos)!=inventorynotfullcolor and img.getpixel(inventorybuttonpos) not in [(222,223,222),(207,208,207),(187, 188, 187)]

def startGame():
    pyautogui.moveTo(checkpos)
    pyautogui.click()
    pyautogui.moveTo(startbuttonpos)
    pyautogui.click()

def exitGame():
    pyautogui.moveTo(exitbuttonpos)
    pyautogui.click()

def toggleInventory():
    pyautogui.moveTo(inventorybuttonpos)
    pyautogui.click()

def goToPage(page):
    pyautogui.moveTo(page)
    pyautogui.click()

def isBetterEquipment(pos):
    pyautogui.moveTo(pos)
    pyautogui.click()
    x,y = ratingcheckpos
    img = ImageGrab.grab()
    radius = 5
    for i in range(-radius,radius,1):
        for j in range(-radius,radius,1):
            if img.getpixel((x+i, y+j))==inventoryGreenRating:
                print(x+i, y+j, img.getpixel((x+i,y+j)))
                print("correct")
                return True
    return False

def processInventory():
    numSlots = 40
    currSlots = 0
    for page in inventoryPagePositions:
        goToPage(page)
        if currSlots==numSlots:
            break
        for pos in inventorypositions:
            currSlots+=1
            print(currSlots)
            if isBetterEquipment(pos):
                pyautogui.click()
            if currSlots==numSlots:
                break
    
    pyautogui.moveTo(recycleAllPos)
    pyautogui.click()
    pyautogui.click()

def startBot():
    while True:
        if isReady():
            print("starting")
            startGame()
            fastloop()
            exitGame()
        elif inventoryIsFull():
            toggleInventory()
            processInventory()
            toggleInventory()
        time.sleep(1)

def getPosWithSpace():
    while len(inventoryPagePositions) < 3:
        keyboard.wait('space')
        x,y = pyautogui.position()
        inventoryPagePositions.append((x,y))
        print('space pressed! Waiting on it again...')

    print(inventoryPagePositions)        

if __name__ == "__main__":
    print("DIE POTATO DIE")
    startBot()
##    getpos()
