#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from PIL import ImageTk, Image
import os

# In[ ]:


import tkinter as tk
from PIL import ImageTk, Image
import os

character_dict = {'Mario': {'number': 1, 'plats': 2, 'vkp': 4, 'hkp':72}, 
                  'Donkey Kong': {'number': 2, 'plats': 19, 'vkp': 1, 'hkp': 23}, 
                  'Link': {'number': 3, 'plats': 3, 'vkp':64 ,'hkp':22}, 
                  'Samus': {'number': 4, 'plats': 5, 'vkp':51, 'hkp': 40}, 
                  'Dark Samus': {'number': 5, 'plats': 51, 'vkp':6, 'hkp': 40}, 
                  'Yoshi': {'number': 6, 'plats': 8, 'vkp':20, 'hkp': 73},
                  'Kirby': {'number': 7, 'plats': 5, 'vkp':84, 'hkp': 44},
                  'Fox': {'number': 8, 'plats': 17, 'vkp':25, 'hkp': 81},
                  'Pikachu': {'number': 9, 'plats': 5, 'vkp':57, 'hkp': 83},
                  'Luigi': {'number': 10, 'plats': 5, 'vkp':15, 'hkp': 57},
                  'Ness': {'number' : 11, 'plats': 64, 'vkp':54, 'hkp': 13},
                  'Captain Falcon': {'number' : 12, 'plats':27, 'vkp':48, 'hkp': 38},
                  'Jigglypuff': {'number': 13, 'plats': 59, 'vkp':37, 'hkp': 34},
                  'Peach': {'number': 14, 'plats': 77, 'vkp':80, 'hkp': 42},
                  'Daisy': {'number': 15, 'plats': 77, 'vkp':80, 'hkp': 42},
                  'Bowser': {'number': 16, 'plats': 29, 'vkp':8, 'hkp': 3},
                  'Ice Climbers': {'number': 17, 'plats': 79, 'vkp':40, 'hkp': 53},
                  'Sheik': {'number': 18, 'plats': 37, 'vkp':32, 'hkp': 82},
                  'Zelda': {'number': 19, 'plats': 62, 'vkp':78, 'hkp': 48},
                  'Dr. Mario': {'number': 20, 'plats': 5, 'vkp':69, 'hkp': 45},
                  'Pichu': {'number': 21, 'plats': 76, 'vkp':79, 'hkp': 17},
                  'Falco': {'number': 22, 'plats': 12, 'vkp':18, 'hkp': 51},
                  'Marth': {'number': 23, 'plats': 5, 'vkp':60, 'hkp': 14},
                  'Lucina': {'number': 24, 'plats': 4, 'vkp':61, 'hkp': 15},
                  'Young Link': {'number': 25, 'plats': 46, 'vkp':52, 'hkp': 41},
                  'Ganondorf': {'number': 26, 'plats': 50, 'vkp':42, 'hkp': 12},
                  'Mewtwo': {'number': 27, 'plats': 56, 'vkp':36, 'hkp': 33},
                  'Roy': {'number': 28, 'plats': 35, 'vkp':52, 'hkp': 16},
                  'Chrom': {'number': 29, 'plats': 7, 'vkp':73, 'hkp': 18},
                  'Mr. Game & Watch': {'number': 30, 'plats': 16, 'vkp':74, 'hkp': 47},
                  'Meta Knight': {'number': 31, 'plats': 67, 'vkp':13, 'hkp': 28},
                  'Pit': {'number': 32, 'plats': 53, 'vkp':54, 'hkp': 79},
                  'Dark Pit': {'number': 33, 'plats': 53, 'vkp':53, 'hkp': 65},
                  'Zero Suit Samus': {'number': 34, 'plats': 24, 'vkp':17, 'hkp': 84},
                  'Wario': {'number': 35, 'plats': 20, 'vkp':46, 'hkp': 36},
                  'Snake': {'number': 36, 'plats': 15, 'vkp':24, 'hkp': 59},
                  'Ike': {'number': 37, 'plats': 13, 'vkp':23, 'hkp': 7},
                  'Pokemon Trainer': {'number': 38, 'plats': 14, 'vkp':6, 'hkp': 26},
                  'Diddy Kong': {'number': 39, 'plats': 18, 'vkp':45, 'hkp': 64},
                  'Lucas': {'number': 40, 'plats': 69, 'vkp':70, 'hkp': 70},
                  'Sonic': {'number': 41, 'plats': 78, 'vkp':71, 'hkp':68},
                  'King Dedede': {'number': 42, 'plats': 65, 'vkp':41, 'hkp': 11},
                  'Olimar': {'number': 43, 'plats': 57, 'vkp':55, 'hkp': 66},
                  'Lucario': {'number': 44, 'plats': 39, 'vkp':75, 'hkp': 20},
                  'R.O.B': {'number': 45, 'plats': 25, 'vkp':7, 'hkp': 2},
                  'Toon Link': {'number': 46, 'plats': 58, 'vkp':67, 'hkp': 71},
                  'Wolf': {'number': 47, 'plats': 45, 'vkp':27, 'hkp': 8},
                  'Villager': {'number': 48, 'plats': 21, 'vkp':43, 'hkp': 62},
                  'Mega Man': {'number': 49, 'plats': 55, 'vkp':35, 'hkp': 61},
                  'Wii Fit Trainer': {'number': 50, 'plats': 38, 'vkp':63, 'hkp': 51},
                  'Rosalina': {'number': 51, 'plats': 26, 'vkp':28, 'hkp': 31},
                  'Little Mac': {'number': 52, 'plats': 80, 'vkp':16, 'hkp': 1},
                  'Greninja': {'number': 53, 'plats': 73, 'vkp':39, 'hkp': 77},
                  'Mii Brawler': {'number': 54, 'plats': 1, 'vkp':2, 'hkp': 74},
                  'Mii Swordfighter': {'number': 55, 'plats': 28, 'vkp':49, 'hkp': 78},
                  'Mii Gunner': {'number': 56, 'plats': 48, 'vkp':65, 'hkp': 8},
                  'Palutena': {'number': 57, 'plats': 10, 'vkp':5, 'hkp': 75},
                  'Pac-Man': {'number': 58, 'plats': 61, 'vkp':83, 'hkp': 67},
                  'Robin': {'number': 59, 'plats': 23, 'vkp':26, 'hkp': 30},
                  'Shulk': {'number': 60, 'plats': 31, 'vkp':51, 'hkp': 39},
                  'Bowser Jr.': {'number': 61, 'plats': 51, 'vkp':65, 'hkp': 49},
                  'Duck Hunt': {'number': 62, 'plats': 47, 'vkp':76, 'hkp': 80},
                  'Ryu': {'number': 63, 'plats': 41, 'vkp':11, 'hkp': 27},
                  'Ken': {'number': 64, 'plats': 43, 'vkp':12, 'hkp': 55},
                  'Cloud': {'number': 65, 'plats': 6, 'vkp':19, 'hkp': 29},
                  'Corrin': {'number': 66, 'plats': 30, 'vkp':29, 'hkp': 60},
                  'Bayonetta': {'number': 67, 'plats': 3, 'vkp':3, 'hkp': 25},
                  'Inkling': {'number': 68, 'plats': 44, 'vkp':33, 'hkp': 76},
                  'Ridley': {'number': 69, 'plats': 71, 'vkp':38, 'hkp': 35},
                  'Simon': {'number': 70, 'plats': 83, 'vkp':72, 'hkp': 46},
                  'Richter': {'number': 71, 'plats': 83, 'vkp':72, 'hkp': 46},
                  'King K. Rool': {'number': 72, 'plats': 36, 'vkp':31, 'hkp': 10},
                  'Isabelle': {'number': 73, 'plats': 68, 'vkp':44, 'hkp': 63},
                  'Incineroar': {'number': 74, 'plats': 11, 'vkp':22, 'hkp': 6},
                  'Piranha Plant': {'number': 75, 'plats': 84, 'vkp':82, 'hkp': 69},
                  'Joker': {'number': 76, 'plats': 22, 'vkp':47, 'hkp': 37},
                  'Hero': {'number': 77, 'plats': 54, 'vkp':77, 'hkp': 21},
                  'Banjo': {'number': 78, 'plats': 81, 'vkp':59, 'hkp': 52},
                  'Terry': {'number': 79, 'plats': 9, 'vkp':21, 'hkp': 5},
                  'Byleth': {'number': 80, 'plats': 49, 'vkp':6, 'hkp': 32},
                  'Min Min': {'number': 81, 'plats': 60, 'vkp':68, 'hkp': 19},
                  'Steve': {'number': 82, 'plats': 34, 'vkp':10, 'hkp': 4},
                  'Sephiroth': {'number': 83, 'plats': 72, 'vkp':58, 'hkp': 24},
                  'Pyra/Mythra': {'number': 84, 'plats': 32, 'vkp':30, 'hkp': 9},
                  'Kazuya': {'number': 85, 'plats': 74, 'vkp':14, 'hkp': 56},
                  'Sora': {'number': 86, 'plats': 33, 'vkp':9, 'hkp': 54},

                 }


