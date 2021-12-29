import openai

# Importing constants for prompt
import tags
import samples.colon as colon
import samples.deleteLastWord as deleteLastWord
import samples.parenthesis as parenthesis
import samples.period as period
import samples.send as send
import samples.space as space

def grammerCorrection(content):
    '''
    Returns a string with standard American english Grammer 

            Parameters:
                    content (str): content (sentence, paragraph) by the user 

            Returns:
                    response.choices[0].text (str): text response from the API 
    '''

    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Original:\n{content}\n###{tags.grammar}",
        temperature=0,
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
                        Res (str); Response with removed voice dictation errors (space, period)
        '''
        text = f"{tags.verbatim_fix}{space.space_eg}{period.period_eg}{deleteLastWord.delete_eg}{colon.colon_eg}{send.send_eg}{parenthesis.parenthesis_eg}{tags.promptStart}{query}{tags.promptEnd}"
        
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

# def summarizer(query):

#     '''
#     Returns three different summaries of the query by the user 

#             Parameters:
#                     query (str): Query (sentence, paragraph) by the user 

#             Returns:
#                     [ summary1 , summary2 , summary3 ] : list of different summary of the query by the user
#     '''

#     text = grammerCorrection(query)

#     r1 = modal_one(text)
#     r2 = modal_two(text)
#     r3 = modal_three(text)

#    return [r1,r2,r3,text]