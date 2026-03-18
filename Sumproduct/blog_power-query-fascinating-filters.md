# Power Query: Fascinating Filters

**Source:** https://sumproduct.com/blog/power-query-fascinating-filters/

---

[Home](https://sumproduct.com/)

\> Power Query: Fascinating Filters

*   May 14, 2019

Power Query: Fascinating Filters
================================

Power Query: Fascinating Filters
================================

15 May 2019

_Welcome to our Power Query blog. Today, I am going to look at how Power Query turns a tricky transformation into a simple task._

I am worried about the expenses my imaginary salespeople are incurring. I have identified target areas that I need to analyse. I have a query with my target areas, and I have a query with my salespeople’s data – I want to filter their data using my target area query.

![](<Base64-Image-Removed>)

I create two queries ‘From Table’ in the ‘Get & Transform’ section of the ‘Data’ tab.

![](<Base64-Image-Removed>)

I am in the ‘Salespeople\_Expenses’ query, and I can see the ‘Target\_Expenses’ query in the left-hand pane. I want to filter **_Expense_** by the column in query ‘Target\_Expenses’ (I have called the column **_Target Expenses_**). The method I am going to use is to treat **_Expense_** like a list. I used similar functionality in [Power Query: Words Are Key](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-words-are-key)
, but this time, instead of **List.ContainsAny()**, I am going to use **List.Contains()**:

List.Contains(**list** as list, **value** as any, optional **equationcriteria** as any) as logical 

This returns true if a **value** is found in a **list**. I also have the option of specifying a condition (**equationcriteria)**, but I won’t need that optional parameter in this example.

In order to get the **M** code needed to apply a filter, I first apply a standard filter to **_Expense_**.

![](<Base64-Image-Removed>)

I use the downward arrow icon next to the title of **_Expense_**, and I opt to filter on the value ‘Petrol’.

![](<Base64-Image-Removed>)

This gives me the generated **M** code:

**\= Table.SelectRows(#”Renamed Columns”, each \[Expense\] = “Petrol”)**

I can edit this to use **List.Contains()**:

**\= Table.SelectRows(#”Renamed Columns”, each List.Contains(Target\_Expenses\[Target Expenses\], \[Expense\]))**

![](<Base64-Image-Removed>)

When I click on the tick (or press **RETURN**), I expect to see only those expenses that I am targeting.

![](<Base64-Image-Removed>)

I can now focus on the expenses that concern me, so I choose to ‘Close & Load’ my query to a worksheet in my Excel workbook. If other expense types are called into question, they can be added to my original worksheet.

![](<Base64-Image-Removed>)

I refresh my query to see the results.

![](<Base64-Image-Removed>)

The latest expense code to cause concern has been added. I have renamed my sheets to make the functionality clearer.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-fascinating-filters/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-fascinating-filters/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-fascinating-filters/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-fascinating-filters/#0)

[](https://sumproduct.com/blog/power-query-fascinating-filters/#0 "close")

top