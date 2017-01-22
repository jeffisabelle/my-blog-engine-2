"""
Pre generate static content of the blog. To store and serve it via S3.
"""
import os
import codecs
import requests
from bs4 import BeautifulSoup

root_address = "http://localhost:5555"
current_dir = os.getcwd()
# parent_dir = os.path.dirname(os.getcwd())
# output_dir = os.path.join(parent_dir, "static-output")
output_dir = os.path.join(current_dir, "static-output")


def get_html_from_path(url):
    """
    return the html of the page as text
    """
    r = requests.get(root_address + url)
    return r.text


def save_html_files(urls):
    for url in urls:
        filename = url[1:]  # remove the starting /
        if url == "/":
            filename = "index.html"

        path = os.path.join(output_dir, filename)
        with codecs.open(path, "w", "utf8") as f:
            html = get_html_from_path(url)
            f.write(html)


def get_urls():
    r = requests.get(root_address)
    soup = BeautifulSoup(r.text, "html.parser")

    urls = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if href.startswith("/") and len(href) > 3:
            urls.append(href)
    return urls

if __name__ == '__main__':
    urls = get_urls()
    save_html_files(urls)
