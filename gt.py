from pyautogui import *
import pyautogui
import time
import keyboard
import pyscreeze
from region import *

pyscreeze.USE_IMAGE_NOT_FOUND_EXCEPTION = False

NUMERO_DE_REPETICOES = 999

def funcao_para_repetir():
    # Values
    caixa = None
    inc_pos = None
    dificulty_select = None
    map_selector = None
    map_dif = None
    mode_dif = None
    okvar = None
    house = None
    sniper = None
    alchemist = None
    startthis = None
    cliq = None
    reload = None
    # Checar Caixa
    while caixa is None:
        time.sleep(1.5) 
        caixa = pyautogui.locateOnScreen('imagens/caixa.png', region=(region_caixa), confidence=0.7)
        if caixa is not None:
            pyautogui.moveTo(689,483)
            time.sleep(0.5) 
            pyautogui.click()
            time.sleep(0.5) 
            pyautogui.moveTo(582,383)
            pyautogui.click()
            time.sleep(0.5) 
            pyautogui.click()
            time.sleep(0.5) 
            pyautogui.moveTo(791,375)
            time.sleep(0.5) 
            pyautogui.click()
            time.sleep(0.5) 
            pyautogui.click()
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(0.5) 
            pyautogui.moveTo(59,44)
            time.sleep(0.5) 
            pyautogui.click()
        else:
            break

    # Click start button
    while inc_pos is None:
        inc_pos = pyautogui.locateOnScreen('imagens/ini.png', region=(region_inc), confidence=0.7)     
        if inc_pos is not None:
            pyautogui.moveTo(600,665)  
            pyautogui.click() 
            time.sleep(0.2) 
        else:
            continue
                        
    # Selelect dificulty of maps
    while dificulty_select is None:
        dificulty_select = pyautogui.locateOnScreen('imagens/mapinf.png', region=(region_map), confidence=0.7)
        if dificulty_select is not None:
            pyautogui.moveTo(989,406)
            time.sleep(0.2)
        else:
            pyautogui.moveTo(950,703)
            pyautogui.click()
            time.sleep(0.2)
            continue

    # Map selector
    while map_selector is None:
        map_selector = pyautogui.locateOnScreen('imagens/mapinf.png', region=(region_map), confidence=0.7)
        if map_selector is not None:
            pyautogui.moveTo(989,406)
            pyautogui.click()
            time.sleep(0.2)
        else:
            continue

    # Select map dificulty 
    while map_dif is None:
        map_dif = pyautogui.locateOnScreen('imagens/mapdif.png', region=(region_mapdif), confidence=0.7)
        if map_dif is not None:
            pyautogui.moveTo(450,295)
            pyautogui.click()
            time.sleep(0.2)
        else:
            continue

    # Select dificult mode of the map
    while mode_dif is None:
        mode_dif = pyautogui.locateOnScreen('imagens/modedif.png', region=(region_modedif), confidence=0.7)
        if map_dif is not None:
            pyautogui.moveTo(914,327)
            pyautogui.click()
            time.sleep(0.2)
        else:
            continue
                    
    # Click OK button
    while okvar is None:
        time.sleep(1.0)
        okvar = pyautogui.locateOnScreen('imagens/okball.png', region=(region_ok), confidence=0.9)
        if okvar is not None:
            pyautogui.moveTo(685,541)
            pyautogui.click()
            time.sleep(0.4)
        else:
            continue

    # Put house and upgrade it
    while house is None:
        keyboard.press_and_release('k')
        pyautogui.moveTo(1125,475)
        time.sleep(1.0)
        pyautogui.click()
        time.sleep(1.0)
        pyautogui.click()
        time.sleep(1.0)
        house = pyautogui.locateOnScreen('imagens/house.png', region=(region_house), confidence=0.7) 
        if house is not None:
            pyautogui.moveTo(1125,475)  
            time.sleep(0.5)
            keyboard.press_and_release(';')
            time.sleep(0.4)
            keyboard.press_and_release(';')
            time.sleep(0.4)
            keyboard.press_and_release(',')
            time.sleep(0.4)
            keyboard.press_and_release(',')
            time.sleep(0.4)
            keyboard.press_and_release('esc')
            time.sleep(0.4)
        else:
            continue

    # Put sniper
    while sniper is None:
        keyboard.press_and_release('z')
        pyautogui.moveTo(1082,430)
        time.sleep(1.0)
        pyautogui.click()
        time.sleep(1.0)
        pyautogui.click()
        time.sleep(1.0)
        sniper = pyautogui.locateOnScreen('imagens/sniper.png', region=(region_sniper), confidence=0.7) 
        if sniper is not None:
            pyautogui.moveTo(1082,430)  
            time.sleep(0.5)
            keyboard.press_and_release(';')
            time.sleep(0.4)
            keyboard.press_and_release(';')
            time.sleep(0.4)
            keyboard.press_and_release(';')
            time.sleep(0.4)
            keyboard.press_and_release(';')
            time.sleep(0.4)
            keyboard.press_and_release('.')
            time.sleep(0.4)
            keyboard.press_and_release('.')
            time.sleep(0.4)
            keyboard.press_and_release('esc')
            time.sleep(0.4)
        else:
            continue     

    # Put alchemist
    while alchemist is None:
        keyboard.press_and_release('f')
        pyautogui.moveTo(1134,419)
        time.sleep(1.0)
        pyautogui.click()
        time.sleep(1.5)
        pyautogui.click()
        time.sleep(1.5)
        alchemist = pyautogui.locateOnScreen('imagens/alch.png', region=(region_alch), confidence=0.7) 
        if alchemist is not None:
            pyautogui.moveTo(1134,419)  
            time.sleep(0.5)
            keyboard.press_and_release(',')
            time.sleep(0.4)
            keyboard.press_and_release(',')
            time.sleep(0.4)
            keyboard.press_and_release(',')
            time.sleep(0.4)
            keyboard.press_and_release(',')
            time.sleep(0.4)
            keyboard.press_and_release('.')
            time.sleep(0.4)
            keyboard.press_and_release('.')
            time.sleep(0.4)
            keyboard.press_and_release('esc')
            time.sleep(0.2)
        else:
            continue       

    # Start turn and put hero in map
    while startthis is None:
        keyboard.press_and_release('u')
        pyautogui.moveTo(592,239)
        time.sleep(1.0)
        pyautogui.click()
        time.sleep(0.5)
        keyboard.press_and_release('space')
        time.sleep(0.5)
        keyboard.press_and_release('space')
        startthis = pyautogui.locateOnScreen('imagens/comece.png', region=(region_start), confidence=0.7) 
        if startthis is not None:
            time.sleep(0.5)
        else: 
            continue

    # Click on screen and use abilities
    while cliq is None:
        pyautogui.moveTo(603,21)
        time.sleep(1.0)
        pyautogui.click()
        time.sleep(1.0)
        pyautogui.click()
        keyboard.press_and_release('1')
        time.sleep(0.5)
        keyboard.press_and_release('2')
        time.sleep(1.0)
        cliq = pyautogui.locateOnScreen('imagens/cliq.png', region=(region_cliq), confidence=0.9) 
        if cliq is not None:
            pyautogui.moveTo(684,643)  
            time.sleep(0.5)
            pyautogui.click()           
            time.sleep(0.5)
        else:
            continue
                                                            
    # Go back to main menu
    while reload is None:
        reload = pyautogui.locateOnScreen('imagens/reload.png', region=(region_reload), confidence=0.9) 
        if reload is not None:
            pyautogui.moveTo(510,605)  
            time.sleep(0.5)
            pyautogui.click()           
            time.sleep(3.5)
        else:
            continue
repeticao_atual = 0
while repeticao_atual != NUMERO_DE_REPETICOES:
    repeticao_atual += 1
    
    funcao_para_repetir()