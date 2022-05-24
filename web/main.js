function update(){
    var serverName = document.getElementById('serverName').value;
    var maxPlayers = document.getElementById('maxPlayers').value;
    eel.updateHostSettings(serverName, maxPlayers);
    eel.setGlobalChat(document.getElementById('globalChat').checked);
    if (document.getElementById("serverPass").value != ""){
        eel.setPassword(document.getElementById("serverPass").value)
    }

    updateYields()
    updatePVP()
    updateBoundItems()
}

async function changeServerType() {
//    var dedicatedServer = await eel.getServerMode()();
//    eel.setServerMode(!dedicatedServer);
//    location.reload();
}


function changeServer() {
    eel.changeSelectedFolder();
    location.reload();
}

async function setup() {
    document.getElementById("showPass").checked = false;
//    var dedicatedServer = await eel.getServerMode()();

//    dedicated server setup
//    var serverModeButton = document.getElementById("serverTypeButton");
//    var modalText = document.getElementById("popupText");

//    console.log(dedicatedServer)
//
//    if (dedicatedServer) {
//        serverModeButton.innerHTML = "Dedicated";
//        modalText.innerHTML = "Are you sure you'd like to change server mode? This will not affect your server, but will change this application to Private mode.";
//    }
//    else{ serverModeButton.innerHTML = "Private"; modalText.innerHTML = "Are you sure you'd like to change server mode? This will not affect your server, but will change this application to Dedicated mode."; };
//

//    end dedicated server setup
    var title = await eel.getTitle()();
    var pvp = await eel.getPVP()();
    var castleMode = await eel.getCastleMode()();
    var castleHeartMode = await eel.getCastleHeartMode()();
    var max = await eel.getServerMaxPlayers()();
    var d_ContainerLoot = await eel.getLootEnemyDContainer()();
    var globalChat = await eel.getGlobalChat()();

    var relics = await eel.getRelicSpawn()();
    var b_teleport = await eel.getBoundTeleport()();
    var e_bound = await eel.getEquipmentBound()();
    var serverPass = await eel.getPassword()();

    document.getElementById("serverPass").value = serverPass

    document.getElementById("teleportBoundItems").checked = b_teleport;
    document.getElementById("bloodBoundEquipment").checked = e_bound;

    document.getElementById("pageTitle").innerHTML = title;
    document.getElementById("serverName").value = title;
    document.getElementById("maxPlayers").value = max;

    document.getElementById('globalChat').checked = globalChat

    if (relics == "1") {
        document.getElementById("relicSpawnType").checked = true;
    }
    else{
        document.getElementById("relicSpawnType").checked = false;
    }

    if (d_ContainerLoot == "0"){
        document.getElementById("containerLoot").checked = false;
    }
    else {
        document.getElementById("containerLoot").checked = true;
    }


    if (pvp === "PVP"){
        document.getElementById("gameModeSwitch").checked = true;
    }
    else {
        document.getElementById("gameModeSwitch").checked = false;
    }

    document.getElementById("castleDamageMode").value = castleMode;
    document.getElementById("castleHeartDamageMode").value = castleHeartMode;

    const clanSlider = document.getElementById("maxClanSize");
    const bloodEssenceSlider = document.getElementById("bloodEssenceYield");
    const materialSlider = document.getElementById("materialYield");
    const dropTableSlider = document.getElementById("dropTableYield");
    const inventorySlider = document.getElementById("inventoryStack");
    const sunDamageModSlider = document.getElementById("sunDamageMod");

    var maxClan = await eel.getMaxClanSize()();
    var inventoryStack = await eel.getInventoryStacksMod()();
    var dropTable = await eel.getDropTableModG()();
    var matYield = await eel.getMaterialYieldModG()();
    var bloodEssenceYield = await eel.getBloodEssenceYieldMod()();
    var sunDamageMod = await eel.getSunDamage()();

    sunDamageModSlider.value = sunDamageMod;
    clanSlider.value = maxClan;
    bloodEssenceSlider.value = bloodEssenceYield;
    materialSlider.value = matYield;
    dropTableSlider.value = dropTable;
    inventorySlider.value = inventoryStack;

    document.getElementById("sunDamageOutput").innerHTML = sunDamageMod
    document.getElementById("clanSizeOutput").innerHTML = maxClan
    document.getElementById("bloodEssenceOutput").innerHTML = bloodEssenceYield
    document.getElementById("materialYieldOutput").innerHTML = matYield
    document.getElementById("dropTableOutput").innerHTML = dropTable
    document.getElementById("inventoryStackOutput").innerHTML = inventoryStack

    sunDamageModSlider.setAttribute("step", "0.1");
    bloodEssenceSlider.setAttribute("step", "0.1");
    materialSlider.setAttribute("step", "0.1");
    dropTableSlider.setAttribute("step", "0.1");
    inventorySlider.setAttribute("step", "0.1");

    sunDamageModSlider.addEventListener('input', updateValue)
    sunDamageModSlider.targetOutput = document.getElementById("sunDamageOutput")
    clanSlider.addEventListener('input', updateValue);
    clanSlider.targetOutput = document.getElementById("clanSizeOutput");

    bloodEssenceSlider.addEventListener('input', updateValue);
    bloodEssenceSlider.targetOutput = document.getElementById("bloodEssenceOutput");

    materialSlider.addEventListener('input', updateValue);
    materialSlider.targetOutput = document.getElementById("materialYieldOutput");

    dropTableSlider.addEventListener('input', updateValue);
    dropTableSlider.targetOutput = document.getElementById("dropTableOutput");

    inventorySlider.addEventListener('input', updateValue);
    inventorySlider.targetOutput = document.getElementById("inventoryStackOutput");

    function updateValue(e) {
    e.currentTarget.targetOutput.innerHTML = e.target.value;
    }
}

function updatePVP() {
    if (document.getElementById("gameModeSwitch").checked) {
        eel.setPVP("PVP");
    }
    else {
        eel.setPVP("PVE");
    }

    if (document.getElementById("containerLoot").checked) {
        eel.setLootEnemyDContainer(1)
    }
    else {
        eel.setLootEnemyDContainer(0)
    }

    eel.setCastleHeartMode(document.getElementById("castleHeartDamageMode").value)

}

function updateBoundItems(){
    eel.setBoundTeleport(document.getElementById('teleportBoundItems').checked);
    eel.setEquipmentBound(document.getElementById('bloodBoundEquipment').checked);
    if (document.getElementById('relicSpawnType').checked) {
        eel.setRelicSpawn("1");
    }
    else { eel.setRelicSpawn("0"); }


}

function updatePasswordVisibility(){
    var x = document.getElementById("serverPass");
    if (x.type === "password") { x.type = "text"; }
    else { x.type = "password"; }
}

function updateYields() {
    const clanSliderVal = document.getElementById("maxClanSize").value;
    const bloodEssenceSliderVal = document.getElementById("bloodEssenceYield").value;
    const materialSliderVal = document.getElementById("materialYield").value;
    const dropTableSliderVal = document.getElementById("dropTableYield").value;
    const inventorySliderVal = document.getElementById("inventoryStack").value;
    const sunDamageModVal = document.getElementById("sunDamageMod").value;

    eel.setSunDamage(sunDamageModVal);
    eel.setMaxClanSize(clanSliderVal);
    eel.setInventoryStacksMod(inventorySliderVal);
    eel.setDropTableModG(dropTableSliderVal);
    eel.setMaterialYieldModG(materialSliderVal);
    eel.setBloodEssenceYieldMod(bloodEssenceSliderVal);
}