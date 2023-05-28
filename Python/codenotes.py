import random


# class MailServer:
#     def connect(self):
#         print('connected')
#
#     def authenticate(self):
#         print('authenticate')
#
#     def send_mail(self):
#         print('send mail')
#
#     def disconnect(self):
#         print('disconnect')
#
#
# m = MailServer
# m.connect()
# m.authenticate()
# m.send_mail()
# m.disconnect()

#
# class MailServer:
#     def send_mail(self):
#         self.__connect()  #uzytkownika w tym momencie interesuje tylko send mail reszta robi sie automatycznie po send mail
#         self.__authenticate()  #dodatkowo zamknelismy __ wszystkie funkcje by klient nie grzebal
#         print('send mail')
#         self.__disconnect()
#
#     def __connect(self):
#         print('connected')
#
#     def __authenticate(self):
#         print('authenticate')
#
#     def __disconnect(self):
#         print('disconnect')
#
# m = MailServer
# m.send_mail()


# Return the words in reverse, without multiple spaces
# def reverse_words(text):
#     result = ""
#     split_text = "".join(text.split())#/ ' '.join(text.split())
#     for sign in split_text[::-1]:
#         result += sign
#     return result
#
# print(reverse_words("This is an example!")) # ==> "sihT si na !elpmaxe"
# print(reverse_words("double  spaces"))      # ==> "elbuod  secaps"
#
# # Hash words except for last 4 characters
# def maskify(cc):
#     result = ""
#     if len(cc) == 0:
#         return ""
#     if len(cc) > 5:
#         for sign in range(len(cc) - 4):
#             result += "#"
#         return result + cc[-4::]
#     else:
#         return cc
#
# print(maskify("4556364607935616")) # "############5616"
# print(maskify("64607935616"))#    "#######5616"
# print(maskify("1")) #            "1"
# print(maskify( ""))        #    ""
# print(maskify("Skippy"))   #"##ippy"
# print(maskify("Nananananananananananananananana Batman!")) # "####################################man!"


# # Split strings
# def solution(s):
#     result = []
#     iterator = 0
#     while len(s) > 0:
#         result.append(s[iterator:iterator+2])
#     return result
#
#
# print(solution('abcdef'))  # => ['ab', 'cd', 'ef']
# print(solution('Split'))  # => ['Sp', 'li', 't_']
#
def array_diff(a, b):
    result = []
    for sign in a:
        if sign not in b:
            result.append(sign)
    return result


print(array_diff([1,2,2,2,3],[2]))#==

# def get_middle(s):
#     if len(s) % 2 == 0:
#         middle1 = int(len(s)/2 -1)
#         middle2 = int(len(s)/2 +1)
#         return s[middle1:middle2:]
#     else:
#         middle1 = int(len(s) / 2 - 0.5)
#         middle2 = int(len(s) / 2 + 0.5)
#         return s[middle1:middle2:]
#
# print(get_middle('henlo'))

# def odd_or_even(arr):
#     oddnrs = 0
#     for sign in arr:
#         if sign % 2 != 0:
#             oddnrs += 1
#     if oddnrs % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# #
#
#
#
# print(odd_or_even([0, 1, 3, 5, 5]))


# Simple Pig Latin


#
# def pig_it(text):
#     interpunction = ".,!@#$%*&()"
#     piggy = ''
#     for sign in text:
#         if sign is not " ":
#             if sign in interpunction:
#                 piggy.join(sign)
#                 lenght = len(text) - 1
#         else:
#             first_character = text[]
#             text.insert()
#
#
#
#
#
# print(pig_it('Pig latin is cool')) # igPay atinlay siay oolcay
# print(pig_it('Hello world !'))


# def first_non_repeating_letter(string):
#     string_one_cap = string.lower()
#     current_characters = ""
#     result = ""
#     for sign in string_one_cap:
#         sign += current_characters
#         if sign not in current_characters:
#             result += sign
#
#
#
#
# print(first_non_repeating_letter('motylanoga'))


#
#
# for x in range(6):
#     print(' *', end='')
# print()
# for x in range(6):
#     print(' |', end='')
# print()
# for x in range(3):
#     for y in range(7):
#         print('()', end='')
#     print()
#
# def move_zeros(lst):
#     new_lst = []
#     zeros = []
#     for sign in lst:
#         if sign == 0:
#             zeros.append(sign)
#         else:
#             new_lst.append(sign)
#     result = new_lst + zeros
#     return result
# lst = [2,3,0,1,0,2,3]
# print(move_zeros(lst))
#
# def generate_hashtag(s):
#     result = '#'
#     if len(s) == 0 and len(s) > 140:
#         return False
#     else:
#         for sign in s:
#             if sign == ' ':
#                 space_len = s.sign
#                 return s[(sign+1)]
#             if sign != ' ':
#                 result += sign
#         return result
#
#
#
# print(generate_hashtag(" Hello there thanks for trying my Kata")) # =>  "#HelloThereThanksForTryingMyKata"
# print(generate_hashtag("    Hello     World   "))                  # =>  "#HelloWorld"
# print(generate_hashtag(""))                                        # =>  false

# # COMPLETED
# def count(string):
#     result = {}
#     for sign in string:
#         sign_counter = 1
#         if sign not in result:
#             result[sign] = sign_counter
#         else:
#             sign_how_many = result.get(sign)
#             result.update({sign: sign_how_many+1})
#     return result
#
# print(count('asssiaaaaa'))
#


#
# def high():
#     for sign in range(a,z):
#         print(sign)
#
# high()
# # print(high('asssiaaaaa'))

# ZADANIE JAVA NA 15.10


