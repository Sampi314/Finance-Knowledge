# Dynamically Highlight the Row

**Source:** https://sumproduct.com/thought/dynamically-highlight-the-row/

---

[Home](https://sumproduct.com/)

\> Dynamically Highlight the Row

*   August 9, 2019

Dynamically Highlight the Row
=============================

VBA Blogs: Dynamically Highlight the Row
========================================

9 August 2019

_Welcome back to the VBA blog! This week we are going to expand our learning of how to highlight selected cells in a worksheet from last week._

Today, we are going to use the joint effort of VBA script and conditional formatting to highlight the row of selected cells. It is useful when we have a large dataset and wish to check the data of specific rows. This VBA project will highlight the row of selected cell and easy for user to locate the data.

We would like to add highlight rows for the dataset below:

![](<Base64-Image-Removed>)

and the result would be like this:

![](<Base64-Image-Removed>)

The first step is to add a new **SelectionChange** event in the target worksheet.

In VBA IDE, choose the target worksheet (**Sheet1 (Test)** in this case) and select Worksheet and **SelectionChange** options as highlighted below.

![](<Base64-Image-Removed>)

The editor will create a Private Sub-procedure automatically. In the coding area, we create a new named range ActiveRow to the workbook. This new named range refers to the active cell by selection in a dynamic way.

Private Sub Worksheet\_SelectionChange(ByVal Target As Range)

ThisWorkbook.Names.Add “ActiveRow”, ActiveCell.Row

End Sub

Then for the next step, go to the conditional formatting Ribbon and add a new rule. We use a formula to determine the cells to format. In the formula input, write the function

“=**ROW**()=**ActiveRow**”.

The role of this function is to determine if the active row is the same as the row of current selection. If so, the row will follow the conditional formatting as required.

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

*   [Log in](https://sumproduct.com/thought/dynamically-highlight-the-row/#0)
    
*   [Register](https://sumproduct.com/thought/dynamically-highlight-the-row/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/dynamically-highlight-the-row/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/dynamically-highlight-the-row/#0)

[](https://sumproduct.com/thought/dynamically-highlight-the-row/#0 "close")

top