# Day 2 - LLM Prompt Engineering Basics
# Core skill for AI Engineer Intern

def generate_prompt(role, task):
    prompt = f"You are a {role}. Your task is to {task}. Be helpful and concise."
    return prompt

# My prompts library
roles = ["AI Engineer", "Python Tutor", "Career Guide"]

print("🚀 Day 2 - LLM Prompts")

for role in roles:
    my_prompt = generate_prompt(role, "explain AI concepts simply")
    print(f"\nRole: {role}")
    print(f"Prompt: {my_prompt}")
    print("-" * 40)

# Custom prompt for today
my_role = input("\nEnter a role for AI today: ")
my_task = input("Enter a task: ")

final_prompt = generate_prompt(my_role, my_task)
print(f"\n✅ Your Final Prompt:\n{final_prompt}")
print("\nDay 2 - Completed by yash")
