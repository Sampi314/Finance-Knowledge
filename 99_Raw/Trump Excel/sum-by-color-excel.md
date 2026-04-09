# How to Sum by Color in Excel (Formula & VBA)

**Source:** https://trumpexcel.com/sum-by-color-excel

---

[Skip to content](https://trumpexcel.com/sum-by-color-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/sum-by-color-excel/#below-title)

Excel has some really amazing functions, but it doesn’t have a function that can sum cell values based on the cell color.

For example, I have the dataset as shown below, and I want to get the sum of all orange and yellow color cells.

![Dataset with colored cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20475%20495'%3E%3C/svg%3E)

Unfortunately, there is no in-built function to do this.

But never say never!

In this tutorial, I will show you three simple techniques you can use to **sum by color in Excel**.

Let’s dive in!

This Tutorial Covers:

[Toggle](https://trumpexcel.com/sum-by-color-excel/#)

SUM Cells by Color Using Filter and SUBTOTAL
--------------------------------------------

Let’s start with the easiest one.

Below I have a dataset where I have the employee names and their sales numbers.

![Dataset with colored cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20475%20495'%3E%3C/svg%3E)

And in this dataset, I want to get the sum of all the cells colored in yellow and orange.

While there is no in-built function in Excel to sum values based on cell color, there is a simple workaround that relies on the fact that you can filter cells based on the cell color.

For this method, enter the below formula in cell B17 (or any cell in the same column below the colored cells dataset).

\=SUBTOTAL(9,B2:B15)

![Subtotal formula to get the sum of sales](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20485%20618'%3E%3C/svg%3E)

In the above SUBTOTAL formula, I have used 9 as the first argument, which tells the function that I want to get the sum of the range that is given as the second argument.

_But why not just use the SUM formula instead?_

This is because when I have the SUBTOTAL formula and I filter the cells to only show those cells that have a specific color in it, the SUBTOTAL formula will show me the sum of visible cells only (something that the SUM formula can not do).

So once you have the SUBTOTAL formula, follow the below steps to get the SUM based on cell color:

1.  Select any cell in the dataset
2.  Click the Data tab

![Click the Data tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20674%20223'%3E%3C/svg%3E)

3.  In the Sort and Filter group, click on the Filter icon. This will apply filter to the dataset and you will be able to see the filter icon in the headers

![Click the Filter icon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20836%20223'%3E%3C/svg%3E)

4.  In the Sales header cell, click on the Filter icon

![Filter icon in the headers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20517%20588'%3E%3C/svg%3E)

5.  Go to the Filter by Color” option
6.  Select the color based on which you want to filter the dataset.

![Select the color for which you want to sum by color](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20624%20615'%3E%3C/svg%3E)

As soon as you do this, you will notice that the subtotal result changes and it will now only give you the sum of those cells that are visible (which would only be those cells that have the color by which you filtered the dataset).

![SUM by color value in the SUBTOTAL formula result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20276'%3E%3C/svg%3E)

Similarly, if you [filter](https://trumpexcel.com/excel-data-filter/)
 by some other color in the data set (say orange instead of yellow), the SUBTOTAL function would accordingly adjust and give you the sum of all cells with orange color

**Pro Tip**: [Keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 to apply a filter to a dataset is Control + Shift + L (hold the Control and the Shift key, and then press the L key). If using Mac, use Command + Shift + L

Also read: [SUM Based on Partial Text Match in Excel (SUMIF)](https://trumpexcel.com/sum-partial-match/)

SUM Cells by Color Using VBA
----------------------------

I mentioned that there is no in-built formula in Excel to sum based on cell color value. However, you can [create your own formula](https://trumpexcel.com/user-defined-function-vba/)
 to do this using VBA.

With VBA, you can create a custom function that you can keep in the back end, and then use it like any other regular function in the worksheet.

Below is the VBA code that will create that custom function that allows you to sum by color in Excel.

'Code created by Sumit Bansal from https://trumpexcel.com/
'This VBA code created a function that can be used to sum cells based on color
Function SumByColor(SumRange As Range, SumColor As Range)
Dim SumColorValue As Integer
Dim TotalSum As Long
SumColorValue = SumColor.Interior.ColorIndex
Set rCell = SumRange
For Each rCell In SumRange
If rCell.Interior.ColorIndex = SumColorValue Then
TotalSum = TotalSum + rCell.Value
End If
Next rCell
SumByColor = TotalSum
End Function

To use this VBA custom function, you will first have to copy this code and paste it in the back end in the VB editor.

Once done, you’ll be able to use this function in the worksheet.

Below are the steps to add this code to the [VB editor](https://trumpexcel.com/visual-basic-editor/)
.

1.  Click the Developer tab in the ribbon (if you don’t have the Developer tab visible, [click here to learn how to get it](https://trumpexcel.com/excel-developer-tab/)
    )
2.  Click on the Visual Basic icon. This will open the Visual Basic editor of Excel.

![Click on Visual Basic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20191'%3E%3C/svg%3E)

3.  Click the Insert option in the menu
4.  Click on Module. This will insert a new module and you will be able to see it in the project explorer (a pane on the left that shows all the objects). If you don’t see the Project Explorer pane, click on View and then click on Project Explorer

![Insert a Module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20332%20261'%3E%3C/svg%3E)

5.  Copy the above VBA code and paste it in the newly inserted Module code window

![Copy paste the code in the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20295'%3E%3C/svg%3E)

6.  Close the VB Editor

Now that you have the code in the back end in excel, you will be able to use the function that we created (SumByColor) in the worksheet.

For this function to work, I will need a cell in the worksheet that contains the same color for which I want to get the sum.

In our example, I have done that to cells D2 and D3, where D2 has the yellow color and D3 has the orange color.

Now I can use the below formula in these cells:

\=SumByColor($B$2:$B$15,D2)

![SUM by Color formula usage in the worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20703%20546'%3E%3C/svg%3E)

The above formula takes two arguments:

*   The range of cells that have the color that I want to add
*   [Reference to any cell](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
     that contains the color (so that the formula can pick the color index and use that as a condition to add the values)

Note that the formula is dynamic and would automatically update in case you make any changes to the data set (such as changing any value or applying/removing color from some cells). And in case you notice that the formula is not updating, hit the F9 key and it would update.

Since we have used a VBA code in the workbook, it needs to be saved as a macro-enabled workbook (with .XLSM extension).

**Pro Tip**: If adding cells based on their background color is something you need to do quite often, I recommend you copy and paste this VBA code for the custom formula in the [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
. This way, that would be available on all your workbooks on your system.

Also read: [Filter By Color in Excel](https://trumpexcel.com/filter-by-color-excel/)

SUM Cells by Color Using GET.CELL
---------------------------------

The final method I want to show you include a hidden Excel formula (that not many people know about).

This method uses the GET.CELL function, which can get us the color index value of colored cells.

And once we have the color index value of each cell, we can then use a simple sum if formula to only get the sum of cells with a specific color in it.

It’s not as elegant as the VBA custom function I covered earlier, but if you don’t want to use VBA, then this could be the way to go for you.

GET.CELL is an old Macro 4 function that has been kept in Excel for compatibility reasons, but you won’t find many details about it (as it’s rarely used).

Below I have a dataset where I have colored cells that I want to sum.

![Dataset with colored cells](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20475%20495'%3E%3C/svg%3E)

For this technique to work, we first need to create a named range that will use the GET.CELL function to give the color value of a colored cell.

Here are the steps to do this:

1.  Click the Formulas tab in the Ribbon
2.  In the Defined Names group, click on the ‘Name Manager’

![Click on Name Manager](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20795%20222'%3E%3C/svg%3E)

3.  In the Name Manager dialog box, click on New

![Click on the New button in the Name Manager dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20469'%3E%3C/svg%3E)

4.  In the ‘New Name dialog box, enter the Name – SumColor

![Enter the name of the new named range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20377%20289'%3E%3C/svg%3E)

5.  In the Refers to field, enter the following formula: =GET.CELL(38,$B2)

![Enter the Get.Cell formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20377%20289'%3E%3C/svg%3E)

6.  Click OK
7.  Close the Name Manager dialog box

The above steps have [created a named range](https://trumpexcel.com/named-ranges-in-excel/)
 that we can now use in the workbook.

Note: GET.CELL function takes two arguments, the first one is a number that tells the function what information we need, and the second is the cell reference of that cell itself. In this case, I have 38 as the first argument, which would give us the color index value of the referred cell.

Now the second step is to get the color index values of all the colors in column B.

Below are the steps to do this:

1.  In cell C1, enter the header – Color Index (or anything that you to call it)

![Add a new color index column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20650%20497'%3E%3C/svg%3E)

2.  In cell C2, enter the following formula: =SumColor

![Use the SUMCOLOR formula](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20545'%3E%3C/svg%3E)

3.  Apply the same formula for all the cell in column C (you can use the [fill handle](https://trumpexcel.com/how-to-use-fill-handle-in-excel/)
     or simply copy paste cell C2)

![Copy Paste formula in the entire column](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20646%20496'%3E%3C/svg%3E)

The above steps would give you a value that would represent the color index of the cell in column B (the cell on the left).

SumColor is the named range we created and it uses the GET.CELL function to get the color index value of the cell on the left. You can use this formula in any column, but it should always start from the second cell in that column. For example, instead of column C, you can have this in column H or J, but from the second cells in these columns.

Now that we have a unique number for each color, we can use this to get the SUM of cells based on their color.

Below are the steps to do this:

1.  In cell E2 and E3, give the cells the color for which you want to get the sum. In my case, I have yellow color in cell E2 and orange in cell E3

![Have same color in two cells in the worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20672%20386'%3E%3C/svg%3E)

2.  In cell F2, enter the following formula: =SUMIF(C2:C15,SumColor,B2:B15)

![Formula to get sum by color using named range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20402'%3E%3C/svg%3E)

3.  Copy the cell and paste in cell F3 (this could copy the formula as well and adjust the references).

![Copy the formula to the next cell as well](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20756%20434'%3E%3C/svg%3E)

The above steps would give you the sum of all the cells that have the color in the adjacent selling column F.

We have used a [SUMIF formula](https://trumpexcel.com/excel-sumif-function/)
, where it adds all the values in column B, if the color index of the cell on the left (in column F) is the same as that in column C.

While this is definitely a slightly longer way to sum cells by color (as compared with SUBTOTAL or VBA), this gets the work done, and you only need to do this setup once.

Note that while the formula is dynamic, in case you make any changes (such as changing the color cells in column B or removing the color from it), the change might not be reflected instantly in the SUMIF formula. A simple workaround for it would be to go to the cell that has the formula, click the F2 key to get into the airport, and then hit the enter key. This would force the formula to recalculate and you will get the updated result.

So these are three methods you can use to sum by color in Excel. While SUBTOTAL is quite easy and straightforward, I personally like the VBA method better.

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [Count Characters in a Cell (or Range of Cells) Using Formulas in Excel](https://trumpexcel.com/count-characters-in-excel/)
    
*   [How to Count Colored Cells in Excel](https://trumpexcel.com/count-colored-cells-in-excel/)
    
*   [How to Sort By Color in Excel (in less than 10 seconds)](https://trumpexcel.com/sort-by-color/)
    
*   [How to Apply Formula to Entire Column in Excel](https://trumpexcel.com/apply-formula-to-entire-column-excel/)
    
*   [How to Sum Only Positive or Negative Numbers in Excel (Easy Formula)](https://trumpexcel.com/sum-positive-numbers-excel/)
    
*   [How to SUM values between two dates (using SUMIFS formula)](https://trumpexcel.com/sum-between-two-dates-sumifs-excel/)
    
*   [How to Combine Duplicate Rows and Sum the Values in Excel](https://trumpexcel.com/combine-duplicate-rows-and-sum-values-excel/)
    
*   [How to Sum Across Multiple Sheets in Excel? (3D SUM Formula)](https://trumpexcel.com/sum-across-multiple-sheets-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “How to Sum by Color in Excel (Formula & VBA)”
------------------------------------------------------------

1.  Goodness, I have been screwing around with this for way too long. One short video and you solved my quest. Thank you so much!!
    
    [Reply](https://trumpexcel.com/sum-by-color-excel/#comment-55491)
    
    *   Glad the video helped 🙂
        
        [Reply](https://trumpexcel.com/sum-by-color-excel/#comment-55796)
        
2.  Thank you for this useful summary. BTW, if you use get.cell, it requires saving the file as xlsm.
    
    [Reply](https://trumpexcel.com/sum-by-color-excel/#comment-33390)
    
3.  How do I sum if I have coloured the parallel Column, like Having the numbers in the K column and colour in the J column, and I want the sum of the column K if the J column cell is green or any other colour.
    
    Thank You
    
    [Reply](https://trumpexcel.com/sum-by-color-excel/#comment-33288)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/sum-by-color-excel/#respond)

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