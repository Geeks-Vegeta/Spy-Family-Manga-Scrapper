import requests
from bs4 import BeautifulSoup
import os
import re


url = "https://spyxfamily.xyz/manga/spy-x-family-chapter-1/"
search_name = re.search(".{23}$", url)
folder_name = search_name.group().replace("-", "_").replace("/", "")
os.mkdir(folder_name)


def main():

    try:

        response = requests.get(str(url)).text.encode('utf8').decode('ascii', 'ignore')
        soup = BeautifulSoup(response, 'html.parser')
        find_all_images = soup.find_all("img", class_="wp-manga-chapter-img")

        images=[]

        for data in find_all_images:
            images.append(" ".join(data['data-src'].strip().split()))

        for image in images:

            req = requests.get(image)
            name=re.search(".{8}$", image)

            with open(f"{folder_name}/{name.group()}", "wb") as f:
                f.write(req.content)

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
