This blog post belongs to my Operating Systems course and it will be about the memory management on operating systems and ram optimizers.

The homework consists of a one question. Which is about memory management. The question is;

Your manager tells you that there are some software which claims that they optimize the memory. On the other hand, there are many people says that this is a hooey and it actually decrease the performance of the system. Make a research, and briefly explain me which is correct.

I've done some google search and I guess I did end up with a correct answer. Here is the things about RAM optimizers and if they do a good job or not.

### My Response to the Manager ###
Okay, I've looked at several memory optimizer. And the thing is, well, they increase the available memory. But, what does it mean to be available? Is it a good thing? How they increase the available memory?

Available memory means, any program that are not yet in the memory can be moved to the memory when the program desire. So, it seems like increasing available memory is a good thing, right? NO.

The problem is not about the available memory but how these optimizer thing increase it. They actually remove cache from memory to increase the available memory. But, hey, don't we know that caching is the one of the most beatiful thing on computer science. We use caching on almost every piece of software (web caches, database systems etc.) and hardware memory caches. (l1, l2 etc.)

Operating Systems do cache memory accesses for a reason. (a good one) and should never ever removed from the memory if there is still available memory. These optimizers actually do a very, very bad for good performance. They want to use a lot of memory and operating system gives them what they want by removing the caches, after that they release the allocated memory, therefor we see an increase on available memory. But, we lost any cache stored in the memory for nothing.

I have found a video which explains this issue with an example optimizer from here; (Title: RAM Tweaker) http://www.letmebreakitdown.com/Tut_vid/Tut_vid.aspx

It was not working on the browser itself, (I use the most recent firefox) so I've downloaded it and uploaded it to youtube for easy access.