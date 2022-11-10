import urllib.request
import re
import random

def found_vid(keyword):
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={keyword}")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    # print(video_ids)
    video_chosen = random.choice(video_ids)
    return video_chosen