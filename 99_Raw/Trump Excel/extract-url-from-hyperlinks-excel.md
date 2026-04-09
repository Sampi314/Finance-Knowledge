# Extract URL from Hyperlinks in Excel (3 Easy Ways)

**Source:** https://trumpexcel.com/extract-url-from-hyperlinks-excel

---

[Skip to content](https://trumpexcel.com/extract-url-from-hyperlinks-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/extract-url-from-hyperlinks-excel/#below-title)

Many of my projects involve working with data from the web, where I get hyperlinks in cells in Excel when I copy the data from other sources.

Something as shown below ([source](https://en.wikipedia.org/wiki/List_of_public_corporations_by_market_capitalization)
):

![Dataset to extract urls from hyperlinks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20508%20308'%3E%3C/svg%3E)

One of the first things I often have to do is extract the URLs from these hyperlinks so that I can do my analysis on these extracted URLs.

And how do you extract URLs from hyperlinks in Excel?

While this can be done manually if you only have a few hyperlinked cells, with a longer list, this is better done using VBA.

In this article, I will show you how to **extract URLs from hyperlinks** using manual methods, as well as automate this process using VBA when you can extract URLs in bulk.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/extract-url-from-hyperlinks-excel/#)

Manually Extracting URLs from Hyperlinks
----------------------------------------

If you only have a [couple of hyperlinks](https://trumpexcel.com/hyperlinks/)
 from which you want to extract the URLs, it’s best to do it manually.

Below, I have a data set where I have hyperlinks in column A, and I want to extract the URLs from each cell in column B:

![Dataset to extract urls from hyperlinks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20508%20308'%3E%3C/svg%3E)

Here are the steps to extract URLs from hyperlinks manually:

1.  Right-click on the cell that has the hyperlink.
2.  In the options that show up, click on the ‘Edit Hyperlink’ option. This will open the Edit Hyperlink dialog box.

![Click on Edit Hyperlinks option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20511%20663'%3E%3C/svg%3E)

3.  Copy the URL listed in the Address field (select the URL and use Control + C)

![Copy the hyperlink in Edit Hyperlink box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20912%20423'%3E%3C/svg%3E)

4.  Close the dialog box.
5.  Go to the cell where you want the URL and paste it there.
6.  Repeat Steps 1-5 for all the cells from which you want to extract the hyperlinks.

**Pro Tip**: You can also open the edit hyperlink dialog box by using the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
 **Control + K** (where you need to hold the Control key and then press the K key)

Since this is a manual process where you need to extract URLs from each cell one by one, this is best suited when you only have a few cells to tackle.

In case you have a large list of hyperlinks from which you want to extract the URLs, it would be better to use the VBA methods covered next.

Also read: [Remove Hyperlinks from a Worksheet in Excel](https://trumpexcel.com/remove-hyperlinks/)

VBA Code to Extract URLs from Hyperlinks
----------------------------------------

If you have many hyperlinked cells from which you want to extract the URLs or need to do this quite often, it’s better to [create a VBA code](https://trumpexcel.com/excel-vba/)
 that can be reused for this purpose.

Let’s take an example of the data set below, where I have hyperlinked cells in column A, and I want to extract the URLs from these cells in column B.

![Dataset to extract urls from hyperlinks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20508%20308'%3E%3C/svg%3E)

Below is the VBA code that would do this.

    Sub ExtractURLs()
    
        ' Declares a variable for the Hyperlink object
        Dim HypLnk As Hyperlink
    
        ' Loops through each hyperlink and extract URL in adjacent cell
        For Each HypLnk In Selection.Hyperlinks
            HypLnk.Range.Offset(0, 1).Value = HypLnk.Address
        Next HypLnk
    
    End Sub

To use this above code, you need to first select the cells that have the hyperlinks and then [run the macro code](https://trumpexcel.com/run-a-macro-excel/)
.

It works by [looping through each cell](https://trumpexcel.com/vba-loops/)
 in the selected range and extracting the URL in the adjacent cell.

Here are the steps to use this VBA code in Excel:

1.  Use the shortcut ALT + F11 to open the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
    . Alternatively, you can also [click on the developer tab](https://trumpexcel.com/excel-developer-tab/)
     and then click on the Visual Basic icon to open the VB editor.
2.  In the VB editor, click on the _Insert_ option in the menu and then click on _Modules_. This will insert a new module for that workbook.

![Insert a new module for the workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20343%20247'%3E%3C/svg%3E)

3.  Copy and paste the above VBA code into the module code window.

![Copy paste the code in module to extract url from hyperlinks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20241'%3E%3C/svg%3E)

4.  Place the cursor anywhere in the code and press the F5 key on your keyboard to run the VBA code (or click on the play icon in the toolbar).

![Run the code to extract url from hyperlinks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20513%20118'%3E%3C/svg%3E)

The above steps would run the VBA code, which would extract all the URLs from all the hyperlinks in the selected cells into the adjacent column on the right.

Below, I have a variation of the same code, which would ask the user to select a range (using an input box) and then extract the URLs in the adjacent column.

    Sub ExtractURLs()
    
        ' Declares variables for range and hyperlink objects
        Dim rng As Range
        Dim HypLnk As Hyperlink
    
        ' Prompts the user to select a range
        On Error Resume Next
        Set rng = Application.InputBox("Please select a range:", "Select Range", Type:=8)
        On Error GoTo 0
    
       ' Loops through each hyperlink and extract in adjacent cell
        If Not rng Is Nothing Then
            For Each HypLnk In rng.Hyperlinks
                HypLnk.Range.Offset(0, 1).Value = HypLnk.Address
            Next HypLnk
        Else
            MsgBox "No valid range selected.", vbExclamation
        End If
    
    End Sub

Here are a couple of important things to know when using a VBA code in Excel:

*   If you want to reuse this code in the same workbook again, you need to save the workbook as a macro-enabled file (with .XLSM extension)
*   If you want to use this VBA code in all of your Excel workbooks on your system, you can save this code in your [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
    . Once saved in your Personal Macro Workbook, it can be run in any workbook on your system.
*   You can also add the macro icon to your [Quick Access Toolbar](https://trumpexcel.com/excel-quick-access-toolbar-options/)
     and then run the macro by clicking on that icon in the QAT.

Also read: [Find Hyperlinks in Excel (using Find and Replace)](https://trumpexcel.com/find-hyperlinks-in-excel/)

Function (UDF) to Extract URLs from Hyperlinks
----------------------------------------------

Another useful way to extract URLs from hyperlinks is by creating a [custom User Defined Function (UDF) using VBA](https://trumpexcel.com/user-defined-function-vba/)
 and then using that function in the worksheet to extract the URLs.

Below is the VBA code to create a function called ExtractURL, which can be used in the worksheet. It takes the cell reference of the cell that has the hyperlink as input and gives the URL as the result of the formula.

    Function ExtractURL(rng As Range) As String
    
        ' Checks if the first cell in the specified range contains hyperlink
        If rng(1).Hyperlinks.Count <> 1 Then
        
            ' If not, returns an empty string
            ExtractURL = ""
        
        Else
            
            ' If there is a hyperlink, returns its URL
            ExtractURL = rng.Hyperlinks(1).Address
        
        End If
    
    End Function

Let me show you how to create and use this custom function in Excel to extract URLs from hyperlinks.

Below is the dataset where I have hyperlinks in column A, and I want to extract the URLs in column B.

![Dataset to extract urls from hyperlinks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20508%20308'%3E%3C/svg%3E)

Here are the steps to do this with a VBA UDF function:

1.  Use the shortcut ALT + F11 to open the VB Editor.
2.  In the VB editor, click on the Insert option in the menu and then click on Modules. This will insert a new module for that workbook.

![Insert a new module for the workbook](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20343%20247'%3E%3C/svg%3E)

3.  Copy and paste the above function VBA code into the module code window.

![Copy paste the UDF function code in module to extract url from hyperlinks](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20284'%3E%3C/svg%3E)

4.  Go back to the worksheet and enter the below formula in cell B2:

\=ExtractURL(A2)

Copy and paste the formula and cell B2 for all the other cells in the column.

![Using the VBA custom function in worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20638%20359'%3E%3C/svg%3E)

Since I created the function _ExtractURL_ in VBA, I wasable to use it as a regular worksheet function in the cells.

When you use this formula, it goes back to its code in VBA and follows the steps to give you the URL as the result. In case the cell is blank or it does not have a hyperlink, it returns blank (“”).

Here are a couple of things to know when using the custom User Defined VBA function in Excel:

*   If you want to reuse this formula in the same workbook again, you need to save the workbook as a macro-enabled file (.XLSM extension)
*   If you remove the VBA code of the formula from the VB Editor, it will give you an error in the worksheet. So, if you plan to not have the VBA code in the back end, you should [convert the formula result into static values](https://trumpexcel.com/convert-formulas-to-values-excel/)
    .
*   If you want to use this function in all of your Excel workbooks on your system, you can save this code in your [Personal Macro Workbook](https://trumpexcel.com/personal-macro-workbook/)
    .
*   If you share the Excel file with the UDF code with someone and they don’t enable macros, they will see an error instead of the formula result.

These are some methods you can use to quickly extract URLs from Hyperlinks in Excel.

If you only have a couple of cells with hyperlinks, you can do this manually using the edit hyperlink dialog box.

In case you have a lot of cells with hyperlinks, or you need to do this quite often, you can use the VBA code method I covered or create your own Custom function, as I showed.

I hope he found this exact tutorial useful. If you have any comments or feedback, do let me know in the comments section.

**Other Excel articles you may also like:**

*   [How to Find External Links and References in Excel](https://trumpexcel.com/find-external-links-excel/)
    
*   [Create Dynamic Hyperlinks in Excel](https://trumpexcel.com/create-dynamic-hyperlinks-in-excel/)
    
*   [Send Email From Excel Using Hyperlink Function + BONUS Email Generator Tool](https://trumpexcel.com/send-email-from-excel-hyperlink/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/extract-url-from-hyperlinks-excel/#respond)

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