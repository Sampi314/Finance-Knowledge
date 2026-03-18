# Monday Morning Mulling: February 2022 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-february-2022-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: February 2022 Challenge

*   February 27, 2022

Monday Morning Mulling: February 2022 Challenge
===============================================

Monday Morning Mulling: February 2022 Challenge
===============================================

28 February 2022

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

The challenge this month was to spill a range of cells that unpivot some last columns of an array. Easy, yes?

**_The Challenge_**

Sometimes, when you work with pivoted data that has a structure similar to a PivotTable, it is difficult to look up a value based on multiple column and row criteria. To make it simpler, we usually unpivot the data. Most of the time, you may choose to use [Unpivot Columns](https://sumproduct.com/blog/power-query-painless-unpivoting/)
 function in Power Query.

This challenge was designed to make you think outside the box to find another way using only Excel formulas. You can download the question file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/feb/sp-unpivoting-columns---challenge.xlsx)
.

This month’s challenge was to write a **formula in one cell** using [Dynamic Arrays](https://sumproduct.com/news/getting-arrays-spilling-the-beans-on-seven-new-functions/)
 that would spill a range of cells to unpivot only the last three \[3\] columns (_i.e._**x**, **y** and **z**) of the array in the file above. The result should look like the array generated on the right _(below)_:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-60-1.jpg)

As always, there were some requirements:

*   the formula needed to be in just one cell (no “helper” cells)
*   this was a formula challenge; no Power Query / Get & Transform or VBA!
*   the formula needed to be flexible, so that if we adjusted the number of rows and / or columns of the input table, the formula should still work
*   obviously, the numbers of rows / columns of the output table could not exceed the row / column limitations of Excel.

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/feb/sp-unpivoting-columns---suggested-solution.xlsx)
 which demonstrates our suggested solution. However, before explaining our solution, we will clarify how we came up with it first.

**_Brainstorming_**

Firstly, inputs of the formula include:

*   **Data** table in the question
*   number of columns that will not be unpivoted, which is two \[2\] (_i.e._**Col 1** and **Col 2**). We name it as **ColstoKeep**.

Therefore, the number of columns to unpivot is three \[3\], which is calculated as below. We name this number as **UCols**.

**\=COLUMNS(Data\[#All\]) – ColstoKeep**

Secondly, we need to consider some features (_e.g_. numbers of rows and columns) of the output array. After we unpivot the table, they should be calculated as below:

*   Number of rows: 9

**\=(ROWS(Data\[#All\]) – 1) \* UCols**

*   Number of columns: 4. The output table will include the first two \[2\] columns of initial table and two \[2\] additional columns for the old Row Headers (_i.e._**x**, **y** and **z**) and Values (_i.e._ numbers in **Data** table in this case).

**\=ColstoKeep + 2**

Thirdly, to create a Dynamic Range for the output, we need the help of [**INDEX**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/)
 and [**SEQUENCE**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sequence-function/)
.

The row and column index numbers of output need to be created by **SEQUENCE** as follows. We will call them **RowID** and **ColID**.

*   **RowID**:

**\=SEQUENCE((ROWS(Data\[#All\]) – 1) \* UCols)**

*   **ColID**:

**\=SEQUENCE(1, ColstoKeep + 2)**

![](<Base64-Image-Removed>)

Additionally, we need to identify row and column positions of the Values in **Data**. We will call them **Ro** and **Col**.

For example, number ‘**7**‘ is located on row 2 and column 4 of **Data**.

*   **Ro**:

**\=ROUNDUP(RowID/UCols,0)+1**

*   **Col**:

**\=MOD(RowID-1,UCols)+1+ColstoKeep**

![](<Base64-Image-Removed>)

Finally, the trick of this challenge is to use **ColID** with an [**IF**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-if-function/)
 statement _(below)_ as a connector for three different **INDEX** functions, _i.e._

“_If_**ColID** is less than or equal to **ColstoKeep**, _then_ get the first two \[2\] columns of **Data**,

_else if_**ColID** is equal to **ColstoKeep** \+ 1, _then_ get the Row Header of unpivoted columns of **Data**,

_else_ get the Values of **Data**.”

The result is as follows:

![](<Base64-Image-Removed>)

**_Returning to the Suggested Solution_**

You may wonder why the challenge only allows a formula cell when there are several working steps above. Our solution is a combination of all described steps above within a [**LET**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-let-function/)
 formula as follows:

**\=LET(Tbl, Data\[#All\],**

 **ColstoKeep, 2,**

 **UCols, COLUMNS(Tbl)-ColstoKeep,**

 **RowID, SEQUENCE((ROWS(Tbl)-1)\*UCols),**

 **ColID, SEQUENCE(1,ColstoKeep+2),**

 **Ro, ROUNDUP(RowID/UCols,0)+1,**

 **Col, MOD(RowID-1,UCols)+1+ColstoKeep,**

**IF(ColID<=ColstoKeep,INDEX(Tbl,Ro,ColID), IF(ColID=ColstoKeep+1,INDEX(Tbl,1,Col), INDEX(Tbl,Ro,Col))))**

There are seven \[7\] variables:

*   **Tbl** is an input table to unpivot
*   **ColstoKeep** is the number of first columns you do not want to unpivot
*   **UCols** is the number of unpivoted columns
*   **RowID** and **ColID** are row and column indices of the output table
*   **Ro** and **Col** are initial row and column positions of Values in the input table.

Then, the final part of the formula is the calculation to unpivot the last three \[3\] columns, _viz._

![](<Base64-Image-Removed>)

Although it is a long and complex formula, you can apply it to your input table by only replacing the values of **Tbl** and **ColstoKeep**.

_The Final Friday Fix will return on Friday 25 March 2022 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-february-2022-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-february-2022-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-february-2022-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-february-2022-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-february-2022-challenge/#0 "close")

top