def format_response(response): # formats the raw markdown response from model into clean readable format.
    lines = response.split("\n")
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line:
            cleaned_lines.append(line)
    return "\n".join(cleaned_lines)