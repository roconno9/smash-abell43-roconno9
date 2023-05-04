#!/usr/bin/env python
# coding: utf-8

# In[5]:


import tkinter as tk
from PIL import ImageTk, Image
import os

# creating main window
root = tk.Tk()

# loading the image
img = ImageTk.PhotoImage(Image.open("SmashRoster.jpg"))

def MarioCallBack():
    global character
    character = 'Mario'
def MarioCallBack2():
    character2 = 'Mario'
def DKCallBack():
    global character
    character = 'Donkey Kong'
def DKCallBack2():
    character2 = 'Donkey Kong'
def LinkCallBack():
    global character
    character = 'Link'
def LinkCallBack2():
    character2 = 'Link'
def SamusCallBack():
    global character
    character = 'Samus'
def SamusCallBack2():
    character2 = 'Samus'
def DarkSamusCallBack():
    global character
    character = 'Dark Samus'
def DarkSamusCallBack2():
    character2 = 'Dark Samus'
def YoshiCallBack():
    global character
    character = 'Yoshi'
def YoshiCallBack2():
    character2 = 'Yoshi'
def KirbyCallBack():
    global character
    character = 'Kirby'
def KirbyCallBack2():
    character2 = 'Kirby'
def FoxCallBack():
    global character
    character = 'Fox'
def FoxCallBack2():
    character2 = 'Fox'
def PikachuCallBack():
    global character
    character = 'Pikachu'
def PikachuCallBack2():
    character2 = 'Pikachu'
def LuigiCallBack():
    global character
    character = 'Luigi'
def LuigiCallBack2():
    character2 = 'Luigi'
def NessCallBack():
    global character
    character = 'Ness'
def NessCallBack2():
    character2 = 'Ness'
def CaptainFalconCallBack():
    global character
    character = 'Captain Falcon'
def CaptainFalconCallBack2():
    character2 = 'Captain Falcon'
def JigglypuffCallBack():
    global character
    character = 'Jigglypuff'
def JigglypuffCallBack2():
    character2 = 'Jigglypuff'
def PeachCallBack():
    global character
    character = 'Peach'
def PeachCallBack2():
    character2 = 'Peach'
def DaisyCallBack():
    global character
    character = 'Daisy'
def DaisyCallBack2():
    character2 = 'Daisy'
def BowserCallBack():
    global character
    character = 'Bowser'
def BowserCallBack2():
    character2 = 'Bowser'
def IceClimbersCallBack():
    global character
    character = 'Ice Climbers'
def IceClimbersCallBack2():
    character2 = 'Ice Climbers'
def SheikCallBack():
    global character
    character = 'Sheik'
def SheikCallBack2():
    character2 = 'Sheik'
def ZeldaCallBack():
    global character
    character = 'Zelda'
def ZeldaCallBack2():
    character2 = 'Zelda'
def DrMarioCallBack():
    global character
    character = 'Dr. Mario'
def DrMarioCallBack2():
    character2 = 'Dr. Mario'
def PichuCallBack():
    global character
    character = 'Pichu'
def PichuCallBack2():
    character2 = 'Pichu'
def FalcoCallBack():
    global character
    character = 'Falco'
def FalcoCallBack2():
    character2 = 'Falco'
def MarthCallBack():
    global character
    character = 'Marth'
def MarthCallBack2():
    character2 = 'Marth'
def LucinaCallBack():
    global character
    character = 'Lucina'
def LucinaCallBack2():
    character2 = 'Lucina'
def YoungLinkCallBack():
    global character
    character = 'YoungLink'
def YoungLinkCallBack2():
    character2 = 'YoungLink'
def GanondorfCallBack():
    global character
    character = 'Ganondorf'
def GanondorfCallBack2():
    character2 = 'Ganondorf'
def MewtwoCallBack():
    global character
    character = 'Mewtwo'
def MewtwoCallBack2():
    character2 = 'Mewtwo'
def RoyCallBack():
    global character
    character = 'Roy'
def RoyCallBack2():
    character2 = 'Roy'
