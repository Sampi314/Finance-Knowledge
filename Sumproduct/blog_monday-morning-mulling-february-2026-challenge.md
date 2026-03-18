# Monday Morning Mulling: February 2026 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-february-2026-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: February 2026 Challenge

*   March 2, 2026

Monday Morning Mulling: February 2026 Challenge
===============================================

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend.  On the Monday, we publish a solution.  If you think there is an alternative answer, feel free to email us.  We’ll feel free to ignore you._

**_The Challenge_**

This month’s Final Friday Fix was the second of six \[6\] instalments on the fundamentals of collecting and sorting data.  It challenged you to find the top three \[3\] and bottom three \[3\] ranked fruits, including ties, according to their total quantities. 

Provided was a scattered list of fruits and quantities:

![](https://sumproduct.com/wp-content/uploads/2026/03/image-7.png)

Whilst we did have a tie for second place [last month](https://sumproduct.com/blog/final-friday-fix-january-2026-challenge/)
, we did not consider ties explicitly.  That was the point of this month’s challenge.

![](https://sumproduct.com/wp-content/uploads/2026/03/image.png)

An input was provided for Top / Bottom **N**.

![](https://sumproduct.com/wp-content/uploads/2026/02/image-2.png)

You can download the original question file [here](https://sumproduct.com/wp-content/uploads/2026/02/SP-Top-N-Challenge-2-Challenge.xlsx)
.

There are solutions for versions of Excel that support dynamic arrays and for those that do not.  For those that do, there was a specific requirement:

*   the formula needed to be calculated in just one cell (no “helper” cells).

Otherwise, for both solutions:

*   no Power Query / Get & Transform or VBA!

**_**_**_Suggested Solution: Modern Excel (Microsoft 365, Excel Online, etc.)_**_**_**

You can find our Excel file [here](https://sumproduct.com/wp-content/uploads/2026/02/SP-Top-N-Challenge-2-Solution.xlsx)
, which shows our suggested solution.

For those with dynamic arrays, if you have completed last month’s challenge and just want to see how ties are included, you may skip to the [**INDEX**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/)
 and [**FILTER**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-filter-function/)
 section of the explanation.

First, we will use the [**GROUPBY**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-groupby-function/)
 function to transform the data into a desirable form:

******\=GROUPBY(Data\[Fruit\],Data\[Quantity\],SUM,,0,-2,Data\[Quantity\]<>””,)******

It should be noted that:

*   [**GROUPBY**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-groupby-function/)
    collects the fruit name and corresponding quantities and sums them to give a total quantity value for each fruit
*   then, with zero \[0\] in the **total\_depth** argument, it omits the default total quantity of all fruits row
*   it also sorts the data based upon the second column in descending order, achieved by inputting -2 \[negative two\] in the **sort\_order** argument.  The two \[2\] specifies the column number to base the sort on (in this case, the quantity column) and the negative sign specifies descending order
*   For the logical test in the **filter\_array** argument, a simple expression is used, _i.e_. keep any row in the end output where the quantity is not blank.

The final [**GROUPBY**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-groupby-function/)
 function produces a spilled array of fruits with corresponding total quantities:

![](<Base64-Image-Removed>)

Next, [**LET**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-let-function/)
 is used to simplify the formula expression, so it is easier to follow.  Therefore, with [**LET**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-let-function/)
 as the parent function, we provide a variable name in the first argument, here ‘**group**’, then in the second argument we use the [**GROUPBY**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-groupby-function/)
 function:

******\=LET(group,GROUPBY(Data\[Fruit\],Data\[Quantity\],SUM,,0,-2,Data\[Quantity\]<>””,)******

For returning the desired values, we start with typing a comma and entering another variable name, ‘**groupvalues**’.  Then, we enter the [**INDEX**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/)
 function.  This will allow us to specify the second column (the **Quantity** column) of the created **group** array.

*   For the **array** argument, enter the variable name **group**
*   for the **row\_num** argument, leave blank
*   and for the **column\_num** argument, enter the column number which is two \[2\]

**\=LET(group, GROUPBY(Data\[Fruit\],Data\[Quantity\],SUM,,0,-2,Data\[Quantity\]<>””,),  
groupvalues, INDEX(group,,2), …)**

Then, in the next argument of the [**LET**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-let-function/)
 function, enter the [**FITLER**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-filter-function/)
 function.  For the **array** argument, enter the variable name **group**.  For the **include** argument, type this calculation:

****groupvalues>=LARGE(groupvalues,N)****

_It should be noted that:_

*   **groupvalues** is the variable name given to the **Quantity** column
*   the [**LARGE**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-large-function/)
     function, with **groupvalues** as the array, allows us to return the **Nth** highest value, in this case the third highest quantity
*   the greater than and equal to operators create parameters, it returns any sum in the **Quantity** column that are greater than or equal to the third highest value of that same column.

Therefore, instead of just returning the top three \[3\] values, this formula configuration returns for all applicable values (including ties):

**\=LET(group, GROUPBY(Data\[Fruit\],Data\[Quantity\],SUM,,0,-2,Data\[Quantity\]<>””,),  
groupvalues, INDEX(group,,2),  
FILTER(group,groupvalues>=LARGE(groupvalues,N)))**

![](<Base64-Image-Removed>)

To find the bottom three \[3\], simply use the [**SMALL**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-small-function/)
 function, instead of the [**LARGE**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-large-function/)
 function, and switch the operator in the [**FITLER**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-filter-function/)
 function from greater than “**\>**” to less than “**<**”.

**_Suggested Solution: Legacy Version_**

First, create a PivotTable by clicking **Insert -> PivotTable -> Table/Range**, referencing the entire table range in the dialog box.  Then, clean, organise and return the desired values through a series of steps:

1.  Sort the values by right clicking inside the ‘Sum of Quantity’ column of the PivotTable, then going to **Sort -> Sort Largest to Smallest**
2.  Omit the grand total row by clicking **Design** **\-> Grand Totals -> Off for Rows and Columns**
3.  Only return the top three \[3\] values, including ties, by clicking on the filter dropdown button **->** **Value Filters** **\-> Top 10** and then changing ten \[10\] to three \[3\] in the **Show** dialog.

   The filter dropdown button is shown:

![](<Base64-Image-Removed>)

   And here is the **Show** dialog box:

![](<Base64-Image-Removed>)

This will return the top three \[3\] values including ties:

![](<Base64-Image-Removed>)

To find the bottom three \[3\] including ties, change ‘Top’ to ‘Bottom’ in the **Show** dialog box.  Also, since there is a blank value that will be included in the top three \[3\], change three \[3\] to four \[4\].  These alterations will produce the desired result:

![](<Base64-Image-Removed>)

Note that PivotTable filter functionality only accepts either top/bottom **N** filter or omitting specific table values using the tick/untick boxes.  As a result, blank rows have been left in.

It’s not perfect, and in some versions of Excel, the PivotTable(s) will need to be manually refreshed if the data changes, but it is a simple alternative.

_The Final Friday Fix will return on Friday 27 March 2026 with a new Excel Challenge.  In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-february-2026-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-february-2026-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-february-2026-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-february-2026-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-february-2026-challenge/#0 "close")

top