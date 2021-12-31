import openai

# Importing constants for prompt
import tags
from samples.voicedictation.colon import colon_eg as colon
from samples.voicedictation.deleteLastWord import delete_eg as deleteLastWord
from samples.voicedictation.parenthesis import parenthesis_eg as parenthesis
from samples.voicedictation.period import period_eg as period
from samples.voicedictation.send import send_eg as send
from samples.voicedictation.space import space_eg as space
from samples.grammar.capital import capital_eg as capital
from samples.grammar.repetetion import repetetion_eg as repetetion

def grammerCorrection(content):
        '''
        Returns a string with standard American english Grammer 

                Parameters:
                        content (str): content (sentence, paragraph) by the user 

                Returns:
                        response.choices[0].text (str): text response from the API without grammatical errors
        '''
        text = f"{tags.grammar_fix}{capital}{repetetion}{tags.promptStart}{content}{tags.promptEnd}"
        
        response = openai.Completion.create(
                engine="davinci",
                prompt=text,
                temperature=0.3,
                max_tokens=400,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["###"]
        )

        return response.choices[0].text

def modal_one(content):

    '''
    Returns a summary using the curie engine from completion endpoint

            Parameters:
                    content (str): content (sentence, paragraph) by the user 

            Returns:
                    response.choices[0].text (str): text response from the API 
    '''

    text = f"{content} {tags.tldr}"

    response = openai.Completion.create(
        engine="curie",
        prompt=text,
        temperature=0.3,
        max_tokens=140,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    return response.choices[0].text

def modal_two(content):

    '''
    Returns a summary using the davinci engine from completion endpoint

            Parameters:
                    content (str): content (sentence, paragraph) by the user 

            Returns:
                    response.choices[0].text (str): text response from the API 
    '''

    text = f"{content} {tags.tldr}"

    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        temperature=0.3,
        max_tokens=140,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    return response.choices[0].text

def modal_three(content):

    '''
    Returns a summary using the davinci engine from completion endpoint

            Parameters:
                    content (str): content (sentence, paragraph) by the user 

            Returns:
                    response.choices[0].text (str): text response from the API 
    '''

    text = f"{content} {tags.inotherwords}"

    response = openai.Completion.create(
        engine="davinci",
        prompt=text,
        temperature=0,
        max_tokens=140,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["."]
    )
    return response.choices[0].text

def summarizer(query):
        
        '''
        Returns the same string as the user's query but removes voice dictation error like "delete last word, period, colon, parenthesis, send, space"

                Parameters:
                        query (str): Query (sentence, paragraph) by the user
                
                Returns:
                        Res (str); Response without voice dictation errors (space, period, delete last word)
        '''
        text = f"{tags.verbatim_fix}{space}{period}{deleteLastWord}{colon}{send}{parenthesis}{tags.promptStart}{query}{tags.promptEnd}"
        
        response = openai.Completion.create(
                engine="davinci",
                prompt=text,
                temperature=0.3,
                max_tokens=400,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["###"]
        )
        responseText = response.choices[0].text
        final = grammerCorrection(responseText) 
        return final

def summarizer2(query):

        '''
        Returns three different summaries of the query by the user 

                Parameters:
                        query (str): Query (sentence, paragraph) by the user 

                Returns:
                        [ summary1 , summary2 , summary3 ] : list of different summary of the query by the user
        '''

        text = grammerCorrection(query)

        r1 = modal_one(text)
        r2 = modal_two(text)
        r3 = modal_three(text)

        return [r1,r2,r3,text]