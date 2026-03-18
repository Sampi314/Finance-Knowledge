# Highlight Rows Based on a Cell Value in Excel (Conditional Formatting)

**Source:** https://trumpexcel.com/highlight-rows-based-on-cell-value

---

[Skip to content](https://trumpexcel.com/highlight-rows-based-on-cell-value/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/highlight-rows-based-on-cell-value/#below-title)

**Watch Video – Highlight Rows based on Cell Values in Excel**

In case you prefer reading written instruction instead, below is the tutorial.

[Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
 allows you to format a cell (or a range of cells) based on the value in it.

But sometimes, instead of just getting the cell highlighted, you may want to highlight the entire row (or column) based on the value in one cell.

To give you an example, below I have a dataset where I have highlighted all the rows where the name of the Sales Rep is Bob.

![Highlight Rows Based on Cell Value - which is Bob](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20607%20436'%3E%3C/svg%3E)

In this tutorial, I will show you how to highlight rows based on a cell value using conditional formatting using different criteria.

**[Click here](https://www.dropbox.com/s/w6ho3ke1fpf0nwq/Highlight%20Rows%20Based%20on%20Cell%20Value.xlsx?dl=1)
** to download the Example file and follow along.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/highlight-rows-based-on-cell-value/#)

Highlight Rows Based on a Text Criteria
---------------------------------------

Suppose you have a dataset as shown below and you want to highlight all the records where the Sales Rep name is Bob.

![DataSet where you want to highlight rows where name is Bob](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20607%20436'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select the entire dataset (A2:F17 in this example).
2.  Click the Home tab.![Home Tab in the Excel Ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20316%20192'%3E%3C/svg%3E)
3.  In the Styles group, click on Conditional Formatting.![Click on Conditional Formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20595%20122'%3E%3C/svg%3E)
4.  Click on ‘New Rules’.![Click on New Rule - Highlight Rows Based on a Cell Value in Excel (Conditional Formatting)](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20248%20462'%3E%3C/svg%3E)
5.  In the ‘New Formatting Rule’ dialog box, click on ‘Use a formula to determine which cells to format’.![Use Formula Option to Highlight Rows based on cell value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20447'%3E%3C/svg%3E)
6.  In the formula field, enter the following formula: **\=$C2=”Bob”![Specify the Formula to Highlight rows if it is True](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)**
7.  Click the ‘Format’ button.![Click on the Format Button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)
8.  In the dialog box that opens, set the color in which you want the row to get highlighted.![Color to Fill to highlight the rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20480'%3E%3C/svg%3E)
9.  Click OK.

This will highlight all the rows where the name of the Sales Rep is ‘Bob’.

![All rows where name is Bob are highlighted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20433'%3E%3C/svg%3E)

**[Click here](https://www.dropbox.com/s/w6ho3ke1fpf0nwq/Highlight%20Rows%20Based%20on%20Cell%20Value.xlsx?dl=1)
** to download the Example file and follow along.

**How does it Work?**

Conditional Formatting checks each cell for the condition we have specified, which is **\=$C2=”Bob”**

So when it’s analyzing each cell in row A2, it will check whether the cell C2 has the name Bob or not. If it does, that cell gets highlighted, else it doesn’t.

Note that the trick here is to use a dollar sign ($) before the column alphabet ($C1). By doing this, we have locked the column to always be C. So even when cell A2 is being checked for the formula, it will check C2, and when A3 is checked for the condition, it will check C3.

This allows us to highlight the entire row by conditional formatting.

**Related**: [Absolute, Relative, and Mixed references](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 in Excel.

Highlight Rows Based on a Number Criteria
-----------------------------------------

In the above example, we saw how to check for a name and highlight the entire row.

We can use the same method to also check for numeric values and highlight rows based on a condition.

Suppose I have the same data (as shown below), and I want to highlight all the rows where the quantity is more than 15.

![DataSet where you want to highlight rows where name is Bob](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20607%20436'%3E%3C/svg%3E)

Here are the steps to do this:

1.  Select the entire dataset (A2:F17 in this example).
2.  Click the Home tab.
3.  In the Styles group, click on Conditional Formatting.
4.  Click on ‘New Rules’.
5.  In the ‘New Formatting Rule’ dialog box, click on ‘Use a formula to determine which cells to format’.
6.  In the formula field, enter the following formula: **\=$D2>=15![Formula to Highlight all Rows Based on a Number Criteria](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20447'%3E%3C/svg%3E)**
7.  Click the ‘Format’ button. In the dialog box that opens, set the color in which you want the row to get highlighted.
8.  Click OK.

This will highlight all the rows where the quantity is more than or equal to 15.

![Resulting Data when Highlighting rows based on number criteria](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20605%20430'%3E%3C/svg%3E)

Similarly, we can also use this to have criteria for the date as well.

For example, if you want to highlight all the rows where the date is after 10 July 2018, you can use the below [date formula](https://trumpexcel.com/excel-date-function/)
:

\=$A2>DATE(2018,7,10)

Highlight Rows Based on a Multiple Criteria (AND/OR)
----------------------------------------------------

You can also use multiple criteria to highlight rows using conditional formatting.

For example, if you want to highlight all the rows where the Sales Rep name is ‘Bob’ and the quantity is more than 10, you can do that using the following steps:

1.  Select the entire dataset (A2:F17 in this example).
2.  Click the Home tab.
3.  In the Styles group, click on Conditional Formatting.
4.  Click on ‘New Rules’.
5.  In the ‘New Formatting Rule’ dialog box, click on ‘Use a formula to determine which cells to format’.
6.  In the formula field, enter the following formula: **\=AND($C2=”Bob”,$D2>10)![Formula to Use Mutliple conditions when highlighting rows in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20447'%3E%3C/svg%3E)**
7.  Click the ‘Format’ button. In the dialog box that opens, set the color in which you want the row to get highlighted.
8.  Click OK.

In this example, only those rows get highlighted where both the conditions are met (this is done using the AND formula).

![Result when rows are highlighted based on multiple conditions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20607%20435'%3E%3C/svg%3E)

Similarly, you can also use the [OR condition](https://trumpexcel.com/excel-or-function/)
. For example, if you want to highlight rows where either the sales rep is Bob or the quantity is more than 15, you can use the below formula:

**\=OR($C2="Bob",$D2>15)**

**[Click here](https://www.dropbox.com/s/w6ho3ke1fpf0nwq/Highlight%20Rows%20Based%20on%20Cell%20Value.xlsx?dl=1)
** to download the Example file and follow along.

Highlight Rows in Different Color Based on Multiple Conditions
--------------------------------------------------------------

Sometimes, you may want to highlight rows in a color based on the condition.

For example, you may want to highlight all the rows where the quantity is more than 20 in green and where the quantity is more than 15 (but less than 20) in orange.

To do this, you need to create two conditional formatting rules and set the priority.

Here are the steps to do this:

1.  Select the entire dataset (A2:F17 in this example).
2.  Click the Home tab.
3.  In the Styles group, click on Conditional Formatting.
4.  Click on ‘New Rules’.
5.  In the ‘New Formatting Rule’ dialog box, click on ‘Use a formula to determine which cells to format’.
6.  In the formula field, enter the following formula: **\=$D2>15![Formula to Highlight rows where value is more than 15](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20447'%3E%3C/svg%3E)**
7.  Click the ‘Format’ button. In the dialog box that opens, set the color to Orange.
8.  Click OK.
9.  In the ‘Conditional Formatting Rules Manager’ dialog box, click on ‘New Rule’.![Click on New Rule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20772%20364'%3E%3C/svg%3E)
10.  In the ‘New Formatting Rule’ dialog box, click on ‘Use a formula to determine which cells to format’.
11.  In the formula field, enter the following formula: **\=$D2>20![Formula to Highlight rows where value is more than 20](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)**
12.  Click the ‘Format’ button. In the dialog box that opens, set the color to Green.
13.  Click OK.
14.  Click Apply (or OK).

The above steps would make all the rows with quantity more than 20 in green and those with more than 15 (but less than equal to 20 in orange).

![Data where rows are highlighted in two colors](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20607%20434'%3E%3C/svg%3E)

**Understanding the Order of Rules:**

When using multiple conditions, it important to make sure the order of the conditions is correct.

In the above example, the Green color condition is above the Orange color condition.

![Order of Conditions when formatting rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20772%20364'%3E%3C/svg%3E)

If it’s the other way round, all the rows would be colored in orange only.

Why?

Because a row where quantity is more than 20 (say 23) satisfies both our conditions (=$D2>15 and =$D2>20). And since Orange condition is at the top, it gets preference.

You can change the order of the conditions by using the Move Up/Down buttons.

![Buttons to change the order of formatting](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20772%20364'%3E%3C/svg%3E)

**[Click here](https://www.dropbox.com/s/w6ho3ke1fpf0nwq/Highlight%20Rows%20Based%20on%20Cell%20Value.xlsx?dl=1)
** to download the Example file and follow along.

Highlight Rows Where Any Cell is Blank
--------------------------------------

If you want to highlight all rows where any of the cells in it is blank, you need to check for each cell using conditional formatting.

Here are the steps to do this:

1.  Select the entire dataset (A2:F17 in this example).
2.  Click the Home tab.
3.  In the Styles group, click on Conditional Formatting.
4.  Click on ‘New Rules’.
5.  In the ‘New Formatting Rule’ dialog box, click on ‘Use a formula to determine which cells to format’.
6.  In the formula field, enter the following formula: **\=COUNTIF($A2:$F2,””)>0![Using Countif to count blank rows](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20448'%3E%3C/svg%3E)**
7.  Click the ‘Format’ button. In the dialog box that opens, set the color to Orange.
8.  Click OK.

The above formula counts the number of blank cells. If the result is more than 0, it means there are blank cells in that row.

If any of the cells are empty, it highlights the entire row.

![Highlighting Blank rows - Resulting Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20606%20433'%3E%3C/svg%3E)

**Related:** Read this tutorial if you only want to [highlight the blank cells](https://trumpexcel.com/highlight-blank-cells-in-excel/)
.

Highlight Rows Based on Drop Down Selection
-------------------------------------------

In the examples covered so far, all the conditions were specified with the conditional formatting dialog box.

In this part of the tutorial, I will show you how to make it dynamic (so that you can enter the condition within a cell in Excel and it will automatically highlight the rows based on it).

Below is an example, where I select a name from the drop-down, and all the rows with that name get highlighted:

![Highlight Entire Row Based on Drop Down Selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20716%20444'%3E%3C/svg%3E)

Here are the steps to create this:

1.  Create a drop-down list in cell A2. Here I have used the names of the sales rep to create the drop down list. Here is a detailed guide on how to [create a drop-down list in Excel](https://trumpexcel.com/excel-drop-down-list/)
    .
2.  Select the entire dataset (C2:H17 in this example).
3.  Click the Home tab.
4.  In the Styles group, click on Conditional Formatting.
5.  Click on ‘New Rules’.
6.  In the ‘New Formatting Rule’ dialog box, click on ‘Use a formula to determine which cells to format’.
7.  In the formula field, enter the following formula: **\=$E2=$A$2![Rule to Highlight Cells that match the drop down value](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20447'%3E%3C/svg%3E)**
8.  Click the ‘Format’ button. In the dialog box that opens, set the color to Orange.
9.  Click OK.

Now when you select any name from the drop-down, it will automatically highlight the rows where the name is the same that you have selected from the drop-down.

Interested in learning more on how to [search and highlight in Excel](https://trumpexcel.com/search-highlight-using-conditional-formatting/)
? Check the below videos.

**You May Also Like the Following Excel Tutorials:**

*   [Dynamic Excel Filter – Extracts Data as you Type](https://trumpexcel.com/dynamic-excel-filter/)
    .
*   [Create a drop-down list with a search suggestion](https://trumpexcel.com/excel-drop-down-list-with-search-suggestions/)
    .
*   [How to Insert and Use a Checkbox in Excel](https://trumpexcel.com/insert-checkbox-in-excel/)
    .
*   [Select Visible Cells in Excel](https://trumpexcel.com/select-visible-cells/)
    .
*   [Highlight Active Row/Column in a Data Range](https://trumpexcel.com/highlight-active-row-column-excel/)
    .
*   [Delete rows based on cell value in Excel](https://trumpexcel.com/delete-rows-based-on-cell-value/)
    
*   [How to Delete Every Other Row in Excel](https://trumpexcel.com/delete-every-other-row-excel/)
    
*   [Apply Conditional Formatting Based on Another Column in Excel](https://trumpexcel.com/conditional-formatting-based-on-another-column-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

67 thoughts on “Highlight Rows Based on a Cell Value in Excel (Conditional Formatting)”
---------------------------------------------------------------------------------------

1.  Not working in Excel online
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-16674)
    
2.  Very helpful. These step-by-step instructions with examples, especially on how to highlight based on multiple criteria, gave me a good understanding of the topic. I was able to figure out the right solution to a challenge I was having. Thank you!
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-16454)
    
3.  Kind of worked. Selected rows, used basic format of your rule “=$C2=”Bob”. However it highlighted the row above the first instance of “Bob” and didn’t highlight the last instance of “Bob”.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-16080)
    
4.  I need help! example…I need a format which shows if any cells in the whole of row 2 say YES (could be more than 1) then I need a visual highlighted cell at the start of that row to flag and tell me I need to look through row 2 (because there a yes along there somewhere).
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-14927)
    
5.  Thank you so much . Helped a lot
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-14514)
    
6.  Hey Sumit, great stuff
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-14501)
    
7.  I followed the first one highlight based on a text value it almost worked but it’s highlighting the row above the one which has the text value in. No idea what I did wrong.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-14210)
    
    *   I had the same issue use =$C1=”bob” worked for me
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-14363)
        
8.  Thanks, excellent – it works very well and it gives a great advantage in displaying dynamic data
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-13833)
    
9.  Doesnt work. No matter what I try, it doesnt work.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-13505)
    
10.  Hello,
    
    My Formatting only seems to work for the first 3 rows, I have tried everything.
    
    Other spreadsheets where I have used this formula work just fine.  
    Would anyone know what the issue may be?
    
    I select the table, new rule and add: =$b6=”APPROVED”  
    2 out of 18 work, the rest remain white.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-13401)
    
11.  Thank you for explaining WHY the formula does what it does. Understanding why cells behave the way they do is so key to remembering how to make them do it!
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-13380)
    
12.  If I have a row of 5 cells containing numbers, how can I format it to show where more than one of the cells are greater than zero? the cell content is dynamic!
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-13175)
    
13.  It works perfectly on a local excel file but stops working when that is uploaded on SharePoint. Any idea how to fix it?
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-13135)
    
14.  Im trying to apply this rule on a drop down list, to color the entire row based on the options in the list “in process – on hold…” however its not working when typing the text between ” ” i get an error. any suggestions please?
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-13090)
    
15.  How can i highlight a certain number of rows and columns in a range based on user input? For instance i have a 10×10 range and the user inputs “3” for rows and “5” for columns. How can i turn the cells in the first 3 rows and 5 columns in my range yellow.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-13036)
    
16.  How can we adjust this VBA code to only format the data from the active row that is currently selected?
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-13007)
    
17.  Simple but really usefull. Thanks !
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12917)
    
18.  This helped me big time with my 28,000 cell spreadsheet I’m working with. Thank you!!!
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12855)
    
19.  Is there a way to highlight a whole row if /any/ value is entered into a cell? For instance: I have a column of “Rejection Reasons” there are any number of different reasons for rejecting a thing (too many for a drop down list), but I want to highlight the row if the thing was rejected for any reason. Can I do that? Basically the opposite of highlighting based on a blank cell.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12666)
    
    *   I think you’d just highlight cells that are greater than zero.
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12847)
        
20.  How do I do highlight the entire row directly based on the value I select from the drop-down menu? E.G. not having a SEPARATE drop-down menu: this example, make the cells in the “Sales Rep” column drop downs.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12624)
    
    *   Wouldn’t you just highlight based on specific text? Above, the goal of highlighting based on a drop down selection is to show the rows that contain that text. It sounds like you just want different colors for different Sales Reps, which you could do by using the first tutorial provided here (highlight specific text) where each Rep has their own color.
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12846)
        
21.  I got the conditional formatting to work for my pivot. However when any changes are made to the data displayed (e.g., collapsing a row expansion) all the CF rules are reset to apply to the first row in the PT. I using $A$10:$M$308 for the range of the CF; should I somehow do this differently?
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12512)
    
22.  I am having a problem using Conditional formatting to find cells with unique values. I have 3 columns across my spreadsheet (D, E & F). I want to compare the 3 values in every row separately. Conditional formatting works great, 1 row at a time. How can I copy the formula down my entire spreadsheet?
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12355)
    
23.  I have a problem with this. When I follow the instructions, the whole table is highlighted, but not only one row. What am I doing wrong?
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12084)
    
    *   You’re probably missing the dollar sign in front of the column letter. E.e. C3 vs $C3
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12848)
        
24.  I followed your instructions and it worked for =$F2=”N/A” Then, I tried adding another formula for a new word =$F2=”PENDING” and it didn’t work anymore. What is the best way to resolve my issue? Thanks in advance
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12073)
    
    *   The only thing I can think of is to double check what the formula applies to. If all your data is from A2 down and across to M67, go into the Conditional Formatting drop down, select Manage Rules …, and ensure the Applies to column next to your formulas lists =$A$2:$M$67 so that the formula covers your whole table.
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12076)
        
25.  Thanks!!
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12059)
    
26.  Wow!! great tutorial. I knew conditional formatting but did not know that one could do so much. Thanks!!
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12044)
    
27.  I was actually looking to find out how to highlight a cell based on if a number was greater then or equal to a number in the same row, not a static number, and if it was lower than a number in the same row. I was able to use your formulas here to discover it. If anyone else needs this, I selected my area I wanted to become highlighted, drop down conditional formatting, manage rules, new rule, went to use a formula to determine which cells to format, and then used the following formulas for each rule:
    
    \=$E2=$C2
    
    This will cause the formula to look at the two corresponding numbers, so for me, if the generated number is greater than the estimated number, it’s green. Lower than the estimated number, it’s red. Hope this helps someone else out there.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11883)
    
    *   Apparently it didn’t format it properly, the formulas are
        
        \=$E2\[LESS THAN\]$C2  
        \=$E2\[GREATER THAN\]=$C2
        
        Hopefully this will show up.
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11884)
        
28.  Need to know how to highlight a row when the first a cell in column A contains a specific word (not =). What if Bob Dylan? Need whole row highlighted when the cell contains “Bob” regardless of last name or other words contained w/in the same cell.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11854)
    
    *   Ruth, try putting “\*Bob\*” for the input instead. If anything comes before or after Bob it will be highlighted, so it could be Bob Dylan or Dylan, Bob or Dylan, Bob J. and it will highlight.
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11882)
        
29.  I have a column which formats the cell to R/A/G based on priority, how can I also apply another format to make the whole line grey when it is complete, this would be a separate column.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11788)
    
    *   Create a conditional formatting rule for complete and make sure it is listed ABOVE your priority filter in the list of conditional formats applied to that area.
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12849)
        
30.  Great tutorial I have always had trouble getting Conditional Formatting to work and it work first time using your tutorial. Don’t know why others say it doesn’t work.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11777)
    
31.  Fantastic
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11588)
    
32.  It should be $D1, $D2 highlights the next row instead. Also you need to say that is applies to all the sheet
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11555)
    
33.  Really useful. Appreciate it.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11523)
    
34.  How can you do this if you want a row to turn a certain color as soon as on cell is populated? In my case it is populated by a date.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11514)
    
    *   $D2>0 will highlight anything that is not blank.
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12850)
        
