function update(){
    var serverName = document.getElementById('serverName').value;
    var maxPlayers = document.getElementById('maxPlayers').value;
    eel.updateHostSettings(serverName, maxPlayers);
    eel.setGlobalChat(document.getElementById('globalChat').checked);
    if (document.getElementById("serverPass").value != ""){
        eel.setPassword(document.getElementById("serverPass").value)
    }

}

function changeServer() {
    eel.changeSelectedFolder();
    location.reload();
}

async function setup() {
    document.getElementById("showPass").checked = false;

    var title = await eel.getTitle()();
    var pvp = await eel.getPVP()();
    var castleMode = await eel.getCastleMode()();
    var castleHeartMode = await eel.getCastleHeartMode()();
    var max = await eel.getServerMaxPlayers()();
    var d_ContainerLoot = await eel.getLootEnemyContainer()();
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

}

function updatePVP() {
    if (document.getElementById("gameModeSwitch").checked) {
        eel.setPVP("PVP");
    }
    else {
        eel.setPVP("PVE");
    }

    if (document.getElementById("containerLoot").checked) {
        eel.setLootEnemyContainer(1)
    }
    else {
        eel.setLootEnemyContainer(0)
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