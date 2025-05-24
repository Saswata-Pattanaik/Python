#making own capitalize , title and upper and lower functions 

def uppercase(s):
    result = "" 
    for chara in s:
        if "a" <= chara <= "z":
            chara = chr(ord(chara) - 32)
            result += chara
        else:
            result += chara
    
    return result

def lowercase(s):
    result = "" 
    for chara in s:
        if "A" <= chara <= "Z":
            chara = chr(ord(chara) + 32)
            result += chara
        else:
            result += chara
    
    return result

def capitalize(s):
    s = s.strip()
    res = ""
    first = s[0]
    if "a" <= first <= "z":
        res += uppercase(first)
    else:
        res += first
    for char in s[1:]:
        if "A" <= char <= "Z":
            res += lowercase(char)
        else:
            res += char
    
    return res
                
def title(s):
    s = s.split()
    res = ""
    for i in s:
        first = i[0]
        if "a" <= first <= "z":
            res += uppercase(first)
        else:
            res += first
        for char in i[1:]:
            if "A" <= char <= "Z":
                res += lowercase(char)
            else:
                res += char
        res += " "
    
    print(res)

title("hello world")