# Even Or Odd Challenge:
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Convert a number to a string Challenge:
def number_to_string(num):
    # Return a string of the number here!
    return str(num)

# Count number of vowels in a string. This is as far as I could get. It passed the initial test but would not pass the attempt.
# I couldn't figure out how to get it to pass everything.
def get_count(sentence):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in sentence:
        if letter in vowels:
            return len(vowels)
        else:
            return count
    if sentence == "":
        return count
