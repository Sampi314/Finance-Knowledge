# Power Pivot Principles: Understanding functions for parent-child hierarchies in DAX – Part 1

**Source:** https://sumproduct.com/blog/power-pivot-principles-understanding-functions-for-parent-child-hierarchies-in-dax-part-1/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Understanding functions for parent-child hierarchies in DAX – Part 1

*   November 25, 2019

Power Pivot Principles: Understanding functions for parent-child hierarchies in DAX – Part 1
============================================================================================

Power Pivot Principles: Understanding functions for parent-child hierarchies in DAX – Part 1
============================================================================================

26 November 2019

_Welcome back to the Power Pivot Principles blog. Beginning this week, we are going to understand some of the functions for parent-child hierarchies in DAX._

DAX does not directly support parent-child hierarchies, _i.e._ a dependent relationship between a subordinate element (child) and its superior element (parent) – similar to the family structure (hence the name). To obtain a browsable hierarchy in the data model, we have to establish the hierarchy by using specific functions in DAX. This week, we are going to look at the function: **PATH**.

The **PATH** function uses the following syntax to operate:

**PATH(<ID\_columnName>, <parent\_columnName>)**

where:

*   <**ID\_columnName**\> is the name of an existing column containing the unique identifier for rows in the table. This cannot be an expression. The data type of the value in **ID\_columnName** must be text or integer, and must also be of the same data type as the column referenced in **parent\_columnName**
*   <**parent\_columnName**\> is the name of an existing column containing the unique identifier for the parent of the current row. This cannot be an expression. The data type of the value in **parent\_columnName** data type must be text or integer, and must be the same data type as the value(s) in **ID\_columnName**_._

For an example, consider the **HR** table shown below:

![](<Base64-Image-Removed>)

The table above specifies the relationships between the names and their managers. **A1** is at the highest level, so **A1** has no manager. **A2** is at the subordinate level to **A1**, but at a higher level to **A3** and **A4**. To better understand this hierarchy, the relationships between the nodes in a tree structure are created as shown below:

![](<Base64-Image-Removed>)

In order to create a similar hierarchy structure in PowerPivot, we can create calculated columns in DAX by leveraging a hidden calculated column that provides a string with the complete path to reach the node in the current row of the table. We write a calculated column in DAX and named it as **Path** as shown below:

![](<Base64-Image-Removed>)

As indicated by the column of **Path**, we can see that the hierarchy is listed as the relationship between managers and employees for different levels. For example, **A1** is the highest level, so it is the first element of the row. **A2** is subordinate to **A1**, so it is listed as the second element. Similar logic applies to other names as well.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-understanding-functions-for-parent-child-hierarchies-in-dax-part-1/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-understanding-functions-for-parent-child-hierarchies-in-dax-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-understanding-functions-for-parent-child-hierarchies-in-dax-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-understanding-functions-for-parent-child-hierarchies-in-dax-part-1/#0)

[](https://sumproduct.com/blog/power-pivot-principles-understanding-functions-for-parent-child-hierarchies-in-dax-part-1/#0 "close")

top