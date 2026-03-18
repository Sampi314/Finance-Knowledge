# Split Each Excel Sheet Into Separate Files (Step-by-Step)

**Source:** https://trumpexcel.com/split-each-excel-sheet-into-separate-files

---

[Skip to content](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#below-title)

**Watch Video – How to Split Each Excel Sheet Into Separate Files**

If you have an Excel workbook with many worksheets, there is no easy way to split each of these sheets into separate Excel files and save separately.

This could be needed when you sheets for different months or regions or products/clients and you want to quickly get a separate workbook for each sheet (as an Excel file or as PDFs).

While there is a manual way to split sheets into separate workbooks and then save it, it’s inefficient and error-prone.

In this tutorial, I will give you a simple [VBA code](https://trumpexcel.com/excel-vba/)
 that you can use to quickly (in a few seconds) split all the worksheets into their own separate files and then save these in any specified folder.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#)

Split Each Worksheet Into a Separate Excel File
-----------------------------------------------

Suppose you have a workbook as shown below where you have a worksheet for each month.

![Excel File with Multiple Sheets for different months](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20493%20188'%3E%3C/svg%3E)

To split these sheets into a separate Excel file, you can use the below VBA code:

'Code Created by Sumit Bansal from trumpexcel.com
Sub SplitEachWorksheet()
Dim FPath As String
FPath = Application.ActiveWorkbook.Path
Application.ScreenUpdating = False
Application.DisplayAlerts = False
For Each ws In ThisWorkbook.Sheets
    ws.Copy
    Application.ActiveWorkbook.SaveAs Filename:=FPath & "\\" & ws.Name & ".xlsx"
    Application.ActiveWorkbook.Close False
Next
Application.DisplayAlerts = True
Application.ScreenUpdating = True
End Sub

There are a few things you need to make sure before using the above VBA code:

1.  Create a folder where you want to get all the resulting files.
2.  Save the main Excel file (which has all the worksheets that you want as separate files) in this folder.

Once you have this done, then you can put the above VBA code in the file and [run the code](https://trumpexcel.com/run-a-macro-excel/)
.

The above code is written in a way that it picks up the location of the folder using the path of the file (in which the code is run). This is why it’s important to save the file in the folder first and then use this code.

**How does the VBA code work** – The above code uses a simple [For Next loop](https://trumpexcel.com/for-next-loop-excel-vba/)
 that goes through each worksheet, creates a copy of the worksheet in an Excel workbook, and then saves this Excel workbook in the specified folder (which is the same that has the main file with all the sheets).

Below are the steps to place this VBA code in the Excel workbook (these will be same for all the other methods shown in this tutorial):

**Where to put this code?**

Below are the steps to place the code in the [Visual Basic Editor](https://trumpexcel.com/visual-basic-editor/)
 where it can be executed:

*   Click the Developer tab.![Click the Developer Tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20748%20198'%3E%3C/svg%3E)
*   In the Code group, click on the Visual Basic option. This will open the VB Editor. \[You can also use the keyboard shortcut – **ALT + F11**\]![Click on Visual Basic to open the VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20748%20198'%3E%3C/svg%3E)
*   In the VB Editor, right-click on any of the objects of the workbook you’re working on.![Right click on any of the object in the Project Explorer](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20495%20364'%3E%3C/svg%3E)
*   Hover the cursor over the Insert option
*   Click on Module. This will insert a new module![Click on Module to insert a new module object](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20489%20519'%3E%3C/svg%3E)
*   Double-click on the Module object. this will open the code window for the module
*   Copy the VBA code provided above and paste it in the module code window.![Copy and Paste the code in the module window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20306'%3E%3C/svg%3E)
*   Select any line in the code and click on the green play button in the toolbar to run the VBA macro code.![Click on the Play button to run the macro](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20373%2088'%3E%3C/svg%3E)

The above steps would instantly split the worksheets into separate Excel files and save these. It takes only a second if you have less number of worksheets. In case you have a lot, it may take some time.

The name of each saved file is the same as that of the sheet name it had in the main file.

![Files after each sheet is split into separate file](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20789%20246'%3E%3C/svg%3E)

Since you have placed a VBA code in the Excel workbook, you need to save this with a .XLSM format (which is the macro-enabled format). This will ensure the macro is saved and works when you open this file next.

Note that I have used the lines _Application.ScreenUpdating = False_ and _Application.DisplayAlerts = False_ in the code so that everything happens in the backend and don’t see things happening on your screen. Once the code runs and split the sheets and saves these, we turn these back to TRUE.

As a best practice, it’s recommended to create a backup copy of the main file (which has the sheets that you want to split). This will ensure you don’t lose your data in case anything goes wrong or if Excel decides to become slow or crash.

Also read: [Inserting Excel Tables Into Word](https://trumpexcel.com/copy-excel-table-to-word/)

Split Each Worksheet and Save as a Separate PDFs
------------------------------------------------

In case you want to split the worksheets and [save these as PDF files](https://trumpexcel.com/convert-excel-to-pdf/)
 instead of the Excel files, you can use the below code:

'Code Created by Sumit Bansal from trumpexcel.com
Sub SplitEachWorksheet()
Dim FPath As String
FPath = Application.ActiveWorkbook.Path
Application.ScreenUpdating = False
Application.DisplayAlerts = False

For Each ws In ThisWorkbook.Sheets
    ws.Copy
    Application.ActiveSheet.ExportAsFixedFormat Type:=xlTypePDF, Filename:=FPath & "\\" & ws.Name & ".xlsx"
    Application.ActiveWorkbook.Close False
Next

Application.DisplayAlerts = True
Application.ScreenUpdating = True
End Sub

Things you need to make sure before using this code:

1.  Create a folder where you want to get all the resulting files.
2.  Save the main Excel file (which has all the worksheets that you want as separate files) in this folder.

The above code splits each sheet in the Excel file and saves it as a PDF in the same folder where you have saved the main Excel file.

Also read: [Insert Pdf Into Excel](https://trumpexcel.com/embed-pdf-file-excel/)

Split Only those Worksheets that Contain a Word/Phrase into Separate Excel Files
--------------------------------------------------------------------------------

In case you have a lot of sheets in a workbook and you only want to split only those sheets that have a specific text in it, you can do that as well.

For example, suppose you have an Excel file where you data for multiple years and each sheet in the file has the year number as the prefix. Something as shown below:

Now, let’s say you want to split all the sheets for 2020 and save these as separate Excel files. To do this, you need to somehow check the name of each worksheet and only those sheets that have the number 2020 should be split and saved, and the rest should be left untouched.

This can be done using the following [VBA macro code](https://trumpexcel.com/excel-macro-examples/)
:

'Code Created by Sumit Bansal from trumpexcel.com
Sub SplitEachWorksheet()
Dim FPath As String
Dim TexttoFind As String
TexttoFind = "2020"
FPath = Application.ActiveWorkbook.Path
Application.ScreenUpdating = False
Application.DisplayAlerts = False

For Each ws In ThisWorkbook.Sheets
    If InStr(1, ws.Name, TexttoFind, vbBinaryCompare) <> 0 Then
        ws.Copy
        Application.ActiveWorkbook.SaveAs Filename:=FPath & "\\" & ws.Name & ".xlsx"
        Application.ActiveWorkbook.Close False
    End If
Next

Application.DisplayAlerts = True
Application.ScreenUpdating = True
End Sub

In the above code, I have used a variable TexttoFind, which has been assigned to “2020” in the beginning.

The VBA code then uses the For Next loop in VBA to go through each worksheet and then check the name of each worksheet [INSTR function](https://trumpexcel.com/excel-vba-instr/)
. This function checks whether the worksheet name has the word 2020 in it or not. If it does, it will return a position number where it finds this text (which is 2020 in this case).

And if it doesn’t find the text we are looking for, it returns 0.

This is used with the [IF Then condition](https://trumpexcel.com/if-then-else-vba/)
. So if a sheet name has the text string 2020 in it, it will be split and saved as a separate file. And if it doesn’t have this text string, the IF condition would not be met and nothing would happen.

**You may also like the following Excel tutorials:**

*   [How to Compare Two Excel Sheets](https://trumpexcel.com/compare-two-excel-sheets/)
    
*   [How to Reduce Excel File Size](https://trumpexcel.com/reduce-excel-file-size/)
    
*   [Combine Data from Multiple Workbooks in Excel](https://trumpexcel.com/combine-data-from-multiple-workbooks/)
    
*   [How to Recover Unsaved Excel Files \[All Options + Precautions\]](https://trumpexcel.com/recover-unsaved-excel-files/)
    
*   [How to Automatically Open Specific Excel File on Startup](https://trumpexcel.com/automatically-open-excel-file-startup/)
    
*   [How to Split Multiple Lines in a Cell into a Separate Cells / Columns](https://trumpexcel.com/split-multiple-lines/)
    
*   [Excel VBA Split Function](https://trumpexcel.com/vba-split-function/)
    
*   [How to Import XML File into Excel | Convert XML to Excel](https://trumpexcel.com/convert-xml-to-excel/)
    
*   [How to Split Screen in Excel (Compare Side-by-Side)](https://trumpexcel.com/excel-split-screen/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

14 thoughts on “Split Each Excel Sheet Into Separate Files”
-----------------------------------------------------------

1.  thank you, big big help 🙂
    
    [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-47450)
    
    *   Glad the article helped.
        
        [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-47452)
        
2.  I am trying to run the split worksheets macro. I have run it before on other computers. When i try to run it on my new computer the macro stops at the  
    ws.Copy  
    portion. Any ideas why it is stopping?
    
    [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-37968)
    
    *   I had same experience. I used the same code perfectly splitting a workbook into individual files. But next time I used it, it error @ the WS.COPY with a runtime 1004.
        
        [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-38178)
        
3.  Thank you, the video and the instructions were very clear and easy to follow. The code worked perfectly!
    
    [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-35691)
    
4.  Worked like a charm.
    
    Thank you
    
    [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-33764)
    
5.  Wow. This worked really well. Very nice, thank you.
    
    [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-31612)
    
6.  I just want to say thank you! I’m just starting to learn VBA. So I appreciate not only the succinct code but the clear explanation of why some steps are necessary.
    
    I have a inventory report with 86 separate tabs of 15,000+ rows with terrible formatting. Having them all as their own file will make the next steps to append into a single table and transform with power query so much easier.
    
    [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-15103)
    
7.  I am trying to split and worksheet into 2 sheets each with the Names Scrap Yard, Faircrest, and Harrison. I would like to know how to do this too, please.
    
    [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-14631)
    
8.  When I copied your VBA for splitting my worksheet, I get an error on the first line. Sub SplitEachWorksheet() is hsow in the macro box name as Sheet2.SplitEachWorkbook. The vba will not run. What am I doing wrong?
    
    Sub SplitEachWorksheet()  
    Dim FPath As String  
    Dim TexttoFind As String  
    TexttoFind = “Scrap Yard”  
    FPath = Application.ActiveWorkbook.Path  
    Application.ScreenUpdating = False  
    Application.DisplayAlerts = False
    
    For Each ws In ThisWorkbook.Sheets  
    If InStr(1, ws.Name, TexttoFind, vbBinaryCompare) 0 Then  
    ws.Copy  
    Application.ActiveWorkbook.SaveAs Filename:=FPath & “” & ws.Name & “.xlsx”  
    Application.ActiveWorkbook.Close False  
    End If  
    Next
    
    Application.DisplayAlerts = True  
    Application.ScreenUpdating = True  
    End Sub
    
    [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-14630)
    
9.  If I copy the code to PERSONAL macro book it is not working. I need to copy the code in a specific sheet of a workbook and execute. Why? Can you provide a macro that works independently?
    
    [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-14382)
    
10.  thanks a ton bro!
    
    [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-14165)
    
11.  What will be the code to select 2 worksheet and then create a newfile
    
    [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-13959)
    
12.  it only works for the first tab then an erorr comes with
    
    [Reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#comment-13870)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/#respond)

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