# Power Query: A Join I Made Earlier

**Source:** https://sumproduct.com/blog/power-query-a-join-i-made-earlier/

---

[Home](https://sumproduct.com/)

\> Power Query: A Join I Made Earlier

*   January 15, 2019

Power Query: A Join I Made Earlier
==================================

Power Query: A Join I Made Earlier
==================================

16 January 2019

_Welcome to our Power Query blog. This week, I look at a neat way of linking tables with similar key data._

When I came across this method of linking key data in tables that is ‘almost’ the same, I wanted to share it! I have two tables of tent data:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-502.jpg)

and

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-522.jpg)

The key data is very similar, but not quite the same. I want to find out which key data in ‘Owned Tent Types’ could be linked to the data in ‘Hired Tent Types’ – so for example, I want to link ‘Large Blue’ owned tents to ‘Large’ hired tents.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-490.jpg)

I’m impressed by how easily this can be achieved by using **keyEqualityComparers.** These comparers determine how the keys on each table are compared with each other. I mentioned them previously in [Power Query: Join Me at the Table](https://sumproduct.com/blog/power-query-join-me-at-the-table/)
, where the option to use **keyEqualityComparers** is provided in **M** function **Table.Join()**.

This time, I will add a column to the table ‘Owned Tents’, which links the two tables. In this case, I want to join my tables if the sequence of letters in the key in the second table appear in the sequence of letters in the key in the first table. I can then link ‘Large Blue’ from the ‘**Owned\_Tents**‘ table to ‘Large’ in the ‘**Hired\_Tents**‘ table.

The line of **M** code that does all this heavy lifting is:

**RelativeMerge = Table.AddColumn(Owned\_Tents, “RelativeJoin”,**

            **(Earlier) => Table.SelectRows(Hired\_Tents,**

                         **each Text.Contains(Earlier\[Owned Tent Type\],\[Hired Tent Type\],**

**Comparer.OrdinalIgnoreCase)))**

This code adds a new column, **_RelativeJoin_**. The new column contains a join between my tables where **_Hired Tent Types_** contain a sequence of letters that match **_Own Tent Type_**, ignoring whether they are upper or lower case.

The use of the ‘**Earlier**‘ syntax is complex to explain. The same function in **DAX** (the Power Pivot language) is described as:

This returns the current value of the specified column in an outer evaluation pass of the mentioned column.

**EARLIER** is useful for nested calculations where you want to use a certain value as an input and produce calculations based on that input. In Microsoft Excel, you can do such calculations only within the context of the current row; however, in **DAX** you can store the value of the input and then make calculation using data from the entire table.

**EARLIER** is mostly used in the context of calculated columns.

I need to use ‘**Earlier**‘ to allow for my nested comparison. This line of **M** code creates a table in each entry of my new column as the result, which can be expanded.

![](<Base64-Image-Removed>)

The expansion is a simple process, as the table only contains the value of **_Hired Tent Type_** if there is a match, and null if there isn’t.

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-a-join-i-made-earlier/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-a-join-i-made-earlier/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-a-join-i-made-earlier/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-a-join-i-made-earlier/#0)

[](https://sumproduct.com/blog/power-query-a-join-i-made-earlier/#0 "close")

top