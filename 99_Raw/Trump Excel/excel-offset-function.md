# Excel OFFSET Function | Formula Examples + FREE Video

**Source:** https://trumpexcel.com/excel-offset-function

---

[Skip to content](https://trumpexcel.com/excel-offset-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-offset-function/#below-title)

Excel OFFSET Function (Example + Video)
---------------------------------------

![Excel OFFSET Function](https://trumpexcel.com/wp-content/uploads/2014/03/OFFSET-FORMULA-EXCEL.png)

### When to use Excel OFFSET Function

Excel OFFSET function can be used when you want to get a reference which offsets specified number of rows and columns from the starting point.

### What it Returns

It returns the reference that OFFSET function points to.

### Syntax

\=OFFSET(reference, rows, cols, \[height\], \[width\])

### Input Arguments

*   **reference –** The reference from which you want to offset. This could be a cell reference or a range of adjacent cells.
*   **rows –** the number of rows to offset. If you use a positive number it offsets to the rows below, and if a negative number is used, then it offsets to the rows above.
*   **cols –** the number of columns to offset. If you use a positive number it offsets to the columns to the right, and if a negative number is used, then it offsets to the columns on the left.
*   **\[height\] –** this is a number that represents the number of rows in the returned reference.
*   **\[width\] –** this is a number that represents the number of columns in the returned reference.

Understanding the Basics of Excel OFFSET Function
-------------------------------------------------

Excel OFFSET function is possibly one of the most confusing functions in Excel.

Let’s take a simple example of a Chess game. There is a piece in Chess called a Rook (also known as a tower, marquess, or rector).

![120px-Chess_piece_-_White_rook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20120%20204'%3E%3C/svg%3E)_\[Image courtesy: [Wonderful Wikipedia](https://en.wikipedia.org/wiki/Rook_(chess))\
\]_

Now, as all the other Chess pieces, a Rook has a fixed path on which it can move around on the board. It can go straight (to the right/left or up/down the board), but it can not go diagonally.

For example, suppose we have a chess board in Excel (as shown below), in a given box (D5 in this case), the Rook can only go in the four highlighted directions.

![Excel Offset Function - Chess](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20396%20302'%3E%3C/svg%3E)

Now if I ask you to take the Rook from it’s current position to the one highlighted in yellow, what will you tell the rook?

![Excel Offset Function - Chess Move](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20302'%3E%3C/svg%3E)

You’ll ask it to take two steps downwards and two steps to the right.. isn’t it?

And that’s a close proximation of how the OFFSET function works.

Now let’s see what this means in Excel. I want to start with the cell D5 (which is where the Rook is) and then go two rows down and two columns to the right and fetch the value from the cell there.

The formula would be:  
\=OFFSET(from where to begin, how many rows down, how many columns to the right)

![Excel Offset Function - Return Value chess](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20490%20335'%3E%3C/svg%3E)

As you can see, the formula in the above example in cell J1 is =OFFSET(D5,2,2).

It started at D5, and then went two rows down and two columns to the right and reached the cell F7. It then returned the value in cell F7.

In the above example, we looked at the OFFSET function with 3 arguments. But there are two more optional arguments that can be used.

Let’s look at a simple example here:

![Excel Offset Function - Area](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20301'%3E%3C/svg%3E)

Suppose you want to use the reference to cell A1 (in yellow) and you want to refer to the entire range highlighted in blue (C2:E4) in a formula.

How would you do that using a keyboard? You would first go to cell C2, and then select all the cells in C2:E4.

Now let’s see how to do this using the OFFSET formula:

\=OFFSET(A1,1,2,3,3)

If you use this formula in a cell, it will return a #VALUE! error, but if you get into the edit mode and select the formula and press F9, you’ll see that it returns all the values that are highlighted in blue.

![Excel OFFSET Function - F9](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20368'%3E%3C/svg%3E)

Now let’s see how this formula works:

\=OFFSET(A1,1,2,3,3)

*   The first argument is the cell where it should start.
*   The second argument is 1, which tells Excel to return a reference which has been OFFSET by 1 row.![Excel OFFSET Function - arg 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20303'%3E%3C/svg%3E)
*   The third argument is 2, which tells Excel to return a reference which has been OFFSET by 2 columns.![Excel OFFSET Function - arg 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20301'%3E%3C/svg%3E)
*   The fourth argument is 3. This specifies that the reference should cover 3 rows. This is called the height argument.![Excel OFFSET Function - arg 4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20301'%3E%3C/svg%3E)
*   The fifth argument is 3. This specifies that the reference should cover 3 columns. This is called the width argument.![Excel OFFSET Function - arg 5](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20395%20301'%3E%3C/svg%3E)

Now that you have the reference to a range of cells (C2:E4), you can use it within other function (such as SUM, COUNT, MAX, AVERAGE).

Hopefully, you have a good basic understanding of using the Excel OFFSET function. Now let’s have a look at some practical examples of using the OFFSET function.

Excel OFFSET Function – Examples
--------------------------------

Here are two examples of using Excel OFFSET function.

### **Example 1 – Finding the Last Filled Cell in the Column**

Suppose you have some data in a column as shown below:

To find the last cell in the column, use the following formula:

![Excel OFFSET Function - Example 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2093%20306'%3E%3C/svg%3E)

\=OFFSET(A1,COUNT(A:A)-1,0)

This formula assumes that there are no values apart from the ones shown and these cells do not have a blank cell in it. It works by counting the total number of cells that are filled, and offsets the cell A1 accordingly.

For example, it this case, there are 8 values, so COUNT(A:A) returns 8. We Offset the cell A1 by 7 to get the last value.

### **Example 2 – Creating a Dynamic Drop Down**

You can extend the concept shows in Example 1 to create dynamic named ranges. These could be useful if you are using the named ranges in formulas or in creating [drop-downs](https://trumpexcel.com/excel-drop-down-list/)
 and you are likely to add/delete data from the reference that makes the named range.

Here is an example:

![Excel OFFSET Function - Dynamic Named Range Example 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20360%20240'%3E%3C/svg%3E)

Note that the drop down adjusts automatically when the year is added or removed.

This happens as the formula that is used to create the drop down is dynamic and identifies any addition or deletion and adjusts the range accordingly.

Here is how to do this:

*   Select the cell where you want to insert the drop down.
*   Go to Data –> Data Tools –> Data Validation.
*   In the Data Validation dialog box, within the Settings tab select List from the drop down.
*   In the source, enter the following formula: \=OFFSET(A1,0,0,COUNT(A:A),1)
*   Click OK.

_Let see how this formula works:_

*   The first three arguments of the OFFSET function are A1, 0 and 0. This essentially means that it would return the same reference cell (which is A1).
*   The fourth argument is for height and here the COUNT function returns the total number of items in the list. It assumes that there are no blanks in the list.
*   The fifth argument is 1, which indicates that the column width should be one.

**Additional Notes:**

*   OFFSET is a [volatile function](https://trumpexcel.com/excel-volatile-formulas/)
     (use with caution).
    *   It recalculates whenever the excel workbook is open or whenever a calculation is triggered in the worksheet. This could add to the processing time and slow down your workbook.
*   If the height or width value is omitted, it is taken as that of the reference.
*   If **rows** and **cols** are negative numbers then the offset direction is reversed.

Excel OFFSET Function Alternatives
----------------------------------

Due to some of the limitations of Excel OFFSET function, you many want to consider alternatives to it:

*   [INDEX Function](https://trumpexcel.com/excel-index-function/)
    : INDEX function can also be used to return a cell reference. [Click here](https://trumpexcel.com/named-ranges-in-excel/)
     to see an example on how to create a dynamic named range using the INDEX function.
*   [Excel Table](https://trumpexcel.com/excel-table/)
    : If you use structured references in Excel Table, you need not worry about new data being added and the need to adjust the formulas.

Excel OFFSET Function – Video Tutorial
--------------------------------------

**Related Excel Functions:**

*   [Excel VLOOKUP Function](https://trumpexcel.com/excel-vlookup-function/)
    .
*   [Excel HLOOKUP Function](https://trumpexcel.com/excel-hlookup-function/)
    .
*   [Excel INDEX Function](https://trumpexcel.com/excel-index-function/)
    .
*   [Excel INDIRECT Function](https://trumpexcel.com/excel-indirect-function/)
    .
*   [Excel MATCH Function](https://trumpexcel.com/excel-match-function/)
    .

**You May Also Like the Following Excel Tutorials:**

*   [Create a Scroll Bar using Excel OFFSET Function](https://trumpexcel.com/create-a-scroll-bar-in-excel/)
    .
*   [Creating Dynamic Chart Range using OFFSET](https://trumpexcel.com/dynamic-chart-range/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “Excel OFFSET Function | Formula Examples + FREE Video”
---------------------------------------------------------------------

1.  Very nice
    
    [Reply](https://trumpexcel.com/excel-offset-function/#comment-14900)
    
2.  Where to download the exercise file?
    
    [Reply](https://trumpexcel.com/excel-offset-function/#comment-13392)
    
3.  How do i use excel to detect two different numbers in a row, appearing in another row?
    
    [Reply](https://trumpexcel.com/excel-offset-function/#comment-12266)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-offset-function/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK