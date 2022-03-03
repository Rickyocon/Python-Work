from random import*;
iSecret = randint(1, 1024);
iNum = -1;
iTimes = 0;
while iSecret!=iNum:
    iNum = int(input("whats your guess: "));
    iTimes = iTimes + 1;
    if iNum>iSecret:
        print("Guess a smaller number!");
    if iNum<iSecret:
        print("Guess a larger number!");
print("You have guessed the correct number");
print("You have guessed " + str(iTimes) + " times");
