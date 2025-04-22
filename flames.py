def format_name(name):

    letters = list(name.upper())
    if len(letters) >= 2:
        letters[1] = str(len(letters))  
    return letters

def get_flames_result(name1, name2):
    name1 = list(name1)
    name2 = list(name2)
    for ch in name1[:]:
        if ch in name2:
            name1.remove(ch)
            name2.remove(ch)
    count = len(name1 + name2)


    flames = ["F", "L", "A", "M", "E", "S"]
    while len(flames) > 1:
        i = (count % len(flames)) - 1
        if i >= 0:
            right = flames[i + 1:]
            left = flames[:i]
            flames = right + left
        else:
            flames = flames[:len(flames)-1]
    
    relation = {
        "F": "FRIENDSHIP",
        "L": "LOVE",
        "A": "AFFECTION",
        "M": "MARRIAGE",
        "E": "ENEMY",
        "S": "SIBLINGS"
    }
    return relation[flames[0]]


boy = input("Enter boy name without spaces: ")
girl = input("Enter girl name without spaces: ")


boy_formatted = format_name(boy)
girl_formatted = format_name(girl)

print("Boy formatted:", boy_formatted)
print("Girl formatted:", girl_formatted)


result = get_flames_result(boy.upper(), girl.upper())
print(result)
