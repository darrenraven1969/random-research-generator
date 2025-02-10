{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import random\
\
# Define the three lists of theories\
message_theories = [\
    "Encoding - Decoding",\
    "The Semiotic Triangle",\
    "Dual-Coding Theory",\
    "Gestalt Principles",\
    "Cognitive Load Theory",\
    "Cultural Context and Symbols",\
    "The Medium is the Message (Marshall McLuhan)",\
    "Message Framing (Prospect Theory)",\
    "Emotional Resonance",\
    "Noise in Communication (Shannon & Weaver Model)",\
    "Visual Metaphors",\
    "Postmodern Communication"\
]\
\
audience_theories = [\
    "Audience Reception Theory",\
    "User-centred Design",\
    "Social Identity Theory",\
    "Media Dependency Theory",\
    "Para-social Interaction Theory",\
    "Diffusion of Innovations",\
    "Attention Economy Theory",\
    "Cultivation Theory",\
    "Expectation-Confirmation Theory",\
    "Perceived Value Theory",\
    "Personalisation and Customisation Theory",\
    "Multimodal Communication Theory"\
]\
\
context_theories = [\
    "Spatial Context",\
    "Digital Context",\
    "Cultural Context",\
    "Historical Context",\
    "Political Context",\
    "Economic Context",\
    "Psychological Context",\
    "Environmental Context",\
    "Temporal Context",\
    "Interaction Context",\
    "Social Context",\
    "Personal Context",\
    "Environmental",\
    "Temporal"\
]\
\
# Streamlit UI setup\
st.title("\uc0\u55356 \u57266  Random Research Idea Generator")\
st.write("Click the button below to generate a random combination of theories for your research project!")\
\
# Button to generate a random combination\
if st.button("Generate Research Combination"):\
    message = random.choice(message_theories)\
    audience = random.choice(audience_theories)\
    context = random.choice(context_theories)\
    \
    # Display the random selection\
    st.success(f"**Message Theory:** \{message\}\\n\\n**Audience Theory:** \{audience\}\\n\\n**Context Theory:** \{context\}")\
}