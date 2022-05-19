# VRisingServerSettings

## Made to make updating your private server simple.

## Please make sure to backup the entire save, including server settings, if a file is in the process of being written to, and something crashes or fails, you run the risk of losing everything.

## Currently Implemented Settings
- Server Name
- Password
- Max Players
- Game Mode
- Dead Container Looting
- Castle Damage Mode
- Castle Heart Damage Mode
- Relic Spawn Type
- Equipment Bloodbound
- Bloodbound Teleport

## I intend on adding every setting, however this will take time.

### The program is written in Python, and can be run as bare python.  I have also made a binary executable for windows so you don't have to do anything.
To run this in python, you will need to install the eel dependency with "pip install eel".

### Next Planned Settings/updates(hopefully by tomorrow)
- InventoryStacksModifier
- DropTableModifiers
- MaterialYieldModifier
- EnemyContainerLoot
- BloodEssenceYieldModifer
- ClanSize
- Considering doing 1 update button instead of separate groups.
- Visual Updates of course

### Currently known issues
- Will crash or hand if loading invalid data, rather than handle the exception
- If reload page too quickly, it may fail
