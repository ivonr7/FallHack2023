// script.js
const userInput = document.getElementById('user-input');
const chatMessages = document.getElementById('chat-messages');
const chatOutPut = document.getElementById('chat-output')

function appendMessage(message, isUser) {
    const messageContainer = document.createElement('div');
    messageContainer.className = isUser ? 'user-message' : 'bot-message';
    const userName = isUser ? 'You' : 'ChatBot'; // Determine the username
    messageContainer.textContent = `${userName}: ${message}`; // Include the username with the message
    chatMessages.appendChild(messageContainer);

    // Automatic Scroll for newer messages
    chatOutPut.scrollTop = chatOutPut.scrollHeight;
}

async function callAPI(url) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const data = await response.text();
        return data
    } catch (error) {
        console.error('Error:', error);
        return 'An error occurred while fetching data';
    }
}

async function processUserInput() {
    const userMessage = userInput.value;
    userInput.value = '';

    appendMessage(userMessage, true);

    // Generate a random response from the bot
    const responseData = await callAPI("http://142.58.89.218:8000/ask/?message=hello");

    const words = responseData;

    // for(const word of words){
    //     if (responseData[word]) {
    //         appendMessage(responseData[word], false); // Display the message associated with the keyword
    //         return; // Exit the loop if a match is found
    //     }
    // }

    appendMessage(words, false);
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

// Pop-up menu buttons and functions
const menuButton = document.getElementById('menu-button');
const menuPopup = document.getElementById('menu-popup');
const resetButton = document.getElementById('reset-button');
const saveButton = document.getElementById('save-button');
const loadButton = document.getElementById('load-button');
const exitButton = document.getElementById('exit-button');

menuButton.addEventListener('click', function () {
    toggleMenu();
});

function toggleMenu() {
    if (menuPopup.style.display === 'block') {
        menuPopup.style.display = 'none';
    } else {
        menuPopup.style.display = 'block';
    }
}

// Handle menu options
resetButton.addEventListener('click', function () {
    // Implement your reset logic here
    alert('Chat Reseted.');
    resetChat();
    menuPopup.style.display = 'none';
});

saveButton.addEventListener('click', function () {
    // Implement your save logic here
    alert('Save button clicked');
});

loadButton.addEventListener('click', function () {
    // Implement your load logic here
    alert('Load button clicked');
});

exitButton.addEventListener('click', function () {
    // Implement your exit logic here
    menuPopup.style.display = 'none';
});

function resetChat(){
    chatMessages.innerHTML = '';
    userInput.value = '';
}
