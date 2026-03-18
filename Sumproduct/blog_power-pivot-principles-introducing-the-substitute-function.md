# Power Pivot Principles: Introducing the SUBSTITUTE Function

**Source:** https://sumproduct.com/blog/power-pivot-principles-introducing-the-substitute-function/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Introducing the SUBSTITUTE Function

*   September 30, 2019

Power Pivot Principles: Introducing the SUBSTITUTE Function
===========================================================

Power Pivot Principles: Introducing the SUBSTITUTE Function
===========================================================

1 October 2019

_Welcome back to our Power Pivot blog. Today, we look at the SUBSTITUTE function._

Last week, we looked at the **REPLACE** function and how it can be used to replace part of a string of text in a column. However, we ran into a problem when we wanted to replace a string of text that existed in different positions in each row. For example, if consider the following dataset:

![](<Base64-Image-Removed>)

In this scenario we want to replace “AB” with “New”. Notice that the positions of “AB” in “Gloves AB” and “Vest AB” differ; “AB” is in the eighth character position in “Gloves AB” and is in the sixth character position in “Vest AB”. In “Gloves AB”, we count each letter as a character position (including blanks), hence why “AB” is in the eighth character position. When we create the following measure to replace “AB” with “New” using the **REPLACE** function:

\=REPLACE**(**ProductTable3\[Product Name\],8,2, “New”**)**

we end up with this result:

![](<Base64-Image-Removed>)

This is because the **REPLACE** function doesn’t necessarily ‘look’ for “AB”; it just replaces the old text starting from the specified starting character position.

Cue the **SUBTITUTE** function.

Before we use the **SUBSTITUTE** function, we must understand how it works. The **SUBSTITUTE** function, like the **REPLACE** function, replaces existing text with new text in text strings in every row in a column. The **SUBSTITUTE** function is usually used to create calculated columns.

The **SUBSTITUTE** function uses the following syntax to operate:

**SUBSTITUTE(<text>, <old\_text>, <new\_text>, <instance\_num>)**

*   the **<text>** parameter is the string of text that contains the characters that we want to substitute; this can also refer to a column that contains text
*   the **<old\_text>** parameter is the string of text that we want the function to look for in the **text>** parameter
*   the **<new\_text>** parameter is the text string that is going to replace the **<old\_text>**.
*   the **<instance\_num>** is the instance which we want the **<old\_text>** to be replaced by the **<next\_text>** parameter if there are multiple **<old\_text>** strings found.

Going back to the dataset mentioned earlier, we can now use the **SUBSTITUTE** function to create the following measure:

\=SUBSTITUTE(\[Product Name\],”AB”,”New”,1)

![](<Base64-Image-Removed>)

The **SUBSTITUTE** function has been able to replace all the “AB” text values with “New” without being affected by the different character locations.

Let’s investigate the **<instance\_num>** parameter. Here, we’ve added another entry to our dataset:

![](<Base64-Image-Removed>)

Using the same DAX formula:

![](<Base64-Image-Removed>)

Only the first instance of “AB” has been replaced in position six (6) of our dataset. This is because we specified ‘1’ as our **<instance\_num>**. If we change the **<instance\_num>** to ‘2’ we get:

![](<Base64-Image-Removed>)

The **SUBSTITUTE** function now only replaces the second instance of “AB” it finds and ignores the first and last instance. Keep this in mind when using the **SUBSTITUTE** function: changing the **<instance\_num>** we specify which instance of the **<old\_text>** we want to substitute.

That’s it for this week, tune in next week for more Power Pivot! Until then, happy pivoting!

Stay tuned for our next post on Power Pivot in the [Blog](https://www.sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [\>here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles in the meantime, you can find all of our past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-introducing-the-substitute-function/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-introducing-the-substitute-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-introducing-the-substitute-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-introducing-the-substitute-function/#0)

[](https://sumproduct.com/blog/power-pivot-principles-introducing-the-substitute-function/#0 "close")

top