# Power Query: See it, Save it, Sort it – Part 6

**Source:** https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-6/

---

[Home](https://sumproduct.com/)

\> Power Query: See it, Save it, Sort it – Part 6

*   June 21, 2022

Power Query: See it, Save it, Sort it – Part 6
==============================================

Power Query: See it, Save it, Sort it – Part 6
==============================================

22 June 2022

_Welcome to our Power Query blog. This week, I group my data._

In [Power Query: See it, Save it, Sort it – Part 1](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-1/)
, I started with some data for my imaginary salespeople:

![](<Base64-Image-Removed>)

and extracted it into Power Query, in order to perform some transformations.

![](<Base64-Image-Removed>)

[Last week](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-5/)
, I merged my query with an earlier version of the same query to filter my data.

![](<Base64-Image-Removed>)

This time, I want to summarise my data so that I have one row per day. To do this, I use the ‘Group by’ functionality, which is on the Home tab:

![](<Base64-Image-Removed>)

This brings up a dialog:

![](<Base64-Image-Removed>)

I will need to create more than one column when I group the data, so I choose the Advanced options:

![](<Base64-Image-Removed>)

I’d like to record the names of the salespeople that contributed to the sales on each date, but there is no option to append the names together. I am going to choose to Sum the **Name** column!

![](<Base64-Image-Removed>)

Power Query can’t do this, so the **Names** column has errors:

![](<Base64-Image-Removed>)

However, I am going to adjust the **M** code. Currently, the **M** code for the ‘Grouped Rows’ step is:

**_\=_ Table.Group(#”Removed Columns”,  
{“Date”}, {{“Amount”, each List.Sum(\[Amount\]), type  
nullable number}, {“Names”, each List.Sum(\[Name\]), type nullable  
text}})**

Currently, I have the following code to create the Names column:

**each List.Sum(\[Name\])**

I want to change this so that it appends the text instead, so I am going to use the **Text.Combine()** function instead:

**each Text.Combine(\[Name\], “, “)**

The second argument here is the separator(, ). The **M** code for the full step is now:

**\= Table.Group(#”Removed Columns”,  
{“Date”}, {{“Amount”, each List.Sum(\[Amount\]), type  
nullable number}, {“Names”, each Text.Combine(\[Name\], “, “),  
type nullable text}})**

This gives me the **Names** column without any errors:

![](<Base64-Image-Removed>)

However, I have values for **Names** with repeating names, e.g. ‘Paul, Paul, John, John, John, Paul, Paul, Paul, Paul’.

Next time, I’ll modify this step again to only show each name once.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-6/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-6/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-6/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-6/#0)

[](https://sumproduct.com/blog/power-query-see-it-save-it-sort-it-part-6/#0 "close")

top