def stage_math(selection1, selection2):
    plat_character_1 = character_dict[selection1]['plats']
    plat_character_2 = character_dict[selection2]['plats']
    vkp_character_1 = character_dict[selection1]['vkp']
    vkp_character_2 = character_dict[selection2]['vkp']
    hkp_character_1 = character_dict[selection1]['hkp']
    hkp_character_2 = character_dict[selection2]['hkp']
    plat_diff = plat_character_1 - plat_character_2
    vkp_diff = vkp_character_1 - vkp_character_2
    hkp_diff = hkp_character_1 - hkp_character_2

    #If the difference is less than ten then the difference in these parameters is next to negligible and should not count towards picking a stage
    if plat_diff >= -10 and plat_diff <= 10:
        plat_character_1 = 1
        plat_character_2 = 1
    if vkp_diff >= -10 and vkp_diff <= 10:
        vkp_character_1 = 1
        vkp_character_2 = 1
    if hkp_diff >= -10 and hkp_diff <= 10:
        hkp_character_1 = 1
        hkp_character_2 = 1

    #comparisons made for picking a stage
    if selection1 == selection2:
        return print('You are playing the ditto, you should pick your favorite stage as the stage will not be a factor in the match up')
    elif (plat_character_1 >= plat_character_2) and (vkp_character_1 >= vkp_character_2) and (hkp_character_1 < hkp_character_2):
        return print(' 1. Yoshis Story \n 2. Battlefield \n 3. Smashville \n 4. Pokemon Stadium 2 \n 5. Small Battlefield \n 6. Kalos Pokemon League \n 7. Town and City \n 8. Final Destination')
    elif (plat_character_1 >= plat_character_2) and (vkp_character_1 >= vkp_character_2) and (hkp_character_1 >= hkp_character_2):
        return print(' 1. Yoshis Story \n 2. Battlefield \n 3. Smashville \n 4. Pokemon Stadium 2 \n 5. Small Battlefield \n 6. Final Destination \n 6. Town and City \n 7. Kalos Pokemon League')
    elif (plat_character_1 >= plat_character_2) and (vkp_character_1 < vkp_character_2) and (hkp_character_1 < hkp_character_2):
        return print(' 1. Yoshis Story \n 2. Battlefield \n 3. Small Battlefield \n 4. Smashville \n 5. Pokemon Stadium 2 \n 6. Kalos Pokemon League \n 7. Town and City \n 8. Final Destination' )
    elif (plat_character_1 >= plat_character_2) and (vkp_character_1 < vkp_character_2) and (hkp_character_1 >= hkp_character_2):
        return print(' 1. Yoshis Story \n 2. Battlefield \n 3. Pokemon Stadium 2 \n 4. Smashville \n 5. Small Battlefield 6. Final Destination \n 7. Town and City \n \n 8. Kalos Pokemon League')
    elif (plat_character_1 < plat_character_2) and (vkp_character_1 >= vkp_character_2) and (hkp_character_1 >= hkp_character_2):
        return print('1. Pokemon Stadium 2 \n 2. Smashville \n 3. Final Destination \n 4. Small Battlefield \n 5. Town and City \n 6. Kalos Pokemon League \n  7. Yoshis Story \n 8. Battlefield')
    elif (plat_character_1 < plat_character_2) and (vkp_character_1 < vkp_character_2) and (hkp_character_1 >= hkp_character_2):
        return print('1. Kalos Pokemon League \n 2. Town and City \n 3. Smashville \n 4. Final Destination \n 5. Smashville \n 6. Small Battlefield \n  \n  7. Battlefield \n 8. Yoshis Story')
    elif (plat_character_1 < plat_character_2) and (vkp_character_1 >= vkp_character_2) and (hkp_character_1 < hkp_character_2):
        return print('1. Pokemon Stadium 2 \n 2. Smashville \n 3. Final Destination \n 4. Small Battlefield \n 5. Town and City \n 6. Kalos Pokemon League \n  7. Yoshis Story \n 8. Battlefield')
    elif (plat_character_1 < plat_character_2) and (vkp_character_1 < vkp_character_2) and (hkp_character_1 < hkp_character_2):
        return print('1. Final Destination \n 2. Kalos Pokemon League \n 3. Final Destination \n 4. Small Battlefield \n 5. Pokemon Stadium 2 \n 6. Smashville \n  7. Battlefield \n 8. Yoshis Sotry')
    else:
        return print('1. Pokemon Stadium 2')
