# How to Remove Drop-Down List in Excel? Easy Steps!

**Source:** https://trumpexcel.com/remove-drop-down-list-excel

---

[Skip to content](https://trumpexcel.com/remove-drop-down-list-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/remove-drop-down-list-excel/#below-title)

I’ve been a big fan of [Excel drop-down lists](https://trumpexcel.com/excel-drop-down-list/)
 since I learned about them. It makes [data entry fast](https://trumpexcel.com/excel-data-entry-tips/)
 It also allows me to [create dashboards and reports](https://trumpexcel.com/creating-excel-dashboard/)
 that are interactive (where a user can choose an option from the drop-down in the entire dashboard updates).

It’s also a useful tool when I’m sharing my files with other people, as I can restrict data entry in some cells and only allow the selection to be made from the drop-down.

However, in some cases, you may have a need to remove the drop-down from your Excel file.

This could be because you no longer need the drop-down, or you want to enter something else other than the options in the drop-down.

In this tutorial, I’m going to show you how to quickly remove a drop-down in Excel. I will also cover how you can remove all the drop-downs in your excel file in one go.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/remove-drop-down-list-excel/#)

Why Remove Drop-down Lists in Excel?
------------------------------------

The biggest reason people want to remove a drop-down list in Excel is that they want to enter some other text apart from the one specified in the drop-down.

If you have a drop-down list in a cell, and you try and enter something else, you will see an error message (as shown below).

![Drop down list error message](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20531%20145'%3E%3C/svg%3E)

Another common reason could be when you want to redo the drop-down list, but first, get rid of all the existing ones in the worksheet

Remove Specific Drop-down Lists in Excel
----------------------------------------

Let me first show you how to remove a specific drop-down list in the worksheet.

For this method to work, you will need to select the drop-downs (all the cells that contain multiple drop-downs) that you want to delete.

_I will also show you how to remove all the drop-downs in the worksheet in the next section_

### Using the Data Validation Dialog Box

Below I have the Employee name data set in column A, and I have created drop-down lists in the adjacent cell (column B) that would show the department names.

![Column B has drop down list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20396'%3E%3C/svg%3E)

From this data, I want to delete all the drop-downs in column B.

Below are the steps to remove the drop-down from column B using the [data validation](https://trumpexcel.com/learn-all-about-data-validation-in-excel/)
 dialog box.

1.  Select the cells that have the drop-down that you want to delete
2.  Click the ‘Data’ tab

![Click the data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20648%20223'%3E%3C/svg%3E)

3.  In the ‘Data Tools’ group, click on the ‘Data Validation’ icon. This will open the Data Validation dialog box

![Click the data validation icon in the data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20223'%3E%3C/svg%3E)

4.  Make sure the ‘Settings’ tab is selected in the Data Validation dialog box
5.  Click on the ‘Clear All’ button

![Click on the clear all option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

6.  Click OK

The above steps would clear all the data validation rules from the selected cells, and since a drop-down list is also a type of data validation rule, these would be cleared as well.

Note that in case you had made selections earlier using the drop-down lists, that value would still remain in the cell. Only the drop-down list would be removed

**Pro Tip**: You can use the following keyboard shortcut to open the data validation dialog box – **ALT + A + V + V** (press these keys one after the other)

### Using the Clear All Button

In the above method, we only remove the drop-down list from the cells. The values in the cell (if there were) and the formatting remained as is.

In case you want to remove everything from the selected cells (including the drop-down lists as well as the values and formatting), you don’t need to go through the data validation route.

Instead, you can use the ‘Clear All’ option available in the ribbon.

Below I have a data set where I have the employee names in column A and the drop-down list in column B (where the drop-down list shows the department names for the employees).

![Column B has drop down list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20396'%3E%3C/svg%3E)

Below are the steps to remove the drop downs in the cells using the ‘Clear All’ method:

1.  Select the cells that have the drop-down that you want to remove
2.  Click the ‘Home’ tab
3.  In the Editing group, click on the ‘Clear’ option

![Click the clear option in the home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20570%20223'%3E%3C/svg%3E)

4.  In the options that show up, click on ‘Clear All’

![Click on the Clear All options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20329%20385'%3E%3C/svg%3E)

The above steps would remove everything from the cells (including the drop-down list, any values in the cells, as well as any formatting applied to the cells).

This method is more suited in situations where you want to start afresh and want to get rid of everything that is already there in the cells.

**Pro Tip**: You can also use the following shortcut to clear everything from the selected cells – **ALT + H +  E + A** (press these keys one after the other)

### Using Copy-Paste Method

Excel treats drop-down lists just like cell formatting. This allows you to copy and paste a drop-down list using a simple copy-paste operation.

And vice versa, if you copy a cell that does not have a drop-down list and paste it over a cell that has it, the drop-down list would be removed (as the formatting and the data validation rules of the copied cells are applied to the destination cell)

Below I have this data set where I have drop-down lists in column B, that I want to remove.

![Column B has drop down list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20396'%3E%3C/svg%3E)

Here are the steps to delete the drop-down list by using a simple copy-paste method:

1.  [Select a blank cell](https://trumpexcel.com/select-blank-cells-in-excel/)
     in the worksheet that does not have a drop-down in it
2.  Copy this cell (you can right-click on the cell and then click on copy or you can use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     Control + C in windows or Command + C in Mac)
3.  Select the cells that have the drop-down list that you want to remove
4.  Right-click on the selected cells and then click on Paste (or use the keyboard shortcut Control + V or Command + V)

![Paste over drop down lists](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20550%20368'%3E%3C/svg%3E)

The above steps would remove the drop-down list from the selected cells.

One drawback of this method is that it removes all the formatting in the cells and [copies the formatting](https://trumpexcel.com/excel-format-painter/)
 from the cell that we copied in step 2.

Remove All Drop-Down Lists in the Worksheet
-------------------------------------------

In the above section, I showed you three methods to remove the drop-down list from the selected cells.

For those methods to work, you have to know where these drop-down lists are, and then select those cells first before removing them.

In this section, I will show you how you can remove all the drop-down lists in the worksheet without manually selecting each cell that has it.

And there are two scenarios where you can use this method:

1.  When you want to remove all the drop-down lists in the worksheet that were created using the same source list, or
2.  When you want to remove all the drop-down lists irrespective of the source list.

### Based on the Same List

Below I have a data set where I have drop-down lists in two columns (columns B and E), which have been created using the same source list (so all the cells show the same data in the drop-down menu)

![Dataset with two drop down lists](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20248'%3E%3C/svg%3E)

And I want to remove both of these drop-down lists.

Here are the steps to remove all the drop-down lists in one go:

1.  Select any one cell that has the drop-down that you want to delete
2.  Press the F5 key on your keyboard, this will open the Go To dialog box (you can also go to the ‘Home’ tab, click on the ‘Find & Select’ option in the Editing group, and then click on the ‘Go To’ option)
3.  In the ‘Go To’ dialog box, click on the ‘Special’ button.

![Click the special button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20419%20347'%3E%3C/svg%3E)

4.  In the ‘Go To Special’ dialog box, select the ‘Data Validation’ option
5.  Select the ‘Same’ option within the Data Validation option

![Select same option under data validation option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20430'%3E%3C/svg%3E)

6.  Click OK

The above steps will select all the cells that have the drop-down list that uses the same source list of the cell that we selected in step 1.

Now that we have selected all the cells that have the drop-down list, here are the steps to remove that drop-down list.

7.  Click the ‘Data’ tab
8.  In the ‘Data Tools’ group, click on the ‘Data Validation’ icon.

![Click the data validation icon in the data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20223'%3E%3C/svg%3E)

9.  Make sure the Settings tab is selected in the Data Validation dialog box
10.  Click on the ‘Clear All’ button

![Click on the clear all option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

11.  Click OK

The above steps would remove all the drop-down menu that is based on the same list as the one in the cell that was selected in Step 1.

### Based on the Different Lists

In case you want to remove all the drop-down lists in the worksheet in one go (irrespective of the source list), you can use the steps in this section.

1.  Press the F5 key on your keyboard, this will open the Go To dialog box (you can also go to the ‘Home’ tab, click on the ‘Find & Select’ option in the Editing group, and then click on the ‘Go To’ option)
2.  Click on the ‘Special’ button. This will open the Go To Special dialog box
3.  Select the ‘Data Validation’ option
4.  Make sure the ‘All’ option is selected

![Select all option in data validation in Go to special dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20430'%3E%3C/svg%3E)

5.  Click OK. This will select all the cells that have data validation rules applied to it
6.  Click the Data tab
7.  In the ‘Data Tools’ group, click on the ‘Data Validation’ icon.
8.  Make sure the ‘Settings’ tab is selected in the Data Validation dialog box
9.  Click on the ‘Clear All’ button

![Clear all data validation rules](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

10.  Click OK

The above steps would remove all the drop-down lists in your worksheet.

The good thing about this method is that you do not need to know that all cells have drop-down menus in them. The ‘Go To Special’ option does that for you.

**Caution**: One important thing to remember is that the above steps would remove all types of data validation rules from the worksheet. While a drop-down list is the most used data validation option, a lot of people also use data validation rules that that does not involve creating a drop-down menu (such as [restricting data entry](https://trumpexcel.com/conditional-data-entry-in-excel/)
 between two numbers or two dates). The above steps would select any cell that has any data validation rule applied to it (not just the drop-down lists)

Keep the Drop Down List But Allows All Entries (No Error Message)
-----------------------------------------------------------------

In some cases, users are ok with keeping the drop-down lists as long as the cells allow entering the data manually as well.

For example, if I have a drop-down list that shows department names for employees, and for one employee I want to enter ‘NA’ or ‘Not Assigned’, I won’t be able to do it as it is not a part of the drop-down list.

But what if there was a way to allow you to enter values that are not part of the drop-down list, and keep the drop-down list at the same time?

Let me show you how to do this.

Below I have data set where I have drop-down lists in column B, and I want to keep the drop-down list as well as be able to enter data manually in these cells.

![Column B has drop down list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20556%20396'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select the cells that have the drop-down
2.  Click the Data tab
3.  In the ‘Data Tools’ group, click on the ‘Data Validation’ icon.

![Click the data validation icon in the data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20592%20223'%3E%3C/svg%3E)

4.  In the Data Validation dialog box, click on the ‘Error Alert’ tab
5.  Uncheck the option – “Show error alert after invalid data is entered”

![Uncheck Show error alert after invalid data is entered](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

6.  Click OK

After you’re done with the above steps, you will be able to enter any data in the cell without triggering the error message prompt.

And at the same time, you can also use the options in the drop-down list to do the data entry (so the best of both worlds).

In this tutorial, I showed you multiple ways to remove drop-down lists from cells in Excel. If you want to remove it from specific cells, you can use the inbuilt clear all option in the data validation dialog box, or you can use the ‘Clear All’ option that removes Everything including the drop-down lists.

I’ve also covered how you can remove all the drop-down lists from a worksheet (based on the same list or irrespective of the source lists)

I hope you found this Excel tutorial useful.

**Other Excel tutorials you may also like**:

*   [Drop Down Lists To Show Numbers Between Two Specified Numbers](https://trumpexcel.com/drop-down-numbers/)
    
*   [How to Make a Yes/No Drop-Down in Excel?](https://trumpexcel.com/make-yes-no-drop-down-excel/)
    
*   [Show Symbols in Drop Down Lists in Excel](https://trumpexcel.com/symbols-in-drop-down-lists-excel/)
    
*   [Creating Multiple Drop-down Lists in Excel without Repetition](https://trumpexcel.com/multiple-drop-down-lists-in-excel/)
    
*   [Display Main and Subcategory in Drop Down List in Excel](https://trumpexcel.com/subcategory-in-drop-down-list-excel/)
    
*   [How to Make Multiple Selections in a Drop Down List in Excel](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/)
    
*   [Creating a Searchable Drop Down list in Excel](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/)
    
*   [How to Remove Cell Formatting in Excel (from All, Blank, Specific Cells)](https://trumpexcel.com/remove-cell-formatting-in-excel/)
    
*   [How to Create a Dependent Drop Down List in Excel](https://trumpexcel.com/dependent-drop-down-list-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/remove-drop-down-list-excel/#respond)

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