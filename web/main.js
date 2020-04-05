alert("test")

eel.expose(loadTextTaskOptions);
function loadTextTaskOptions(text, table){
	document.getElementById("textTask").style.opacity = 1;
	document.getElementById("textTask").style.zIndex= 1;
	document.getElementById("imgTask").style.opacity = 0;
	document.getElementById("imgTask").style.zIndex= -1;
	
	document.getElementById("textTaskOptions").style.display = "table";
	document.getElementById("textTaskNumber").style.display = "none";
	document.getElementById("textTaskText").style.display = "none";
	
	document.getElementById("taskTextText").innerHTML = text;
	document.getElementById("textTaskOptions").innerHTML = table;
}

eel.expose(loadTextTaskNumber);
function loadTextTaskNumber(text){
	
	document.getElementById("textTaskOptions").style.display = "none";
	document.getElementById("textTaskNumber").style.display = "inline";
	document.getElementById("textTaskText").style.display = "none";
	
	document.getElementById("textTask").style.opacity = 1;
	document.getElementById("textTask").style.zIndex= 1;
	document.getElementById("imgTask").style.opacity = 0;
	document.getElementById("imgTask").style.zIndex= -1;
	
	document.getElementById("taskTextText").innerHTML = text;
}

eel.expose(loadTexttextTaskText);
function loadTexttextTaskText(text){
	
	document.getElementById("textTaskOptions").style.display = "none";
	document.getElementById("textTaskNumber").style.display = "none";
	document.getElementById("textTaskText").style.display = "inline";
	
	document.getElementById("textTask").style.opacity = 1;
	document.getElementById("textTask").style.zIndex= 1;
	document.getElementById("imgTask").style.opacity = 0;
	document.getElementById("imgTask").style.zIndex= -1;
	
	document.getElementById("taskTextText").innerHTML = text;
}



eel.expose(loadImgTaskOptions);
function loadImgTaskOptions(text, table, url){
	document.getElementById("textTask").style.opacity = 0;
	document.getElementById("textTask").style.zIndex= -1;
	document.getElementById("imgTask").style.opacity = 1;
	document.getElementById("imgTask").style.zIndex= 1;
	
	document.getElementById("imgTaskOptions").style.display = "table";
	document.getElementById("imgTaskNumber").style.display = "none";
	document.getElementById("imgTaskText").style.display = "none";
	
	document.getElementById("taskTextImg").innerHTML = text;
	document.getElementById("imgTaskOptions").innerHTML = table;
	
	document.getElementById("imgTaskImg").src = url;
}

eel.expose(loadImgTaskNumber);
function loadImgTaskNumber(text, url){
	document.getElementById("textTask").style.opacity = 0;
	document.getElementById("textTask").style.zIndex= -1;
	document.getElementById("imgTask").style.opacity = 1;
	document.getElementById("imgTask").style.zIndex= 1;
	
	document.getElementById("imgTaskOptions").style.display = "none";
	document.getElementById("imgTaskNumber").style.display = "inline";
	document.getElementById("imgTaskText").style.display = "none";
	
	document.getElementById("taskTextImg").innerHTML = text;
	
	document.getElementById("imgTaskImg").src = url;
}

eel.expose(loadImgTaskNumber);
function loadImgTaskNumber(text, url){
	document.getElementById("textTask").style.opacity = 0;
	document.getElementById("textTask").style.zIndex= -1;
	document.getElementById("imgTask").style.opacity = 1;
	document.getElementById("imgTask").style.zIndex= 1;
	
	document.getElementById("imgTaskOptions").style.display = "none";
	document.getElementById("imgTaskNumber").style.display = "none";
	document.getElementById("imgTaskText").style.display = "inline";
	
	document.getElementById("taskTextImg").innerHTML = text;
	
	document.getElementById("imgTaskImg").src = url;
}



eel.expose(unload);
function unload(){
	document.getElementById("textTask").style.opacity = 0;
	document.getElementById("imgTask").style.opacity = 0;
	document.getElementById("taskFormat3").style.opacity = 0;
}


function debugShowTaskFormat1(){
	document.getElementById("textTask").style.opacity = 1;
	document.getElementById("imgTask").style.opacity = 0;
}

function debugShowImgFormatOptions(){
	document.getElementById("textTask").style.opacity = 0;
	document.getElementById("textTask").style.zIndex = -1;
	document.getElementById("imgTask").style.opacity = 1;
	document.getElementById("imgTask").style.zIndex= 1;
}

function debugHideTaskFormat1(){
	document.getElementById("textTask").style.opacity = 0;
	document.getElementById("imgTask").style.opacity = 0;
	document.getElementById("textTask").style.zIndex= -1;
	document.getElementById("imgTask").style.zIndex= -1;
}


function checkEnterClick(e, id){
	if(e.keyCode == 13){
	   value = document.getElementById(id).value
	   eel.answer(value, 2);
   }
}