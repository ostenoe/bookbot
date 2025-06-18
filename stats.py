def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1 
        else:
            char_counts[char] = 1 
    return char_counts 
     
def sort_characters(char_counts):
    # Convert the dictionary to a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    
    # Sort by the "num" key in descending order
    char_list.sort(key=lambda item: item["num"], reverse=True)
    
    return char_list
