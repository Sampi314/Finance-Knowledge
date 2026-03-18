# How to Remove Comma in Excel (from Text and Numbers)

**Source:** https://trumpexcel.com/remove-comma-excel

---

[Skip to content](https://trumpexcel.com/remove-comma-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-comma-excel/#below-title)

A comma is commonly used when working with both text and numbers in Excel.

With text, a comma can be used as a separator (such as a separator between the first and last name or address) or as a part of regular grammar.

And with numbers, it often used to make the numbers more readable (a thousand separators is the most common use of comma with numbers).

While comma does help make the data a lot more readable, sometimes, you may want to remove all the commas from the data (or remove specific instances of the comma).

In this tutorial, I will show you some simple ways to **remove comma in Excel** from text and numbers.

So let’s get started!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-comma-excel/#)

Remove Comma from Numbers
-------------------------

When working with numbers in Excel, you can apply various formats to the cells and the numbers would be displayed accordingly.

Since these commas are part of the formating and not the number itself, we need to edit the formatting to remove these commas from the numbers.

Suppose you have a dataset as shown below and you want to get rid of the commas from the numbers in column B.

![Numbers from which the comma needs to be removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20322%20436'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the dataset (the one with the numbers)
2.  Click the Home tab in the ribbon![Click the home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20454%20200'%3E%3C/svg%3E)
3.  In the number group, click on the dialogue box launcher (the small slanted arrow icon at the bottom-right part of the group)![Click on the dialog box launcher](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20321%20175'%3E%3C/svg%3E)
4.  In the Format Cells dialogue box, make sure the Number tab is selected
5.  In the Category list, select Number (if not selected already)![Select the number option in the left pane](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20651'%3E%3C/svg%3E)
6.  Uncheck the ‘Use 1000 Separator (,)’ option and specify how many decimal digits you want![Uncheck the thousand separator option to remove comma from numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20651'%3E%3C/svg%3E)
7.  Click OK

The above steps would remove the comma from all the selected numbers.

![Numbers from which comma has been removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20323%20435'%3E%3C/svg%3E)

Tip: You can also use the keyboard shortcut **Control + 1** to open the format cells dialog box (after selecting the cells). Hold the Control key and then press the 1 key.

Remember that this method would only work where the comma was a part of the formatting and not the cell. To check this, select the cell and see the value in the formula bar. If you see commas in the formula bar, then these are not part of the formatting.

### Using the NUMBERVALUE Function

In case you have a situation where numbers are not actually numbers (but text) and you want to remove the comma from these numbers, you can use the [NumberValue function](https://support.microsoft.com/en-us/office/numbervalue-function-1b05c8cf-2bfa-4437-af70-596c7ea7d879)
.

This function does exactly this – [converts text to a number](https://trumpexcel.com/convert-text-to-numbers-excel/)
.

Suppose you have a dataset as shown below where someone has manually entered the comma (or it came as a part of a data download).

![Number with comma in it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20396%20491'%3E%3C/svg%3E)

You can see that these are not numbers as they align to the left in the cell (by default). Also, when you select a cell and see in the formula bar, you can see the commas as a part of the number (indicating that this is not numeric but text).

Below is the formula that will convert these text into numbers.

\=NUMBERVALUE(B2)

Copy this formula for all the cells in the column and you will have the numbers.

![NUMBERVALUE formula to convert text to numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20496%20492'%3E%3C/svg%3E)

There is a possibility that you may still see the comma in the result of the formula, but that would then be because of number formatting. You can use the previous method to remove these commas from the numbers.

Remove comma from Text String
-----------------------------

Removing comma from text string would work differently than removing comma from numbers.

With text strings, the comma is actually a part of the string and you need to find and then remove these commas somehow.

Let me show you a couple of methods to do this when you have the text data.

### Using Find and Replace

With [Find and Replace functionality](https://trumpexcel.com/find-and-replace-in-excel/)
, you can easily find all the commas in a cell and replace it will something else (blank or some other character).

Note that this method will only work with text data. In case you have numbers where the comma is because of the formatting, then this method will not remove the comma.

Suppose you have the names data as shown below where there is a comma between the first and the last name.

![Names dataset from which to remove comma](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20301%20310'%3E%3C/svg%3E)

Below are the steps to remove the comma from this names  dataset:

1.  Select the dataset
2.  Click the Home tab
3.  In the Editing group, click on the Find & Replace option
4.  Click on Replace. This will open the Find and Replace dialog box![Click on the replace option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20304%20526'%3E%3C/svg%3E)
5.  In the ‘Find what:’ field, enter **,** (a comma)![Enter comma in find and replace field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20255'%3E%3C/svg%3E)
6.  Leave the ‘Replace with:’ field empty. In case you want to remove the comma and replace it with something else, you should enter that in the ‘Replace with:’ field.
7.  Click on Replace All button![Click on replace all button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20575%20255'%3E%3C/svg%3E)

The above steps would remove all the commas from all the selected cells.

![Names data from which comma has been removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20301%20310'%3E%3C/svg%3E)

Note that the above steps would remove all the instances of commas from all the cells. So, if you have more that one comma in a cell, all the commas would be removed.

Also, this would change the original dataset. In case you want to keep the original data intact, first, create a backup copy or copy the data to another sheet/range and then use the above steps.

**Pro Tip**:  You can also use the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
 – Control + H to open the find and replace dialog box.

### Using SUBSTITUTE Formula

Another way to remove the comma is by using the [SUBSTITUTE function](https://trumpexcel.com/excel-substitute-function/)
, where you can substitute the comma with a blank or any other character.

Unlike the Find and Replace method where it removes all the commas in one go, with the SUBSTITUTE function, you get a bit more control (as we will see in the examples later in this section).

Suppose you have a dataset as shown below where you want to remove all the commas.

![names data with multiple commas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20327%20310'%3E%3C/svg%3E)

Below is the formula that will do this:

\=SUBSTITUTE(A2,",","")

![Substitute formula to remove all the commas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20593%20370'%3E%3C/svg%3E)

The above formula takes three arguments:

1.  The text (or [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
     containing the text) from which you want to remove the comma
2.  The character that you want to substitute (comma in this example)
3.  The character with which you want to remove the comma (blank in this example)

But what if you want to remove only the first comma and not the second one.

With SUBSTITUTE function, you can specify the number of instances that you want to substitute. This can be done using the fourth argument, which is an optional argument. In case you don’t specify this optional argument, the function will substitute all the instances of the specified character/string.

Suppose you have a dataset as shown below and you want to remove only the first comma and not the second one.

![names data with multiple commas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20327%20310'%3E%3C/svg%3E)

Below is the formula that will do this:

\=SUBSTITUTE(A2,",","",1)

![Formula to remove the first instance of the comma](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20594%20369'%3E%3C/svg%3E)

The above formula also uses the fourth argument (which is optional) – \[instance\_num\].

Specifying the instance number as 1 tells the formula that it should only substitute the first instance of the comma and leave all the other instances as is.

But what if you don’t want to remove the first comma, but instead substitute the second comma with a dash instead.

You can do that using the below formula:

\=SUBSTITUTE(A2,","," -",2)

![Formula to remove the second comma with dash](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20368'%3E%3C/svg%3E)

The above formula only does the substitution to the second instance of the comma and replaces it with a dash.

So, these are some simple ways to **remove the comma from numbers and text strings in Excel**.

I hope you found this tutorial useful!

**Other Excel tutorials you may like:**

*   [How to Remove Line Breaks in Excel](https://trumpexcel.com/remove-line-break-excel/)
    
*   [How to Remove Dashes (-) in Excel?](https://trumpexcel.com/remove-dashes-excel/)
    
*   [Change Negative Number to Positive in Excel \[Remove Negative Sign\]](https://trumpexcel.com/change-negative-to-positive-in-excel/)
    
*   [How to Remove the First Character from a String in Excel](https://trumpexcel.com/remove-first-character-from-string/)
    
*   [How to Remove Time from Date/Timestamp in Excel](https://trumpexcel.com/remove-time-from-date-in-excel/)
    
*   [Separate First and Last Name in Excel (Split Names Using Formulas)](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [How To Remove Text Before Or After a Specific Character In Excel](https://trumpexcel.com/remove-text-before-after-character-excel/)
    
*   [Remove Asterisk (\*) in Excel](https://trumpexcel.com/remove-asterisk-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-comma-excel/#respond)

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