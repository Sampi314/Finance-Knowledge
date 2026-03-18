# Monday Morning Mulling: December 2021 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-december-2021-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: December 2021 Challenge

*   January 2, 2022

Monday Morning Mulling: December 2021 Challenge
===============================================

Monday Morning Mulling: December 2021 Challenge
===============================================

3 January 2022

_Happy New Year! On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

The special challenge this month was to spill a range of cells that vertically appends two input arrays. Easy, yes?

**_The Challenge_**

Sometimes, you may need to append separate tables into one big table. To solve this, you may choose to manually copy and paste one table below another or use a more advanced way in Power Query, _i.e_. [Append Queries](https://sumproduct.com/blog/power-query-appending-files/)
.

This challenge was designed to make you think outside the box to find another way using only Excel formulas. You can download the question data [here](https://sumproduct.com/assets/blog-pictures/2021/fff-mmm/dec/fff/sp-appending-arrays---challenge.xlsx)
.

This month’s challenge was to write a **formula in one cell** using [Dynamic Arrays](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
 that would spill a range of cells to vertically append **two arrays** in the file above. The input tables in the question were different, but the result should look similar to the array generated on the right _(below)_:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-84.jpg)

As always, there were some requirements:

*   the formula needed to be in just one cell (no “helper” cells)
*   this was a formula challenge; no Power Query / Get & Transform or VBA!
*   the formula needed to be flexible, so that if we adjusted the number of rows and / or columns of the two input tables, the formula should still work
*   obviously, the numbers of rows / columns of the output table could not exceed the row / column limitations of Excel.

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2021/fff-mmm/dec/mmm/sp-appending-arrays---suggested-solution.xlsx)
 which demonstrates our suggested solution. However, before explaining our solution, we will clarify how we came up with it first.

**_Brainstorming_**

Firstly, we need to consider some features (_e.g_. numbers of rows and columns) of the output array. In the question, **Table 1** has five \[5\] rows and two \[2\] columns, whereas **Table 2** has four \[4\] rows and three \[3\] columns.

As the two tables are to be combined vertically, the number of rows and columns of the output should be calculated as below:

*   Number of rows: 9

**\=ROWS(Table1) + ROWS(Table2)**

*   Number of columns: 3

**\=MAX(COLUMNS(Table1), COLUMNS(Table2))**

Secondly, to create a Dynamic Range for the output, we need the help of [**INDEX**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/)
 and [**SEQUENCE**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sequence-function/)
.

The row and column index numbers of **INDEX** need to be created by **SEQUENCE** as follows. We will call them **rowIndex** and **colIndex**.

![](<Base64-Image-Removed>)

Therefore, when we apply the combination of **INDEX** and **SEQUENCE** to **Table 1**, the result will look as below.

![](<Base64-Image-Removed>)

Finally, when appending two items, we need to think of something as a connector. For example, in order to attach two papers together, you may need a piece of tape, a staple or a paper clip.

Regarding this challenge, the trick here is to use **rowIndex** with a simple [**IF**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-if-function/)
 statement _(below)_ as a connector, _i.e._

“_If_**rowIndex** is less than or equal to the number of rows of **Table 1**, _then_ get **Table 1** _else_ get **Table 2**.”

The **rowIndex** numbers of **Table2** used in **INDEX** function need to restart with one \[1\], so that they are calculated a little bit differently from those of **Table1**, using the formula below:

![](<Base64-Image-Removed>)

After applying this connector, we will get the result as follows:

![](<Base64-Image-Removed>)

You can see that we obtain some _#REF!_ errors, since there is no value of **Table 1** in the third column. These are easily fixed by adding an [**IFERROR**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-iferror-function/)
 function outside the **IF** statement to replace the resulting errors with blanks (**“”**).

![](<Base64-Image-Removed>)

**_Returning to the Suggested Solution_**

You may wonder why the challenge only allows a formula cell when there are a number of working steps above. Our solution is a combination of all of the described steps above within a [**LET**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-let-function/)
 formula as follows:

**\=LET(array1,Table1,**

**array2,Table2,**

**colIndex,SEQUENCE(,MAX(COLUMNS(array1),COLUMNS(array2))),**

**rowIndex,SEQUENCE(ROWS(array1)+ROWS(array2)),**

**IFERROR(IF(rowIndex<=ROWS(array1),INDEX(array1,rowIndex,colIndex),INDEX(array2,rowIndex-ROWS(array1),colIndex)),””))**

There are four variables, namely **array1**, **array2**, **colIndex** and **rowIndex**:

*   **array1** and **array2** are the two input tables in the question
*   **colIndex** and **rowIndex** are the index numbers of columns and rows of the output array.

Then, the final part of the formula is the calculation to vertically append two input arrays, _viz._

![](<Base64-Image-Removed>)

Although it is a long and complex formula, you can apply it to your input tables by only replacing the values of **array1** and **array2**. Moreover, you can use the similar trick to append arrays horizontally instead of vertically or append more than two arrays. Feel free to think outside the box and create your own megaformulae.

Happy New Year 2022!

_The Final Friday Fix will return on Friday 28 January 2022 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-december-2021-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-december-2021-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-december-2021-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-december-2021-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-december-2021-challenge/#0 "close")

top