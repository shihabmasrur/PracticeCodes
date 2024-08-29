import random;
print ("Welcome TO The Valorant Hangman!")

words = ['kj' , 'sova', 'neon', 'omen' , 'clove'];

theWord = random.choice(words); 
displayWord = ['_' for _ in theWord];
#print(displayWord);

attempts = 10;

while (attempts > 0 and '_' in displayWord):
    print("\n" + " ".join(displayWord));
    guess = input("Guess A letter").lower();
    if guess in theWord:
        for index, letter in enumerate(theWord):  #the enumerate function adds index to iterable stuff like for here we are going to add indexing to our word.
            
            if letter == guess:
                displayWord[index] = guess; #changing the indext letter of the word to guessed letter when player guesses correctly
                print(theWord + " is correct"+"\n"+"n1 wp" + "\n" + "gg");
    else:
        print("dafuq noob bronze guessing or wut?!");
        attempts -= 1;




