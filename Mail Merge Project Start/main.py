with open("./Input/Letters/starting_letter.txt") as letters:
    starting_letter = letters.read()

template_letter = starting_letter

with open("./Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()

for name in invited_names:
    with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode='w') as out_file:
        out_file.write(template_letter.replace("[name]", name.strip()))
    template_letter = starting_letter
