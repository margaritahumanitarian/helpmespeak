import openai
import os
from dotenv import load_dotenv
from dotenv.main import find_dotenv

import functions

# getting the API key from env
load_dotenv(find_dotenv())
openai.api_key = os.environ.get("openai.api_key")

# user input
query = str(input("input: "))

# test case
# query = "It looks like the deadline on the AI for accessibility grant has moved to January 12, 2022. I'm interested in working closely with at least one intern on pair programming to build a prototype that uses AI and/or match machine learning. For the internship position, we will be screen sharing for 1 to 2 hours a day. "

# create summary 
summary = functions.summarizer(query)

# output
fobj = open("summary.txt","w")

fobj.write(f"##Original Text:\n{query}\n")
fobj.write(f'\n-[] First Summary:\n {summary[0]} \n ')
fobj.write(f'\n-[] Second Summary:\n {summary[1]} \n ')
fobj.write(f'\n-[] Third Summary:\n {summary[2]} \n ')

fobj.close()