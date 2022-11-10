#! /usr/bin/env python3
from people_ask_update import get_related_questions
import sys
import re

import openai
import config

from suggestions import get_title
from youtube_videos_finder import found_vid
from datetime import datetime
import time

# record start time
start = time.time()

################################################################

the_title = ""
final_questions = []

def get_title_and_subtitle(mc):
    questions = []
    print("Mot cle: ", mc, '\n')
    suggestion = get_title(str(mc))
    print("Les suggestions de Google: ", suggestion, '\n')
    if suggestion != [] and config.suggestions_google == True:
        the_title = suggestion[0]
    else:
        the_title = mc
    test = get_related_questions(the_title  + ' ')
    questions += test
        
    # uncomment if using many keywords
    #questions = list(set(questions))
    #print(questions)

    # fix the questions strings
    for question in questions:
        new_question = re.search(r"(.*[?$])Rechercher", question)
        if new_question:
            final_questions.append(new_question.group(1))

    # print the questions
    # for i in final_questions:
    #     print('\n', i)
    
    return the_title, final_questions

# openai section

def write_article(the_title, final_questions):
    
    openai.api_key = config.KEY

    sous_titre = ''

    response_intro = openai.Completion.create(model=config.model,
                                            prompt=f"{config.templates[0].format(the_title)}",
                                            temperature=0.7,
                                            max_tokens=500,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0
                                            )
    response_conclusion = openai.Completion.create(model=config.model,
                                                prompt=f"{config.templates[2].format(the_title)}",
                                                temperature=0.7,
                                                max_tokens=500,
                                                top_p=1,
                                                frequency_penalty=0,
                                                presence_penalty=0
                                                )

    paragraphs = ""
    for i in final_questions:
        sous_titre = i
        response_article = openai.Completion.create(model=config.model,
                                                prompt=f"{config.templates[1].format(sous_titre)}",
                                                temperature=0.7,
                                                max_tokens=500,
                                                top_p=1,
                                                frequency_penalty=0,
                                                presence_penalty=0
                                                )

        sous_titre_image = openai.Image.create(
        prompt=sous_titre,
        n=1,
        size="1024x1024"
        )

        paragraphs += sous_titre_image['data'][0]['url'] + '\n' + f'\n<h2>{sous_titre.upper()}</h2>\n' + response_article.choices[0].text + '\n'

    featured_image = openai.Image.create(
    prompt=the_title,
    n=1,
    size="1024x1024"
    )

    video_yt = found_vid(the_title)
    print(video_yt)

    # print("\n", f"<h1>{the_title}</h1>", "\n")
    # print("\n", response_intro.choices[0].text)
    # print("\n", paragraphs)
    # print(f"\n <h2>CONCLUSION</h2>\n", response_conclusion.choices[0].text)
    return f"""
    {featured_image['data'][0]['url']}
    \n<h1>{the_title}</h1>
    \n{response_intro.choices[0].text}
    \n{paragraphs}
    \n<h2>CONCLUSION</h2>\n {response_conclusion.choices[0].text}
    """


# record end time
end = time.time()

if __name__ == "__main__":
    for mc in config.new_mc:
        the_title, final_questions = get_title_and_subtitle(mc)
        output = write_article(the_title, final_questions)
        currentDateTime = datetime.now().strftime("%Y%m%d-%H%M%S")
        path = f"articles/{the_title}-{currentDateTime}.txt"
        with open(path, "w") as txt:
            txt.write(output)
    print(f"\nLe script a pris: {end-start}s")
