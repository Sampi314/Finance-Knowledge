# VBA Blogs: Header-ache

**Source:** https://sumproduct.com/blog/vba-blogs-header-ache/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Header-ache

*   December 21, 2017

VBA Blogs: Header-ache
======================

VBA Blogs: Header-ache
======================

22 December 2017

_The sixth in a series about using ListObjects to manipulate Tables within an Excel workbook in VBA featuring the Headers Range._

Let’s not get ahead of ourselves and examine our table.

![](https://sumproduct.com/wp-content/uploads/2025/05/ea4a2089e0c7897b86782d53642164f7.jpg)

Notice how our table has no header names? Excel has just given it the generic Column + # header name. How would one fix this in VBA? No need to bury your head in the sand, it’s no head-scratcher.

Go head-to-head with the _HeaderRowRange_ property of the _ListObject_. This can be used to retrieve the range of the header row.

![](https://sumproduct.com/wp-content/uploads/2025/05/78f38a616b76ecfe0f7bf79c071b8f3d.jpg)

With a cool head, this then can be accessed directly to change the name of the headers. The _Cells_ property can be used. Remember off the top of your head that _Cells_ uses (\[RowNumber\] , \[ColumnNumber\]) references – the column ordinality of the table will definite which header is changed.

Let’s run the following code and head toward a more meaningfully named table:

![](https://sumproduct.com/wp-content/uploads/2025/05/52d0483fc366da8fe9f8f2694799aa01.jpg)

Heads up! This is the result:

![](https://sumproduct.com/wp-content/uploads/2025/05/814416e890d3dd7e001dd809855b0b7d.jpg)

Success! But heads will roll if this table was sent out – “Drug Name” is a misnomer, using “Brand” name would be more accurate. If the column number is unknown, how does one rename the column? How do we make heads or tails about that?

Don’t knock your head against a brick wall, use the _Find_ method of _Range_ to find the cell address of a particular name in the Header list and then the column position. Then reference the cell directly in order to change the header.

![](https://sumproduct.com/wp-content/uploads/2025/05/d81330c04e145a7a7a7564c5637f3de4.jpg)

And tada! Hold your head up high to a correctly named table:

![](https://sumproduct.com/wp-content/uploads/2025/05/74d039e6e22ecd87e8ee227064e5bec2.jpg)

Working on tables head to toe, next week will be about the Totals Row on the other end of the Table.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-header-ache/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-header-ache/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-header-ache/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-header-ache/#0)

[](https://sumproduct.com/blog/vba-blogs-header-ache/#0 "close")

top