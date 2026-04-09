# How to redirect traffic / visitors / searches from old blogger pages to new wordpress posts

**Source:** https://chandoo.org/wp/how-i-redirect-traffic-from-blogger-pages-to-wordpress-posts

---

How I redirect traffic from blogger pages to wordpress posts
============================================================

[blogging](https://chandoo.org/wp/category/blogging/)
 , [hacks](https://chandoo.org/wp/category/hacks/)
 , [technology](https://chandoo.org/wp/category/computer/)
 - 5 comments

  

After moving the blog from the blogger to wordpress, my first challenge was to organize the posts for better discovery and search. I have done that by [automatically generating tags and tagging posts](http://chandoo.org/wp/2008/01/07/auto-tagging-your-old-blog-posts/)
 using a bit of analysis and a bit of insanity.

The next challenge was to redirect the traffic from the old blogger posts to wordpress posts. Thanks to the beautiful wordpress search feature, my job is almost 90% done. The search is really powerful and fetches the correct posts 99% of the time. So instead of setting up either 301/401 redirects or adding complex javascript code or using some kind of mapping \[old -> new\] mechanism in PHP, all I had to do is to send the traffic from http://chandoo.org/blog/ \[archive path\] / \[post title\].html to http://chandoo.org/wp/?s=\[post title\] and wordpress would fetch and display the post for me.

So I went to my blogger template edit screen and added this piece of javascript code.

> `    window.location = "http://www.chandoo.org/wp/?s= < $BlogItemTitle$ >";    `  
> The $BlogItemTitle$ is the old blogger tag for blog post title, which I am passing as an argument to my wordpress search.

![How to redirect traffic, visitors, searches from blogger to wordpress posts](https://phd.blog.googlepages.com/redirecting_traffic_from_blogger_to_.jpg)

Since most of the people visiting the old posts on my blog are coming from search engines this method of redirecting is working perfectly for me. There are few problems though, this works only for post pages, if you have monthly / weekly archives like I do, some people may still visit the archive pages. I am thinking of adding permanent redirects or some PHP script to redirect the blogger archive requests to wordpress archives. But the traffic to those pages is small enough to neglect it for now. Once the search engines catch hold of new URLs I can permanently remove the old blog content from my website.

Feel free to comment incase you need some help in figuring out how to do this for your site.

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
| Written by Chandoo  <br>Tags: [blogging](https://chandoo.org/wp/tag/blogging/)<br>, [how to](https://chandoo.org/wp/tag/how-to/)<br>, [technology](https://chandoo.org/wp/tag/technology/)<br>, [web](https://chandoo.org/wp/tag/web/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 5 Responses to “How I redirect traffic from blogger pages to wordpress posts”

1.  [Search Engine Optimization Direct » How I redirect traffic from blogger pages to wordpress posts](http://searchengineoptimizationdirect.com/?p=21707)
     says:
    
    [January 11, 2008 at 5:51 am](https://chandoo.org/wp/how-i-redirect-traffic-from-blogger-pages-to-wordpress-posts/#comment-3345)
    
    \[...\] sneha article is brought to you using rss feeds.Here are some of the top articles on search engine optimization.Since most of the people visiting the old posts on my blog are coming from search engines this method of redirecting is working perfectly for me. There are few problems though, this works only for post pages, if you have monthly … \[...\]
    
    [Reply](https://chandoo.org/wp/how-i-redirect-traffic-from-blogger-pages-to-wordpress-posts/#comment-3345)
    
2.  ![](https://secure.gravatar.com/avatar/e7d1625851413e1d0d5b51b2b9933eb7431b41fdf4e875be8b8d5f6b627a6105?s=64&d=mm&r=g) [Kapil](http://www.kapilb.com/blog)
     says:
    
    [January 12, 2008 at 9:24 am](https://chandoo.org/wp/how-i-redirect-traffic-from-blogger-pages-to-wordpress-posts/#comment-3362)
    
    Can I do this with a blog address like kapsi.blogspot.com - and direct it to my current wordpress powered website at kapilb.com?
    
    [Reply](https://chandoo.org/wp/how-i-redirect-traffic-from-blogger-pages-to-wordpress-posts/#comment-3362)
    
3.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/)
     says:
    
    [January 12, 2008 at 6:13 pm](https://chandoo.org/wp/how-i-redirect-traffic-from-blogger-pages-to-wordpress-posts/#comment-3368)
    
    @kapil... you can do it with blogspot hosted blogs as well. I guess your blog is hosted on old blogger, if you have migrated to new blogger (which google literally forced everyone to do) then you may have to change the tag "$BlogItemTitle$" .
    
    In that case, near the blog header in "edit html" section of your blogger settings insert the below script. I havent tested, but i am guessing it should work with little or no corrections.
    
    SCRIPT
    
    < b:if cond=â€™data:blog.pageType == â€œitemâ€â€˜ >  
    < script >  
    window.location = "http://www.kapilb.com/wp/?s= < data:post.title / >  
    < / script >
    
    Oh yeah, you may have to adjust the spaces in that script, I had put spaces to ensure that comment gets published instead of being parsed.
    
    [Reply](https://chandoo.org/wp/how-i-redirect-traffic-from-blogger-pages-to-wordpress-posts/#comment-3368)
    
4.  ![](https://secure.gravatar.com/avatar/ef92bffe95964a6d0abe27536ddd73aef372f457dbdc0f08647fd2025677119c?s=64&d=mm&r=g) [ankur?](http://enagar.com/)
     says:
    
    [January 15, 2008 at 8:45 am](https://chandoo.org/wp/how-i-redirect-traffic-from-blogger-pages-to-wordpress-posts/#comment-3423)
    
    anyways people r not allowed to put adds on wordpress.com  
    so how does it matter
    
    [Reply](https://chandoo.org/wp/how-i-redirect-traffic-from-blogger-pages-to-wordpress-posts/#comment-3423)
    
5.  ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
     says:
    
    [January 15, 2008 at 3:37 pm](https://chandoo.org/wp/how-i-redirect-traffic-from-blogger-pages-to-wordpress-posts/#comment-3425)
    
    @ankur... hmm, but you may want your visitors to find your site for other purposes also... For example, in my case I want to remove the old archives once most of my readers have updated their bookmarks or when I am getting no further visits to those files.
    
    [Reply](https://chandoo.org/wp/how-i-redirect-traffic-from-blogger-pages-to-wordpress-posts/#comment-3425)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/how-i-redirect-traffic-from-blogger-pages-to-wordpress-posts/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Mera Jahan](https://chandoo.org/wp/mera-jahan/) | [Amazon’s recommendation system – is it crazy?](https://chandoo.org/wp/amazons-recommendation-system-is-it-crazy/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)