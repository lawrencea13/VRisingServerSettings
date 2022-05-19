import eel
import json
import tkinter as tk
from tkinter import filedialog
import os

eel.init('web')

# get the localLow directory where server settings are saved
baseDir = os.path.join(os.getenv('APPDATA'), '..\\LocalLow\\Stunlock Studios\\VRising\\Saves\\V1')
serverDirName = ""
game_settings_dir = ""
host_settings_dir = ""
server = {}
game = {}
local_data = {}


root = tk.Tk()
root.attributes('-topmost', True)
root.withdraw()

def loadData(serversettings):
    with open(serversettings, 'r') as f:
        s = f.read()
        data = json.loads(s)

    return data

def saveData(file, data):
    with open(file, 'w') as f:
        str = json.dumps(data)
        f.write(str)


def attemptLoadSettings(folder):
    global game_settings_dir
    global host_settings_dir
    global serverDirName
    global local_data
    global server
    global game
    game_settings_dir = folder + "\\ServerGameSettings.json"
    host_settings_dir = folder + "\\ServerHostSettings.json"
    try:
        server = loadData(host_settings_dir)
        game = loadData(game_settings_dir)
        serverDirName = os.path.basename(os.path.dirname(host_settings_dir))
        local_data['path'] = serverDirName
    except:
        firstTimeSetup()

    saveData('localdata.txt', local_data)


def firstTimeSetup():
    folder_selected = filedialog.askdirectory(initialdir=baseDir)
    if folder_selected == "":
        exit()
    else:
        root.destroy()
        attemptLoadSettings(folder_selected)


def main():
    # print(os.path.exists("localdata.txt"))
    global baseDir
    if os.path.exists("localdata.txt"):
        global local_data
        local_data = loadData("localdata.txt")
        attemptLoadSettings(os.path.join(baseDir, local_data['path']))
    else:
        firstTimeSetup()


@eel.expose
def getPassword():
    try:
        return server['Password']
    except:
        return ""

@eel.expose
def setPassword(password):
    print("called")
    if password == "":
        return
    else:
        server["Password"] = password
    saveData(host_settings_dir, server)

@eel.expose
def changeSelectedFolder():
    global root
    try:
        root.destroy()
    except:
        pass
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    folder_selected = filedialog.askdirectory(initialdir=baseDir)
    root.destroy()
    if folder_selected == "":
        pass
    else:
        attemptLoadSettings(folder_selected)

@eel.expose
def getServerMaxPlayers():
    return server['MaxConnectedUsers']


@eel.expose
def updateHostSettings(name=None, maxUsers=None):
    if name is not None:
        server['Name'] = name
    if maxUsers is not None:
        try:
            int(maxUsers)
            server['MaxConnectedUsers'] = int(maxUsers)
        except:
            pass

    saveData(host_settings_dir, server)


@eel.expose
def getTitle():
    return server["Name"]


@eel.expose
def getPVP():
    if game["GameModeType"] == 0:
        return "PVE"
    else:
        return "PVP"


@eel.expose
def setPVP(mode):
    if mode == "PVP":
        game["GameModeType"] = 1
    else:
        game["GameModeType"] = 0

    saveData(game_settings_dir, game)

@eel.expose
def getLootEnemyContainer():
    return str(game["DeathContainerPermission"])

@eel.expose
def setLootEnemyContainer(loot):
    game["DeathContainerPermission"] = int(loot)
    saveData(game_settings_dir, game)

@eel.expose
def getCastleMode():
    return str(game["CastleDamageMode"])

@eel.expose
def setCastleMode(mode):
    game["CastleDamageMode"] = int(mode)
    saveData(game_settings_dir, game)

@eel.expose
def getCastleHeartMode():
    return str(game["CastleHeartDamageMode"])

@eel.expose
def setCastleHeartMode(mode):
    game["CastleHeartDamageMode"] = int(mode)
    saveData(game_settings_dir, game)

@eel.expose
def getRelicSpawn():
    return game['RelicSpawnType']


@eel.expose
def setRelicSpawn(mode):
    game['RelicSpawnType'] = mode
    saveData(game_settings_dir, game)

@eel.expose
def getEquipmentBound():
    return game['BloodBoundEquipment']

@eel.expose
def setEquipmentBound(mode):
    game['BloodBoundEquipment'] = mode
    saveData(game_settings_dir, game)

@eel.expose
def getBoundTeleport():
    return game['TeleportBoundItems']

@eel.expose
def setBoundTeleport(mode):
    game['TeleportBoundItems'] = mode
    saveData(game_settings_dir, game)

@eel.expose
def getGlobalChat():
    return game['AllowGlobalChat']

@eel.expose
def setGlobalChat(mode):
    game['AllowGlobalChat'] = mode
    saveData(game_settings_dir, game)


main()

eel.start('main.html')





