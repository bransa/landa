from translations import words, phrases

def is_composite(input_phrase):
    for phrase in phrases:
        if phrase in input_phrase:
            return True
    return False

def replace_substring(input_str, phrases):
    for phrase in phrases:
        if phrase in input_str:
            input_str = input_str.replace(phrase, phrases[phrase])
    return input_str

def translate_input(input_str):
    # First try to replace substrings
    translated_str = replace_substring(input_str.lower(), phrases)

    # If no replacements were made, check the words dictionary
    if translated_str == input_str.lower() and input_str.lower() in words:
        return words[input_str.lower()]

    return translated_str

def main():
    print("Landa - Your Bemba/English Translator")

    while True:
        user_input = input("Make an entry in English to translate. Type 'exit' to quit: ")

        if user_input.lower() == 'exit':
            break

        if is_composite(user_input.lower()):
            print(f"'{user_input}' is a composite")
        else:
            translation = translate_input(user_input)
            print(f"Translation: {translation}\n")

if __name__ == "__main__":
    main()
