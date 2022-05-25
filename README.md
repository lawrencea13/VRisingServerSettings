# VRisingServerSettings

## Made to make updating your private server simple.
## Download the current release [here.](https://github.com/lawrencea13/VRisingServerSettings/releases/tag/UIUpdate)

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
- InventoryStacksModifier
- DropTableModifiers
- MaterialYieldModifier
- EnemyContainerLoot
- BloodEssenceYieldModifer
- ClanSize
- SunDamageModifier

## I intend on adding every setting, however this will take time.

### The program is written in Python, and can be run as bare python.  I have also made a binary executable for windows so you don't have to do anything.
To run this in python, you will need to install the eel dependency with "pip install eel".

### Next Planned Settings/updates

- Visual Updates
- Dedicated Server support
- Ability to migrate from a private server to a dedicated server
- CastleMinimumDistanceInFloors
- BloodDrainModifier
- DurabilityDraginModifier
- GarlicAreaStrengthModifier
- SilverStrengthModifier
- CastleDecayRateModifier
- CastleBloodEssenceDrainModifier
- AnnounceSiegeWeaponSpawn
- BuildCostModifier
- CraftRateModifier
- RefinementCostModifier
- RefinementRateModifier
- DismantleResourceModifier
- ServantConvertRateModifier
- Death_DurabilityFactorLoss
- Death_DurabilityLossFactorAsResources

### Planned backend changed

- JS reorganization: Update the JS to align more with the output. E.g. instead of updating with different functions, incorporate the whole update page to 1 function
- Python code cleanup and rewrite: Rewrite the python so I don't need to make a "getter" and "setter" for each value, instead I can call 1 get/set function and indicate the data I'd like to pull, making adding future settings a lot easier.

### Fixed Bugs

- Previously would open only in chrome, now it will open in default browser
- Will crash or hand if loading invalid data, rather than handle the exception.  Now it will not crash if data is not valid, it will ignore that data, then create it upon next save at the default state.  This can potentially fix a corrupted server if the settings prevented it from loading previously.

### Currently known issues
- If reload page too quickly, it may fail
