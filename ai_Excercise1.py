from mellea import start_session

m = start_session()

response1 = m.instruct("write a three sentence announcement about you cancelling the class because you got into a gigantic car accident")
print(response1)

response2 = m.instruct("Explain the topic of recursion to a beginner noob")
print(response2)

response3 = m.instruct("Create Python programming exercise about lists")
print(response3)

response4 = m.instruct("Write a short description of a data science project")
print(response4)

response5 = m.instruct("Generate a 5-question quiz about machine learning")
print(response5)