# Monday Morning Mulling: May 2025 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-may-2025-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: May 2025 Challenge

*   June 2, 2025

Monday Morning Mulling: May 2025 Challenge
==========================================

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend.  On the Monday, we publish a solution.  If you think there is an alternative answer, feel free to email us.  We’ll feel free to ignore you._

**_The Challenge_**

[Last Friday’s challenge](https://www.sumproduct.com/blog/article/fff-mmm/final-friday-fix-may-2025-challenge)
 invited you to create a PivotTable that provides the date of the month only when displaying dates, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/06/image-29.png)

to this:

![](https://sumproduct.com/wp-content/uploads/2025/06/image-30.png)

A Table (called **Inputs**) was provided containing a set of dates and sales you may use to create your PivotTable:

![](https://sumproduct.com/wp-content/uploads/2025/06/image-31.png)

You can download the original question file [here](https://www.sumproduct.com/assets/blog-pictures/2022/fff-mmm/2025/May/sp-pivottable-date-formatting---challenge.xlsx)
. 

These were the challenge guidelines, you could:

*   use PivotTables only
*   not use conditional formatting
*   not use Excel formulae
*   not use VBA, Office Scripts or any other programming code.

**_Suggested Solution_**

You can find our Excel file [here](https://www.sumproduct.com/assets/blog-pictures/2022/fff-mmm/2025/May/sp-pivottable-date-formatting---suggested-solution.xlsx)
.  which shows our suggested solution.  The steps are detailed below.

This Final Friday Fix sounded simple.  However, as you might have already realised, finding the right feature within Excel to complete even simple tasks can sometimes be tricky.

First, we need to construct the PivotTable.  Select any cell in the ‘Data’ table, then go to the Insert tab and click the PivotTable icon:

![](<Base64-Image-Removed>)

…and press OK:

![](https://sumproduct.com/wp-content/uploads/2025/06/image-33.png)

You will see the PivotTable Fields pane on the right-hand side.  Drag the ‘Date’ field (red) into Columns and the ‘Sales’ field (blue) into Values:

![](https://sumproduct.com/wp-content/uploads/2025/06/image-34-493x1024.png)

This will be the result, showing both the PivotTable Fields and the constructed PivotTable:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

(Some versions of Excel will automatically replicate the numerical formatting of the source data.  The version used above did not, but it is easy to change the Vales number formatting – that is not the challenge!!)

Now, on the PivotTable Fields pane, click on the ‘Date’ heading under Columns. Click on ‘Field Settings…’ and then ‘Number Format’ in the ‘Field Settings’ dialog box:

![](<Base64-Image-Removed>)

Then click on Custom:

![](<Base64-Image-Removed>)

…and change the current date formatting (d/mm/yyyy) under Type to just ‘d’:

![](<Base64-Image-Removed>)

Then click OK and OK again.

![](<Base64-Image-Removed>)

which will produce the desired date format, only displaying the day:

![](<Base64-Image-Removed>)

The trick here is to format the ‘Date’ field.  If you select a different field, the formatting will not “stick” – hence the challenge.

This concludes this month’s challenge.  Sometimes, Excel can feel like a maze to navigate even for simple tasks, luckily, we’re here to help!

_The Final Friday Fix will return on Friday 27 June 2025 with a new Excel Challenge.  In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-may-2025-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-may-2025-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-may-2025-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-may-2025-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-may-2025-challenge/#0 "close")

top