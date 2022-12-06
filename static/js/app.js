const PubNub = require('pubnub');

const pubnub = new PubNub({
	publishKey: "pub-c-d6e8028a-60ab-4860-85d8-84e6af8d04a6",
	subscribeKey: "sub-c-99b2f757-497d-4a91-861b-95ce13125533",
	userId: "6e6e91be-676d-11ed-9022-0242ac120002",
  });
  

let aliveSecond = 0;
let heartbeatRate = 5000;

//Rewrite using the fetch api
function keepAlive()
{
	fetch('/keep_alive')
	.then(response=> {
		if(response.ok){
			let date = new Date();
			aliveSecond = date.getTime();
			return response.json();
		}
		throw new Error('Server offline');
	})
	.then(responseJson => console.log(responseJson))
	.catch(error => console.log(error));
	setTimeout('keepAlive()', heartbeatRate);
}

function time(){
	let d = new Date();
	let currentSec = d.getTime();
	if(currentSec - aliveSecond > heartbeatRate + 1000){
		document.getElementById("Connection_id").innerHTML = "DEAD";
	}
	else{
		document.getElementById("Connection_id").innerHTML = "ALIVE";
	}
	setTimeout('time()', 1000);
}


// add listener
const listener = {
    status: (statusEvent) => {
        if (statusEvent.category === "PNConnectedCategory") {
            console.log("Connected");
        }
    },
    message: (message) => {
        let msg = message.message;
		console.log(msg)
		if (msg["dht11"]){
			document.getElementById("dht11-temp").innerHTML = msg["dht11"]["temperature"] + "ºC";
			document.getElementById("dht11-hum").innerHTML = msg["dht11"]["humidity"] + "%";

		}
		showMessage(messageEvent.message.description);
    },
    presence: (presenceEvent) => {
        // handle presence
    }
};
pubnub.addListener(listener);


//Not sure if this is necessary
// function handleClick(cb){
// 	if(cb.checked){
// 		value = "ON";
// 	}else{
// 		value = "OFF";
// 	}
// 	sendEvent(cb.id+"-"+value);
// }

//sendEvent
function sendEvent(value){
	fetch("/status="+value,
		{
			method:"POST"
		})
}
