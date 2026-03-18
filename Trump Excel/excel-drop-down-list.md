# How to Create a Drop Down List in Excel (the Only Guide You Need)

**Source:** https://trumpexcel.com/excel-drop-down-list

---

[Skip to content](https://trumpexcel.com/excel-drop-down-list/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-drop-down-list/#below-title)

A drop-down list is an excellent way to give the user an option to select from a pre-defined list.

It can be used while getting a user to fill a form, or while creating interactive [Excel dashboards](https://trumpexcel.com/creating-excel-dashboard/)
.

Drop-down lists are quite common on websites/apps and are very intuitive for the user.

**Watch Video – Creating a Drop Down List in Excel**

In this tutorial, you’ll learn how to create a drop down list in Excel (it takes only a few seconds to do this) along with all the awesome stuff you can do with it.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-drop-down-list/#)

How to Create a Drop Down List in Excel
---------------------------------------

In this section, you will learn the exacts steps to create an Excel drop-down list:

1.  Using Data from Cells.
2.  Entering Data Manually.
3.  Using the OFFSET formula.

### #1 Using Data from Cells

Let’s say you have a list of items as shown below:

![List of Items for which a drop down list needs to be created](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20127%20139'%3E%3C/svg%3E)

Here are the steps to create an Excel Drop Down List:

1.  Select a cell where you want to create the drop down list.
2.  Go to Data –> Data Tools –> Data Validation.![An image of Data Validation option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20527%20130'%3E%3C/svg%3E)
3.  In the Data Validation dialogue box, within the Settings tab, select List as the Validation criteria.
    *   As soon as you select List, the source field appears.![Data Validation settings for creating drop down list in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20404%20327'%3E%3C/svg%3E)
4.  In the source field, enter \=$A$2:$A$6, or simply click in the Source field and select the cells using the mouse and click OK. This will insert a drop down list in cell C2.
    *   Make sure that the In-cell dropdown option is checked (which is checked by default). If this option in unchecked, the cell does not show a drop down, however, you can manually enter the values in the list.![Selecting the range for which a drop down menu is to be created](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20540%20396'%3E%3C/svg%3E)

_**Note:** If you want to create drop down lists in multiple cells at one go, select all the cells where you want to create it and then follow the above steps. Make sure that the cell references are absolute (such as $A$2) and not relative (such as A2, or A$2, or $A2)._

### #2 By Entering Data Manually

In the above example, cell references are used in the Source field. You can also add items directly by entering it manually in the source field.

For example, let’s say you want to show two options, Yes and No, in the drop down in a cell. Here is how you can directly enter it in the data validation source field:

*   Select a cell where you want to create the drop down list (cell C2 in this example).
*   Go to Data –> Data Tools –> Data Validation.![Data Validation option in the Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20527%20130'%3E%3C/svg%3E)
*   In the Data Validation dialogue box, within the Settings tab, select List as the Validation criteria.
    *   As soon as you select List, the source field appears.![Excel Drop Down Menu - Settings in Data Validation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20404%20327'%3E%3C/svg%3E)
*   In the source field, enter Yes, No
    *   Make sure that the In-cell dropdown option is checked.
*   Click OK.

This will create a drop-down list in the selected cell. All the items listed in the source field, separated by a comma, are listed in different lines in the drop down menu.

All the items entered in the source field, separated by a comma, are displayed in different lines in the drop down list.

![Drop-Down Menu in Excel - Manual Entry demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20524%20352'%3E%3C/svg%3E)

_**Note:** If you want to create drop down lists in multiple cells at one go, select all the cells where you want to create it and then follow the above steps._

### #3 Using Excel Formulas

Apart from selecting from cells and entering data manually, you can also use a formula in the source field to create an Excel drop down list.

Any formula that returns a list of values can be used to create a drop-down list in Excel.

For example, suppose you have the data set as shown below:

![List of items for which a drop-down list needs to be created](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20127%20139'%3E%3C/svg%3E)

Here are the steps to create an Excel drop down list using the [OFFSET function](https://trumpexcel.com/excel-offset-function/)
:

*   Select a cell where you want to create the drop down list (cell C2 in this example).
*   Go to Data –> Data Tools –> Data Validation.![Data validation option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20527%20130'%3E%3C/svg%3E)
*   In the Data Validation dialogue box, within the Settings tab, select List as the Validation criteria.
    *   As soon as you select List, the source field appears.![Settings for creating the Excel drop down list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20404%20327'%3E%3C/svg%3E)
*   In the Source field, enter the following formula: \=OFFSET($A$2,0,0,5)
    *   Make sure that the In-cell dropdown option is checked.
*   Click OK.

This will create a drop-down list that lists all the fruit names (as shown below).

![Using OFFSET function to create the Excel drop down list](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20524%20400'%3E%3C/svg%3E)_**Note:** If you want to create a drop-down list in multiple cells at one go, select all the cells where you want to create it and then follow the above steps._ Make sure that the cell references are absolute (such as $A$2) and not relative (such as A2, or A$2, or $A2).

**How this formula Works??**

In the above case, we used an OFFSET function to create the drop down list. It returns a list of items from the ra

It returns a list of items from the range A2:A6.

Here is the syntax of the OFFSET function: \=OFFSET(reference, rows, cols, \[height\], \[width\])

It takes five arguments, where we specified the reference as A2 (the starting point of the list). Rows/Cols are specified as 0 as we don’t want to offset the reference cell. Height is specified as 5 as there are five elements in the list.

Now, when you use this formula, it returns an array that has the list of the five fruits in A2:A6. Note that if you enter the formula in a cell, select it and press F9, you would see that it returns an array of the fruit names.

![Offset function returns a set of items](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20528%20136'%3E%3C/svg%3E)

Creating a Dynamic Drop Down List in Excel (Using OFFSET)
---------------------------------------------------------

The above technique of using a formula to create a drop down list can be extended to create a dynamic drop down list as well. If you use the OFFSET function, as shown above, even if you add more items to the list, the drop down would not update automatically. You will have to manually update it each time you change the list.

Here is a way to make it dynamic (and it’s nothing but a minor tweak in the formula):

*   Select a cell where you want to create the drop down list (cell C2 in this example).
*   Go to Data –> Data Tools –> Data Validation.
*   In the Data Validation dialogue box, within the Settings tab, select List as the Validation criteria. As soon as you select List, the source field appears.
*   In the source field, enter the following formula: \=OFFSET($A$2,0,0,COUNTIF($A$2:$A$100,”<>”))
*   Make sure that the In-cell drop down option is checked.
*   Click OK.

In this formula, I have replaced the argument 5 with COUNTIF($A$2:$A$100,”<>”).

The COUNTIF function counts the non-blank cells in the range A2:A100. Hence, the OFFSET function adjusts itself to include all the non-blank cells.

![A demo of how dynamic drop-down lists work in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20528%20400'%3E%3C/svg%3E)

**_Note:_**

*   _For this to work, there must NOT be any blank cells in between the cells that are filled._
*   _If you want to create a drop-down list in multiple cells at one go, select all the cells where you want to create it and then follow the above steps. Make sure that the cell references are absolute (such as $A$2) and not relative (such as A2, or A$2, or $A2)._

Copy Pasting Drop-Down Lists in Excel
-------------------------------------

You can copy paste the cells with data validation to other cells, and it will copy the data validation as well.

For example, if you have a drop-down list in cell C2, and you want to apply it to C3:C6 as well, simply copy the cell C2 and paste it in C3:C6. This will copy the drop-down list and make it available in C3:C6 (along with the drop down, it will also copy the formatting).

If you only want to copy the drop down and not the formatting, here are the steps:

*   Copy the cell that has the drop down.
*   Select the cells where you want to copy the drop down.
*   Go to Home –> Paste –> Paste Special.![Paste Special options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20156%20339'%3E%3C/svg%3E)
*   In the Paste Special dialogue box, select Validation in Paste options.![Selecting Validation Option in Paste Special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20336'%3E%3C/svg%3E)
*   Click OK.

This will only copy the drop down and not the formatting of the copied cell.

Caution while Working with Excel Drop Down List
-----------------------------------------------

You need to to be careful when you are working with drop down lists in Excel.

When you copy a cell (that does not contain a drop down list) over a cell that contains a drop down list, the drop down list is lost.

The worst part of this is that Excel will not show any alert or prompt to let the user know that a drop down will be overwritten.

How to Select All Cells that have a Drop Down List in it
--------------------------------------------------------

Sometimes, it ‘s hard to know which cells contain the drop down list.

Hence, it makes sense to mark these cells by either giving it a distinct border or a background color.

Instead of manually checking all the cells, there is a quick way to select all the cells that have drop-down lists (or any data validation rule) in it.

*   Go to Home –> Find & Select –> Go To Special.![Go to special to select all cells with drop down lists in it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20217%20347'%3E%3C/svg%3E)
*   In the Go To Special dialogue box, select Data Validation
    *   Data validation has two options: All and Same. All would select all the cells that have a data validation rule applied on it. Same would select only those cells that have the same data validation rule as that of the active cell.![How to Create a Drop Down List in Excel - Goto DataVal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20323%20334'%3E%3C/svg%3E)
*   Click OK.

This would instantly select all the cells that have a data validation rule applied to it (this includes drop down lists as well).

Now you can simply format the cells (give a border or a background color) so that visually visible and you don’t accidentally copy another cell on it.

Here is [another technique](https://www.excelcampus.com/tips/drop-list-arrow-always-visible/)
 by Jon Acampora you can use to always keep the drop down arrow icon visible. You can also see some ways to do this in this [video by Mr. Excel](https://www.youtube.com/watch?v=gKxbDqoBWsw)
.

Creating a Dependent / Conditional Excel Drop Down List
-------------------------------------------------------

Here is a video on how to create a dependent drop-down list in Excel.

If you prefer reading over watching a video, keep reading.

Sometimes, you may have more than one drop-down list and you want the items displayed in the second drop down to be dependent on what the user selected in the first drop-down.

These are called dependent or conditional drop down lists.

Below is an example of a conditional/dependent drop down list:

![A demo of dependent drop down list in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20616%20212'%3E%3C/svg%3E)

In the above example, when the items listed in ‘Drop Down 2’ are dependent on the selection made in ‘Drop Down 1’.

Now let’s see how to create this.

Here are the steps to create a dependent / conditional drop down list in Excel:

*   Select the cell where you want the first (main) drop down list.
*   Go to Data –> Data Validation. This will open the data validation dialog box.![Data validation option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20120'%3E%3C/svg%3E)
*   In the data validation dialog box, within the settings tab, select List.![Data validation settings to create a dependent drop down list in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20314'%3E%3C/svg%3E)
*   In Source field, specify the range that contains the items that are to be shown in the first drop down list.![Using Headers to create the first drop down list ](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20686%20352'%3E%3C/svg%3E)
*   Click OK. This will create the Drop Down 1.![Excel Drop Down List - Conditional - DD1 Demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20597%20185'%3E%3C/svg%3E)
*   Select the entire data set (A1:B6 in this example).![Excel Drop Down List - Conditional - Select Entire Range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20259%20186'%3E%3C/svg%3E)
*   Go to Formulas –> Defined Names –> Create from Selection (or you can use the keyboard shortcut Control + Shift + F3).![Creating named ranges from selections](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20443%20123'%3E%3C/svg%3E)
*   In the ‘Create Named from Selection’ dialog box, check the Top row option and uncheck all the others. Doing this creates 2 names ranges (‘Fruits’ and ‘Vegetables’). Fruits named range refers to all the fruits in the list and Vegetables named range refers to all the vegetables in the list.![Creating named ranges from the top row of the selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20260%20173'%3E%3C/svg%3E)
*   Click OK.
*   Select the cell where you want the Dependent/Conditional Drop Down list (E3 in this example).
*   Go to Data –> Data Validation.![Data validation option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20120'%3E%3C/svg%3E)
*   In the Data Validation dialog box, within the setting tab, make sure List in selected.![Settings List in Data Validation dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20314'%3E%3C/svg%3E)
*   In the Source field, enter the formula =INDIRECT(D3). Here, D3 is the cell that contains the main drop down.![Using Indirect Function to create conditional drop down list in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20314'%3E%3C/svg%3E)
*   Click OK.

Now, when you make the selection in Drop Down 1, the options listed in Drop Down List 2 would automatically update.

**Download the Example File**  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2015/11/Dependent-Drop-Down-List-Excel.xlsx)

**How does this work?** – The conditional drop down list (in cell E3) refers to =INDIRECT(D3). This means that when you select ‘Fruits’ in cell D3, the drop down list in E3 refers to the [named range](https://trumpexcel.com/named-ranges-in-excel/)
 ‘Fruits’ (through the [INDIRECT function](https://trumpexcel.com/excel-indirect-function/)
) and hence lists all the items in that category.

**_Important Note While Working with Conditional Drop Down Lists in Excel:_**

*   _When you have made the selection, and then you change the parent drop down, the dependent drop down would not change and would, therefore, be a wrong entry. For example, if you select the US as the country and then select Florida as the state, and then go back and change the country to India, the state would remain as Florida. Here is a [great tutorial by Debra](http://blog.contextures.com/archives/2014/09/11/clear-dependent-drop-down-cells/)
     on clearing dependent (conditional) drop down lists in Excel when the selection is changed._
*   _If the main category is more than one word (for example, ‘Seasonal Fruits’ instead of ‘Fruits’), then you need to use the formula =INDIRECT(SUBSTITUTE(D3,” “,”\_”)), instead of the simple INDIRECT function shown above. The reason for this is that Excel does not allow spaces in named ranges. So when you create a named range using more than one word, Excel automatically inserts an underscore in between words. So ‘Seasonal Fruits’ named range would be ‘Seasonal\_Fruits’. Using the [SUBSTITUTE function](https://trumpexcel.com/excel-substitute-function/)
     within the INDIRECT function makes sure that spaces_ are _converted into underscores._ 

**You May Also Like the Following Excel Tutorials:**

*   [Extract Data from Drop Down List Selection in Excel](https://trumpexcel.com/extract-data-from-drop-down-list/)
    .
*   [Select Multiple Items from a Drop Down List in Excel](https://trumpexcel.com/select-multiple-items-drop-down-list-excel/)
    .
*   [Creating a Dynamic Excel Filter Search Box](https://trumpexcel.com/dynamic-excel-filter/)
    .
*   [Display Main and Subcategory in Drop Down List in Excel](https://trumpexcel.com/subcategory-in-drop-down-list-excel/)
    .
*   [How to Insert Checkbox in Excel](https://trumpexcel.com/insert-checkbox-in-excel/)
    .
*   [Using a Radio Button (Option Button) in Excel](https://trumpexcel.com/insert-use-radio-button-in-excel/)
    .
*   [How to Remove Drop-Down List in Excel?](https://trumpexcel.com/remove-drop-down-list-excel/)
    
*   [Create Data Validation List from Excel Table as Source](https://trumpexcel.com/data-validation-list-from-excel-table/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

39 thoughts on “How to Create a Drop Down List in Excel (the Only Guide You Need)”
----------------------------------------------------------------------------------

1.  how to download calculation ot formula
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-14666)
    
2.  When I try to use an OFFSET formula in my Source field in Data Validation, I’m getting an error message (“there’s a problem with this formula…”) even though the formula works correctly when in a cell by itself. Any ideas why this would happen?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-14596)
    
3.  How do you create a dropdown list with dates? For example, November 1, 2020, November 1, 2021, November 1, 2022 etc.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-14233)
    
4.  Is there any way to make a relational database in excel where i can keep entry cells different and link them to another set of entries. for eg : category in one table linked to products offered in another table. If there is please answer?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-13662)
    
    *   It is possible. I see two or options: (a) fomulaicially, largely using referencing functions, eg index, lookup etc with logical functions probably, or (b) programatically using Excel VBA.
        
        A programmatic solution, using Excel VBA, would need to be supported by using VBA equivalents of spreadsheet functions or where they don’t exist in Excel VBA using the Excel VBA “Application.Spreadsheetfunction …” method to access spreadsheet functions. Knowledge of conditional branching, eg “If”, “Select Case” and looping, For/Next, “Do Until” constructions would be very useful, if not essential in acheiving a programmatic solution. In addition you can make use of VBA User forms for editing records, or creating a spreadsheet-based form which writes and reads record data items from other sheets of data tables. If using either VBA User Form or a spreadsheet template to display records they would need to be accompanied by user entry text fields, buttons, dropdowns, etc (Controls in VBA speak) or cell(s) for fields, Shapes for buttons and spreadsheet dropdowns (data validation) cells. VBA buttons and spreadsheets would have VBA code assigned to them that would be executed when the cuttons are clicked.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-14852)
        
5.  I followed your video to do some assignment. I did it very successful and my supervisor was very happy. Thank-you for the good work you have done by putting all the steps.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12979)
    
6.  Hi, I’m working on an offset dropdown list so that each item is listed once. Say for example that I have 10 items to select, across a possible 20 rows. I noticed that once 10 rows are filled in with the items, the dropdown doesn’t show any items to select (as planned) but I’m able to include any free text in the other void rows, effectively bypassing the dropdown validation. What am I doing wrong?
    
    thanks!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12912)
    
7.  Hello, I was wondering how or if it is even possible to use the Dynamic Drop Down List function to work across different sheets? To keep my spreadsheets clean I keep info used to populate the various pull down lists on one sheet but use them on another. Thank you
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12895)
    
8.  Hi Sumit,  
    Your videos are very helpful and you make it very easy and clear to understand.  
    Keep up the great work and thank you for making Excel look not nearly as daunting as I thought it would be
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12837)
    
9.  I want to create a drop down list where I have full names, but when I choose one of those, instead of the cell shows the full name, it displays only the first letter. For example, the drop down shows Javier, but when I choose that the cell only shows J. How can I do this? Thank you.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12813)
    
10.  I’ve got one spreadsheet that has a huge number of cells that have dynamic drop-down lists, and it is running painfully slow, which I think is caused by having INDIRECT in thousands of cells’ validation. Is there a way to get a dynamic drop-down list that doesn’t use INDIRECT or OFFSET? I’ve tried using INDEX():INDEX() formulas but it’s just throwing an error.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12774)
    
11.  WOW THENKS
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12756)
    
12.  Question,  
    In our Petanque club, we have club matches member A and B playing against members X and Y.  
    Creating a sheet for the results I can use input dropdown lists, with all the members (200+) in, but often I know the first name, but what was the surname again?
    
    Is there a way to start typing in the list so it starts filtering all the John’s or Mary’s in the list?
    
    Would help me a lot, thanks
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12695)
    
13.  Great
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12563)
    
14.  This tutorial is very comprehensive and very helpful. Do more videos, would love to subscribe to your tutorials. Good job!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12530)
    
15.  I Have a query, i have drop-down ( pre & post as inputs) now i want that when i select “pre” i should get the value “x” and when i select post i should get value as blank( like total empty field) , can you suggest any method.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12529)
    
16.  This was helpful. Question: If I want an option which adds 2 items from the list together, how do I do that? I pull in data from a separate sheet using a list which updates my formulas. I need to see POS (point of sale) numbers and APOS (after point of sale) numbers separately and both added together. how do I do this?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12406)
    
17.  Hi, I really enjoyed the instructional videos and have created my own dynamic drop down list. I have two questions:  
    1\. Is there a way to have the drop down list working with the keyboard? (Every time I press the down button my excel workbook closes.)  
    2\. After typing in the name I want to see, can I have the option to scroll down?  
    I would very much appreciate the help!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12363)
    
18.  thanks for the excel book
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12346)
    
19.  Pl. add a pdf file to read the excel training
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12342)
    
20.  I’m using the indirect function to create dependent drop down lists. Why do I need to place an underscore “\_” in front of some of my drop down items with similar but not the exact name? For example, DV, DV0 and DV30. Excel is forcing me to use \_DV0 and \_DV30 as my drop down items rather than simply DV0 and DV30.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12206)
    
    *   ‘DV30’ could be a cell reference (column DV, row 30) and you can’t give a range a name that could also be a cell reference.
        
        [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-12773)
        
21.  VERY HELPFUL
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-11900)
    
22.  It was explained in a very simple and clear manner. Appreciated it. Thank you for the video
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-11822)
    
23.  Thanks for the excellent work
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-11576)
    
24.  Very helpful to me. Thanks
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-11469)
    
25.  Doesn’t work. Downloaded example does nothing when you select fruits. Formula is different than example on this page for use of INDIRECT
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-11094)
    
26.  I understand all that has been written above about independent drop down lists, works great. The problem I have is doing exactly the same but with different workbooks. I have used two workbooks for one drop down and it works with no problem. I have also tried and independent drop down in the same workbook and that also works fine, but as soon as I try to do an independent list, using indirect, in two different workbooks it does not work. I have spent so much time trying to get it to work…my latest attempt is that I have two drop downs in my target file that but they are not independent….can you help!!!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-11068)
    
27.  Nice
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-10886)
    
28.  Hi, I am creating a rota where different tasks/assignments are selected and I want to use drop down lists to select names. The problem is, because it is based on skill levels, I want only those people who have those skills to show on each relevant drop down list.  
    The source I want to use is another sheet with names and check boxes that can be ticked to say they have the relevant skill/s.  
    I don’t know how to link the names-tick boxes-drop down lists all together.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-10875)
    
29.  Dear brother, I’m very grateful to you. Very helpful indeed!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-10813)
    
30.  This is extremely helpful! Thank you so much! Do you know if there is a way to keep the formatting from the original list so that it populates those format changes into the lists when they are created? An example would be that when an option is chosen in the list, that cell is formatted red where others cells (options) are different or no colours. I can’t seem to figure this one out. Thank you!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-10745)
    
31.  By far the most helpful website on this topic!!
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-10637)
    
32.  Hi Hi  
    Can you make the drop down bigger and readable ,. like i have really a long list of supplier names and its rather small , but was wondering any idea to make the drop down bigger.  
    Serena
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-10549)
    
33.  how do I remove an entry from the drop down list selection? I would like to be able to select the same entry again to remove. Essentially selecting again should add back the entry.
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-10539)
    
34.  Pls kindly help me with all the necessary info on EXCEL
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-10436)
    
35.  how do you use dependent drop down list with the first condition being a range of value? for example, if cell A2=100, D,E,F will appear on drop down list?
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-9640)
    
36.  Thank you… excellent explanation. But how do I provide a drop down list that provides the option to complete a response (e.g. a name) that was not in the original list) and better still… have this name automatically included in the database for future drop downs?  
    Consider a list of employees that changes,staff coming in, going out, being able to add a name in the form rather than searching the list must be an advantage others have sought
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-9297)
    
37.  Very Nice…..
    
    [Reply](https://trumpexcel.com/excel-drop-down-list/#comment-3020)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/excel-drop-down-list/#respond)

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