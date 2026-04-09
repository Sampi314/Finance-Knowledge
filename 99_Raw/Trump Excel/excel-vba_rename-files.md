# Rename Files Using VBA (Easy Examples)

**Source:** https://trumpexcel.com/excel-vba/rename-files

---

[Skip to content](https://trumpexcel.com/excel-vba/rename-files/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-vba/rename-files/#below-title)

VBA in Excel allows you to rename files in any folder that you can access easily.

This can be done using the Name statement in VBA:

Name oldFilePath As newFilePath

This could be especially useful if you want to rename files in bulk.

In this article, I will show you some examples of how to use VBA to rename files in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-vba/rename-files/#)

VBA to Rename Single File
-------------------------

Below is a very simple VBA code that renames the file Old.xlsx to New.xlsx

    Sub RenameFile()
    
        Name "C:\Users\sumit\Downloads\Old.xlsx" As "C:\Users\sumit\Downloads\New.xlsx"
    
    End Sub

Note that you need to provide the entire file path along with the file name for the old name as well as the new file name.

While the above code works, it does not have any inbuilt error checking for cases where a file might not exist or the name I’ve used in the code is incorrect.

So below is a more refined code that renames the file and shows a confirmation message box when the renaming is done. It also has [error handling](https://trumpexcel.com/vba-error-handling/)
 in case an error occurs while executing the code.

    Sub RenameFile()
        
        Dim oldName As String
        Dim newName As String
        
        oldName = "C:\Users\sumit\Downloads\Old.xlsx"
        
        newName = "C:\Users\sumit\Downloads\New.xlsx"
        
        On Error GoTo ErrorHandler
        
        Name oldName As newName
        
        MsgBox "File has been renamed from " & oldName & " to " & newName
        
        Exit Sub
        
    ErrorHandler:
    
    MsgBox "Couldn't Rename the File - " & Err.Description
    
    End Sub

Renaming All Files in a Folder (Add Prefix / Suffix)
----------------------------------------------------

One practical example could be when you have to rename all the files in a folder and add a prefix or a suffix to the files in that folder.

This could be useful when you have different folders (such as, say, Sales, Marketing, Finance) and you want each file to have this department name so that it’s easily recognizable.

Below is a code that adds the prefix New\_ to all the files in the specified folder:

    Sub RenameAllFilesInFolder()
        Dim folderPath As String
        Dim file As Object
        Dim fileSystem As Object
        Dim newName As String
        Dim prefix As String
        
        ' Specify the folder path
        folderPath = "C:\Users\sumit\Downloads\"
        
        ' Specify the prefix to add to each file name
        prefix = "New_"
        
        On Error GoTo ErrorHandler
        
        ' Create FileSystemObject
        Set fileSystem = CreateObject("Scripting.FileSystemObject")
        
        ' Check if folder exists
        If Not fileSystem.FolderExists(folderPath) Then
            MsgBox "Error: The specified folder does not exist.", vbExclamation
            Exit Sub
        End If
        
        ' Loop through each file in the folder
        For Each file In fileSystem.GetFolder(folderPath).Files
            ' Generate the new file name
            newName = folderPath & prefix & fileSystem.GetFileName(file.Path)
            
            ' Rename the file
            Name file.Path As newName
        Next file
        
        ' Notify the user
        MsgBox "All files have been renamed successfully."
        
        Exit Sub
        
    ErrorHandler:
    
        MsgBox "Couldn't Rename the File - " & Err.Description
    
    End Sub

_Change the Folderpath value and the prefix to customize this code for your needs_

Also read: [VBA Rename Sheet in Excel](https://trumpexcel.com/excel-vba/rename-sheet/)

Renaming Files Based on Cell Values
-----------------------------------

Another common scenario is when you have the existing file name and the new file name in a range in Excel, and you want to use those values to rename the files.

Below, I have a sample data set where I have the folder name in column A, the existing file name in column B, and the new file name in column C.

![Rename Files Using VBA Old and new file names](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20177'%3E%3C/svg%3E)

I want to use this data in Excel to quickly rename the files.

Here is a VBA code that will do this in milli-seconds:

    Sub RenameMultipleFiles()
    Dim ws As Worksheet
    Dim FolderPath As String
    Dim oldFileName As String
    Dim newFileName As String
    Dim lastRow As Long
    Dim i As Long
    Set ws = ActiveSheet
    lastRow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row
    For i = 2 To lastRow
    oldFilePath = ws.Cells(i, 1).Value & "\" & ws.Cells(i, 2).Value
    newFilePath = ws.Cells(i, 1).Value & "\" & ws.Cells(i, 3).Value
    If Dir(oldFilePath) <> "" Then
        Name oldFilePath As newFilePath
    Else
        MsgBox "File was not found: " & oldFilePath
    End If
    Next i
    MsgBox "Files renaming complete"
    End Sub

Note that I have used Activesheet as the sheet with the data about new and old file names. You can use any other sheet in the workbook (or any sheet in any other open workbook as well).

If you’re looking for a non-VBA solution to do this, check out the below video:

Renaming Files that Meet Specific Criteria
------------------------------------------

Another scenario in which VBA can be helpful is when you want to rename files with a specific extension only.

Below is a VBA code that goes through all the files in a folder but only renames the text files (with the .txt extension)

    Sub RenameTXTFiles()
        Dim FSO As Object
        Dim sourceFolder As Object
        Dim file As Object
        Dim folderPath As String
        Dim newName As String
        Dim counter As Integer
        
        ' Create a FileSystemObject
        Set FSO = CreateObject("Scripting.FileSystemObject")
        
        ' Specify the folder path (change this to your desired folder)
        folderPath = "C:\Users\sumit\Downloads\"
        
        ' Check if the folder exists
        If FSO.FolderExists(folderPath) Then
            Set sourceFolder = FSO.GetFolder(folderPath)
            
            ' Initialize counter
            counter = 1
            
            ' Loop through each file in the folder
            For Each file In sourceFolder.Files
                ' Check if the file has a .txt extension
                If LCase(FSO.GetExtensionName(file.Name)) = "txt" Then
                    ' Create new name (you can modify this format as needed)
                    newName = "NewFile_" & file.name & ".txt"
                    
                    ' Rename the file
                    file.Name = newName
                    
                    ' Increment counter
                    counter = counter + 1
                End If
            Next file
            
            MsgBox "Renaming complete. " & (counter - 1) & " files renamed.", vbInformation
        Else
            MsgBox "The specified folder does not exist.", vbExclamation
        End If
        
        Set file = Nothing
        Set sourceFolder = Nothing
        Set FSO = Nothing
    End Sub

You can customize this code by changing the folder path and the file extension.

Also read: [How to Open Excel Files Using VBA (Examples)](https://trumpexcel.com/open-excel-files-using-vba/)

Renaming Files Based on File Size
---------------------------------

Another useful scenario where this kind of code can be useful is when you want to rename files based on their size.

This can help you identify large Excel files or image files that might need some looking into.

Below is the VBA code that would go into a specified folder and then append the text _Large\__ before the five names of all the files that are more than 5MB.

    Sub RenameLargeFiles()
        Dim FSO As Object
        Dim sourceFolder As Object
        Dim file As Object
        Dim folderPath As String
        Dim newName As String
        Dim counter As Integer
        Const SIZE_THRESHOLD As Long = 5242880 ' 5MB in bytes
        
        ' Create a FileSystemObject
        Set FSO = CreateObject("Scripting.FileSystemObject")
        
        ' Specify the folder path (change this to your desired folder)
        folderPath = "C:\Users\sumit\Downloads\"
        
        ' Check if the folder exists
        If FSO.FolderExists(folderPath) Then
            Set sourceFolder = FSO.GetFolder(folderPath)
            
            ' Initialize counter
            counter = 0
            
            ' Loop through each file in the folder
            For Each file In sourceFolder.Files
                ' Check if the file is larger than 5MB
                If file.Size > SIZE_THRESHOLD Then
                    ' Create new name with "Large_" prefix
                    newName = "Large_" & file.Name
                    
                    ' Rename the file
                    file.Name = newName
                    
                    ' Increment counter
                    counter = counter + 1
                End If
            Next file
            
            MsgBox "Renaming complete. " & counter & " files renamed.", vbInformation
        Else
            MsgBox "The specified folder does not exist.", vbExclamation
        End If
        
        ' Clean up
        Set file = Nothing
        Set sourceFolder = Nothing
        Set FSO = Nothing
    End Sub

In the above code, I’ve hardcoded the folder path and specified the file threshold as 5MB. You can change both of these based on your requirements.

Also read: [8 Ways to Reduce Excel File Size (that actually work)](https://trumpexcel.com/reduce-excel-file-size/)

Appending Date and Time to File Names
-------------------------------------

Another useful scenario where VBA can be helpful is when renaming files, such as when you want to append the current date and time in front of all the file names in a specified location.

For example, if you have all the sales invoices in a folder, you can run this VBA code, and it will add the current date (or the current date and time) in all the invoice file names.

Below is a sample VBA code that can do this.

    Sub AppendDateTimeToFileNames()
        Dim FSO As Object
        Dim sourceFolder As Object
        Dim file As Object
        Dim folderPath As String
        Dim newName As String
        Dim dateTimeStr As String
        Dim counter As Integer
        
        ' Create a FileSystemObject
        Set FSO = CreateObject("Scripting.FileSystemObject")
        
        ' Specify the folder path (change this to your desired folder)
        folderPath = "C:\Users\sumit\Downloads\Test\"
        
        ' Check if the folder exists
        If FSO.FolderExists(folderPath) Then
            Set sourceFolder = FSO.GetFolder(folderPath)
            
            ' Initialize counter
            counter = 0
            
            ' Loop through each file in the folder
            For Each file In sourceFolder.Files
                ' Get current date and time string
                dateTimeStr = Format(Now, "dd-mmm-yyyy_hhmmss")
                
                ' Create new name with date and time appended
                newName = dateTimeStr & "_" & FSO.GetBaseName(file.Name) & "." & FSO.GetExtensionName(file.Name)
                
                ' Rename the file
                file.Name = newName
                
                ' Increment counter
                counter = counter + 1
            Next file
            
            MsgBox "Renaming complete. " & counter & " files renamed.", vbInformation
        Else
            MsgBox "The specified folder does not exist.", vbExclamation
        End If
        
        ' Clean up
        Set file = Nothing
        Set sourceFolder = Nothing
        Set FSO = Nothing
    End Sub

You can customize this VBA code by changing the folder path and the date and time format that you want before the file name.

In this article, I showed you a couple of examples where you can use VBA to easily rename files.

I hope you found this article helpful. If you have any questions, feedback, or suggestions for me, please let me know in the comments section.

**Other Excel articles you may also like:**

*   [What is VBA in Excel?](https://trumpexcel.com/excel-vba/)
    
*   [How to Rename a Sheet in Excel (Shortcut)](https://trumpexcel.com/rename-sheet-in-excel/)
    
*   [Excel VBA FileSystemObject (FSO)](https://trumpexcel.com/vba-filesystemobject/)
    
*   [Create New Sheet Using VBA in Excel (Sheets.Add)](https://trumpexcel.com/excel-vba/add-new-sheet/)
    
*   [VBA Copy Sheet to New/Existing Workbook](https://trumpexcel.com/excel-vba/copy-sheet/)
    
*   [Bulk Create Folders (and Subfolders) Using Excel List](https://trumpexcel.com/bulk-create-folders-subfolders-excel-list/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

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