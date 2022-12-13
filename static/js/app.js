let aliveSecond = 0;
let heartbeatRate = 5000;

let myChannel = "Channel-Pumpkin";
let pubnub;

function myFunction() {
  alert("Alert 4 JS");
}

pubnub = new PubNub({
    publishKey: "pub-c-d6e8028a-60ab-4860-85d8-84e6af8d04a6",
    subscribeKey: "sub-c-99b2f757-497d-4a91-861b-95ce13125533",
    userId: "94af794a-7593-11ed-a1eb-0242ac120002",
  })

console.log("PubNub object");

pubnub.addListener({
 
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

  pubnub.subscribe({channels: ["Channel-Pumpkin"] });


// from https://www.pubnub.com/blog/the-right-way-to-log-all-messages-to-a-private-database/

  // Request Handler
// export default request => { 
//     const xhr  = require('xhr');
//     const post = { method : "POST", body : request.message };
//     const url  = "http://127.0.0.1:5000/save";
//     // save message asynchronously
//     return xhr.fetch( url, post ).then( serverResponse => {
//         // Save Success! 
//         return request.ok();
//     }).catch( err => {
//         // Save Failed! handle err
//         return request.abort();
//     });
// }

