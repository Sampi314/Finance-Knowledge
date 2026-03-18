# Power Query: Mad Max

**Source:** https://sumproduct.com/blog/power-query-mad-max/

---

[Home](https://sumproduct.com/)

\> Power Query: Mad Max

*   September 1, 2020

Power Query: Mad Max
====================

Power Query: Mad Max
====================

2 September 2020

_Welcome to our Power Query blog. This week, I look at an example of how to work with maximum values._

I have the following tent data:

![](<Base64-Image-Removed>)

I want to derive the latest date for each supplier and the salesperson who contacted them. I start by extracting my data to Power Query. I can then choose to ‘Group By’ from the Transform tab.

![](<Base64-Image-Removed>)

If I try and get the maximum date with the salesperson attached, I get the following results:

![](<Base64-Image-Removed>)

The problem here is that although the dates are right, the salesperson is not. The salespeople should be Liam, Newbie and Mark, but Mary and Peter are being selected because alphabetically, their names are the latest.

If I go back to the ‘Group By’ step, I can change the way I group my data.

![](<Base64-Image-Removed>)

Instead of choosing the salesperson in the second aggregation, I opt for ‘All rows’. I click ‘OK’ to see the results.

![](<Base64-Image-Removed>)

I have a table against each row with all the data for that supplier. I need to extract the correct row from the table for each supplier. To do this, I create a new custom column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Table.Max(\[By\], “Date”)**

This selects the record in the table in my **By** column which has the maximum value in **Date**.

![](<Base64-Image-Removed>)

When I click ‘OK’, I get a new column, with a record as each entry. Clicking next to my first record, I can see that, this time, I have the correct salesperson associated with my date. I can expand the record by clicking on the icon next to the column title.

![](<Base64-Image-Removed>)

I only need the salesperson from the expanded row. I choose not to ‘use the original column as prefix’.

![](<Base64-Image-Removed>)

I have the correct salesperson for each date. Next time, I’ll look at a way to achieve this in fewer steps.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-mad-max/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-mad-max/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-mad-max/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-mad-max/#0)

[](https://sumproduct.com/blog/power-query-mad-max/#0 "close")

top