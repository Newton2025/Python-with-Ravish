def chatbot():
    print("Hello! I'm Your Chatbot")
    d={'hi':'hello how Should i help you','what is your Name':"I'm a Chatbot Created By R.K.T "}
    while True:
        user_input=input("You : ")
        if user_input.lower()=='exit':
            print("Goodbye! See You Later")
            break
        else:
            for i in d:
                if i.lower()==user_input:
                    response=d[i]
                    print("Bot : ",response)
                elif i.lower()!=user_input:
                    print("I'm Learning")   
chatbot()