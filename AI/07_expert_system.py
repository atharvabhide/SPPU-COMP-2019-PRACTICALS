import streamlit as st
from typing import List

knowledge_base = {
    "cold" : [
        "1: Tylenol",
        "2: Panadol",
        "3: Nasal spray",
        "4: Please wear warm clothes!"
    ],

    "influenza": [
        "1: Tamiflu"
        "2: Panadol",
        "2: Zanamivir",
        "4: Please take a warm bath and do salt gargling!"
    ],

    "typhoid": [
        "1: Chloramphenicol",
        "2: Amoxicillin",
        "3: Ciproflaxacin",
        "4: Azithromycin",
        "5: Please do complete bed rest and take soft diet!"
    ],

    "chicken pox" : [
        "1: Varicella vaccine",
        "2: Immunoglobulin",
        "3: Acetomenaphin",
        "4: Acyclovir",
        "5: Please do have have oatmeal and stay at home!"
    ],

    "measles" : [
        "1: Tylenol",
        "2: Aleve",
        "3: Advil",
        "4: Vitamin A",
        "5: Please get rest and use more liquid!"
    ],   

    "malaria" : [
        "1: Aralen",
        "2: Qualaquin",
        "3: Plaquenil",
        "4: Mefloquine",
        "5: Please do not sleep in open air and cover your full skin!"
    ]
}

st.header("Medical Diagnosis Expert System")

def respond(input: List[str]):
    symptoms = input
    if (len(symptoms) == 3):
        if (symptoms[0] == "rash" and symptoms[1] == "body ache" and symptoms[2] == "fever"):
            st.write("You have chicken pox!")
            st.write("Please take the following medicines and precautions-")
            for i in knowledge_base["chicken pox"]:
                st.write(i)
        else:
            st.write("Question is not present in the knowledge base!\nCould you please enter the appropriate answer for the question below-")
            answer = st.text_input("Answer")
            add = st.button("Add answer")
            if (add):
                for key in symptoms:
                    knowledge_base[key] = [answer]
    elif (len(symptoms) == 4):
        if (symptoms[0] == "headache" and symptoms[1] == "runny nose" and symptoms[2] == "sneezing" and symptoms[3] == "sore throat"):
            st.write("You have cold!")
            st.write("Please take the following medicines and precautions-")
            for i in knowledge_base["cold"]:
                st.write(i)
        elif (symptoms[0] == "headache" and symptoms[1] == "abdominal pain" and symptoms[2] == "poor appetite" and symptoms[3] == "fever"):
            st.write("You have typhoid!")
            st.write("Please take the following medicines and precautions-")
            for i in knowledge_base["typhoid"]:
                st.write(i)
        elif (symptoms[0] == "fever" and symptoms[1] == "runny nose" and symptoms[2] == "rash" and symptoms[3] == "conjunctivitis"):
            st.write("You have measles!")
            st.write("Please take the following medicines and precautions-")
            for i in knowledge_base["measles"]:
                st.write(i)
        else:
            st.write("Question is not present in the knowledge base!\nCould you please enter the appropriate answer for the question below-")
            answer = st.text_input("Answer")
            add = st.button("Add answer")
            if (add):
                for key in symptoms:
                    knowledge_base[key] = [answer]
    elif (len(symptoms) == 5):
        if (symptoms[0] == "sore throat" and symptoms[1] == "fever" and symptoms[2] == "headache" and symptoms[3] == "chills" and symptoms[4] == "body ache"):
            st.write("You have influenza!")
            st.write("Please take the following medicines and precautions-")
            for i in knowledge_base["influenza"]:
                st.write(i)
        else:
            st.write("Question is not present in the knowledge base!\nCould you please enter the appropriate answer for the question below-")
            answer = st.text_input("Answer")
            add = st.button("Add answer")
            if (add):
                for key in symptoms:
                    knowledge_base[key] = [answer]
    elif (len(symptoms) == 6):
        if (symptoms[0] == "fever" and symptoms[1] == "sweating" and symptoms[2] == "headache" and symptoms[3] == "nausea" and symptoms[4] == "vomiting" and symptoms[5] == "diahrrea"):
            st.write("You have malaria!")
            st.write("Please take the following medicines and precautions-")
            for i in knowledge_base["malaria"]:
                st.write(i)
        else:
            st.write("Question is not present in the knowledge base!\nCould you please enter the appropriate answer for the question below-")
            answer = st.text_input("Answer")
            add = st.button("Add answer")
            if (add):
                for key in symptoms:
                    knowledge_base[key] = [answer]

if __name__ == "__main__":
    options = st.multiselect(
    'What are your symptoms?',
    ["headache", "runny nose", "sneezing", "sore throat", "fever", "chills", "body ache", "abdominal pain", "poor appetite", "rash", "conjunctivitis", "sweating", "nausea", "vomiting", "diahrrea"],
    [])

    col1, col2 = st.columns([1,0.1])
    with col1:
        ask = st.button("Ask")
    with col2:
        quit = st.button("Quit")
    if (ask):
        respond(options)
    if (quit):
        st.write("Thank you for using the Expert system!")
