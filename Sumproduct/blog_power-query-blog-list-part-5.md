# Power Query: Blog List – Part 5

**Source:** https://sumproduct.com/blog/power-query-blog-list-part-5/

---

[Home](https://sumproduct.com/)

\> Power Query: Blog List – Part 5

*   December 26, 2023

Power Query: Blog List – Part 5
===============================

Power Query: Blog List – Part 5
===============================

27 December 2023

_Welcome to our Power Query blog. I would like to get a list of all the Power Query blogs I have posted. Today, I look at why the method I used required Power Query in Power BI._

**Please Note**: This series of blogs was written using an old platform for the SumProduct website and the links referred to in this example have now changed.  Also, the **M** functions used to manipulate web data are now available in Excel.

I started writing this blog series way back in 2016:

![](<Base64-Image-Removed>)

There have been many developments since then, some of which I have reported upon. Since I am going to revisit more of the areas that have been improved, I am going to start with a reminder of what we have covered so far. In order to do this, I am going to use Power Query in Power BI, since there are some functions that will help me to access web data, which are not yet recognised in Power Query (Get & Transform) in Excel.

In [Part 1](https://sumproduct.com/blog/power-query-blog-list-part-1/)
, I noted that to get a full list, I am going to need several pages:

![](<Base64-Image-Removed>)

I extracted and tidied up the data for the first page:

![](<Base64-Image-Removed>)

In [Part 2](https://sumproduct.com/blog/power-query-blog-list-part-2/)
, I changed the Source step of my query to accept a parameter **P\_PageNumber,** which allows me to get the data from a specific page. I used the following **M** code:

**\=  
Web.BrowserContents(“https://www.sumproduct.com/blog/power-query-blogs?page=”&Number.ToText(P\_PageNumber))**

I checked that this still gave the same results for the query:

![](<Base64-Image-Removed>)

In [Part 3](https://sumproduct.com/blog/power-query-blog-list-part-3/)
, I converted this query into a function and generated a list of page numbers to concatenate my data:

![](<Base64-Image-Removed>)

[Last week](https://sumproduct.com/blog/power-query-blog-list-part-4/)
, I finished the query by extracting the last page number from the data, and using it as a parameter **P\_LastPage** when generating the list:

![](<Base64-Image-Removed>)

The list was then generated, and can be refreshed, no matter how many pages exist.

![](<Base64-Image-Removed>)

I can load this query to Power BI, by choosing to ‘Close & Apply’ from the Home tab:

![](<Base64-Image-Removed>)

This loads the data into the Data pane, and I can create a Table visual with the data in **Extract Blogs**:

![](<Base64-Image-Removed>)

I can export this to Excel. I start by clicking on the ‘More options’ icon.

![](<Base64-Image-Removed>)

I can then see the ‘Export data’ option:

![](<Base64-Image-Removed>)

I choose a location for the **CSV** file:

![](<Base64-Image-Removed>)

This will export the data, and I can then load it to Excel, but what is it about the queries that means they cannot be run from Excel (at the time of writing)? To answer this, I copy the **Extract Blogs** query:

![](<Base64-Image-Removed>)

I can then paste it into the ‘Queries & Connections’ pane in a blank workbook:

![](<Base64-Image-Removed>)

This copies most of the queries to my new workbook, but the process is not smooth!

![](<Base64-Image-Removed>)

I will look at what this error means in a moment. Meantime, in the Power Query editor, the only query without errors is the parameter **P\_PageNumber**:

![](<Base64-Image-Removed>)

The other queries are using functionality from Power Query in Power BI, which is not available here:

![](<Base64-Image-Removed>)

This is the same error that I encountered when pasting the queries. ‘Web.BrowserContents’ is not recognised (at the time of writing). This is the **M** function used in the Source step:

![](<Base64-Image-Removed>)

The **M** code is:

**\=  
Web.BrowserContents(“https://www.sumproduct.com/blog/power-query-blogs?page=”&Number.ToText(P\_PageNumber))**

Whilst this is recognised in Power BI, **Web.BrowserContents()** is not currently used by Power Query in Excel, hence the errors. There is more **M** code used in **fn\_ExtractBlogs**, which is also not recognised here:

![](<Base64-Image-Removed>)

The helper query **Table1** has not been copied, so I need to look in the ‘Advanced Editor’ from the Home tab:

![](<Base64-Image-Removed>)

Despite the fact that ‘No syntax errors have been detected’, we clearly have some! The source step is using **Web.BrowserContents()**, and the next step is using **Html.Table()**:

**#”Extracted Table  
From Html” = Html.Table(Source, {{“Column1”, “H2 \*”},  
{“Column2”, “.date”}, {“Column3”,  
“.teaser-text P”}, {“Column4”, “.more”}},  
\[RowSelector=”H2 \*”\]),**

If I try to view this function in the Formula bar, I get an error:

![](<Base64-Image-Removed>)

This is the same error I saw earlier for **Web.BrowserContents()**. If I try to access the webpage from Power Query in Excel, the Graphical User Interface (GUI) does not provide any useful data:

![](<Base64-Image-Removed>)

Until Power Query in Excel is able to use the same functionality as Power Query in Power BI, only webpages that use tables can be accessed in this way by Power Query in Excel.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-blog-list-part-5/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-blog-list-part-5/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-blog-list-part-5/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-blog-list-part-5/#0)

[](https://sumproduct.com/blog/power-query-blog-list-part-5/#0 "close")

top