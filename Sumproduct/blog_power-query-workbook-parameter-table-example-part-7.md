# Power Query: Workbook Parameter Table Example Part 7

**Source:** https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-7/

---

[Home](https://sumproduct.com/)

\> Power Query: Workbook Parameter Table Example Part 7

*   November 12, 2025

Power Query: Workbook Parameter Table Example Part 7
====================================================

_Welcome to our Power Query blog.  This week, I continue with the example by combining the queries._

During training, attendees often ask how to use parameters to make their Power Query reports more flexible.  I recently looked at this in two \[2\] blog collections: [Workbook Parameter Tip](https://sumproduct.com/uncategorized/power-query-workbook-parameter-tip/)
 and [Workbook Parameter Table Tip](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/)
.  My fictional salespeople can take some well-earned leave since I will be applying the same method to a much larger dataset.  I will show how I can quickly create the same Parameters query in a new workbook and use it to access specific information.  I will be using car data I have extracted from the Kaggle website.  There are 241,205 rows.

![](<Base64-Image-Removed>)

Some of the filters required have been entered on the Outputs sheet:

![](<Base64-Image-Removed>)

In [Part 1](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-1/)
, I converted this into the Table I need for the **fnGetParameter** method I used in the [Workbook Parameter Table Tip](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/)
 series.

![](<Base64-Image-Removed>)

I copied the function from the workbook I used in the [Workbook Parameter Table Tip](https://sumproduct.com/blog/power-query-workbook-parameter-table-tip-part-1/)
 series to the current workbook.

![](<Base64-Image-Removed>)

In [Part 2](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-2/)
 , I imported the car sales data into Power Query and temporarily reduced the data in the query.

![](<Base64-Image-Removed>)

[In Part 3](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-3/)
, I added a filter on the **Date** column and used **fnGetParameter** to pass the range parameters from the workbook to the query.  This currently gives me no data, as the parameters don’t have values:

![](<Base64-Image-Removed>)

[In Part 4](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-4/)
, I entered **M** code to determine how to filter the **Date** based on how many of the date parameters the user entered.  I tested various combinations of ‘Date from’ and ‘Date to’ values.

![](<Base64-Image-Removed>)

[In Part 5](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-5/)
, I moved on to the ‘Top 10 salespeople’.  Although this refers to ‘Top 10’ the user can enter any number of salespeople here.  If they leave it empty or enter zero \[0\], then no filtering will take place.  I began by taking a reference copy of **Car\_Sales**, which I called **Top Ten**:

![](<Base64-Image-Removed>)

I grouped and sorted the data and created the framework for the filter by opting to keep the top 10 rows.

![](<Base64-Image-Removed>)

[Last week](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-6/)
, I refined the **M** code to ensure that the steps in this query only access **Car\_Sales** if the ‘Top 10 salespeople’ parameter were not _null_ or zero \[0\].

![](<Base64-Image-Removed>)

I have the salespeople, but I need to show all the date rows for each of them.  It is time to combine **Top Ten** and **Car\_Sales**.

Since **Top Ten** references **Car\_Sales**, I cannot begin with **Car\_Sales** and merge with **Top Ten**.  I would have a circularity.  I could ‘Merge as new’  to create a new query, but this would make it difficult to  apply the parameter checks.  If ‘Top 10 salespeople’ is _null_ or zero, I don’t need to merge.  Instead, I create a duplicate copy of **Car\_Sales**, which I call **Car\_Sales Reference**.

![](<Base64-Image-Removed>)

I change **Top Ten** to reference **Car\_Sales Reference**.

![](<Base64-Image-Removed>)

I have changed the **M** code for the Source step from:

> **\= if fnGetParameter(“Top 10 salespeople”) <> null and fnGetParameter(“Top 10 salespeople”) <> 0 then Car\_Sales else null**

to:

> **\= if fnGetParameter(“Top 10 salespeople”) <> null and fnGetParameter(“Top 10 salespeople”) <> 0 then #”Car\_Sales Reference” else null**

Note that I needed to add speech marks (**“”**) and a hash / pound sign (**#**), since the new query has a space in its name.

Now I can begin in **Car\_Sales**, and use ‘Merge Queries’ on the Home tab to merge with **Top Ten**:

![](<Base64-Image-Removed>)

I have selected the **Salesperson** column in each query and chosen to use a ‘Right Outer’ join.  This ensures that only rows for the selected salespeople are returned.  When I click OK, a new column called **Top Ten** is created:

![](<Base64-Image-Removed>)

Next time, I will extract the data I need from the Tables in the **Top Ten** column and check the value in ‘Top 10 salespeople’ before performing the merge.

Come back next time for more ways to use Power Query!              

*   [Log in](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-7/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-7/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-7/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-7/#0)

[](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-7/#0 "close")

top