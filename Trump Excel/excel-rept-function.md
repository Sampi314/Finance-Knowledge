# How to Use Excel REPT Function (Examples + Video)

**Source:** https://trumpexcel.com/excel-rept-function

---

[Skip to content](https://trumpexcel.com/excel-rept-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-rept-function/#below-title)

Excel REPT Function (Example + Video)
-------------------------------------

![Excel REPT Function](https://trumpexcel.com/wp-content/uploads/2014/03/REPT-FORMULA-EXCEL.png)

### When to use Excel REPT Function

REPT function can be used when you want to repeat a specified text for a certain number of times.

![Excel REPT Function - example output](https://trumpexcel.com/wp-content/uploads/2014/03/Excel-REPT-Function-example-output.png)

If you’re wondering what can be the use of just repeating characters, check out the examples covered later in this tutorial.

### What it Returns

It returns a text string that has the specified text repeat for the specified number of times.

### Syntax

\=REPT(text, number\_times)

### Input Arguments

*   **text –** the text to repeat. You can specify this with the double quotes, or have it in a cell and use the cell reference instead.
*   **number\_times –** the number of times text should repeat. You can specify the number by manually entering it in the formula, or have the number in a cell and use the cell reference.

### Additional Notes

*   If the second argument (number of times to repeat) is 0, it returns “” (blank).
*   If the second argument (number of times to repeat) is not an integer, it is truncated. For example, if you use the number 10.8, it will only consider 10 and repeat the specified text 10 number of times.
*   The result of the REPT function cannot be longer than 32,767 characters, or else it will return a #VALUE! error.

Examples of Using REPT Function in Excel
----------------------------------------

Below are some practical examples of using the REPT function in Excel.

### Example 1 – Make all the Output String of the same length

While working with data in Excel (especially financial data), it is needed to make all the numbers of the same length. This can be done by [adding leading zeroes](https://trumpexcel.com/add-leading-zeroes-excel/)
 in the numbers.

For example, as shown below, the numbers in column B are all of the same lengths. When used in a report, these will look aligned and more professional.

![Numbers Aligned Using REPT Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20208%20289'%3E%3C/svg%3E)

Below is the formula that will do this using the REPT function.

**\=REPT("0",4-LEN(A1))&A1**

In the above function, we first calculate the length of the existing string using the [LEN function](https://trumpexcel.com/excel-len-function/)
. The result of the LEN function is then subtracted from 4 (which is the consistent length we want for all numbers). You can use whatever

The result of the LEN function is then subtracted from 4 (which is the consistent length we want for all numbers). You can use whatever character length you want.

REPT function returns the numbers of 0’s based on the existing character length of the numbers. For example, if the number is 15, it would return 00 and two zeroes are needed to make the combined string of 4 characters.

Now we simply combine the REPT function with the number to get the consistent length numbers.

Note that the REPT function would return the output as a string. So you may find the output aligned to the left in the cell. If needed, you can use the alignment tool to align it to the middle or to the right.

### Example 2 – Creating In-cell Charts Using REPT Function

You can also use the REPT function to show some comparison right along the data right within the cell (hence called in-cell charts).

Something as shown below:

![Creating incell charts using REPT Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20295%20315'%3E%3C/svg%3E)

This can be helpful if you’re [creating an Excel dashboard](https://trumpexcel.com/creating-excel-dashboard/)
 and don’t want to insert a chart or use [conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
.

Here are the steps to create these in-cell bars using REPT function:

*   In the cell adjacent to the score, enter the following formula
    
    \=REPT("|",B2/3)
    
*   Copy the formula for all the cells.
*   Select all the cells and change the font to Stencils.

The above steps would create the in cell bars. However, these would all be in the default text font color (most likely black).

![Incell charts using REPT Function - Stencil font](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20277%20314'%3E%3C/svg%3E)

You can use conditional formatting to change the color of the bars (green if the score is greater than or equal to 35, else red).

Below are the steps to use conditional formatting to show in-cell bars in specific colors.

*   Select the cells that have the in-cell bars/charts.
*   Go to the Home tab.
*   Click on the Conditional Formatting drop down.
*   Click on New Rule.![conditional formatting in incell charts](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20196%20385'%3E%3C/svg%3E)
*   In the New Formatting Rule dialog box, select ‘Use a formula to determine which cells to format’.![Conditional Formatting Use Formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20366'%3E%3C/svg%3E)
*   In the Rule field, enter the formula: =B2>=35![Formula in Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20366'%3E%3C/svg%3E)
*   Click on the Format button.
*   Change the font color to green.
*   Close the dialog box.

You need to follow the same steps to create a new rule to highlight score less than 35 in red.

![In cell charts using REPT function - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20328'%3E%3C/svg%3E)

Below are some more interesting in-cell charts you can create using the REPT function.

![In-cell charts created using REPT function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20587%20316'%3E%3C/svg%3E)

**Related Excel Functions:**

*   [Excel CONCATENATE Function](https://trumpexcel.com/excel-concatenate-function/)
    .
*   [Excel LEFT Function](https://trumpexcel.com/excel-left-function/)
    .
*   [Excel LEN Function](https://trumpexcel.com/excel-len-function/)
    .
*   [Excel MID Function](https://trumpexcel.com/excel-mid-function/)
    .
*   [Excel RIGHT Function](https://trumpexcel.com/excel-right-function/)
    .
*   [Excel TEXT Function](https://trumpexcel.com/excel-text-function/)
    .
*   [Excel TRIM Function](https://trumpexcel.com/excel-trim-function/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-rept-function/#respond)

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