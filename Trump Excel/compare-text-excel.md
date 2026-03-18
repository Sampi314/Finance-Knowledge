# How to Compare Text in Excel (Easy Formulas)

**Source:** https://trumpexcel.com/compare-text-excel

---

[Skip to content](https://trumpexcel.com/compare-text-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/compare-text-excel/#below-title)

Excel users often need to compare cells or columns to check if the same text is available in the cells/columns or not.

A very common example of this is when you have names in two columns and you want to check if the names are exactly the same or what names are missing in one column.

Comparing text in Excel is fairly easy and can be achieved with simple formulas.

In this tutorial, I will show you how to **compare text in Excel** using simple arithmetic operators or the EXACT function. I will also cover how you can compare text in two columns to find out the missing text entries.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/compare-text-excel/#)

Compare Text in Excel (Exact Cell against Cell Comparison)
----------------------------------------------------------

Below I have a data set where I have names in column A as well as column B, and I want to compare the names in each row. I want to check whether the names in the same row are the same or not.

![Names Dataset to compare text in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20403'%3E%3C/svg%3E)

Let’s look at two simple ways to get this done.

### Using the Equal to Operator

The equal operator can commit will pare the content in one cell with another cell, and give you a TRUE in case the cells have the exact same text in it, or FALSE in case the text is not the same.

Below is the formula that will compare the text in two cells in the same row:

\=A2=B2

Enter this formula in cell C3 and then copy and paste it into all the cells.

![Equal to formula to compare text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20626%20446'%3E%3C/svg%3E)

The above formula returns a TRUE in case there is an exact match (meaning that the names are exactly the same), and it returns a FALSE in case the names do not match

In our example above, you can see that the formula returns FALSE in cells C6 and C11, indicating that the names in row #6 and row #11 are not the same.

If you want to only see the rows where the names are not the same, you can [apply filters](https://trumpexcel.com/excel-data-filter/)
 on the headers and then filter only those cells in column C where the value is FALSE

**Note**: For the formula to return a TRUE, the cell contents need to be exactly the same. In case there is an [extra space](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
 in one of the cells, while it may look as if the cells have the same name, the formula would return a FALSE.

When you use the equal to operator, it does not consider the case of the text in the cell.

For example, if you have ‘James Baker’ in one cell and ‘james baker’ in another cell and you compare these two, the formula would return a TRUE.

In case you want the comparison to be case-sensitive, use the EXACT function method covered next.

### Using the EXACT function

Another easy way to compare text in two cells in Excel is by using the EXACT function.

As the name suggests, it would return TRUE in case the content of the two cells being compared is exactly the same, and FALSE in case the contents are not the same.

Considering the same data set with names and column A and column B, below is the formula that will compare the names and give us the result

\=EXACT(A2,B2)

Enter this formula in cell C3 and then copy and paste it into all the cells.

![EXACT formula to compare text in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20621%20448'%3E%3C/svg%3E)

The EXACT function takes the [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 of the cells that need to be compared as the arguments and returns a TRUE in case there is an exact match, and a FALSE if there is not.

In case you’re using newer versions of Excel that have dynamic arrays, you can also use the below formula in cell C2 (and you don’t need to copy and paste the formula in the remaining cells as the dynamic formula would spill over and fill the other cells automatically)

\=EXACT(A2:A12,B2:B12)

Note that the EXACT function is case sensitive, so even if the names are exactly the same but in different cases (lower or upper, or proper), the formula would return a FALSE.

Compare Text and Find Missing Text Using VLOOKUP
------------------------------------------------

Another real-life situation where you may need to compare text is when you have a list in two columns and you want to find out the items/names that are there in one column but missing in the other column.

Below I have a data set where I have some names in column A and in column B, and I want to check what names in column A are also they’re in column B, and which ones are missing

![Dataset to compare text in two columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20501%20403'%3E%3C/svg%3E)

Below is the formula that would give us the text “Present” in case the name in column A is also there in column B and it would give us “Missing” in case the name in column A is not present in column B.

\=IF(ISERROR(VLOOKUP(A2,$B$2:$B$9,1,0)),"Missing","Present")

Enter this formula in cell C3 and then copy and paste it into all the cells.

![VLOOKUP formula to compare text in two columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20644%20474'%3E%3C/svg%3E)

The above formula uses the [VLOOKUP function](https://trumpexcel.com/excel-vlookup-function/)
 to check for each name in column A against the list in column B.

If the VLOOKUP formula finds the name, it would return that name, and in case it doesn’t find the name, it would return the #N/A! error

I haven’t wrapped this VLOOKUP formula inside the [ISERROR function](https://trumpexcel.com/excel-is-function/)
 so that if the names are present, it would return a FALSE, and if the names are missing then it would return a TRUE.

And then I wrapped this inside an [IF function](https://trumpexcel.com/excel-if-function/)
, which gives us the text ‘Present’ if the name in column A is also there in column B, as it returns the text ‘Missing’

You can also use a similar formula construct to check the other way around, whether the names in column B are present in column A or not (by adjusting the formula accordingly).

_In this example, I have used the VLOOKUP function to compare the text in two columns, but this can also be done with other formulas such as [INDEX/MATCH](https://trumpexcel.com/index-match/)
 or [XLOOKUP](https://trumpexcel.com/xlookup-function/)
._

Compare Text and Check If Partial Text Matches
----------------------------------------------

Another common situation that I have come across is when people want to compare the text in one cell with another cell, but they’re not looking for an exact comparison, and just need to check whether the text in one cell is present in the other cell or not.

Below I have a data set where I have some names in column A and in column B.

![Dataset to compare partial text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20405'%3E%3C/svg%3E)

You would notice that the names in column B are only the first names, and the names in column A are full names.

Now I want to compare these two names and check whether the name in column B is there in column A or not.

As you can see, I’m not looking for an exact comparison but a partial text match.

And below is the formula that will do this for me:

\=ISNUMBER(FIND(B2,A2))

Enter this formula in cell C3 and then copy and paste it into all the cells.

![Formula to compare text and check for partial match](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20547%20449'%3E%3C/svg%3E)

The above formula uses the [FIND function](https://trumpexcel.com/excel-find-function/)
 to check whether the text value in column B is present in the cell in column A or not.

If the FIND function finds the text in column A it would return the starting position of that text (i.e., it would return a numeric value), and if it cannot find the text, it would return the [VALUE error](https://trumpexcel.com/fix-value-error-in-excel/)
.

I have wrapped the FIND function inside the ISNUMBER function, which would return a TRUE in case the FIND function found the text in column A and returned a value, otherwise, it would return a FALSE.

In this tutorial, I covered some simple formulas that you can use to quickly compare text in Excel.

If you’re looking to compare one cell with another, you can use the equal-to operator or the EXACT function.

And if you’re trying to compare two columns, you can use the VLOOKUP function. And finally, I’ve also covered a method to show you how to compare partial text using the find function.

**Other Excel tutorials you may also like:**

*   [How to Compare Two Excel Sheets (for differences)](https://trumpexcel.com/compare-two-excel-sheets/)
    
*   [How to Compare Dates in Excel (Greater/Less Than, Mismatches)](https://trumpexcel.com/compare-dates-in-excel/)
    
*   [How to Compare Two Columns in Excel (for matches & differences)](https://trumpexcel.com/compare-two-columns/)
    
*   [Separate Text and Numbers in Excel (4 Easy Ways)](https://trumpexcel.com/separate-text-and-numbers-in-excel/)
    
*   [How To Remove Text Before Or After a Specific Character In Excel](https://trumpexcel.com/remove-text-before-after-character-excel/)
    
*   [Compare Two Lists](https://trumpexcel.com/tools/compare-two-lists/)
     (Free Online Tool)

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Compare Text in Excel (Easy Formulas)”
-----------------------------------------------------------

1.  THANK YOU
    
    [Reply](https://trumpexcel.com/compare-text-excel/#comment-32908)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/compare-text-excel/#respond)

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