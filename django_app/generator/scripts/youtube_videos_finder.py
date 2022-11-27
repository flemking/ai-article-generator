import urllib.request
from urllib import parse
import re
import random

def found_vid(keyword):
    keyword = parse.quote_plus(keyword)
    # print(keyword)
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={keyword}")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_chosen = f"""<iframe width="560" height="315" src="https://www.youtube.com/embed/{video_ids[0]}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""
    return video_chosen                                            
