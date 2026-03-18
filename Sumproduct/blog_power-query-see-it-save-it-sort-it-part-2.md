# Power Query: See it, Save it, Sort it – Part 2

**Source:** https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: See it, Save it, Sort it – Part 2

*   May 24, 2022

Power Query: See it, Save it, Sort it – Part 2
==============================================

Power Query: See it, Save it, Sort it – Part 2
==============================================

25 May 2022

_Welcome to our Power Query blog. This week, I continue looking at a sorting issue._

[Last time](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-1/)
, I started with some data for my imaginary salespeople:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-26-1.jpg)

and extracted it into Power Query, in order to perform some transformations.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-33-1.jpg)

I want to ensure that I have a row for every date, as I plan to apply time intelligence calculations to my data. To do this, I am going to create a list of all dates that I can append to my data. To find the range of dates I need, I start by right-clicking on **Sales\_Transactions** in the Queries pane, and then I choose to make a Duplicate query. As the new query is copied from, but not linked to **Sales\_Transactions**, any new dates will be picked up, but if I add steps to **Sales\_Transactions**, they will not be picked up by the new query.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-26-1.jpg)

I call my new query **Full\_Dates**:

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-21-1.jpg)

Power Query has generated a ‘Changed Type’ step based on algorithms that sample the data.

**\= Table.TransformColumnTypes(Source,{{“Date”, type datetime}, {“Amount”, Int64.Type}, {“ID”, Int64.Type}, {“Name”, type text}})**

Although **Date** does indeed contain dates, I want to use the data type ‘Whole Number’. I plan to create a list, and lists currently work with numbers, but not dates.

I could either change the **M** code is this step, or I can get Power Query to do it for me by using the dropdown under the data type icon:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-14-1.jpg)

When I choose ‘Whole Number’ , Power Query recognises that this would be another ‘Changed Type’ step, so it offers to combine them:

![](<Base64-Image-Removed>)

This is exactly what I want, so I choose to ‘Replace current’:

![](<Base64-Image-Removed>)

Date is now shown as a ‘Whole Number’. To find the maximum and minimum date, I can use the ‘Group By’ functionality which is on the Transform tab and the Home tab:

![](<Base64-Image-Removed>)

This opens a dialog. I need to choose the ‘Advanced’ option, and I need to remove the grouping on date by clicking on the ellipsis (…) and deleting it.

![](<Base64-Image-Removed>)

I add two \[2\] aggregations:

![](<Base64-Image-Removed>)

Clicking OK gives me the values I need to create a list of dates:

![](<Base64-Image-Removed>)

Now I can enter the **M** code to create the list of dates; to do this, I add a ‘Custom Column’ from the ‘Add Column’ tab:

![](<Base64-Image-Removed>)

In the dialog, I create a list from the columns:

![](<Base64-Image-Removed>)

The **M** code is:

**\= {\[Min\_Date\]..\[Max\_Date\]}**

This gives me a column with a _List_ in it, which will start from **\[Min Date\]** and end at **\[Max Date\]** and contain every number in between.

![](<Base64-Image-Removed>)

I right-click on Custom and ‘Remove Other Columns’. I can then click on the expand icon to extract the _List_ values:

![](<Base64-Image-Removed>)

I can ‘Expand to New Rows’ as I want a column containing all the dates:

![](<Base64-Image-Removed>)

I rename my column **Date** and change the data type to ‘Date’ using the dropdown from the data type icon. **Full\_Dates** is now ready to use:

![](<Base64-Image-Removed>)

Next time, I will append this to my original query.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-2/#0)

[](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-2/#0 "close")

top