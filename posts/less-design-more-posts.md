Last day, I redesigned my blog nth time. (where n > 5) It feels so bad that I redesign my blog more than actually writing to my blog. Generally, I do it because it's so much fun, no-one is in front of you, no clients, no boss, no partners. You do it as you wish & you do it for yourself.

## What's Changed? ##
I have changed many things for the blog. In fact, the remaining parts are just the posts. I had several reasons for the change, here are the things that bother me most.

* My older django code was too complex, (it is converted from wordpress)
* It had millions of unnecessary data, (again, probably because of wordpress)
* My old system was not extensible enough.
* Deployment stack seemed quite overwhelming
* Typography

You can find my old blog source code at github. For now, lets look at the details over my concerns stated above.

### 1 - Hail for the Micro-Frameworks! ###
I've been working with flask over a year now, I've worked on several projects with flask. It is just awesome. I remember my early days of running django. It was frustrating experience for me a few years ago.

I remember having trouble many of the things. Even getting static files right. Bunch of middlewares I had no idea why they are there for. Weird dilemmas of class based views and function based views. I'm pretty sure it got better today, all in all we shouldn't judge the technology for the experience we had years ago.

The reward was just being able to write python and automated admin interface. Well, I can get that with flask too. Looking at my current flask server, it is 55 lines of total code. the settings file with django alone was 176 lines. Line count doesn't mean a lot. But simplicity is always important when you read back your code after some time.

### 2 - Some Changes on Server Stack ###
I used uwsgi over nginx on my old system. My datastore was postgresql. I have changed both. Now it runs with gunicorn, and supervisor controls it. I remember having hard times runnig / controlling uWSGI server. Gunicorn documentation seemed more intuitive. (god, I like that sphinx theme!) Following articles helped me a lot while running my server.

* [How to Run Flask Applications with Nginx Using Gunicorn](http://www.onurguzel.com/how-to-run-flask-applications-with-nginx-using-gunicorn/)
* [Managing Gunicorn Processes With Supervisor](http://www.onurguzel.com/managing-gunicorn-processes-with-supervisor/)

Many people will argue that uWSGI is superior/faster and more customizable. Well, this is not new-york-times. I want the server stack to be as much as transparent to me. Gunicorn is. uWSGI isn't.

### 3 - Typography ###
For the front-end, I wanted another design because the older version had an ugly typography and I never love the feeling of writing there. I used typecast this time, and hopefully it is a little bit better (readable) now. I find typography really interesting and one of the most difficult piece of front-end development. I suggest you to check that out if you have problems with typography as I do.

## What's Next? ##
I hope to write more blog posts now. I really force myself to write more. I never like the taste of my writings and I believe writing more could let me write better essays. On the other hand, I delete my old posts and think 'how the hell i wrote this bad'. If i keep deleting posts this fast, the blog probably end up with 0-post.
