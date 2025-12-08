from agents import create_agent

agent = create_agent()

print("Milestone 2 Agent is ready.")
print("Type 'exit' to quit.\n")

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    try:
        response = agent.run(query)
        print("Agent:", response)

    except Exception as e:
        print("Error:", str(e))