def ChromCallBack():
    global character
    character = 'Chrom'
def ChromCallBack2():
    character2 = 'Chrom'
def MrGameNWatchCallBack():
    global character
    character = 'Mr. Game & Watch'
def MrGameNWatchCallBack2():
    character2 = 'Mr. Game & Watch'
def MetaKnightCallBack():
    global character
    character = 'Meta Knight'
def MetaKnightCallBack2():
    character2 = 'Meta Knight'
def PitCallBack():
    global character
    character = 'Pit'
def PitCallBack2():
    character2 = 'Pit'
def DarkPitCallBack():
    global character
    character = 'Dark Pit'
def DarkPitCallBack2():
    character2 = 'Dark Pit'
def ZeroSuitSamusCallBack():
    global character
    character = 'Zero Suit Samus'
def ZeroSuitSamusCallBack2():
    character2 = 'Zero Suit Samus'
def WarioCallBack():
    global character
    character = 'Wario'
def WarioCallBack2():
    character2 = 'Wario'
def SnakeCallBack():
    global character
    character = 'Snake'
def SnakeCallBack2():
    character2 = 'Snake'
def IkeCallBack():
    global character
    character = 'Ike'
def IkeCallBack2():
    character2 = 'Ike'
def PokemonTrainerCallBack():
    global character
    character = 'Pokemon Trainer'
def PokemonTrainerCallBack2():
    character2 = 'Pokemon Trainer'
def DiddyKongCallBack():
    global character
    character = 'Diddy Kong'
def DiddyKongCallBack2():
    character2 = 'Diddy Kong'
def LucasCallBack():
    global character
    character = 'Lucas'
def LucasCallBack2():
    character2 = 'Lucas'
def SonicCallBack():
    global character
    character = 'Sonic'
def SonicCallBack2():
    character2 = 'Sonic'
def KingDededeCallBack():
    global character
    character = 'King Dedede'
def KingDededeCallBack2():
    character2 = 'King Dedede'
def OlimarCallBack():
    global character
    character = 'Olimar'
def OlimarCallBack2():
    character2 = 'Olimar'
def LucarioCallBack():
    global character
    character = 'Lucario'
def LucarioCallBack2():
    character2 = 'Lucario'
def ROBCallBack():
    global character
    character = 'R.O.B.'
def ROBCallBack2():
    character2 = 'R.O.B.'
def ToonLinkCallBack():
    global character
    character = 'Toon Link'
def ToonLinkCallBack2():
    character2 = 'Toon Link'
def WolfCallBack():
    global character
    character = 'Wolf'
def WolfCallBack2():
    character2 = 'Wolf'
def VillagerCallBack():
    global character
    character = 'Villager'
def VillagerCallBack2():
    character2 = 'Villager'
def MegaManCallBack():
    global character
    character = 'Mega Man'
def MegaManCallBack2():
    character2 = 'Mega Man'
def WiiFitTrainerCallBack():
    global character
    character = 'Wii Fit Trainer'
def WiiFitTrainerCallBack2():
    character2 = 'Wii Fit Trainer'
def RosalinaNLumaCallBack():
    global character
    character = 'Rosalina & Luma'
def RosalinaNLumaCallBack2():
    character2 = 'Rosalina & Luma'
def LittleMacCallBack():
    global character
    character = 'Little Mac'
def LittleMacCallBack2():
    character2 = 'Little Mac'
def GreninjaCallBack():
    global character
    character = 'Greninja'
def GreninjaCallBack2():
    character2 = 'Greninja'
def PalutenaCallBack():
    global character
    character = 'Palutena'
def PalutenaCallBack2():
    character2 = 'Palutena'
def PacManCallBack():
    global character
    character = 'Pac-Man'
def PacManCallBack2():
    character2 = 'Pac-Man'
def RobinCallBack():
    global character
    character = 'Robin'
def RobinCallBack2():
    character2 = 'Robin'
def ShulkCallBack():
    global character
    character = 'Shulk'
def ShulkCallBack2():
    character2 = 'Shulk'
