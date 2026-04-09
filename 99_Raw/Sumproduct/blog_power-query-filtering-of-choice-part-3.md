# Power Query: Filtering of Choice Part 3

**Source:** https://sumproduct.com/blog/power-query-filtering-of-choice-part-3/

---

[Home](https://sumproduct.com/)

\> Power Query: Filtering of Choice Part 3

*   September 10, 2024

Power Query: Filtering of Choice Part 3
=======================================

Power Query: Filtering of Choice Part 3
=======================================

11 September 2024

_Welcome to our Power Query blog. This week, I continue finding a solution to a challenge involving a choice of filters by transforming **Tbl\_Sales\_Data**._

In this series, I am considering a filtering challenge. Essentially, I have a Table of data, **Tbl\_Sales\_Data**, shown below::

![](<Base64-Image-Removed>)

I will be filtering this data, by comparing values from one of these Tables, which have been named **Tbl\_Dates**, **Tbl\_Amounts** and **Tbl\_Person**:

![](<Base64-Image-Removed>)

The choice of which Table to use is controlled by a dropdown, which has been given the Named Range **P\_Choice** and another translation Table, **Tbl\_Translation**:

![](<Base64-Image-Removed>)

In **Tbl\_Translation**, the first column, **Choice** will link to the value from the dropdown. The second column **Translation**, then translates to a column from the data Table. All of the data has been entered manually and the results will be driven by the value selected in **P\_Choice**.

![](<Base64-Image-Removed>)

[Last week](https://sumproduct.com/blog/power-query-filtering-of-choice-part-2/)
, I started with the queries I had extracted to Power Query, and combined them to build on to the **P\_Choice** query:

![](<Base64-Image-Removed>)

The final step was to change the data type of **Value** to ‘Text’. The filter choices are ready; this week I move onto the **Tbl\_Sales\_Data** query and apply the filters. I begin by removing the auto-generated ‘Changed Type’ step. It is important that all the columns I am comparing have the same data type; therefore, I set them all to ‘Text’:

![](<Base64-Image-Removed>)

This is to prevent any mismatch errors. I choose to create a ‘Custom Column’ from the ‘Add Columns’ tab:

![](<Base64-Image-Removed>)

I enter some **M** code:

![](<Base64-Image-Removed>)

I have named the column **Match**, and the **M** code is:

**(CheckStrings) =>**

**  
List.AnyTrue(List.Transform(P\_Choice\[Value\], each  
Text.Contains((Table.Column(CheckStrings,P\_Choice\[Translation\]{0})),\_ )))**

This is entering a function **CheckStrings()** which is using list functionality to indicate if there is a match in the column identified by **Translation** of **P\_Choice** for the values in Value of **P\_Choice**. However, this returns an error:

![](<Base64-Image-Removed>)

Instead of using a record from the query **P\_Choice**:

**P\_Choice\[Translation\]{0}**

I need to extract this into a parameter containing the value. I begin by taking a reference copy of **P\_Choice**:

![](<Base64-Image-Removed>)

I may then right-click on any cell in the **Translation** column and opt to ‘Drill Down’:

![](<Base64-Image-Removed>)

I call the new query / parameter **P\_Choice\_Column**:

![](<Base64-Image-Removed>)

Back in the query **Tbl\_Sales\_Data**, I amend the custom column I created:

![](<Base64-Image-Removed>)

The **M** code is now:

**\=** **(CheckStrings)  
\=>**

**List.AnyTrue(List.Transform(P\_Choice\[Value\],  
each Text.Contains((Table.Column(CheckStrings,P\_Choice\_Column)),\_ )))**

This time, the resulting column contains a Boolean:

![](<Base64-Image-Removed>)

I may filter to exclude the ‘FALSE’ values in **Matched**:

![](<Base64-Image-Removed>)

I have the data I need. It just remains for me to remove the **Matched** Column and use **CTRL**\+ **A** whilst in any of the headings to allow me to use the ‘Detect Data Type’ option from the Transform Tab:

![](<Base64-Image-Removed>)

My data is ready to be loaded into the Excel workbook, where I will check that it works for all choices.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-filtering-of-choice-part-3/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-filtering-of-choice-part-3/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-filtering-of-choice-part-3/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-filtering-of-choice-part-3/#0)

[](https://sumproduct.com/blog/power-query-filtering-of-choice-part-3/#0 "close")

top