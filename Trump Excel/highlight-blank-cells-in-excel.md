# Highlight Blank Cells in Excel (in less than 10 seconds)

**Source:** https://trumpexcel.com/highlight-blank-cells-in-excel

---

[Skip to content](https://trumpexcel.com/highlight-blank-cells-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/highlight-blank-cells-in-excel/#below-title)

**Watch Video – How to Highlight Blank Cells in Excel**

When I get a data file from a client/colleague or I download it from a database, I do some basic checks on the data. I do this to make sure there are no missing data points, errors or duplicates that may lead to issues later.

One such check is to find and highlight blank cells in Excel.

There are many reasons that can result in blank cells in a dataset:

*   The data is not available.
*   Data points accidentally got deleted.
*   A formula returns an empty string resulting in a blank cell.

While it’s easy to spot these blank cells in a small dataset, if you have a huge one with hundreds of rows and columns, doing this manually would be highly inefficient and error prone.

In this tutorial, I will show you various ways to find and highlight blank cells in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/highlight-blank-cells-in-excel/#)

Highlight Blank Cells Using Conditional Formatting
--------------------------------------------------

[Conditional Formatting](https://trumpexcel.com/excel-conditional-formatting/)
 is a great way to highlight cells based on its value when the given condition is met.

_I am going to showcase these examples with a small dataset. However, you can use these same techniques with large datasets as well._

Suppose you have a dataset as shown below:

![Highlight Blank Cells in Excel - Dataset](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20444%20231'%3E%3C/svg%3E)

You can see there are blank cells in this dataset.

Here are the steps to highlight blank cells in Excel (using conditional formatting):

*   Select the data.![Highlight Blank Cells in Excel - select data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%20233'%3E%3C/svg%3E)
*   Go to the Home tab.![Highlight Blank Cells in Excel - Home](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20371%20126'%3E%3C/svg%3E)
*   In the Conditional Formatting drop down, click on New Rule.![Highlight Blank Cells in Excel - New Rule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20195%20374'%3E%3C/svg%3E)
*   In the ‘New Formatting Rules’ dialog box, select ‘Format only cells that contain’.![Highlight Blank Cells in Excel - New formatting rule](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20639%20366'%3E%3C/svg%3E)
*   Select ‘Blanks’ from the drop down (as shown below):![Highlight Blank Cells in Excel - CF Blanks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20639%20366'%3E%3C/svg%3E)
*   Specify the formatting (in which you want to highlight blanks).![Highlight Blank Cells in Excel - format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20366'%3E%3C/svg%3E)
*   Click OK.![Highlight Blank Cells in Excel - OK](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%20366'%3E%3C/svg%3E)

This would highlight all the blank cells in the dataset.

![Highlight Blank Cells in Excel - highlighted](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20445%20231'%3E%3C/svg%3E)

Note that conditional formatting is dynamic. This means that if conditional formatting is applied and you delete a data point, that cell would get highlighted automatically.

At the same time, this dynamic behavior comes with an overhead cost. Conditional Formatting is volatile, and if used on large data sets, may [slow down your workbook](https://trumpexcel.com/suffering-from-slow-excel-spreadsheets/)
.

Also read: [Delete Blank Columns in Excel](https://trumpexcel.com/delete-blank-columns-excel/)

Select and Highlight Blank Cells in Excel
-----------------------------------------

If you want to quickly select and highlight cells that are blank, you can use the ‘Go to Special’ technique.

Here are the steps to select and highlight blank cells in Excel:

*    Select the data.
*   Press the F5 key. It will open the Go To dialog box.
*   In the Go To dialog box, click on the Special button.![Highlight Blank Cells in Excel - special](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20283%20269'%3E%3C/svg%3E)
*   In the Go To Special dialog box, select Blanks.![Highlight Blank Cells in Excel - GTS blanks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20314%20330'%3E%3C/svg%3E)
*   Click OK. This will select all the blank cells in the dataset.![Highlight Blank Cells in Excel - GTS OK](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20314%20330'%3E%3C/svg%3E)
*   With all the blank cells selected, highlight these by giving it a cell color.

As mentioned, this method is useful when you want to quickly select all the blank cells and highlight it.

You can also use the same steps to select all the blank cells and then fill 0 or NA or any other relevant text in it.

Note that, unlike conditional formatting, this method is not dynamic. If you do it once and then by mistake delete a data point, it will not get highlighted.

Also read: [Highlight Cells With Formulas in Excel](https://trumpexcel.com/highlight-cells-with-formulas-excel/)

Using VBA to Highlight Blank Cells in Excel
-------------------------------------------

You can also use a short VBA code to highlight blank cells in a selected dataset.

This method is more suitable when you need to often find and highlight blank cells in data sets. You can easily use the code below and [create an add-in](https://trumpexcel.com/excel-add-in/)
 or save it in your [personal macro workbook](https://support.office.com/en-us/article/Copy-your-macros-to-a-Personal-Macro-Workbook-aa439b90-f836-4381-97f0-6e4c3f5ee566)
.

Here is the VBA code that will highlight blank cells in the selected dataset:

'Code by Sumit Bansal (https://trumpexcel.com)
Sub HighlightBlankCells()
Dim Dataset As Range
Set Dataset = Selection
Dataset.SpecialCells(xlCellTypeBlanks).Interior.Color = vbRed
End Sub

Here are the steps to put this VBA code in the backend and then use it to highlight blank cells in Excel:

*   Go to the Developer tab and click on Visual Basic (or press ALT + F11).![Highlight Blank Cells in Excel - VB](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20610%20127'%3E%3C/svg%3E)
*   In the Vb Editor, within the Project Explorer, right-click on any of the sheet names (if you don’t see Project Explorer, press CONTROL + R).
*   Go to Insert and click on Module.![Highlight Blank Cells in Excel - module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20415%20422'%3E%3C/svg%3E)
*   In the Module code window, copy and paste the VBA code.![Highlight Blank Cells in Excel - code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20836%20269'%3E%3C/svg%3E)
*   Close the VB Editor.

### **How to Run the VBA code (Macro)?**

Once you have copy pasted this macro, there are a couple of ways you can use this macro.

**Using the Macro Dialog Box**

Here are the steps to run this macro using the Macro dialog box:

1.  Select the data.
2.  Go to the [Developer tab](https://trumpexcel.com/excel-developer-tab/)
     and click on Macros.![Highlight Blank Cells in Excel - run - macros](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20609%20127'%3E%3C/svg%3E)
3.  In the Macro dialog box, select the ‘HighlightBlankCells’ macro and click on Run.![Macro dialog box to run macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20363'%3E%3C/svg%3E)

**Using the VB Editor**

Here are the steps to run this macro using the VB Editor:

1.  Select the data.
2.  Go to the Developer tab and click on Visual Basic.![Highlight Blank Cells in Excel - Visual Basic](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20608%20126'%3E%3C/svg%3E)
3.  In the VB Editor, click anywhere within the code.
4.  Click on the Green triangle button in the toolbar (or hit the F5 key).![Highlight Blank Cells in Excel - play button](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20337%2069'%3E%3C/svg%3E)

As I mentioned, using VBA macro to highlight blank cells is the way to go if you need to do this often.

Apart from the ways shown above to run the macro, you can also create an add-in or save the code in the [Personal macro workbook](https://trumpexcel.com/personal-macro-workbook/)
.

This will allow you to access this code from any workbook in your system.

**You May Also Like the Following Excel Tutorials:**

*   [How to Find External Links and References in Excel](https://trumpexcel.com/find-external-links-excel/)
    .
*   [How to Quickly Find and Remove Hyperlinks in Excel](https://trumpexcel.com/find-hyperlinks-in-excel/)
    .
*   [Highlight EVERY Other ROW in Excel](https://trumpexcel.com/highlight-every-other-row-excel/)
    .
*   [The Ultimate Guide to Find and Remove Duplicates in Excel](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
    .
*   [Using InStr Function in Excel VBA](https://trumpexcel.com/excel-vba-instr/)
    .
*   [How to Filter Cells with Bold Font Formatting in Excel.](https://trumpexcel.com/filter-bold-font-formatting-in-excel/)
    
*   [How to Compare Two Columns in Excel.](https://trumpexcel.com/compare-two-columns/)
    
*   [VBA Check IF Cell is Empty (ISEMPTY Function)](https://trumpexcel.com/excel-vba/check-if-cell-empty/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

4 thoughts on “How to Highlight Blank Cells in Excel”
-----------------------------------------------------

1.  found my answer! thank you for the detailed instructions!
    
    [Reply](https://trumpexcel.com/highlight-blank-cells-in-excel/#comment-12097)
    
2.  VBA. How about if that is not a range but a table?
    
    [Reply](https://trumpexcel.com/highlight-blank-cells-in-excel/#comment-10766)
    
3.  It makes no sense to me that the rule “only cells containing blanks” does not include cells like “fast secure”. There is a blank in that cell!  
    Anyway, great guide. I would not have tried this solution without your guide.
    
    [Reply](https://trumpexcel.com/highlight-blank-cells-in-excel/#comment-10460)
    
4.  Wonderful. Thank you.
    
    [Reply](https://trumpexcel.com/highlight-blank-cells-in-excel/#comment-9204)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/highlight-blank-cells-in-excel/#respond)

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