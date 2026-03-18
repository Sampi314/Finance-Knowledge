# Using Active Cell in VBA in Excel (Examples)

**Source:** https://trumpexcel.com/active-cell-vba-excel

---

[Skip to content](https://trumpexcel.com/active-cell-vba-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/active-cell-vba-excel/#below-title)

‘Active Cell’ is an important concept in Excel.

While you don’t have to care about the active cell when you’re working on the worksheet, it’s an important thing to know when working with VBA in Excel.

Proper use of the active cell in Excel VBA can help you write better code.

In this tutorial, I first explained what is an active cell, and then show you some examples of how to use an active cell in VBA in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/active-cell-vba-excel/#)

What is an Active Cell in Excel?
--------------------------------

An active cell, as the name suggests, is the currently active cell that will be used when you enter any text or formula in Excel.

For example, if I select cell B5, then B5 becomes my active cell in the worksheet. Now if I type anything from my keyboard, it would be entered in this cell, because this is the active cell.

While this may sound obvious, here is something not that obvious – when you select a range of cells, even then you would only have one active cell.

For example, if I select A1:B10, although I have 20 selected cells, I still have only one single active cell.

So now, if I start typing any text or formula, it would only be entered in the active cell.

You can identify the active cell by looking at the difference in color between the active cell in all the other cells in the selection. You would notice that the active cell is of a lighter shade than the other selected cells.

![Active cell is highlighted in a different color](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20470%20417'%3E%3C/svg%3E)

Another quick way to know which cell is the active cell is by looking at the [Name box](https://trumpexcel.com/name-box-excel/)
 (the field that is next to the formula bar). The [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 of the active cell would be shown in the Name Box.

![Active cell address is shown in the name box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20472%20474'%3E%3C/svg%3E)

Using Active Cell in VBA in Excel
---------------------------------

Now that I’ve explained what is an active cell in a worksheet in excel, let’s learn how an Active cell can be used in Excel VBA.

### Active Cell Properties and Methods

In VBA, you can use an active cell in two ways:

1.  To get the information about it (these are called **Properties**)
2.  To perform some action on it (these are called **Methods**)

Here is how you can access all the properties and methods of an active cell in VBA:

1.  Open a Module in [Excel VBA editor](https://trumpexcel.com/visual-basic-editor/)
    
2.  Type the phrase ‘ActiveCell’
3.  Enter a dot (.) after the word ActiveCell

As soon as you do this, you would notice that a set of properties and methods appear as a drop-down (this is called an IntelliSense in Excel VBA).

In the drop-down that appears, you would see two types of options – the one that has a green icon and the one that has a gray icon (with a hand).

The one with the grey icons is the Properties, and the one with the green icons is the Methods.

Some examples of Methods would include Activate, AddComment, Cut, Delete, Clear, etc. As you can notice, these are actions that can be performed on the active cell.

Some examples of Properties would include Address, Font, HasFormula, Interior.Color. All these are properties of the active cell that gives you information about that active cell.

For example, you can use this to get the cell address of the active cell or change the interior cell color of the cell.

Now let’s have a few simple VBA code examples that you can use in your day-to-day work when working with active cell in excel

### Making a Cell the Active Cell

To make any cell the active cell, you first have to make sure that it is selected.

If you only have one single cell selected, it by default becomes the active cell.

Below is the VBA code to make cell B5 the active cell:

Sub Change\_ActiveCell()
Range("B5").Activate
End Sub

In the above VBA code, I have first specified the cell address of the cell that I want to activate (which is B5), and then I use the activate method to make it the active cell.

When you only want to make one single cell the active cell, you can also use the select method (code below):

Sub Change\_ActiveCell()
Range("B5").Select
End Sub

As I mentioned earlier, you can only have one active cell even if you have a range of cell selected.

With VBA, you can first select a range of cells, and then make any one of those cells the active cell.

Below the VBA code that would first select range A1:B10, and then make cell A5 the active cell:

Sub Select\_ActiveCell()
Range("A1:B10").Select
Range("A5").Activate
End Sub

### Clear the Active Cell

Below is the VBA code that would first make cell A5 the active cell, and then clear its content (cell content as well any formatting applied to the cell).

Sub Clear\_ActiveCell()
Range("A5").Activate
ActiveCell.Clear
End Sub

Note that I have shown you the above code just to show you how the clear method work with active cell. In VBA, you don’t need to always select or activate the cell to perform any method on it.

For example, you can also clear the content of cell A5 using the below code:

Sub Clear\_CellB5()  
Range("A5").Clear  
End Sub

### Get the Value from the Active Cell

Below the VBA code that could show you a [message box](https://trumpexcel.com/vba-msgbox/)
 displaying the value in the active cell:

Sub Show\_ActiveCell\_Value()  
MsgBox ActiveCell.Value  
End Sub

Similarly, you can also use a simple VBA code to show the cell address of the active cell (code below):

Sub Show\_ActiveCell\_Address()
MsgBox ActiveCell.Address
End Sub

The above code would show the address in absolute reference (such as $A$5).

![Showing the cell address of the active cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20461%20378'%3E%3C/svg%3E)

### Formating the Active Cell (Color, Border)

Below the VBA code that would make the active cell blue in color and change the font color to white.

Sub Format\_ActiveCell()
_'Makes the active cell blue in color_
ActiveCell.Interior.Color = vbBlue

_'Changes the cell font color to white_
ActiveCell.Font.Color = vbWhite

End Sub

Note that I have used the inbuilt [color constant](https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/color-constants?f1url=%3FappId%3DDev11IDEF1%26l%3Den-US%26k%3Dk(vblr6.chm1106125)%3Bk(TargetFrameworkMoniker-Office.Version%3Dv16)%26rd%3Dtrue)
 (vbBlue and vbWhite). You can also use the [RGB constant](https://docs.microsoft.com/en-us/office/vba/language/reference/user-interface-help/rgb-function)
. For example, instead of vbRed, you can use RGB(255, 0, 0)

### Offsetting From the Active Cell

VBA in Excel allows you to refer to cells relative to the position of the active cell (this is called offsetting).

For example, if my active cell is cell A1, I can use the offset property on the active cell and refer to the cell below it by specifying the position of that row corresponding to the active cell.

Let me show you an example.

Sub Offset\_From\_ActiveCell()

_'Make cell A1 the Active Cell_
Range("A1").Activate

_'Goes One cell Below the Actice Cell and Enters the text Test in it_
ActiveCell.Offset(1, 0).Value = "Test"

End Sub

The above code first activate cell A1 and makes it the active cell. It then uses the offset property on the active cell, to refer to the cell which is one row below it.

And in the same line in the code, I have also assigned a value “Test” to that cell which is one row below the active cell.

Let me show you another example where offsetting from the active cell could be used in a practical scenario.

Below I have a VBA code that first activates cell A1, and then uses the offset property to cover 10 cells below the active cell and enter numbers from 1 to 10 in cell A1:A10.

Sub Offset\_From\_ActiveCell()

_'Activates cell A1_
Range("A1").Activate

_'Loop to go through 10 cells below the active cell and enter sequential numbers in it_
For i = 1 To 10
    ActiveCell.Offset(i - 1, 0).Value = i
Next i

End Sub

The above code uses a For Next loop that runs 10 times (and each time the value of the variable ‘i’ increases by 1). And since I am also using ‘i’ in the offset property, it keeps going one cell down with each iteration.

### Get ActiveCell Row or Column Number

Below the VBA code that will show you the row number of the active cell in message box:

Sub ActiveCell\_RowNumber()
MsgBox ActiveCell.Row
End Sub

And the below code will show you the column number in a message box:

Sub ActiveCell\_ColumnNumber()  
MsgBox ActiveCell.Column  
End Sub

### Assign Active Cell Value to a Variable

You can also use VBA to assign the active cell to a variable. Once this is done, you can use this variable instead of the active cell in your code.

And how does this help? Good Question!

When you assign the active cell to a variable, you can continue to use this variable instead of the active cell. The benefit here is that unlike the active cell (which can change when other sheets or workbooks are activated) your variable would continue to refer to the original active cell it was assigned to.

So if you are writing a VBA code that cycles through each worksheet and activates these worksheets, while your active cell would change as new sheets are activated, the variable to which you assigned the active cell initially wouldn’t change.

Below is an example code that defines a variable ‘varcell’ and assigns the active cell to this variable.

Sub Assign\_ActiveCell()
Dim varcell As Range
Set varcell = ActiveCell
MsgBox varcell.Value
End Sub

### Select a Range of Cells Starting from the Active Cell

And the final thing I want to show you about using active cell in Excel VBA is to select an entire range of cells starting from the active cell.

A practical use case of this could be when you want to quickly format a set of cells in every sheet in your workbook.

Below is the VBA code that would select cells in 10 rows and 10 columns starting from the active cell:

Sub Select\_from\_Activecell()  
Range(ActiveCell, ActiveCell.Offset(10, 10)).Select  
End Sub

When we specify two cell references inside the Range property, VBA refers to the entire range covered between there two references.

For example, Range(Range(“A1”), Range(“A10”)).Select would select cell A1:A10.

Similarly, I have used it with active cell, Where the first reference is the active cell itself, and the second reference offsets the active cell by 10 rows and 10 columns.

I hope this tutorial has been useful for you in understanding how active cell works in Excel VBA.

**Other Excel tutorials you may also find useful:**

*   [Highlight the Active Row and Column in a Data Range in Excel](https://trumpexcel.com/highlight-active-row-column-excel/)
    
*   [24 Useful Excel Macro Examples for VBA Beginners (Ready-to-use)](https://trumpexcel.com/excel-macro-examples/)
    
*   [How to Filter Cells with Bold Font Formatting in Excel (An Easy Guide)](https://trumpexcel.com/filter-bold-font-formatting-in-excel/)
    
*   [How to Delete Entire Row in Excel Using VBA](https://trumpexcel.com/vba-delete-row-excel/)
    
*   [Copy and Paste Multiple Cells in Excel (Adjacent & Non-Adjacent)](https://trumpexcel.com/copy-paste-multiple-cells-excel/)
    
*   [Working with Worksheets using Excel VBA (Explained with Examples)](https://trumpexcel.com/vba-worksheets/)
    
*   [Using Workbook Object in Excel VBA (Open, Close, Save, Set)](https://trumpexcel.com/vba-workbook/)
    
*   [Excel VBA Events – An Easy (and Complete) Guide](https://trumpexcel.com/vba-events/)
    
*   [How to Edit Cells in Excel? (Shortcuts)](https://trumpexcel.com/edit-cells-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “Using Active Cell in VBA in Excel (Examples)”
-----------------------------------------------------------

1.  Dear Sumit,  
    Thank you very much for your clear explanations on concepts in VBA.  
    For the first time I understood in no time how object in VBA work!!  
    Just data retrieval through Properties and data setting through Methods.  
    I am always completely confused by Microsof’s “explanations” without to-the-point non-complex examples.  
    Best regards, Tim
    
    [Reply](https://trumpexcel.com/active-cell-vba-excel/#comment-33376)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/active-cell-vba-excel/#respond)

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