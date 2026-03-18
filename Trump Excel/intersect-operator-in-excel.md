# What is Intersect Operator in Excel and How to Use it

**Source:** https://trumpexcel.com/intersect-operator-in-excel

---

[Skip to content](https://trumpexcel.com/intersect-operator-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/intersect-operator-in-excel/#below-title)

**Watch Video – Using Intersect Operator in Excel**

**Intersect Operator in Excel** can be used to find the intersecting value(s) of two lists/ranges. This an unusual operator as it is represented by a space character (yes that’s right).

If you use a space character in between two ranges, then it becomes the Intersect operator in Excel.

**Intersect Operator in Excel**
-------------------------------

You can use Intersect Operator in Excel to find:

*   The intersection of a single row and column.
*   The intersection of multiple rows and columns.
*   The intersection of Named Ranges.

### Intersection of a Single Row and Column

Suppose there is a data set as shown below:

![Intersect Operator in Excel - Data Set](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20383%20294'%3E%3C/svg%3E)

Now if you use \=C2:C13 B5:D5 \[_Note there is a single space in between the ranges, which is also our intersect operator in Excel_\], it will return 523 (the value in cell C5), which is the intersection of these 2 ranges.

![Intersect Operator in Excel - Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20292'%3E%3C/svg%3E)

### Intersection of a Multiple Rows and Columns

You can also use the same technique to find the intersection of ranges that spans more than one row or column. For example, with the same data set as shown above, you can get the intersection of Product 1 and Product 2 in April.

Here is the formula that can do that: \=B2:C13 B5:D5

Note that the result of this formula would display a [Value error](https://trumpexcel.com/fix-value-error-in-excel/)
, however, when you select the formula and press F9, it will show the result as {649,523}. This formula returns an array of the intersection values. You can use this within formulas, such as [SUM](https://trumpexcel.com/excel-sum-function/)
 (to get the total of the intersection values) or [MAX](https://trumpexcel.com/excel-max-function/)
 (to get the maximum of the intersection values).

![Intersect Operator in Excel - 2 Ranges](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20292'%3E%3C/svg%3E)

### Intersection of Named Ranges

You can also use named ranges to find the intersection using the Intersect Operator in Excel.

Here is an example where I have named the Product 1 values as Prdt1, Product 2 values as Prdt2 and April Values as Apr.

Now you can use the formula \=Prdt1 Apr to get the intersection of these 2 ranges. Similarly, you can use =Prdt1:Prdt2 Apr to get the intersection of Product 1, Product 2 and April.

![Intersect Operator in Excel - Named Ranges](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20292'%3E%3C/svg%3E)

### A Practical Example of Using Intersect Operator in Excel

Here is a situation where this trick might come in handy. I have a data-set of Sales Rep and the sales they made in each month in 2012.

I have also created a [drop-down list](https://trumpexcel.com/excel-drop-down-list/)
 with _Sales Rep_ Name in one cell and _Month_ name in another, and I want to extract the sales that the Rep did in that month.

Something as shown below:

![Intersect Operator in Excel Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20930%20470'%3E%3C/svg%3E)

**How to create this:**

1.  Select the entire data set (B3:N13) and press Control + Shift + F3 to create [named ranges](https://trumpexcel.com/named-ranges-in-excel/)
     (it can also be done through Formula –> Defined Names –> Create from Selection). This will open a ‘Create Names from Selection’  dialogue box.
2.  Select the ‘Top Row’ and ‘Left Column’ options and click OK.
3.  This will create named ranges for all the Sales Reps and all the Month.![Intersect Operator in Excel - Create Named Ranges from Selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20255%20187'%3E%3C/svg%3E)
4.  Now go to cell B16 and create a drop-down list for all the sales rep.
5.  Similarly, go to cell C15 and create a drop down list for all the months.
6.  Now in cell C16, use the following formula \=INDIRECT(B16) INDIRECT(C15) 

**How does it work?**

Notice that there is a space in between the two INDIRECT formulas.

The [INDIRECT function](https://trumpexcel.com/excel-indirect-function/)
 returns the range for the named ranges – Sales rep and the Month, and the space between them works as an intersect operator and returns the intersecting value.

Note: This invisible intersect operator get precedence over other operators. So if in this case, if you use =INDIRECT(B16) INDIRECT(C15)>5000, it will return TRUE or FALSE based on the intersecting value.

**You May Also Like the Following Excel Tutorials:**

*   [How to Use Excel Freeze Panes to Handle Large Data Sets](https://trumpexcel.com/excel-freeze-panes/)
    .
*   [How to Lock Cells in Excel](https://trumpexcel.com/lock-cells-in-excel/)
    .
*   [How to Calculate Compound Annual Growth Rate (CAGR) in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    .
*   [REGEX Functions in Excel](https://trumpexcel.com/excel-functions/regex-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

7 thoughts on “What is Intersect Operator in Excel and How to Use it”
---------------------------------------------------------------------

1.  Very good book  
    Thanku
    
    [Reply](https://trumpexcel.com/intersect-operator-in-excel/#comment-14838)
    
2.  Excellent et s’avère extrêmement utile. Merci bcp
    
    [Reply](https://trumpexcel.com/intersect-operator-in-excel/#comment-13584)
    
3.  How to use this operator in a Visual Foxpro Program with named ranges in excel? e.g., there are 2 ranges : RNAME AND TNAME. I want the intersect value. I entered as .range(tname rname).value. Error message recd. what is the correct coding?
    
    [Reply](https://trumpexcel.com/intersect-operator-in-excel/#comment-13471)
    
4.  this doesn’t work if you have spaces in the name (say “First” “Last”) because the named ranges put an Underscore where the space is, and the Indirect function doesn’t
    
    [Reply](https://trumpexcel.com/intersect-operator-in-excel/#comment-12175)
    
5.  Instead of pressing F9 what can I click on?
    
    [Reply](https://trumpexcel.com/intersect-operator-in-excel/#comment-11536)
    
6.  Is there any way to find the set difference between 2 ranges (i.e. start with one range, and remove all cells from the other range)?
    
    [Reply](https://trumpexcel.com/intersect-operator-in-excel/#comment-9749)
    
7.  From your above sales rep data table, is there any way to find the max value, which I believe is 9437, and then extrapolate backwards to find out that it was Rachael for the month of May?
    
    [Reply](https://trumpexcel.com/intersect-operator-in-excel/#comment-9527)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/intersect-operator-in-excel/#respond)

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