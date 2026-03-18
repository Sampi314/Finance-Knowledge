# Power Query: Blog List – Part 6

**Source:** https://sumproduct.com/blog/power-query-blog-list-part-6/

---

[Home](https://sumproduct.com/)

\> Power Query: Blog List – Part 6

*   January 2, 2024

Power Query: Blog List – Part 6
===============================

Power Query: Blog List – Part 6
===============================

3 January 2024

_Welcome to our Power Query blog. I would like to get a list of all the Power Query blogs I have posted. Today, I welcome some new functionality, currently in Preview, which will allow me to achieve my goal in Power Query in Excel._

**Please Note**: This series of blogs was written using an old platform for the SumProduct website and the links referred to in this example have now changed.  Also, the **M** functions used to manipulate web data are now Generally Available in Excel.

I started writing this blog series back in 2016:

![](<Base64-Image-Removed>)

There have been many developments since then, some of which I have reported upon. Since I am going to revisit more of the areas that have been improved, I am going to start with a reminder of what we have covered so far. In order to do this, I used Power Query in Power BI, since there are some functions that will help me to access web data, which were not yet recognised in Power Query in Excel. However, this is changing, as I will show shortly.

In [Part 1](https://sumproduct.com/blog/power-query-blog-list-part-1/)
, I noted that to get a full list, I am going to need several pages:

![](<Base64-Image-Removed>)

I extracted and tidied up the data for the first page:

![](<Base64-Image-Removed>)

In [Part 2](https://sumproduct.com/blog/power-query-blog-list-part-2/)
, I changed the Source step of my query to accept a parameter **P\_PageNumber,** which allowed me to get the data from a specific page. I used the following **M** code:

**\=  
Web.BrowserContents(“https://www.sumproduct.com/blog/power-query-blogs?page=”&Number.ToText(P\_PageNumber))**

I checked that this still gave the same results for the query.

![](<Base64-Image-Removed>)

In [Part 3](https://sumproduct.com/blog/power-query-blog-list-part-3/)
, I converted this query into a function, and generated a list of page numbers to concatenate my data.

![](<Base64-Image-Removed>)

In [Part 4](https://sumproduct.com/blog/power-query-blog-list-part-4/)
, I finished the query by extracting the last page number from the data and using it as a parameter **P\_LastPage** when generating the list.

![](<Base64-Image-Removed>)

The list was then generated, and could be refreshed, no matter how many pages exist.

![](<Base64-Image-Removed>)

[Last week](https://sumproduct.com/blog/power-query-blog-list-part-5/)
, I looked at why I couldn’t do this in Power Query in Excel. However, having completed my series on ‘Blog List’, I was delighted to find that the first blog series that I can update is this one, as there are some changes which are currently in Preview in Excel.

Today, I am running a Beta version:

![](<Base64-Image-Removed>)

I use the web icon in the ‘Get & Transform Data’ section of the Data tab, and I enter the same **URL** that I used in [Part 2](https://sumproduct.com/blog/power-query-blog-list-part-2/)
 to get the first page of blogs.

![](<Base64-Image-Removed>)

When I click OK, I can see that the Navigator dialog has been improved, and now resembles the same dialog in Power BI, which I looked at in detail in [Part 1](https://sumproduct.com/blog/power-query-blog-list-part-1/)
:

![](<Base64-Image-Removed>)

I select **Table 1** from the ‘Suggested Tables’ and transform the data:

![](<Base64-Image-Removed>)

If I look at the Source step, I can see that the function **Web.BrowserContents()** is now recognised.

![](<Base64-Image-Removed>)

Similarly, if I look at the ‘Extracted Table From Html’ step, I can see that the function **Html.Table()** is also recognised.

![](<Base64-Image-Removed>)

These were the functions that I noted were missing last week in the Generally Available version of Power Query in Excel.

This means that the process I described in the ‘Blog List’ series of blogs can be performed in Power Query in Excel in the Beta version, and it will soon be Generally Available. This is very good news when it comes to extracting data from the Web!

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-blog-list-part-6/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-blog-list-part-6/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-blog-list-part-6/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-blog-list-part-6/#0)

[](https://sumproduct.com/blog/power-query-blog-list-part-6/#0 "close")

top