def get_mode_instruction(mode): # prompt injection for different modes of explanation.
    if mode == "ELI5":
        return "Explain like I am 5 years old."
    elif mode == "ELI10":
        return "Explain like I am 10 years old."
    else:
        return "Give a complete and detailed explanation."

def clean_text(text): # removes extra whitespaces and other useless characters and makes the prompt cleaner.
    return " ".join(text.strip().split())

def optimize_prompt(user_input, mode): # final optimized prompt which will be sent to the model.
    mode_instruction = get_mode_instruction(mode)
    cleaned = clean_text(user_input)
    optimized_prompt = f"""{mode_instruction} Question: {cleaned}"""
    return optimized_prompt.strip()