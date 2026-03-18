# Power Query: Blog List – Part 3

**Source:** https://sumproduct.com/blog/power-query-blog-list-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Blog List – Part 3

*   December 12, 2023

Power Query: Blog List – Part 3
===============================

Power Query: Blog List – Part 3
===============================

13 December 2023

_Welcome to our Power Query blog. I would like to get a list of all the Power Query blogs I have posted. Today, I continue to extend the query to extract data from all pages._

**Please Note**: This series of blogs was written using an old platform for the SumProduct website and the links referred to in this example have now changed.

I started writing this blog series way back in 2016:

![](<Base64-Image-Removed>)

There have been many developments since then, some of which I have reported upon. Since I am going to revisit more of the areas that have been improved, I am going to start with a reminder of what we have covered so far. In order to do this, I am going to use Power Query in Power BI, since there are some functions that will help me to access web data, which are not yet recognised in Power Query (Get & Transform) in Excel.

In [Part 1](https://sumproduct.com/blog/power-query-blog-list-part-1/)
, I noted that to get a full list, I am going to need several pages:

![](<Base64-Image-Removed>)

I extracted and tidied up the data for the first page:

![](<Base64-Image-Removed>)

[Last week](https://sumproduct.com/blog/power-query-blog-list-part-2/)
, I changed the Source step of my query to accept a parameter **P\_PageNumber**, in order to get the data from a specific page. I used the following code:

**\= Web.BrowserContents(“https://www.sumproduct.com/blog/power-query-blogs?page=”&Number.ToText(P\_PageNumber))**

I checked that this still gave the same results for the query:

![](<Base64-Image-Removed>)

This time, I will convert this query into a function and generate a list of page numbers to concatenate my data. To convert the query into a function, I simply right-click and choose ‘Create Function’:

![](<Base64-Image-Removed>)

I choose to call the function **fn\_ExtractBlogs**:

![](<Base64-Image-Removed>)

When I click OK, Power Query creates the function, and keeps the underlying query **Table1**, to enable me to see the steps easily without going into the ‘Advanced Editor’. The query, the function and the parameter are all automatically moved to a new folder (or group) with the same name as the function:

![](<Base64-Image-Removed>)

To get all the pages, I will need to generate a list. I right-click in the Queries pane, and choose to create a ‘Blank Query’:

![](<Base64-Image-Removed>)

In the query, I create a list from 1 to 40. I have chosen 40 as a number that is more than the current number of pages. This is a placeholder, as I will be using a parameter here.

![](<Base64-Image-Removed>)

The **M code** is simply:

**\= {1..40}**

In the ‘List Tools’ tab, I ‘Convert’ ‘To Table’:

![](<Base64-Image-Removed>)

I take the default settings:

![](<Base64-Image-Removed>)

I rename the first column **Page Number**, change the datatype to ‘Whole Number’ and add a column using ‘Invoke Custom Function’ from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

Having chosen to use **fn\_ExtractBlogs**, I use **Page Number** as the parameter value, and click OK.

![](<Base64-Image-Removed>)

I can extract the data from each ‘Table’ by using the icon next to the **Blog** heading:

![](<Base64-Image-Removed>)

I select all the data and choose not to ‘Use original column name as prefix’:

![](<Base64-Image-Removed>)

I have all the blogs, but since the first page number has the latest blogs, I sort in descending order on **Page Number**:

![](<Base64-Image-Removed>)

This leaves me with the list items at the top that did not link to any pages. I can remove these by filtering on **Date**and removing the _null_ values:

![](<Base64-Image-Removed>)

This gives me the full list, but I see that the **Description** is no longer working as I intended:

![](<Base64-Image-Removed>)

Next time, I will make some improvements to the process.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-blog-list-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-blog-list-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-blog-list-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-blog-list-part-3/#0)

[](https://sumproduct.com/blog/power-query-blog-list-part-3/#0 "close")

top