# creating main window
root = tk.Tk()

# loading the image
img = ImageTk.PhotoImage(Image.open("SmashRoster.jpg"))

def MarioCallBack():
    global character
    character = 'Mario'
def MarioCallBack2():
    character2 = 'Mario'
    return stage_math(character, character2)
def DKCallBack():
    global character
    character = 'Donkey Kong'
def DKCallBack2():
    character2 = 'Donkey Kong'
    return stage_math(character, character2)
def LinkCallBack():
    global character
    character = 'Link'
def LinkCallBack2():
    character2 = 'Link'
    return stage_math(character, character2)
def SamusCallBack():
    global character
    character = 'Samus'
def SamusCallBack2():
    character2 = 'Samus'
    return stage_math(character, character2)
def DarkSamusCallBack():
    global character
    character = 'Dark Samus'
def DarkSamusCallBack2():
    character2 = 'Dark Samus'
    return stage_math(character, character2)
def YoshiCallBack():
    global character
    character = 'Yoshi'
def YoshiCallBack2():
    character2 = 'Yoshi'
    return stage_math(character, character2)
def KirbyCallBack():
    global character
    character = 'Kirby'
def KirbyCallBack2():
    character2 = 'Kirby'
    return stage_math(character, character2)
def FoxCallBack():
    global character
    character = 'Fox'
def FoxCallBack2():
    character2 = 'Fox'
    return stage_math(character, character2)
def PikachuCallBack():
    global character
    character = 'Pikachu'
def PikachuCallBack2():
    character2 = 'Pikachu'
    return stage_math(character, character2)
def LuigiCallBack():
    global character
    character = 'Luigi'
def LuigiCallBack2():
    character2 = 'Luigi'
    return stage_math(character, character2)
def NessCallBack():
    global character
    character = 'Ness'
def NessCallBack2():
    character2 = 'Ness'
    return stage_math(character, character2)
def CaptainFalconCallBack():
    global character
    character = 'Captain Falcon'
def CaptainFalconCallBack2():
    character2 = 'Captain Falcon'
    return stage_math(character, character2)
def JigglypuffCallBack():
    global character
    character = 'Jigglypuff'
def JigglypuffCallBack2():
    character2 = 'Jigglypuff'
    return stage_math(character, character2)
def PeachCallBack():
    global character
    character = 'Peach'
def PeachCallBack2():
    character2 = 'Peach'
    return stage_math(character, character2)
def DaisyCallBack():
    global character
    character = 'Daisy'
def DaisyCallBack2():
    character2 = 'Daisy'
    return stage_math(character, character2)
def BowserCallBack():
    global character
    character = 'Bowser'
def BowserCallBack2():
    character2 = 'Bowser'
    return stage_math(character, character2)
def IceClimbersCallBack():
    global character
    character = 'Ice Climbers'
def IceClimbersCallBack2():
    character2 = 'Ice Climbers'
    return stage_math(character, character2)
def SheikCallBack():
    global character
    character = 'Sheik'
def SheikCallBack2():
    character2 = 'Sheik'
    return stage_math(character, character2)
def ZeldaCallBack():
    global character
    character = 'Zelda'
def ZeldaCallBack2():
    character2 = 'Zelda'
    return stage_math(character, character2)
def DrMarioCallBack():
    global character
    character = 'Dr. Mario'
def DrMarioCallBack2():
    character2 = 'Dr. Mario'
    return stage_math(character, character2)
def PichuCallBack():
    global character
    character = 'Pichu'
def PichuCallBack2():
    character2 = 'Pichu'
    return stage_math(character, character2)
def FalcoCallBack():
    global character
    character = 'Falco'
def FalcoCallBack2():
    character2 = 'Falco'
    return stage_math(character, character2)
