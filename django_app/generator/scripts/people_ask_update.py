# pip3 install people_also_ask
from people_also_ask.request import get
from people_also_ask.exceptions import (
    RelatedQuestionParserError,
    FeaturedSnippetParserError
)
from people_also_ask.parser import (
    extract_related_questions,
    get_featured_snippet_parser,
)
from typing import List, Dict, Any, Optional, Generator
from bs4 import BeautifulSoup


URL = "https://www.google.com/search"


def search(keyword: str) -> Optional[BeautifulSoup]:
    """return html parser of google search result"""
    params = {"q": keyword,
              'hl': 'fr',
              "gl": "fr"}
    response = get(URL, params=params)
    return BeautifulSoup(response.text, "html.parser")


def _get_related_questions(text: str) -> List[str]:
    """
    return a list of questions related to text.
    These questions are from search result of text
    :param str text: text to search
    """
    document = search(text)
    if not document:
        return []
    try:
        return extract_related_questions(document)
    except Exception:
        raise RelatedQuestionParserError(text)


def generate_related_questions(text: str) -> Generator[str, None, None]:
    """
    generate the questions related to text,
    these quetions are found recursively
    :param str text: text to search
    """
    questions = set(_get_related_questions(text))
    searched_text = set(text)
    while questions:
        text = questions.pop()
        yield text
        searched_text.add(text)
        questions |= set(_get_related_questions(text))
        questions -= searched_text


def get_related_questions(text: str, max_nb_questions: Optional[int] = None):
    """
    return a number of questions related to text.
    These questions are found recursively.
    :param str text: text to search
    """
    if max_nb_questions is None:
        return _get_related_questions(text)
    nb_question_regenerated = 0
    questions = set()
    for question in generate_related_questions(text):
        if nb_question_regenerated > max_nb_questions:
            break
        questions.add(question)
        nb_question_regenerated += 1
    return list(questions)