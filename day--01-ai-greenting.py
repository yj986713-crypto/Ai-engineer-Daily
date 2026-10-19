# Day 1 - AI Engineer Daily
# Simple AI Assistant Logic

def ai_assistant():
    print("🤖 Hello! I am your AI Assistant - Day 1")

    name = input("What is your name? : ")
    print(f"Nice to meet you, {name}!")

    skills = ["Python", "LLM", "RAG", "Generative AI"]
    print("\nMy learning roadmap:")
    
    for i, skill in enumerate(skills, 1):
        print(f"{i}. {skill}")

    goal = input("\nWhat you want to learn today? : ")
    
    if goal:
        print(f"\nGreat! Let's start {goal} today.")
        print("Day 1 - Completed ✅")
    else:
        print("No problem, we will start with Python!")

# Run the assistant
ai_assistant()
