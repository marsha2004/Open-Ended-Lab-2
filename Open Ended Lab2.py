def pattern(words, a):
    x1 = a.split()
    
    # Lengths should be the same
    if len(words) != len(x1):
        return False
    
    char_to_word = {}
    word_to_char = {}

    for char, word in zip(words, x1):
        # Check if the character is already mapped to a word
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word

        # Check if the word is already mapped to a character
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char

    return True


pattern1, a1 = "qwwq", "peach mango mango peach"
pattern2, a2 = "qwwq", "peach mango mango cherry"
pattern3, a3 = "qqqq", "peach cherry mango peach"
pattern4, a4 = "qwqw", "peach cherry mango cherry"

# Printing outputs
print(pattern(pattern1, a1))  
print(pattern(pattern2, a2))  
print(pattern(pattern3, a3)) 
print(pattern(pattern4, a4)) 
