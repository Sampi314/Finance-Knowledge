# A to Z of Excel Functions: The CUBESET Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubeset-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The CUBESET Function

*   March 15, 2018

A to Z of Excel Functions: The CUBESET Function
===============================================

A to Z of Excel Functions: The CUBESET Function
===============================================

16 March 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **CUBESET** function._

**The CUBESET function**

When the workbook is connected to a Microsoft SQL Server 2005 Analysis Services or later data source, this function defines a calculated set of members or tuples by sending a set expression to the cube on the server, which creates the set, and then returns that set to Microsoft Excel.

![](https://sumproduct.com/wp-content/uploads/2025/05/9a6f7780eb45e5188e7142b811e3715c.jpg)

The **CUBESET** function employs the following syntax to operate:

**CUBESET(connection, set\_expression, , \[sort\_order\], \[sort\_by\])**

The **CUBESET** function has the following arguments:

*   **connection:** this is required and represents a text string of the name of the connection to the cube
*   **set\_expression:** this is also required. This is a text string of a set expression that results in a set of members or tuples
*   **set\_expression** can also be a cell reference to an Excel range that contains one or more members, tuples or sets included in the set
*   **caption:** this is optional. This is a text string that is displayed in the cell instead of the caption, if one is defined, from the cube
*   **sort\_order:** this is also optional. This is the type of sort, if any, to perform and can be one of the following:

![](https://sumproduct.com/wp-content/uploads/2025/05/845fd191d1cdb99398ab8463c3463224.jpg)

*   **sort\_by:** this is optional and represents a text string of the value by which to sort. For example, to get the city with the highest sales, **set\_expression** would be a set of cities and **sort\_by** would be the sales measure. Alternatively, to get the city with the highest population, **set\_expression** would be a set of cities, and **sort\_by** would be the population measure. If **sort\_order** requires **sort\_by** and **sort\_by** is omitted, **CUBESET** returns the _#VALUE!_ error message.

It should be further noted that:

*   the **CUBESET** function is supported only when the workbook is connected to a Microsoft SQL Server 2005 Analysis Services or later data source
*   when the **CUBESET** function evaluates, it temporarily displays a “#GETTING\_DATA…” message in the cell before all of the data is retrieved
*   if the connection name is not a valid workbook connection stored in the workbook, **CUBESET** returns an _#NAME?_ error value. If the Online Analytical Processing (OLAP) server is not running, not available or returns an error message, **CUBESET** returns an _#NAME?_ error value
*   if the **set\_expression** syntax is incorrect or the set contains at least one member with a different dimension than the other members, **CUBESET** returns an _#N/A_ error value
*   If **set\_expression** is longer than 255 characters, which is the limit for an argument to a function, **CUBESET** returns an _#VALUE!_ error value. To use text strings longer than 255 characters, enter the text string in a cell (for which the limit is 32,767 characters), and then use a cell reference as the argument
*   **CUBESET** may return an _#N/A_ error value if you reference a session-based object, such as a calculated member or named set, in a PivotTable when sharing a connection, and that PivotTable is deleted or you convert the PivotTable to formulae (on the ‘Options’ tab in the Ribbon, in the ‘Tools’ group, click ‘OLAP Tools’, and then click ‘Convert to Formulas’).

Please see my examples below:

**\=CUBESET(“Finance”,”Order(\[Product\].\[Product\].\[Product Category\].Members,\[Measures\].\[Unit Sales\],ASC)”,”Products”)**

**\=CUBESET(“Sales”,”\[Product\].\[All Products\].Children”,”Products”,1,”\[Measures\].\[Sales Amount\]”)**

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubeset-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubeset-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubeset-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubeset-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubeset-function/#0 "close")

top