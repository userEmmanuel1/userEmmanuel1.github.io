my_list = [
    "3 love",
    "6 computers",
    "2 dogs",
    "4 cats",
    "1 I",
    "5 you"
]

my_dict = {}

for item in my_list:
    number, text = item.split(maxsplit=1)  # Split each item into number and text
    my_dict[int(number)] = text.strip()  # Convert number to integer and remove any leading/trailing whitespaces from text

print(my_dict)

def love_comps(my_dict):
    num = 1
    for i in range (1, my_dict +1):
        print(" " *(my_dict-1), end = "")

        for j in range(1, 2 * i):
            print(num % 10, end="")
            num +=1

        print()

print(love_comps(my_dict))
