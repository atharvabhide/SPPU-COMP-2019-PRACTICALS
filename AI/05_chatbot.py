import streamlit as st

bot_name = "College Buddy"

knowledge_base = {

    "what is your name?" : [
        f"My name is {bot_name}! \n Happy to help you out with your College enquiries!"
    ],

    "hello": [
        f"Hello my name is {bot_name}! \n Happy to help you out with your College enquiries!"
    ],

    "what are the best colleges from pune?": [
        "COEP",
        "PICT",
        "VIT",
        "CUMMINS",
        "PCCOE"
    ],

    "which are the best engineering branches?" : [
        "Computer Engineering",
        "IT Engineering",
        "ENTC Engineering"
    ],

    "what are the top branch cut-offs for COEP?" : [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT branch",
        "ENTC Engineering: 99.2 percentile",
    ],   

    "what are the top branch cut-offs for PICT?" : [
        "Computer Engineering : 99.4 percentile",
        "IT Engineering : 98.6 percentile",
        "ENTC Engineering: 97.2 percentile",
    ],  

    "what are the top branch cut-offs for VIT?" : [
        "Computer Engineering : 99.8 percentile",
        "IT Engineering: 97.1 percentile",
        "ENTC Engineering: 96.2 percentile",
    ],    

    "what are the top branch cut-offs for CUMMINS?" : [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT branch",
        "ENTC Engineering: 99.2",
    ],  

    "what are the top branch cut-offs for PCCOE?" : [
        "Computer Engineering : 99.8 percentile",
        "Does not have IT branch",
        "ENTC Engineering: 99.2",
    ], 

    "When do college admissions start?": [
        "Admissions generally start around August",
    ],
   
}

st.header("College Enquiry Rule Based Chatbot")

def respond(input: str):
    if (input in knowledge_base):
        values = knowledge_base[input]
        for value in values:
            st.write(value)
    else:
        key = input
        st.write("Question is not present in the knowledge base!\nCould you please enter the appropriate answer for the question below")
        answer = st.text_input("Answer")
        add = st.button("Add answer")
        if (add):
            knowledge_base[key] = [answer]

if __name__ == "__main__":
    input = st.text_input("Enter a query here-")
    input = input.lower()
    col1, col2 = st.columns([1,0.1])
    with col1:
        ask = st.button("Ask")
    with col2:
        quit = st.button("Quit")
    if (ask):
        respond(input)
    if (quit):
        st.write("Thank you for using the Chatbot")
    
