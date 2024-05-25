
def letter_breakdown(letters_compiled):
    #Function that splits dictionary into matching lists.
    #Prints lists in pairs

    letter_index = []
    letter_count = []
    for letters in letters_compiled:
        letter_index.append(letters)
        letter_count.append(letters_compiled[letters]) 
    for each in range(len(letter_index)):
        print(f"The '{letter_index[each]}' character was found {letter_count[each]} times")


    


def main():
    word_count = 0
    letter_dict = {}
    sorted_letters = {}
    #Open file at path, assign to f
    with open("books/frankenstein.txt") as f:
        #read the contents of the string into a variable
        file_contents = f.read()

    print (f"--- Begin report of books/frankenstein.txt ---")

    #turn file_contents string into a list of words
    words = file_contents.split()
    
    #for each word, add 1 to the tally
    for word in words:
        word_count += 1
    

    print(f"{word_count} words found in the document")

    #turn book into all lowercase
    lowered_string = file_contents.lower()
    #For every letter, if not in dictionary, add to dictionary as key: 1
    #Else add 1 to the key-letter
    for letter in lowered_string:
        if letter.isalpha(): #Keeps out non-letters    
            if letter not in letter_dict:
                letter_dict[letter] = 1 
        
            else:
                letter_dict[letter] += 1

    sorted_letters = dict(sorted(letter_dict.items()))        

    #Function that splits dictionary into matching lists.
    #Prints lists in pairs
    letter_breakdown(sorted_letters)

    print("--- End report ---")


if __name__ == "__main__":
    main ()