35.  This did not work for me either. I had to do a workaround to have it come out the way I wanted.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11488)
    
36.  Is there a way to do the first method, but as you go?
    
    Basically a way that you can automatically have the row fill based on one cell, but not have to do the format every time and have this happen as you fill in your spread sheet?
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11394)
    
    *   Once you create the rule, you have to change the area it applies to so that it covers your entire table. In the “Conditional Formatting Rules Manager” you’ll select the applicable area for that rule under “Applies to”.
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12851)
        
37.  only highlights the cells containing criteria but not the entire row
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11387)
    
    *   Once you create the rule, you have to change the area it applies to so that it covers your entire table. In the “Conditional Formatting Rules Manager” you’ll select the applicable area for that rule under “Applies to”.
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12852)
        
38.  doesn’t work. tried the first example and it highlighted the row ABOVE where the selected text appeared.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11380)
    
    *   Make sure the D2 is highlighted when you’re creating a rule based on D2.
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12853)
        
    *   I had the same issue. When I changed the formula to $C1 instead of $C2 it highlighted the correct row.
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-38192)
        
39.  you forgot to include the “Applies to” cell range to get it to highlight the full row.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11351)
    
40.  This did not work as I wanted to shade rows where the content was in a ‘Day column to shade rows with ‘Friday’ in them, but the cell was derived by a formula ‘=WEEKDAY(A6)’ so it doesn’t recognise the cell is a Friday
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11300)
    
