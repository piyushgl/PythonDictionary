from difflib import get_close_matches
import json

data = json.load(open("data.json"))
print(f"Total words available in dictionary {len(data)}")

w = input("Enter word to search for its meaning:")

def search_it(word):
    if word in data:
        meanings = data[word.lower()]
        print(f"Meaning of {word} is:")
        for meaning in meanings:
            print(f">{meaning}")
        return 1    

if search_it(w) != 1:
    wd = get_close_matches(w,data.keys())
    if len(wd) > 0:
        for w in wd:
            answer = input(f"Did you mean:{w} Y/N?")
            if answer == "Y":
                search_it(w)
                break
    else:    
        print("No matching word found!")