This is my second blog post for the operating systems course. This will be a reflection paper for the Kernel Based Virtual Machine paper as homework one.

I'll structure this blog post by starting with a quick introduction, then I'll write what I knew about virtualization before reading the paper and after reading the paper. I guess that approach will reflect the paper quite well.

By the way, I'll be using diagrams ( a lot of ) for this post, and I'm drawing them on an online diagram creator. If someone found them interesting, I'm using gliffy.com as my diagram creator. It has a lot of features; from drawing ER diagrams to UML diagrams, uploading your own images to working on some diagrams collaboratively. It's free.

### Introduction ###
The paper we studied present the idea behind the KVM. (Kernel Based Virtual Machine) It starts with a quick overview of the earlier methodologies (Binary Translation, Paravirtualization & Hardware Assisted Virtualization).

Then, the papers shows the advantages and disadvantages of these methods very technically just before presenting KVM.

### Before Reading The Paper ###
As an end user, I was aware of the virtual machines for 3 to 4 years. I was using it when I need to work with Windows machines. (E.g. 2 semester ago when we were using emu8086 for microprocessors course.)

But, I had no real knowledge that how important virtualization for business. When I was doing my internship at Labris Tech, we were using a lot of VM's to easily test our systems & to easily take snapshots so if we got a problem on a newly worked code, it was easier to return to last working version before losing too much data.

So, the only methodology I'm aware of was this structure.

![VM01](https://muhammetcan.net/dosya/img/vmpost/vm01.png)

I have never thought that VM's are so powerful for production environment too.

Lately, I knew that VM's are used by VPS providers, however I never understood how they handle performance issues that VM's have. This article (and of course, couple of lectures we had last week) helped me to understand what's going on deeply.

### After Reading the Paper ###
Okay, I can say that I'm shocked when I learned how virtual machines actually works. I have always thought that they're working like usual applications and I presumed that there need to be Host OS to run a VM.

Before reading the paper, I didn't know that there are some cpu instructions that you can't use as a programmer. I knew that there are instructions you can't make but I always thought that OS is intercepting the instructions and reject the instructions that are not allowed for the programmer.

After reading the paper, I learned that CPU, itself has different level of privileges for those dangerous instructions. So, this is hardware controlled issue. CPU gives full power of it to operating systems, however normal programs on the operating systems are running with limited permissions.

This is the one of the biggest problem for the virtual machines as described by the paper. If you want to run an operating system, it needs to control the cpu without permissions. However this is not possible because VM's are ordinary programs.

To solve this issue, earlier researchers decided to run VM's on emulated hardware which talks to another layer ( hypervisor ), and the hypervisor itself runs with full privileges. In this way, VM's are able to make every cpu call to the emulated hardware, and hypervisor will handle those calls to use physical hardware. The structure will look like this after this operation.

![VM02](https://muhammetcan.net/dosya/img/vmpost/vm02.png)

If you look at the structure, it solves privilege problem gently, but if you look at deeper and think about it, it comes with a price. Hypervisor handles too much work, it needs to manage the physical cpu calls, physical memory management, physical IO devices and so on.

This is too much work for a middle layer and it will result as a poor performance. (Though as paper stated, Xen-Hypervisors and VMware created different solutions for the performance issues but it is still lacking of full performance of the physical cpu)

This is where KVM jumps in. KVM is a linux kernel module, it is working just like hypervisor layer but it is way small since it is a part of the linux kernel, KVM module doesn't need to worry about the IO scheduling or Memory Management. Those are the jobs that linux kernel already handling for years. So, the structure of the KVM based virtualization will look like this.

![VM03](https://muhammetcan.net/dosya/img/vmpost/vm03.png)

Technical details lays on the paper, but as a summary, VM's are working just like the other linux processes and KVM handles privilege issues.

### Conclusion ###
The paper changed my point of view of the virtual machines. It seems to be an interesting area where too much research going on, I'm glad to have a deeper understanding of how VM's works.

### What's Next? ###
Scribd has bunch of KVM and virtualization documents. The next thing would be studying them. I expect to find some time to study them next.

Documents About KVM
Documents About Virtualization
