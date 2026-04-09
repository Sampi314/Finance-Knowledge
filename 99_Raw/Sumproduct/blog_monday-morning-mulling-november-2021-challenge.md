# Monday Morning Mulling: November 2021 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-november-2021-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: November 2021 Challenge

*   November 28, 2021

Monday Morning Mulling: November 2021 Challenge
===============================================

Monday Morning Mulling: November 2021 Challenge
===============================================

29 November 2021

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

This month, we wanted you to generate a list of duplicates from the original list containing a mix of “real” numbers, numbers with leading zeros, and numbers in text strings. Easy, yes?

**_The Challenge_**

Numbers with leading zeroes may sometimes cause problems. In order to find duplicates from a list, you might think of using [**FILTER**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-filter-function)
 with [**COUNTIF**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-countif-function)
. However, **COUNTIF** cannot distinguish between numbers with and without leading zeroes, or “real” numbers and numbers stored as text or else in text format.

As you can see below, the number of occurrences of each number is calculated incorrectly by **COUNTIF**:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-102.jpg)

Therefore, this challenge was trickier than it may have first appeared. You can download the number list [here](https://sumproduct.com/assets/blog-pictures/2021/fff-mmm/nov/fff/sp-list-of-duplicates---question.xlsm)
.

This month’s challenge was to write a **formula in one cell** using [Dynamic Arrays](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
 that would spill down to generate a list of duplicates (_i.e_. all numbers that show up more than once) from the number list in the file above. The result had to be similar to the list on the right _(below)_:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-138.jpg)

As always, there were some requirements:

*   the formula should be in just one cell (no “helper” cells)
*   it should treat these kinds of numbers differently:
    *   with and without leading zeros
    *   “real” numbers as opposed to text strings
*   this was a formula challenge – no Power Query / Get & Transform or VBA!

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2021/fff-mmm/nov/mmm/sp-list-of-duplicates---suggested-solution.xlsm)
 which demonstrates our suggested solution.

When finding duplicates, you may think of some of the following common ways:

*   [**COUNTIF**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-countif-function)
     / [**COUNTIFS**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-countifs-function)
    
*   [**SUMPRODUCT**](https://www.sumproduct.com/thought/multiple-criteria)
    
*   [**EXACT**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-exact-function)
    
*   [conditional formatting](https://www.sumproduct.com/thought/conditional-formatting)
     to highlight duplicates
*   _etc._

However, after we had tried all the options above, we realised that they could not meet the requirements of the question.

For example, if we use Dynamic Arrays with **COUNTIF**, the result may be wrong. As numbers 12 and 123, and string “012” only show up once in the list, they should not be considered as duplicates.

![](<Base64-Image-Removed>)

Before explaining our solution, we will clarify how we came up with it first.

**_Brainstorming_**

The aim was to count the number of occurrences of each number in the list to check whether those numbers were considered as duplicates or not.

Firstly, we think of using a matrix with:

*   **x axis** being the Number list (_i.e_. **G12#**) with the help of **TRANSPOSE**
*   **y axis** being its unique list (_i.e._**F13#**) with the help of **UNIQUE**
*   counting only numbers from the unique list is enough.

You can read more about **TRANSPOSE** and **UNIQUE** in this [blog](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
.

The values in the matrix will be 1 (TRUE) or 0 (FALSE) depending on whether numbers on the **y** axis show up on the **x** axis (_i.e._ the number list) or not.

![](<Base64-Image-Removed>)

Secondly, we need to sum up each row of the matrix to get the frequency each number show up.

As you may know, we cannot use **SUM** with Dynamic Arrays to calculate each row’s result as it will aggregate the result of _all_ rows. Hence, we will apply a trick with the **MMULT** function _(see below)_ to multiply the matrix above by a matrix containing only number ones \[1’s\]

The second matrix is created by **SEQUENCE** which you can also read more about in a [blog](https://www.sumproduct.com/thought/creating-a-calendar-with-dynamic-arrays)
 we have written previously. The number of rows of this matrix needs to be the same as the number of columns of the first matrix above. The formula is as follows:

**\=SEQUENCE(COLUMNS(G13#),,,0)**

![](<Base64-Image-Removed>)

The syntax of the **MMULT** function is as below. It will return the matrix product of two specified arrays or matrices:

**\=MMULT(array1, array2)**

Hence, we will get a result matrix on column **R** below, which is a list of the number of occurrences.

![](<Base64-Image-Removed>)

Finally, we just need to use the [**FILTER**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-filter-function)
 function to remove all the numbers which only occur once.

**\=FILTER(F13#,R13#>1)**

![](<Base64-Image-Removed>)

**_Returning to the Suggested Solution_**

You may wonder why the challenge only allows a formula cell while there are quite a number of working steps above.

Our solution is a combination of all steps above within a [**LET**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-let-function)
 formula as follows:

**\=LET(List,Number\[List\],matrix,(UNIQUE(List)=TRANSPOSE(List))+0, FILTER(UNIQUE(List),MMULT(matrix,SEQUENCE(ROWS(List),,,0))>1))**

There are two variables, namely **List** and **matrix**. **List** is the original number list in the question, whereas **matrix** is the first matrix to calculate the number of occurrences. Then, the final part of the formula is the calculation to get the list of duplicates, _viz._

![](<Base64-Image-Removed>)

Although it is a long and complex formula, you can apply it to your own list by only replacing the value (_i.e_. **Number\[List\]**) of the variable **List**.

See you next month!

_The Final Friday Fix will return on Friday 31 December 2021 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-november-2021-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-november-2021-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-november-2021-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-november-2021-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-november-2021-challenge/#0 "close")

top