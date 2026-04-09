# Power Query: PDF Pandemonium – Part 4

**Source:** https://sumproduct.com/blog/power-query-pdf-pandemonium-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: PDF Pandemonium – Part 4

*   October 5, 2021

Power Query: PDF Pandemonium – Part 4
=====================================

Power Query: PDF Pandemonium – Part 4
=====================================

6 October 2021

_Welcome to our Power Query blog. This week, I continue transforming some data that is coming in from a PDF file, by creating transformations in preparation for developing a function next week._

The tent business is continuing to do well, and the UK division still plans to expand the workforce. I have a PDF file, and it contains tables for 10 stores. [Last week](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-3/)
, I transformed **Pay Scales** and this week I turn to the **Stores** table.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-127.jpg)

I have 10 stores in my table, and I need to perform the same transformations for each one. The first step I will take is to merge the columns I need for **Store 1**. I select **Store 1**, **Pay Scales** and **Workforce expansion** whilst holding down the **CTRL** key. When I right-click, I have the option to ‘Merge Columns’.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-168.jpg)

Clicking on this option reveals a dialog:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-133.jpg)

I choose not to use a separator, since I can split by non-numeric and numeric characters later. I want to call my new column **Store 1**, but Power Query won’t let me do this as this is one of the names of the original columns, so for now I take the default **Merged**.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-131.jpg)

I can adjust the step created from:

**Table.CombineColumns(Table.TransformColumnTypes(Source, {{“Store 1”, type text}}, “en-AU”),{“Store 1”, “Pay Scales”, “Workforce#(lf)expansion”},Combiner.CombineTextByDelimiter(“”, QuoteStyle.None),_“Merged”_)**

to:

**Table.CombineColumns(Table.TransformColumnTypes(Source, {{“Store 1”, type text}}, “en-AU”),{“Store 1”, “Pay Scales”, “Workforce#(lf)expansion”},Combiner.CombineTextByDelimiter(“”, QuoteStyle.None),_“Store 1”_)**

This is then accepted with no issues:

![](<Base64-Image-Removed>)

I repeat this for the other stores.

![](<Base64-Image-Removed>)

I could keep working on all the stores together, but it would soon become a large table. Instead, I am going to work on the stores separately. Before I do this, I need to make sure that the store name is included in the data, so I demote headers using the option from the Transform tab:

![](<Base64-Image-Removed>)

My data is now safely stored in the rows, and I can create a query from a column. I right-click with **Column1** selected:

![](<Base64-Image-Removed>)

This creates a new List Query.

![](<Base64-Image-Removed>)

I will rename my List Query to **Store 1** to reflect the data.

![](<Base64-Image-Removed>)

What I want now, is to create a series of steps that will work on any of the stores. I need a function. I start by taking a reference copy of **Store 1.**

![](<Base64-Image-Removed>)

I call my new query **fn\_store**.

![](<Base64-Image-Removed>)

The first step is to convert this list to a table. I can do this from the List tab or I may otherwise right-click.

![](<Base64-Image-Removed>)

A dialog appears where I shall accept the defaults:

![](<Base64-Image-Removed>)

This gives me access to the other tabs.

![](<Base64-Image-Removed>)

I start by promoting the first row to headers using the option on the Transform Tab.

![](<Base64-Image-Removed>)

I am ready to enter the transformations required and convert this query into a function next time.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-4/#0)

[](https://sumproduct.com/blog/power-query-pdf-pandemonium-part-4/#0 "close")

top