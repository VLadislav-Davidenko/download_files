#!/usr/bin/env python
import requests


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


download("https://group-media.mercedes-benz.com/marsMediaSite/scr/1595861642000/46940473v-2tv3/Mercedes-AMG%20GT"
         "%20now%20available%20to%20order%20as%20Coup%C3%A9%20and%20Roadster.jpg")