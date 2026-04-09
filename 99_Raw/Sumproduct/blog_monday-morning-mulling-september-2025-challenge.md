# Monday Morning Mulling: September 2025 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-september-2025-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: September 2025 Challenge

*   September 29, 2025

Monday Morning Mulling: September 2025 Challenge
================================================

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend.  On the Monday, we publish a solution.  If you think there is an alternative answer, feel free to email us.  We’ll feel free to ignore you._

**_The Challenge_**

This month’s Final Friday Fix invited you to return select data from a larger data table.  For example, we provided the following larger table:

![](<Base64-Image-Removed>)

The aim was that when values were typed into the **ID No.** assumption cells below, the table would populate using just one formula typed into the top left-hand corner of the range, _viz._

![](<Base64-Image-Removed>)

Where values cannot be found, the results should have returned blank cells as pictured above. 

To assist, we provided an original question file [here](https://sumproduct.com/wp-content/uploads/2025/09/SP-Returning-Select-Data-Challenge.xlsx)
.

The requirements were as follows:

*   the formula needed to be in just one cell (no “helper” cells)
*   this was a formula challenge; no Power Query / Get & Transform or VBA!

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/wp-content/uploads/2025/09/SP-Returning-Select-Data-Suggested-Solution.xlsx)
, which shows our suggested solution.

![](<Base64-Image-Removed>)

Please note the cell references in order to understand the rest of our solution.

First, we will use the [**INDEX**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/)
 function and need a version of Excel that supports dynamic arrays.  This is necessary for the results to “spill”.  For the **array** argument, we refer to the original table labelled **Data**.  For the **row** argument, use the following formula:

> **MATCH(D26:D30,Data\[ID No.\],0)**

The [**MATCH**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-match-function/)
 function returns a row number by matching these two components:

*   **D26:D30** is the range for the IDs whose data you want to return (the input **ID No.** values)
*   **Data\[ID No.\]** is the field of the IDs in the original table, **Data**.

You should note that the optional **match\_type** is zero \[0\] meaning it will return the first exact match.

The [**INDEX**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/)
 function will use the row number to return the appropriate row of data, in this case, the rows will spill.  For the third argument of the [**INDEX**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/)
 function, **column**, instead of using another **MATCH** formula (we know the order of columns), we will “simply” use the following:

> **SEQUENCE(1,COUNTA(Data\[#Headers\]))**

where:

*   **Data\[#Headers\]** is the range of headers in the provided data table, **Data**
*   [**COUNTA**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-counta-function/)
     counts the number of headers in the provided data table, **Data**
*   [**SEQUENCE**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-sequence-function/)
     spills out column counters based upon the number of headers in the provided data table, **Data**.

In some cases, if there is no match between any proposed IDs and the IDs in the original provided data table, this formula will return an error.  To ensure all errors are replaced with blank text (**“”**), we will use the [**INDEX**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/)
 function nested within an [**IFNA**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-ifna-function/)
 function.

With both the row and column parameters defined and errors handled, the correct data can be returned.  However, there will be an extra ID column produced, as written.  We can remove this with the use of the [**DROP**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-drop-function/)
 function where:

*   the **array** argument is the [**INDEX**](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-index-function/)
     calculation above
*   the **rows** argument is zero \[0\]
*   the **columns** argument is one \[1\].

With that, we can arrive at the final solution:

![](<Base64-Image-Removed>)

This is the full formula:

> **\=IFNA(DROP(INDEX(Data,MATCH(D26:D30,Data\[ID No.\],0),SEQUENCE(1,COUNTA(Data\[#Headers\]))),,1),””)**
> 
> _The Final Friday Fix will return on Friday 31 October 2025 with a new Excel Challenge.  In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-september-2025-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-september-2025-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-september-2025-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-september-2025-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-september-2025-challenge/#0 "close")

top