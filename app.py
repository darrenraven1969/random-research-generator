import streamlit as st
import random

# Define the three lists of theories
message_theories = [
    "Encoding - Decoding",
    "The Semiotic Triangle",
    "Dual-Coding Theory",
    "Gestalt Principles",
    "Cognitive Load Theory",
    "Cultural Context and Symbols",
    "The Medium is the Message (Marshall McLuhan)",
    "Message Framing (Prospect Theory)",
    "Emotional Resonance",
    "Noise in Communication (Shannon & Weaver Model)",
    "Visual Metaphors",
    "Postmodern Communication"
]

audience_theories = [
    "Audience Reception Theory",
    "User-centred Design",
    "Social Identity Theory",
    "Media Dependency Theory",
    "Para-social Interaction Theory",
    "Diffusion of Innovations",
    "Attention Economy Theory",
    "Cultivation Theory",
    "Expectation-Confirmation Theory",
    "Perceived Value Theory",
    "Personalisation and Customisation Theory",
    "Multimodal Communication Theory"
]

context_theories = [
    "Spatial Context",
    "Digital Context",
    "Cultural Context",
    "Historical Context",
    "Political Context",
    "Economic Context",
    "Psychological Context",
    "Environmental Context",
    "Temporal Context",
    "Interaction Context",
    "Social Context",
    "Personal Context",
    "Environmental",
    "Temporal"
]

# Streamlit UI setup
st.title("🎲 Random Research Idea Generator")
st.write("Click the button below to generate a random combination of theories for your research project!")

# Button to generate a random combination
if st.button("Generate Research Combination"):
    message = random.choice(message_theories)
    audience = random.choice(audience_theories)
    context = random.choice(context_theories)
    
    # Display the random selection
    st.success(f"**Message Theory:** {message}\n\n**Audience Theory:** {audience}\n\n**Context Theory:** {context}")
