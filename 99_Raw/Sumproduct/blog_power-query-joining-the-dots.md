# Power Query: Joining the dots

**Source:** https://sumproduct.com/blog/power-query-joining-the-dots/

---

[Home](https://sumproduct.com/)

\> Power Query: Joining the dots

*   February 14, 2023

Power Query: Joining the dots
=============================

Power Query: Joining the dots
=============================

15 February 2023

_Welcome to our Power Query blog. This week, I return to the topic of **Table.Join()**._

Regular readers of this blog may recall [Power Query: More Merging Matters](https://sumproduct.com/blog/power-query-more-merging-matters/)
 _f_rom a couple of years ago. I am going to revisit this, as I now have an improvement. Allow me to refresh your memory. I needed to combine data from two tables:

![](<Base64-Image-Removed>)

I extracted both tables into Power Query and called the queries **Charges** and **Descriptions**. I started with **Charges** and opted to ‘Merge Queries as New’ from the Home tab.

![](<Base64-Image-Removed>)

I chose to use the default ‘Left Outer’ join and viewed the resulting **M** code.

![](<Base64-Image-Removed>)

The **M** code generated was:

**_\=_ Table.NestedJoin(Charges, {“Table\_Key”}, Descriptions,  
{“Table\_Key”}, “Descriptions”, JoinKind.LeftOuter)**

I changed this to:

**\= Table.Join(Charges,  
{“Table\_Key”}, Descriptions, {“Table\_Key”},  
“Descriptions”, JoinKind.LeftOuter, JoinAlgorithm.SortMerge)**

The use of **JoinAlgorithm.SortMerge** is explained in  [Power Query: More Merging Matters](https://sumproduct.com/blog/power-query-more-merging-matters/)
.

When I applied my code, I had a problem:

![](<Base64-Image-Removed>)

Since some of the column names in **Charges** and **Descriptions** were the same, applying **Table.Join()** meant that I encountered an error. **Table.Join()** extracts the selected columns from the joined table and adds them to the current table. To solve this at the time, I manually renamed the columns in **Descriptions**, and amended the join information to get my result:

![](<Base64-Image-Removed>)

However, there is another way I could have achieved this. There is a function called **Table.PrefixColumns()**:

Table.PrefixColumns(**table** as table, **prefix** as text) as table

This returns a table where all the column names from the **table** provided are prefixed with the given text, **prefix**, plus a period / full stop (**.**) in the form ‘**prefix.ColumnName**‘.

If I change the following **M** code:

**_\=_ Table.NestedJoin(Charges, {“Table\_Key”}, Descriptions,  
{“Table\_Key”}, “Descriptions”, JoinKind.LeftOuter)**

To use this function:

**\= Table.Join(Charges,  
{“Table\_Key”}, Table.PrefixColumns(Descriptions,”Descriptions”),  
{“Descriptions.Table\_Key”}, “Descriptions”,  
JoinKind.LeftOuter, JoinAlgorithm.SortMerge)**

This then avoids the need to manually rename columns and the columns in the query **Descriptions** remain unaffected (which would also avoid impacting any other queries that use **Descriptions**). I do need to change the join to use the amended column name **Descriptions.Table\_Key** :

![](<Base64-Image-Removed>)

This makes the use of **Table.Join()** even more efficient.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-joining-the-dots/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-joining-the-dots/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-joining-the-dots/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-joining-the-dots/#0)

[](https://sumproduct.com/blog/power-query-joining-the-dots/#0 "close")

top