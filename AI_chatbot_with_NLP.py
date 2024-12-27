import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK packages if not already present
nltk.download('punkt')
nltk.download('stopwords')

# Define a knowledge base (dictionary of predefined questions and answers)
knowledge_base = {
    "what is html": "HTML stands for HyperText Markup Language. It is the standard language used to create web pages.",
    "what is python": "Python is a high-level programming language that is widely used in software development, web development, and data science.",
    "what is artificial intelligence": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn.",
    "who are you": "I am an AI-powered chatbot here to assist you with any queries you might have.",
    "how are you": "I am just a chatbot, but thank you for asking! How can I assist you today?",
    "what can you do": "I can answer questions, help with tasks, and engage in conversations. Just ask me anything!"
}

# Define a set of patterns and responses for common queries
patterns = [
    (r'hi|hello|hey', ['Hello! How can I assist you today?', 'Hey there! How can I help you?']),
    (r'how are you\?', ['I am fine, thank you for asking!', 'I am doing well, how about you?']),
    (r'what is your name\?', ['I am a chatbot, created to assist you!', 'I am your virtual assistant.']),
    (r'what can you do\?', ['I can answer your questions, help with tasks, and engage in conversations.']),
    (r'can you help me\?', ['Sure! How can I assist you today?', 'Yes, I am here to help. What do you need?']),
    (r'(.*) your name?', ['My name is ChatBot, nice to meet you!', 'I am simply called ChatBot!']),
    (r'how do you work\?', ['I use Natural Language Processing to understand your queries and respond accordingly.']),
    (r'where are you from\?', ['I exist in the virtual world, created to assist you with various tasks!']),
    (r'bye|goodbye', ['Goodbye! Have a great day!', 'Bye! Take care!']),
    (r'(.*) your purpose?', ['My purpose is to assist you with information, answer your questions, and help with tasks!']),
    (r'(.*) help(.*)', ['I am here to help you. What do you need assistance with?', 'Please tell me what you need help with.']),
    (r'what is your function\?', ['I am designed to answer questions and assist with tasks like providing information, solving problems, and chatting!']),
    (r'what is your job\?', ['I am your virtual assistant, helping you with various tasks and providing information!']),
    (r'what do you mean\?', ['I mean exactly what I say. Can you please clarify your question?']),
    (r'(.*) how are you\?', ['I am doing great, thanks for asking!', 'I am functioning well. How are you doing?']),
    (r'what do you think\?', ['I am here to assist you, not to think. But I am happy to help with anything you need.']),
]

def get_response(user_input):
    # Check if the question is in the knowledge base
    user_input = user_input.lower().strip()
    if user_input in knowledge_base:
        return knowledge_base[user_input]
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"

# Create the chatbot
class CustomChat(Chat):
    def respond(self, user_input):
        # First, check the knowledge base for predefined responses
        response = get_response(user_input)
        if response != "Sorry, I didn't understand that. Can you please rephrase?":
            return response
        # If no predefined response found, fallback to default behavior
        return super().respond(user_input)

# Create the chatbot with CustomChat
chatbot = CustomChat(patterns, reflections)

# Function to start the conversation
def start_chat():
    print("Hello! I am your chatbot. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

# Start the chat
start_chat()