def MarthCallBack():
    global character
    character = 'Marth'
def MarthCallBack2():
    character2 = 'Marth'
    return stage_math(character, character2)
def LucinaCallBack():
    global character
    character = 'Lucina'
def LucinaCallBack2():
    character2 = 'Lucina'
    return stage_math(character, character2)
def YoungLinkCallBack():
    global character
    character = 'Young Link'
def YoungLinkCallBack2():
    character2 = 'Young Link'
    return stage_math(character, character2)
def GanondorfCallBack():
    global character
    character = 'Ganondorf'
def GanondorfCallBack2():
    character2 = 'Ganondorf'
    return stage_math(character, character2)
def MewtwoCallBack():
    global character
    character = 'Mewtwo'
def MewtwoCallBack2():
    character2 = 'Mewtwo'
    return stage_math(character, character2)
def RoyCallBack():
    global character
    character = 'Roy'
def RoyCallBack2():
    character2 = 'Roy'
    return stage_math(character, character2)
def ChromCallBack():
    global character
    character = 'Chrom'
def ChromCallBack2():
    character2 = 'Chrom'
    return stage_math(character, character2)
def MrGameNWatchCallBack():
    global character
    character = 'Mr. Game & Watch'
def MrGameNWatchCallBack2():
    character2 = 'Mr. Game & Watch'
    return stage_math(character, character2)
def MetaKnightCallBack():
    global character
    character = 'Meta Knight'
def MetaKnightCallBack2():
    character2 = 'Meta Knight'
    return stage_math(character, character2)
def PitCallBack():
    global character
    character = 'Pit'
def PitCallBack2():
    character2 = 'Pit'
    return stage_math(character, character2)
def DarkPitCallBack():
    global character
    character = 'Dark Pit'
def DarkPitCallBack2():
    character2 = 'Dark Pit'
    return stage_math(character, character2)
def ZeroSuitSamusCallBack():
    global character
    character = 'Zero Suit Samus'
def ZeroSuitSamusCallBack2():
    character2 = 'Zero Suit Samus'
    return stage_math(character, character2)
def WarioCallBack():
    global character
    character = 'Wario'
def WarioCallBack2():
    character2 = 'Wario'
    return stage_math(character, character2)
def SnakeCallBack():
    global character
    character = 'Snake'
def SnakeCallBack2():
    character2 = 'Snake'
    return stage_math(character, character2)
def IkeCallBack():
    global character
    character = 'Ike'
def IkeCallBack2():
    character2 = 'Ike'
    return stage_math(character, character2)
def PokemonTrainerCallBack():
    global character
    character = 'Pokemon Trainer'
def PokemonTrainerCallBack2():
    character2 = 'Pokemon Trainer'
    return stage_math(character, character2)
def DiddyKongCallBack():
    global character
    character = 'Diddy Kong'
def DiddyKongCallBack2():
    character2 = 'Diddy Kong'
    return stage_math(character, character2)
def LucasCallBack():
    global character
    character = 'Lucas'
def LucasCallBack2():
    character2 = 'Lucas'
    return stage_math(character, character2)
def SonicCallBack():
    global character
    character = 'Sonic'
def SonicCallBack2():
    character2 = 'Sonic'
    return stage_math(character, character2)
def KingDededeCallBack():
    global character
    character = 'King Dedede'
def KingDededeCallBack2():
    character2 = 'King Dedede'
    return stage_math(character, character2)
def OlimarCallBack():
    global character
    character = 'Olimar'
def OlimarCallBack2():
    character2 = 'Olimar'
    return stage_math(character, character2)
def LucarioCallBack():
    global character
    character = 'Lucario'
def LucarioCallBack2():
    character2 = 'Lucario'
    return stage_math(character, character2)
def ROBCallBack():
    global character
    character = 'R.O.B.'
def ROBCallBack2():
    character2 = 'R.O.B.'
    return stage_math(character, character2)
def ToonLinkCallBack():
    global character
    character = 'Toon Link'
def ToonLinkCallBack2():
    character2 = 'Toon Link'
    return stage_math(character, character2)
def WolfCallBack():
    global character
    character = 'Wolf'
def WolfCallBack2():
    character2 = 'Wolf'
    return stage_math(character, character2)
def VillagerCallBack():
    global character
    character = 'Villager'
def VillagerCallBack2():
    character2 = 'Villager'
    return stage_math(character, character2)
def MegaManCallBack():
    global character
    character = 'Mega Man'
def MegaManCallBack2():
    character2 = 'Mega Man'
    return stage_math(character, character2)
def WiiFitTrainerCallBack():
    global character
    character = 'Wii Fit Trainer'
def WiiFitTrainerCallBack2():
    character2 = 'Wii Fit Trainer'
    return stage_math(character, character2)
def RosalinaNLumaCallBack():
    global character
    character = 'Rosalina & Luma'
def RosalinaNLumaCallBack2():
    character2 = 'Rosalina & Luma'
    return stage_math(character, character2)
def LittleMacCallBack():
    global character
    character = 'Little Mac'
def LittleMacCallBack2():
    character2 = 'Little Mac'
    return stage_math(character, character2)
def GreninjaCallBack():
    global character
    character = 'Greninja'
def GreninjaCallBack2():
    character2 = 'Greninja'
    return stage_math(character, character2)
def PalutenaCallBack():
    global character
    character = 'Palutena'
def PalutenaCallBack2():
    character2 = 'Palutena'
    return stage_math(character, character2)
def PacManCallBack():
    global character
    character = 'Pac-Man'
def PacManCallBack2():
    character2 = 'Pac-Man'
    return stage_math(character, character2)
def RobinCallBack():
    global character
    character = 'Robin'
def RobinCallBack2():
    character2 = 'Robin'
    return stage_math(character, character2)
