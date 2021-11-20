import pyautogui

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
# print(screenWidth, screenHeight)

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
print("El mouse se encuentra en la posición: ")
print(currentMouseX, currentMouseY)