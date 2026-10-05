# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# Group 2: Fast Lookup / Uniqueness
# 5. Unique Word Count
# Count how many distinct words are in the collection.
# Input: "one fish two fish red fish blue fish"
# Output: 5

def count_unique_words(text):
    if not isinstance(text, str):
        print("Incorrect data type: Please enter a string")
        return
    words = text.split()
    return len(set(words))

print(count_unique_words("one fish two fish red fish blue fish"))
print(count_unique_words(""))
print(count_unique_words("fish fish fish"))
print(count_unique_words(123))
print(count_unique_words("one two three four"))

### Timed Challenge Reflection ###
#The structure that I chose for this task was a set because it only stores unique values, making it useful for counting distinct words. 
#By converting strings to a list of words and then to a set, I could automatically remove duplicates and use len() to get the number of 
#unique words.  I don’t think that the time constraint significantly affected my solution, as I was able to implement a solution, test 
#different inputs and edge cases, and include error handling for incorrect data types within the allotted time. It helped that this task 
#was similar to one of the practice problems, so from there I just had to discern how the end goal differed, what type of input was 
#expected, which in this case was a string, and potential errors. I will say that I think that the time limit encouraged me to focus on 
#a simple solution that was quick to implement, rather than trying more complicated approaches. Choosing to use a set does come with 
#trade-offs, such as not maintaining the original order of the words, but given that the instructions only required the count of distinct
#words, maintaining their order was unnecessary, making a set the suitable choice.