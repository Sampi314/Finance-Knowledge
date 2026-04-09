# Sorry, I screwed it up... » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/sorry-i-screwed-it-up

---

Sorry, I screwed it up…
=======================

[blogging](https://chandoo.org/wp/category/blogging/)
 - 8 comments

  

Over the weekend I tried to move this site (chandoo.org) from one hosting provider to another. Whenever I do this, I dont feel so good and yesterday was no exception.

**The move failed**

Soon after changing the DNS Server settings to point to new host, I was getting HTTP 500 error. A closer look at error logs and I found a message “premature end of headers in index.php” which could mean several things according to mighty internet.

Well, I couldnt do much about this, so I silently changed back my DNS to old provider. I will look in to this issue again this weekend. So meanwhile if you see something funny on the blog hosting front, just hang in there and be with me. I am sorry if you are frustrated seeing a useless http error but beleive me, I am even more frustrated seeing the same errors.

![Chandoo](https://chandoo.org/wp/wp-content/uploads/2018/05/chandoo-profile-pic.png)

**Hello Awesome...**

My name is Chandoo. Thanks for dropping by. My mission is to make you awesome in Excel & your work. I live in Wellington, New Zealand. When I am not F9ing my formulas, I cycle, cook or play lego with my kids. Know more [about me](https://chandoo.org/wp/about/)
.

I hope you enjoyed this article. Visit [Excel for Beginner](https://chandoo.org/wp/excel-basics/)
 or [Advanced Excel](https://chandoo.org/wp/advanced-excel-skills/)
 pages to learn more or join my [online video class to master Excel](https://chandoo.org/wp/excel-school-program/)
.

Thank you and see you around.

### Related articles:

|     |     |
| --- | --- |
| Written by Chandoo  <br>Tags: [blogging](https://chandoo.org/wp/tag/blogging/)<br>, [http 500 error](https://chandoo.org/wp/tag/http-500-error/)<br>, [wordpress](https://chandoo.org/wp/tag/wordpress/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 8 Responses to “Sorry, I screwed it up…”

1.  ![](https://secure.gravatar.com/avatar/42a31893acf45c0ad0784e8f4c82d4f1299aa62c5173714238cdec5e95c43655?s=64&d=mm&r=g) teylyn says:
    
    [January 19, 2009 at 3:59 am](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-34763)
    
    Hang in there, Chandoo. There are a lot of us who will hunt you down, wherever you host. Just too good a blog to miss!
    
    [Reply](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-34763)
    
2.  ![](https://secure.gravatar.com/avatar/caa03efaaee981ef101f8fd05b8015f33953867ac9609577d3f2fa31efe490bb?s=64&d=mm&r=g) [Jon Peltier](http://peltiertech.com/WordPress/)
     says:
    
    [January 19, 2009 at 4:22 am](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-34768)
    
    This is a frustrating process. I did it last April, and may have to again this spring. There are so many ways to get it wrong, and only one way to get it right. And all of the guides online differ in their protocols.
    
    Good luck.
    
    [Reply](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-34768)
    
3.  ![](https://secure.gravatar.com/avatar/3a16b963356b781afa2aa9b1cceae35e30f4f1d90c0e0292811ccd5f805aee35?s=64&d=mm&r=g) [Tarun](http://www.techbanyan.com/)
     says:
    
    [January 23, 2009 at 12:28 pm](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-35642)
    
    2-3 days back I changed my host from 1and1 to Media Temple.
    
    Flawless migration.
    
    1\. Using WinSCP, copy all your files & directories to the local computer first, and then to the new host.
    
    2\. Use MyPhPAdmin to take a dump of the db, and then import it using the MyPhPAdmin on the new host.
    
    3\. Update the DNS on the old host to point to the new host.
    
    Did you edit your index.php file?
    
    [Reply](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-35642)
    
4.  ![](https://secure.gravatar.com/avatar/3a16b963356b781afa2aa9b1cceae35e30f4f1d90c0e0292811ccd5f805aee35?s=64&d=mm&r=g) [Tarun](http://www.techbanyan.com/)
     says:
    
    [January 23, 2009 at 12:30 pm](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-35644)
    
    Why did your index.php fail.  
    .  
    Which host are you migrating to and from where.
    
    [Reply](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-35644)
    
5.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [January 23, 2009 at 12:46 pm](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-35651)
    
    @Tarun: I did the same steps...
    
    but since my current host doesnt allow winSCP or SFTP, I used FTP (took several hours 🙁 ) to download the current installation's theme, plugin and upload folders
    
    unzipped a fresh install of wordpress from wordpress.org to my new hosting account
    
    replaced the theme, plugin and upload folders
    
    updated DB through SSH (phpmyadmin cant be accessed until I change my nameservers, thus, I used mysqld)
    
    and finally updated name servers.
    
    I was able to view static files (like [http://chandoo.org/](http://chandoo.org/)
    ) and images... but not the index page.
    
    the current host is godaddy and I tried to migrate to dreamhost.
    
    [Reply](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-35651)
    
6.  ![](https://secure.gravatar.com/avatar/3a16b963356b781afa2aa9b1cceae35e30f4f1d90c0e0292811ccd5f805aee35?s=64&d=mm&r=g) [Tarun](http://www.techbanyan.com/)
     says:
    
    [January 24, 2009 at 12:00 am](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-35717)
    
    Potential error step 1.  
    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
    Chandoo - unzipped a fresh install of wordpress from wordpress.org to my new hosting account  
    \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    
    Potential error step 2.  
    \_\_\_\_\_\_\_\_  
    updated DB through SSH (phpmyadmin cant be accessed until I change my nameservers, thus, I used mysqld)  
    \_\_\_\_\_\_\_\_
    
    You should not install a fresh WordPress during migration. Just copy over exact same files from your old host to new host.
    
    What do you mean - current host does not allowWinSCP - but you used FTP?
    
    WinSCP IS a GUI FTP!
    
    PhpAdmin cannot be access until you change the nameservers? I would find that extremely hard to believe! Where you getting you info from!
    
    You don't have to edit your index.php ...that was my point in the last post. Why did you do that!
    
    Lastly, Dreamhost Vs Mediatemple grid service. Compare these two and if you are within 30 days of the purchase, reconsider the decision to go with Dreamhost and shift to Mediatemple.
    
    Unless of course you are going with Dedicated servers or something similar.
    
    [Reply](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-35717)
    
7.  ![](https://secure.gravatar.com/avatar/3a16b963356b781afa2aa9b1cceae35e30f4f1d90c0e0292811ccd5f805aee35?s=64&d=mm&r=g) [Tarun](http://www.techbanyan.com/)
     says:
    
    [January 24, 2009 at 12:02 am](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-35718)
    
    Hey I noticed too many exclamation marks...I was not really jumping around writing that post 😀
    
    [Reply](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-35718)
    
8.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [January 24, 2009 at 2:16 am](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-35734)
    
    @Tarun: Awesome.. I kind of guessed that step 1 "unzip fresh install" was the problem.
    
    I did have the winSCP FTP client. But when you create a new connection, it asks for preferred protocol and the options are FTP, SFTP and SCP. I meant my current host doesnt allow anything other than FTP.
    
    The reason I used fresh install is, download rates from FTP to my comp were bad due to my slow internet connection. I thought I could avoid some extra download by getting a zipped file from wordpress.org.
    
    And wrt. mysql, dreamhost gives a mysql subdomain through which you can access phpmyadmin. that is why nameserver change is required.
    
    I never really edited the index.php. But after few hours and still the same error, I have opened it and added a headers section (that seems to be one cause for this according to few articles on the net).
    
    Thank you so much for answering my questions. You are really helpful 🙂
    
    btw, I am moving this site to the basic package on dreamhost. I doubt if moving to a Grid Hosting or Dedicated is required for a small site like mine. It gets around 5k page views a day and the template isnt particularly mysql hungry either.
    
    [Reply](https://chandoo.org/wp/sorry-i-screwed-it-up/#comment-35734)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/sorry-i-screwed-it-up/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Why No One Likes Your Pie Charts (And What to Do About It)](https://chandoo.org/wp/excel-pie-chart/) | [Visualizing Search Terms on Travel Sites – Excel Dashboard](https://chandoo.org/wp/excel-bubble-chart/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)