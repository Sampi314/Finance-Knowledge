# Monday Morning Mulling: June 2022 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-june-2022-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: June 2022 Challenge

*   June 26, 2022

Monday Morning Mulling: June 2022 Challenge
===========================================

Monday Morning Mulling: June 2022 Challenge
===========================================

27 June 2022

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

The challenge this month was to calculate the running total despite the filter. Easy, yes?

**_The Challenge_**

The issue this month may be common and useful for anyone who uses Excel to produce cumulative/running total reports frequently. You can download the original question file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/June/sp-running-total---challenge.xlsx)
.

This month’s challenge was to write a **formula** on a new column of the provided table to calculate the running total of column Number regardless of whether the Excel Table (_i.e._created using **Insert -> Table** or **CTRL + T**) is filtered or not. The result should look like the column Total generated on the right _(below)_:

![](<Base64-Image-Removed>)

As always, there were some requirements:

*   the formula needed to be within just one column (no “helper” cells)
*   this was a formula challenge; no Power Query / Get & Transform or VBA!
*   the formula still calculated the correct running total when the table was _filtered_.

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/June/sp-running-total---suggested-solution.xlsx)
 which demonstrates our suggested solution.

Normally, we would think of using **SUM** to sum up the range from the top row to current row to calculate the running total. However, the result will not be adjusted if the table is filtered, especially if the first row goes walkabout.

Hence, we think of using an Excel function that ignores any rows that are not included in the result of a filter. That function is [**SUBTOTAL**](https://www.sumproduct.com/thought/subtotal-function-and-functionality)
.

Firstly, the current row of column Number can be easily identified using the Table reference as below.

**\[@Number\]**

You may recall the **@**symbol denotes the implicit intersection and literally means the value of the ‘Number’ field for the row you are on.

Secondly, we can easily select a range from the top row to current row and anchor the top row reference. However, it is not dynamic enough when a top row can be added or deleted. Therefore, we use [**INDEX**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-index-function)
 to find the top cell of the ‘Number’ field as follows.

**INDEX(\[Number\],1)**

As you may know, **INDEX** returns not only a value but also a cell reference. This means you can use it along with a colon “:” to refer to a range of cells. The range that we need for the running total is as follows:

**INDEX(\[Number\],1):\[@Number\]**

Finally, we then use **SUBTOTAL** to generate the running total. **SUBTOTAL** ignores all filtered rows regardless of which function number in the first argument is used.

**\=SUBTOTAL(9,INDEX(\[Number\],1):\[@Number\])**

The number nine \[9\] represents the **SUM** function including hidden rows while number 109 works similarly but ignores hidden rows. These hidden rows need to be caused by either hiding or grouping (not filtering). Depending upon your purpose for the running total, you can choose which number to use.

_The Final Friday Fix will return on Friday 29 July 2022 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-june-2022-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-june-2022-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-june-2022-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-june-2022-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-june-2022-challenge/#0 "close")

top