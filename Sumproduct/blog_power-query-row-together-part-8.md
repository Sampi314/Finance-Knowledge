# Power Query: Row Together Part 8

**Source:** https://sumproduct.com/blog/power-query-row-together-part-8/

---

[Home](https://sumproduct.com/)

\> Power Query: Row Together Part 8

*   August 13, 2025

Power Query: Row Together Part 8
================================

_Welcome to our Power Query blog.  This week, I look at how to make my query from way back in Part 2 more robust._

Often when using Power Query to solve a problem, there is more than one way to attack it.  This is true when it comes to combining multiple rows to make one row.  The solution will depend upon the requirements of the data and how the rows are connected.  In [Part 1](https://sumproduct.com/blog/power-query-row-together-part-1/)
, I started with a simple scenario:

![](<Base64-Image-Removed>)

In [Part 2](https://sumproduct.com/blog/power-query-row-together-part-2/)
, I created two \[2\] versions of the query, one that outputs the region data to one column and one that outputs the region data to multiple columns.  I called them **SalesRegionsRows** and **SalesRegionsColumns** respectively.  I loaded both queries to the Outputs worksheet.

![](<Base64-Image-Removed>)

I then changed the data on the Inputs worksheet:

![](<Base64-Image-Removed>)

I added a row for Mary.  When I refreshed the queries, **SalesRegionsColumns** had a row with a space, although all the data was returned:

![](<Base64-Image-Removed>)

In [Part 4](https://sumproduct.com/blog/power-query-row-together-part-4/)
,  I grouped the data in **SalesRegionsColumns** and ensured that the region data was in alphabetical order:

![](<Base64-Image-Removed>)

I need to make further improvements to query **SalesRegionsColumns**.  Let’s assume that the requirements have changed and there can be more than two \[2\] region columns:

![](<Base64-Image-Removed>)

I have created a new Table **SalesMoreRegions**.  I have also created a copy of the query **SalesRegionsColumns** called **SalesRegionsColumns\_Copy** which uses **SalesMoreRegions** as the source.  I have created a duplicate copy, which means that the steps after the source step are the same in both queries:

![](<Base64-Image-Removed>)

There are no errors but there is a problem.  In the Source step, you can see the data in **Region 3**:

![](<Base64-Image-Removed>)

However, it does not appear in the final step:

![](<Base64-Image-Removed>)

The problem is in the ‘Merged Columns’ step:

![](<Base64-Image-Removed>)

The column names **Region 1** and **Region 2** appear in the step:

> **\= Table.CombineColumns(Source,{“Region 1”, “Region 2”},Combiner.CombineTextByDelimiter(“,”, QuoteStyle.None),”Region”)**

Although the data in column **Region 3** may be seen, it is not included in the ‘Grouped Rows’ step:

![](<Base64-Image-Removed>)

This is clearly an issue if the number of region columns can vary, or even if they are renamed.  Next time, I will look at a solution which does not hard code the source column names.

Come back next time for more ways to use Power Query!

*   [Log in](https://sumproduct.com/blog/power-query-row-together-part-8/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-row-together-part-8/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-row-together-part-8/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-row-together-part-8/#0)

[](https://sumproduct.com/blog/power-query-row-together-part-8/#0 "close")

top