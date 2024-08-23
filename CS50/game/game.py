import random
def main():
    rand()

def rand():
  while True:
    n = input("Level: ")
    if n.isnumeric() and int(n)>=1:
         return guess(random.randint(1,int(n)))
    else:
        continue

def guess(key):
    while True:
       guess_input =  input("Guess :")
       if guess_input.isnumeric():
        guess_input = int(guess_input)
        if guess_input == key:
          print("Just right!")
          break
        elif guess_input > key:
          print("Too large!")
        else:
          print("Too small!")
       else:
        continue

if __name__ == "__main__":
    main()
    



