alert("test")

eel.expose(loadtextTask);
function loadtextTask(text, table){
	document.getElementById("textTask").style.opacity = 1;
	document.getElementById("imgTask").style.opacity = 0;
	document.getElementById("taskText").innerHTML = text;
	document.getElementById("textTaskOptions").innerHTML = table;
}

eel.expose(loadimgTask);
function loadimgTask(text, table){
	document.getElementById("textTask").style.opacity = 0;
	document.getElementById("imgTask").style.opacity = 1;
	document.getElementById("taskText").innerHTML = text;
	document.getElementById("taskTable2").innerHTML = table;
}

eel.expose(unload);
function unload(){
	document.getElementById("textTask").style.opacity = 0;
	document.getElementById("imgTask").style.opacity = 0;
	document.getElementById("taskFormat3").style.opacity = 0;
}