# current_number_counter = 0
# current_number = 0
# max_number_counter = 0
# max_number = 0
# iteration_counter = 0
#
# while True:
#     number = int(input("dej number nie zero: "))
#     if number == 0:
#         if current_number_counter > max_number_counter:
#             max_number = current_number
#             max_number_counter = current_number_counter
#         break
#     else:
#         iteration_counter += 1
#         if iteration_counter != 1:
#             if number != current_number:
#                 current_number = number
#                 current_number_counter = 1
#             else:
#                 if current_number_counter > max_number_counter:
#                     current_number_counter += 1
#                     max_number_counter = current_number_counter
#                     max_number = current_number
#                     current_number_counter = 0
#                 else:
#                     current_number_counter += 1
#         else:
#             max_number = number
#             max_number_counter += 1
#             current_number = number
#             current_number_counter += 1
# print(f'{max_number_counter} times {max_number}')
#
# current_number_counter = 0
# current_number = 0
# max_number_counter = 0
# max_number = 0
# iteration_counter = 0
#
#
# while True:
#     if current_number_counter > max_number_counter:
#         max_number_counter = current_number_counter
#         max_number = current_number
#     input_number = int(input("dej number nie zero: "))
#     if input_number == 0:
#         if current_number_counter > max_number_counter:
#             max_number = current_number
#             max_number_counter = current_number_counter
#         break
#     else:
#         iteration_counter += 1
#         if iteration_counter == 1:
#             max_number = input_number
#             max_number_counter = 1
#             current_number = input_number
#             current_number_counter = 1
#         else:
#             if input_number == current_number:
#                 current_number_counter += 1
#             else:
#                 current_number = input_number
#                 current_number_counter = 1
# print(f'{max_number_counter} times {max_number}')

# def valid_phone_number(phone_number):
#     if phone_number[0] == "(" and phone_number[4] == ")" and phone_number[5] == " " and phone_number[-5] == "-":
#         signs = phone_number[1:3]+phone_number[6:8]+phone_number[-4:]
#         for sign in signs:
#             if sign.isdigit() == True:
#                 return sign
#     else:
#         return False
#
#
# print(valid_phone_number("(1K3) 455-7890"))#  => true
# print(valid_phone_number("(1111)555 2345")) # => false
# print(valid_phone_number("(098) 123 4567")) # =>  false


#
# a = input('a: ') # najmniejsze
# b = input('b: ') # srednie
# c = input('c: ') # najwieksze
#
# print(f'pierwsze {a}, {b}, {c}')
#
#
# if a < b:
#     if b <= c:
#         smallest = a
#         middle = b
#         biggest = c
#     elif b >= c:
#         smallest = a
#         middle = c
#         biggest = b
#     else:
#         smallest = c
#         middle = a
#         biggest = b
# elif a > b:
#     if c >= a:
#         smallest = b
#         middle = a
#         biggest = c
#     elif b < c:
#         smallest = b
#         middle = c
#         biggest = a
#     else:
#         smallest = c
#         middle = b
#         biggest = a
# elif a == b:
#     if a > c:
#         smallest = c
#         middle = a
#         biggest = b
#     else:
#         smallest = a
#         middle = b
#         biggest = c
#
# a = smallest
# b = middle
# c = biggest
#
# print(f'drugie {a}, {b}, {c}')


# Write a program which reads five numbers1 of type int and prints the two greatest
# of them (in particular, it may happen that they are equal). You can define at most
# three variables, not counting the variable for the Scanner.
# Do not use loops or arrays


# def returnbiggestnumber():
#     biggest_number = int(input("Give first number: "))
#     next_input = int(input("Give second number: "))
#
#     second_biggest = 0
#     if next_input >= biggest_number:
#         second_biggest = biggest_number
#         biggest_number = next_input
#     next_input = int(input("Give third number: "))
#     if next_input >= biggest_number:
#         biggest_number = next_input
#     elif next_input >= second_biggest:
#         second_biggest = next_input
#     message = f'Biggest number is: {biggest_number} and second biggest is: {second_biggest}'
#     return message
# print(returnbiggestnumber())


# my_list = [0,0,0,3,2]
# biggest_number = my_list[0]
# next_input = my_list[1]
# second_biggest = 0
#
# if next_input >= biggest_number:
#     second_biggest = biggest_number
#     biggest_number = next_input
# else:
#     second_biggest = next_input
# for number in my_list[2:]:
#     next_input = number
#     if next_input >= second_biggest and next_input <= biggest_number:
#         second_biggest = next_input
#     elif next_input >= biggest_number:
#         second_biggest = biggest_number
#         biggest_number = next_input
# print(f'Biggest number: {biggest_number}, second biggest: {second_biggest}')

# Supporting code for Java assignment, printing out code to insert into Java Switch statements (as required by task instructions)

# for number in range(2,13):
#     print(f"'{number}', ",end="")
# list_of_names = ["Ace", "Deuce", "Trey","Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
# list_of_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
# for number, name in zip(list_of_numbers, list_of_names):
#     print(f'case {number} -> "{name}";')


# my_list = [1,2,3,4,5,67,4,5,2,6,4,6,6,7]
#
# counter = 0
# for number in my_list:
#     for i in range(0, len(my_list)):
#         for j in range(i, len(my_list)):
#             if j not in i:
#                 counter =+ 1
#                 print(j)


# how_big = 6
# snow = ["°", "☆", "●", "★", "*", " ", " "]
#
# for x in range(how_big):
#     for n in range(how_big - x):
#         print(*random.choices(snow), end="")
#     for z in range(x):
#         print("/", end="")
#     for y in range(x):
#         print('\u005c', end="")
#     for n in range(how_big - x):
#         print(*random.choices(snow), end="")
#     print()
# print(x*" " + "||")
# print("𝓜𝓮𝓻𝓻𝔂 𝓒𝓱𝓻𝓲𝓼𝓽𝓶𝓪𝓼")
