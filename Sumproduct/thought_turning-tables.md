# Turning Tables

**Source:** https://sumproduct.com/thought/turning-tables/

---

[Home](https://sumproduct.com/)

\> Turning Tables

*   November 20, 2017

Turning Tables
==============

VBA Blogs: Turning Tables
=========================

20 November 2017

_“Hello”, this is the second in a series about using ListObjects to manipulate Tables within an Excel workbook in VBA._

**Warning! This was written whilst listening to an Adele playlist…**

“Rumour Has It” that last time, how to convert a Range into a Table object using VBA was discussed. But “Hello”, what if the table already is in the workbook? How to get access to the “One and Only”?

Let’s look at the table in the workbook.

![](<Base64-Image-Removed>)

The \_correct\_ way to reference a table is to use the following codes. Let’s create a variable so that VBA can “Take It All” from the table to work with.

![](<Base64-Image-Removed>)

This works very well if there is “One and Only” table on the worksheet and if the subroutine/function is called from the worksheet that the table is on. If there are multiple tables on the worksheet, how would one check that the right one is being referenced? One would get “Tired” trying to figure it all out.

A better way to reference it by using the Table and Worksheet Names.

![](<Base64-Image-Removed>)

However it “Can’t Let Go” using the sheet reference and the table might move around the workbook or the sheet might be renamed. “All I Ask” is to avoid using the Sheet as a reference. Saving the “Best for Last”, this can be done by using **Range** in conjunction with Range’s **ListObject** property. Tables are also defined Named Ranges in the Excel dictionary. The Name Manager will also include all Tables that are in the Workbook so don’t go “Rolling in the Deep” trying to find all the Tables!

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

So now having found the “Remedy”, the Table can be referenced directly from VBA! There will be problems “Now and Then” when referring to a Named Range that isn’t actually a Table so some error checking code would be appropriate.

I’m going to “Make You Feel My Love” by going through the ListObject properties next time, so for not “That’s It, I Quit, I’m Moving On”.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/turning-tables/#0)
    
*   [Register](https://sumproduct.com/thought/turning-tables/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/turning-tables/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/turning-tables/#0)

[](https://sumproduct.com/thought/turning-tables/#0 "close")

top