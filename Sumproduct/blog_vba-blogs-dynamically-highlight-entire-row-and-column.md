# VBA Blogs: Dynamically highlight entire row and column

**Source:** https://sumproduct.com/blog/vba-blogs-dynamically-highlight-entire-row-and-column/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Dynamically highlight entire row and column

*   August 15, 2019

VBA Blogs: Dynamically highlight entire row and column
======================================================

VBA Blogs: Dynamically highlight entire row and column
======================================================

16 August 2019

_Welcome back to the VBA blog! This week we are going to expand our learning of how to highlight selected cells in a worksheet from last week._

Last week, we have used both VBA script and conditional formatting to highlight the row of selected cells. This week we are going to use the VBA script and conditional formatting to highlight both the row and column of selected cells. It is an enhancement of the method we used last week and it will highlight the row of selected cell and easy for user to locate the data.

We would like to add highlight rows and columns for the dataset below:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-378.jpg)

and the result would look like this:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-388.jpg)

The first step is to add a new SelectionChange event in the target worksheet as described in last week blog.

In the coding area of sub-procedure, we create two new named ranges ActiveRow and ActiveColumn to the workbook the same way as described last week. The new named ranges refer to the active cell by selection. Therefore, the reference here is dynamic.

Private Sub Worksheet\_SelectionChange(ByVal Target As Range)

ThisWorkbook.Names.Add “ActiveRow”, ActiveCell.Row

ThisWorkbook.Names.Add “ActiveCol”, ActiveCell.Column

End Sub

Then for the next step, go to the conditional formatting Ribbon and add a new rule. We use a formula to determine the cells to format. In the formula input, write the function

“**\=OR(ROW()=ActiveRow, COLUMN()=ActiveCol)**“.

The role of this function is to determine if the active row and active column is the same as the row and column of current cell selection. If so, the row and column will follow the conditional formatting as required.

![](<Base64-Image-Removed>)

In our case, we use the grey colour fill for the cells following the formula setup in conditional formatting:

![](<Base64-Image-Removed>)

Then in the Conditional Formatting Rules Manager, set up the area of the rule to be applied. In this case, we apply the rule to Columns **A** to **O**.

![](<Base64-Image-Removed>)

Click OK and you should now have the following:

![](<Base64-Image-Removed>)

With this method, we can easily locate the data as required.

See you next week for more VBA tips!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-dynamically-highlight-entire-row-and-column/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-dynamically-highlight-entire-row-and-column/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-dynamically-highlight-entire-row-and-column/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-dynamically-highlight-entire-row-and-column/#0)

[](https://sumproduct.com/blog/vba-blogs-dynamically-highlight-entire-row-and-column/#0 "close")

top