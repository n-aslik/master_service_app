const roomdata = document.getElementById("room-data");
const roomid = roomdata.getAttribute("data-room-id");
const firstname = roomdata.getAttribute("data-first-name");
const userid = roomdata.getAttribute("data-user-id");

const ws = new WebSocket("ws://localhost:8000/ws/chat/${roomid}/${userid}?firstname=${first_name}");

ws.onmessage = (event = MessageEvent)=>{
    const messages=document.getElementById("messages");
    const messageData=JSON.parse(event.data);
    const message=document.createElement("div");

    if (messageData.is_self){
        message.className = "p-2 my-1 bg-blue-500 text-white rounded-md self-end max-w-xs ml-auto";
    } else{
        message.className = "p-2 my-1 bg-blue-200 text-black rounded-md self-start max-w-xs";
    }

    message.textContent = messageData.text;
    messages.appendChild(message);
    message.scrollTop = messages.scrollHeight;
};

function sendmessage() {
    const input = document.getElementById("messageinput");
    if (input.value.trim()){
        ws.send(input.value);
        input.value = '';
    }
}

document.getElementById("messageinput").addEventListener("keypress", (e = KeyboardEvent)=>{
    if (e.key === "Enter"){
        sendmessage();
    }
});

ws.onopen = () =>{
    console.log("Соединение установлено");
};

ws.onclose = () =>{
    console.log("Соединение прервано")
};





