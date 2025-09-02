import time
import random

#responses that chatbot gives to user
greetings=['Hi ','Hello ','Hi there ','Nice to see you ','Hey ','Welcome ']
jokes=["Why don't scientists trust atoms?\nBecause they make up everything!",
       "Why did the computer go to the doctors?\nBecause it caught a virus!",
       "Why was the math book sad?\nBecause it had too many problems!"]
quotes=["Belive in yourself,and you're halfway there!",
        "The best way to get started is to quit talking and begin doing.",
        "Don't watch the clock; do what it does.keep going!"]


 #take responses from chatbot       
def chatbot_response(user_input,name):
    user_input=user_input.lower()
    if user_input in ["hello","hi","hey","hello buddy","bot"]:
        return random.choice(greetings)+f"{name}!"
    elif  "jokes" in user_input :
        return random.choice(jokes)
    elif "quotes" in user_input or "motivate" in user_input:
        return random.choice(quotes)
    elif user_input in ["how are you","how are you?"]:
        return "I'm doing great, thanks for asking! How about you?"
    elif user_input in ["fine","i'm fine","i am fine","good","i am also fine"]:
        return "great"
    
    elif user_input in ["bye","goodbye"]:
        return f"Goodbye,{name}! Have a wonderful day!"
    elif user_input in ["time","what's time now","tell me present time"]:
        return time.ctime()
    else:
        return "Hmm... I don't understand what you want to say"
#make for runnig chatbot function  or initialization
def run_chatbot():
    print("Chatbot: Hi! I'm your friendly chatbot")
    name=input("Chatbot: What's your name?\nyou:")
    print(f"Chatbot: Nice to meet you,{name}!\nLet's chat (Type 'bye'  or 'goodbye' to exit")
    while True:
        user_input=input(f"{name}: ")
        print("Chatbot is typing....\n",end="\r")
        time.sleep(1.5)
        response=chatbot_response(user_input,name)
        print("Chatbot:",response)
        if user_input.lower() in ["bye","goodbye"]:
            break

#run the chatbot by calling function
run_chatbot()

        
    
