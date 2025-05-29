tweet = "Learning #Python is fun! #coding #dev"
# Expected Output: ['#Python', '#coding', '#dev']
for words in tweet.split(" "):
  if "#" in words:
    print(words)

sentence = "This is a (simple) string with (some) words."
# Expected Output: ['simple', 'some']
for words in sentence.split(" "):
  if "(" in words:
    print(words)

mails = ["alice@example.com", "bob@gmail.com"]
# Expected Output: ['example.com', 'gmail.com']
for mail in mails:
    x = mail.split("@")
    print(x[1])

html = "The weather is <condition>sunny</condition> today."
# Expected Output: ['sunny']
words = []
temp = ''
state = False
for char in html:
    if char == ">":
        state = True
        temp = ""
    elif char == "<" and state:
       state = False
       words.append(temp)
    if state:
       if char == ">":
          pass
       else:
        temp += char

for word in words:
   print(word)

info = "name=John; age=25; city=Delhi"
dic = {}
for pair in info.split(";"):
   pair = pair.lstrip()
   key , value = pair.split("=")
   dic[key] = value
print(dic)
# Expected Output: {'name': 'John', 'age': '25', 'city': 'Delhi'}

# 7. Extract timestamps from subtitles

subtitle = "00:01:23,456 --> 00:01:25,789"
timestamp = []
for x in subtitle.split("-->"):
   timestamp.append(x.strip())
print(timestamp)
# Expected Output: ['00:01:23,456', '00:01:25,789']

# 8. Template engine simulation
template = "Hello {{username}}, your balance is {{balance}}."
values = {"username": "Alice", "balance": "$100"}
words = []
temp = ""
for word in word.split(" "):
      if "{" in word:
         for char in word:
            if char.isalpha():
               temp += char
      words.append(temp)
for key , value in values.items():
   for word in words:
      if key == word:
         print("hello {value}")

# Expected Output: 'Hello Alice, your balance is $100.'

# 9. Decode a compressed pattern
pattern = "3[a]2[bc]"
inside = False
ans = []
temp = ""
final_ans = ""
for char in pattern:
      if char.isdigit():
         num = int(char)
      if char == "[":
         inside = True
         temp = ""
      if char == "]" and inside:
         inside = False
         temp = temp*num
         ans.append(temp)
      if inside:
         if char == "[":
            pass
         else:
            temp += char
for string in ans:
   final_ans += string
print(final_ans)
# Expected Output: 'aaabcbc'

# 10. Extract all quoted strings
quote_text = 'She said "Hello", and then he replied "Hi there"'
inside = False
temp = ""
words = []
for index,char in enumerate(quote_text):
   print(char)
   if char == '"':
      inside = True
      temp = ""
   if char == '"' and inside and quote_text[index-1].isalpha():
      inside = False
      words.append(temp)
   if inside:
      temp += char
print(words)
# Expected Output: ['Hello', 'Hi there']
