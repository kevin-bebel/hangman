from random import randrange
def getword():
    try:
        fh = open('words.txt')
        words = fh.readlines()
        fh.close()
        word = words[randrange(0,len(words))]
        return word.strip()
    except IOError:
        print("Error Openning/Locating File")
        return ''

def setup(word):
    letters = [char for char in word] #converting the word in a list for later use
    placeholder = ["_" for char in letters] #this will contain the corrected selected letters and also the underscores printed on the screen
    print("Ok, Lets start to play!")
    print("This word is {} letter long".format(len(word)))

    print("")

    print(" ".join(placeholder))
    print("")
    return(letters,placeholder) #tuple unwrapping for multi returns 

def main():
    word = getword()
    #word = 'proxy'
    letters,placeholder = setup(word)

    tries = -1
    tries_display = []
    while True :
        guess = input("Guess a letter in the word : ")
        try:
            #print(letters) # -- Here for debug purposes --
            idx = letters.index(guess.strip()) 
            #Get the index and replace the placehoder with guessed
            if idx > -1:
                placeholder[idx] = guess
                letters[idx] = "_"
                print(" ".join(placeholder).upper())

                if "".join(placeholder) == word:
                    print("Congratulations! You guessed the word right!")
                    break
        except ValueError as e:
            print("OOPS like you guessed wrong!")
            print("")
            tries += 1
            tries_display.append("HANGMAN"[tries])
            print("============= {} =============".format("".join(tries_display)))
            print("")
            print(" ".join(placeholder).upper())
            print("")
            if len(tries_display) == len("HANGMAN"):
                print("Game Over. The word is {}".format(word.upper()))
                break

if __name__ == "__main__":main()
