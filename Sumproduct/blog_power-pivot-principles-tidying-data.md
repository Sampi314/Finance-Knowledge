# Power Pivot Principles: Tidying Data

**Source:** https://sumproduct.com/blog/power-pivot-principles-tidying-data/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Tidying Data

*   July 30, 2018

Power Pivot Principles: Tidying Data
====================================

Power Pivot Principles: Tidying Data
====================================

31 July 2018

_Welcome back to our Power Pivot blog. Today, we discuss potential steps we can take when we receive ‘messy’ data._

Before we begin, you can download our ‘messy’ data sample [here](https://sumproduct.com/assets/blog-pictures/2018/power-pivot/07-july/29/power-pivot-data-set-dirty-data.xlsx)
 and work along.

Using this data, after importing our data into Power Pivot, it looks something like this:

![](<Base64-Image-Removed>)

There are columns that are entirely blank, such as the **Suffix** and **AddressLine2** columns. Looking at the rows, some of them are completely blank too.

To eliminate blank rows and columns, we can filter the data before importing it to Power Pivot. If you forgot how to do this, head to the design tab on the Ribbon of the Power Pivot window, and select ‘Table Properties’.

![](<Base64-Image-Removed>)

We can then filter out the blank columns by choosing to not have them imported into the dataset:

![](<Base64-Image-Removed>)

To filter out the blank rows, we can choose a drop-down menu of one of the columns ‘Customer Name’ and unselect the ‘Blanks’ values.

![](<Base64-Image-Removed>)

Our dataset is now looking a lot better:

![](<Base64-Image-Removed>)

Looking closer, some entries in the **Customer Name** column have been entered incorrectly into the **Customer Group** column, together with a couple of errors in the **Customer Group** and **Email Address** columns.

We can fix these issues by ‘cleaning’ the data in Excel. Let’s utilise Power Pivot’s clipboard function. Select all (**CTRL + A**) and copy (**CTRL + C**) the table from Power Pivot and paste it (**CTRL + V**) into a sheet in Excel. Let’s perform a few more adjustments to the data, _et voilà_!

![](<Base64-Image-Removed>)

Obviously, it would make sense to perform the adjustments in Power Query or Power Pivot, but that’s not the point here…

Now how do we get this back into Power Pivot? First, convert the range into a Table. Highlight the range and press (**CTRL + T**), to convert it into a Table. Be sure to tick ‘My table has headers’.

![](<Base64-Image-Removed>)

Give the Table a name, then head up to the ‘Power Pivot’ tab on the Ribbon and select the ‘Add to Data Model’ option.

![](<Base64-Image-Removed>)

And there you have it, our data all cleaned up, back in Power Pivot.

![](<Base64-Image-Removed>)

Happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-tidying-data/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-tidying-data/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-tidying-data/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-tidying-data/#0)

[](https://sumproduct.com/blog/power-pivot-principles-tidying-data/#0 "close")

top