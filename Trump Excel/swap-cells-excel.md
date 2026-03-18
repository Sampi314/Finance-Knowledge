# How to Swap Cells in Excel?

**Source:** https://trumpexcel.com/swap-cells-excel

---

[Skip to content](https://trumpexcel.com/swap-cells-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/swap-cells-excel/#below-title)

Sometimes, when you’re organizing data, creating charts, or analyzing information, you may need to swap two cells (i.e., change the position of two cells).

![Swap cells in Excel](https://trumpexcel.com/wp-content/uploads/2023/09/Swap-cells-in-Excel.png)

While there is no built-in feature in Excel to swap cells, this can easily be done using a simple mouse drag-and-drop technique or the old and traditional Cut-Paste method.

In this short article, I will show you how to swap cells in Excel using some simple shortcuts and a VBA code.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/swap-cells-excel/#)

Using Mouse + Shift Key to Swap Cells
-------------------------------------

The easiest and fastest way to quickly swap two cells is by using this Mouse and Shift key technique.

This works best when you want to swap to adjacent cells or columns, but it can also be used for swapping non-adjacent cells or columns.

Below, I have the sample data set where I have the trainer’s name in column B, and the day they need to deliver the training in column A.

![Dataset to swap cells in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20360%20305'%3E%3C/svg%3E)

Now, for some reason, Mike is unable to take the training on Tuesday and wants to switch his slot with Jenny on Wednesday.

Below are the steps you can use to quickly swap the two cells so that the names are interchanged in cells B3 and B4:

1.  Select one of the cells that you want to swap. In this case, I would select cell B3, which has the name Mike.
2.  Bring the cursor to the bottom edge of the selection. You will notice that the cursor changes into a four-arrow icon (see the image below).

![Cursor changes when placed at bottom edge of selection](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20362%20305'%3E%3C/svg%3E)

3.  Hold the Shift key (and keep holding it)
4.  Press and hold the right mouse key (or keypad key if using a trackpad on a laptop)
5.  Move the mouse cursor down till you see a thick green line (it looks like an elongated H) below the cell B4 (which is the cell with which I want to swap my currently selected cell)

![Move the cell down while holding shift key](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20365%20313'%3E%3C/svg%3E)

6.  Leave the mouse key and the Shift key.

Voila! Magic amigo!

You can see the entire process in action below:

![Swap two cells in Excel demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20394%20330'%3E%3C/svg%3E)

The two cells have been swapped. Mike is now in front of Wednesday, and Jenny is now in front of Tuesday.

This is the simplest and the fastest way to quickly swap cells or even rows and columns. The only thing you need to ensure is that the thick green line appears after the cell where you want to move your current cell.

**Note**: This method moves the entire cell and not just the value in the cell. So when you swap two cells, it would also swap the cell formatting as well as any formula in that cell.

Also read: [Flip Data in Excel | Reverse Order of Data in Column/Row](https://trumpexcel.com/flip-data-in-excel/)

### Swapping Non-Adjacent Cells

In this above example, I’ve shown you how to swap two contiguous cells.

You can also use this to swap to nonadjacent cells. However, you would have to repeat this process twice.

For example, suppose I have the same data set as shown below, and I want to sort the days for Mike and Kate.

![Dataset to swap cells in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20360%20305'%3E%3C/svg%3E)

In this case, I will first have to move the cell B3 (Mike) to B5 (Kate). This will move Mike into Kate’s place and move Jenny and Kate’s cell above.

Now, I will have to select cell B4 (which has the name Kate) and move it to cell B3.

![Swapping non adjacent cells using shift](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20386%20338'%3E%3C/svg%3E)

**Note**: While I have shown you an example where I’m swapping the cells in a column, you can also do this for swapping the cells in a row. You can use this method to swap entire rows or columns.

Also read: [Convert Columns to Rows in Excel](https://trumpexcel.com/convert-columns-to-rows-excel/)

Using Old and Dependable Cut and Paste
--------------------------------------

Another way to swap cells would be to use the longer but dependable cut-and-paste option.

In this method, the process remains the same whether you swap adjacent or non-adjacent cells.

Let me show you how it works:

Below, I have the data set where I want to swap the cells that have the names Mike and Jenny.

![Dataset to swap cells in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20360%20305'%3E%3C/svg%3E)

Here are the steps to swap the two cells using the cut-paste method.

1.  Select one of the cells you want to swap. In this case, I will select the cell B3.
2.  Cut the cell. You can use the shortcut Control + X in Windows or Command + X in Mac. You can also right-click on the cell and then click on Cut.
3.  Go to any blank cells in the worksheet, select it, and paste the cell you cut in Step 2. You can use Control + V to do this (or Command + V in Mac). In this example, I will do this in cell D5.

![Cut the cell and put it in temporary cell in worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20627%20310'%3E%3C/svg%3E)

4.  Now select cell B4 and cut it (Control + X). You will see dancing ants around the cell when you cut it.

![Cut cell B4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20620%20305'%3E%3C/svg%3E)

5.  Now select cell B3 and paste this cell you cut in Step 4. You can do this using Control + V

![Paste it in B3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20618%20308'%3E%3C/svg%3E)

6.  Now, select cell D5 (where we paste cell B3 in Step 3), and cut it using Control + X

![Cut the temp cell with name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20620%20307'%3E%3C/svg%3E)

7.  Paste this on cell B4.

![Paste it in B4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20366%20311'%3E%3C/svg%3E)

While this may look like a long process with a lot of steps, it’s not that hard once you get the process.

**Note**: While I have shown how to use this method to swap two cells only, you can use this to swap multiple cells and even rows and columns.

Also read: [How to Copy Column Widths in Excel (Shortcut)](https://trumpexcel.com/copy-column-width-excel/)

Using VBA (to Swap non-adjacent cells)
--------------------------------------

You can also use a simple VBA code swap two cells.

Since VBA takes some setting up, this method would only make sense when you have to do this for many different sheets, or you need to do this often so you can create the code once and then reuse it multiple times.

Below is the VBA code that would swap

    'Code developed by Sumit Bansal from https://trumpexcel.com
    Sub SwapCells()
    Dim temp As Variant
    Dim Cell1 As Range
    Dim Cell2 As Range
        
    'Define the cell ranges
    Set Cell1 = Range("B3")
    Set Cell2 = Range("B4")
        
    'Swap values using a temporary variable
    temp = Cell1.Value
    Cell1.Value = Cell2.Value
    Cell2.Value = temp
    
    End Sub

The above creates a temporary location (using the temp variable) and stores the values of the first cell in this location. It then copies the second cell over the first one and then uses the value in the temp variable to paste in the second cell.

The VBA code follows the same logic as the one in the second method I covered in this article (using Cut Paste).

**Note**: One limitation of this VBA code is that it will only swap the values in the cell and not the formatting. While you can create a code to swap the value as well as the formatting since you cannot hold the formatting value in a temporary cell, it would need to be a lot more elaborate code that uses an actual cell in the worksheet to first hold the formatting and then copy it back to the original cells.

### Where to Put this VBA Code?

You will have to put this code in the [Visual Basic editor](https://trumpexcel.com/visual-basic-editor/)
, which is the programming back end of Excel.

Follow the below steps to do this:

1.  Hold the ALT key and then press the F11 key. This will open the VB editor. You can also click on the Developer tab and then click on the Visual Basic icon.

![Click on the visual basic icon in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20196'%3E%3C/svg%3E)

2.  In the VB editor that opens, click on the Insert option in the menu and then click on Module. This will insert a new module where we are going to copy and paste the above VBA code.

![Insert a module for the workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20346%20244'%3E%3C/svg%3E)

3.  Copy and Paste the above VBA code into the module code window.

![Copy paste the VBA code in the module code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20720%20337'%3E%3C/svg%3E)

4.  Save the code using Control + S (or click the save icon in the toolbar).

![Save the code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20515%20186'%3E%3C/svg%3E)

Now that the code is in the VB editor, you can run it to shop the specified cells in the code.

### How to Run this Code?

To run the VBA macro code, follow the steps below:

1.  Hold the ALT key and then press the F8 key. This will open the Macro dialog box. Alternatively, you can also click on the Developer tab in the ribbon and then click on the Macro icon
2.  Select the name of the macro that you want to run.
3.  Click on the Run button.

![Click on the run button in the macro dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20551%20470'%3E%3C/svg%3E)

If you want to learn about some other ways to run a macro, [click here to read the detailed article](https://trumpexcel.com/run-a-macro-excel/)
.

Here are a few important things to remember when using VBA macro codes in Excel:

*   If you want to reuse the macro code, you will have to save that file as a macro-enabled file (that has the .XLSM file extension)
*   Changes done by VBA macro scripts are irreversible, so make sure you have a backup copy of your data in case you need it in the future.

So, these are some of the methods you can use to quickly swap cells in Excel.

The easiest and fastest method would be to use the Shift + Mouse technique. You can also use the old and traditional cu-copy-paste method, which works for both adjacent and non-adjacent cells.

And if you prefer VBA to do this, then you can use the code I provided in this article.

I hope you found this Excel tutorial useful.

**Other Excel articles you may also find useful:**

*   [Keyboard & Mouse Tricks that will Reinvent the Way You Excel](https://trumpexcel.com/keyboard-mouse-tricks/)
    
*   [How to Lock Row Height & Column Width in Excel](https://trumpexcel.com/lock-row-height-column-width-excel/)
    
*   [How to Move Rows and Columns in Excel](https://trumpexcel.com/move-rows-columns/)
    
*   [How to Select Non-adjacent cells in Excel?](https://trumpexcel.com/select-non-adjacent-cells-in-excel/)
    
*   [Copy Visible Cells Only in Excel](https://trumpexcel.com/copy-visible-cells/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/swap-cells-excel/#respond)

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