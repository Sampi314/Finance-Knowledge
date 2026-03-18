# Deleting Specific Rows

**Source:** https://sumproduct.com/thought/deleting-specific-rows/

---

[Home](https://sumproduct.com/)

\> Deleting Specific Rows

*   September 13, 2019

Deleting Specific Rows
======================

VBA Blogs: Deleting Specific Rows
=================================

13 September 2019

_Welcome back to the VBA blog. This week, we are going to learn how to use VBA to delete specific rows._

Today we are going to create VBA script to delete rows with even numbers in an example ID field automatically. It is a useful method to conduct data ETL (extracting, transforming and loading) for the specific format of a data table.

Essentially, we would like to delete the records with even number in the ID field:

![](<Base64-Image-Removed>)

The result would look like this:

![](<Base64-Image-Removed>)

The first step is to define relevant variables. We defined two variables **lngRow** and **i**

Dim lngRow As Long

Dim i As Long

Then, we locate the last row of data in column **A** and assign the value to variable “**lngRow**”.

lngRow = Range(“A” & Rows.Count).End(xlUp).Row

We then use an ‘If’ statement to determine the value used for next loop.

This requires ‘Mod’ which determines the remainder when a value is divided by a divisor. For example, the ‘Mod’ of the value five (5) using the divisor three (3) is the remainder two (2) – that is. 5 / 3 = 1 r 2. Therefore, if the ‘Mod’ value of **lngRow** with divisor two (2) equals to 0 (_i.e._ it is an even number), then the value of **lngRow** is further reduced by one (1).

If lngRow Mod 2 = 0 Then

   lngRow = lngRow – 1

End If

After this step, we use the ‘for loop’ to start from the row determined by variable “**lngRow**” and loop through backward to row 2 with step -2. This would help to locate the row with even number of ID as shown in the data table and then delete the entire row.

For i = lngRow To 2 Step -2

        Rows(i).Delete

Next i

Combing all the lines of code together, we get this:

Sub DeleteRows()

    Dim lngRow As Long

    Dim i As Long

    lngRow = Range(“A” & Rows.Count).End(xlUp).Row

    If lngRow Mod 2 = 0 Then

        lngRow = lngRow – 1

    End If

    For i = lngRow To 2 Step -2

        Rows(i).Delete

    Next i

End Sub

By using this method, we can delete the specific row based on rules without manual and repetitive operation.

See you next week for more VBA tips!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/deleting-specific-rows/#0)
    
*   [Register](https://sumproduct.com/thought/deleting-specific-rows/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/deleting-specific-rows/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/deleting-specific-rows/#0)

[](https://sumproduct.com/thought/deleting-specific-rows/#0 "close")

top