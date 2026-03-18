# Power Query: Group Dynamics

**Source:** https://sumproduct.com/blog/power-query-group-dynamics/

---

[Home](https://sumproduct.com/)

\> Power Query: Group Dynamics

*   October 9, 2018

Power Query: Group Dynamics
===========================

Power Query: Group Dynamics
===========================

10 October 2018

_Welcome to our Power Query blog. This week, I look at how to calculate a group share._

This week’s blog looks at how to achieve a group share calculation in Power Query, in the same way that I can perform one in Excel. This is an exercise in how to manipulate data in Power Query; it is not how I would actually attempt to do this calculation, since it is much easier to do this in Excel or PowerPivot

I have the following data. I am interested in finding out which groups make up most owned items. I want to see the percentage of owned or outsourced items for each group.

![](<Base64-Image-Removed>)

In Excel I can create an additional column and enter the formula

**\=\[@\[Items\_in\_Group\]\]/SUMIFS(\[Items\_in\_Group\],\[Owned/Outsourced\],\[@\[Owned/Outsourced\]\])**

which calculates the percentage of outsourced or owned items that are in the current group.

![](<Base64-Image-Removed>)

I can see that ‘Floor’ items make up 40% of the owned items.

I want to perform the same calculation in Power Query, so I create a new query ‘From Table’ from the ‘Get & Transform’ section on the ‘Data’ tab.

![](<Base64-Image-Removed>)

I start by grouping by my **_Owned/Outsourced_** column. This will allow me to make my first step – to calculate the total number of items in each group:

![](<Base64-Image-Removed>)

I use a basic group by statement, where I sum **_Items\_In\_Group._** This will simplify my data so that I can see the number of items that are owned and the number of items that are outsourced.

![](<Base64-Image-Removed>)

I know that step ‘Changed Type’ shows me all the details, and ‘Grouped Rows’ shows me the total items owned and outsourced. The first method I will use to get to my final calculation is to merge these steps by merging **Table2** with itself (I will show another method later).

![](<Base64-Image-Removed>)

I choose the first column each time, and select the left outer join.

![](<Base64-Image-Removed>)

From the **M** code generated for this step, I can see that the ‘Grouped Rows’ step has been merged with itself.

**\= Table.NestedJoin(#”Grouped Rows”,{“Owned/Outsourced”},#”Grouped Rows”,{“Owned/Outsourced”},”Grouped Rows”,JoinKind.LeftOuter)**

I can edit this step so that I merge the ‘Changed Type’ step instead.

![](<Base64-Image-Removed>)

I have now taken my ‘Changed Type’ step with all the details and merged the ‘Grouped Rows’ step. I only want **_Total Items Owned or Outsourced_** from the ‘Grouped Rows’ step, so I expand the table and pick this column.

![](<Base64-Image-Removed>)

As usual, I don’t want to ‘Use original column name as prefix’!

![](<Base64-Image-Removed>)

Now I have the two key values for my percentage calculation, I can create a custom column from the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

I divide the number of items in the group by the items owned or outsourced to see which group is mostly made up of owned and outsourced items respectively. I could also do this using the ‘Divide’ option from the ‘Standard’ part of the ‘From Number’ section.

![](<Base64-Image-Removed>)

In the same way I did for the Excel method, I convert my new column to type ‘Percentage’.

![](<Base64-Image-Removed>)

My calculations are consistent with the Excel method.

I can achieve the same result in another way. I can use **M** code if I don’t want to merge my queries. Instead of using the ‘Grouped Rows’ step above, I create a custom column which will carry out the grouping for me.

![](<Base64-Image-Removed>)

The **M** code I have used is:

**\= Table.AddColumn(#”Sorted Rows”, “Items\_Owned\_Outsourced”, each Table.Group(Table2, “Owned/Outsourced”, {“Total”, each List.Sum(\[Items\_in\_Group\])}))**

The part of this which creates my grouped total is **Table.Group(Table2, “Owned/Outsourced”, {“Total”, each List.Sum(\[Items\_in\_Group\])})**

I have grouped by **_Owned/Outsourced_** and summed **_Items\_in\_Group_** within this. This gives me a table very similar to the one created by the merging of the query with itself, which I can expand.

![](<Base64-Image-Removed>)

As before, I can create my custom (or divide) column and convert it to a percentage. This time, I will use the divide functionality.

![](<Base64-Image-Removed>)

This gives me a new **_Division_** column which I can rename.

![](<Base64-Image-Removed>)

Having converted this to the right data type, my data is consistent with the other results.

![](<Base64-Image-Removed>)

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-group-dynamics/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-group-dynamics/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-group-dynamics/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-group-dynamics/#0)

[](https://sumproduct.com/blog/power-query-group-dynamics/#0 "close")

top