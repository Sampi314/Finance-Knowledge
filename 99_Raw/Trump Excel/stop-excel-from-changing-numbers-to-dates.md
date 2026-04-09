# How to Stop Excel from Changing Numbers to Dates Automatically

**Source:** https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates

---

[Skip to content](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/#below-title)

Excel has some really smart features that can be really useful in many cases (and sometimes it could be frustrating).

One such area is when you enter numbers in Excel. Sometimes, Excel automatically changes these numbers to dates.

For example, if you enter 1/2 in Excel, Excel will automatically change this to 01-02-2020 (or 02-01-2020 if you’re in the US)

Similarly, if you enter 30-06-2020, Excel assumes you want to enter a date, and it changes this to a date (as shown below)

![Number Changes to date when entered in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20424%20228'%3E%3C/svg%3E)

While this may be what you want in most cases, but what if I don’t want this. What if I simply want the exact text 30-06-2020 or the fraction 1/2.

**_How do I stop Excel from changing numbers to dates?_**

That’s what this tutorial is about.

In this Excel tutorial, I will show you two really simple ways to stop Excel from changing numbers to text.

But before I show you methods, let me quickly explain why Excel does this.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/#)

Why does Excel Changes Numbers to Date?
---------------------------------------

While it can be frustrating when Excel does this, it’s trying to help.

In most cases, when people enter numbers that can also represent valid [date formats in Excel](https://trumpexcel.com/change-date-format-excel/)
, it will automatically convert these numbers into dates.

And this just doesn’t mean that it changes the format, it actually changes the underlying value.

For example, if you enter 3/6/2020 (or 6/3/2020 if you’re in the US and using the US date format), Excel changes the cell value to 44012, which is the numerical value of the date.

Also read: [How to Convert Numbers to Text in Excel](https://trumpexcel.com/convert-numbers-to-text-excel/)

Stop Excel from Changing Numbers to Dates Automatically
-------------------------------------------------------

The only way to stop Excel from changing these numbers (or text string) into dates is by clearing letting it know that these are not numbers.

Let’s see how to do this.

### Change the format to text

The easiest way to make sure Excel understands that it’s not supposed to change a number to date is by specifying the format of the cell as Text.

Since dates are stored as numbers, when you make the format of a cell text, Excel will understand that the entered number is supposed to be in the text format and not to be converted into a date.

Below is how you can stop Excel from changing numbers to dates:

1.  Select the cell or range of cells where you want to make the format as Text
2.  Click the Home tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20411%20198'%3E%3C/svg%3E)
3.  In the Number group, click on the dialog box launcher icon (or you can use the keyboard shortcut Control + 1).![Click on the dialog launcher icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20239%20134'%3E%3C/svg%3E)
4.  In the Format Cells dialog box, in the category option, click in Text
5.  Click OK

The above steps would change the cell format to text. Now when you enter any number such as 30-06-2020 or 1/2, Excel will not convert these into date format.

You can also open the Format Cells dialog box by selecting the cell, right-clicking on it and then clicking on the Format Cell option.

**Note**: You need to change the format before you enter the number. If you do this after the number has been entered, this would change the format to text but you would get the numeric value of the date and not the exact number/text-string you entered.

This method is best suited when you have to change the format of a range of cells. If you only have to do this for a couple of cells, it’s best to use the apostrophe method covered next

Also read: [How to Convert Serial Numbers to Dates in Excel (2 Easy Ways)](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)

### Add an Apostrophe before the Number

If you only have to enter a number in a few cells and you don’t want Excel to change it to date, you can use this simple technique.

Just add an apostrophe sign before you enter the number (as shown below).

![Stop Excel from Changing Numbers to Dates Using apostrophe](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20423%20119'%3E%3C/svg%3E)

When you add an apostrophe at the very beginning, Excel considers that cell as text.

While you would not see the apostrophe sign, you can visually see that the numbers would be aligned to the left (indicating that it’s text).

_By default, all numbers align to the right and all text values align to the left._

Another benefit of using the apostrophe sign is that you can still use the lookup formulas (such as VLOOKUP or MATCH) using the value in the cell. The apostrophe will be ignored by these functions.

You can also use this method to change existing dates into text. For example, if you have 30-06-2020 in a cell, you can simply add an apostrophe (‘) at the beginning and it will be changed the date to text

Sometimes, you may see a green triangle at the top-left part of the cell, which indicates that [numbers have been stored as text](https://support.office.com/en-us/article/fix-text-formatted-numbers-by-applying-a-number-format-6599c03a-954d-4d83-b78a-23af2c8845d0)
 in those cells. But since that’s exactly what we want in this case, you can ignore those green triangles, or click on it and then select the Ignore Error option to make it go away.

While these methods are great, what if you have a column full of dates that you want to use as a text and not as dates. Here are some simple methods you can use to [convert date to text in Excel](https://trumpexcel.com/convert-date-to-text-excel/)
.

I hope you found this Excel tutorial useful!

**You may also like the following Excel tutorials:**

*   [How to Remove Cell Formatting in Excel](https://trumpexcel.com/remove-cell-formatting-in-excel/)
    
*   [How to Remove Time from Date/Timestamp in Excel](https://trumpexcel.com/remove-time-from-date-in-excel/)
    
*   [How to Wrap Text in Excel](https://trumpexcel.com/wrap-text/)
    
*   [Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [How to Stop Excel from Rounding Numbers](https://trumpexcel.com/stop-excel-from-rounding-numbers/)
    
*   [How to Display Numbers as Fractions in Excel (Write Fractions in Excel)](https://trumpexcel.com/display-numbers-as-fractions-excel/)
    
*   [How to Compare Dates in Excel (Greater/Less Than, Mismatches)](https://trumpexcel.com/compare-dates-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “How to Stop Excel from Changing Numbers to Dates Automatically”
------------------------------------------------------------------------------

1.  This is fine for creating new documents but does not work if you are opening a file that already contains data that could be construed as a date.
    
    example 91 06 27 ,for my system, becomes ’27/06/2091 using the apostrophe or 69941 by formatting as text. I will get the same DATE value if the data is 27 06 91 or 06 27 91 but they are obviously different.
    
    You cannot parse this data or perform any text functions on it.
    
    However if I save the sheet as a CSV file and use a text editor to open it, the value remains 90 06 27 , so the original data has not been modified.
    
    [Reply](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/#comment-40754)
    
2.  All of the solutions which suggest changing the format to text miss the point that you can then no longer use the data for calculations. Anything pasted into excel from say a web site will change numbers to text and they can no longer be used in calculations.  
    it is an annoying and ridiculous (and time consuming feature to cope with) of the latest excel software. None of the suggested solutions I have found actually work apart from time wasting manual changing.
    
    [Reply](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/#comment-14809)
    
3.  These can reverse the format, but it doesn’t give the original value. How can you simply prevent Excel from doing this?
    
    [Reply](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/#comment-14083)
    
4.  Entering extra spaces etc. helps if you are enetring values manually. However, there’s a bigger problem if you are importing data from a text- or .csv-file.  
    I have no solution for preventing excel chancing numerical values with decimal points to dates. How can I do that??
    
    [Reply](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/#comment-13540)
    
5.  another way, which avoids the apostrophe, is to enter =”1/2″, then copy that and paste as values; no need to format anything – useful if you have many values to enter which can be formularised (you can’t enter a formula in a cell formatted as text)
    
    [Reply](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/#comment-13146)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/#respond)

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