# NAME Error in Excel (#NAME?)- What Causes it and How to Fix it!

**Source:** https://trumpexcel.com/name-error-excel

---

[Skip to content](https://trumpexcel.com/name-error-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/name-error-excel/#below-title)

If you have worked with Excel formulas for a while, I am sure you must have encountered the **#NAME error**.

Just like any other error in Excel, the #NAME error also occurs in specific situations (which I will cover in this tutorial), and there are some simple ways to find and fix the #NAME error.

Let’s get to it right away!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/name-error-excel/#)

What causes the #NAME Error?
----------------------------

When you use a formula and it gives you a NAME error, it means that the formula can not recognize something in it.

Let’s have a look at some of the most common issues that can cause a name error to raise its ugly head in your spreadsheet.

### Misspelled Formula Name

One of the most common reasons people see the name error is when they have used the wrong formula name.

For example, if you’re using the [VLOOKUP formula](https://trumpexcel.com/excel-vlookup-function/)
 and you type VLOKUP instead, Excel wouldn’t know what you mean, and it will show its disapproval by giving you the name error.

Below is an example where I have used the wrong formula name and have been slapped with the name error.

![Wrong formula name giving NAME Error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20450'%3E%3C/svg%3E)

**How to correct this** – Just check the names of all the functions you have used. A quick way is to simply place the cursor somewhere in the function name and Excel will show you a tool-tip. If it doesn’t, there is a possibility that you have misspelled the function name.

_Note: You can also get the name error in case you created a [User Defined formula (UDF) using VBA](https://trumpexcel.com/user-defined-function-vba/)
 and then misspelled the name. In this case, you should check the formula name in the VB Editor and make sure it’s correct_.

### Misspelled Named Range

If you work with [named ranges](https://trumpexcel.com/named-ranges-in-excel/)
, there is a possibility that you have misspelled them. And since Excel has no idea what range to refer to in this case, it shows the name error.

Below I have an example where I have used the named range name ‘Scores’ for data in column A and B.

![Named Range for a selected range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20478'%3E%3C/svg%3E)

And when I used the wrong name in the formula (where ‘s’ is missing in ‘Score’), Excel shows me the name error.

![Misspelled named range in the formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20441'%3E%3C/svg%3E)

**How to correct this** – Check the named ranges you have used and correct any misspelled names. When you use a named range in the formula, you will notice that its color changes. So in this case, you can spot any named range where the color is black, you may have found the culprit

As a best practice, I always let Excel show me the Named Range names while I am typing.

For example, if I have a named range ‘Scores’, and I type ‘Sco’, Excel will go out of the way to be helpful and show me all the names that match the text I entered (i.e., all the names starting with ‘Sco’).

![Excel formula showing named ranges matching the entered text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20433%20149'%3E%3C/svg%3E)

It’s best to choose from the list Excel shows as there would be no chance of misspelled named ranges in that case.

### Incorrect Range

In case you’re manually entering the range, there is a possibility that you may make a mistake and end up with a name error.

These mistakes could include:

*   Missing a colon in the range reference (A1A10 instead of A1:A10)

![Incorrect range with a missing colon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20663%20424'%3E%3C/svg%3E)

*   Using a reference that isn’t valid. In Excel, the range varies from A1: XFD1048576. If you use anything outside of this range, it will show you a name error. For example, enter =XFD1048577 in a cell and you will see the error.

### Opening New Version Formulas in Older Versions

Excel has been working on adding a lot of new formulas in the new versions.

For example, a lot of new functions such as [XLOOKUP](https://trumpexcel.com/xlookup-function/)
, [FILTER](https://trumpexcel.com/filter-function/)
, SORTBY, etc. were added in Excel 2019 and Microsoft Excel 365.

There are also many functions that were added in excel 2013 or 2016 which may not work with Excel 2010 and prior versions (such as IFNA).

So if you open an Excel workbook in an older version that uses these new formulas, you likely see the name error.

The logic is the same – since these formulas do not exist in that version of Excel, it considers these as misspelled names.

Unfortunately, there is no fix to this problem.

If you are sending a file to a person who’s using an older version of Excel, you need to make sure that you don’t use any newer formulas (or insist them on upgrading to a newer version of Excel)

### Missing Quotation Around Text in the Formula

In formulas that expect the text values to be in double quotes, a missing double quote will show you the name error.

When you keep a text within double quotes, Excel treats it as a text string, but when it’s not within double quotes, Excel thinks it’s a named range or formula name.

For example, if I use the formula =LEN(“Excel”), it works. But if I use =LEN(Excel) or LEN(“Excel), it would show the name error.

![Missing quotation in the formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%20145'%3E%3C/svg%3E)

In some cases, Excel can recognize that there is a missing quotation mark and show you the prompt with a suggestion. If you click on Yes, then in some cases it sorts the issue.

![Excel prompt with a suggestion](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20427%20192'%3E%3C/svg%3E)

How to Fix the #NAME erorrs in Excel
------------------------------------

Now that I have covered most of the reasons that can cause a name error in your worksheet, let’s have a look at some simple tips that will help you avoid this error to crop up in your work.

### Use the Formula Assistance

When you enter an equal-to sign and start typing the name of a formula, you will see that Excel shows you all the matching names of the formulas.

![Formula assist that shows a list of formulas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20394'%3E%3C/svg%3E)

I am not sure what this feature is called, but I call this formula assistance.

Instead of manually typing the formula in full, it would help if you choose the from the list. This makes sure that the name of the formula is not misspelled.

In case you have named ranges or tables, you will also see those show up in the list, making it easy for you to avoid any misspelled words.

### Use the Formula Wizard

In case you’re not sure about the arguments that the function takes (any error in which can result in the name error), you can use the formula wizard.

To open it, click on the fx icon just next to the formula bar.

![Click on the FX icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20473%20212'%3E%3C/svg%3E)

In the Insert Function dialog box that shows up, enter the formula name (you can also enter a partial name and then search) and double-click on it.

This opens the Function Arguments dialog box which shows a lot of help on each argument.

![Function argument dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20346'%3E%3C/svg%3E)

If you’re new to Excel formulas, I recommend you use the Formula Wizard till you are confident enough to use formulas directly in the worksheet.

### Use Name Manager

If you create a lot of [Excel tables](https://trumpexcel.com/excel-table/)
 and named ranges when working with complex data and calculations, there is a good chance you will forget the name you used and may end up misspelling it.

Instead of relying on your wonderful memory power, give Name Manager a chance.

It’s a place that will show you all the named ranges and table names, and you can choose and use the one you want right from the name manager.

Below are the steps to open the Name Manager:

1.  Click the Formulas tab
2.  In the Defined Names group, click on the ‘Name Manager’ icon.

![Click on the Name Manager](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20684%20165'%3E%3C/svg%3E)

This opens the name manager with all the names. You can also create new names or delete/edit the existing ones here.

![Name Manager dialog box with all the names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20499%20390'%3E%3C/svg%3E)

If you’re a keyboard person like I am, use the below keyboard shortcut to open the name manager:

Control + F3 (for Windows)

Command + F3 (for Mac)

Here is another useful tip when working with a lot of named ranges.

Pro Tip: If you’re writing formulas and need to use a named range, you can go to the Formula tab and then click on the ‘Use in Formula’ option in the Defined Names group. This will show you all the named ranges you have and you can get the name in the formula with a click of a button.

How to Find all #NAME Errors in Excel?
--------------------------------------

So far, I have covered what can cause a name error and some tips to make sure it doesn’t appear in your work.

But sometimes, it’s possible that you get a file from someone else and you need to find and correct any name errors (or any error) in the file.

In this section, I will show you a couple of methods that you can use to quickly identify cells that have the name error and correct it (or get rid of it).

### Using Go To Special Technique

Using go to special, you can quickly select all the cells that have an error.

This is not ‘Name error’ specific, which means that any cells that have any kind of error would be selected.

Below are the steps to do this:

1.  Select the data in which you want to select the cells with error
2.  Click the Home tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20498%20232'%3E%3C/svg%3E)

3.  In the Editing group, click on the Find and Select icon
4.  Click on Go To Special. This will open the Go To Special dialog box

![Click on Go To Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20438%20610'%3E%3C/svg%3E)

5.  In the Go To Special dialog box, select the Formulas option
6.  Deselect all the other options under Formulas, and only select the Errors option

![Select errors in formulas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20430'%3E%3C/svg%3E)

7.  Click OK

The above steps would select all the cells that have any kind of error in them.

Once you have these cells selected, you can treat them any way you want.

For example, you can highlight these cells by giving them a background color, delete these, or you can manually go through them one by one and find out the cause for these errors.

### Using Find and Replace

If you only want to find out the name errors, you can use the [Find and Replace](https://trumpexcel.com/find-and-replace-in-excel/)
 functionality within Excel to do this.

Below are the steps to find out all the name errors in a selected data set (or worksheet).

1.  Select the data set in which you want to find the name error. In case you want to so to the entire worksheet, select all the cells in the worksheet
2.  Use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     Control + F to open the Find & Replace dialog box (use Command + F if using a Mac)
3.  In the Find and Replace dialog box, enter #NAME? in the ‘Find what’ field.

![Enter NAME in find what field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20225'%3E%3C/svg%3E)

4.  Click on the Option button.

![Click on the Options button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20225'%3E%3C/svg%3E)

5.  In the additional options that show up, select ‘Values’ in the ‘Look in’ drop-down

![Select Values in Look In](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20281'%3E%3C/svg%3E)

6.  Click on Find All

![Click on Find all](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20601%20281'%3E%3C/svg%3E)

If your selected range has a name error, you’ll see that an additional box opens below the Find and Replace dialog box that lists all the cells that have the name error.

![All found cells with name error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20393'%3E%3C/svg%3E)

Here, you can select each cell one by one and treat these cells, or select all of these at once and perform operations such as highlight these cells or delete these cells.

Just the way I have used this technique to find out all the name errors in the worksheet, you can use it to find out any other kind of error as well.

So this is all about the name error in excel.

In this tutorial, I covered the possible reasons that are causing the name error in your data, some of the techniques you can use to make sure that it doesn’t appear, and two methods that you can use to find the name errors in your worksheet or workbook.

I hope you found this tutorial useful.

**Other excel tutorials you may also like:**

*   [#REF! Error in Excel – How to Fix the Reference Error!](https://trumpexcel.com/ref-error-in-excel/)
    
*   [Excel Formulas Not Working: Possible Reasons and How to FIX IT!](https://trumpexcel.com/excel-formulas-not-working/)
    
*   [Microsoft Excel Won’t Open – How to Fix it! (6 Possible Solutions)](https://trumpexcel.com/microsoft-excel-wont-open/)
    
*   [Identify Errors Using Excel Formula Debugging (2 Methods)](https://trumpexcel.com/excel-formula-debugging/)
    
*   [Use IFERROR with VLOOKUP to Get Rid of #N/A Errors](https://trumpexcel.com/iferror-vlookup/)
    
*   [How to Get Rid of #DIV/0! Error in Excel?](https://trumpexcel.com/div-error-in-excel/)
    
*   [How to Fix #VALUE Error in Excel?](https://trumpexcel.com/fix-value-error-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/name-error-excel/#respond)

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