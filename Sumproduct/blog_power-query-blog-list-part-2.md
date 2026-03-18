# Power Query: Blog List – Part 2

**Source:** https://sumproduct.com/blog/power-query-blog-list-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Blog List – Part 2

*   December 5, 2023

Power Query: Blog List – Part 2
===============================

Power Query: Blog List – Part 2
===============================

6 December 2023

_Welcome to our Power Query blog. I would like to get a list of all the Power Query blogs I have posted. Today, I extend the query to extract data from all pages._

**Please Note**: This series of blogs was written using an old platform for the SumProduct website and the links referred to in this example have now changed.

I started writing this blog series way back in 2016:

![](<Base64-Image-Removed>)

There have been many developments since then, some of which I have reported upon. Since I am going to revisit more of the areas that have been improved, I am going to start with a reminder of what we have covered so far. In order to do this, I am going to use Power Query in Power BI, since there are some functions that will help me to access web data, which are not yet recognised in Power Query (Get & Transform) in Excel.

[Last week](https://sumproduct.com/blog/power-query-blog-list-part-1/)
, I noted that to get a full list, I am going to need several pages:

![](<Base64-Image-Removed>)

I extracted and tidied up the data for the first page:

![](<Base64-Image-Removed>)

Now I am happy with this page, I shall go back to the website to check out the URL for the second page:

![](<Base64-Image-Removed>)

If I compare the URL I used for the first page:

**https://www.sumproduct.com/blog/power-query-blogs**

to the URL for the second page:

**https://www.sumproduct.com/blog/power-query-blogs?page=2**

I can see I have more characters_, i.e._ “?page=2”

If I go back to the query I created [last week](https://sumproduct.com/blog/power-query-blog-list-part-1/)
, and look at the source step:

![](<Base64-Image-Removed>)

It is reasonable to assume that I could add the characters “?page=1” to this, and still get the same results. I try this:

![](<Base64-Image-Removed>)

As I expected, the results are the same. However, I want to extract all the pages, therefore, I am going to use a parameter for the page number. On the Home tab, I can create a ‘New Parameter’ from the ‘Manage Parameters’ dropdown:

![](<Base64-Image-Removed>)

I create **P\_PageNumber**:

![](<Base64-Image-Removed>)

I make this a ‘Decimal Number’ (since I do not have the option of making it a whole number) and give it an initial value of 1. If I use this parameter in the Source step of my query, I should see no change to the data extracted. Instead of the current **M** code:

**\=  
Web.BrowserContents(“https://www.sumproduct.com/blog/power-query-blogs?page=1”)**

I need to use the following code:

**\=  
Web.BrowserContents(“https://www.sumproduct.com/blog/power-query-blogs?page=”&Number.ToText(P\_PageNumber))**

I need to use the function **Number.ToText()** for **P\_PageNumber**, because the file location string is a character datatype, and **P\_PageNumber** is a number. As before, I can test that this works by checking that the results are the same:

![](<Base64-Image-Removed>)

Next time, I will convert this query into a function and generate a list of page numbers to concatenate my data.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-blog-list-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-blog-list-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-blog-list-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-blog-list-part-2/#0)

[](https://sumproduct.com/blog/power-query-blog-list-part-2/#0 "close")

top