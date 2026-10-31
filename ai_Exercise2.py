from mellea import start_session
import streamlit as st
m = start_session()

requirement = st.text_input("The output must contain the word Python")
response1 = m.instruct("write a three sentence announcement about you cancelling the class because you got into a gigantic car accident")
if requirement:

response1 = m.instruct("write a three sentence announcement about you cancelling the class because you got into a gigantic car accident")
print(response1)

response2 = m.instruct("Explain the topic of recursion to a beginner noob",requirements = ["The output must contain exactly three sentences"])
print(response2)

response3 = m.instruct("Create Python programming exercise about lists",requirements = ["The output must contain the name Dr. Reis"])
print(response3)

response4 = m.instruct("Write a short description of a data science project", requirements = ["The output must contain the word Python"])
print(response4)

response5 = m.instruct("Generate a 5-question quiz about machine learning",requirements = ["The output must be fewer than 50 words"])
print(response5)