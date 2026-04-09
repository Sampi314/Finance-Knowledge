# Power Query: Workbook Parameter Table Example Part 6

**Source:** https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-6/

---

[Home](https://sumproduct.com/)

\> Power Query: Workbook Parameter Table Example Part 6

*   November 5, 2025

Power Query: Workbook Parameter Table Example Part 6
====================================================

_Welcome to our Power Query blog.  This week, I continue with the example by utilising the top 10 salespeople parameter._

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

[Last week](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-5/)
, I moved on to the ‘Top 10 salespeople’.  Although this refers to ‘Top 10’ the user can enter any number of salespeople here.  If they leave it empty or enter zero \[0\], then no filtering will take place.  I began by taking a reference copy of **Car\_Sales**, which I called **Top Ten**:

![](<Base64-Image-Removed>)

I grouped and sorted the data and created the framework for the filter by opting to keep the top 10 rows.

![](<Base64-Image-Removed>)

I need to replace 10 in the ‘Kept First Rows’ step with **fnGetParameter**.  But when I changed the **M** code from this:

> **\= Table.FirstN(#”Sorted Rows”,10)**

to this:

> **\= Table.FirstN(#”Sorted Rows”, fnGetParameter(“Top 10 salespeople”))**

I received an error:

![](<Base64-Image-Removed>)

I need to change the **M** code for this query to skip the filter if the ‘Top 10 salespeople’ parameter is _null_.  In the ‘Advanced Editor’, the code looks like this:

![](<Base64-Image-Removed>)

Let’s keep in mind that the whole purpose of this query is to find the top salespeople.  If the parameter is zero or _null_, none of the steps are needed.  I change the **M** code from this:

> **let**
> 
>     **Source = Car\_Sales,**
> 
>     **#”Grouped Rows” = Table.Group(Source, {“Salesperson”}, {{“Total Sales”, each List.Sum(\[Sale Price\]), type nullable number}}),**
> 
>     **#”Sorted Rows” = Table.Sort(#”Grouped Rows”,{{“Total Sales”, Order.Descending}}),**
> 
>     **#”Kept First Rows” = Table.FirstN(#”Sorted Rows”, fnGetParameter(“Top 10 salespeople”))**
> 
> **in**
> 
>     **#”Kept First Rows”**

to this:

> **let**
> 
> **// We do not need to carry out any of these steps if the parameter is null or zero**
> 
>     **Source = if fnGetParameter(“Top 10 salespeople”) <> null and fnGetParameter(“Top 10 salespeople”) <> 0 then Car\_Sales else null,**
> 
>     **#”Grouped Rows” = if fnGetParameter(“Top 10 salespeople”) <> null and fnGetParameter(“Top 10 salespeople”) <> 0 then Table.Group(Source, {“Salesperson”}, {{“Total Sales”, each List.Sum(\[Sale Price\]), type nullable number}}) else null,**
> 
>     **#”Sorted Rows” = if fnGetParameter(“Top 10 salespeople”) <> null and fnGetParameter(“Top 10 salespeople”) <> 0 then Table.Sort(#”Grouped Rows”,{{“Total Sales”, Order.Descending}}) else null,**
> 
>     **#”Kept First Rows” = if fnGetParameter(“Top 10 salespeople”) <> null and fnGetParameter(“Top 10 salespeople”) <> 0 then Table.FirstN(#”Sorted Rows”, fnGetParameter(“Top 10 salespeople”)) else null**
> 
> **in**
> 
>     **#”Kept First Rows”**

When I click Done, the result is currently _null_.

![](<Base64-Image-Removed>)

This avoids wasting resources.  Now, let’s ‘Close & Load To…’ from the Home tab and save this query as ‘Connection Only’.  I can then input a value for the ‘Top ten salespeople’:

![](<Base64-Image-Removed>)

When I go back into the Power Query Editor by double-clicking on the **Top Ten** query, the preview is refreshed:

![](<Base64-Image-Removed>)

I have the salespeople, but I need to show all the date rows for each of them.  Next week, I will combine **Top Ten** and **Car\_Sales**.

Come back next time for more ways to use Power Query!              

*   [Log in](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-6/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-6/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-6/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-6/#0)

[](https://sumproduct.com/blog/power-query-workbook-parameter-table-example-part-6/#0 "close")

top