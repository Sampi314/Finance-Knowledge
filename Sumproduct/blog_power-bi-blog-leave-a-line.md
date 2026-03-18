# Power BI Blog: Leave a Line

**Source:** https://sumproduct.com/blog/power-bi-blog-leave-a-line/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Leave a Line

*   July 21, 2021

Power BI Blog: Leave a Line
===========================

Power BI Blog: Leave a Line
===========================

22 July 2021

_Welcome back to this week’s edition of the Power BI blog series. This week, we will look at how to leave a blank line in a Matrix visualisation._

[Last week](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-draw-a-line)
, I had a simple table of accounting data, which I created a Matrix for:

![](<Base64-Image-Removed>)

I used a measure which I called **asterisk**

\*  = ” “

to create a line in my Matrix.

![](<Base64-Image-Removed>)

Today, I have imported rental data into a new table called **Rent**:

![](<Base64-Image-Removed>)

I want to include a calculation based upon this data in the same Matrix I created [last week](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-draw-a-line)
. I have created a relationship between the **Rent** and **Accounts** tables:

![](<Base64-Image-Removed>)

In this very simple example, I can use a 1 to 1 relationship using the **Month** field.

![](<Base64-Image-Removed>)

I can create a new measure to work out the **Net Rental Income**:

![](<Base64-Image-Removed>)

**Net Rental Income = CALCULATE(SUM(Rent\[Rental Income\]) – SUM(Rent\[Overheads\]))**

This is very similar to the **Profit** measure I created [last week](https://www.sumproduct.com/blog/article/power-bi-tips/power-bi-blog-draw-a-line)
. Now I can add **Rental Income,****Overheads** and **Net Rental Income** to my Matrix. I include the **asterisk** measure before **Net Rental Income** to insert a line.

![](<Base64-Image-Removed>)

There are a couple of changes I want to make to the formatting. Now I have more lines, I would prefer to see the line all the way across to the row names. I can do this in the Formatting pane in the ‘Field formatting’ section for the **asterisk** measure.

![](<Base64-Image-Removed>)

If I toggle ‘Apply to header’ to On, then the line is extended for both occurrences of my **asterisk** measure:

![](<Base64-Image-Removed>)

This is looking better, but I’d like to leave a gap between **Profit** and **Rental Income**. I can do this by creating another measure:

![](<Base64-Image-Removed>)

“” = ” “

I will refer to this as the **blank** measure. I add the **blank** measure to my Matrix.

![](<Base64-Image-Removed>)

I have a space, but it’s a bit thin. I can just add more **blank** measures until I am happy with the gap.

![](<Base64-Image-Removed>)

This gives me a gap I am happy with. For this Matrix, I want the font and background colour of the **blank** measure to be white, but this will depend upon the formatting chosen for each Matrix.

![](<Base64-Image-Removed>)

I can now add a **Total Net Income** measure.

![](<Base64-Image-Removed>)

**Total Net Income = \[Profit\] + \[Net Rental Income\]**

I add this to my Matrix and format it with more **asterisk** and **blank** measures. I also alter the background in the ‘Field formatting’ section of the Formatting tab for each field to give my Matrix a more balanced appearance.

![](<Base64-Image-Removed>)

Check back next week for more Power BI tips and tricks!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-leave-a-line/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-leave-a-line/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-leave-a-line/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-leave-a-line/#0)

[](https://sumproduct.com/blog/power-bi-blog-leave-a-line/#0 "close")

top