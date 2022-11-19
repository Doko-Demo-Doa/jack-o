import os
from typing import Union
import requests
from bs4 import BeautifulSoup, Tag, NavigableString
from urllib.parse import urljoin
from dotenv import load_dotenv
from github import Github, InputFileContent

load_dotenv()


# First create a Github instance:

# using an access token
g = Github(os.getenv("GITHUB_TOKEN"))

# Then play with your Github objects:
target_gist = g.get_gist(os.getenv("DORA_WORLD_GIST_ID"))


def diff(li1, li2):
    set_dif = set(li1).symmetric_difference(set(li2))
    temp3 = list(set_dif)
    return temp3


g_desktop_list = str(
    target_gist.files['desktop-wallpapers.txt'].content).splitlines()


URL = "https://dora-world.com/wallpaper"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

wallpaper_boxes = soup.find_all("div", class_="wallpaper_box")
wallpaper_box_desktop: Union[Tag, NavigableString] = wallpaper_boxes[0]
wallpaper_box_mobile: Union[Tag, NavigableString] = wallpaper_boxes[1]

desktop_items: list[Union[Tag, NavigableString]
                    ] = wallpaper_box_desktop.find_all("div", class_="item")

mobile_items: list[Union[Tag, NavigableString]
                   ] = wallpaper_box_mobile.find_all("div", class_="item")

desktop_lst: list[str] = []
for item in desktop_items:
    link = item.find("a")
    link_url = link["href"]

    desktop_lst.append(urljoin(URL, link_url))

list_diff = diff(desktop_lst, g_desktop_list)
if len(list_diff) > 0:
    input_file_content = InputFileContent(
        content='\n'.join(desktop_lst)
    )
    content_dict = {
        'desktop-wallpapers.txt': input_file_content
    }
    target_gist.edit(files=content_dict)

for item in mobile_items:
    link = item.find("a")
    link_url = link["href"]
    # print(urljoin(URL, link_url))
