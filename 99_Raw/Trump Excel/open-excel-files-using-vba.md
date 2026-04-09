# How to Open Excel Files Using VBA (Examples)

**Source:** https://trumpexcel.com/open-excel-files-using-vba

---

[Skip to content](https://trumpexcel.com/open-excel-files-using-vba/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/open-excel-files-using-vba/#below-title)

With [VBA in Excel](https://trumpexcel.com/excel-vba/)
, you can easily open one or more Excel files by specifying their location.

This is made possible by the _Workbooks.Open_ method, which takes the file location as the argument and opens that Excel file.

You can do a lot more with the Workbooks.Open method, such as opening all the files in a given folder, opening files as read-only, opening files and then saving them with a different name, etc.

In this tutorial, I will show you how to use VBA to open Excel files and all the amazing things you can do with it.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/open-excel-files-using-vba/#)

Workbooks.Open Method
---------------------

In Excel VBA, you can use Workbooks.Open method to open an Excel file, where you need to specify the file path of the Excel workbook that you want to open.

Below is the syntax of the Workbooks.Open method

_expression.Open (FileName, UpdateLinks, ReadOnly, Format, Password, WriteResPassword, IgnoreReadOnlyRecommended, Origin, Delimiter, Editable, Notify, Converter, AddToMru, Local, CorruptLoad)_

While the Workbooks.Open method can use 15 arguments, in most cases, we only need to use two or three of them.

I will show you examples that will make it clearer how to use these arguments.

Open Workbook By Specifying the File Path
-----------------------------------------

Let’s first look at how to open an Excel file where you know the entire file path.

Below is the VBA code that would open an Excel file named Example.xlsx in the folder called Project on my system:

    Sub OpenWorkbook()
    Workbooks.Open ("C:\Users\sumit\OneDrive\Desktop\Project\Example.xlsx")
    End Sub

Note that the part of the Excel file needs to be in double quotes, and you need to specify the entire file path including the name of the file and the extension.

In case Excel is not able to find the file at the location that you specified, it will show you an error as shown below.

![Error When File is not found](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20550%20308'%3E%3C/svg%3E)

### Open Multiple Excel Files Together

If you want to open multiple Excel files using one single subroutine, you can do that as well (by using multiple Workbooks.Open methods with the file paths)

Below I have a VBA code that would open three Excel files, where I need to specify the path for each file in separate Workbooks.Open method.

    Sub OpenMulitpleWorkbook()
    Workbooks.Open ("C:\Users\sumit\OneDrive\Desktop\Project\Example1.xlsx")
    Workbooks.Open ("C:\Users\sumit\OneDrive\Desktop\Project\Example2.xlsx")
    Workbooks.Open ("C:\Users\sumit\OneDrive\Desktop\Project\Example3.xlsx")
    End Sub

Open All Excel Workbooks in a Folder
------------------------------------

If you have multiple Excel files in a folder, and you want to open all the files in that folder in one go, you can do that easily using the Workbooks.Open method along with the simple [Do While loop](https://trumpexcel.com/vba-loops/)
.

Below I have code where I have specified the folder path, and when this [code is executed](https://trumpexcel.com/run-a-macro-excel/)
, it goes through each Excel file in the folder and opens it.

    Sub OpenFilesFromFolder()
        Dim wb As Workbook
        Dim FolderPath As String
        Dim FilePath As String
            FolderPath = "C:\Users\sumit\OneDrive\Desktop\Project\"
            FilePath = Dir(FolderPath & "*.xls*")
            Do While FilePath <> ""
                Set wb = Workbooks.Open(FolderPath & FilePath)
                FilePath = Dir
            Loop
    End Sub

### Open Excel Files Based on the Name

If you only want to open specific Excel files in a folder based on its name, you can modify the above VBA code to do that.

Below I have a VBA code where it would open only those Excel files in the specified folders that have the word “Sales” in the name of the Excel file.

    Sub OpenFilesFromFolder()
        Dim wb As Workbook
        Dim FolderPath As String
        Dim FilePath As String
            FolderPath = "C:\Users\sumit\OneDrive\Desktop\Project\"
            FilePath = Dir(FolderPath & "*Sales*" & ".xls*")
            Do While FilePath <> ""
                Set wb = Workbooks.Open(FolderPath & FilePath)
                FilePath = Dir
            Loop
    End Sub
    

In the above code, I have used Dir(FolderPath & “\*Sales\*” & “.xls\*”) as the FilePath, where the word Sales is wrapped in [asterisks (\*)](https://trumpexcel.com/excel-wildcard-characters/)
.

This ensures that only the files with the word ‘Sales’ in the name would get opened, and the rest would be ignored.

Also read: [VBA Copy Sheet to New/Existing Workbook](https://trumpexcel.com/excel-vba/copy-sheet/)

Opening a Password Protected Excel Workbook
-------------------------------------------

You can also open password-protected workbooks by specifying the password in the VBA code.

Below I have a VBA code that would open a password-protected Excel file, where the password is Excel123

    Sub OpenExcelFile()
    Workbooks.Open "C:\Users\sumit\OneDrive\Desktop\Project\Example.xlsx", , , Password:="Excel123"
    End Sub

_Also read: [Rename Files Using VBA](https://trumpexcel.com/excel-vba/rename-files/)
_

Open Excel File By Showing the Open Dialog Box
----------------------------------------------

In the examples covered so far, I have specified the file name or the path of the files that need to be opened in the VBA code itself.

However, you can use VBA to open the Open File dialog box, where the user can navigate to the file and select it to open it.

Below is the VBA code that would show the Open dialog box, where the user can select the file and open it.

    Sub OpenFileDialogBox()
    On Error Resume Next
        Dim FilePath As String
        FilePath = Application.GetOpenFilename()
        Workbooks.Open (FilePath)
    End Sub

![Open File Dialog Box using VBA Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20439'%3E%3C/svg%3E)

I have used [On Error Resume Next](https://trumpexcel.com/vba-error-handling/)
 in case the user decides to close the Open dialog box without selecting any file. If this statement is not used, it will show an error.

In this short tutorial, I showed you a couple of different ways you can use to open workbooks using VBA in Excel.

While you may not use these codes to simply open an Excel file, the concept could be quite useful when working on bigger VBA projects where you need to open Excel files as part of the code

**Other Excel tutorials you may also like:**

*   [Save As Shortcuts in Excel (Quick and Easy)](https://trumpexcel.com/save-as-shortcuts-excel/)
    
*   [How to Automatically Open Specific Excel Files on Startup](https://trumpexcel.com/automatically-open-excel-file-startup/)
    
*   [Check If Workbook Is Open Using VBA](https://trumpexcel.com/excel-vba/check-if-workbook-open/)
    
*   [Microsoft Excel Won’t Open – How to Fix it! (6 Possible Solutions)](https://trumpexcel.com/microsoft-excel-wont-open/)
    
*   [Using Workbook Object in Excel VBA (Open, Close, Save, Set)](https://trumpexcel.com/vba-workbook/)
    
*   [Working with Cells and Ranges in Excel VBA (Select, Copy, Move, Edit)](https://trumpexcel.com/vba-ranges/)
    
*   [Working with Worksheets using Excel VBA (Explained with Examples)](https://trumpexcel.com/vba-worksheets/)
    
*   [Bulk Create Folders from Excel List](https://trumpexcel.com/bulk-create-folders-subfolders-excel-list/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Open Excel Files Using VBA (Examples)”
-----------------------------------------------------------

1.  Sir, thank you for the video.  
    In code “Open all excel files” I could not understand the statement:  
    FilePath = Dir  
    Would you kindly explain or provide a link that has detailed explanation?  
    I also looked at your webpage [https://trumpexcel.com/vba-dir-function/](https://trumpexcel.com/vba-dir-function/)
     but could not find this statement.  
    I tried stepping through then there is an error message but the code works without stepping through.  
    Thank You
    
    [Reply](https://trumpexcel.com/open-excel-files-using-vba/#comment-41397)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/open-excel-files-using-vba/#respond)

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