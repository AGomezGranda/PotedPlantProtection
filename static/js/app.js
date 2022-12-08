// import PubNub from 'pubnub';
let aliveSecond = 0;
let heartbeatRate = 5000;

let myChannel = "Channel-Pumpkin";
let pubnub;

pubnub = new PubNub({
    publishKey: "pub-c-d6e8028a-60ab-4860-85d8-84e6af8d04a6",
    subscribeKey: "sub-c-99b2f757-497d-4a91-861b-95ce13125533",
    userId: "94af794a-7593-11ed-a1eb-0242ac120002",
  })

console.log("PubNub object");


pubnub.addListener({
 

  // status: function(statusEvent){
  //     console.log("PubNub setting listener");
  //     if(status.category == "PNConnectedCategory")
  //     {
  //         console.log("Successfully connected to PubNub");
  //         publishMessage(myChannel, "Hello everyone. Online");
  //     }
  // },
  status: (statusEvent) => {
      if (statusEvent.category === "PNConnectedCategory") {
        console.log("Connected to Pubnub");
      }
    },
  message : function(msg)
  {
      msg = msg.message;
      console.log(msg);
      if (msg["dht11"]) {
        document.getElementById("dht11-temp").innerHTML =
          msg["dht11"]["Temperature"] + "ºC";
        document.getElementById("dht11-hum").innerHTML =
          msg["dht11"]["Humidity"] + "%";
        document.getElementById("dht11-date").innerHTML =
          msg["dht11"]["Date"] + "";
  }
  
  },
  presence: function(presenceEvent)
  {
  }
})

  // pubnub.addListener(listener);

  pubnub.subscribe({channels: ["Channel-Pumpkin"] });

  // window.onload = setupPubNub;

// const setupPubNub = () => {
//   pubnub = new PubNub({
//     publishKey: "pub-c-d6e8028a-60ab-4860-85d8-84e6af8d04a6",
//     subscribeKey: "sub-c-99b2f757-497d-4a91-861b-95ce13125533",
//     userId: "94af794a-7593-11ed-a1eb-0242ac120002",
//   });

//   const listener = {

//     status: (statusEvent) => {
//       if (statusEvent.category === "PNConnectedCategory") {
//         console.log("Connected to Pubnub");
//       }
//     },
//     message: (message) => {
//       let msg = message.message;
//       console.log(msg);
//       if (msg["dht11"]) {
//         document.getElementById("dht11-temp").innerHTML =
//           msg["dht11"]["Temperature"] + "ºC";
//         document.getElementById("dht11-hum").innerHTML =
//           msg["dht11"]["Humidity"] + "%";
//         document.getElementById("dht11-date").innerHTML =
//           msg["dht11"]["Date"] + "";
//       }
//       showMessage(messageEvent.message.description);
//     },
//     presence: (presenceEvent) => {
//       // handle presence
//     },
//   };
//   pubnub.addListener(listener);

//   pubnub.subscribe({channels: ["Channel-Pumpkin"] });
// };

// window.onload = setupPubNub;

function myFunction() {
  alert("Alert 4 JS");
}

/**
function sendEvent(value) {
    fetch("/status=" + value, {
      method: "POST",
    });
  }


let aliveSecond = 0;
let heartbeatRate = 5000;

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
*/
