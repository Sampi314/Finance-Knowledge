# VBA Blogs: ListColumn

**Source:** https://sumproduct.com/blog/vba-blogs-listcolumn/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: ListColumn

*   January 11, 2018

VBA Blogs: ListColumn
=====================

VBA Blogs: ListColumn
=====================

12 January 2018

Welcome back to our VBA blog series. This is the eighth blog in the series about using ListObjects to manipulate Tables within an Excel workbook in VBA. Today we will be featuring ListColumns.

The ListColumns property allows us to manipulate columns within a table. Say we have the following table, with the table name of ‘Table1’:

![](<Base64-Image-Removed>)

We can select a specific column in a table using the following code in VBA:

Dim Tbl As ListObject

Set Tbl = Range(“Table1”).ListObject

Tbl.ListColumns(1).Range.Select 

Or if we just want the data in a specific column we can use this VBA code:

Set Tbl = Range(“Table1”).ListObject

Tbl.ListColumns(1).DataBodyRange.Copy 

From here we can copy and paste the column with this code (but being a devoted reader of our VBA blogs, you already know how to do this

![](<Base64-Image-Removed>)

That’s not the only thing we can do with ListColumns; we can also add columns. The following VBA code will insert a column at the end of the table:

Set Tbl = Range(“Table1”).ListObject

Tbl.ListColumns.Add

![](<Base64-Image-Removed>)

Furthermore, we can specify exactly where we want the new column by adding “Position: =2” at the end of the previous code:

Tbl.ListColumns.Add Position:=2

Our example table now looks like this:

![](<Base64-Image-Removed>)

Remember these codes alone are trivial at best, but combine them with other properties or functions and the sky is the limit!

That’s all for now, join us next week on our [blog page](https://www.sumproduct.com/blog)
 for more on VBA! Alternatively, if you’re hungry for more VBA now, [here](https://www.sumproduct.com/thought/vba-blog-series)
 is a page with all of our past VBA blogs.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-listcolumn/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-listcolumn/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-listcolumn/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-listcolumn/#0)

[](https://sumproduct.com/blog/vba-blogs-listcolumn/#0 "close")

top