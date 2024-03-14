## 1
text = input()
text_length = len(text)

for index in range(0, len(text)):
    print(text[index])


## 2
text = input()
for index in text:
    print(index)


## 3
text = input()

for index, character in enumerate(text):
    print(f"Index is '{index}' Character is '{character}'")
    print(type(index))

    if index % 2 == 0:
        print(character)
