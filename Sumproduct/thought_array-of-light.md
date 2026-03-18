# Array of Light

**Source:** https://sumproduct.com/thought/array-of-light/

---

[Home](https://sumproduct.com/)

\> Array of Light

*   May 14, 2025

Array of Light
==============

Providing an overview of array formulae in Excel.

Array of Light
==============

This article provides a basic introduction to array formulae using a simple problem as an example. By Liam Bastick, director with SumProduct Pty Ltd.

Query
-----

A data file has been created with two columns, dates and data, viz.

![](<Base64-Image-Removed>)

Dates Challenge

Is there a simple formula to put in cell G12 (yellow cell) which will return the most recent date at which the corresponding data was less than or equal to the value in the ‘Target’ cell (cell G14)?

It can be assumed that there will be at most one data point for each date, but the dates may not necessarily be in ascending order. The ideal formula should take into account what happens if no date meets the criterion.

Advice
------

To be a successful solution, the formula had to allow for dates out of order and provide a meaningful output (i.e. not “0”) if there was no solution.

Ignoring the error trap requirement, possible solutions include:

*   An array function, e.g. **\={MAX(IF($G$18:$G$40<=$G$14,$F$18:$F$40))}**
*   Database functions by building a “criteria table” (sic) and using **\=DMAX(database,field,criteria)** (I plan to explain DFunctions in March’s column)
*   SUMPRODUCT, e.g. **\=SUMPRODUCT(MAX($F$18:$F$40\*($G$18:$G$40<=$G$14)))**
*   INDEX, e.g. **=MAX(INDEX((F18:F40)\*(G18:G40<=G14),))**
*   Including an extra column to identify dates that met the criteria, then finding the most recent date using the **MAX()** function.

Typical solutions are provided in the [attached Excel file](https://sumproduct.com/assets/user-upload/sp-simple-array-example.xls)
.

Common mistakes included using the **LOOKUP()** function (this requires the dates to be in strict ascending order), getting the inequality the wrong way round and forgetting the error trap.

In summary, to solve this problem, you needed to find the most recent (biggest) date out of a list of dates that met a particular condition: one viable option is to consider an **array**.

### Arrays

In Excel, an array is a contiguous set of items in a single row (called a one-dimensional horizontal array or “vector”), or in a single column (a one-dimensional vertical vector), or in a table consisting of at least two rows and two columns (a two-dimensional array). If you need more dimensions, you are better served with relational databases such as MS Access.

Array formulae perform multiple calculations on one or more of the items in an array. Array formulae can return either multiple outputs or a single result. There are two types:

*   Formulae that work with an array or series of data and aggregate it, typically using **SUM()**, **AVERAGE()**, **MIN()**, **MAX()** or **COUNT()**, to return a single value to a single cell. Microsoft calls these **single cell array formulae**
*   Formulae that return a result in to two or more cells (there are various formulae that will do this including **MINVERSE()**, **LINEST()** and **TRANSPOSE()**). These types of array formulas return an array of values as their result and are referred to as **multi-cell array formulae**.

Some functions, such as **SUMPRODUCT()**, **INDEX()** and **OFFSET()** will allow you to work with an array in a single cell by just pressing **ENTER**. However, Excel often needs to know you are working with an array formula, and this is performed by entering the formula using **CTRL + SHIFT + ENTER**. This will result in the formula appearing in braces ({}). These braces cannot be typed in.

Array formulae allow you to perform tasks that would require multiple cells otherwise (hence some readers used an additional column).

Our problem requires working with a list to return a single value, i.e. using a single cell array formula on a column vector.

Let’s consider the most common right answer (excluding the error trap):

\={MAX(IF($G$18:$G$40<=$G$14,$F$18:$F$40))}

The central formula, **IF($G$18:$G$40<=$G$14,$F$18:$F$40)**, checks to see which data is less than or equal to the target value **($G$14)** and returns the corresponding dates (otherwise it provides a default value of FALSE since the **value\_if\_false** in the **IF(logical\_test,\[value\_if\_true\],\[value\_if\_false\])** syntax is not defined).

Hence we get an array in the form **{Date\_1,FALSE,FALSE,Date\_2,…}**. **MAX()** simply takes the largest value, i.e. the most recent date – easy!

### Problems with Arrays

Multi-cell formulae can cause problems as the range of cells to hold your results must be selected before you enter the formula. Once entered, the contents of an individual cell in a multi-cell array formula cannot be edited and / or deleted.

End users may not understand your array formulae. How many basic Excel users would understand the **MAX(IF)** array explained above? Advanced users will all too often use an array function when there are simpler, easier to understand alternatives.

Large array formulae can slow down calculations significantly. Worse still, they can simply stop calculating with no error message provided.

In conclusion, array formulae can be very powerful but they should be used sparingly.

If you have a query for this section, please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)
 or visit the website [www.sumproduct.com](https://www.sumproduct.com/)

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/array-of-light/#0)
    
*   [Register](https://sumproduct.com/thought/array-of-light/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/array-of-light/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/array-of-light/#0)

[](https://sumproduct.com/thought/array-of-light/#0 "close")

top