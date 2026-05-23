intents_repository = {
    'hello': 'Hi there! Welcome to DecodeLabs. How can I help you today? 😊',
    'hi': 'Hello! Great to have you in the AI training block.',
    'how are you': 'As a deterministic engine, my runtime state is optimal. How can I assist?',
    'your name': 'I am the DecodeLabs Control-Layer Assistant (System 2 Engine). 🤖',
    'project 1': 'Project 1 is the fundamental phase: Mastering Control Flow and Logic.',
    'help': 'You can ask me about: "hello", "project 1", "your name", or type "exit" to quit.',
    'bye': 'Goodbye! Keep building amazing systems. 👋'
}

print("==================================================================")
print("🤖 SYSTEM 2 CHATBOT: ONLINE (Type 'exit' to terminate session)")
print("==================================================================")


while True:
    user_raw_feed = input('You: ')
    sanitized_input = user_raw_feed.lower().strip()
    if sanitized_input == 'exit':
        print("Chatbot: Terminating digital loop. Session safe closure. Goodbye!")
        break
        
    system_response = intents_repository.get(
        sanitized_input, 
        '[FALLBACK] Input intent unrecognized. Please consult the rule handbook or try again.'
    )
    
    print(f"Chatbot: {system_response}")