def ShulkCallBack():
    global character
    character = 'Shulk'
def ShulkCallBack2():
    character2 = 'Shulk'
    return stage_math(character, character2)
def BowserJrCallBack():
    global character
    character = 'Bowser Jr.'
def BowserJrCallBack2():
    character2 = 'Bowser Jr.'
    return stage_math(character, character2)
def DuckHuntCallBack():
    global character
    character = 'Duck Hunt'
def DuckHuntCallBack2():
    character2 = 'Duck Hunt'
    return stage_math(character, character2)
def RyuCallBack():
    global character
    character = 'Ryu'
def RyuCallBack2():
    character2 = 'Ryu'
    return stage_math(character, character2)
def KenCallBack():
    global character
    character = 'Ken'
def KenCallBack2():
    character2 = 'Ken'
    return stage_math(character, character2)
def CloudCallBack():
    global character
    character = 'Cloud'
def CloudCallBack2():
    character2 = 'Cloud'
    return stage_math(character, character2)
def CorrinCallBack():
    global character
    character = 'Corrin'
def CorrinCallBack2():
    character2 = 'Corrin'
    return stage_math(character, character2)
def BayonettaCallBack():
    global character
    character = 'Bayonetta'
def BayonettaCallBack2():
    character2 = 'Bayonetta'
    return stage_math(character, character2)
def InklingCallBack():
    global character
    character = 'Inkling'
def InklingCallBack2():
    character2 = 'Inkling'
    return stage_math(character, character2)
def RidleyCallBack():
    global character
    character = 'Ridley'
def RidleyCallBack2():
    character2 = 'Ridley'
    return stage_math(character, character2)
def SimonCallBack():
    global character
    character = 'Simon'
def SimonCallBack2():
    character2 = 'Simon'
    return stage_math(character, character2)
def RichterCallBack():
    global character
    character = 'Richter'
def RichterCallBack2():
    character2 = 'Richter'
    return stage_math(character, character2)
def KingKRoolCallBack():
    global character
    character = 'King K. Rool'
def KingKRoolCallBack2():
    character2 = 'King K. Rool'
    return stage_math(character, character2)
def IsabelleCallBack():
    global character
    character = 'Isabelle'
def IsabelleCallBack2():
    character2 = 'Isabelle'
    return stage_math(character, character2)
def IncineroarCallBack():
    global character
    character = 'Incineroar'
def IncineroarCallBack2():
    character2 = 'Incineroar'
    return stage_math(character, character2)
def PiranhaPlantCallBack():
    global character
    character = 'Piranha Plant'
def PiranhaPlantCallBack2():
    character2 = 'Piranha Plant'
    return stage_math(character, character2)
def JokerCallBack():
    global character
    character = 'Joker'
def JokerCallBack2():
    character2 = 'Joker'
    return stage_math(character, character2)
def HeroCallBack():
    global character
    character = 'Hero'
def HeroCallBack2():
    character2 = 'Hero'
    return stage_math(character, character2)
def BanjoNKazooieCallBack():
    global character
    character = 'Banjo & Kazooie'
def BanjoNKazooieCallBack2():
    character2 = 'Banjo & Kazooie'
    return stage_math(character, character2)
def TerryCallBack():
    global character
    character = 'Terry'
def TerryCallBack2():
    character2 = 'Terry'
    return stage_math(character, character2)
def BylethCallBack():
    global character
    character = 'Byleth'
def BylethCallBack2():
    character2 = 'Byleth'
    return stage_math(character, character2)
def MinMinCallBack():
    global character
    character = 'Min Min'
def MinMinCallBack2():
    character2 = 'Min Min'
    return stage_math(character, character2)
def SteveCallBack():
    global character
    character = 'Steve'
def SteveCallBack2():
    character2 = 'Steve'
    return stage_math(character, character2)
def SephirothCallBack():
    global character
    character = 'Sephiroth'
def SephirothCallBack2():
    character2 = 'Sephiroth'
    return stage_math(character, character2)
def PyraMythraCallBack():
    global character
    character = 'Pyra/Mythra'
def PyraMythraCallBack2():
    character2 = 'Pyra/Mythra'
    return stage_math(character, character2)
def KazuyaCallBack():
    global character
    character = 'Kazuya'
def KazuyaCallBack2():
    character2 = 'Kazuya'
    return stage_math(character, character2)
def SoraCallBack():
    global character
    character = 'Sora'
def SoraCallBack2():
    character2 = 'Sora'
    return stage_math(character, character2)
def MiiBrawlerCallBack():
    global character
    character = 'Mii Brawler'
def MiiBrawlerCallBack2():
    character2 = 'Mii Brawler'
    return stage_math(character, character2)
def MiiSwordfighterCallBack():
    global character
    character = 'Mii Swordfighter'
def MiiSwordfighterCallBack2():
    character2 = 'Mii Swordfighter'
    return stage_math(character, character2)
def MiiGunnerCallBack():
    global character
    character = 'Mii Gunner'
def MiiGunnerCallBack2():
    character2 = 'Mii Gunner'
    return stage_math(character, character2)

