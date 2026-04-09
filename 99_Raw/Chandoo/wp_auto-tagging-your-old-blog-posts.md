# Automatically tagging your old wordpress posts

**Source:** https://chandoo.org/wp/auto-tagging-your-old-blog-posts

---

Auto tagging your old blog posts
================================

[Analytics](https://chandoo.org/wp/category/analytics/)
 , [blogging](https://chandoo.org/wp/category/blogging/)
 , [hacks](https://chandoo.org/wp/category/hacks/)
 , [ideas](https://chandoo.org/wp/category/ideas/)
 , [technology](https://chandoo.org/wp/category/computer/)
 - 16 comments

  

As you all may know I have recently [moved my blog from blogger to wordpress](http://chandoo.org/wp/2007/12/23/moved-to-wordpress-from-blogger/)
. Since I have started blogging way back in 2004 most of my posts were untagged. I have used blogger labels ever since they were introduced, still almost 400 of my posts were untagged. I had two options,

*   Manually edit posts and tag / categorize them
*   Auto tag posts through some plug-in and then fine tune the post tags over the next few months

I have chosen the 2nd option and promptly installed [Simple Tags plugin](http://www.herewithme.fr/wordpress-plugins/simple-tags)
. **Even though simple tags had the capability to automatically tag all your posts you still have to provide the list of the tags to use.** I could create the list by typing out all things that I think I have been blogging about (for eg. IIM, CAT, Indore, software, excel, data, business, advertising, IRIS, Utsaha, marketing etc.), but over the years I have actually blogged about whole lot of things that thinking them itself would take a lot of time and I could always miss some of the tags. So I wanted to analyze my posts (400+ of them) to generate the tags.

*   My first job is to somehow convert the blogposts in to plain text so that its easy to analyze. So I exported the entire blog using WP’s incredible xml export option \[Go to wordpress blog dashboard > manage > export and select the author for whom you want to export the posts\]. Then I opened it in notepad++ to see the file structure. As you can see it below the post contents are included in the `content:encoded` tags.![Wordpress XML export file structure](https://phd.blog.googlepages.com/wordpress_xml_export_structure.jpg)
*   Then I wrote a small java program to extract all the post contents and analyzed the word counts. The logic for this is simple,`    1. Find the first "content :encoded" tag   2. while the next word is not "/content:encoded"   3. increase that word frequency by 1   4. get next word   5. get next "content :encoded" tag   6. send the output in the form of word: frequency to a txt file    `
*   Once I had the words and their frequencies in a text file I used my favorite tool, thats right, excel and sorted the list in descending order of the frequency. There were 25000 + unique words in my blog posts. But the list needed a bit of cleaning since I have used StringTokenizer to parse words it returned words like “<a “, “@something” “hello.” “because,” After cleaning and removing all the unnecessary symbols and special characters I was left with atleast 23000 words and their frequencies.
*   I neglected all the words with more than 175 as frequency (just a random number I used) or less than 15 as frequency.  
    ![blog posts word frequencies](https://phd.blog.googlepages.com/blog_word_frequencies.gif)
*   I took the left over list and manually scanned it to find out the unique words. This way I could knockoff most of the synonyms (like advertising and ads, marketing and selling, b-school and bschool etc.).
*   After all this I had a list of about 100 words. Then I edited the words to bring out clarity and pasted them in Simple Tags plug-in page. Then I ran the auto-tag feature and all my posts were tagged.

Now most of my previous posts are tagged, hence I could automatically locate the related posts when I write something.

**Well, incase you have migrated your blog from blogger to wordpress and trying to tag your posts please drop a comment here, I can send you my java program which can generate the word frequency based on the xml format.** You can then analyze it and findout the tags for your posts.  
The program is no longer in a reusable position (I have edited it so much that it is pretty much useless for everyone except me). If you are trying to write it, follow the above logic and you should be able to do this. Good luck.

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
| Written by Chandoo  <br>Tags: [blogging](https://chandoo.org/wp/tag/blogging/)<br>, [guide](https://chandoo.org/wp/tag/guide/)<br>, [how to](https://chandoo.org/wp/tag/how-to/)<br>, [idea](https://chandoo.org/wp/tag/idea/)<br>, [information](https://chandoo.org/wp/tag/information/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 16 Responses to “Auto tagging your old blog posts”

1.  [How to redirect traffic / visitors / searches from old blogger pages to new wordpress posts | Pointy Haired Dilbert - Chandoo.org](http://chandoo.org/wp/2008/01/11/how-i-redirect-traffic-from-blogger-pages-to-wordpress-posts/)
     says:
    
    [January 11, 2008 at 4:55 am](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-3344)
    
    \[...\] my first challenge was to organize the posts for better discovery and search. I have done that by automatically generating tags and tagging posts using a bit of analysis and a bit of \[...\]
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-3344)
    
2.  ![](https://secure.gravatar.com/avatar/a7c7dddb8cd45e728081fd1179c141c8c7b82adebc340dd0ef0f85595af8db60?s=64&d=mm&r=g) [Online Shopping Network](http://www.shop-network.org/)
     says:
    
    [March 22, 2008 at 6:05 am](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-4347)
    
    I would love to have a copy of your Java program. Would you mind posting it for download?
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-4347)
    
3.  ![](https://secure.gravatar.com/avatar/2f2d4673633f6be2e015d82865a02b5028a944a47f2794d9654ee4729f3f5cc0?s=64&d=mm&r=g) [Ram](http://www.findnearyou.com/)
     says:
    
    [March 28, 2008 at 7:37 am](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-4475)
    
    Hi chandoo
    
    great post. lemme try it. we at [http://www.findnearyou.com](http://www.findnearyou.com/)
    , have tons of content and are looking at some neat way to autotag all of them.
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-4475)
    
4.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/)
     says:
    
    [March 28, 2008 at 6:36 pm](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-4495)
    
    @Ram - thanks for the comments  
    @Online Sho... - Will send you the program in email
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-4495)
    
5.  ![](https://secure.gravatar.com/avatar/ec84b51e3444f485c287c2a44982dd55a82218d6db03f5df7555abf5b1366693?s=64&d=mm&r=g) [Ajay](http://readerszone.com/)
     says:
    
    [April 10, 2008 at 5:32 am](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-4999)
    
    gr8 post  
    never know before this  
    thanks
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-4999)
    
6.  ![](https://secure.gravatar.com/avatar/8f9e81e05bd4f362960684616bef3e03eb655cb8e79ab963c8f5aafe0a9fe5ed?s=64&d=mm&r=g) [Agel](http://www.buildingdynamicfutures.com/)
     says:
    
    [May 22, 2008 at 6:28 am](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-9408)
    
    I really thankful to you for posting this article and I never know about this.
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-9408)
    
7.  ![](https://secure.gravatar.com/avatar/2e8d3131340143ca64d718546265e6d5230512904d6a3ba62ddad1124b13b696?s=64&d=mm&r=g) [sunish](http://sunishrocks.com/)
     says:
    
    [June 17, 2008 at 5:30 pm](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-12005)
    
    I recently moved from blogger to wordpress.
    
    Did some manual tagging for old posts.
    
    Can you send me the java program?
    
    Regards  
    S
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-12005)
    
8.  ![](https://secure.gravatar.com/avatar/0e3cf2576646118cccd6710dac7519ba8ff40d9164240cdda2e1ec06a8a29969?s=64&d=mm&r=g) MinPin says:
    
    [August 19, 2008 at 4:02 pm](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-19014)
    
    This looks really helpful. I'd love to get your program too!
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-19014)
    
9.  ![](https://secure.gravatar.com/avatar/08fcaf7ecc8a391a3363fe519aecfa067b521357a8049b19631fde14be901008?s=64&d=mm&r=g) [JonnieCrunch](http://www.crunchymunchkin.com/)
     says:
    
    [December 21, 2008 at 12:19 am](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-31711)
    
    Hey, this looks really helpful.. can you please send me the java app?
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-31711)
    
10.  ![](https://secure.gravatar.com/avatar/052b08f8597395473d55d253a6eb9b3beb193244cf20eb7dc404c17429fb094f?s=64&d=mm&r=g) [Albert](http://www.albertwavering.com/)
     says:
    
    [February 6, 2009 at 4:08 am](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-39224)
    
    Hi P.H.D. - could you possibly send me a copy of that java app? That would rock. Thanks.
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-39224)
    
11.  ![](https://secure.gravatar.com/avatar/6538af76b343d550eda2c7bc03ea07d467b055bdf5862f90fdc2f36bfca1d2a4?s=64&d=mm&r=g) [Shawn](http://www.inet-investigation.com/)
     says:
    
    [May 21, 2009 at 8:33 pm](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-63343)
    
    Hey, great idea. I'm in the same situation and was wondering if I could get a copy of your java program?
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-63343)
    
12.  ![](https://secure.gravatar.com/avatar/68aa9f8e574d402b781ef4ba2bd5418b2d31b71ab163012fcaf7b0c8dab9f913?s=64&d=mm&r=g) [Rebecca](http://fridaythang.com/blog)
     says:
    
    [May 30, 2009 at 5:01 am](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-64340)
    
    Hate to add a 'me to!' post, but I'd also love a copy of the program. Thanks!
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-64340)
    
13.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [June 1, 2009 at 12:40 pm](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-64649)
    
    @all.. I am sorry to say this, but the program is no longer in a reusable condition. But it is a fairly simple program, you can follow the logic mentioned in the post to recreate it yourself.
    
    all the best. 🙂
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-64649)
    
14.  [What is the most unusual thing you have used Excel for? \[Quick Poll\] | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2010/08/13/unusual-excel-uses/)
     says:
    
    [August 13, 2010 at 9:11 am](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-121693)
    
    \[...\] have used excel to generate and clean a list of tags for this \[...\]
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-121693)
    
15.  ![](https://secure.gravatar.com/avatar/cf9092fb5ccaa6789400608e486cbcf69550647be4f3dfa526cc8796bd11a2c6?s=64&d=mm&r=g) [Athif](http://twitter.com/Athif)
     says:
    
    [August 16, 2010 at 10:52 am](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-122236)
    
    Hi Chandoo,  
    Athif here. BTW, which wordpress related posts plugin do you use?
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-122236)
    
16.  ![](https://secure.gravatar.com/avatar/df882a1aea8fae4390910f30438e4bae875ee9a8d2d48902451fea9f30d0bd35?s=64&d=mm&r=g) [la tahzen](https://islamguzelahlaktir.blogspot.com/)
     says:
    
    [August 31, 2016 at 9:23 pm](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-1270319)
    
    thank you
    
    [Reply](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#comment-1270319)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/auto-tagging-your-old-blog-posts/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Normal is Boring : Having fun in whatever you do](https://chandoo.org/wp/normal-is-boring-having-fun-in-whatever-you-do/) | [Tales of riding an auto in Chennai](https://chandoo.org/wp/tales-of-riding-an-auto-in-chennai/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)