# Having a Row

**Source:** https://sumproduct.com/thought/having-a-row/

---

[Home](https://sumproduct.com/)

\> Having a Row

*   February 9, 2018

Having a Row
============

VBA Blogs: Having a Row
=======================

9 February 2018

_This is the eleventh blog in the series about using **ListObjects** to manipulate Tables within an Excel workbook in VBA. Today we will be looking at all the commonalities between **ListColumns** and **ListRows** on the **Item** level._

**ListColumns** and **ListRows** are very similar. There are no properties that are unique specifically to **ListRows**. The methods and properties that apply to **ListRows** is strictly a subset of the properties that apply to **ListColumns**.

![](https://sumproduct.com/wp-content/uploads/2025/06/7cc4a392f179a3149ce9bcf42812bd14.jpg)

The methods and properties that are in common with **ListColumns(Index)** and **ListRows(Index)** ignoring the those covered [last week](https://www.sumproduct.com/blog/article/vba-blogs/vba-blog-same-same-but-different-introducing-listrows)
 are:

*   **Delete:** deletes the specified column/row
*   **Index:** returns the index number of the column/row referenced. This might be useful is because columns can actually be referred by their header names. Let’s look at an example to see how using the **Index** property might be useful. This is “MyTable”.

![](https://sumproduct.com/wp-content/uploads/2025/06/438ad6d264987daceb3995e558586c10.jpg)

Running the following code to get the index value of column with the header “A” would result with a value of 1 as expected:

![](https://sumproduct.com/wp-content/uploads/2025/06/30041be3048d48a3213c28902959c29b.jpg)

*   An alternative use for **Index** is when data is being processed through loops and one would like to know the specific row or column that it would be in (detailed example to follow at the end)

*   **Range:** This returns the Range object referenced by its address (and applications thereof). However, note this includes the _Header_ of the column, because the header is considered part of the column.

Which row has number 5 in column “B”?

The following code has been run:

![](<Base64-Image-Removed>)

This is obviously a very simplistic example given that returning **iCounter** would have netted the same result. However, if subsections of records through nested loops are used, using **Index** to return what column or row that matches specific criteria can be very powerful.

This concludes **ListRows** so next time, let’s look at the things that are unique to **ListColumns**.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/having-a-row/#0)
    
*   [Register](https://sumproduct.com/thought/having-a-row/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/having-a-row/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/having-a-row/#0)

[](https://sumproduct.com/thought/having-a-row/#0 "close")

top