import pyautogui

paginas = int(input("Indique el número de páginas del PDF: "))

# Eliminamos las 2 primeras páginas
pyautogui.click(21, 255, 1)  # Abrimos el editor de páginas
pyautogui.click(109, 305, 1, 0, pyautogui.RIGHT)
pyautogui.click(134, 481, 1)
pyautogui.click(1201, 609, 1)

pyautogui.click(109, 305, 1, 0, pyautogui.RIGHT)
pyautogui.click(134, 481, 1)
pyautogui.click(1201, 609, 1)

paginas = paginas - 2


# hacemos zoom out (hay que poner 72 en concreto)
pyautogui.click(1190, 121, 1)
pyautogui.press('del')
pyautogui.press('del')
pyautogui.press('del')
pyautogui.typewrite('72\n')


pyautogui.click(25, 166, 1)

for j in range(paginas):
    pyautogui.click(1093, 1005, 1)
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.click(871, 1030, 1)
    pyautogui.press('del')
    pyautogui.press('del')
    pyautogui.press('pagedown')