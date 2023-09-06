def getInput(wordType: str) -> str:
    user_input = input(f"Enter {wordType}: ").strip()
    return user_input

adjective1 = getInput("an ajdective")
adjective2 = getInput("an adjective")
adjective3 = getInput("an adjective")
adjective4 = getInput("an adjective")
noun1 = getInput("an animal type, Eg. dragon")
noun2 = getInput("its name")
object1 = getInput("an object")
object2 = getInput("another object")
object3 = getInput("another object")
verb1 = getInput("a verb (present participle form)")
verb2 = getInput("another verb (present participle form)")

Story = f'''In a {adjective1} kingdom far, far away, there lived a peculiar {noun1} named {noun2}. One {adjective2} morning, while napping on a cloud, {noun2} discovered a mysterious treasure chest hidden beneath a rainbow.
With an excited whoosh, {noun2} opened it and was instantly transported to a whimsical realm filled with talking {object1}, flying {object2}, and dancing {object3}.
The adventure was a {adjective3} mix of laughter, challenges, and surprise encounters, but it was {noun2}'s infectious laughter that ultimately saved the day, {verb1} them back home with a heart {verb2} with the joy of their {adjective4} journey.'''

print()
print("Your Crafted Story:")
print(Story)