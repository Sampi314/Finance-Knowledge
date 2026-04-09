# Power Query: More Haste Less Steps Part 4

**Source:** https://sumproduct.com/blog/power-query-more-haste-less-steps-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: More Haste Less Steps Part 4

*   May 10, 2022

Power Query: More Haste Less Steps Part 4
=========================================

Power Query: More Haste Less Steps Part 4
=========================================

11 May 2022

_Welcome to our Power Query blog. This week, I look at how to move steps._

[Last time](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-3/)
, I left you with a challenge. Looking at my improved query **Dates Quicker**,

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-31-1.jpg)

how can I change the order of the columns **Month Name** and **Quarter**, using the User Interface (UI), without adding an extra step?

Before I answer that, I’ll look at the **M** code from the ‘Advanced Editor’, which is on the Home tab:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-41-1.jpg)

This shows me all the steps in my query:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-31-1.jpg)

The steps are:

**let**

    **Source = Excel.CurrentWorkbook(){\[Name=”Table1″\]}\[Content\],**

    **#”Changed Type” = Table.TransformColumnTypes(Source,{{“Column1”, type datetime}}),**

    **#”Renamed Columns” = Table.RenameColumns(#”Changed Type”,{{“Column1”, “Date”}}),**

    **#”Inserted Month Name” = Table.AddColumn(#”Renamed Columns”, “Month Name”, each Date.MonthName(\[Date\]), type text),**

    **#”Extracted First Characters” = Table.TransformColumns(#”Inserted Month Name”, {{“Month Name”, each Text.Start(\_, 3), type text}}),**

    **#”Inserted Quarter” = Table.AddColumn(#”Extracted First Characters”, “Quarter”, each Date.QuarterOfYear(\[Date\]), Int64.Type),**

    **#”Added Prefix” = Table.TransformColumns(#”Inserted Quarter”, {{“Quarter”, each “Q” & Text.From(\_, “en-GB”), type text}})**

**in**

    **#”Added Prefix”**

To change the order of the columns without adding a step, I can move the step that creates the **Quarter** column, ‘Inserted Quarter’. First, I select the column:

![](<Base64-Image-Removed>)

Next, I click and drag the step:

![](<Base64-Image-Removed>)

I place it before the step ‘Inserted Month Name’:

![](<Base64-Image-Removed>)

When I return to the final ‘Added Prefix’ step, the order of the columns has changed:

![](<Base64-Image-Removed>)

When I check the **M** code, I can see that the steps have been re-ordered:

![](<Base64-Image-Removed>)

The **M** code is now:

**let**

    **Source = Excel.CurrentWorkbook(){\[Name=”Table1″\]}\[Content\],**

    **#”Changed Type” = Table.TransformColumnTypes(Source,{{“Column1”, type datetime}}),**

    **#”Renamed Columns” = Table.RenameColumns(#”Changed Type”,{{“Column1”, “Date”}}),**

    **#”Inserted Quarter” = Table.AddColumn(#”Renamed Columns”, “Quarter”, each Date.QuarterOfYear(\[Date\]), Int64.Type),**

    **#”Inserted Month Name” = Table.AddColumn(#”Inserted Quarter”, “Month Name”, each Date.MonthName(\[Date\]), type text),**

    **#”Extracted First Characters” = Table.TransformColumns(#”Inserted Month Name”, {{“Month Name”, each Text.Start(\_, 3), type text}}),**

    **#”Added Prefix” = Table.TransformColumns(#”Extracted First Characters”, {{“Quarter”, each “Q” & Text.From(\_, “en-GB”), type text}})**

**in**

    **#”Added Prefix”**

Note that the number of the steps is the same, and the reference to the previous step has automatically been updated in each case. For example, the last step ‘Added Prefix’ has changed from

**#”Added Prefix” = Table.TransformColumns(#”Inserted Quarter”, {{“Quarter”, each “Q” & Text.From(\_, “en-GB”), type text}})**

to

**#”Added Prefix” = Table.TransformColumns(#”Extracted First Characters”, {{“Quarter”, each “Q” & Text.From(\_, “en-GB”), type text}})**

Of course, this method of moving steps around must be used with caution. For instance, I can’t move a step to change the type of a column before the column exists!

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-4/#0)

[](https://sumproduct.com/blog/power-query-more-haste-less-steps-part-4/#0 "close")

top