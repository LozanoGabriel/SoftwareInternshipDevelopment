from latex2sympy2_extended import gen
from mellea import start_session

m = start_session()

response1 = m.instruct("Say hello in one sentence and an emoji.")
print(response1)

response2 = m.instruct("What is the capital of France?")
print(response2)

response3 = m.instruct("Write a haiku about Python.")
print(response3)

response4 = m.instruct("Explain what a Python list is.")
print(response4)
#instruct is you telling the model what to do.

# A better implementation - what mellea can do
from mellea import generative

@generative
def write_haiku(topic: str):
    """Write a haiku about Python"""

print(write_haiku("Python"))

import streamlit as st
from mellea import start_session
from mellea.stdlib.sampling import RejectionSamplingStrategy


@st.cache_resource
def get_session():
    # Created once and reused across reruns so the model isn't reloaded each click
    return start_session()


st.set_page_config(page_title="Dr. Reis's Office Hours")
st.title("Dr. Reis's Office Hours")
st.caption("Local LLM via Ollama · granite4.1:3b · no API key")

task = st.text_area(
    "What should the model do?",
    "Write a two-sentence email inviting students to office hours.",
    height=100,
)

requirement = st.text_input(
    "Requirement (optional) — a rule the output must satisfy",
    "Mention the room number INV1 455",
)

retries = st.slider("Max retries if the requirement fails", 1, 5, 3)

if st.button("Generate", type="primary"):
    m = get_session()
    reqs = [requirement] if requirement.strip() else []

    with st.spinner("Thinking..."): #HCI Principle - let the user know something
        result = m.instruct(
            task,
            requirements=reqs,
            strategy=RejectionSamplingStrategy(loop_budget=retries),
        )

    st.subheader("Output")
    st.write(str(result))

    if reqs:
        st.success(f"Passed requirement: “{requirement}”")