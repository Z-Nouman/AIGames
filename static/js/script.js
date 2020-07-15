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

function AIResponse(){

  var entry = {
    message: "This shows that my JSON objects work!"
  };

  fetch(window.origin.toString() + '/connect4/AIResponse', {
    method: "POST",
    credentials: "omit",
    body: JSON.stringify(entry),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  })
  .then(function (response){

    if (response.status !== 200){
      console.log('Response was not 200: ${response.status}');
    }

    response.json().then(function (data){
      console.log(data);
    })
  })
}

AIResponse();