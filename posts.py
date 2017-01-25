import markdown2


class Post(object):
    def __init__(self, title, slug, md_path):
        self.title = title
        self.slug = slug
        self.excerpt = self.excerptify(md_path)
        self.content = self.htmlify(md_path)

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
    ),
    Post(
        title="Less Design, More Posts",
        slug="less-design-more-posts",
        md_path="posts/less-design-more-posts.md",
    ),
    Post(
        title="My Thoughts on Startup Weekend Izmir",
        slug="my-thoughts-on-startup-weekend-izmir",
        md_path="posts/my-thoughts-on-startup-weekend-izmir.md",
    ),
    Post(
        title="Do Memory Optimizers Really Work?",
        slug="do-memory-optimizers-really-work",
        md_path="posts/do-memory-optimizers-really-work.md",
    ),
    Post(
        title="The Real Usage Statistics of Linux",
        slug="the-real-usage-statistics-of-linux",
        md_path="posts/the-real-usage-statistics-of-linux.md",
    ),
    Post(
        title="Some Words on Package Managers, Wine and Strace",
        slug="some-words-on-package-managers-wine-and-strace",
        md_path="posts/some-words-on-package-managers-wine-and-strace.md",
    ),
    Post(
        title="Kernel Based Virtual Machines",
        slug="kernel-based-virtual-machines",
        md_path="posts/kernel-based-virtual-machines.md",
    ),
    Post(
        title="Using Aspell as a Scrabble Helper",
        slug="using-aspell-as-a-scrabble-helper",
        md_path="posts/using-aspell-as-a-scrabble-helper.md",
    ),
    Post(
        title="Subtitle Problems on Ubuntu Linux",
        slug="subtitle-problems-on-ubuntu-linux",
        md_path="posts/subtitle-problems-on-ubuntu-linux.md",
    ),
]
