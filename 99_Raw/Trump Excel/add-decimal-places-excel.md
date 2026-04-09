# How to Add Decimal Places in Excel (Automatically)

**Source:** https://trumpexcel.com/add-decimal-places-excel

---

[Skip to content](https://trumpexcel.com/add-decimal-places-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/add-decimal-places-excel/#below-title)

When you’re working with data in Excel, most of the time you’ll have to deal with decimals (especially if you’re working with currency data or accounting numbers).

In an attempt to make Excel a smart and more user-friendly tool, there are some in-built features that end up being a little bit of an irritation.

Working with decimals, you will likely face such an issue.

Let me explain!

If you type 10.00 in a cell in Excel, it would automatically convert this to 10 by removing the zeros after the decimal. While this is a smart thing to do, sometimes, you may want all your numbers to show a specific number of digits after the decimal, even if these are zeros.

In this tutorial, I will show you how to **automatically add decimals to the numbers in Excel**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/add-decimal-places-excel/#)

Format Cells to Show Fixed Number Length after Decimal Point
------------------------------------------------------------

In some cases, you may want to have consistent numbers, where there are always two or three numbers after the decimal point (as shown below).

![Data with two decimal numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20280%20267'%3E%3C/svg%3E)

While Excel does not allow this by default (as it doesn’t allow only zeros after the decimal number), you can easily change this by modifying the custom number formatting of the cells.

Below are the steps to make sure that your numbers always show at least 2 numbers after the decimal point.

1.  Select the cells that have the numbers where you want to add the decimal point
2.  Click the ‘Home’ tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20365%20182'%3E%3C/svg%3E)
3.  In the Number group, click on the dialog box launcher (the small, tilted arrow at the bottom right of the group). you can also use the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
     Control + 1![Click on the dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20365%20149'%3E%3C/svg%3E)
4.  In the Number tab, within Category options, select Number![Click on the Number option in Format cells dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20657'%3E%3C/svg%3E)
5.  Change the ‘Decimal places’ value to 2 (or 3 in case you want three decimal numbers)![vSpecify the decimal point position](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20657'%3E%3C/svg%3E)
6.  Click OK

The above steps would make sure that all the numbers now show two numbers after the decimal point.

Even if you have a whole number, a decimal point and two zeros after the decimal point would automatically be added to these numbers.

In case there are more numbers after the decimal point, those would be rounded. For example, 91.333 would be changed to 91.33, and 91.338 would be changed to 91.34.

Note: While the format cells dialog box gives you more control over how we want your numbers to be displayed, if all you want to do is show two numbers after the decimal point, you can also do that by selecting the number formatting option in the format options drop-down in the Number group in the Home tab

![Select the Number formatting from the drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20458'%3E%3C/svg%3E)

Also read: [How to Convert Fraction to Decimal in Excel](https://trumpexcel.com/convert-fraction-to-decimal-excel/)

Automatically Add Decimal Point to Numbers While Typing
-------------------------------------------------------

Another thing that you can do with Excel is automatically inserting a decimal point in the numbers of white you are typing these numbers.

For example, if you want to have two numbers after the decimal point in all the numbers that you type, then you can change a setting in Excel so that you can simply type the number in the decimal point would automatically be inserted (you won’t have to manually enter the decimal point yourself).

Below are the settings that you need to change to enable this:

1.  Click the File tab![Click the File tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20360%20180'%3E%3C/svg%3E)
2.  Click on Options![Click on Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20566'%3E%3C/svg%3E)
3.  In the [Excel Options](https://trumpexcel.com/excel-options-hacks/)
     dialog box that opens up, click on the ‘Advanced’ option in the left pane![Click on the Advanced option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20639'%3E%3C/svg%3E)
4.  In the editing options, enable the setting – “Automatically insert or decimal point”![Select automatically insert decimal places](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%20612'%3E%3C/svg%3E)
5.  You can also specify how many numbers you want after the decimal point (the default being 2)
6.  Click OK

After this setting is enabled, whenever you enter a number in a cell in Excel, it would automatically insert a decimal point before 2 numbers.

For example, if you enter 1 in a cell, it would be converted into .01. If you enter 1234, it would be converted into 12.34

While I don’t recommend this setting to be enabled in general, it’s a good option when you’re manually entering the data and want to save some time.

Note that this setting would only affect the numbers that you enter after you have enabled the setting. All the numbers that were already there in the worksheet would remain unchanged

Once you are done with the [data entry](https://trumpexcel.com/excel-data-entry-tips/)
, you can go back to the same Excel options dialog box and disable this setting.

So these are two methods that you can use to add decimal places to numbers in Excel. The first method using [custom number formatting](https://trumpexcel.com/excel-custom-number-formatting/)
 is what you would need in most cases.

But in case you are doing manual [data entry](https://trumpexcel.com/data-entry-form/)
 and want to save some time by not entering the decimal point (and still getting a consistent result with decimals), you can use the second method.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [Convert Time to Decimal Number in Excel (Hours, Minutes, Seconds)](https://trumpexcel.com/convert-time-to-decimal-in-excel/)
    
*   [How to Remove Comma in Excel (from Text and Numbers)](https://trumpexcel.com/remove-comma-excel/)
    
*   [How to Remove Leading Zeros in Excel](https://trumpexcel.com/remove-leading-zeros-excel/)
    
*   [How to Add Leading Zeros in Excel](https://trumpexcel.com/add-leading-zeroes-excel/)
    
*   [Round to the Nearest 1000 in Excel](https://trumpexcel.com/round-to-nearest-1000-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/add-decimal-places-excel/#respond)

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