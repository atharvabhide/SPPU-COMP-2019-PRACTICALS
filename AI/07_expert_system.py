import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import streamlit as st
from typing import List
from shared.streamlit_utils import create_ask_quit_buttons, handle_unknown_query

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

def _diagnose_and_respond(disease_name, symptoms):
    """Display diagnosis and treatment from the knowledge base."""
    st.write(f"You have {disease_name}!")
    st.write("Please take the following medicines and precautions-")
    for i in knowledge_base[disease_name]:
        st.write(i)

def _handle_unknown_symptoms(symptoms):
    """Fallback when symptoms don't match any known disease."""
    handle_unknown_query(knowledge_base, str(symptoms))

def respond(input: List[str]):
    symptoms = input
    if (len(symptoms) == 3):
        if (symptoms[0] == "rash" and symptoms[1] == "body ache" and symptoms[2] == "fever"):
            _diagnose_and_respond("chicken pox", symptoms)
        else:
            _handle_unknown_symptoms(symptoms)
    elif (len(symptoms) == 4):
        if (symptoms[0] == "headache" and symptoms[1] == "runny nose" and symptoms[2] == "sneezing" and symptoms[3] == "sore throat"):
            _diagnose_and_respond("cold", symptoms)
        elif (symptoms[0] == "headache" and symptoms[1] == "abdominal pain" and symptoms[2] == "poor appetite" and symptoms[3] == "fever"):
            _diagnose_and_respond("typhoid", symptoms)
        elif (symptoms[0] == "fever" and symptoms[1] == "runny nose" and symptoms[2] == "rash" and symptoms[3] == "conjunctivitis"):
            _diagnose_and_respond("measles", symptoms)
        else:
            _handle_unknown_symptoms(symptoms)
    elif (len(symptoms) == 5):
        if (symptoms[0] == "sore throat" and symptoms[1] == "fever" and symptoms[2] == "headache" and symptoms[3] == "chills" and symptoms[4] == "body ache"):
            _diagnose_and_respond("influenza", symptoms)
        else:
            _handle_unknown_symptoms(symptoms)
    elif (len(symptoms) == 6):
        if (symptoms[0] == "fever" and symptoms[1] == "sweating" and symptoms[2] == "headache" and symptoms[3] == "nausea" and symptoms[4] == "vomiting" and symptoms[5] == "diahrrea"):
            _diagnose_and_respond("malaria", symptoms)
        else:
            _handle_unknown_symptoms(symptoms)

if __name__ == "__main__":
    options = st.multiselect(
    'What are your symptoms?',
    ["headache", "runny nose", "sneezing", "sore throat", "fever", "chills", "body ache", "abdominal pain", "poor appetite", "rash", "conjunctivitis", "sweating", "nausea", "vomiting", "diahrrea"],
    [])

    ask, quit = create_ask_quit_buttons()
    if (ask):
        respond(options)
    if (quit):
        st.write("Thank you for using the Expert system!")
