
og_str = ""


def dup_sub_str(og_str):
    dup_str: list = og_str.split()
    temp = dup_str.copy()
    repeted_words = []
    
    for indx, i in enumerate(dup_str):
        if indx < len(temp):
            deleted = temp.pop(indx)
        if deleted in temp:
            repeted_words.append(deleted)
    repeted_words = set(repeted_words)
    repeted_words = list(repeted_words)
    return repeted_words

        
data = dup_sub_str("Hello")
print(data)