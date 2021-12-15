# making query tags a constants 

grammar = '\nStandard American English:'
tldr = "\n tl;dr:"
inotherwords = "\nIn other words:"
onesentence = "\nOne-sentence summary:"
grader = '\nI rephrased this for my daughter, in plain language a second grader can understand:'

def gettoken(token):
    return int((token)/4)