# How to Remove Leading Zeros in Excel (5 Easy Ways)

**Source:** https://trumpexcel.com/remove-leading-zeros-excel

---

[Skip to content](https://trumpexcel.com/remove-leading-zeros-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-leading-zeros-excel/#below-title)

Many people have a love-hate relationship with leading zeros in Excel.

Sometimes you want it, and sometimes you don’t.

While Excel has been programmed in such a way that it automatically removes any leading zeros from the numbers, there are some cases when you may have these.

In this Excel tutorial, I will show you **how to remove the leading zeros** in your numbers in Excel.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-leading-zeros-excel/#)

Possible Reasons You May Have Leading Zeros in Excel
----------------------------------------------------

As I mentioned, Excel automatically removes any leading zeros from numbers. For example, if you enter 00100 in a cell in Excel, it would automatically convert it into 100.

In most cases, this makes sense as these leading zeros are not really meaningful.

But in some cases, you may want it.

Here are some possible reasons that may cause your numbers to retain the leading zeros:

*   If the number has been formatted as text (mostly by adding an apostrophe before the number), it would retain the leading zeros.
*   The cell may have been formatted in such a way that it always shows a certain length of a number. And in case the number is smaller, leading zeros are added to make up for it. For example, you can format a cell to always show 5 digits (and if the number is less then five digits, leading zeros are added automatically)

The method we choose to remove the leading zeros would depend on what is causing it.

Also read: [How to Add Leading Zeroes in Excel](https://trumpexcel.com/add-leading-zeroes-excel/)

So, the first step is to identify the cause so that we can choose the right method to remove these leading zeros.

How to Remove Leading Zeros from Numbers
----------------------------------------

There are multiple ways you can use to remove the leading zeros from numbers.

In this section, I will show you five such methods.

### Convert the Text to Numbers Using the Error Checking Option

If the cause of leading numbers is that someone has added apostrophe before these numbers (to convert these into text), you can use the error checking method to convert these back into numbers with a single click.

This is probably the easiest method to get rid of leading zeros.

Here I have a data set where I have the numbers that have an apostrophe before these as well as the leading zeros. This is also the reason you see these numbers aligned to the left (whereas by default numbers align to the right) and also have the leading 0’s.

![Numbers with leading zeros and apostrophe](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20405'%3E%3C/svg%3E)

Below are the steps to remove these leading zeros from these numbers:

1.  Select the numbers from which you want to remove the leading zeros. You will notice that there is a yellow icon at the top right part of the selection.![Select the cells that have the numbers and yellow icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20425'%3E%3C/svg%3E)
2.  Click on the yellow error checking icon
3.  Click on ‘Convert to Number’![Select Convert to Numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20345%20427'%3E%3C/svg%3E)

That’s it! The above steps would [remove the apostrophe](https://spreadsheetplanet.com/remove-apostrophe-in-excel/)
 and convert these text values back into numbers.

![Data from which leading zeros have been removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20291%20433'%3E%3C/svg%3E)

And since Excel is programmed to remove leading spaces from any numbers by default, you’ll see that doing this automatically removes all the leading zeros.

Note: This method would not work if the leading zeros have been added as a part of the custom number formatting of the cells. To handle those cases, use the methods covered next.

### Change the Custom Number Formatting of the Cells

Another really common reason that may make your numbers show up with leading zeros is when your cells have been formatted to always show a specific number of digits in each number.

A lot of people want to make the numbers look consistent and of the same length, so they specify the minimum length of the numbers by changing the formatting of the cells.

For example, if you want all the numbers to show up as 5 digits numbers, if you have a number which is only three-digit Excel would automatically add two leading zeros to it.

Below I have a dataset where custom number formatting has been applied to always show a minimum of five digits in the cell.

![Number with leading zeros because of custom number formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20404'%3E%3C/svg%3E)

And the way to get rid of these leading zeros is just to remove the existing formatting from the cells.

Below are the steps to do this:

1.  Select the cells that have the numbers with the leading zeros
2.  Click the Home tab![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20550%20201'%3E%3C/svg%3E)
3.  In the Numbers group, click on the Number Format dropdown![Click on the Number Format dropd down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20582%20202'%3E%3C/svg%3E)
4.  Select ‘General’![Select the General Format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20469%20715'%3E%3C/svg%3E)

The above steps would change the custom number formatting of the cells and now the numbers would be displayed as expected (where there would be no leading zeros).

Note that this technique would only work when the reason for the leading zeroes was custom number formatting. It would not work if an apostrophe has been used to [convert numbers to text](https://trumpexcel.com/convert-numbers-to-text-excel/)
 (in which case you should use the previous method)

### Multiply by 1 (using Paste Special technique)

This technique works in both scenarios (where the numbers have been converted into text by using an apostrophe or a custom number formatting has been applied to the cells).

Suppose you have a data set as shown below and you want to remove the leading zeros from it.

![Dataset with leading zeros with apostrophe and custom formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20250%20401'%3E%3C/svg%3E)

Below are the steps to do this

1.  Copy any empty cell from the worksheet
2.  Select the cells where you have the numbers from which you want to remove the leading zeros
3.  Right-click on the selection and then click on Paste Special. This will open the Paste Special dialog box![Click on Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20416%20549'%3E%3C/svg%3E)
4.  Click on the ‘Add’ option (in the operations group)![Clcik on the Add option in the Paste Special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20429'%3E%3C/svg%3E)
5.  Click OK

The above steps add 0 to the range of cells you selected and also remove all the leading zeros and apostrophe.

![Data converted where leading zeros are removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20342%20446'%3E%3C/svg%3E)

While this does not change the value of the cell, it converts all the text values into numbers as well as copies the formatting from the blank cell that you copied (thereby replacing the existing formatting that was making the leading zeros show up).

This method only impacts the numbers. In case you have any text string in a cell, it would remain unchanged.

### Using the VALUE function

Another quick and easy method to remove the leading zeros is to use the value function.

This function takes one argument (which could be the text or the cell reference that has the text) and returns the numerical value.

This would also work in both scenarios where your leading numbers are a result of the apostrophe (used to convert numbers to text) or the custom number formatting.

Suppose I have a data set as shown below:

![Data with zeros to be removed with formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20403'%3E%3C/svg%3E)

Below is the formula that would remove the leading zeros:

\=VALUE(A1)

![VALUE formula to remove leading zeros](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20453%20452'%3E%3C/svg%3E)

Note: In case you still see the leading zeros, you need to go to the home tab and change the cell format to General (from the Number Format dropdown).

### Using Text to Columns

While the Text to Columns functionality is used to [split a cell into multiple columns](https://trumpexcel.com/split-cells-in-excel/)
, you can also use it to remove the leading zeros.

Suppose you have a data set as shown below:

![Data with zeros to be removed with formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20403'%3E%3C/svg%3E)

Below are the steps to remove leading zeros using Text to Columns:

1.  Select the range of cells that have the numbers
2.  Click on the ‘Data’ tab![Click on the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20664%20203'%3E%3C/svg%3E)
3.  In the Data Tools group, click on ‘Text to Columns’![Click on Text to Columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20617%20202'%3E%3C/svg%3E)
4.  In the ‘Convert Text to Columns’ wizard, make the following changes:
    1.  Step 1 of 3: Select ‘Delimited’and click on Next![Select delimited](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20755%20538'%3E%3C/svg%3E)
    2.  Step 2 of 3: Deselect all the delimiters and click on Next![Deselect all delimiters](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20755%20538'%3E%3C/svg%3E)
    3.  Step 3 of 3: Select a destination cell (B2 in this case) and click on Finish![Select the destination cell and click on Finish](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20755%20538'%3E%3C/svg%3E)

The above steps should remove all the leading zeros and give you only the numbers. In case you still see the leading zeros, you need to change the formatting of the cells to General (this can be done from the Home tab)

How to Remove Leading Zeros from Text
-------------------------------------

While all the above methods work great, these are meant for only those cells that have a numerical value.

But what if you have alphanumeric or text values that also happened to have some leading zeros in it.

The above methods would not work in that case, but thanks to amazing formulas in Excel, you can still get this time.

Suppose you have a data set as shown below and you want to remove all the leading zeros from it:

![Alphanumeric dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20484%20265'%3E%3C/svg%3E)

Below is the formula to do that:

\=RIGHT(A2,LEN(A2)-FIND(LEFT(SUBSTITUTE(A2,"0",""),1),A2)+1)

![Formula to remove zero from alphanumeric string](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20681%20368'%3E%3C/svg%3E)

Let me explain how this formula works

The [SUBSTITUTE](https://trumpexcel.com/excel-substitute-function/)
 part of the formula replaces the zero with a blank. So for the value 001AN76, the substitute formula gives the result as 1AN76

The [LEFT formula](https://trumpexcel.com/excel-left-function/)
 then extracts the left-most character of this resulting string, which would be 1 in this case.

The [FIND formula](https://trumpexcel.com/excel-find-function/)
 then looks for this left-most character given by the LEFT formula and returns its position. In our example, for the value 001AN76, it would give 3 (which is the position of 1 in the original text string).

1 is added to the result of the FIND formula, to make sure that we get the entire text string extracted (except the leading zeros)

The result of the FIND formula is then subtracted from the result of the [LEN formula](https://trumpexcel.com/excel-len-function/)
 (which is used to give the length of the entire text string). This gives us the length of the text ring without the leading zeros.

This value is then used with the [RIGHT function](https://trumpexcel.com/excel-right-function/)
 to extract the entire text string (except the leading zeros).

In case there is a possibility that there may be [leading or trailing spaces](https://trumpexcel.com/remove-spaces-in-excel-leading-trailing/)
 in your cells, it’s best to use the [TRIM function](https://trumpexcel.com/excel-trim-function/)
 with every cell reference.

So the new formula with the TRIM function added would be as shown below:

\=RIGHT(TRIM(A2),LEN(TRIM(A2))-FIND(LEFT(SUBSTITUTE(TRIM(A2),"0",""),1),TRIM(A2))+1)

So, these are some easy ways that you can use to remove leading zeros from your data set in Excel.

I hope you found this tutorial useful!

**Other Excel tutorials you may like:**

*   [Hide Zero Values in Excel | Make Cells Blank If the Value is 0](https://trumpexcel.com/hide-zero-values-excel/)
    
*   [How to Replace Blank Cells with Zeros in Excel Pivot Tables](https://trumpexcel.com/replace-blank-cells-with-zeros-excel-pivot-tables/)
    
*   [Delete Rows Based on a Cell Value (or Condition) in Excel](https://trumpexcel.com/delete-rows-based-on-cell-value/)
    
*   [How to Stop Excel from Changing Numbers to Dates](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/)
    
*   [How to Convert Serial Numbers to Dates in Excel](https://trumpexcel.com/convert-serial-numbers-to-dates-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-leading-zeros-excel/#respond)

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