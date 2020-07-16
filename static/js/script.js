var array = [0, 0, 0, 0, 0, 0, 0];
var board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
var redTurn = true;

function chbg(id) {
    var columnNum = id.charCodeAt(0) - 48;
    var name = array[columnNum] + (columnNum * 6);
    if (redTurn){
      color = 'lightpink';
      document.getElementById(name.toString()).style.backgroundColor = color;
    }
}

function out(id){
  var columnNum = id.charCodeAt(0) - 48;
  console.log(id.charCodeAt(0));
  var name = array[columnNum] + (columnNum * 6);
  document.getElementById(name.toString()).style.backgroundColor = 'white';
}

function placeToken(id){
  if (redTurn){
    var columnNum = id.charCodeAt(0) - 48;
    var name = array[columnNum] + (columnNum * 6);
    array[columnNum] += 1;
    color = 'red';
    redTurn = false;
    board[name] = -1;
    document.getElementById(name.toString()).style.backgroundColor = color;
    AIResponse();
    }
}
function botPlaceToken(id){
  console.log("This bot wants to place a token at index:");
  console.log(id);
  columnNum = Math.floor((id / 6));
  array[columnNum] += 1;
  color = 'yellow';
  redTurn = true;
  board[id] = 1;
  document.getElementById(id.toString()).style.backgroundColor = color;
}

function AIResponse(){
  var entry = {
    message: board
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
      if (data.endGame){
        if (data.player == -1){
          console.log("Hey, you won! This bot is garbage!!")
        }
        else if (data.player == -2){
          console.log("Looks like there was a tie")
        }
        else{
          botPlaceToken(data.player);
          console.log("The bot won!!!")
        }
      }
      else{
        console.log(data.player)
        botPlaceToken(data.player);
      }
    })
  })
}

//Problems for Zaid tomorrow:
//Fix win issue where 1 + blank + 3 should not be a win
//Fix AI placing down it's winning move and end the game immediately
//Add a reset button
//Fix hover implementation so that it doesn't overfill to the next column