# Power Query: Month Mayhem – Part 2

**Source:** https://sumproduct.com/blog/power-query-month-mayhem-part-2/

---

[Home](https://sumproduct.com/)

\> Power Query: Month Mayhem – Part 2

*   July 9, 2024

Power Query: Month Mayhem – Part 2
==================================

Power Query: Month Mayhem – Part 2
==================================

10 July 2024

_Welcome to our Power Query blog. Today, I continue looking at how to index my data to keep everything in order._

My salespeople are back from their break and I have more reports to construct. I have a report with a list of the clients they have been working with each month:

![](<Base64-Image-Removed>)

I would like to display the amount details in the salesperson sections but aligned to the relevant month at the top of the page:

![](<Base64-Image-Removed>)

[Last time](https://sumproduct.com/blog/power-query-month-mayhem-part-1/)
, I extracted the data to a new workbook and began transforming the data, _viz._

![](<Base64-Image-Removed>)

I created two indices, **Source Full Index** indicates the position of the row in the report, and **Section Index** will be used to keep the sub-sections together. This time, I will recombine the data, and show how this will help me to identify the data in each section.

I choose to merge my query with itself, using the ‘Merge Queries’ option on the Home tab:

![](<Base64-Image-Removed>)

In the dialog, I select ‘Sheet1(Current)’ to merge with the same query.

![](<Base64-Image-Removed>)

I select the column **Source Full Index** on both instances of the query and choose a ‘Left Outer’ join:

![](<Base64-Image-Removed>)

Having created the step, I have the following **M** code:

**\=  
Table.NestedJoin(#”Renamed Columns1″, {“Source Full  
Index”}, #”Renamed Columns1″, {“Source Full Index”},  
“Renamed Columns1”, JoinKind.LeftOuter)**

I want to change the first table to be the step ‘Renamed Columns’ (_i.e._ when I renamed the first index) instead of ‘Renamed Columns1’:

**\=  
Table.NestedJoin(#”Renamed Columns”, {“Source Full  
Index”}, #”Renamed Columns1″, {“Source Full Index”},  
“Renamed Columns1”, JoinKind.LeftOuter)**

This gives me the following result:

![](<Base64-Image-Removed>)

I click on the icon next to the heading in the column **Renamed Columns1**, and choose which data to expand:

![](<Base64-Image-Removed>)

I only need the column **Section Index**. I also notice that my data is no longer in ascending **Source Full Index** order:

![](<Base64-Image-Removed>)

I sort ascending on **Source Full Index**:

![](<Base64-Image-Removed>)

Now I can see that the report sub-heading sections may be grouped together by filling down **Section Index**. I can achieve this by right-clicking on the heading of **Section Index** and choosing Fill and then Down:

![](<Base64-Image-Removed>)

I may now remove the column **Source Full Index**:

![](<Base64-Image-Removed>)

From this point, I need to treat the rows with amounts differently from the rest of the data. I will be using this query as a building block. I rename it to **Source Data** to make its purpose clearer:

![](<Base64-Image-Removed>)

Next time, I will take a reference copy of **Source Data** and continue transforming the data.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-month-mayhem-part-2/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-month-mayhem-part-2/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-month-mayhem-part-2/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-month-mayhem-part-2/#0)

[](https://sumproduct.com/blog/power-query-month-mayhem-part-2/#0 "close")

top