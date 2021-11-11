from yaml import dump
from requests import get
from bs4 import BeautifulSoup
from re import findall

yaml_file = get("https://www.w3schools.io/file/yaml-sample-example/")
tags = BeautifulSoup(yaml_file.text, "html5lib")
comment_scrapper = tags.findAll('span')
yaml_text = [span.text for span in comment_scrapper]
yaml_text_string = " ".join([str(i) for i in yaml_text])
comments = findall("# .*", yaml_text_string)

with open("scrapped_yaml", "w") as file:
    dump(comments, file)