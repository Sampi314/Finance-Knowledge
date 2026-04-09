# How to Convert Fraction to Decimal in Excel (3 Easy Ways)

**Source:** https://trumpexcel.com/convert-fraction-to-decimal-excel

---

[Skip to content](https://trumpexcel.com/convert-fraction-to-decimal-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/convert-fraction-to-decimal-excel/#below-title)

Sometimes when you download data from external sources or import information from other systems, you end up with fractions that are stored as text instead of actual numbers.

You might see values like “17/76” or “1/4” sitting in your cells, and Excel treats them as text rather than mathematical expressions you can work with.

This can be frustrating when you need to perform calculations or create charts, since Excel can’t do math on text that looks like fractions.

In this tutorial, I’ll show you some easy ways to convert fractions to decimals in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/convert-fraction-to-decimal-excel/#)

Convert the Format from Fraction to General
-------------------------------------------

Before we dive into complex formulas, let’s start with the simplest solution that many people overlook.

Sometimes what looks like fractions in your cells are actually decimal values that Excel has automatically formatted to display as fractions.

The easiest way to check if this is the case is to simply change the cell format from Fraction to General.

Below is a dataset where some values might be formatted as fractions but are actually decimals in the backend.

![Fractions data set in excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20524%20774'%3E%3C/svg%3E)

If you select any of the cells, you will see that in the [formula bar](https://trumpexcel.com/show-hide-formula-bar-excel/)
 it shows you the decimal value. This is an indication that the format has been changed of the cell to show the value as a fraction.

![Cell shows decimal in the formula bar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201082%20891'%3E%3C/svg%3E)

Here are the steps to convert these fractions back into decimals:

1.  Select all the cells that have the fraction values.
2.  Click the _Home_ tab.
3.  In the _Number_ group, click on the format drop-down and select _General_.

![Set the formatting to general](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202194%201435'%3E%3C/svg%3E)

This should change the formatting of all the cells and the fractions should now be displayed as decimal values.

![Fractions converted to decimal in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20521%20774'%3E%3C/svg%3E)

Note: If changing the format doesn’t work and your values still show as text-like fractions (such as “17/76”), then your data is actually stored as text, and you’ll need to use one of the other methods below.

Also read: [How to Add Decimal Places in Excel (Automatically)](https://trumpexcel.com/add-decimal-places-excel/)

Using TEXTBEFORE and TEXTAFTER Functions
----------------------------------------

Sometimes when you download data from the web or a database, or you get a file from a colleague, the fractions are actually stored as text values rather than numbers.

In such cases, changing the format won’t work since Excel sees them as text strings like “17/76” or “1/4” rather than mathematical expressions.

This is where the TEXTBEFORE and TEXTAFTER functions come in handy.

_Note: These are new Excel functions that are available only on Excel with Microsoft 365 in Excel on the web._

These new [Excel functions](https://trumpexcel.com/excel-functions/)
 can extract the numerator and denominator from the text, and then we can divide them to get the decimal equivalent.

Below I have a dataset where I have fractions in column A that I want to convert and get the decimal values in column B.

![Dataset to convert fractions to decimals using formulas in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20910%20772'%3E%3C/svg%3E)

Here is the formula that will do this for me.

\=TEXTBEFORE(A2,"/")/TEXTAFTER(A2,"/")

![Textbefore and textafter function to convert fractions to decimals](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201594%20888'%3E%3C/svg%3E)

In the above formula:

*   **TEXTBEFORE(A2,”/”)** – This extracts everything that comes before the forward slash. So if A2 contains “17/76”, this part gives you “17” (the numerator)
*   **TEXTAFTER(A2,”/”)** – This extracts everything that comes after the forward slash. So from “17/76”, this part gives you “76” (the denominator)
*   **The division operator (/)** – This divides the numerator by the denominator to calculate the decimal value.

Essentially, the formula breaks apart the text fraction into its two components and then performs the mathematical division to convert it into a proper decimal number that Excel can use for calculations.

Note: this formula will not be able to work with mixed fractions such as 3 1/2. If you want to work with mixed fractions, you will have modify the formula to extract the digit before the space character, the digit after the space character and before the /, and the digit after the forward slash. If you are dealing with mixed fractions, check out the EVALUATE function method.

Also read: [Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)

Using EVALUATE Function
-----------------------

If you’re using an older version of Excel and do not have access to the TEXTBEFORE and TEXTAFTER function, then you can use this method.

In this method, we are going to use an EVALUATE function which is a hidden function in Excel that is not available in the worksheet.

While you cannot use this function in a cell in the worksheet, you can use it in a [Named Range](https://trumpexcel.com/named-ranges-in-excel/)
.

This method requires you to first create a named range using the Evaluate function, and then that named range can be used in a cell to convert fractions to decimals.

Let’s go through each step.

### Step 1 – Setting up the Named Range

1.  Click the Formulas tab and then click on the Define Name option.

![Click on the 'Define Name' option in the Formulas tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201712%20533'%3E%3C/svg%3E)

2.  In the New Name dialog box, enter the name for this Name Range. In this example, I am going to use _FractoDec_.

![Enter the name for the defined name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20906%20688'%3E%3C/svg%3E)

3.  In the refers to field, enter the below formula:

\=EVALUATE(INDIRECT(ADDRESS(ROW(),COLUMN()-1)))

![Enter the formula in the new name dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20906%20688'%3E%3C/svg%3E)

4.  Click OK

The above steps creates a named range called _FractoDec_ that you can now use in the worksheet.

Formula Explaination:

*   _ADDRESS(ROW(),COLUMN()-1)_ – this part of the formula returns the cell reference of the cell that is to the left of the cell where this formula is entered. So, if I enter this formula in cell B2, then this would return the reference of cell A2.
*   _[INDIRECT](https://trumpexcel.com/excel-indirect-function/)
    ()_ – this converts that text address into an actual cell reference that Excel can use
*   _EVALUATE()_ – this will take the text content from the referenced cell and evaluate it to give you the result

So if you put this formula in cell B2, it looks at cell A2, takes whatever text is there (like “3/4”), and calculates it as a math problem to give you the decimal result (0.75). It’s basically telling Excel to treat the text fraction as a real calculation.

But as I said, you cannot use the EVALUATE function in the worksheet. This is why we have put this function in the named range, because named range is something we can use in the worksheet.

### Step 2 – Using the Named Range in the worksheet

Now that the named range is in place, you can enter the name of the named range in cell B2 to get the decimal value from the fraction in cell A2.

So in this example, in cell B2, enter the following formula.

\=FracToDec

![Enter the named range name in the cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201014%20890'%3E%3C/svg%3E)

While using the VALUATE function does take a little bit of setup, it is a little more robust than using the TEXT BEFORE or TEXT AFTER function or the LEFT and RIGHT function because it can also handle mixed fractions properly.

For example, if in a cell you have “3 1/4”, you will have to adjust the text formulas accordingly, which can get a bit complicated. But Evaluate will also handle it, just like a regular fraction.

Important Note: EVALUATE is an old Macro 4 function. When you use this function, we need to ensure that you save the file as a macro-enabled file with a .xlsm extension. If you don’t, then this formula would be removed.

In this article, I have shown you some simple methods to convert fractions to decimals in Excel.

If you are using Excel with Microsoft 365, the easiest way would be to use the TEXTBEFORE and TEXTAFTER functions. And if you are using an older version of Excel, then you can consider using the EVALUATE function.

I hope you found this article helpful.

If you have any questions or suggestions for me, kindly let me know in the comment section.

**Other Excel articles you may also like:**

*   [How to Display Numbers as Fractions (Write Fractions in Excel)](https://trumpexcel.com/display-numbers-as-fractions-excel/)
    
*   [How to Stop Excel from Rounding Numbers (Decimals/Fractions)](https://trumpexcel.com/stop-excel-from-rounding-numbers/)
    
*   [How to Write Scientific Notation in Excel?](https://trumpexcel.com/scientific-notation-excel/)
    
*   [How to Calculate Ratios in Excel?](https://trumpexcel.com/calculate-ratios-excel/)
    
*   [Convert text to numbers in Excel](https://trumpexcel.com/convert-text-to-numbers-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Convert Fraction to Decimal in Excel”
----------------------------------------------------------

1.  It is a great work. I could get almost all of my Excel problems clarified. My honour to you.  
    \-Thilak Wijesinghe  
    (Excel lover)
    
    [Reply](https://trumpexcel.com/convert-fraction-to-decimal-excel/#comment-46252)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/convert-fraction-to-decimal-excel/#respond)

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