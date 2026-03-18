# Change Negative Number to Positive in Excel [Remove Negative Sign]

**Source:** https://trumpexcel.com/change-negative-to-positive-in-excel

---

[Skip to content](https://trumpexcel.com/change-negative-to-positive-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/change-negative-to-positive-in-excel/#below-title)

**Watch Video – Convert Negative Number to Positive in Excel**

Most of the people who work with Excel spreadsheets deal with numbers in large/small datasets.

And when you work with numbers, you will have all types of it (positive, negative, decimals, date/time).

One of the common tasks a lot of us need to do often is to convert these numbers from one format to another.

And probably the most common one is when you have to **change negative numbers to positive numbers** (**remove the negative sign**) for some calculations.

And again, there are multiple ways you can do this in Excel.

In this tutorial, I will show you some simple ways to change negative numbers to positive in Excel (using formulas, a copy-paste technique, and other awesome methods).

So if you’re interested, keep reading!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/change-negative-to-positive-in-excel/#)

Multiply with minus 1 to Convert Negative Number to Positive
------------------------------------------------------------

If you have a column full of numbers and you want to quickly get the numbers where negatives have been converted into positive, you can easily do that by multiplying these negative values by -1.

But you also have to ensure that you’re only multiplying the negative numbers and not the positive ones.

Suppose you have a dataset as shown below:

![Dataset where negative sign needs to be removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20249%20340'%3E%3C/svg%3E)

Below is the formula that will convert negative numbers to positives and keep the rest unchanged:

\=IF(A2>0,A2,-A2)

![Formula to convert negative numbers to positive numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20454%20404'%3E%3C/svg%3E)

The above formula uses the IF function to first check whether the number is positive or not. If it’s positive, the sign is not changed and if it’s negative, a negative sign is added to the reference, which ends up giving us a positive number only.

In case you have text values in the dataset as well, this function is going to ignore that (and only negative values will be changed)

Now that you have the required result, you can [convert these formulas to values](https://trumpexcel.com/convert-formulas-to-values-excel/)
 (and copy it over the original data in case you don’t need it)

Use the ABS function to Change all Negative Numbers to Positive
---------------------------------------------------------------

Excel has a dedicated function that strips out the negative sign and gives you the absolute value.

.. the **ABS function**

Suppose you have the dataset as shown below and you want to change negative values to positive values.

Below is the formula that will do this:

\=ABS(A2)

![ABS function to change negative numbers to positive values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20404%20399'%3E%3C/svg%3E)

The above ABS function doesn’t impact the positive numbers but converts negative numbers into positive values.

Now that you have the required result, you can [convert these formulas to values](https://trumpexcel.com/convert-formulas-to-values-excel/)
 (and copy it over the original data in case you don’t need it)

One minor drawback of the ABS function is that it can only work with numbers. In case you have text data in some of the cells and you use the ABS function, it will give you [#VALUE! error](https://trumpexcel.com/fix-value-error-in-excel/)
.

Multiply Using Paste Special To Reverse the Sign
------------------------------------------------

In case you want to reverse the sign of the number (i.e., change negative to positive and positive to negative), you can also use this [paste special multiplication](https://trumpexcel.com/multiply-in-excel-using-paste-special/)
 technique.

Suppose you have the dataset as shown below and you want to reverse the sign:

Below are the steps to reverse the sign using Paste Special:

1.  In any empty cell in the worksheet, enter -1![Enter -1 in any empty cell in the worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20470%20346'%3E%3C/svg%3E)
2.  Copy this cell (which has the value -1)
3.  Select the range where you want to reverse the sign.
4.  Right-click on any of the selected cells
5.  Click on Paste Special. This will open the Paste Special dialog box![Click on Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20460%20358'%3E%3C/svg%3E)
6.  In the Paste option, select ‘Values’![Select values in Paste Special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20429'%3E%3C/svg%3E)
7.  In the Operation  options, select ‘Multiply’![Select multiply in the Paste Special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20468%20429'%3E%3C/svg%3E)
8.  Click Ok
9.  Delete -1 from the cell

You would notice that the above steps instantly change reverses the sign of the number (i.e., positive numbers become negative and negative numbers become positive).

But what if you only want to convert negative numbers to positive numbers and not the other way round?

In that case, you somehow first need to select all the negative numbers and then follow the above steps.

Here is how to select only the negative numbers in Excel:

1.  Select the entire dataset
2.  Hold the Control key and then press the F key. This will open the Find and Replace dialog box.
3.  In the Find what field, enter – (the minus sign)
4.  Click on Find All
5.  Hold the Control Key and press the A key.

The above steps would select only those cells that have a negative sign. Now that you have these cells selected, you can use the Paste Special technique to change the sign of only the negative numbers.

This technique has two advantages over the formula technique (the two methods covered before this):

1.  It doesn’t require you to add an additional column and then use a formula to get the result in that column. You can use this on your existing dataset.
2.  You don’t need to convert the formulas to values (as the result you get is already value and not a formula)

Flash Fill To Remove the Negative Sign
--------------------------------------

[Flash Fill](https://trumpexcel.com/flash-fill-excel/)
 is a new functionality that was introduced in Excel 2013.

It allows you to quickly identify patterns and then give you the result where the pattern has been applied to the entire dataset.

One use of this is when you have names and you want to separate first name and last name. As soon as you type the first name in an adjacent cell a couple of times, Flash Fill will identify the pattern and give you all the first names.

Similarly, you can use it to quickly **remove the negative sign** from a number, while the positive values remain unchanged.

Below is a dataset where I have the negative numbers and I want to change these to positives values.

Below are the steps to change negative numbers to positive numbers using Flash Fill:

1.  In the adjacent to the one with the data, enter the expected result manually. In this example, I will manually enter 874
2.  In the cell below it, enter the expected result (162 in this example)
3.  Select both the cells
4.  Place the cursor over the bottom right part of the selection. It will change into a plus icon
5.  Click and drag to fill the column (or double-click)
6.  Click on the AutoFill Options icon
7.  Click on Flash Fill

![Flash fill to remove the negative sign](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%20480'%3E%3C/svg%3E)

The above steps would give you the expected result, where the negative sign has been removed.

One thing you need to remember when using this method is that Excel relies on guessing the pattern. So you will have to at least show Excel that you are converting a negative number to positive.

This means that you will have to manually enter the expected result until you have covered at least one negative number.

Convert Negative Numbers to Postive with a Single Click (VBA)
-------------------------------------------------------------

And lastly, you can also use VBA to convert negative values to positive values.

I would recommend using this method if doing this is something you have to do often. Maybe you regularly get the dataset from a database or a colleague and you have to do this every time.

In such a case, you can create and save the VBA macro code to the Personal Macro Workbook and place the VBA in the Quick Access Toolbar. This way, the next time you get a dataset where you have to do this, you simply select the data and click on the icon in the QAT…

… and you’ll be done!

Don’t worry, I will show you the exact steps to get this up and running.

Below is the VBA code that will convert negative values to positive values in the selected range:

Sub ChangeNegativetoPOsitive()
For Each Cell In Selection
    If Cell.Value < 0 Then
        Cell.Value = -Cell.Value
    End If
Next Cell
End Sub

The above code uses the [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to go through each cell in the selection. It uses the [IF statement](https://trumpexcel.com/if-then-else-vba/)
 to check whether the cell value is negative or not. If the value is negative, the sign is reversed, and if it’s not, it’s ignored.

You can add this code to a regular module in a workbook (if you only want to use this in that workbook). And in case you want to use this macro code in any workbook on your system, you can save it in a personal macro workbook.

Here are the steps to [get the Personal Macro Workbook (PMW)](https://trumpexcel.com/personal-macro-workbook/#Where-Can-I-Find-the-Personal-Macro-Workbook)
.

Here are the steps to [save this code in the PMW](https://trumpexcel.com/personal-macro-workbook/#How-to-Copy-Macros-in-the-Personal-Macro-Workbook)
.

Now let me show you how to add this code to the Quick Access Toolbar (steps are the same whether you save this code in a single workbook or in the PMW)

1.  Open the workbook where you have the data
2.  Add the VBA code to the workbook (or to the PMW)
3.  Click on the ‘Customize Quick Access Toolbar’ option in the QAT![Click on the Customize Quick Access Toolbar option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20199'%3E%3C/svg%3E)
4.  Click on ‘More Commands’![Click on More commands](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20523%20531'%3E%3C/svg%3E)
5.  In the Excel Options dialog box, click on the ‘Choose Commands from’ drop-down
6.  Click on Macros. This will show you all the macros in the workbook (or the Personal Macro Workbook)![Click on Macros in the Excel Options drop down](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20546%20408'%3E%3C/svg%3E)
7.  Click on the ‘Add’ button![Click on the Add button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20460'%3E%3C/svg%3E)
8.  Click OK

Now you will have the macro icon in the QAT.

![Macro button in the QAT](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20381%20197'%3E%3C/svg%3E)

To use this macro with a single click, simply make the selection and click on the macro icon.

Note: In case you’re saving the VBA macro code in the workbook, you need to save the workbook in the macro-enabled format (XLSM)

I hope you found this Excel tutorial useful.

**You may also like the following Excel tutorials:**

*   [Convert Date to Text in Excel](https://trumpexcel.com/convert-date-to-text-excel/)
    
*   [Show Negative Numbers in Parentheses (Brackets) in Excel](https://trumpexcel.com/show-negative-numbers-parentheses-brackets-excel/)
    
*   [How to Add Plus Sign Before Numbers in Excel](https://trumpexcel.com/add-plus-sign-before-numbers-excel/)
    
*   [Convert Text to Numbers in Excel](https://trumpexcel.com/convert-text-to-numbers-excel/)
    
*   [How to add serial numbers to rows in Excel](https://trumpexcel.com/number-rows-in-excel/)
    
*   [How to Stop Excel from Changing Numbers to Dates](https://trumpexcel.com/stop-excel-from-changing-numbers-to-dates/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/change-negative-to-positive-in-excel/#respond)

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