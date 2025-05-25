with open("story.txt", "r") as file:
    lines = file.read()

inside = False
words = []
temp = ''

for char in lines:
    if char == "[":
        inside = True
        temp = ''
    elif char == "]" and inside:
        inside = False
        words.append(temp)
    if inside == True:
        if char == "]" or char == "[":
            pass
        else:
            temp += char

for word in words:
    print("what do want to fill instead of :", word)
    rep = input()
    lines = lines.replace(word, rep)
