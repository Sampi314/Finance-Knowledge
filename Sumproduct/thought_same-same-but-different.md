# Same Same But Different

**Source:** https://sumproduct.com/thought/same-same-but-different/

---

[Home](https://sumproduct.com/)

\> Same Same But Different

*   February 2, 2018

Same Same But Different
=======================

VBA Blogs: Same Same But Different
==================================

2 February 2018

_This is the tenth blog in the series about using **ListObjects** to manipulate Tables within an Excel workbook in VBA. Today we will be reviewing **ListColumns** and how it applies to **ListRows**._

**ListColumns** can be really confusing. Using **ListColumns** references ALL the columns, but using **ListColumns(Index)** which references a specific column.

Remember, in VBA, one can press “.” and the applicable method/properties that apply to that object comes up? This is what can be done with **ListColumns**:

![](https://sumproduct.com/wp-content/uploads/2025/06/cd07ee4f4dcad7ae5bf8cd92bb0f8c9f.jpg)

*   **Add**: lets us add a column. By default it will be added at the end of the table
*   **Application:** returns the name of the application from which the object belongs to (in this case Excel)
*   **Count:** returns the number of columns
*   **Creator:** returns the name of the author of the object
*   **Item** returns the column as an object. **ListColumns.Item(Index)** is identical to using **ListColumns(Index)** in terms of referencing a specific column
*   **Parent** returns the overall owner of the object, in this case, being “MyTable”.

All of these things are identical in **ListRows** rows. Simply interchange column in the above list with row!

Notice how there is no **Delete** property here and is done on a row/column indexed basis. This is because invoking delete would either delete your entire data set (on **ListRows**) or the entire table (on **ListColumns**). If that is indeed what one wishes to do, then using **DataBodyRange** or **ListObject** table itself would be more intuitive and understandable.

Come back next week to look at the properties of individual rows/columns.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/same-same-but-different/#0)
    
*   [Register](https://sumproduct.com/thought/same-same-but-different/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/same-same-but-different/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/same-same-but-different/#0)

[](https://sumproduct.com/thought/same-same-but-different/#0 "close")

top