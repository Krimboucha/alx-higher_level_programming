#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_str = ""
    newline_chars = ['.', '?', ':']
    for char in text:
        new_str += char
        if char in newline_chars:
            new_str += "\n\n"
    lines = [line.strip() for line in new_str.splitlines()]
    formatted_text = "\n".join(lines)
    print(formatted_text)
