# Excel COUNTA Function (Explained with Examples)

**Source:** https://trumpexcel.com/excel-functions/counta-function

---

[Skip to content](https://trumpexcel.com/excel-functions/counta-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-functions/counta-function/#below-title)

The COUNTA function is one of the counting functions in Excel that **counts all non-empty cells in a range**.

Whether you’re working with text, numbers, dates, or even error values, COUNTA will count them all as long as the cell isn’t completely empty.

When to Use Excel COUNTA Function
---------------------------------

COUNTA function can be used when you want to count all the cells in a range that are not empty. This is particularly useful for:

*   **Counting survey responses** – regardless of whether they contain text, numbers, or dates
*   **Data validation** – ensuring all required fields have been filled
*   **Progress tracking** – monitoring how many items in a list have been completed
*   **Attendance tracking** – counting entries in attendance sheets
*   **Quality control** – verifying data entry completion

### What COUNTA Function Returns

It returns a number that represents the number of cells that are not empty in the specified range(s).

### Syntax

\=COUNTA(value1, \[value2\], \[value3\], …)

where:

*   value1 – the first item, cell reference, or range within which you want to count the number of cells that are not empty.
*   \[value2\], … – (optional) up to 255 additional items, cell references, or ranges within which you want to count the number of cells that are not empty.

### Example 1: Count Non Blank Cells in a Range

Let’s start with a simple example.

Below I have a dataset, and I want to count the total number of non-empty cells in the range A1:A10.

![Data to use counta](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20355%20846'%3E%3C/svg%3E)

Here is the formula that will do this.

    =COUNTA(A1:A10)

![COUNTA function to count non blank cells in a range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201102%20969'%3E%3C/svg%3E)

This counts all non-empty cells in the range A1:A10.

**Pro Tip**: If you want to count all the non-blank cells in the entire column, you can use _\=COUNTA(A.:.A)_

### Example 2: Count Non Blank Cells in Multiple Ranges

Below I have numbers in Column A and Column C, and I want to count all the non-blank cells in these two ranges.

![Data in multiple ranges](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20865%20853'%3E%3C/svg%3E)

I can use multiple ranges within a single COUNTA function, as shown below.

    =COUNTA(A1:A10, C1:C10)

![Formula to count non-empty cells in multiple ranges](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201363%20976'%3E%3C/svg%3E)

This will count all the non-empty cells across all the multiple separate ranges specified in the formula.

### Example 3: Count Non Blank Cells with Mixed Data Types

Below I have a dataset where I have different types of data types in the cells, including text, error, number, date, and Boolean value.

![Dataset with mixed data type](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20481%20693'%3E%3C/svg%3E)

Here is the formula that will count all the non empty cells:

    =COUNTA(A1:A7)

![COUNTA function to count cells with mixed data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201069%20820'%3E%3C/svg%3E)

### Example 4 – Number all the Filled Cells / Rows

Below I have a dataset where I have some data in column B, and I want to add a serial number in the cells in column A only if the cell in column B is filled. If the cell in column B is empty, I do not want to put any number on it.

![Dataset to number rows in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20666%20774'%3E%3C/svg%3E)

Here is the formula that will do this.

\=IF(ISBLANK(B2), "",COUNTA($B$2:B2))

![CountA formula to number filled rows in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201584%20891'%3E%3C/svg%3E)

The above formula first checks whether cell B2 is empty or not using the ISBLANK function. If the cell is empty, it returns a null string. But if it is not empty, it uses the COUNTA function to count all the filled cells starting from cell B2.

This gives us a sequential serial number for all the filled cells while skipping the blank cells.

### Example 5: Survey Response Tracking

You can also combine the result of the COUNTA function with a text string to get insights about your data.

For example, below I have a dataset where I have survey responses, and I want to know how many survey responses I have received.

![survey response data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201133%201034'%3E%3C/svg%3E)

Below is a formula that could give the result of the counter function and then append the string to give me insights about the data.

    =COUNTA(B2:B50) & " responses received"

![COUNTA function to get survey responses](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201661%201333'%3E%3C/svg%3E)

### Additional Notes

*   _Counts all non-empty cells_ – If a cell contains any type of information including error values, it is counted by COUNTA
*   _Empty string handling_ – If a formula returns an empty string (“”), that cell is still counted by COUNTA
*   _Performance tip_ – For large datasets, specify exact ranges instead of entire columns (use A1:A1000 instead of A:A). Or use the TRIMREF function or the dot operator to ensure that blank cells around the ranges are ignored
*   _Hidden data_ – COUNTA counts cells that appear empty but contain spaces or non-visible characters

**Related Excel Functions:**

*   [Excel COUNT Function](https://trumpexcel.com/excel-count-function/)
     – Count numeric values only
*   [Excel COUNTBLANK Function](https://trumpexcel.com/excel-countblank-function/)
     – Count empty cells
*   [Excel COUNTIF Function](https://trumpexcel.com/excel-countif-function/)
     – Count with criteria
*   [Excel COUNTIFS Function](https://trumpexcel.com/excel-countifs-function/)
     – Count with multiple criteria

**Other Excel articles you may also like:**

*   [Count Unique Values in Excel Using COUNTIF Function](https://trumpexcel.com/count-unique-values-in-excel-countif/)
    .
*   [Using Multiple Criteria in Excel COUNTIF and COUNTIFS Function](https://trumpexcel.com/multiple-criteria-in-excel-countif/)
    
*   [How to Count Cells that Contain Text Strings.](https://trumpexcel.com/count-cells-that-contain-text/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

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