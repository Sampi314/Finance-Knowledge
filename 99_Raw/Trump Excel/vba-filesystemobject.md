# Using VBA FileSystemObject (FSO) in Excel - Examples

**Source:** https://trumpexcel.com/vba-filesystemobject

---

[Skip to content](https://trumpexcel.com/vba-filesystemobject/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vba-filesystemobject/#below-title)

When we use VBA in Excel, most of it is to automate our tasks.

This also means that most of the time, we work with [cells and ranges](https://trumpexcel.com/vba-ranges/)
, [worksheets](https://trumpexcel.com/vba-worksheets/)
, [workbooks](https://trumpexcel.com/vba-workbook/)
, and other objects which are a part of the Excel application.

But VBA is a lot more powerful and can also be used to work with stuff outside of Excel.

In this tutorial, I will show you how to use VBA FileSystemObject (FSO) to work with files and folders on your system or network drives.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/vba-filesystemobject/#)

What is VBA FileSystemObject (FSO)?
-----------------------------------

FileSystemObject (FSO) allows you to access the file system of your computer. Using it, you can access and modify the files/folders/directories in your computer system.

For example, below are some of the things you can do by using FileSystemObject in Excel VBA:

*   Check if a file or a folder exists.
*   Create or [rename files](https://trumpexcel.com/excel-vba/rename-files/)
    /folders.
*   Get a list of all the file names (or sub-folder names) in a folder.
*   Copy files from one folder to another.

I hope you get the idea.

I will cover all these above examples (plus more) later in this tutorial.

While some of the things mentioned above can also be done using traditional VBA functions (such as the [DIR function](https://trumpexcel.com/vba-dir-function/)
) and methods, that would lead to longer and more complicated codes. FileSystemObject makes it easy to work with files and folders while keeping the code clean and short.

Note: FSO can only be used in Excel 2000 and later versions.

What All Objects Can You Access Through FileSystemObject?
---------------------------------------------------------

As I mentioned above, you can access and modify files and folders using the FileSystemObject in VBA.

Below is a table that shows the most important objects that you can access and modify using FSO:

|     |     |
| --- | --- |
| **Object** | **Description** |
| Drive | Drive Object allows you to get information about the drive such as whether it exists or not, it’s path name, drive type (removable or fixed), it’s size, etc. |
| Folder | Folder object allows you to create or modify folders in your system. For example, you can create, delete, rename, copy folders using this object. |
| File | File Object allows you to work with files in your system. For example, you can create, open, copy, move, and delete files using this object. |
| TextStream | TextStream object allows you to create or read text files. |

Each of the above objects has methods that you can use to work with these.

To give you an example, if you want to delete a folder, you will use the DeleteFolder method of the Folder object. Similarly, if you want to copy a file, you will use the CopyFile method of the File object.

Don’t worry if this seems overwhelming or hard to understand. You will get a much better understanding when you go through the examples that I have covered in this tutorial.

Just for the reference purpose, I have covered all the FileSystemObject methods (for each object) at the [end of this tutorial](https://trumpexcel.com/vba-filesystemobject/#FileSystemObject-FSO-Methods)
.

Enabling FileSystemObject in Excel VBA
--------------------------------------

FileSystemObject is not available by default in the Excel VBA.

Since we are dealing with files and folders that are outside of the Excel application, we need to first create a reference to the library that holds these objects (drives, files, folders).

Now there are two ways you can start using FileSystemObject in Excel VBA:

1.  Setting the reference to the Microsoft Scripting Runtime Library (Scrrun.dll)
2.  Creating an object to refer to the library from the code itself

While both these methods work (and I’ll show you how to do this next), I recommend using the first method.

Note: When you enable FileSystemObject, you can access all the objects in it. This includes the FileSystemObject, Drive, Files, Folders, etc. I will be focussing majorly on the FileSystemObject in this tutorial.

### Setting the Reference to the Microsoft Scripting Runtime Library

When you create a reference to the Scripting Runtime Library, you allow Excel VBA the access to all the properties and methods of files and folder. Once this is done, you can refer to the files/folders/drives object from within the Excel VBA (just like you can refer the cells, worksheets or workbooks).

Below are the steps to create a reference to the Microsoft Scripting Runtime Library:

1.  In the VB Editor, click on Tools.![Tools in Excel VB Editor Toolbar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20483%2093'%3E%3C/svg%3E)
2.  Click on References.![References Option in Excel VB Editor Toolbar to Enable VBA FileSystemObject FSO](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20627%20228'%3E%3C/svg%3E)
3.  In the References dialog box that opens, scroll through the available references and check the ‘Microsoft Scripting Runtime’ option.![Scrrun Microsoft Scripting Runtime Library Option Checked to access VBA FileSystemObject](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20518%20447'%3E%3C/svg%3E)
4.  Click OK.

The above steps would now allow you to refer to the FSO objects from Excel VBA.

#### Creating an Instance of FileSystemObject in the Code

Once you have set the reference to the Scripting FileSystemObject library, you need to create an instance of the FSO object in your code.

Once this is created, you can use it in VBA.

Below is the code that will set the object variable MyFSO as a FileSystemObject object:

Sub CreatingFSO()
Dim MyFSO As FileSystemObject
Set MyFSO = New FileSystemObject
End Sub

In this code, first I have declared the variable MyFSO as a FileSystemObject type object. This is possible only because I have created a reference to the Microsoft Scripting Runtime Library. If the reference is not created, this is going to give you an error (as Excel wouldn’t recognize what FileSystemObject means).

In the second line, two things happen:

1.  The NEW keyword creates an instance of the FileSystemObject. This means that now I can use all the methods of FileSystemObject to work with files and folders. If you don’t create this instance, you’ll not be able to access the methods of FSO.
2.  The SET keyword sets the object MyFSO to this new instance of FileSystemObject. This allows me to use this object to access files and folders. For example, if I need to create a folder, I can use MyFSO.CreateFolder method.

If you want, you can also combine the above two statements into one as shown below:

Sub CreatingFSO()
Dim MyFSO As New FileSystemObject
End Sub

A big benefit of using this method (which is to set the reference to the Microsoft Scripting Runtime Library) is that when you use the FSO objects in your code, you will be able to use the IntelliSense feature that shows the methods and properties associated with an object (as shown below).

![Intellisense in FileSystemObject (FSO) in Excel VBA](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20640%20360'%3E%3C/svg%3E)

This is not possible when you create the reference from within the code (covered next).

### Creating an Object from the Code

Another way to create a reference to FSO is by doing it from the code. In this method, you don’t need to create any reference (as done in the previous method).

When you are writing the code, you can create an object from within the code and refer to the Scripting.FileSystemObject.

The below code creates an object FSO and then makes this a FileSystemObject type.

Sub FSODemo()
Dim FSO As Object
Set FSO = CreateObject("Scripting.FileSystemObject")
End Sub

While this may seem more convenient, a big downside of using this method is that it would not show an IntelliSense when you work with objects in FSO. For me, this is a huge negative and I always recommend using the previous method of enabling FSO (which is by setting the reference to the ‘Microsoft Scripting Runtime’)

VBA FileSystemObject Examples
-----------------------------

Now let’s dive in and have a look at some practical examples of using FileSystemObject in Excel.

### Example 1: Check if a File or Folder Exists

The following code will check whether the folder with the name ‘Test’ exists or not (in the specified location).

If the folder exists, the [IF condition](https://trumpexcel.com/if-then-else-vba/)
 is True and it shows a message – ‘The Folder Exists’ in a [message box](https://trumpexcel.com/vba-msgbox/)
. And if it doesn’t exist, it shows a message – The Folder Does Not Exist’.

Sub CheckFolderExist()
Dim MyFSO As FileSystemObject
Set MyFSO = New FileSystemObject
If MyFSO.FolderExists("C:\\Users\\sumit\\Desktop\\Test") Then
    MsgBox "The Folder Exists"
Else
    MsgBox "The Folder Does Not Exist"
End If
End Sub

Similarly, you can also check if a file exists or not.

The below code checks whether there is a file with the name Test.xlsx in the specified folder or not.

Sub CheckFileExist()
Dim MyFSO As FileSystemObject
Set MyFSO = New FileSystemObject
If MyFSO.FileExists("C:\\Users\\sumit\\Desktop\\Test\\Test.xlsx") Then
    MsgBox "The File Exists"
Else
    MsgBox "The File Does Not Exist"
End If
End Sub

### Example 2: Create a New Folder in the Specified Location

The below code would create a folder with the name ‘Test’ in the C drive of my system (you will have to specify the path on your system where you want to create the folder).

Sub CreateFolder()
Dim MyFSO As FileSystemObject
Set MyFSO = New FileSystemObject
MyFSO.CreateFolder ("C:\\Users\\sumit\\Desktop\\Test")
End Sub

While this code works fine, it would show an error in case the folder already exists.

The below code checks whether the folder already exists and creates a folder if it doesn’t. In case the folder already exists, it shows a message. To check whether the folder exists, I have used the **FolderExists method** of the FSO.

Sub CreateFolder()
Dim MyFSO As FileSystemObject
Set MyFSO = New FileSystemObject
If MyFSO.FolderExists("C:\\Users\\sumit\\Desktop\\Test") Then
    MsgBox "The Folder Already Exist"
Else
    MyFSO.CreateFolder ("C:\\Users\\sumit\\Desktop\\Test")
End If
End Sub

### Example 3: Get a List of All Files in a Folder

The below code would show the names of all the files in the specified folder.

Sub GetFileNames()
Dim MyFSO As FileSystemObject
Dim MyFile As File
Dim MyFolder As Folder

Set MyFSO = New Scripting.FileSystemObject
Set MyFolder = MyFSO.GetFolder("C:\\Users\\sumit\\Desktop\\Test")

For Each MyFile In MyFolder.Files
    Debug.Print MyFile.Name
Next MyFile

End Sub

This code is a little more complex that the ones we have already seen.

As I mentioned above in this tutorial, when you reference the ‘Microsoft Scripting Runtime Library’, you can use FileSystemObject as well as all other objects (such as Files and Folders).

In the above code, I use three objects – FileSystemObject, File, and Folder. This allows me to go through each file in the specified folder. I then use the name property to get the list of all file names.

Note that I am using Debug.Print to get the names of all the files. These names will be listed in the [immediate window in the VB Editor](https://trumpexcel.com/vba-immediate-window/)
.

### Example 4: Get the List of All Sub-folders in a Folder

The below code will give the names of all the sub-folders in the specified folder. The logic is exactly the same as covered in the above example. Instead of files, in this code, we have used sub-folders.

Sub GetSubFolderNames()
Dim MyFSO As FileSystemObject
Dim MyFile As File
Dim MyFolder As Folder
Dim MySubFolder As Folder

Set MyFSO = New Scripting.FileSystemObject
Set MyFolder = MyFSO.GetFolder("C:\\Users\\sumit\\Desktop\\Test")

For Each MySubFolder In MyFolder.SubFolders
    Debug.Print MySubFolder.Name
Next MySubFolder

End Sub

### Example 5: Copy a File from One Place to Another

The below code will copy the file from ‘Source’ folder and copy it to the ‘Destination’ folder.

Sub CopyFile()
Dim MyFSO As FileSystemObject
Dim SourceFile As String
Dim DestinationFolder As String
Set MyFSO = New Scripting.FileSystemObject

SourceFile = "C:\\Users\\sumit\\Desktop\\Source\\SampleFile.xlsx"
DestinationFolder = "C:\\Users\\sumit\\Desktop\\Destination"

MyFSO.CopyFile Source:=SourceFile, Destination:=DestinationFolder & "\\SampleFileCopy.xlsx"

End Sub

In the above code, I have used two variables – SourceFile and DestinationFolder.

Source File holds the address of the file I want to copy and the DestinationFolder variable holds the address to the folder I want the file to be copied to.

Note that it’s not sufficient to give the destination folder name when you’re copying a file. You also need to specify the file name. You can use the same file name or can also change it. In the above example, I copied the file and named it SampleFileCopy.xlsx

### Example 6: Copy All Files From One Folder to Another

The below code will copy all the files from the Source folder to the destination folder.

Sub CopyAllFiles()
Dim MyFSO As FileSystemObject
Dim MyFile As File
Dim SourceFolder As String
Dim DestinationFolder As String
Dim MyFolder As Folder
Dim MySubFolder As Folder

SourceFolder = "C:\\Users\\sumit\\Desktop\\Source"
DestinationFolder = "C:\\Users\\sumit\\Desktop\\Destination"

Set MyFSO = New Scripting.FileSystemObject
Set MyFolder = MyFSO.GetFolder(SourceFolder)

For Each MyFile In MyFolder.Files
    MyFSO.CopyFile Source:=MyFSO.GetFile(MyFile), \_
    Destination:=DestinationFolder & "\\" & MyFile.Name, Overwritefiles:=False
Next MyFile

End Sub

The above code will copy all the files from the Source folder to the Destination Folder.

Note that in the MyFSO.CopyFile method, I have specified the ‘Overwritefiles’ property to be False (this is True by default). This makes sure that in case you already have the file in the folder, it’s not copied (and you will see an error). If you remove ‘Overwritefiles’ or set this to True, in case there are files in the destination folder with the same name, these would be overwritten.

**Pro Tip:** When copying files, there is always a chance of overwriting files. A good idea, in this case, is to add the timestamp along with the name. This will ensure that the names are always different and you can easily track which files were copied at what time.

If you want to copy the files of a certain extension only, you can do that by using an IF Then statement to check whether the extension is xlsx or not.

Sub CopyExcelFilesOnly()
Dim MyFSO As FileSystemObject
Dim MyFile As File
Dim SourceFolder As String
Dim DestinationFolder As String
Dim MyFolder As Folder
Dim MySubFolder As Folder

SourceFolder = "C:\\Users\\sumit\\Desktop\\Source"
DestinationFolder = "C:\\Users\\sumit\\Desktop\\Destination"

Set MyFSO = New Scripting.FileSystemObject
Set MyFolder = MyFSO.GetFolder(SourceFolder)

For Each MyFile In MyFolder.Files
    If MyFSO.GetExtensionName(MyFile) = "xlsx" Then
        MyFSO.CopyFile Source:=MyFSO.GetFile(MyFile), \_
        Destination:=DestinationFolder & "\\" & MyFile.Name, Overwritefiles:=False
    End If
Next MyFile

End Sub

FileSystemObject (FSO) Methods
------------------------------

Here are the methods that you can use for each object. This is just for reference purpose and doesn’t worry about it too much. The usage of some of these has been shown in the examples covered above.

|     |     |     |
| --- | --- | --- |
| **FSO Methods** | **For Object** | **Description** |
| DriveExists | Drive | Checks whether the drive exists or not |
| GetDrive | Drive | Returns an instance of the drive object based on the specified path |
| GetDriveName | Drive | Reruns the drive name |
| BuildPath | File/Folder | Generate a path from an existing path and a name |
| CopyFile | File/Folder | Copies a file |
| GetAbsolutePathName | File/Folder | Return the canonical representation of the path |
| GetBaseName | File/Folder | Return base name from a path. For example, “D:\\TestFolder\\TestFile.xlsm” will return TextFile.xlsm |
| GetTempName | File/Folder | Generate name that can be used to name a temporary file |
| CopyFolder | Folder | Copies a folder from one location to other |
| CreateFolder | Folder | Creates a new folder |
| DeleteFolder | Folder | Deletes the specified folder |
| FolderExists | Folder | Checks whether the Folder exists or not |
| GetFolder | Folder | Returns an instance of the folder object based on the specified path |
| GetParentFolderName | Folder | Retruns the name of the parent folder based on the specified path |
| GetSpecialFolder | Folder | Get the location of various system folders. |
| MoveFolder | Folder | Moves a folder from one location to other |
| DeleteFile | File | Deletes a file |
| FileExists | File | Checks if a file exists or not |
| GetExtensionName | File | Returns the file extension |
| GetFile | File | Returns the instance of a file object based on the specified path |
| GetFileName | File | Returns the file name |
| GetFileVersion | File | Returns the file version |
| MoveFile | File | Moves a file |
| CreateTextFile | File | Creates a text file |
| GetStandardStream | File | Retrieve the standard input, output or error stream |
| OpenTextFile | File | Open a file as a TextStream |

**You May Also Like the Following Excel Tutorials:**

*   [Get a List of File Names from Folders & Sub-folders (using Power Query)](https://trumpexcel.com/list-file-names-power-query/)
    .
*   [Get the List of File Names from a Folder in Excel (with and without VBA)](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/)
    .
*   [Understanding Excel VBA Data Types (Variables and Constants)](https://trumpexcel.com/vba-data-types-variables-constants/)
    .
*   [Creating a User Defined Function (UDF) in Excel VBA.](https://trumpexcel.com/user-defined-function-vba/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

13 thoughts on “Using VBA FileSystemObject (FSO) in Excel”
----------------------------------------------------------

1.  Hi,  
    I have been using this for getting the file names from a folder and is works great.  
    The name is the folder is stored in a string variable.  
    But, I have run into issues where the path name contains a space.  
    I get path not found errors. Many google searches have not provided a solution.  
    Looking for a working example with a space in the path or file name.  
    The one drive setup for work has this in almost every file.  
    Thanks,  
    Bob
    
    [Reply](https://trumpexcel.com/vba-filesystemobject/#comment-14515)
    
2.  It is truly helpful. Thanks for all your efforts
    
    [Reply](https://trumpexcel.com/vba-filesystemobject/#comment-13719)
    
3.  Thanks for write this article. Thorough article with some great examples students can try. Thanks, Stewart
    
    [Reply](https://trumpexcel.com/vba-filesystemobject/#comment-13308)
    
4.  Thanks much!  
    Notice: With method “add Microsoft scripting runtime” is functional also “prediction”, which is not functional with “CreateObject(“Scripting.FileSystemObject”)”.
    
    [Reply](https://trumpexcel.com/vba-filesystemobject/#comment-12829)
    
5.  Hi Sumit,
    
    Thanks for the information, however, I run into an issue with below, can you please help where am doing wrong.
    
    Path = “C:WSDataFilesPTP” & Cells(1, 2).Value  
    Dim MyFSO As New FileSystemObject  
    If MyFSO.FolderExists(Path) Then  
    ‘Folder Exists  
    Else  
    MyFSO.CreateFolder (Path) ‘I tried this command also MyFSO.CreateFolder Path  
    End If
    
    Regards  
    Chandrakanth Jampala
    
    [Reply](https://trumpexcel.com/vba-filesystemobject/#comment-12356)
    
    *   use this I think it will shove your problem
        
        a = Cells(1, 2).Value  
        path = “D:other” & a
        
        [Reply](https://trumpexcel.com/vba-filesystemobject/#comment-12698)
        
6.  This tutorial is very helpful, thank you. Although the list of Methods (and some properties) is great for reference, it seems to be incomplete. For example, properties drivetype and freespace are missing. Please notice that this is just a hint for improvement, not criticism
    
    [Reply](https://trumpexcel.com/vba-filesystemobject/#comment-11850)
    
7.  Hello,  
    Many thanks for this excellent tutorial, with helped me much.  
    I had the challenge to find all files in all subfolders of a given path. Based on your code and instructions and with the idee I found in the web, I wrote the following recursive subroutine to use with your example 3.
    
    Sub GetFileNamesInSubFolders (Folder As Folder)  
    Dim MyFSO As FileSystemObject  
    Dim MyFile As File  
    Dim MySubFolder As Folder  
    If Folder Is Nothing Then Exit Sub  
    For Each MySubFolder In Folder.SubFolders  
    Debug.Print MySubFolder.Path  
    For Each MyFile In MySubFolder.Files  
    Debug.Print MyFile.Name  
    Next MyFile  
    Next MySubFolder  
    ‘recursive call  
    GetFileNamesInSubFolders MySubFolder  
    End Sub
    
    It can be called from your procedure in example 3 with the Line…
    
    GetFileNamesInSubFolders MyFolder
    
    .. inserted just before ‘End Sub’.
    
    Btw: Your example 4 could also be complemented in this manner to list all subfolders in all subfolders by omitting the Lines ‘For Each Myfile ..’ to ‘… Next My File’ . Hope I did it correctly – in my test it works fine.
    
    Best regards  
    Lothar
    
    [Reply](https://trumpexcel.com/vba-filesystemobject/#comment-11807)
    
8.  useful info
    
    [Reply](https://trumpexcel.com/vba-filesystemobject/#comment-11694)
    
9.  wonderful
    
    [Reply](https://trumpexcel.com/vba-filesystemobject/#comment-11512)
    
10.  Hello Sumit. Thank you for the VBA Script as it is help for me as I want to find out where all my photo’s are on file and the duplicated ones.  
    I am using a Mac with Excel for Mac 16.16.3 (181015) version and cannot find the “Microsoft Scripting Runtime”. Does this mean that I cannot use this VBA for finding files?  
    Thanks  
    Paul
    
    [Reply](https://trumpexcel.com/vba-filesystemobject/#comment-10705)
    
11.  Hello Summit. Thanks for the clear tutorial. One question: is it possible to use wildcards in these vba scripts (like \*)  
    Thanks  
    Peter
    
    [Reply](https://trumpexcel.com/vba-filesystemobject/#comment-10702)
    
12.  Dear Sumit,
    
    Many thanks for sharing this Great and systematic tutorial.  
    Just wanted to know on how to get a List of File Names from Folders & Sub-folders in Excel with VBA and create hyperlink to that file from that list .
    
    Looking forward to having your further advice in this regards
    
    Best regards  
    Arsil Hadjar
    
    [Reply](https://trumpexcel.com/vba-filesystemobject/#comment-10699)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/vba-filesystemobject/#respond)

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