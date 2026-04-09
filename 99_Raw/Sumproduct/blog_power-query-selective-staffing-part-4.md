# Power Query: Selective Staffing Part 4

**Source:** https://sumproduct.com/blog/power-query-selective-staffing-part-4/

---

[Home](https://sumproduct.com/)

\> Power Query: Selective Staffing Part 4

*   November 16, 2021

Power Query: Selective Staffing Part 4
======================================

Power Query: Selective Staffing Part 4
======================================

17 November 2021

_Welcome to our Power Query blog. This week, I revisit my first inclusion examples to find solutions that involve exclusion._

I have looked at two examples over the last few weeks where I included data based upon a list of values. I will look at both examples to see how I would have excluded the data instead.

The first example was in [Selective Staffing Part 1](https://sumproduct.com/blog/power-query-selective-staffing-part-1/)
 where I had allocated salespeople:

![](<Base64-Image-Removed>)

I needed to produce a version of this table only including the available salespeople:

![](<Base64-Image-Removed>)

I created a new table which showed only the included salespeople for each area:

![](<Base64-Image-Removed>)

However, I could have the situation where some of the salespeople have been booked for a conference, and I need to exclude them from my allocations.

![](<Base64-Image-Removed>)

The Excel Tables for this example are **Staffing\_Exclude** and **Selection\_Exclude**. I create a new query **Selection Exclude** which is similar to the query **Selection** I used in [Selective Staffing Part 2](https://sumproduct.com/blog/power-query-selective-staffing-part-2/)
. **Selection** extracted the included staff table **Selection** and converted it to a list. This query extracts **Selection\_Exclude**.

![](<Base64-Image-Removed>)

You will recall that there were two main issues to solve when solving the inclusion problem. I needed to work out which values to keep and then remove spaces in the table. Only the first issue is affected by excluding instead of including, so I will make a duplicate of the query I finished in [Selective Staffing Part 2](https://sumproduct.com/blog/power-query-selective-staffing-part-2/)
, which is called **Staffing.** The first step I need to change is the Source step:

![](<Base64-Image-Removed>)

Currently, this is extracting data from the Excel table **Staffing**:

**\= Excel.CurrentWorkbook(){\[Name=”Staffing”\]}\[Content\]**

I can change this to Staffing\_Exclude, to point at the new table.

**\= Excel.CurrentWorkbook(){\[Name=”Staffing\_Exclude”\]}\[Content\]**

To save this change, I press **ENTER** or use the tick next to the formula bar.

Having changed the Source, I need to change any steps that selected data based upon the included list.

![](<Base64-Image-Removed>)

The only steps that will be affected are the ‘Added Custom’ steps, as the remainder of the query is dealing with blank values.

If I look at the first ‘Added Custom’ step using the gear icon, I can see the **M** code I used:

![](<Base64-Image-Removed>)

The **M** code is:

**\= if List.ContainsAny(Selection, {\[#”Marketing “\]}) then \[#”Marketing “\]  else null**

**Selection** is the included staff table; I need to change this to use **Selection\_Exclude.**

**\= if List.ContainsAny(Selection\_Exclude, {\[#”Marketing “\]}) then \[#”Marketing “\]  else null**

I also need to reverse the logic, as I need to include data which is not on the list.

**\= if List.ContainsAny(Selection\_Exclude, {\[#”Marketing “\]}) then null else \[#”Marketing “\]**

I need to make these changes to all the ‘Custom Column’ steps.

![](<Base64-Image-Removed>)

The salespeople in the excluded list have now been removed from the table, and the remaining steps will reorganise the data to remove the blank values. I rename the query **Staffing Exclude**.

![](<Base64-Image-Removed>)

When I ‘Close & Load’ the data, I have only the salespeople that are not excluded:

![](<Base64-Image-Removed>)

Next time I will look at how to exclude data in my second example…

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-selective-staffing-part-4/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-selective-staffing-part-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-selective-staffing-part-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-selective-staffing-part-4/#0)

[](https://sumproduct.com/blog/power-query-selective-staffing-part-4/#0 "close")

top