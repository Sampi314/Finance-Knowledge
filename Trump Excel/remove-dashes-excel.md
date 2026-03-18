# How to Remove Dashes (-) in Excel? 4 Easy Ways!

**Source:** https://trumpexcel.com/remove-dashes-excel

---

[Skip to content](https://trumpexcel.com/remove-dashes-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-dashes-excel/#below-title)

Excel is a great tool when it comes to data manipulation. There are many functionalities and functions in Excel that allow you to modify your data to get the desired result quickly.

One common scenario is when you get your data with dashes/hyphens, and you want to remove them.

For example, below, I have the dummy data in the Social Security Numbers format where I want to remove the dashes in between the numbers.

In this tutorial, I will show you four easy methods to remove dashes in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-dashes-excel/#)

Method 1 – Remove Dashes Using Flash Fill
-----------------------------------------

If you have a consistent dataset, then the easiest way to remove dashes would be by using [Flash Fill](https://trumpexcel.com/flash-fill-excel/)
.

Flash Fill works by identifying patterns and giving you the result once you enter the expected result in one or two cells.

Let me show you how it works with a simple example.

Below I have a data set where I have the SSNs with dashes, and I want to remove these dashes and only get the numbers.

![Dataset to remove dashes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20435%20386'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Enter the expected result in Cell B2 (which is the first cell adjacent to our data set where we have the numbers from which we want to remove the dashes)

![Enter the expected result in Cell B2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20435%20383'%3E%3C/svg%3E)

2.  Hit the Enter key. This will bring the cursor to cell B3.
3.  Hold the **Control key and press the E key**. This is the shortcut to use Flash Fill in Excel. Alternatively, you can also click the Home tab, click on the Fill icon in the Editing group, and then click on the Flash Fill icon.

![click on the flash fill icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20295%20478'%3E%3C/svg%3E)

The above steps would instantly fill the entire column with the expected results (where the dashes have been removed).

![result after flash fill where dashes have been removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20437%20386'%3E%3C/svg%3E)

This is made possible as Flash Fill was able to identify the pattern when we entered the data in cell B2, and then replicate the same while giving us the result in all the cells in the column.

You can also use Flash Fill to remove some of the dashes. For example, if I only want to get rid of the first dash while keeping the second one, I can do that by entering 695-77990 in cell B2 and then using Flash Fill.

**Note**: While Flash Fill is quite good at identifying patterns, it may not always be correct. So make sure to check that you have got the right result. If it’s giving you the wrong result, try entering the expected result in the first two cells and then use Flash Fill.

Also read: [Remove Parentheses in Excel](https://trumpexcel.com/remove-parentheses-excel/)

Method 2 – Remove Dashes Using Find and Replace
-----------------------------------------------

Another fast way to quickly remove dashes from a cell is by using the [Find and Replace](https://trumpexcel.com/find-and-replace-in-excel/)
 technique (where we find the dash and replace it with a null string)

Let me show you how it works by using a simple example.

Below I have a data set where I have numbers in column A that have dashes in between, and I want to get rid of these dashes:

![data set to remove dashes using find and replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20237%20386'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select the cells that have the data from which you want to remove the dashes
2.  Click the Home tab

![click the home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20548%20223'%3E%3C/svg%3E)

3.  In the Editing group, click on the Find and Select option, and then click on Replace. This will open the Find and Replace dialog box.

![click on the replace option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20295%20504'%3E%3C/svg%3E)

**Tip**: You can also use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 Control + F to open the Find and Replace dialog box

4.  In the Find what field, enter a dash character (this is what we want to find and then remove from the cells)

![enter dash in find what field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20312'%3E%3C/svg%3E)

5.  Leave the ‘Replace with’ field empty.

![leave replaced with field blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20312'%3E%3C/svg%3E)

6.  Click on Replace All button.

![click on the replace all button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20667%20312'%3E%3C/svg%3E)

7.  It will show a message box mentioning how many dashes have been removed. Click OK.

![click OK in the message box that shows how many dahses have been removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20301%20145'%3E%3C/svg%3E)

The above steps would remove all the dashes from all the selected cells, and you would be left with the numbers only.

![data set up to the dashes have been removed](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20393%20418'%3E%3C/svg%3E)

**Note**: One limitation of this method is that you cannot use it to remove the dashes selectively. For example, you cannot choose to remove only the first or the last dash. When Find and Replace is used, it will remove all the dashes in the selected range.

Also read: [Remove Asterisk (\*) in Excel](https://trumpexcel.com/remove-asterisk-excel/)

Method 3 – Remove Dashes Using Formula
--------------------------------------

Another useful method to remove dashes/hyphens in Excel is by using the [SUBSTITUTE function](https://trumpexcel.com/excel-substitute-function/)
.

You should consider using it when you want more control over the result.

Let me show you how it works.

Below I have a data set where I have numbers with dashes in column A, and I want to use a formula to remove the dashes and get the result in column B.

![Dataset to remove dashes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20435%20386'%3E%3C/svg%3E)

Here is the formula that would remove the dashes from the cell:

\=SUBSTITUTE(A2,"-","")

Enter this formula in cell B2, and copy it for all the other cells in the column.

![substitute function to remove dashes in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20518%20430'%3E%3C/svg%3E)

In the above SUBSTITUTE formula:

*   The first argument is the cell reference with the text from which I want to remove the dash.
*   In the second argument, I have specified dash as the text string that I want to substitute (in double quotes)
*   In the third argument, I have specified the text with which I want to replace the dash. Since all I want to do is remove the dashes, this would be a null string in double quotes.
*   There is also a fourth optional argument (which I have not used here). In this argument, you can specify what instance of the dash you want to remove. So if you want to remove only the first dash, you can enter 1 as the fourth argument, and if you only want to remove the second one, you can use 2. When you don’t specify this argument, it will remove all the instances of the dash symbol.

Method 4 – Remove Dashes Using Power Query
------------------------------------------

Another method you can use to remove dashes and hyphens from your data set is by using Power Query.

This is not the most straightforward method and would only be useful if you’re already using Power Query as part of your work.

For example, if you’re already using Power Query to get the data from a database or from an Excel table and transform it, then you can use the steps I cover here to learn how to remove the dashes from that data as well.

Another scenario where this Power Query method could be useful is when you have to do this quite often. So you can create a flow using Power Query, and then whenever you get new data, you can change the source data and refresh the query.

Let me show you how to use Power Query to remove dashes in Excel.

Below I have a dataset where I have dashes in column A that I want to remove.

![data set to remove dashes using find and replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20237%20386'%3E%3C/svg%3E)

Here are the steps to do this using Power Query:

1.  First, we will need to convert this into an Excel table (so that we can use this in Power Query). To do this, select the entire dataset.
2.  Click the Insert tab in the ribbon
3.  Click on the Table option

![click on the table icon in the insert group](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20223'%3E%3C/svg%3E)

4.  In the Create Table dialog box that opens, make sure that the range is correct, and then click OK.

![check the range in the create table dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20266%20161'%3E%3C/svg%3E)

5.  Click the Data tab
6.  Click on the From Table/Range option. This will open the Power Query editor.

![click the data tab and then click on from table range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20583%20223'%3E%3C/svg%3E)

7.  Right-click on the column header
8.  Click on Replace Values option.

![right click on the column header and then click on replace values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20643%20492'%3E%3C/svg%3E)

9.  Enter a dash character in the ‘Value to Find’ field

![enter dash in value to find field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20296'%3E%3C/svg%3E)

10.  Leave the Replace with field empty

![leave the replace with field blank](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20296'%3E%3C/svg%3E)

11.  Click OK. You will notice that all the dashes have been removed from the data.

![dashes have been removed in the data in power query](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20527%20332'%3E%3C/svg%3E)

12.  Click on the Close and Load option in the ribbon.

![click on close and load](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20557%20140'%3E%3C/svg%3E)

The above steps will insert a new worksheet in the workbook and give us the resulting table in this new worksheet.

![power query result inserted in a new sheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20892'%3E%3C/svg%3E)

While this method does have a lot of steps, it is useful in case you keep getting new datasets from which you want to remove dashes.

With Power Query, you can create this process once, and then whenever you get a new dataset, or there are changes in the original data set, you do not have to repeat the entire process.

Just go to the new table that has been inserted in the new sheet, right-click, and then click on refresh. It will repeat all the processes in the back end, go to the original data, remove the dashes and give you the new result.

In this tutorial, I showed you four different ways to quickly remove dashes from a data set in Excel.

If you do this once in a while and want to get this done quickly, you can use the Flash Fill (Method #1) or the Find & Replace (Method #2).

If you want a little more control over the result, you can consider using the SUBSTITUTE formula (Method #3). And if this is something you need to do quite often on a regular basis, you can also automate the process by using Power Query (Method #4).

**Other Excel articles you may also like:**

*   [How to Remove Comma in Excel (from Text and Numbers)](https://trumpexcel.com/remove-comma-excel/)
    
*   [How to Remove Line Breaks in Excel](https://trumpexcel.com/remove-line-break-excel/)
    
*   [How To Remove Text Before Or After a Specific Character In Excel](https://trumpexcel.com/remove-text-before-after-character-excel/)
    
*   [How to Remove the First Character from a String in Excel](https://trumpexcel.com/remove-first-character-from-string/)
    
*   [Separate First and Last Name in Excel (Split Names Using Formulas)](https://trumpexcel.com/separate-first-and-last-name-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-dashes-excel/#respond)

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