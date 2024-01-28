from translations import words, phrases

# we should try to write a function 
# that tests if an input phrase is a composite
# of multiple dictionary entries
    
def translate_input(input):

    # first try to replace substring
    for phrase in phrases:
        if phrase in input:
            return input.replace(phrase,phrases[phrase])
        
    if input in phrases:
        return phrases[input]
    elif input in words:
        return words[input]
    else:
        return input # this is how many translators work online

def main():
    print("Landa - Your Bemba/English Translator")

    while True:
        user_input = input("Make an entry in English to translate. type 'exit' to quit: ")
  
        if user_input.lower() == 'exit':
            break

        translation = translate_input(user_input.lower())
        print(f"Translation: {translation}\n")

if __name__ == "__main__":
    main()