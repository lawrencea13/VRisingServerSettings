import eel
import json
import tkinter as tk
from tkinter import filedialog
import os

eel.init('web')

gameShortcut = "\\ServerGameSettings.json"
settingsShortcut = "\\ServerHostSettings.json"

# get the localLow directory where server settings are saved
baseDir = os.getenv('UserProfile') + '\\AppData\\LocalLow\\Stunlock Studios\\VRising\\Saves\\V1\\'
serverDirName = ""
game_settings_dir = ""
host_settings_dir = ""
server = {}
game = {}
local_data = {}
returned_servers = []


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
    except Exception as e:
        print(e)
        firstTimeSetup()

    saveData('localdata.txt', local_data)


def firstTimeSetup():
    """
    Trying to remove tkinter from the libraries, unless absolutely needed.
    :return:
    """
    print(os.getenv('UserProfile'))
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
        eel.start('main.html', mode='default')
    else:
        eel.start('serverselect.html', mode='default')

@eel.expose
def getServerFolders():
    global returned_servers
    returned_servers = []
    returnData = []
    for folder in os.listdir(baseDir):
        l_serverData = loadData(baseDir + "\\" + folder + settingsShortcut)
        # l_gameData = loadData(baseDir + "\\" + folder + gameShortcut)
        returnData.append(l_serverData["Name"])
        returned_servers.append(folder)

    return returnData

@eel.expose
def newSelectServer(server):
    # print(baseDir + returned_servers[server])
    attemptLoadSettings(baseDir + returned_servers[server])

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
    try:
        return server['MaxConnectedUsers']
    except:
        return 40


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
    try:
        return server["Name"]
    except:
        pass


@eel.expose
def getPVP():
    try:
        if game["GameModeType"] == 0:
            return "PVE"
        else:
            return "PVP"
    except:
        pass


@eel.expose
def setPVP(mode):
    if mode == "PVP":
        game["GameModeType"] = 1
    else:
        game["GameModeType"] = 0

    saveData(game_settings_dir, game)

@eel.expose
def getLootEnemyDContainer():
    try:
        return str(game["DeathContainerPermission"])
    except:
        pass


@eel.expose
def setLootEnemyDContainer(loot):
    game["DeathContainerPermission"] = int(loot)
    saveData(game_settings_dir, game)

@eel.expose
def getCastleMode():
    try:
        return str(game["CastleDamageMode"])
    except:
        pass


@eel.expose
def setCastleMode(mode):
    game["CastleDamageMode"] = int(mode)
    saveData(game_settings_dir, game)

@eel.expose
def getCastleHeartMode():
    try:
        return str(game["CastleHeartDamageMode"])
    except:
        pass


@eel.expose
def setCastleHeartMode(mode):
    game["CastleHeartDamageMode"] = int(mode)
    saveData(game_settings_dir, game)

@eel.expose
def getRelicSpawn():
    try:
        return game['RelicSpawnType']
    except:
        pass


@eel.expose
def setRelicSpawn(mode):
    game['RelicSpawnType'] = mode
    saveData(game_settings_dir, game)

@eel.expose
def getEquipmentBound():
    try:
        return game['BloodBoundEquipment']
    except:
        pass


@eel.expose
def setEquipmentBound(mode):
    game['BloodBoundEquipment'] = mode
    saveData(game_settings_dir, game)

@eel.expose
def getBoundTeleport():
    try:
        return game['TeleportBoundItems']
    except:
        pass


@eel.expose
def setBoundTeleport(mode):
    game['TeleportBoundItems'] = mode
    saveData(game_settings_dir, game)

@eel.expose
def getGlobalChat():
    try:
        return game['AllowGlobalChat']
    except:
        pass


@eel.expose
def setGlobalChat(mode):
    game['AllowGlobalChat'] = mode
    saveData(game_settings_dir, game)





@eel.expose
def getLootEnemyContainer():
    try:
        return game["CanLootEnemyContainers"]
    except:
        pass


@eel.expose
def setLootEnemyContainer(mode):
    game["CanLootEnemyContainers"] = mode
    saveData(game_settings_dir, game)


@eel.expose
def getInventoryStacksMod():
    try:
        return game["InventoryStacksModifier"]
    except:
        pass


@eel.expose
def setInventoryStacksMod(value):
    game["InventoryStacksModifier"] = value
    saveData(game_settings_dir, game)

@eel.expose
def getDropTableModG():
    try:
        return game["DropTableModifier_General"]
    except:
        pass


@eel.expose
def setDropTableModG(value):
    game["DropTableModifier_General"] = value
    saveData(game_settings_dir, game)

@eel.expose
def getMaterialYieldModG():
    try:
        return game["MaterialYieldModifier_Global"]
    except:
        pass


@eel.expose
def setMaterialYieldModG(value):
    game["MaterialYieldModifier_Global"] = value
    saveData(game_settings_dir, game)

@eel.expose
def getBloodEssenceYieldMod():
    try:
        return game["BloodEssenceYieldModifier"]
    except:
        pass


@eel.expose
def setBloodEssenceYieldMod(value):
    game["BloodEssenceYieldModifier"] = value
    saveData(game_settings_dir, game)

@eel.expose
def getMaxClanSize():
    try:
        return game["ClanSize"]
    except:
        return 4

@eel.expose
def setMaxClanSize(value):
    game["ClanSize"] = value
    saveData(game_settings_dir, game)

@eel.expose
def setSunDamage(value):
    game["SunDamageModifier"] = value
    saveData(game_settings_dir, game)

@eel.expose
def getSunDamage():
    try:
        return game["SunDamageModifier"]
    except:
        pass


main()


