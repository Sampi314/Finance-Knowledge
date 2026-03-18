# Power Query: X Marks the Spot

**Source:** https://sumproduct.com/blog/power-query-x-marks-the-spot/

---

[Home](https://sumproduct.com/)

\> Power Query: X Marks the Spot

*   May 8, 2018

Power Query: X Marks the Spot
=============================

Power Query: X Marks the Spot
=============================

9 May 2018

_Welcome to our Power Query blog. This week, I look at a simple method to convert a check box into a name (next time I will move up a gear!)._

For this week’s task, the easiest way to explain what I am trying to achieve is with a ‘before and after’ example. I am going to start with this:

![](<Base64-Image-Removed>)

I have a simple table showing me my imaginary salespeople, and the benefits they have access to. However, instead of the x’s, I want to put the name of the benefit into the table, so I want to end up with this:

![](<Base64-Image-Removed>)

This is then much easier to manipulate and merge with other tables.

In this blog, I am going to look at a way to achieve this on a small scale, by adding new columns. Next time, I will look at a more complex version that will work for any number of columns.

I create my query using ‘From Table’ on the ‘Get and Transform’ section of the ‘Data’ tab:

![](<Base64-Image-Removed>)

I will use the ‘Add Column from Examples’ on the ‘Add Column’ tab.

![](<Base64-Image-Removed>)

I give myself the option of using any column, and start typing what I would like to see in a new version of the **_Car_** column.

![](<Base64-Image-Removed>)

It’s important to keep an eye on the formula at the top of the screen:

**Transform if \[Name\] = ‘Derek’ then ‘Car’ else if \[Name\] = ‘Mary’ then null else null**

This is clearly not what I want so I enter another example.

![](<Base64-Image-Removed>)

This is what I am looking for –

**Transform if \[#”Car”\] = “x” then “Car” else if \[#”Car”\] = null then null else null**

This is replacing my x’s with ‘Car’. I can either add all my columns in this way or use ‘Conditional Column’ and use the same idea for my other columns. An example of this alternative approach is shown below.

![](<Base64-Image-Removed>)

Having added all four new columns, I have my desired format.

![](<Base64-Image-Removed>)

I can delete my original columns from the ‘Home’ Tab using the ‘Remove Columns’ option.

![](<Base64-Image-Removed>)

I then rename my columns and ‘Close & Load’ the data to my Excel worksheet.

![](<Base64-Image-Removed>)

This is fine if I have four columns, but what if there are hundreds? Also, whilst this query can be refreshed if new employees join the company, what if new benefits are introduced? Next time, I will show a different method which will work for any number of columns…

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-x-marks-the-spot/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-x-marks-the-spot/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-x-marks-the-spot/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-x-marks-the-spot/#0)

[](https://sumproduct.com/blog/power-query-x-marks-the-spot/#0 "close")

top