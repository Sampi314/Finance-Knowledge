# A to Z of Excel Functions: The CUBEMEMBER Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubemember-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The CUBEMEMBER Function

*   March 4, 2018

A to Z of Excel Functions: The CUBEMEMBER Function
==================================================

A to Z of Excel Functions: The CUBEMEMBER Function
==================================================

5 March 2018

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **CUBEMEMBER** function._

**The CUBEMEMBER function**

When the workbook is connected to a Microsoft SQL Server 2005 Analysis Services or later data source, this function returns a member or tuple from the cube. This is used to validate that the member or tuple exists in the cube.

![](https://sumproduct.com/wp-content/uploads/2025/05/8c04f0838bffb67e0ce4ccc350ad5163.jpg)

The **CUBEMEMBER** function employs the following syntax to operate:

**CUBEMEMBER(connection, member\_expression, )**

The **CUBEMEMBER** function employs the following syntax to operate:

**CUBEMEMBER(connection, member\_expression, )**

The **CUBEMEMBER** function has the following arguments:

*   **connection:** this is required and represents a text string of the name of the connection to the cube
*   **member\_expression:** this is also required. This is a text string of a multi-dimensional expression (**MDX**) that evaluates to a unique member in the cube. Alternatively, **member\_expression** can be a tuple, specified as a cell range or an array constant
*   **caption:** this is optional. This represents a text string displayed in the cell instead of the caption, if one is defined, from the cube. When a tuple is returned, the caption used is the one for the last member in the tuple.

It should be further noted that:

*   the **CUBEKPIMEMBER** function is supported only when the workbook is connected to a Microsoft SQL Server 2005 Analysis Services or later data source
*   when the **CUBEMEMBER** function evaluates, it temporarily displays a “#GETTING\_DATA…” message in the cell before all of the data is retrieved
*   when you use **CUBEMEMBER** as an argument to another **CUBE** function, the **MDX** expression that identifies the member or tuple is used by that **CUBE** function, not the displayed value in the cell of the **CUBEMEMBER** function
*   if the connection name is not a valid workbook connection stored in the workbook, **CUBEMEMBER** returns a _#NAME?_ error value. If the Online Analytical Processing (OLAP) server is not running, not available or returns an error message, **CUBEMEMBER** returns a _#NAME?_ error value
*   if at least one element within the tuple is invalid, **CUBEMEMBER** returns an _#VALUE!_ error value
*   if **member\_expression** is longer than 255 characters, which is the limit for an argument to a function, **CUBEMEMBER** returns a _#VALUE!_ error value. To use text strings longer than 255 characters, enter the text string in a cell (for which the limit is 32,767 characters), and then use a cell reference as the argument instead
*   **CUBEMEMBER** returns an _#N/A_ error value when:
    *   the **member\_expression** syntax is incorrect
    *   the member specified by the **MDX** text string doesn’t exist in the cube
    *   the tuple is invalid because there is no intersection for the specified values (this can occur with multiple elements from the same hierarchy)
    *   the set contains at least one member with a different dimension than the other members
*   **CUBEMEMBER** may return an _#N/A_ error value if you reference a session-based object, such as a calculated member or named set, in a PivotTable when sharing a connection, and that PivotTable is deleted or you convert the PivotTable to formulae (on the ‘Options’ tab in the Ribbon, in the ‘Tools’ group, click ‘OLAP Tools’, and then click ‘Convert to Formulas’).

Please see my examples below:

**\=CUBEMEMBER(“Sales”,”\[Time\].\[Fiscal\].\[2020\]”)**

**\=CUBEMEMBER($A$1,D$12)**

**\=CUBEMEMBER(“Sales”,(B4, C6, D5),”SalesFor2020″)**

**\=CUBEMEMBER(“xlextdat8 FoodMart 2020 Sales”,”(\[Product\].\[Food\],\[Time\].\[2019\])”)**

**\=CUBEMEMBER($A$1,C$12:D$12)**

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubemember-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubemember-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubemember-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubemember-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-cubemember-function/#0 "close")

top