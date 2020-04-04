alert("test")

eel.expose(loadTaskFormat1);
function loadTaskFormat1(text, table){
	document.getElementById("taskFormat1").style.opacity = 1;
	document.getElementById("taskFormat2").style.opacity = 0;
	document.getElementById("taskFormat3").style.opacity = 0;
	document.getElementById("taskText").innerHTML = text;
	document.getElementById("taskTable1").innerHTML = table;
}

eel.expose(loadTaskFormat2);
function loadTaskFormat2(text, table){
	document.getElementById("taskFormat1").style.opacity = 0;
	document.getElementById("taskFormat2").style.opacity = 1;
	document.getElementById("taskFormat3").style.opacity = 0;
	document.getElementById("taskText").innerHTML = text;
	document.getElementById("taskTable2").innerHTML = table;
}

eel.expose(loadTaskFormat3);
function loadTaskFormat3(text, table){
	document.getElementById("taskFormat1").style.opacity = 0;
	document.getElementById("taskFormat2").style.opacity = 0;
	document.getElementById("taskFormat3").style.opacity = 1;
	document.getElementById("taskText").innerHTML = text;
	document.getElementById("taskTable3").innerHTML = table;
}

eel.expose(unload);
function unload(){
	document.getElementById("taskFormat1").style.opacity = 0;
	document.getElementById("taskFormat2").style.opacity = 0;
	document.getElementById("taskFormat3").style.opacity = 0;
}