I hate domain business. I honestly do. Every single time I come up with an idea, I instantly look for a domain that is catchy enough and suitable for the project. But it usually end up already taken or listed as premium for 1000$. I hate those premium domains.

Domains like getmyapp.com, usethis.com or thefacebook.com seems weird to me too.

You want advice?  
drop the 'the'. just facebook. it's cleaner.

Well, dropping THE is not cheap either. But dropping .COM is a more viable option today. There are bunch of ccTLDs to choose from. However it is not easy to check for bunch of registrar if the domain is available. Forget checking, it is even difficult to think a meaningful domain.

So, I tried to find a way to look for domains programmatically. Turns out it is just 20 lines of python code, with the power of gnu/aspell and some shell commands.

Here is the script that tries to find meaningful domains that has 3-7 length & ends with .ly

    import shlex
    from subprocess import Popen, PIPE

    extension = "ly"

    egrep_regex = "egrep '^\w{3,5}" + extension + "$'"
    aspell_command = shlex.split("aspell -l en dump master")
    egrep_command = shlex.split(egrep_regex)

    p1 = Popen(aspell_command, stdout=PIPE)
    p2 = Popen(egrep_command, stdin=p1.stdout, stdout=PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]

    for domain in output.split("\n"):
        domain = domain.replace(extension, "." + extension)
        p3 = Popen(["whois", domain], stdout=PIPE)

        if "not found" in str(p3.communicate()[0]).lower():
            print "the domain " + domain + " seems available"

This code will print over hundreds of possible domains that actually has a meaning in the dictionary. At first sight, I can see the available domains like awful.ly or evil.ly

You can force aspell to use another language if you want. Just pass appropriate language prefix after -l parameter.

It is also possible that, there might be registered domains which returns not found to whois requests. But I couldn't find a better way to check if a domain is registered. Please leave me a comment if you have better idea!

- - -

as Pritam Baral commented, the shell version is way simpler.

    for domain in $(aspell -l en dump master | egrep '^\w{3,5}ly$')
    do
        domain=$(echo $domain | head -c-3).ly
        if whois $domain &>/dev/null
        then
            echo "the domain $domain seems available"
        fi
    done

