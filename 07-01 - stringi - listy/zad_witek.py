text = "oto Pierwsze zdanie. a potem jest drugie? 2! 3!!! tak! ale co potem?"
print(text)

# zamiana pierwszych liter zdań
text_list = text.split()
print(text_list)

# pierwszy wyraz na dużą literę
word_1 = text_list[0]
new_word_1 = word_1[0].upper() + word_1[1:]
print(new_word_1, end=" ")

# pozostałe wyrazy
word_counter = 0
for word in text_list[1:]:
    word_counter += 1
    if word.endswith((".", "?", "!")):
        uppered_word = text_list[word_counter+1][0].upper() + text_list[word_counter+1][1:]
        print(word, uppered_word, end=" ")
    else:
        print(word, end=" ")


# # liczenie interpunkcji i liczb
# inter_counter = 0
# att_counter = 0
# num_counter = 0

# for letter in text:
#     if letter in {".", ",", "?", "!"}:
#         inter_counter += 1
#         if letter == "!":
#             att_counter += 1
#     elif letter.isnumeric():
#         num_counter += 1



# print(f'''
# W tekście wystąpiło tyle:
# - znaków interpunkcyjnych: {inter_counter}
# - liczb: {num_counter}
# - wykrzykników: {att_counter}
# ''')
