# How to Return Cell Address Instead of Value in Excel (Easy Formula)

**Source:** https://trumpexcel.com/return-cell-address-instead-of-value-excel

---

[Skip to content](https://trumpexcel.com/return-cell-address-instead-of-value-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/return-cell-address-instead-of-value-excel/#below-title)

When using lookup formulas in Excel (such as [VLOOKUP](https://trumpexcel.com/excel-vlookup-function/)
,  [XLOOKUP](https://trumpexcel.com/xlookup-function/)
, or [INDEX/MATCH](https://trumpexcel.com/index-match/)
), the intent is to find the matching value and get that value (or a corresponding value in the same row/column) as the result.

But in some cases, instead of getting the value, you may want the formula to return the cell address of the value.

This could be especially useful if you have a large data set and you want to find out the exact position of the lookup formula result.

There are some functions in Excel that designed to do exactly this.

In this tutorial, I will show you how you can **find and return the cell address instead of the value** in Excel using [simple formulas](https://trumpexcel.com/excel-functions/)
.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/return-cell-address-instead-of-value-excel/#)

Lookup And Return Cell Address Using the ADDRESS Function
---------------------------------------------------------

The ADDRESS function in Excel is meant to exactly this.

It takes the row and the column number and gives you the cell address of that specific cell.

Below is the syntax of the ADDRESS function:

\=ADDRESS(row\_num, column\_num, \[abs\_num\], \[a1\], \[sheet\_text\])

where:

*   row\_num: Row number of the cell for which you want the cell address
*   column\_num: Column number of the cell for which you want the address
*   \[abs\_num\]: Optional argument where you can specify whether want the cell reference to be [absolute, relative, or mixed](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
    .
*   \[a1\]: Optional argument where you can specify whether you want the reference in the [R1C1 style or A1 style](https://trumpexcel.com/a1-r1c1-reference-notation-excel/)
    
*   \[sheet\_text\]: Optional argument where you can specify whether you want to add the sheet name along with the cell address or not

Now, let’s take an example and see how this works.

Suppose there is a dataset as shown below, where I have the Employee id, their name, and their department, and I want to quickly know the cell address that contains the department for employee id KR256.

![Dataset to Return Cell Address Instead of Value in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20588'%3E%3C/svg%3E)

Below is the formula that will do this:

\=ADDRESS(MATCH("KR256",A1:A20,0),3)

![Address formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20562'%3E%3C/svg%3E)

In the above formula, I have used the [MATCH function](https://trumpexcel.com/excel-match-function/)
 to find out the row number that contains the given employee id.

And since the department is in column C, I have used 3 as the second argument.

This formula works great, but it has one drawback – it won’t work if you add the row above the dataset or a column to the left of the dataset.

This is because when I specify the second argument (the column number) as 3, it’s hard-coded and won’t change.

In case I add any column to the left of the dataset, the formula would count 3 columns from the beginning of the worksheet and not from the beginning of the dataset.

So, if you have a fixed dataset and need a simple formula, this will work fine.

But if you need this to be more fool-proof, use the one covered in the next section.

Lookup And Return Cell Address Using the CELL Function
------------------------------------------------------

While the ADDRESS function was made specifically to give you the cell reference of the specified row and column number, there is another function that also does this.

It’s called the CELL function (and it can give you a lot more information about the cell than the ADDRESS function).

Below is the syntax of the CELL function:

\=CELL(info\_type, \[reference\])

where:

*   **info\_type**: the information about the cell you want. This could be the address, the column number, the [file name](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/)
    , etc.
*   **\[reference\]**: Optional argument where you can specify the cell reference for which you need the cell information.

Now, let’s see an example where you can use this function to look up and get the cell reference.

Suppose you have a dataset as shown below, and you want to quickly know the cell address that contains the department for employee id KR256.

![Dataset to Return Cell Address Instead of Value in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20588'%3E%3C/svg%3E)

Below is the formula that will do this:

\=CELL("address", INDEX($A$1:$D$20,MATCH("KR256",$A$1:$A$20,0),3))

![CELL formula to return Cell Address Instead of Value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20759'%3E%3C/svg%3E)

The above formula is quite straightforward.

I have used the [INDEX formula](https://trumpexcel.com/excel-index-function/)
 as the second argument to get the department for the employee id KR256.

And then simply wrapped it within the CELL function and asked it to return the cell address of this value that I get from the INDEX formula.

Now here is the **secret to why it works** – the INDEX formula returns the lookup value when you give it all the necessary arguments. But at the same time, it would also return the cell reference of that resulting cell.

In our example, the INDEX formula returns “Sales” as the resulting value, but at the same time, you can also use it to give you the cell reference of that value instead of the value itself.

Normally, when you enter the INDEX formula in a cell, it returns the value because that is what it’s expected to do. But in scenarios where a cell reference is required, the INDEX formula will give you the cell reference.

In this example, that’s exactly what it does.

And the best part about using this formula is that it is not tied to the first cell in the worksheet. This means that you can select any data set (which could be anywhere in the worksheet), use the INDEX formula to do a regular look up and it would still give you the correct address.

And if you insert an additional row or column, the formula would adjust accordingly to give you the correct cell address.

So these are two simple formulas that you can use to look up and **find and return the cell address instead of the value in Excel**.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [Lookup and Return Values in an Entire Row/Column in Excel](https://trumpexcel.com/lookup-and-return-values-entire-row-column-excel/)
    
*   [Find the Last Occurrence of a Lookup Value a List in Excel](https://trumpexcel.com/find-last-occurrence/)
    
*   [Lookup the Second, the Third, or the Nth Value in Excel](https://trumpexcel.com/lookup-second-value/)
    
*   [How to Reference Another Sheet or Workbook in Excel](https://trumpexcel.com/reference-another-sheet-or-workbook-in-excel/)
    
*   [Lookup and Return Values in an Entire Row/Column in Excel](https://trumpexcel.com/lookup-and-return-values-entire-row-column-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/return-cell-address-instead-of-value-excel/#respond)

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