# reading the image
background = tk.Label(root, image = img)
words = tk.Label(root, text= 'Select your character!')
MarioButton = tk.Button(root, command=MarioCallBack)
DKButton = tk.Button(root, command=DKCallBack)
LinkButton = tk.Button(root, command=LinkCallBack)
SamusButton = tk.Button(root, command=SamusCallBack)
DarkSamusButton = tk.Button(root, command=DarkSamusCallBack)
YoshiButton = tk.Button(root, command=YoshiCallBack)
KirbyButton = tk.Button(root, command=KirbyCallBack)
FoxButton = tk.Button(root, command=FoxCallBack)
PikachuButton = tk.Button(root, command=PikachuCallBack)
LuigiButton = tk.Button(root, command=LuigiCallBack)
NessButton = tk.Button(root, command=NessCallBack)
CaptainFalconButton = tk.Button(root, command=CaptainFalconCallBack)
JigglypuffButton = tk.Button(root, command=JigglypuffCallBack)
PeachButton = tk.Button(root, command=PeachCallBack)
DaisyButton = tk.Button(root, command=DaisyCallBack)
BowserButton = tk.Button(root, command=BowserCallBack)
IceClimbersButton = tk.Button(root, command=IceClimbersCallBack)
SheikButton = tk.Button(root, command=SheikCallBack)
ZeldaButton = tk.Button(root, command=ZeldaCallBack)
DrMarioButton = tk.Button(root, command=DrMarioCallBack)
PichuButton = tk.Button(root, command=PichuCallBack)
FalcoButton = tk.Button(root, command=FalcoCallBack)
MarthButton = tk.Button(root, command=MarthCallBack)
LucinaButton = tk.Button(root, command=LucinaCallBack)
YoungLinkButton = tk.Button(root, command=YoungLinkCallBack)
GanondorfButton = tk.Button(root, command=GanondorfCallBack)
MewtwoButton = tk.Button(root, command=MewtwoCallBack)
RoyButton = tk.Button(root, command=RoyCallBack)
ChromButton = tk.Button(root, command=ChromCallBack)
MrGameNWatchButton = tk.Button(root, command=MrGameNWatchCallBack)
MetaKnightButton = tk.Button(root, command=MetaKnightCallBack)
PitButton = tk.Button(root, command=PitCallBack)
DarkPitButton = tk.Button(root, command=DarkPitCallBack)
ZeroSuitSamusButton = tk.Button(root, command=ZeroSuitSamusCallBack)
WarioButton = tk.Button(root, command=WarioCallBack)
SnakeButton = tk.Button(root, command=SnakeCallBack)
IkeButton = tk.Button(root, command=IkeCallBack)
PokemonTrainerButton = tk.Button(root, command=PokemonTrainerCallBack)
DiddyKongButton = tk.Button(root, command=DiddyKongCallBack)
LucasButton = tk.Button(root, command=LucasCallBack)
SonicButton = tk.Button(root, command=SonicCallBack)
KingDededeButton = tk.Button(root, command=KingDededeCallBack)
OlimarButton = tk.Button(root, command=OlimarCallBack)
LucarioButton = tk.Button(root, command=LucarioCallBack)
ROBButton = tk.Button(root, command=ROBCallBack)
ToonLinkButton = tk.Button(root, command=ToonLinkCallBack)
WolfButton = tk.Button(root, command=WolfCallBack)
VillagerButton = tk.Button(root, command=VillagerCallBack)
MegaManButton = tk.Button(root, command=MegaManCallBack)
WiiFitTrainerButton = tk.Button(root, command=WiiFitTrainerCallBack)
RosalinaNLumaButton = tk.Button(root, command=RosalinaNLumaCallBack)
LittleMacButton = tk.Button(root, command=LittleMacCallBack)
GreninjaButton = tk.Button(root, command=GreninjaCallBack)
PalutenaButton = tk.Button(root, command=PalutenaCallBack)
PacManButton = tk.Button(root, command=PacManCallBack)
RobinButton = tk.Button(root, command=RobinCallBack)
ShulkButton = tk.Button(root, command=ShulkCallBack)
BowserJrButton = tk.Button(root, command=BowserJrCallBack)
DuckHuntButton = tk.Button(root, command=DuckHuntCallBack)
RyuButton = tk.Button(root, command=RyuCallBack)
KenButton = tk.Button(root, command=KenCallBack)
CloudButton = tk.Button(root, command=CloudCallBack)
CorrinButton = tk.Button(root, command=CorrinCallBack)
BayonettaButton = tk.Button(root, command=BayonettaCallBack)
InklingButton = tk.Button(root, command=InklingCallBack)
RidleyButton = tk.Button(root, command=RidleyCallBack)
SimonButton = tk.Button(root, command=SimonCallBack)
RichterButton = tk.Button(root, command=RichterCallBack)
KingKRoolButton = tk.Button(root, command=KingKRoolCallBack)
IsabelleButton = tk.Button(root, command=IsabelleCallBack)
IncineroarButton = tk.Button(root, command=IncineroarCallBack)
PiranhaPlantButton = tk.Button(root, command=PiranhaPlantCallBack)
JokerButton = tk.Button(root, command=JokerCallBack)
HeroButton = tk.Button(root, command=HeroCallBack)
BanjoNKazooieButton = tk.Button(root, command=BanjoNKazooieCallBack)
TerryButton = tk.Button(root, command=TerryCallBack)
BylethButton = tk.Button(root, command=BylethCallBack)
MinMinButton = tk.Button(root, command=MinMinCallBack)
SteveButton = tk.Button(root, command=SteveCallBack)
SephirothButton = tk.Button(root, command=SephirothCallBack)
PyraMythraButton = tk.Button(root, command=PyraMythraCallBack)
KazuyaButton = tk.Button(root, command=KazuyaCallBack)
SoraButton = tk.Button(root, command=SoraCallBack)
MiiBrawlerButton = tk.Button(root, command=MiiBrawlerCallBack)
MiiSwordfighterButton = tk.Button(root, command=MiiSwordfighterCallBack)
MiiGunnerButton = tk.Button(root, command=MiiGunnerCallBack)

