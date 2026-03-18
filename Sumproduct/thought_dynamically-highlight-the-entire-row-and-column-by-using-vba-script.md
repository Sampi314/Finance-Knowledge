# Dynamically Highlight the Entire Row and Column by Using VBA Script

**Source:** https://sumproduct.com/thought/dynamically-highlight-the-entire-row-and-column-by-using-vba-script/

---

[Home](https://sumproduct.com/)

\> Dynamically Highlight the Entire Row and Column by Using VBA Script

*   August 23, 2019

Dynamically Highlight the Entire Row and Column by Using VBA Script
===================================================================

VBA Blogs: Dynamically Highlight the Entire Row and Column by Using VBA Script
==============================================================================

23 August 2019

_Welcome back to the VBA blog. This week, we are going to expand our learning of how to highlight selected cells in a worksheet from last week’s article._

Last week, we have used both VBA script and conditional formatting to highlight the row and columns of selected cells. This week, we are going to create the VBA script to achieve the same effect as last week’s blog.

We would like to add highlight rows and columns for the dataset below:

![](https://sumproduct.com/wp-content/uploads/2025/06/e774d10cbbb9450fc45efbe51abdf434-716.jpg)

The result would look like this:

![](https://sumproduct.com/wp-content/uploads/2025/06/f32e5a15e2cf9c3e4d2d058458ce054d-823.jpg)

The first step is to add a new **SelectionChange** event in the target worksheet as described previously, together with some relevant variables.

Dim iColor As Integer

Then, we use the statement **On Error Resume Next**. As one of most used error-handling routines, it allows execution to continue despite a run-time error.

On Error Resume Next

We delete the current formatting in the cells of the target worksheet (If any) and assign the colour index to the variable **iColor**:

Cells.FormatConditions.Delete

iColor = 15

Then we use the **With** statement to locate the target cell’s entire row formatting. Here, we delete the target cell formatting, add format condition type parameter **xlExpression**, which specifies whether the conditional format is based on a cell value or an expression, and then assign the colour index to the target cell’s interior colour index.

With Target.EntireRow.FormatConditions

     .Delete

     .Add xlExpression, , “TRUE”

     .Item(1).Interior.ColorIndex = iColor

End With

Next, we apply the same coding logic to the target cell’s entire column formatting as the code indicated below:

With Target.EntireColumn.FormatConditions

     .Delete

     .Add xlExpression, , “TRUE”

     .Item(1).Interior.ColorIndex = iColor

End With

Combing all the lines of code together, we get this:

Private Sub Worksheet\_SelectionChange(ByVal Target As Range)

Dim iColor As Integer

On Error Resume Next

Cells.FormatConditions.Delete

iColor = 15

With Target.EntireRow.FormatConditions

     .Delete

     .Add xlExpression, , “TRUE”

     .Item(1).Interior.ColorIndex = iColor

     End With

With Target.EntireColumn.FormatConditions

     .Delete

     .Add xlExpression, , “TRUE”

     .Item(1).Interior.ColorIndex = iColor

     End With

End Sub

With this method, we can easily locate the data as required.

See you next week for more VBA tips!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/dynamically-highlight-the-entire-row-and-column-by-using-vba-script/#0)
    
*   [Register](https://sumproduct.com/thought/dynamically-highlight-the-entire-row-and-column-by-using-vba-script/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/dynamically-highlight-the-entire-row-and-column-by-using-vba-script/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/dynamically-highlight-the-entire-row-and-column-by-using-vba-script/#0)

[](https://sumproduct.com/thought/dynamically-highlight-the-entire-row-and-column-by-using-vba-script/#0 "close")

top