def get_valid_input(valid_input_set, prompt_message):
    is_valid = False
    user_input = ""
    while not is_valid:
        print(prompt_message)
        user_input = input()
        is_valid = user_input in valid_input_set

    return user_input
