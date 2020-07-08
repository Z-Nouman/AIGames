var array = [0, 0, 0, 0, 0, 0, 0];
var redTurn = true;
function chbg(color, id) {
		var name = id.toString() + array[id].toString();
    if (redTurn){
    	color = 'lightpink';
    }
    else{
    	color = 'LemonChiffon';
    }
    document.getElementById(name.toString()).style.backgroundColor = color;
}
function out(id){
	var name = id.toString() + array[id].toString();
  document.getElementById(name.toString()).style.backgroundColor = 'white';
}

function placeToken(color, id){
		var name = id.toString() + array[id].toString();
    array[id] += 1;
    if (redTurn){
    	color = 'red';
      redTurn = false;
    }
    else{
    	color = 'yellow';
      redTurn = true;
    }
    document.getElementById(name.toString()).style.backgroundColor = color;
}