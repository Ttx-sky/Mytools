const socket = new WebSocket('https://192.168.1.5:1005');

socket.addEventListener('open', (event) => {
	console.log('连接成功');
});

socket.addEventListener('message', (event) => {
	console.log('收到消息：', event.data);
	addMessage(event.data);
});

socket.addEventListener('close', (event) => {
	console.log('连接关闭');
});

function sendMessage() {
	const messageInput = document.querySelector('#message');
	const message = messageInput.value;

	if (message) {
		socket.send(message);
		messageInput.value = '';
		messageInput.focus();
	}
}

function addMessage(message) {
	const messagesDiv = document.querySelector('#messages');
	const messageNode = document.createElement('div');
	messageNode.textContent = message;
	messagesDiv.appendChild(messageNode);
}

