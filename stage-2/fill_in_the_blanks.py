def level(userChoice):

    # Levels
    """

    All text levels defined for the game

    Returns: String selected

    """
    if userChoice == "easy":
        text = '''Basketball is a ___1___ sport. Two teams of ___2___ players each try to score by shooting a
         ___3___ through a hoop elevated 10 feet above the ground.The game is played on a rectangular floor called the
          ___4___, and there is a hoop at each end.'''
    elif userChoice == "medium":
        text = '''The court is divided into two main sections by the mid-court line. If
        the ___1___ team puts the ball into play behind the mid-court line, it has ___2___ seconds to get the ball
        over the mid-court line. If it doesn't, then the ___3___ gets the ball. Once the ___4___ team gets the
        ball over the mid-court line, it can no longer have possession of the ball in the area in back of the line.
        If it does, the defense is awarded the ball. '''
    else:
        text = '''Each team is assigned a ___1___ or goal to defend. This means that the other basket is their ___2___ basket.
        At halftime, the teams switch goals. The game begins with one player from either team at center court.
        A ___3___ will toss the ball up between the two. The player that gets his hands on the ball will tip it to a
        ___4___. This is called a tip-off. In addition to ___5___ the ball from an opposing player, there are other
        ways for a team to get the ball.'''
    return text

def answers(userChoice):
    """
    The correct answers for the specific level selection
    chosen by the player.

    Returns: list of answers

    """
    if userChoice == "easy":
        answer = ["team", "five", "ball", "court"]
    elif userChoice == "medium":
        answer = ["offensive", "ten", "defense", "ball"]
    else:
        answer = ["basket", "scoring","referee","teammate", "stealing"]

    return answer


def difficultyLevel():
    """
    User to define difficulty level
    Selected level is returned to proceed with game

    """
    print "Please select the game difficulty by typing it in!"
    d_Level = raw_input("Possible choices include easy, medium, and hard.")
    print " "

    # Incorrect Level Assignment
    while d_Level.lower() != "easy" and d_Level.lower() != "medium" and d_Level.lower() != "hard":
        print "That's not an option"
        print "Please select a game difficulty by typing it in"
        d_Level = raw_input("Possible choices include easy, medium, and hard.")
        print " "

    return d_Level


def falseTries():
    '''User to define number of possible tries before losing the game'''
    # Number of false tries
    tries = input("How many wrong guesses do you want to make before losing?")
    return tries


def word_in_pos(blankNum,word):
    """
    This function checks to find the numbered blanks
    :param blankNum: the blank at which we are at
    :param word: word of the text at which we are currently searching
    :return: the blank to be replaced

    """
    if word == "___"+str(blankNum)+"___":
        return word
    else:
        return None


def fill_string(blankNum,text,userAnswer):
    """
    This function initializes the replacement of the blanks with a user defined value
    :param blankNum: the blank at which we are at
    :param text: the text selected from easy / medium / hard
    :param userAnswer: user defined word
    :return: the modified text

    """
    new_ml_string = []
    ml_string = text.split()
    for word in ml_string:
        replacement = word_in_pos(blankNum,word)
        if replacement != None:
            word = word.replace(replacement, userAnswer)
            new_ml_string.append(word)
        else:
            new_ml_string.append(word)
    new_text = " ".join(new_ml_string)
    return new_text

def userCalls():

    # Select difficulty level
    userDifficulty = difficultyLevel()

    # Number of false tries
    tries = falseTries()

    # Set Level
    text = level(userDifficulty)
    answer = answers(userDifficulty)

    return userDifficulty, tries, text, answer

def logic(blankNum, ans, tries, text, answer):

    while blankNum <= len(answer):
        userInput = raw_input("What should be substituted in for ___" + str(blankNum) + "___.")
        index = blankNum - 1
        if userInput.lower() == answer[index]:
            print "Correct!"
            text = fill_string(blankNum, text, userInput)
            blankNum += 1
        else:
            remTries = tries - ans
            print "Incorrect!"
            print "You have " + str(remTries) + " more tries"
            ans += 1
        if ans > tries:
            print "Sorry, you have lost! Try again.."
            break
        print text
        if blankNum > len(answer):
            print "Congratulations You WON!!"



def playGame():
    """ This function is the Main() function of the game.
    Initializing this sets up basic parameters and further calls to play the game .
    """

    # User Option Calls
    prefs = userCalls()
    userDifficulty, tries, text, answer = prefs[0], prefs[1], prefs[2], prefs[3]

    # Print User Preferences
    print " "
    print "You have chosen to play the " + userDifficulty + " level with " + str(tries) + " attempts per blank"
    print "The current paragraph reads as such:"
    print " "
    print text

    blankNum = 1
    ans = 1

    logic(blankNum, ans, tries, text, answer)




playGame()
