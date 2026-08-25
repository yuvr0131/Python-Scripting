#Building a Translator
#Giraffe Language
#vowels ->replace by g

#--------
#dog->dgt
#cat->cgt
#
# def translate(phrase):
#     translation=""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation+='G'
#             else:
#              translation+='g'
#         else:
#             translation+=letter
#     return translation
#
# print(translate(input("Enter your phrase:")))

# Comment
#This program is cool
# print("Comments are cool")

# Try Except - Catching error
try:
    # value=10/0
    number=int(input("Enter a number:"))
    print(number)
except ValueError:
    print("invalid input")
except ZeroDivisionError as err:
    print(err)


