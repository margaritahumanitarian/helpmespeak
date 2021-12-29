import openai
import os
from dotenv import load_dotenv
from dotenv.main import find_dotenv

import functions

# getting the API key from env
load_dotenv(find_dotenv())
openai.api_key = os.environ.get("openai.api_key")

# user input
query = str(input("Input: "))

#test case
# query = """
# Hi@ codemuncher I am currently unable to use my hands to type without extreme pain. For the past couple months I couldn't get typing through voice dictation to work in discord. On December 4 famousfigures show me a hack that got it to work on my computer. Basically to enable voice typing I have to show the on screen keyboard. Now I am finally able to communicate my ideas via chat instead of chewing them up in my head for when my hands get better. Thank you for asking and for thinking of me. Pardon any errors due to voice dictation period"""

# create summary 
string = functions.summarizer(query)


# output
fobj = open("summary.txt","a")
fobj.write("\n###\n")
fobj.write(f"User text with speech-to-text errors: {query}\n")
# fobj.write(f'\n-[] First Summary:\n {summary[0]} \n ')
# fobj.write(f'\n-[] Second Summary:\n {summary[1]} \n ')
# fobj.write(f'\n-[] Third Summary:\n {summary[2]} \n ')
# fobj.write(f'\n-[] American English:\n {summary[0]} \n ')
fobj.write(f'\n###\nUser text without speech-to-text errors: {string}')

fobj.close()