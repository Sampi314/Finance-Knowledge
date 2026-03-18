# How to Add Parentheses Around Text in Excel (4 Easy Ways)

**Source:** https://trumpexcel.com/add-parentheses-excel

---

[Skip to content](https://trumpexcel.com/add-parentheses-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/add-parentheses-excel/#below-title)

Sometimes, when working with text data in Excel, you may want to add parentheses around the text in a cell or range of cells.

For example, below, I have a data set with the region name in column A, and I want to put these names in parentheses or brackets.

![Data set where I want to add Parentheses around text in Excel](https://trumpexcel.com/wp-content/uploads/2023/11/Data-set-where-I-want-to-add-Parentheses-around-text-in-Excel.png)

As always, Excel offers multiple ways to do this easily.

In this article, I will show you four different methods you can use to quickly add parentheses around text in a range of cells in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/add-parentheses-excel/#)

Add Parentheses Around Text Using Flash Fill
--------------------------------------------

The fastest way to quickly add parentheses in cells is by using [Flash Fill](https://trumpexcel.com/flash-fill-excel/)
.

Flash Fill works by identifying patterns based on the result that you manually enter in one or two cells and then use it to fill the entire column following the same pattern.

Let me show you how it works.

Below is the data set where I have country names in column A, and I want to add parentheses around these names.

![Data set to add parentheses around text Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%20337'%3E%3C/svg%3E)

Here are the steps to do this using Flash Fill:

1.  In cell B2, manually enter the result that you expect (which would be (US) in this case)

![Enter the expected result in the first cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%20336'%3E%3C/svg%3E)

2.  Now, hold the Control key and press the E key. This is the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     to run Flash Fill, which would fill the entire column based on the pattern that it has identified in cell B2.

![Use flash fill to fill the entire column with the result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20477%20341'%3E%3C/svg%3E)

If you don’t want to remember a new keyboard shortcut, you can also run Flash Fill by going to the Home tab, clicking on the Fill option, and then clicking on Flash Fill.

![Click the flash fill option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20313%20471'%3E%3C/svg%3E)

_Note that the result you get with this method is not dynamic. So, if your original data in the column changes, the result will not automatically update, and you’ll have to use Flash Fill again to get the updated results._

In some cases, it’s possible that Flash Fill may not be able to recognize the pattern correctly. In such cases, you can enter the expected result manually in two or three cells and then try using Flash Fill.

Also read: [Remove Parentheses in Excel](https://trumpexcel.com/remove-parentheses-excel/)

Add Parentheses Around Text Using Formula
-----------------------------------------

You can also use a simple concatenate formula to quickly add parentheses around text in a range of cells.

Below, I have the same data set where I have country names in column A, and I want to get these names within parentheses.

![Data set to add parentheses around text Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%20337'%3E%3C/svg%3E)

Here is the formula that will do this:

\="("&A2&")"

Enter this formula in cell B2, then hit enter, and then copy the formula down for all the cells to get the results.

![Formula to add parentheses around text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20464%20383'%3E%3C/svg%3E)

If your version of Excel has dynamic arrays, then you can also use the following formula (with no need to copy down the formula as it automatically sills and fills the entire range):

\="("&A2:A7&")"

![Dynamic array formula to add parentheses around text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20487%20383'%3E%3C/svg%3E)

One advantage of using this formula method is that your result is dynamic. So, if the original data in column A changes, the result in Column B will automatically update

Add Parentheses Around Text Using Custom Cell Formatting
--------------------------------------------------------

One smart technique to add parentheses around text without changing the actual text in the cell is by using custom cell formatting.

With this method, we change the cell format so that it shows you the parentheses around the cell content, but it doesn’t actually add them to the cell.

Let me show you how it works.

Below is the data set where I have country names in column A, and I want to display these country names within parentheses.

![Data set to add parentheses around text Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%20337'%3E%3C/svg%3E)

Here are the steps to do this using custom cell formatting:

1.  Select the range of cells to which you want to add parentheses
2.  Hold the Control key and then press the 1 key. This will open the Format Cells dialog box. Alternatively, you can also click on the Home tab and then click on the dialog box launcher in the Number group.

![Click on the dialog box launcher in the home tab in number group](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20698%20163'%3E%3C/svg%3E)

3.  In the Number tab, click on the Custom option

![Select the custom option in the number tab in format cells dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20628'%3E%3C/svg%3E)

4.  Enter the following format in the Type field:

"("@")"

![Enter the custom formatting in the type field to add parentheses around text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20628'%3E%3C/svg%3E)

5.  Click ok

As soon as you click ok in step 5, you will notice that an opening and closing parenthesis have been added around the cell content in the selected range.

![Custom formatting added brackets around text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20310%20337'%3E%3C/svg%3E)

But if you select any of these cells, you will notice that in the formula bar, it shows you the cell values without parentheses.

![Formula bar does not show the parentheses](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20383%20389'%3E%3C/svg%3E)

Unlike the other methods covered above, in this method, you do not need an additional column to get the result. Also, if you change the content of any cell to which this format has been applied, it will automatically update and put the new cell content within brackets.

Also read: [Display Negative Numbers in Parentheses](https://trumpexcel.com/show-negative-numbers-parentheses-brackets-excel/)

Add Parentheses Around Text Using VBA
-------------------------------------

If adding parentheses around the text is something you need to do quite often, you can also consider creating a [VBA macro script](https://trumpexcel.com/excel-vba/)
 and adding it to your workbook (or personal macro workbook).

Below is the VBA code that adds an opening and closing parenthesis to the cells in the selected range:

    'Code by Sumit Bansal from trumpexcel.com
    Sub AddParnetheses()
    For Each cell In Selection
    cell.Value = "(" & cell & ")"
    Next cell
    End Sub

The above VBA code uses a [For Each Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 to go through each cell in the selection and add an opening and closing parenthesis around the cell content

Here are the steps to use this macro code:

1.  Press Alt + F11 on your keyboard (or click the [Developer tab](https://trumpexcel.com/excel-developer-tab/)
     and then click on the Visual Basic icon). This will open the Visual Basic for Applications (VBA) editor.

![Click on visual basic option in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20196'%3E%3C/svg%3E)

2.  In the [Visual Basic Editor](https://trumpexcel.com/visual-basic-editor/)
    , click on the Insert option in the menu and then click on Module. This will insert a new module for that workbook.

![Insert module in the VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20456%20324'%3E%3C/svg%3E)

3.  Copy and paste the above VBA code into the Module code window. If the module code window is not open or you have closed it accidentally, double-click on the module object in the Project Explorer, and it will reopen the module code window.

![Copy paste the macro code in the module to add brackets](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20297'%3E%3C/svg%3E)

4.  Now, to run the macro code, Place the cursor anywhere in the code and press the F5 key, or click on the run macro icon in the toolbar.

![Run the macro to add parentheses](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20534%20175'%3E%3C/svg%3E)

5.  Close the VB Editor.

Once you have the code in the workbook, you can reuse it by clicking on the Developer tab, clicking on the Macros button, and then selecting the macro and clicking the Run button.

**Important Note**: Remember that any changes that are done by a vb macro cannot be undone. So, I strongly suggest you create a backup copy of your data set just in case you need the original data set back.

If you want to reuse the macro in the workbook, ensure that you save it as a macro-enabled file (with .XLSM extension). This option appears in the Save As dialog box when saving the file.

So, these are four methods that you can use to quickly add parentheses around text in a cell or range of cells in Excel.

I’ve also created a table below that briefly summarizes each method along with some of the important things you need to know.

| Method | Pros | Cons |
| --- | --- | --- |
| Using Flash Fill | Quick and Easy | The result is static. Flash Fill may recognize a wrong pattern sometimes |
| Using Formula | Result is dynamic, so it updates if you change the original dataset | –   |
| Using Cell Formatting | Parentheses are not actually added (but only displayed in the cell. Result is dynamic. | More complicated than other methods |
| Using VBA | Useful when you need to repeat this often | Needs some setting up |

I hope you found this Excel article helpful. Do let me know your thoughts while leaving a comment below.

**Other Excel articles you may also like:**

*   [Write Fractions in Excel](https://trumpexcel.com/display-numbers-as-fractions-excel/)
    
*   [Remove Negative Signs in Excel](https://trumpexcel.com/change-negative-to-positive-in-excel/)
    
*   [Find and Replace in Excel](https://trumpexcel.com/find-and-replace-in-excel/)
    
*   [CONCATENATE Excel Range with separator](https://trumpexcel.com/concatenate-excel-ranges/)
    
*   [Extract the First Word from a Text String in Excel](https://trumpexcel.com/extract-first-word-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/add-parentheses-excel/#respond)

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