# setting the application
background.pack(side = "bottom", fill = "both", expand = "yes")
words.pack(side = 'top')
MarioButton.place(x=10, y=30)
DKButton.place(x=100, y=30)
LinkButton.place(x=190, y=30)
SamusButton.place(x=290, y=30)
DarkSamusButton.place(x=380, y=30)
YoshiButton.place(x=470, y=30)
KirbyButton.place(x=560, y=30)
FoxButton.place(x=660, y=30)
PikachuButton.place(x=750, y=30)
LuigiButton.place(x=840, y=30)
NessButton.place(x=930, y=30)
CaptainFalconButton.place(x=1020, y=30)
JigglypuffButton.place(x=1110, y=30)
PeachButton.place(x=10, y=90)
DaisyButton.place(x=100, y=90)
BowserButton.place(x=190, y=90)
IceClimbersButton.place(x=290, y=90)
SheikButton.place(x=380, y=90)
ZeldaButton.place(x=470, y=90)
DrMarioButton.place(x=560, y=90)
PichuButton.place(x=660, y=90)
FalcoButton.place(x=750, y=90)
MarthButton.place(x=840, y=90)
LucinaButton.place(x=930, y=90)
YoungLinkButton.place(x=1020, y=90)
GanondorfButton.place(x=1110, y=90)
MewtwoButton.place(x=10, y=140)
RoyButton.place(x=100, y=140)
ChromButton.place(x=190, y=140)
MrGameNWatchButton.place(x=290, y=140)
MetaKnightButton.place(x=380, y=140)
PitButton.place(x=470, y=140)
DarkPitButton.place(x=560, y=140)
ZeroSuitSamusButton.place(x=660, y=140)
WarioButton.place(x=750, y=140)
SnakeButton.place(x=840, y=140)
IkeButton.place(x=930, y=140)
PokemonTrainerButton.place(x=1020, y=140)
DiddyKongButton.place(x=1110, y=140)
LucasButton.place(x=10, y=190)
SonicButton.place(x=100, y=190)
KingDededeButton.place(x=190, y=190)
OlimarButton.place(x=290, y=190)
LucarioButton.place(x=380, y=190)
ROBButton.place(x=470, y=190)
ToonLinkButton.place(x=560, y=190)
WolfButton.place(x=660, y=190)
VillagerButton.place(x=750, y=190)
MegaManButton.place(x=840, y=190)
WiiFitTrainerButton.place(x=930, y=190)
RosalinaNLumaButton.place(x=1020, y=190)
LittleMacButton.place(x=1110, y=190)
GreninjaButton.place(x=10, y=250)
PalutenaButton.place(x=100, y=250)
PacManButton.place(x=190, y=250)
RobinButton.place(x=290, y=250)
ShulkButton.place(x=380, y=250)
BowserJrButton.place(x=470, y=250)
DuckHuntButton.place(x=560, y=250)
RyuButton.place(x=660, y=250)
KenButton.place(x=750, y=250)
CloudButton.place(x=840, y=250)
CorrinButton.place(x=930, y=250)
BayonettaButton.place(x=1020, y=250)
InklingButton.place(x=1110, y=250)
RidleyButton.place(x=10, y=290)
SimonButton.place(x=100, y=290)
RichterButton.place(x=190, y=290)
KingKRoolButton.place(x=290, y=290)
IsabelleButton.place(x=380, y=290)
IncineroarButton.place(x=470, y=290)
PiranhaPlantButton.place(x=560, y=290)
JokerButton.place(x=660, y=290)
HeroButton.place(x=750, y=290)
BanjoNKazooieButton.place(x=840, y=290)
TerryButton.place(x=930, y=290)
BylethButton.place(x=1020, y=290)
MinMinButton.place(x=1110, y=290)
SteveButton.place(x=190, y=340)
SephirothButton.place(x=290, y=340)
PyraMythraButton.place(x=380, y=340)
KazuyaButton.place(x=470, y=340)
SoraButton.place(x=560, y=340)
MiiBrawlerButton.place(x=660, y=340)
MiiSwordfighterButton.place(x=750, y=340)
MiiGunnerButton.place(x=840, y=340)

