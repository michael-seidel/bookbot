def get_num_words(inputfile):
    countlist = inputfile.split()
    count = len(countlist)
    print(f"Found {count} total words")

def char_count(text):
    char_totals = {}
    for char in list(text):
        char = char.lower()
        if char in char_totals:
            char_totals[char] += 1
        else:
            char_totals[char] = 1
       
    return char_totals

def sort_on(items):
    return items["num"]
    
def sortit(letter_counts):
    chars = []
    for k, v in letter_counts.items():
        #print(k, v)
        chars.append({"char" :k, "num" : v })
    #print(chars)
 
    #print()
    chars.sort(reverse=True, key=sort_on)
    #print(chars)

    for mychar in chars:
        if mychar['char'].isalpha():
            print(f"{mychar['char']}: {mychar['num']}")
