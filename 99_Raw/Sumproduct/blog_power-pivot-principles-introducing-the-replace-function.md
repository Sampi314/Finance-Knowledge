# Power Pivot Principles: Introducing the REPLACE Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-replace-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the REPLACE Function

*   September 23, 2019

Power Pivot Principles: Introducing the REPLACE Function
========================================================

Power Pivot Principles: Introducing the REPLACE Function
========================================================

24 September 2019

_Welcome back to our Power Pivot blog. Today, we look at the REPLACE function._

The **REPLACE** function is used in creating custom columns in the ‘Power Pivot for Excel’ window, to create new groupings or categories for datasets. The **REPLACE** function replaces part of a text string in each row in a column, based on the number of characters specified by the user, with a different text string.

The **REPLACE** function uses the following syntax to operate:

**REPLACE( <old\_text>, <start\_num>, <num\_characters>, <new\_text>)**

*   the **<old\_text>** parameter is the string of text that contains the characters that we want to replace, this can also be a reference to a column that contains text
*   the **<start\_num>** parameter is the position of the first character in the **<old\_text>** that we wish to replace with **<new\_text>**
*   the **<num\_chars>** parameter is the number of characters that we want to replace
*   the **<new\_text>** parameter is the text that is going to replace the **<old\_text>**.

Let’s move on to an example. This week, we are going to use the following extremely complicated dataset:

![](<Base64-Image-Removed>)

Picture that an intern has accidentally typed in “AB” in front of all the product names, instead of “New”. Sure, we can fix this in Excel, but let’s do it in DAX. We can use the **REPLACE** function in DAX to create a calculated column that will correct this step.

After adding the data table to our data set in Power Pivot, we can create a calculated column with the following DAX function:

\=REPLACE(ProductTable\[Product Name\],1,2, “New”)

As a side note, we have entered ‘1’ as the **<start\_num>** as “AB” is in the first character position in the “AB Gloves” text string. If we wanted to replace “Gloves”we would specify ‘4’ as the **<start\_num>**: this is because we count each letter and blank in the text string as a character position.

![](<Base64-Image-Removed>)

Problem solved! The **REPLACE** function works well with replacing text strings “AB” that all begin in the same spot in the text field. What if the AB was at the end of the text string?

![](<Base64-Image-Removed>)

We can specify the **<start\_num>** as ‘8’ since “AB” begins on the eighth character position in “Gloves AB”.

\=REPLACE**(**ProductTable3\[Product Name\],8,2, “New”**)**

However, this does not work very well as AB begins in different positions in each row, _viz._

![](<Base64-Image-Removed>)

Stay tuned! We will revisit this problem in a future blog!

That’s it for this week, tune in next week for more Power Pivot! Until then, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-replace-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-replace-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-replace-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-replace-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-replace-function/#0 "close")

top