41.  Thanks. Useful information.
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11291)
    
42.  It did not work. I have a table(which I then changed back to a range) from A2 to L371. My formula was =L$13=”Inactive”. Column L has blank cells, cells with the word Active, and cells with the word “Inactive”. This method, highlighted mostly cells that said Active, ?? I then capitalized all the INACTIVE rows – still nothing. I’m so confused. Why this didn’t work – does the reference cell need to be the in the beginning?
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11190)
    
    *   You put the dollar sign on the row number instead of the column number which means it will only look at the 13th row when evaluating the formatting.
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12854)
        
43.  Thank youuu!!!!!
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11151)
    
44.  looking for highlight the cells and values belongs to a formula cell
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11136)
    
45.  great
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11135)
    
46.  hi, If i type the number 5 in excel cell, 5 rows should be need to highlighted in excel . how to do this?
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-11024)
    
47.  this formula has 2 typos: the quotation marks are closing quotations. Delete these in this formula and replace them and type fresh quotations around the text “Bob”
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-10989)
    
48.  Highlight Rows Based on a Text Criteria not working for whole row & Also not automatically applies to whole table…
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-10941)
    
49.  I agree Kristin P, something doesn’t seem right with the explanation for formatting based on text
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-10932)
    
50.  Is there a typo in the first explanation (Highlight based on Text) as to which cells you select the formula to apply to?
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-10823)
    
    *   No, it works super fine for me
        
        [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-12550)
        
51.  Thank You Very Very Much…
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-10684)
    
52.  Your program is contributing to my Excel Growth
    
    [Reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#comment-10335)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/highlight-rows-based-on-cell-value/#respond)

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