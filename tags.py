# making query tags a constants 

tldr = "\n tl;dr:"
inotherwords = "\nIn other words:"
onesentence = "\nOne-sentence summary:"
grader = '\nI rephrased this for my daughter, in plain language a second grader can understand:'

verbatim_fix = """\nVoice recognition technology has come a long way, but it is still very error-prone. Often what the person dictates does not match what the person actually wants to type.
A few examples for removing the unnecessary word from the user's text are:"""

promptStart = """\n###\nUser text with speech-to-text errors: """

promptEnd = """\n###\nUser text without speech-to-text errors: """

def gettoken(token):
    return int((token)/4)