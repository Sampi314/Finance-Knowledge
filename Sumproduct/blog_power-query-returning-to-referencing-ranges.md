# Power Query: Returning to Referencing Ranges

**Source:** https://sumproduct.com/blog/power-query-returning-to-referencing-ranges/

---

[Home](https://sumproduct.com/)

\> Power Query: Returning to Referencing Ranges

*   February 20, 2018

Power Query: Returning to Referencing Ranges
============================================

Power Query: Returning to Referencing Ranges
============================================

21 February 2018

_Welcome to our Power Query blog. This week, I take another look at what I can do with Excel.CurrentWorkbook._

In [Power Query: Cell Referencing](https://sumproduct.com/blog/power-query-cell-referencing/)
, I looked at how to reference a single cell in a worksheet. I’d like to return to the **M** function **Excel.CurrentWorkbook** to show how to reference more than one cell.

To begin with, the description of **Excel.CurrentWorkbook** in the Microsoft help pages doesn’t give much away:

**Excel.CurrentWorkbook() as table** 

      **Returns the tables in the current Excel Workbook.**

What this doesn’t reveal, is that it is not just the tables that are returned, but also any named ranges. I have a workbook containing some of my fictional employee data, which has a table on one sheet and named ranges on another sheet, as shown below:

![](<Base64-Image-Removed>)

I might want to pull data from these ranges into a query on employee data, to use for parameter selection for example. If I create a Blank Query, I can use the **Excel.CurrentWorkbook()** function to show me what tables and ranges are available. To create a Blank Query, in the ‘Data’ tab I choose the ‘New Query’ option and select ‘Blank Query’ from the ‘From Other Sources’ section, _viz._

![](<Base64-Image-Removed>)

Now I can use the function **Excel.CurrentWorkbook()**.

![](<Base64-Image-Removed>)

At the top I have my ‘Employees’ table, named according to the Access database it has been extracted from. Below that I have three ranges. There is a range missing from my workbook, and it is missing because of a particular property.

![](<Base64-Image-Removed>)

I created a non-contiguous range in my workbook (where the cells are not consecutive) and this hasn’t been picked up by Power Query. The previous version of Power Query dealt inconsistently with these types of ranges, which is probably why they are no longer accessed by the function **Excel.CurrentWorkbook()**.

Back in my query, I remove the row relating to the ‘Employee Table’ and use the split arrow icon to drill down to the content of my named ranges:

![](<Base64-Image-Removed>)

This shows that all my data is accessible. If I want to select data from a particular named range, then instead of using the expand icon, I can click on the word ‘Table’ next to the range I want.

![](<Base64-Image-Removed>)

(Note that when I tried this, Power Query tried to promote the top row to a heading – if this happens, just delete that step!)

I can also get to this data at the beginning of the query creation if I know the name of the range that I want.

![](<Base64-Image-Removed>)

The **M** language to access my ‘Country\_Range’ is

**\= Excel.CurrentWorkbook(){\[Name=”Country\_Range”\]}\[Content\]**

To access a single cell, _e.g._ ‘United States’, I can right click on the value and use the ‘Drill Down’ option:

![](<Base64-Image-Removed>)

This extracts a single value:

![](<Base64-Image-Removed>)

This is the functionality that was used in [Power Query: Cell Referencing](https://sumproduct.com/blog/power-query-cell-referencing/)
, but amended to look at ‘Country\_Range’:

**Excel.CurrentWorkbook(){\[Name=”Country\_Range”\]}\[Content\]{0}\[Column1\]**

If I enter this at the beginning of the query I can go straight to the value in that cell:

![](<Base64-Image-Removed>)

Note that in the function,

**Excel.CurrentWorkbook(){\[Name=”Country\_Range”\]}\[Content\]{_0_}\[Column1\]**

the 0 that I have highlighted in green indicates the value on the first row; if I wanted the second value I would enter 1 instead (Power Query likes to index many lists starting at zero rather than one).

![](<Base64-Image-Removed>)

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-returning-to-referencing-ranges/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-returning-to-referencing-ranges/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-returning-to-referencing-ranges/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-returning-to-referencing-ranges/#0)

[](https://sumproduct.com/blog/power-query-returning-to-referencing-ranges/#0 "close")

top