# VBA Blogs: Can’t Row with a Column

**Source:** https://sumproduct.com/blog/vba-blogs-cant-row-with-a-column/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Can’t Row with a Column

*   February 15, 2018

VBA Blogs: Can’t Row with a Column
==================================

VBA Blogs: Can’t Row with a Column
==================================

16 February 2018

_This is the twelfth blog in the series about using **ListObjects** to manipulate Tables within an Excel workbook in VBA. Today let’s look at the unique properties of **ListColumn**._

Whilst doing some research to eloquently explain the difference between rows and columns – came across this quote:

![](<Base64-Image-Removed>)

There are a few things can be done with **ListColumn** that are not possible with **ListRow** due to the nature of how one thinks to store data. Think of each row as a _record_ in a database or an item. There can be unlimited number of records as data is added. Columns are the _fields_ of data which are defined. They are attributes of the record storing a single piece of information in relation to that item. The column is the structure of your data whereas the row is the data itself.

The properties that are unique to **ListColumn** are as follows:

*   **DataBodyRange:** Remember that **Range** refers to the whole column including the header. This returns just the information in the column under the header, the data portion of the table
*   **Name:** returns the name stored in the Header of the column
*   **Total:** returns the value in the Totals Row. Note, the table must have a total otherwise it will return the following error as it is looking for an object that does not exist:

![](<Base64-Image-Removed>)

*   **TotalsCalculation:** this gives the ability to change the type of calculation in the Totals Row which was previously covered in a [previous article](https://www.sumproduct.com/blog/article/vba-blogs/vba-blog-total-eclipse-of-the-heart)
    
*   **XPath:** XPath gives the ability to change the XPath information stored about the table. XPath uses path expressions to select nodes or node-sets in an XML document. XML is designed to manage and share structured data. Using **XPath** in VBA, one can manipulate the structure and tags in order to format in a certain way for importing/exporting between applications. This is outside the scope of this blog and a basic primer about XPath can be found [here](https://www.w3schools.com/xml/xpath_intro.asp)
     as well as an overview how XML works in Excel [here](https://support.office.com/en-us/article/overview-of-xml-in-excel-f11faa7e-63ae-4166-b3ac-c9e9752a7d80)
    

That wraps up **ListColumns** and **ListRows** and concludes the distinct ranges in a table! Check back next week for our series on Loops!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-cant-row-with-a-column/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-cant-row-with-a-column/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-cant-row-with-a-column/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-cant-row-with-a-column/#0)

[](https://sumproduct.com/blog/vba-blogs-cant-row-with-a-column/#0 "close")

top