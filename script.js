// script.js
const userInput = document.getElementById('user-input');
const chatMessages = document.getElementById('chat-messages');

function appendMessage(message, isUser) {
    const messageContainer = document.createElement('div');
    messageContainer.className = isUser ? 'user-message' : 'bot-message';
    const userName = isUser ? 'You' : 'ChatBot'; // Determine the username
    messageContainer.textContent = `${userName}: ${message}`; // Include the username with the message
    chatMessages.appendChild(messageContainer);
}

function processUserInput() {
    const userMessage = userInput.value;
    appendMessage(userMessage, true);

    // Generate a random response from the bot
    const randomResponses = [
        "Hello there!",
        "How can I assist you?",
        "Nice to meet you!",
        "What's on your mind?",
        "I'm here to help.",
    ];

    const randomResponse = randomResponses[Math.floor(Math.random() * randomResponses.length)];
    appendMessage(randomResponse, false);

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
