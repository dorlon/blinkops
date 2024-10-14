def get_valid_input(question, options=None):
    if options:
        # Convert all options to lowercase for case-insensitive comparison
        lower_options = [opt.lower() for opt in options]
        while True:
            # Display the question and options to the user
            print(f"{question} (Options: {', '.join(options)}): ", end="")
            answer = input().strip().lower()  # Normalize user input to lowercase

            # Allow users to enter multiple choices for questions with multi-choice options
            if ',' in answer:
                selected_options = [opt.strip().lower() for opt in answer.split(',')]
                # Validate all selected options
                if all(opt in lower_options for opt in selected_options):
                    # Return selected options in original case
                    return [options[lower_options.index(opt)] for opt in selected_options]
                else:
                    print("Invalid options selected. Please try again.")
            elif answer in lower_options:
                # Return the option in original case
                return options[lower_options.index(answer)]
            else:
                print("Invalid option. Please try again.")
    else:
        return input(f"{question}: ").strip()  # For questions without predefined options

def fill_form(questions):
    answers = {}  # Dictionary to store the answers
    for question in questions:
        # Get the question text
        q_text = question['question']
        options = question.get('options', [])  # Get valid options if available

        # Check if the question has a condition (e.g., for drinks or dessert)
        if 'condition' in question:
            condition_question = question['condition']
            if answers.get(condition_question) != "Yes":
                # Skip this question if the condition is not met
                continue

        # Get user input while ensuring it's valid
        if options:
            answer = get_valid_input(q_text, options)
        else:
            answer = get_valid_input(q_text)

        answers[q_text] = answer  # Store the user's answer

        # Handle the case where the user wants to specify how many drinks
        if q_text == "How many drinks would you like?":
            answers["How many drinks"] = int(answer)  # Store the number of drinks as an integer

    return answers  # Return the collected answers