def BowserJrCallBack():
    global character
    character = 'Bowser Jr.'
def BowserJrCallBack2():
    character2 = 'Bowser Jr.'
def DuckHuntCallBack():
    global character
    character = 'Duck Hunt'
def DuckHuntCallBack2():
    character2 = 'Duck Hunt'
def RyuCallBack():
    global character
    character = 'Ryu'
def RyuCallBack2():
    character2 = 'Ryu'
def KenCallBack():
    global character
    character = 'Ken'
def KenCallBack2():
    character2 = 'Ken'
def CloudCallBack():
    global character
    character = 'Cloud'
def CloudCallBack2():
    character2 = 'Cloud'
def CorrinCallBack():
    global character
    character = 'Corrin'
def CorrinCallBack2():
    character2 = 'Corrin'
def BayonettaCallBack():
    global character
    character = 'Bayonetta'
def BayonettaCallBack2():
    character2 = 'Bayonetta'
def InklingCallBack():
    global character
    character = 'Inkling'
def InklingCallBack2():
    character2 = 'Inkling'
def RidleyCallBack():
    global character
    character = 'Ridley'
def RidleyCallBack2():
    character2 = 'Ridley'
def SimonCallBack():
    global character
    character = 'Simon'
def SimonCallBack2():
    character2 = 'Simon'
def RichterCallBack():
    global character
    character = 'Richter'
def RichterCallBack2():
    character2 = 'Richter'
def KingKRoolCallBack():
    global character
    character = 'King K. Rool'
def KingKRoolCallBack2():
    character2 = 'King K. Rool'
def IsabelleCallBack():
    global character
    character = 'Isabelle'
def IsabelleCallBack2():
    character2 = 'Isabelle'
def IncineroarCallBack():
    global character
    character = 'Incineroar'
def IncineroarCallBack2():
    character2 = 'Incineroar'
def PiranhaPlantCallBack():
    global character
    character = 'Piranha Plant'
def PiranhaPlantCallBack2():
    character2 = 'Piranha Plant'
def JokerCallBack():
    global character
    character = 'Joker'
def JokerCallBack2():
    character2 = 'Joker'
def HeroCallBack():
    global character
    character = 'Hero'
def HeroCallBack2():
    character2 = 'Hero'
def BanjoNKazooieCallBack():
    global character
    character = 'Banjo & Kazooie'
def BanjoNKazooieCallBack2():
    character2 = 'Banjo & Kazooie'
def TerryCallBack():
    global character
    character = 'Terry'
def TerryCallBack2():
    character2 = 'Terry'
def BylethCallBack():
    global character
    character = 'Byleth'
def BylethCallBack2():
    character2 = 'Byleth'
def MinMinCallBack():
    global character
    character = 'Min Min'
def MinMinCallBack2():
    character2 = 'Min Min'
def SteveCallBack():
    global character
    character = 'Steve'
def SteveCallBack2():
    character2 = 'Steve'
def SephirothCallBack():
    global character
    character = 'Sephiroth'
def SephirothCallBack2():
    character2 = 'Sephiroth'
def PyraMythraCallBack():
    global character
    character = 'Pyra/Mythra'
def PyraMythraCallBack2():
    character2 = 'Pyra/Mythra'
def KazuyaCallBack():
    global character
    character = 'Kazuya'
def KazuyaCallBack2():
    character2 = 'Kazuya'
def SoraCallBack():
    global character
    character = 'Sora'
def SoraCallBack2():
    character2 = 'Sora'
def MiiBrawlerCallBack():
    global character
    character = 'Mii Brawler'
def MiiBrawlerCallBack2():
    character2 = 'Mii Brawler'
def MiiSwordfighterCallBack():
    global character
    character = 'Mii Swordfighter'
def MiiSwordfighterCallBack2():
    character2 = 'Mii Swordfighter'
def MiiGunnerCallBack():
    global character
    character = 'Mii Gunner'
def MiiGunnerCallBack2():
    character2 = 'Mii Gunner'

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


# In[ ]:




