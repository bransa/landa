from translations import words, phrases

def partial_translator(input_phrase,test_phrase,dict_phrases):
    if test_phrase in input_phrase and test_phrase in dict_phrases:
        return input_phrase.replace(test_phrase,dict_phrases[test_phrase])
    else:
        return input_phrase

# we should try to write another function 
# that tests if an input phrase is a composite 
# of multiple dictionary entries
    
def translate_input(input):
    for phrase in phrases:
        new_phrase = partial_translator(input,phrase,phrases)
        if new_phrase is not input:
            return new_phrase
              
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