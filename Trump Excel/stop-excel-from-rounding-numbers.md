# How to Stop Excel from Rounding Numbers (Decimals/Fractions)

**Source:** https://trumpexcel.com/stop-excel-from-rounding-numbers

---

[Skip to content](https://trumpexcel.com/stop-excel-from-rounding-numbers/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/stop-excel-from-rounding-numbers/#below-title)

Excel is an amazingly well-developed spreadsheet tool that has been designed to maximize the efficiency of its users.

While it works as expected in most of the cases, in some cases, it can be a little counterproductive.

One such area is when Excel decides to round-off numbers (arghhh).

In this tutorial, I will show you how to take control and **stop Excel from rounding numbers**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/stop-excel-from-rounding-numbers/#)

Why Excel Rounds Off Numbers?
-----------------------------

Here are some possible reasons why Excel might be rounding off numbers:

1.  The [column width](https://trumpexcel.com/copy-column-width-excel/)
     is not enough to accommodate all the numbers, so Excel ends up rounding numbers so that it can fit the final value in the cell that it can display completely
2.  The number is too large and it’s shown in the exponential format
3.  Excel can only display numbers up to 15 digits, and any number longer than this will show 0 instead of the number after the 15th digit
4.  The [cell is formatted](https://trumpexcel.com/excel-custom-number-formatting/)
     in a way to round off numbers and only show specific digits (or specific digits after decimal) in a number

Now the table look at each of these scenarios and how you can stop Excel from rounding numbers in each case

Stop Rounding Number By Increasing Column Width
-----------------------------------------------

When you enter a number in a cell, Excel tries it’s best to fit that number in the given width of the cell.

And in case the width of the column in which the number is entered is not enough, Excel does the next best thing – it rounds the number to show the value in the cell (while still keeping the original number in the cell).

As you can see below in the screenshot, I have entered a large number (12354.546) which is fully visible in the formula bar, but it’s rounded off in the cell.

![Number with decimal digits getting rounded off](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20416%20143'%3E%3C/svg%3E)

**How to Fix this:**

All you need to do is increase the [column width](https://trumpexcel.com/lock-row-height-column-width-excel/)
 and make it wide enough so that the numbers have space to be fully displayed.

To do this, place your cursor at the edge of the column header (the column alphabet). You will notice that your cursor changes into a double-pointed arrow. [Double click](https://trumpexcel.com/mouse-double-click/)
 and it would [autofit the column width](https://trumpexcel.com/autofit-excel/)
 to accommodate the content that takes the most width.

Stop Excel from Rounding Large Numbers
--------------------------------------

When it comes to entering large numbers in Excel, there are a couple of reasons why Excel maybe rounding your large numbers.

*   The cell format is set to General, and only shows a specific number length
*   The number is longer than 15 digits and any number after the 15th digit is shown as 0

Let’s go through each of these scenarios and see how we can stop Excel from rounding our numbers in each case

### Changing the Cell Format from General to Number

When the cell format is set to General, Excel only shows a specific number of digits in a cell, and any number exceeding it is shown in the exponential format (also called the scientific format).

Below is an example of an exponential format number in cell A2.

![12 digit number gets rounded off](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20533%20220'%3E%3C/svg%3E)

As you can see in the screenshot above, when I have a number that is 11 digits long, Excel has no issues showing the entire number.

But when I have a number that is 12 digits long, except converts it into the exponential format.

**How to Fix this:**

This one has an easy fix. All you need to do is change the format of the cell from General to Number.

Below the steps to do this:

1.  Select the cells or range of cells for which you want to change the format
2.  Click the Home tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20403%20201'%3E%3C/svg%3E)
3.  In the Number group, click on the formatting dropdown![Select the Number format from the drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20549'%3E%3C/svg%3E)
4.  Select ‘Number’ as the format

The above steps should make your numbers show up as expected.

When you change the cell format to Number format, Excel automatically adds 2 digits after the decimal point. If you don’t want these, click on to Decrease decimal icon in the ribbon (it’s in the Home tab).

![Decrease decimal icon in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20403%20159'%3E%3C/svg%3E)

Also, in case you see a series of hash symbols instead of the number in the cell, simply expand the column. Once the column is wide enough to accommodate the entire number, you should see the number.

### Making the Number Text to Show More than 15 Digits

Another issue that you may face when working with large numbers in Excel is that after 15 digits in a number, Excel converts any digit into 0.

This is by design and Excel only considers 15 digits as significant, and any digit after that is automatically converted into a 0.

This can be a problem when you are working with large numbers (such as Credit Card numbers or Order Numbers).

Below is an example where when I enter the digit 1, 16 times in a cell, the first 15 instances are shown and the 16th one is converted into a 0.

![Excel converting digits after the 15 digit into 0](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20445%20161'%3E%3C/svg%3E)

_Caution: Unlike other methods, it’s not that Excel is just showing me 0 after the 15th digit and has the actual number in the back end. Even in the back end, Excel converts the digits after the 15th digit into 0._  

**How to Handle this:**

To stop Excel from doing this, you need to convert your number into a text format. While Excel is pre-programmed to treat numbers in a certain way, it doesn’t mess around with the text format (thankfully).

And the simplest way to do this would be to add an apostrophe before the number.

This would force Excel to consider anything that follows the apostrophe as a text string, and at the same time, as soon as you hit enter the apostrophe would not be shown in the cell (so you would be able to see the entire number without the apostrophe)

Below is an example, where the number in cell A1 has an apostrophe before it and shows the entire number, but the number in cell A2 does not have an apostrophe and converts the last digit into a 0

![Apostrophe added to convert number into text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20485%20175'%3E%3C/svg%3E)

Stop Excel from Rounding Decimal Numbers / Currencies
-----------------------------------------------------

Excel also gives the users the flexibility to decide how many digits after the decimal place should show up.

This may also mean that in case you have more digits after the decimal, these would get rounded off only to show the specified number of digits.

This is often the case when you’re using the currency format or the accounting format, where the numbers always show up with two digits after the decimal point. And if you have a number that has three or four or 5 digits after the decimal point, it’s rounded off to only show two digits.

Below is an example where I have a number with more than two digits after the decimal, but it’s rounded and only two digits are shown

![Number shows with only two digits after decimal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20405%20163'%3E%3C/svg%3E)

**How to Fix this:**

This is happening because of the number format of the cells in which you have the numbers.

And to stop Excel from rounding these numbers, change the cell format so that it can show more numbers than what it’s showing currently.

Below the steps to change the cell format and make more numbers show up:

1.  Select the cells that have the numbers
2.  Hold the Control Key and press the 1 key (this will open the Format cells dialog box)
3.  Make sure you’re in the ‘Number’ tab![Select the Number tab in the Format Cells dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20464'%3E%3C/svg%3E)
4.  Select Number in the left pane (or Currency/Accounting if you’re using those formats)
5.  Change the ‘Decimal places’ value from 2 to 3 or 4 (or whatever number of digits you want to display).![Change the Decimal Place](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20464'%3E%3C/svg%3E)
6.  Close the dialog box

The above steps would make sure that Excel always shows your numbers with a specified number of digits after the decimal. Any more digits after the specified value would be rounded (which is acceptable in most cases)

Also, note that none of this actually changes the value in the cell. It only changes the way it is being displayed.

So if you enter a number that has five digits after the decimal point, and only two show up in the cell, the original number still remains as you entered it.

So these are some of the ways you can **stop Excel from rounding numbers**.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [How to Round to the Nearest Integer or Multiple of 0.5 / 5 / 10 in Excel](https://trumpexcel.com/round-to-nearest-integer/)
    
*   [How to Use Excel ROUND Function](https://trumpexcel.com/excel-round-function/)
    
*   [Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [How to Display Numbers as Fractions in Excel (Write Fractions in Excel)](https://trumpexcel.com/display-numbers-as-fractions-excel/)
    
*   [Round to the Nearest 1000 in Excel](https://trumpexcel.com/round-to-nearest-1000-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Stop Excel from Rounding Numbers (Decimals/Fractions)”
---------------------------------------------------------------------------

1.  I need to use these 15+ digit values in a formula (XLOOKUP), but as text I get the #VALUE! error message. Is this just a limitation of Excel? I’m surprised this is not something they’ve fixed.
    
    [Reply](https://trumpexcel.com/stop-excel-from-rounding-numbers/#comment-33322)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/stop-excel-from-rounding-numbers/#respond)

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