newWindow = tk.Toplevel(root)
tk.Label(newWindow, text= 'Select opponent character!').pack(side='top')
tk.Label(newWindow, image= img).pack(side = "bottom", fill = "both", expand = "yes")
tk.Button(newWindow, command = MarioCallBack2).place(x=10, y=30)
tk.Button(newWindow, command = DKCallBack2).place(x=100, y=30)
tk.Button(newWindow, command = LinkCallBack2).place(x=190, y=30)
tk.Button(newWindow, command = SamusCallBack2).place(x=290, y=30)
tk.Button(newWindow, command = DarkSamusCallBack2).place(x=380, y=30)
tk.Button(newWindow, command = YoshiCallBack2).place(x=470, y=30)
tk.Button(newWindow, command = KirbyCallBack2).place(x=560, y=30)
tk.Button(newWindow, command = FoxCallBack2).place(x=660, y=30)
tk.Button(newWindow, command = PikachuCallBack2).place(x=750, y=30)
tk.Button(newWindow, command = LuigiCallBack2).place(x=840, y=30)
tk.Button(newWindow, command = NessCallBack2).place(x=930, y=30)
tk.Button(newWindow, command = CaptainFalconCallBack2).place(x=1020, y=30)
tk.Button(newWindow, command = JigglypuffCallBack2).place(x=1110, y=30)
tk.Button(newWindow, command = PeachCallBack2).place(x=10, y=90)
tk.Button(newWindow, command = DaisyCallBack2).place(x=100, y=90)
tk.Button(newWindow, command = BowserCallBack2).place(x=190, y=90)
tk.Button(newWindow, command = IceClimbersCallBack2).place(x=290, y=90)
tk.Button(newWindow, command = SheikCallBack2).place(x=380, y=90)
tk.Button(newWindow, command = ZeldaCallBack2).place(x=470, y=90)
tk.Button(newWindow, command = DrMarioCallBack2).place(x=560, y=90)
tk.Button(newWindow, command = PichuCallBack2).place(x=660, y=90)
tk.Button(newWindow, command = FalcoCallBack2).place(x=750, y=90)
tk.Button(newWindow, command = MarthCallBack2).place(x=840, y=90)
tk.Button(newWindow, command = LucinaCallBack2).place(x=930, y=90)
tk.Button(newWindow, command = YoungLinkCallBack2).place(x=1020, y=90)
tk.Button(newWindow, command = GanondorfCallBack2).place(x=1110, y=90)
tk.Button(newWindow, command = MewtwoCallBack2).place(x=10, y=140)
tk.Button(newWindow, command = RoyCallBack2).place(x=100, y=140)
tk.Button(newWindow, command = ChromCallBack2).place(x=190, y=140)
tk.Button(newWindow, command = MrGameNWatchCallBack2).place(x=290, y=140)
tk.Button(newWindow, command = MetaKnightCallBack2).place(x=380, y=140)
tk.Button(newWindow, command = PitCallBack2).place(x=470, y=140)
tk.Button(newWindow, command = DarkPitCallBack2).place(x=560, y=140)
tk.Button(newWindow, command = ZeroSuitSamusCallBack2).place(x=660, y=140)
tk.Button(newWindow, command = WarioCallBack2).place(x=750, y=140)
tk.Button(newWindow, command = SnakeCallBack2).place(x=840, y=140)
tk.Button(newWindow, command = IkeCallBack2).place(x=930, y=140)
tk.Button(newWindow, command = PokemonTrainerCallBack2).place(x=1020, y=140)
tk.Button(newWindow, command = DiddyKongCallBack2).place(x=1110, y=140)
tk.Button(newWindow, command = LucasCallBack2).place(x=10, y=190)
tk.Button(newWindow, command = SonicCallBack2).place(x=100, y=190)
tk.Button(newWindow, command = KingDededeCallBack2).place(x=190, y=190)
tk.Button(newWindow, command = OlimarCallBack2).place(x=290, y=190)
tk.Button(newWindow, command = LucarioCallBack2).place(x=380, y=190)
tk.Button(newWindow, command = ROBCallBack2).place(x=470, y=190)
tk.Button(newWindow, command = ToonLinkCallBack2).place(x=560, y=190)
tk.Button(newWindow, command = WolfCallBack2).place(x=660, y=190)
tk.Button(newWindow, command = VillagerCallBack2).place(x=750, y=190)
tk.Button(newWindow, command = MegaManCallBack2).place(x=840, y=190)
tk.Button(newWindow, command = WiiFitTrainerCallBack2).place(x=930, y=190)
tk.Button(newWindow, command = RosalinaNLumaCallBack2).place(x=1020, y=190)
tk.Button(newWindow, command = LittleMacCallBack2).place(x=1110, y=190)
tk.Button(newWindow, command = GreninjaCallBack2).place(x=10, y=250)
tk.Button(newWindow, command = PalutenaCallBack2).place(x=100, y=250)
tk.Button(newWindow, command = PacManCallBack2).place(x=190, y=250)
tk.Button(newWindow, command = RobinCallBack2).place(x=290, y=250)
tk.Button(newWindow, command = ShulkCallBack2).place(x=380, y=250)
tk.Button(newWindow, command = BowserJrCallBack2).place(x=470, y=250)
tk.Button(newWindow, command = DuckHuntCallBack2).place(x=560, y=250)
tk.Button(newWindow, command = RyuCallBack2).place(x=660, y=250)
tk.Button(newWindow, command = KenCallBack2).place(x=750, y=250)
tk.Button(newWindow, command = CloudCallBack2).place(x=840, y=250)
tk.Button(newWindow, command = CorrinCallBack2).place(x=930, y=250)
tk.Button(newWindow, command = BayonettaCallBack2).place(x=1020, y=250)
tk.Button(newWindow, command = InklingCallBack2).place(x=1110, y=250)
tk.Button(newWindow, command = RidleyCallBack2).place(x=10, y=290)
tk.Button(newWindow, command = SimonCallBack2).place(x=100, y=290)
tk.Button(newWindow, command = RichterCallBack2).place(x=190, y=290)
tk.Button(newWindow, command = KingKRoolCallBack2).place(x=290, y=290)
tk.Button(newWindow, command = IsabelleCallBack2).place(x=380, y=290)
tk.Button(newWindow, command = IncineroarCallBack2).place(x=470, y=290)
tk.Button(newWindow, command = PiranhaPlantCallBack2).place(x=560, y=290)
tk.Button(newWindow, command = JokerCallBack2).place(x=660, y=290)
tk.Button(newWindow, command = HeroCallBack2).place(x=750, y=290)
tk.Button(newWindow, command = BanjoNKazooieCallBack2).place(x=840, y=290)
tk.Button(newWindow, command = TerryCallBack2).place(x=930, y=290)
tk.Button(newWindow, command = BylethCallBack2).place(x=1020, y=290)
tk.Button(newWindow, command = MinMinCallBack2).place(x=1110, y=290)
tk.Button(newWindow, command = SteveCallBack2).place(x=190, y=340)
tk.Button(newWindow, command = SephirothCallBack2).place(x=290, y=340)
tk.Button(newWindow, command = PyraMythraCallBack2).place(x=380, y=340)
tk.Button(newWindow, command = KazuyaCallBack2).place(x=470, y=340)
tk.Button(newWindow, command = SoraCallBack2).place(x=560, y=340)
tk.Button(newWindow, command = MiiBrawlerCallBack2).place(x=660, y=340)
tk.Button(newWindow, command = MiiSwordfighterCallBack2).place(x=750, y=340)
tk.Button(newWindow, command = MiiGunnerCallBack2).place(x=840, y=340)

# running the application
root.mainloop()

