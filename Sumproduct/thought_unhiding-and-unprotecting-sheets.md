# Unhiding and Unprotecting Sheets

**Source:** https://sumproduct.com/thought/unhiding-and-unprotecting-sheets/

---

[Home](https://sumproduct.com/)

\> Unhiding and Unprotecting Sheets

*   April 21, 2017

Unhiding and Unprotecting Sheets
================================

VBA Blogs: Unhiding and Unprotecting Sheets
===========================================

21 April 2017

Today, we’re going to look at a common application of VBA involving a range of skills that we’ve gone through. We are going to create a VBA script that will look through all the sheets of a workbook and unhide the worksheets, unprotect them if necessary, and unhide the columns and rows. This is useful to help identify the entirety of a file.

The first step involves declaring a Worksheet variable. We can do this with the code:

Dim ws as Worksheet

We can then loop through all of the worksheets using the following loop:

For Each ws in ActiveWorkbook.Sheets

…

Next ws 

Inside the loop, each worksheet will be defined by the variable “ws”. With this, we can perform additional commands, such as:

ws.Visible = xlSheetVisible

ws.Activate

ws.Unprotect

ws.Rows.EntireRow.Hidden = False

ws.Columns.EntireColumn.Hidden = False

Hopefully all of these lines of code make logical sense! If not, they perform the following actions:

*   Unhide the relevant sheet
*   Select and activate the sheet
*   Unprotect the sheet if it is protected
*   Take all of the rows and unhide them
*   Take all of the columns and unhide them

To put the whole piece of code together, it would look like the following:

Sub UnhideAll()

Dim ws As Worksheet

For Each ws In ActiveWorkbook.Sheets

    ws.Visible = xlSheetVisible

    ws.Activate

    ws.Unprotect

    ws.Rows.EntireRow.Hidden = False

    ws.Columns.EntireColumn.Hidden = False

Next ws

End Sub

Next week is the Final Friday Fix for April, but the following week, we will look at what happens if we run into an error when the code is being run, and how we can modify this routine to handle those errors. Happy Friday!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/unhiding-and-unprotecting-sheets/#0)
    
*   [Register](https://sumproduct.com/thought/unhiding-and-unprotecting-sheets/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/unhiding-and-unprotecting-sheets/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/unhiding-and-unprotecting-sheets/#0)

[](https://sumproduct.com/thought/unhiding-and-unprotecting-sheets/#0 "close")

top