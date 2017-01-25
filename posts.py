from datetime import datetime
import markdown2


class Post(object):
    def __init__(self, title, slug, md_path, published):
        self.title = title
        self.slug = slug
        self.excerpt = self.excerptify(md_path)
        self.content = self.htmlify(md_path)
        self.publish_date = published

    def htmlify(self, md_path):
        """make html out of markdown file"""
        md = open(md_path, "r").read()
        return markdown2.markdown(md)

    def excerptify(self, md_path):
        md = open(md_path, "r").read()
        splitted = md.split("\n")
        return splitted[0]

    @classmethod
    def all(self):
        """return all posts"""
        return data

    @classmethod
    def one(self, slug):
        """return single post from the slug"""
        for post in data:
            if post.slug == slug:
                return post

        return None

data = [
    Post(
        title="Cool Domains with a Little Bit Hack",
        slug="cool-domains-with-a-little-bit-hack",
        md_path="posts/cool-domains-with-a-little-bit-hack.md",
        published=datetime(2014, 7, 7, 6, 30, 00)  # year, month, day
    ),
    Post(
        title="Less Design, More Posts",
        slug="less-design-more-posts",
        md_path="posts/less-design-more-posts.md",
        published=datetime(2014, 7, 6, 6, 30, 00)  # year, month, day
    ),
    Post(
        title="My Thoughts on Startup Weekend Izmir",
        slug="my-thoughts-on-startup-weekend-izmir",
        md_path="posts/my-thoughts-on-startup-weekend-izmir.md",
        published=datetime(2013, 11, 22, 6, 30, 00)  # year, month, day
    ),
    Post(
        title="Do Memory Optimizers Really Work?",
        slug="do-memory-optimizers-really-work",
        md_path="posts/do-memory-optimizers-really-work.md",
        published=datetime(2013, 11, 12, 6, 30, 00)  # year, month, day
    ),
    Post(
        title="The Real Usage Statistics of Linux",
        slug="the-real-usage-statistics-of-linux",
        md_path="posts/the-real-usage-statistics-of-linux.md",
        published=datetime(2013, 7, 3, 6, 30, 00)  # year, month, day
    ),
    Post(
        title="Some Words on Package Managers, Wine and Strace",
        slug="some-words-on-package-managers-wine-and-strace",
        md_path="posts/some-words-on-package-managers-wine-and-strace.md",
        published=datetime(2013, 5, 24, 6, 30, 00)  # year, month, day
    ),
    Post(
        title="Kernel Based Virtual Machines",
        slug="kernel-based-virtual-machines",
        md_path="posts/kernel-based-virtual-machines.md",
        published=datetime(2013, 5, 21, 6, 30, 00)  # year, month, day
    ),
    Post(
        title="Using Aspell as a Scrabble Helper",
        slug="using-aspell-as-a-scrabble-helper",
        md_path="posts/using-aspell-as-a-scrabble-helper.md",
        published=datetime(2013, 5, 12, 6, 30, 00)  # year, month, day
    ),
    Post(
        title="Subtitle Problems on Ubuntu Linux",
        slug="subtitle-problems-on-ubuntu-linux",
        md_path="posts/subtitle-problems-on-ubuntu-linux.md",
        published=datetime(2012, 10, 18, 6, 30, 00)  # year, month, day
    ),
]
