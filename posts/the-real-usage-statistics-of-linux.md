Back Story; Our Instructor, M. Selcuk Karaca force his students to write blog posts for lectures that he gave. (which is a good sign that the course will be very pragmatic) This is my first blog post for the course.

My first blog post will be about the OS Usage Statistics and Why Some OSes have success over the others that we talked about last lecture. (May 7 2013)

At lecture we saw some graphics that shows the percentages of the operating system usages. Which is collected from w3counter as our lecturer stated. This statistics shows that current Linux usage is around 2.28%

### How these stats calculated? ###
When you fire-up your web-browser and connect to a web page, you are making a http request to that web server. That request contains some information about you & your computer. Namely, it contains the operating system you use and web browser you use and so on.

W3 Counter and the other counters look at these information to figure out the market share of operating systems. So, If you are running a Microsoft OS to read this blog post, if W3Counter tracks my web page, it sees you as a Windows User and updates its database.

### But what is actually happening? ###
You are using linux! You are using a service that is running on linux. My server is running a gnu/linux distribution and when you want to connect this web page, linux is the Operating System that is responding your request.

Even If I had a .NET application that is running on Windows Server, you would be still using linux because most of the routers of your ISP, and your modem at home probably powered by linux. Forget about my tiny blog, google, facebook, twitter and most of the pages you can think of powered by linux!

However you still count as a Windows User. Because your desktop computer is running Windows and counters don't look at the bandwidth usage on the NET and just look at the requests that have been made.

Linux Foundation's How Linux is Built video can let you understand the true power & usage statistics of linux if you have some minutes.


<iframe width="560" height="315" src="https://www.youtube.com/embed/yVpbFMhOAwE" frameborder="0" allowfullscreen></iframe>


### But, what is the problem with Desktops? ###
As I saw one of the slides that we discussed in the class, that states Linux is hard to use, that leads it has the lowest market share on desktops. I just can't agree with that. Why? Because Android is linux based too, and I've never seen someone complaining that Android is hard to use.

Then what is the reason? Author of the linux kernel, Linus Torvalds explains it here, which I accept that is the real answer. There is nothing to write about more then his words.


<iframe width="560" height="315" src="https://www.youtube.com/embed/KFKxlYNfT_o" frameborder="0" allowfullscreen></iframe>


### Driver problems? Anyone? ###
Again, as we discussed in the lecture, there are some driver issues on IO devices on linux. But I guess this is as misleading as the desktop market share.

I agree that there are some issues with IO devices on linux. (Although it is getting better day by day) But the Operating System has nothing to do about it. It's all about the hardware producers that are really being dumb and doesn't care the linux community.

For example, I got an ASUS laptop which has an nvidia Graphics Card which has an optimus technology. I had very difficult times to get it working properly, and I'm pretty sure non experienced users can't get it working on linux. The following video is about this problem that I have.


<iframe width="560" height="315" src="https://www.youtube.com/embed/O0r6Pr_mdio" frameborder="0" allowfullscreen></iframe>


However this is changing, When I got my computer, nvidia driver page stated that "there is no support for linux for optimus powered chips". Last week or so, nvidia announced a new linux driver (319.19) which has support for linux. I'm pretty sure this video has forced them to do it. (of course there is a steam on linux effect too.)


So driver issues are almost going to zero. Linux have a new famous Secure Boot problem which MS forces. I love these things, because it shows the power of my operating system and how it threatens MS. :)
