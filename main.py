import pyautogui

paginas = int(input("Indique el número de páginas del PDF: "))

# Eliminamos las 2 primeras páginas
pyautogui.click(14, 218, 1)  # Abrimos el editor de páginas
pyautogui.click(121, 261, 1, 0, pyautogui.RIGHT)
pyautogui.click(187, 392, 1)
pyautogui.click(748, 442, 1)
pyautogui.click(950, 442, 1)
pyautogui.typewrite('1, 2')
pyautogui.click(1127, 647, 1)

paginas = paginas - 2

resto = paginas % 4

# hacemos zoom out (hay que poner 76 en concreto)
pyautogui.click(1214, 98, 1)
pyautogui.press('del')
pyautogui.press('del')
pyautogui.press('del')
pyautogui.typewrite('76\n')

for i in range(int(paginas/4)):
    
    # quitamos los anuncios de la pagina con imagenes
    pyautogui.click(31, 138, 1)

    # imagen superior
    pyautogui.click(1044, 267, 1)
    pyautogui.press('del')
    pyautogui.click(779, 575, 1)
    pyautogui.press('del')

    # imagen lateral
    pyautogui.click(1044, 267, 1)
    pyautogui.press('del')
    pyautogui.click(779, 575, 1)
    pyautogui.press('del')


    # texto lateral
    pyautogui.click(1306, 607, 1)
    pyautogui.press('del')
    pyautogui.press('del')

    # logo de wuolah
    pyautogui.click(1246, 993, 1)
    pyautogui.press('del')

    # PASAMOS A LA SIGUIENTE PÁGINA
    pyautogui.click(1681, 219, 1, 0, pyautogui.RIGHT)
    pyautogui.click(1767, 336, 1)



    # quitamos los anuncios sin imagenes de las tres paginas siguientes

    for j in range(3):
        # texto lateral
        pyautogui.click(1306, 607, 1)
        pyautogui.press('del')
        pyautogui.press('del')

        # logo de wuolah
        pyautogui.click(1246, 993, 1)
        pyautogui.press('del')

    
        # eliminamos texto de abajo
        pyautogui.click(1024, 1033, 1)
        pyautogui.press('del')
        pyautogui.click(1024, 1033, 2)
        pyautogui.press('del')



        # PASAMOS A LA SIGUIENTE PÁGINA
        pyautogui.click(1681, 219, 1, 0, pyautogui.RIGHT)
        pyautogui.click(1767, 336, 1)

        # aumentamos el i
        i += 1