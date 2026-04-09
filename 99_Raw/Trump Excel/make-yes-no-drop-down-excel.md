# How to Make a Yes/No Drop-Down in Excel? (Easy Ways)

**Source:** https://trumpexcel.com/make-yes-no-drop-down-excel

---

[Skip to content](https://trumpexcel.com/make-yes-no-drop-down-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/make-yes-no-drop-down-excel/#below-title)

The [drop-down feature in Excel](https://trumpexcel.com/excel-drop-down-list/)
 it’s quite useful when doing data entry.

Using it, you can create a drop-down in a cell that will show you all the pre-populated options that you can choose from.

It saves time as you can simply choose from the list instead of entering it manually, and it also helps you avoid errors such as [misspelled words](https://trumpexcel.com/using-spell-check-in-excel/)
.

One common drop-down list that is often needed is a Yes and No drop-down list. Once you create this Yes/No drop-down list, you can quickly choose to fill the value yes or no in a cell by simply selecting it from the drop-down.

In this tutorial, I will show you two simple ways to quickly create a Yes / No drop-down list in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/make-yes-no-drop-down-excel/#)

Create a Yes/No Drop Down List by Manually Entering the Values
--------------------------------------------------------------

The easiest way to create a Yes No drop-down list is to manually specify the values that you want will be shown in the dropdown in the [data validation](https://trumpexcel.com/learn-all-about-data-validation-in-excel/)
 option.

Below I have a data set of names and column A and I want to create a Yes-No drop-down list in column B so that I can select whether the person has completed the training or not from the drop-down.

![Data for yes no column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20526%20386'%3E%3C/svg%3E)

Below are the steps to do this:

1.  Select the cell or range of cells where you want to get this drop-down
2.  Click the ‘Data’ tab

![Click the data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20680%20223'%3E%3C/svg%3E)

3.  In the ‘Data Tools’ group, click on the ‘Data Validation’ icon

![Click on the data validation icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20590%20223'%3E%3C/svg%3E)

4.  In the Data Validation dialog box that opens up, within the ‘Settings’ tab, click on the ‘Allow’ drop-down menu
5.  Select the ‘List’ option

![Click on Allow drop down list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

6.  In the ‘Source:’ field, enter the following:

Yes,No

![Enter Yes No in the data validation field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

7.  Click OK

The above steps would create a Yes-No dropdown list in the selected cells (you should see a small drop-down icon when the cell is selected).

![Yes No drop down list added](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20555%20396'%3E%3C/svg%3E)

Now to show these options in the cell and select Yes or No, click on the drop-down icon and then select the option you want.

You can also use the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
 ALT + Down Arrow Key to show the drop-down in the selected cells (you need to hold the alt key and then press the down arrow key).

Once you have created the drop-down list in a cell, you won’t be able to enter anything other than Yes or No. If you try doing that, you would see an error box as shown below:

![Error when value doesn't match the Yes No value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20531%20145'%3E%3C/svg%3E)

In this method, we have hard-coded the drop-down values, and in case you want to change the options that show up in the drop-down, you will have to go back to the Ddata Validation dialog box and make the changes there.

**Pro Tip**: You can use the following keyboard shortcut to open the data validation dialog box (use this after selecting the cells where you want the drop-down) – **ALt + A + V + V** (press these keys one after the other

Create a Yes/No Drop Down List by Using a Cell Range
----------------------------------------------------

In the above method, we hard-coded the Yes/No values in the data validation dialog box.

Another way of doing this is to enter the values that you wanted in the drop-down in a cell, and then create the drop-down by using these cells as the source for the drop-down values.

The benefit of doing this is that it makes your drop-down list dynamic, i.e., if you change the values in the cells that I used to create the drop-down, the values in the drop-down would also automatically change.

Below I have the same data set where I want to create the yes no dropdown list in column B, and I also have Yes and No entered in two cells as shown below (in D2 and D3):

![Data with Yes No options in cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20568%20311'%3E%3C/svg%3E)

Here are the steps to create a drop-down list using the values from cells:

1.  Select the cell or range of cells where you want to get this drop-down
2.  Click the Data tab
3.  Click on the ‘Data Validation’ icon (it’s in the ‘Data Tools’ group)
4.  In the Data Validation dialog box that opens up, within the ‘Settings’ tab, click on the Allows drop-down menu
5.  Select the List option

![Click on Allow drop down list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

6.  In the Source field, click on the range selection icon

![Click on the range selection icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

7.  Select the cells that have the Yes/No values. The [reference to these cells](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
     would automatically be added to the ‘Source’ field

![Source cell reference is entered as the source](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20412'%3E%3C/svg%3E)

8.  Click Ok

The above steps would create the drop-down list in the selected cells using the values that we selected as the source.

![Drop down shows up in the selected cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20573%20312'%3E%3C/svg%3E)

While this gives us the same result as the previous method, the benefit of this method is that if you change the values in the source cells, drop-down values would automatically update.

Also read: [Create Data Validation List from Excel Table as Source](https://trumpexcel.com/data-validation-list-from-excel-table/)

Copy and Paste the Yes/No Drop-down Lists
-----------------------------------------

Dropdown lists can be copied just like [cell color](https://trumpexcel.com/count-colored-cells-in-excel/)
 or cell formatting.

So, if you already have a yes-no dropdown list in a cell and you want to create the same one in another cell or another range of cells, instead of doing it by following the steps I’ve shown in the previous methods, you can simply copy the cell that already has the drop-down list and paste it over the cells where you want it.

Editing the Yes/No Drop-Down Lists
----------------------------------

In case you want to change the values in the drop-down or edit the existing values, you need to open the data validation dialog box, and make the changes there.

For example, if you have made a spelling error or you want to change the source of the cells from where the dropdown values are picked up, you will have to go back to the data validation dialog box to make these changes.

In this short tutorial, I showed you how to create a simple Yes/No drop-down list in Excel.

I hope you found this tutorial useful.

**Other Excel tutorials you may also like:**

*   [Drop Down Lists To Show Numbers Between Two Specified Numbers](https://trumpexcel.com/drop-down-numbers/)
    
*   [Show Symbols in Drop Down Lists in Excel](https://trumpexcel.com/symbols-in-drop-down-lists-excel/)
    
*   [Creating Multiple Drop-down Lists in Excel without Repetition](https://trumpexcel.com/multiple-drop-down-lists-in-excel/)
    
*   [Display Main and Subcategory in Drop Down List in Excel](https://trumpexcel.com/subcategory-in-drop-down-list-excel/)
    
*   [How to Make Multiple Selections in a Drop-Down List in Excel](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/)
    
*   [Creating a Searchable Drop-Down list in Excel – Step by Step Guide](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/)
    
*   [How to Create a Dependent Drop-Down List in Excel](https://trumpexcel.com/dependent-drop-down-list-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

3 thoughts on “How to Make a Yes/No Drop-Down in Excel? (Easy Ways)”
--------------------------------------------------------------------

1.  Found out that this difference is related to regional settings. Semicolon in Sweden, comma in USA.
    
    [Reply](https://trumpexcel.com/make-yes-no-drop-down-excel/#comment-38061)
    
2.  Turns out the current version of Excel uses a semicolon as a separator, rather than the comma you state here.
    
    [Reply](https://trumpexcel.com/make-yes-no-drop-down-excel/#comment-38059)
    
3.  Strange. When I follow the exact steps you outline under “Create a Yes/No Drop Down List by Manually Entering the Values”, it creates a drop-down with only one choice, “Yes,No”
    
    [Reply](https://trumpexcel.com/make-yes-no-drop-down-excel/#comment-38058)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/make-yes-no-drop-down-excel/#respond)

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