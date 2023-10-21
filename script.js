// script.js
const userInput = document.getElementById('user-input');
const chatMessages = document.getElementById('chat-messages');

function appendMessage(message, isUser) {
    const messageContainer = document.createElement('div');
    messageContainer.className = isUser ? 'user-message' : 'bot-message';
    messageContainer.textContent = message;
    chatMessages.appendChild(messageContainer);
}

function processUserInput() {
    const userMessage = userInput.value;
    appendMessage(userMessage, true);

    // Your chat bot logic here

    userInput.value = '';
}

const clearChatButton = document.getElementById('clear-chat-button');

clearChatButton.addEventListener('click', function () {
    clearChat();
});

function clearChat() {
    chatMessages.innerHTML = ''; // This clears all the content inside the chat-messages container.
}


userInput.addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
        processUserInput();
    }
});
