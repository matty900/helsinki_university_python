from string import punctuation

def change_case(orig_string: str) -> str:
              words = []
              for letter in orig_string:
                            if letter.isupper():
                                    letter = letter.lower()
                            elif letter.islower():
                                    letter = letter.upper()
                            words.append(letter)
              
              return " ".join(words)
        
def split_in_half(orig_string: str) -> tuple:
        length = len(orig_string)
        mid = 0
        mid = length / 2
        left_half = " "
        if length %2 != 0:
              mid = int(length / 2)
              left_half = orig_string[0:mid]
              right_half = orig_string[mid:]
        else:
                mid = int(length / 2)
                left_half = orig_string[0:mid]
                right_half = orig_string[mid:]
        words = (left_half,right_half)
        return words

def remove_special_characters(orig_string: str):  # using list and generators
    return "".join(char for char in orig_string if char not in punctuation)

def remove_special_characters(orig_string: str):  # using list
    filtered_chars = [char for char in orig_string if char not in punctuation]  # List comprehension
    return "".join(filtered_chars)
