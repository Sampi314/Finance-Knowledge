# How to Highlight Cells With Formulas? 3 Easy Ways!

**Source:** https://trumpexcel.com/highlight-cells-with-formulas-excel

---

[Skip to content](https://trumpexcel.com/highlight-cells-with-formulas-excel/#content "Skip to content")

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](https://trumpexcel.com/wp-content/uploads/2026/03/Sumit-Bansal.jpg)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/highlight-cells-with-formulas-excel/#below-title)

In many situations, you may want to quickly highlight all the cells with formulas in Excel.

When I was working as a financial analyst a few years ago, this is something I used to do often to mark the cells that contain formulas.

Another situation where this may be useful is when you want to share your file with a client or a colleague, and you do not want them to make changes to cells with formulas.

So you can highlight the cells that contain formulas, which also act as a visual indicator to be extra cautious with these cells.

Other times, you may want to quickly highlight cells that contain formulas so that you can get rid of any additional formulas that you do not need in your workbook.

In this short tutorial, I’m going to show you three straightforward ways you can use to quickly **highlight cells with formulas in Excel**.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/highlight-cells-with-formulas-excel/#)

Using Conditional Formatting
----------------------------

The best way to highlight sales with formulas would be by [using conditional formatting](https://trumpexcel.com/excel-conditional-formatting/)
.

Conditional Formatting can be configured to check each cell in a given range (or the entire worksheet) and highlight only those cells that have a formula in them.

Let me show you how this works with a simple example.

Below I have an example data set where I have the Sales Rep name in column A, the sales they have made in column B, and the commission that they have earned in column C.

![Dataset with formulas that we want to highlight](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20531%20373'%3E%3C/svg%3E)

The commission column (i.e., column C) is calculated based on the sales value and contains a formula.

![Column C contains formulas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20530%20419'%3E%3C/svg%3E)

Here are the steps to use conditional formatting to highlight all the cells that contain a formula:

1.  Select the entire data set or the entire worksheet in which you want to highlight the cells with formulas
2.  Click the Home tab

![Click the Home tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20406%20223'%3E%3C/svg%3E)

3.  In the Styles group, click on the Condition Formatting drop-down icon.
4.  Click on the New Rule icon in the options that show up

![Click on New Conditional Formatting rule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20302%20626'%3E%3C/svg%3E)

5.  In the **New Formatting Rule** dialog box, click on the ‘_Use a formula to determine which cells to format_‘ option

![Select use a formula to determine which cells to format option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

6.  Enter the below formula in the field:

\=ISFORMULA(A1)

![Enter the formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20642%20458'%3E%3C/svg%3E)

7.  Click the Format button

![Click the Format button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20640%20418'%3E%3C/svg%3E)

8.  In the ‘Format Cells’ dialog box that opens, select the color with which you want to highlight the cells that have the formulas. In this example, I’ll go with the green color.

![Choose the color to fill the cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20673'%3E%3C/svg%3E)

9.  Click OK
10.  Click OK

As soon as you do the above steps, conditional formatting will instantly highlight all the cells that contain a formula (as shown below).

![Cells with formulas have been highlighted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20531%20373'%3E%3C/svg%3E)

I have used ISFORMULA in conditional formatting to check whether a cell has a formula or not. If it does, ISFORMULA returns TRUE, and the cell gets highlighted with the specified color.

One good thing about condition formatting is that this highlighting is dynamic, which means that in case you remove the formula from a cell, the cell will stop being highlighted. And on the other hand, if you add a formula to any cell (in the range that has the conditional formatting applied to it), it would instantly get highlighted.

**Caution**: One small thing to remember when using conditional formatting is that [it’s volatile](https://trumpexcel.com/excel-volatile-formulas/)
 and can [slow down your workbook](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/)
. While the performance impact is negligible when it’s applied to a small data set, it could lead to a little bit of lag when it’s applied to a large data set in a worksheet or on multiple worksheets in your workbook.

Also read: [How to Lock Formulas in Excel](https://trumpexcel.com/lock-formulas-excel/)

Using the Go-To Option
----------------------

Another quick way to highlight cells that contain formulas is by using the Go-To option in Excel.

With the Go To option, you can select all the cells that contain formulas, and once you have them selected, you can manually highlight them.

Below I have the same data set where I have the names in column A, sales values in column B, and commission values that are calculated using a formula in column C.

![Dataset with formulas that we want to highlight](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20531%20373'%3E%3C/svg%3E)

Here are the steps to highlight all the cells containing formulas:

1.  Select the range in which you want to select the cells that have the formula. If you want to select the entire worksheet, you can click on the gray triangle at the top left part of the worksheet or use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     Control + A + A

![Select entire worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20543%20400'%3E%3C/svg%3E)

2.  Press the F5 key on your keyboard. This will open the Go To dialog box.
3.  Click on the Special button. This will open the Go To Special dialog box.

![Click the Special button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20419%20348'%3E%3C/svg%3E)

_You can also open the Go To Special dialog box by clicking on the Home tab, and then clicking on the Find and Select option (in the Editing group), and then clicking on the Go To Special option._

4.  Select the Formula option in the Go To Special dialog box.

![Click the formula tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20430'%3E%3C/svg%3E)

5.  Click OK

The above steps would select all the cells that contain a formula in the selected range (the one that we selected in Step 1).

6.  Fill color in the selected cells. You can do this by clicking on the Home tab and then using the Fill Color option.

![Fill color in the selected cells with formulas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20544%20466'%3E%3C/svg%3E)

Unlike the Conditional Formatting method, this one is not dynamic.

This means that in case you [remove formulas from any cell](https://trumpexcel.com/convert-formulas-to-values-excel/)
 over adding any formula in another cell, the highlight will not automatically update.

Also read: [How to Hide Formulas in Excel (and Only Display the Value)](https://trumpexcel.com/hide-formulas-excel/)

Using VBA To Highlight Cells with Formulas
------------------------------------------

If this is something that you need to do on a regular basis, you can consider using a simple VBA code to do this.

One benefit of [using VBA](https://trumpexcel.com/excel-vba/)
 is that you can set it up once and then reuse it easily in the same workbook.

You can also save the VBA code in your Personal Macro Workbook so that you can use it on any Excel workbook on your system.

Let me show you how it works.

Below have the same data set where I have formulas in column C that I want to highlight:

![Dataset with formulas that we want to highlight](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20531%20373'%3E%3C/svg%3E)

And here are the steps to highlight cells with formulas using VBA:

1.  Select the range of cells where you want to highlight the cells
2.  Click the Developer tab and then click on the Visual Basic icon. This will [open the VB E](https://trumpexcel.com/visual-basic-editor/)
    ditor for the workbook.

![Click on visual basic icon in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20184'%3E%3C/svg%3E)

3.  Click the Insert option in the menu.
4.  Click on Module. This will insert a new module for the workbook.

![Insert a new module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20340%20322'%3E%3C/svg%3E)

5.  Copy and paste the below VBA code into the module code window.

    'Code developed by Sumit Bansal from https://trumpexcel.com
    
    Sub HighlightCellsWithFormulas()
    
        Dim rng As Range
        Dim cell As Range
        
    
        Set rng = Selection
        
        ' Loop through each cell in the range
        For Each cell In rng
        
            ' Check if the cell contains a formula
            If cell.HasFormula Then
            
                ' Highlight the cell with yellow background color, change RGB values as desired
                cell.Interior.Color = RGB(255, 255, 0)
                
            End If
            
        Next cell
    
    End Sub

6.  Place the cursor anywhere in the code and press the F5 key (to run the macro)
7.  Click on the View Microsoft Excel icon in the menu (or press ALT + F11) to return to the worksheet.

![click on the view Microsoft Excel icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20342%20330'%3E%3C/svg%3E)

You will see that the cells with formulas have been highlighted in yellow color.

![Cells with formula highlighted in yellow color](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20530%20376'%3E%3C/svg%3E)

The above VBA code goes through each cell in the selection and then identifies those cells that have a formula. Once it has identified these cells, it applies the specified fill color to it (which is yellow in this case).

_Remember that the changes done by the VBA code are not reversible. So it’s always a good idea to create a backup copy of your dataset before [running the VBA code](https://trumpexcel.com/run-a-macro-excel/)
._

**Note**: If you want to reuse this code in the workbook, you will have to save your file as a macro-enabled Excel workbook with a .xlsm extension

**Pro Tip**: If you add this code to your Personal Macro Workbook ([click here to learn how](https://trumpexcel.com/personal-macro-workbook/)
) and then add an icon to run this code in the Quick Access Toolbar (QAT), you will then be able to access this code in any of your Excel files on your system with a single click on the QAT

So these are three straightforward methods you can use to quickly highlight all the cells that contain formulas in Excel.

Personally, I prefer using the conditional formatting method as it dynamically identifies cells with formulas while I’m creating data models in Excel.

Many people also prefer the VB method as it only has a one-time setup and can be reused easily.

**Other Excel articles you may also like:**

*   [Formula vs Function in Excel – What’s the Difference?](https://trumpexcel.com/formula-vs-function-excel/)
    
*   [How to Highlight Blank Cells in Excel](https://trumpexcel.com/highlight-blank-cells-in-excel/)
    
*   [Remove Formulas (but Keep Data) in Excel](https://trumpexcel.com/remove-formulas-keep-data-excel/)
    
*   [Highlight Alternate Rows in Excel](https://trumpexcel.com/highlight-every-other-row-excel/)
    
*   [How to Count Cells that Contain Text Strings](https://trumpexcel.com/count-cells-that-contain-text/)
    
*   [How to Copy and Paste Formulas in Excel without Changing Cell References](https://trumpexcel.com/copy-paste-formulas-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/highlight-cells-with-formulas-excel/#respond)

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