import inflect

p = inflect.engine()
sample_list = []
while True:
    try:

        sample_list.append(input())
    except EOFError:

        break
mylist = p.join(sample_list, final_sep=",")
print(f"Adieu, adieu, to {mylist}")
