# VBA Blogs: Deleting Error Values

**Source:** https://sumproduct.com/blog/vba-blogs-deleting-error-values/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Deleting Error Values

*   October 3, 2019

VBA Blogs: Deleting Error Values
================================

VBA Blogs: Deleting Error Values
================================

4 October 2019

_Welcome back to the VBA blog. This week, we are going to learn how to delete error values using VBA._

Today we are going to create a VBA script to delete error values in specific ranges. It is a useful method for the data extraction, transformation and loading (ETL) process(es) in some cases.

Essentially, we have a data set _(as shown below)_, let’s imagine we want to delete all the error values automatically:

![](<Base64-Image-Removed>)

Removing the grid lines, the result would look like this:

![](<Base64-Image-Removed>)

The first step is to define two range variables.

Dim myrng As Range

Dim mycell As Range

Set the range of data table to variable **myrng** as shown below:

Set myrng = Range(“A1:E15”)

Then we use the ‘For loop’ to loop through each cell and use the **IsError** property to determine if the value in the cell is an error. If the value is an error, then the value is set to blank:

For Each mycell In myrng

    If VBA.IsError(mycell.Value) = True Then

        mycell.Value = “”

    End If

Next

The final step is to set variable to nothing:

Set myrng = Nothing

Set mycell = Nothing

Combing all the lines of code together, we get this:

Sub DeleteError()

Dim myrng As Range

Dim mycell As Range

Set myrng = Range(“A1:E15”)

For Each mycell In myrng

    If VBA.IsError(mycell.Value) = True Then

        mycell.Value = “”

    End If

Next

Set myrng = Nothing

Set mycell = Nothing

End Sub

By using this method, we can delete error values in a data set automatically.

See you next week for more VBA tips!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-deleting-error-values/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-deleting-error-values/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-deleting-error-values/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-deleting-error-values/#0)

[](https://sumproduct.com/blog/vba-blogs-deleting-error-values/#0 "close")

top