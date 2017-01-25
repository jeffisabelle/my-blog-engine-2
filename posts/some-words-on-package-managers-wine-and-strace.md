Hello, this blog post belongs to my operating systems course as homework 2. You can have a look at earlier posts for the course from the links below.

The Real Usage Statistics of Linux
Kernel Based Virtual Machines

This homework has 3 questions, I'll answer them with given order. Here is the questions;

* (q1) rhel 6 is running on a server which has ibm power 7 processor. if i take xeyes application from there, and move it to the my virtual rhel 6 instillation on my pc, would it be run? Explain briefly.
* (q2) how can we run notepad++ on rhel 6 that we installed to the vm. take a video for it and upload it to youtube. (well, no, i don't like videos)
* (q3) Write a `hello world` program with c. Run strace utility on it and paraphrase the system calls.

### a1) ISA is important ###
I've never worked with IBM Power 7 processors, but a quick look-up to this wikipedia article showed that it has a microarchitecture called Power ISA v.2.06. We can guess that it is probably not compatible with our x86 architecture processors.

But, can it be run? yes, if virtual machine utility creators (vbox, vmware) supports an emulated power 7 processors on their program, that should work just fine. But, it's not there today. (I'm talking from virtual box side, I have 0 idea what vmware supports in terms of hardware emulation)

### a2) Wine installation on Cent-OS ###
We talked about that linux is free and it has a lot of variants on the lecture. RedHat is a linux distribution which is mainly focuses on server platforms. There are some variants of redhat enterprise linux such as centos (which we installed to our machines) and fedora (which is more focused on desktop users). I want to give you some information on installing packages on these systems so you can get what's going on more easily.

Now, if we want to install wine on our system, we can just download the source code, and compile it, but this can get a bit complex. For that reason, linux distributions created some package installer for their system. Since CentOS and Fedora are RedHat forks, we can use RPM (RedHat Package Manager) to install software.

However this is not as easy as you might think. Why? Because RPM do not help you to install dependencies automatically. This has advantages and disadvantages. The disadvantage is, well you have to install every dependency by hand, furthermore, the dependent libraries may be dependent to another libraries and so on.

If you think about it, it's quite overwhelming. What can be the advantage then? Well, you might be running a server, and you don't want to install something automatically that you're not aware. E.g. you may be installing some sort of application but you are not aware that it is dependent on Java, if it was automatically installs java on your server, you can get in serious troubles. (According to recent reports, java is the most vulnerable software out there: Kaspersky Top 10 Vulnerability List )

But, what if you're not running a server, and you just want to install something on your computer. (like our wine installation) Well, there is a solution for that, which is called YUM. YUM is more intelligent package manager then RPM, it search your query on its database, and installs it with dependencies. So we just need to update yum database to insert wine specific packages to there, and install it using yum easily.

#### Step 1: Update your current software. ####
(this is not needed but recommended before installing new software)
($ means a new line of code to the linux terminal screen)

    $ yum upgrade


#### Step 2: Insert EPEL to your yum database to install wine. ####

    $ su
    $ wget http://dl.fedoraproject.org/pub/epel/5/x86_64/epel-release-5-4.noarch.rpm
    $ wget http://rpms.famillecollet.com/enterprise/remi-release-5.rpm
    $ rpm -Uvh remi-release-5*.rpm epel-release-5*.rpm

We first used su (switch user) command to be root user. You will need to be root to install new software. Then we have run every line one by one. (wget is used to download something from the web and we used rpm to install epel)

You should verify that the following output is similar in your machine.

    $ ls -l /etc/yum.repos.d/
    total 28
    -rw-r--r--. 1 root root 1926 Feb 25 10:57 CentOS-Base.repo
    -rw-r--r--. 1 root root  638 Feb 25 10:57 CentOS-Debuginfo.repo
    -rw-r--r--. 1 root root  630 Feb 25 10:57 CentOS-Media.repo
    -rw-r--r--. 1 root root 3664 Feb 25 10:57 CentOS-Vault.repo
    -rw-r--r--. 1 root root  957 Nov  5  2012 epel.repo
    -rw-r--r--. 1 root root 1056 Nov  5  2012 epel-testing.repo
    -rw-r--r--. 1 root root 1020 Feb 12 20:50 remi.repo


#### Step 3: Enable REMI before installing wine ####

Type the following command to the terminal. Gedit is a text editor for linux machines. Find the line that states enabled=0, you should change it to enabled=1 and save it.



$ gedit /etc/yum.repos.d/remi.repo


#### Step 4: Install wine with yum ####

Type the codes below one by one again. The first line will install wine the second line will configure it. You should be able to run many .exe files from your linux distro by right clicking on it and choosing run with wine option.

    $ yum install wine
    $ winecfg

#### Step 5: Install notepad++ ####

You can type the following code to the terminal to install notepad++ from its website or you can go to notepad++ website and downloading the installer from there.

    $ wget http://download.tuxfamily.org/notepadplus/6.3.3/npp.6.3.3.Installer.exe


note; I was planning to take screenshots but the post itself get quite long. So I'm skipping that as well.

### a3) Strace Utility ###
There is nothing fancy here and I don't have intention to copy/paste API calls from here:
Linux API Calls

I just wondered what would happen if I run strace from virtual machine and from native installation on the same code. (Since vm uses emulated processor and memory) I noticed that VM based output contains few lines more than the native one. (it has some more MMAP calls) But that can be about the compiler versions, so I'm not sure whats going on there.
