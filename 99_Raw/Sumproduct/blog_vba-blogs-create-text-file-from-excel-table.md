# VBA Blogs: Create text file from Excel table

**Source:** https://sumproduct.com/blog/vba-blogs-create-text-file-from-excel-table/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Create text file from Excel table

*   July 4, 2019

VBA Blogs: Create text file from Excel table
============================================

VBA Blogs: Create text file from Excel table
============================================

5 July 2019

_Welcome back to the VBA blog! This week we are going to expand on our blog from last week, relating to file path selectors._

Today, we are going to create a VBA script that will create a text file based on a specific table in the Excel workbook. This is useful to create text templates for a range of purposes, such as uploading data into databases and other systems that only accept text files.

We would like to save the following table (**Table1**) in Excel:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-400.jpg)

to a text file as below. More specifically, we want to generate a text file with the same content as listed in the Excel table above and insert blank rows between lines with different descriptions in Memo column. Also. We want to keep the structure of the Excel table unchanged:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-413.jpg)

The first step involves declaring relevant variables.

Dim filename As String, lineText As String

Dim myrng As Range

Dim i, j

Then, we define the file path in the local drive where we want the text file to be saved. The code “ThisWorkbook.path” defines the file path for the current workbook and we use this file path as the root directory for the text file. The code “Worksheets(“Product Table”).Name” defines the name of the text file to be saved.

filename = ThisWorkbook.path & “” & Worksheets(“”Product Table””).Name & “”.txt””

The next line of code sets up the output file and gives a file number for the output file. The file number allows us to distinguish between the different output files if we have more than one output text file.

Open filename For Output As #1

Then

*   [Log in](https://sumproduct.com/blog/vba-blogs-create-text-file-from-excel-table/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-create-text-file-from-excel-table/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-create-text-file-from-excel-table/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-create-text-file-from-excel-table/#0)

[](https://sumproduct.com/blog/vba-blogs-create-text-file-from-excel-table/#0 "close")

top