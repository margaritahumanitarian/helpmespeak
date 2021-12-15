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

# create summary 
summary = functions.summarizer(query)

# output
fobj = open("summary.txt","w")

fobj.write(f"##Original Text:\n{query}\n")
fobj.write(f'\n-[] First Summary:\n {summary[0]} \n ')
fobj.write(f'\n-[] Second Summary:\n {summary[1]} \n ')
fobj.write(f'\n-[] Third Summary:\n {summary[2]} \n ')

fobj.close()