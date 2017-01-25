If you are running a linux distro and you need subtitles when watching series and movies, it is more than likely that you have trouble with subtitles when it comes to non-english characters. The problem comes from character encoding, they usually encoded for windows codesets instead of utf-8 or similar.

So, if your media player can't render your native language specific characters, you probably open the text file with windows character set from your text editor (gedit, kedit, etc.) end you save as the document with utf-8 encoding. That simply solves the problem, but it's kinda headache especially when you are watching 20min sitcoms or something like that, you have to open the editor and change the character set for every single episode.

Instead, I did code a nautilus script that takes a folder and change any files encoding inside that folder. In my case, It is changing windows-1254 character encodes (turkish) to utf-8. I think it is a problem for any language that has special characters. You can find the correct encoding set depending on your language from this wikipedia article and then just change the relevant line from the source code.

http://en.wikipedia.org/wiki/Character_encoding By default, nautilus scripts are placed in /home/.gnome2/nautilus-scripts folder. And you call that scripts by right clicking any folder or file and expanding the Scripts item.


    #!/usr/bin/python

    import os
    import codecs

    selected = os.environ.get('NAUTILUS_SCRIPT_SELECTED_FILE_PATHS', '')

    def convert_line_ending(filename):
        old = codecs.open(filename, encoding='windows-1254', mode='r')
        newname = "utf-"+filename
        new = codecs.open(newname, encoding='utf-8',mode='w+')

        for line in old:
            new.write(line)

    if selected:
        target = selected.splitlines()[0]
        listing = os.listdir(target)

        os.chdir(target)

        for file in listing:
            if not file.startswith("utf-"):
                if file.endswith(".srt"):
                    try:
                        convert_line_ending(file)
                    except:
                        pass


after you put these script into /home/.gnome2/nautilus-scripts/scriptname make it executable. (yes this is mandatory)

    chmod +x scriptname

then you are good to go.

![ubuntu](http://www.ibm.com/developerworks/linux/library/l-script-linux-desktop-2/figure1.jpg)

more on nautilus scripting;
http://www.ibm.com/developerworks/linux/library/l-script-linux-desktop-2/index.html

some useful nautilus scripts;
http://www.techdrivein.com/2010/09/6-useful-nautilus-extensions-and.html
