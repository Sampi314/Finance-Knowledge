# A to Z of Excel Functions: The PIVOTBY Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-pivotby-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The PIVOTBY Function

*   December 17, 2023

A to Z of Excel Functions: The PIVOTBY Function
===============================================

A to Z of Excel Functions: The PIVOTBY Function
===============================================

18 December 2023

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **PIVOTBY** function._

**The PIVOTBY function**

The **PIVOTBY** function allows you to create a summary of your data via a formula, akin to a formulaic [PivotTable](https://www.sumproduct.com/thought/pivotal-pivottables)
. It supports grouping along two axes and aggregating the associated values. For instance, if you had a table of sales data, you might generate a summary of sales by state and year.

It should be noted that **PIVOTBY** is a function that returns an array of values that can spill to the grid. Furthermore, at this stage, not all features of a PivotTable appear to be replicable by this function.

The syntax of the **PIVOTBY** function is:

**PIVOTBY(row\_fields,  
col\_fields, values, function, \[field\_headers\], \[row\_total\_depth\], \[row\_sort\_order\],  
\[col\_total\_depth\], \[col\_sort\_order\], \[filter\_array\])**

It has the following arguments:

*   **row\_fields:** this is required, and represents a column-oriented array or range that contains the values which are used to group rows and generate row headers. The array or range may contain multiple columns. If so, the output will have multiple row group levels

*   **col\_fields:** alsorequired, and represents a column-oriented array or range that contains the values which are used to group columns and generate column headers. The array or range may contain multiple columns. If so, the output will have multiple column group levels

*   **values:** this is also required, and denotes a column-oriented array or range of the data to aggregate. The array or range may contain multiple columns. If so, the output will have multiple aggregations

*   **function:** also required, this is an explicit or eta reduced lambda (_e.g._ **[SUM](https://www.sumproduct.com/thought/sum-things-to-consider)
    **, **[PERCENTOF](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-percentof-function)
    **, **[AVERAGE](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-average-function)
    **, **[COUNT](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-count-function)
    **) that is used to aggregate **values**. A vector of lambdas may be provided. If so, the output will have multiple aggregations. The orientation of the vector will determine whether they are laid out row- or column-wise

*   **field\_headers:** this and the remaining arguments are all optional. This represents a number that specifies whether the **row\_fields, col\_fields** and **values** have headers and whether field headers should be returned in the results. The possible values are:
    
    *   **Missing:** Automatic
    *   **0:** No
    *   **1:** Yes and don’t show
    *   **2:** No but generate
    *   **3:** Yes and show
    
    It should be noted that “Automatic” assumes the data contains headers based upon the **values** argument. If the first value is text and the second value is a number, then the data is assumed to have headers. Fields headers are shown if there are multiple row or column group levels
    

*   **rows\_total\_depth:** this optional argument determines whether the row headers should contain totals. The possible values are:
    
    *   **Missing**: Automatic, with grand totals and, where possible, subtotals
    *   **0:** No Totals
    *   ****1:****Grand Totals
    *   ****2:****Grand and Subtotals
    *   ****\-1:****Grand Totals at Top
    *   ****\-2:****Grand and Subtotals at Top
    
    It should be noted that for subtotals, **row\_fields** must have at least two \[2\] columns. Numbers greater than two \[2\] are supported provided **row\_fields** has sufficient columns
    

*   **rows\_sort\_order:** again optional, this argument denotes a number indicating how rows should be sorted. Numbers correspond with the columns in **row\_fields** followed by the columns in **values**. If the number is negative, the rows are sorted in descending / reverse order. A vector of numbers may be provided when sorting based upon only **row\_fields  
    **

*   **col\_total\_depth:** this optional argument determines whether the column headers should contain totals. The possible values are:
    
    *   **Missing**: Automatic, with grand totals and, where possible, subtotals
    *   **0:** No Totals
    *   ****1:****Grand Totals
    *   ****2:****Grand and Subtotals
    *   ****\-1:****Grand Totals at Top
    *   ****\-2:****Grand and Subtotals at Top
    
    It should be noted that for subtotals, **col\_fields** must have at least two \[2\] columns. Numbers greater than two \[2\] are supported provided **col\_fields** has sufficient columns
    

*   **col\_sort\_order:** again optional, this argument denotes a number indicating how rows should be sorted. Numbers correspond with the columns in **col\_fields** followed by the columns in **values**. If the number is negative, these are sorted in descending / reverse order. A vector of numbers may be provided when sorting based upon only **col\_fields**

*   **filter\_array:** the final optional argument, this represents a column-oriented one-dimensional array of Boolean values \[1, 0\] that indicate whether the corresponding row of data should be considered. It should be noted that the length of the array must match the length of **row\_fields** and **col\_fields**.

Similar in many ways to**[GROUPBY](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-groupby-function)
**, **PIVOTBY** is fairly straightforward to use. Consider the following Excel Table called **tbl**:

![](<Base64-Image-Removed>)

Consider the following formula:

**\=PIVOTBY(tbl\[Category\],tbl\[Year\],tbl\[Sales\],AVERAGE)**

![](<Base64-Image-Removed>)

You can get more imaginative and sort in descending order by the **AVERAGE** of **Rating**, _viz._

**\=PIVOTBY(tbl\[Item\],tbl\[Year\],tbl\[Rating\],AVERAGE,,,-2)**

![](<Base64-Image-Removed>)

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every other business day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-pivotby-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-pivotby-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-pivotby-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-pivotby-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-pivotby-function/#0 "close")

top