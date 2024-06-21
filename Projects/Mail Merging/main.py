# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open(
    "Projects/Mail Merging/Input/Names/invited_names.txt", encoding="utf-8",
        mode="r") as name:

    contents = name.readlines()

    for name in contents:
        name_needed = str(name)

        with open(
            "Projects/Mail Merging/Input/Letters/starting_letter.txt",
            encoding="utf-8",
            mode="r",
        ) as letter_template, open(
            f"Projects/Mail Merging/ReadyToSend/{name_needed}.txt",
            encoding="utf-8",
            mode="w",
        ) as ready_to_send:
            for line in letter_template:
                ready_to_send.write(
                    line.replace("[name]", name_needed.strip())
                    )
