# ListColumn Swan Song

**Source:** https://sumproduct.com/thought/listcolumn-swan-song/

---

[Home](https://sumproduct.com/)

\> ListColumn Swan Song

*   January 19, 2018

ListColumn Swan Song
====================

VBA Blogs: ListColumn Swan Song
===============================

19 January 2018

This is the ninth blog in the series about using ListObjects to manipulate Tables within an Excel workbook in VBA. Today we will be featuring ListColumns.

Let’s start with the **Aria\_TopTen** table:

![](https://sumproduct.com/wp-content/uploads/2025/06/234da60c6a65177d93a71095cbdedd61.jpg)

Visually, it is clear that there are 3 columns in the table. **ListColumns** can be used to determine how many columns are in a table. This is done by using the **COUNT** method.

![](https://sumproduct.com/wp-content/uploads/2025/06/18d6df45970100a5cfe39b6a05b0e211.jpg)

The result is:

![](https://sumproduct.com/wp-content/uploads/2025/06/4fd363f83aac02f4a64c718e62f52bfb.jpg)

But what if one wanted to know what was the 2nd column in the table? Then the **Item** method can help impart that information.

![](https://sumproduct.com/wp-content/uploads/2025/06/23aecbeec29b9a5d38ccbc1e6ecbdf1e.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/1aae65cbeece7f78f959b0186633a0eb.jpg)

However, this is directly equivalent to using the **Cells** property of **HeaderRowRange** as examined in a previous blog [here](https://www.sumproduct.com/blog/article/vba-blogs/vba-header-ache)
.

Hope you enjoyed **ListColumns**, come back next time to **ListRows**!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/listcolumn-swan-song/#0)
    
*   [Register](https://sumproduct.com/thought/listcolumn-swan-song/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/listcolumn-swan-song/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/listcolumn-swan-song/#0)

[](https://sumproduct.com/thought/listcolumn-swan-song/#0 "close")

top