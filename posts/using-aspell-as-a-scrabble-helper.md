This semester I'm taking Artificial Intelligence course at college. Last semester, when I was taking Data Mining, I did learn some of the classification and clustering Machine Learning algorithms, so I wanted to choose a project for AI class that is both challenging & pragmatical and does not contains ML in it.

This made me think about algorithmic solutions of scrabble and I decided to take it as a course project and build an Artificially Intelligent scrabble player.

As almost anything in computer science, there is some work done for scrabble AI. I have looked at what's happening on that era yesterday, there is two major data-structures to store the all possible words in memory. These are the DAWG data structure and GADDAG data structure which use tree like structure for an efficient storing & searching. I'll look into them and probably will write another blog post for them later.

But, before I dive into those data structures, I thought possible helpers that can help me playing this game. I would need a dictionary first, aspell come in mind instantly. I knew it because one of my friends worked with it for auto completion. I grabbed it and started to work with it.

Aspell is a spell checker which is built by GNU and it is used for spell checking on many of the GNU tools. Thankfully it has a dump action which make it easy to work with it.


    16:08 ~/ $ aspell -l tr dump master

This will dump all the Turkish words to stdout. So we can easily use regular expressions to dig the dictionary. By default, It has 80,261 Turkish words on it and it is ~1mb.

To make calculations faster, I reduced the dictionary by removing the words that are greater then the 9 letters and saved the result to a text file.

    16:08 ~/ $ aspell -l tr dump master | egrep '^\w{1,9}$' > dict.txt

This end up with 17,807 words which is around 135kb. For one look up this is not necessary, but for brute forcing the dictionary it is a good way to improve the performance for sure.

I kept using master dump for quick searches. So If the rack has BEL in somewhere and if I need 5 letters words that starts with BEL, it was just a simple regex to get the result.

    16:11 ~/ $ aspell -l tr dump master | egrep '^bel\w{2}$'
    belli
    belce
    belde
    belge
    belgi
    :
    :

Of course, I needed to automate this in some way, because it depends on the hand on scrabble. So, I wrote a python script to get all the permutations of the hand and grep them from the dictionary to get the possible words. Here is the script source to let you know whats going on.

    # -*- coding: utf-8 -*-
    from itertools import permutations
    import commands
    import time


    class WordTools():
        def is_valid_word(self, word):
            """
            check if the given word is present in dictionary

            - `word`: word to be written
            """
            regex = "^" + word + "$"
            command = "egrep " + regex + " dict.txt"
            return commands.getstatusoutput(command)

        def can_be_written(self, pieces, word, max_word_length):
            """

            Arguments:
            - `pieces`: pieces that hand contains
            - `word`: word to be written
            - `max_word_length`: maximum word length
            """

            # i refers to combinations
            # and it starts with 2 letters
            # for i in range(len(pieces) - 1):
            for i in range(max_word_length - 1):
                perms = list(set(permutations("".join(pieces), i + 2)))
                for token in perms:
                    word = "".join(token)
                    if self.is_valid_word(word)[1] != '':
                        print word


    start_time = time.time()

    word_tools = WordTools()
    word_tools.can_be_written(
        ["k", "k", "i", "z", "s", "l", "j", "o"], "", 4)

    print time.time() - start_time, "seconds"

The script I wrote is pretty straight forward. If I had a hand that contains "k", "k", "i", "z", "s", "l", "j", "o", I just need to make that letters an array and run the script to get possible words.

This will end up with an output similar like this;


    16:08 ~/okul/artificialintelligence/src $ python utils.py
    ok
    il
    ki
    si
    is
    iz
    kil
    kol
    ski
    ilk
    zil
    iks
    koz
    lok
    kik
    siz
    sol
    kok
    kilo
    kils
    silo
    klik
    koli
    4.21648097038 seconds


If you look at the time spent on just to find out for maximum 4 letter words it took ~4 seconds. Which is sloooooooowwww. (Those data structures I have mentioned is out for some reason)

Yet, this grows exponentially if we would like to find out 5 or 6 letters words and it can take 40 to 100 seconds to calculate. But still, it's a good start. This information is not enough to win a scrabble game as AI, It may help to a person, but there is too much work needed to make it competitive AI scrabble player.

I'll work on it when I have time, and make a new blog posts about the project I will be working for the course. This is it, for now. :)
