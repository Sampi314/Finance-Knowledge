# VBA DIR Function - An Easy Explanation with Examples

**Source:** https://trumpexcel.com/vba-dir-function

---

[Skip to content](https://trumpexcel.com/vba-dir-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/vba-dir-function/#below-title)

VBA has some useful functions that can take your automation in Excel to the next level.

One such function is the **VBA DIR function**.

While by itself, it may seem like a simple function that does one specific thing.

But when you combine it with some other useful elements of the [VBA coding language](https://trumpexcel.com/excel-vba/)
, you can create powerful stuff (covered in the examples later in this tutorial).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/vba-dir-function/#)

What Does VBA Dir Function Do?
------------------------------

Use VBA DIR function when you want to get the name of the file or a folder, using their path name.

To give you an example, if you have an Excel file in a folder, you can use the VBA DIR function to get the name of that Excel file (or any other type of file).

What if I want to get the names of all the Excel files in the folder (or all the files – be it Excel file or not)?

_You can do that too!_

When you use DIR function once, it returns the **first file name** in a folder. Now if you want to get the names of the second, third, fourth files as well, you can use the DIR function again (covered later as an example).

**Dir** returns the first file name that matches the pathname. To get any additional [file names](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/)
 that match pathname, call **Dir** again with no arguments. When no more file names match, **Dir** returns a zero-length string (“”). Covered in Example 3 and 4 later in this tutorial.

Syntax of VBA DIR Function
--------------------------

Dir \[ (pathname \[ ,attributes \] ) \]

*   **pathname**: This is an optional argument. This can be the file name, folder name, or directory name. If pathname is not found, VBA DIR function returns a zero-length string (“”)
*   **attributes**: This is an optional argument. You can use this argument to specify some attributes and DIR function will return the file names based on those attributes. For example, if you want a list of all hidden files or read-only files (along with files with no attributes), you need to specify that in this argument.

Attributes available to use in VBA DIR function (you can use one or more of these):

|     |     |     |
| --- | --- | --- |
| **Constant** | **Value** | **Description** |
| vbNormal | 0   | (Default) Specifies files with no attributes. |
| vbReadOnly | 1   | Specifies read-only files in addition to files with no attributes. |
| vbHidden | 2   | Specifies hidden files in addition to files with no attributes. |
| VbSystem | 4   | Specifies system files in addition to files with no attributes. Not available on the Macintosh. |
| vbVolume | 8   | Specifies volume label; if any other attributed is specified, vbVolume is ignored. Not available on the Macintosh. |
| vbDirectory | 16  | Specifies directories or folders in addition to files with no attributes. |
| vbAlias | 64  | Specified file name is an alias. Available only on the Macintosh. |

Using Wildcard Characters with DIR Function
-------------------------------------------

If you’re working with Windows, you can also use the wildcard characters in the DIR function.

_Note that you can not use these when working with VBA in Macintosh._

Using wildcards can be useful when:

*   You want to get the file names of a particular file type (such as .XLSX or .PPTX)
*   When you have a specific suffix/prefix in filenames and you want to get the names of these files/folders/directories. For example, if you want the names of all the files with the prefix 2019 in it, you can do that using wildcard characters.

There are three wildcard characters in Excel:

1.  **\* (asterisk)** – It represents any number of characters. For example, **2019\*** would give you the names of all the files with the prefix 2019 in it.
2.  **? (question mark)** – It represents one single character. For example, 2019? would give you the names of all the files that start with 2019 and has one more character in the name (such as 2019A, 2019B, 2019C, and so on)

_Note: There is one more wildcard character – tilde (~). Since it’s not used a lot, I have skipped its explanation. You can [read more about it here if interested](https://trumpexcel.com/excel-wildcard-characters/)
._

VBA DIR Function – Examples
---------------------------

Now let’s dive in and see some examples of using the VBA DIR function.

### Example 1 – Getting the File Name from its Path

When you have the path of a file, you can use the DIR function to get the name of the file from it.

For example, the below code returns the name of the file and shows it in a [message box](https://trumpexcel.com/vba-msgbox/)
.

Sub GetFileNames()
Dim FileName As String
FileName = Dir("C:\\Users\\sumit\\Desktop\\Test\\Excel File A.xlsx")
MsgBox FileName
End Sub

The above code uses a variable ‘FileName’ to store the file name that is returned by the DIR function. It then uses a message box to display the file name (as shown below).

![File Name using VBA DIR Function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20160%20186'%3E%3C/svg%3E)

And what happens when the file doesn’t exist?

In that case, the DIR function would return an empty string.

The below code uses an [If Then Else statement](https://trumpexcel.com/if-then-else-vba/)
 to check whether the file exists or not. If the file doesn’t exist, it shows a message box with a text “File Doesn’t Exist”, else it shows the file name.

Sub CheckFileExistence()
Dim FileName As String
FileName = Dir("C:\\Users\\sumit\\Desktop\\Test\\Excel File A.xlsx")

If FileName <> "" Then
    MsgBox FileName
Else
    MsgBox "File Doesn't Exist"
End If

End Sub

### Example 2 – Check if a Directory Exists or Not (and create if it doesn’t)

The below code checks whether the folder ‘Test’ exists or not.

A message box is used to show a message in case the folder exists or when it doesn’t exist.

Sub CheckDirectory()
Dim PathName As String
Dim CheckDir As String

PathName = "C:\\Users\\sumit\\Desktop\\Test"
CheckDir = Dir(PathName, vbDirectory)

If CheckDir <> "" Then
    MsgBox CheckDir & " exists"
Else
    MsgBox "The directory doesn't exist"
End If

End Sub

You can refine this code further to check whether the folder exists or not, and if it doesn’t, then you can use VBA to create that folder.

Below is the code that uses the **MkDir function** to create a folder in case it doesn’t exist.

Sub CreateDirectory()
Dim PathName As String
Dim CheckDir As String

PathName = "C:\\Users\\sumit\\Desktop\\Test"
CheckDir = Dir(PathName, vbDirectory)

If CheckDir <> "" Then
    MsgBox CheckDir & " folder exists"
Else
    MkDir PathName
    MsgBox "A folder has been created with the name" & CheckDir
End If

End Sub

### Example 3 – Get the Names of All File and Folders in a Directory

If you want to get a list of all the file and folder names in a directory, you can use the DIR Function.

The below code lists all the files and folder names in the Test folder (which is located at the following path – C:\\Users\\sumit\\Desktop\\Test\\).

I am using Debug.Print to show the names in the [Immediate window](https://trumpexcel.com/vba-immediate-window/)
. You can also use this to list the names in a message box or in a column in Excel.

Sub GetAllFile&FolderNames()
Dim FileName As String
FileName = Dir("C:\\Users\\sumit\\Desktop\\Test\\", vbDirectory)

Do While FileName <> ""
    Debug.Print FileName
    FileName = Dir()
Loop
End Sub

The Do While loop in the above code continues till all the files and folders in the given path have been covered. When there are no more files/folders to cover, FileName becomes a null string and the loop stops.

### Example 4 – Get the Names of All Files in a Folder

You can use the below code to get the names of all the files in a folder/directory (and not the names of the sub-folders).

Sub GetAllFileNames()
Dim FileName As String
FileName = Dir("C:\\Users\\sumit\\Desktop\\Test\\")

Do While FileName <> ""
    Debug.Print FileName
    FileName = Dir()
Loop
End Sub

This code is just like the code used in Example 3, with one minor difference.

In this code, I have not specified **vbDirectory** in the DIR function. When you specify vbDirectory, it will give you the names of all the files as well as folders.

When you don’t specify vbDirectory, DIR function will only give you the names of the files.

**Note**: If you want to get the names of all the files in the main folder and the sub-folders, you can’t use the DIR function (as it’s not recursive). To do this, you can either use [Power Query (no coding needed)](https://trumpexcel.com/list-file-names-power-query/)
 or use the [File System Object in VBA](https://trumpexcel.com/vba-filesystemobject/)
 (with recursion).

### Example 5 – Get the Names of All the Sub-Folders within a Folder

The below code would give you the names of all the sub-folders within the specified folder.

It uses the **GetAtr function** in VBA, which allows us to check whether the name returned by the DIR function is the name of a file or a folder/directory.

Sub GetSubFolderNames()
Dim FileName As String
Dim PathName As String

PathName = "C:\\Users\\sumit\\Desktop\\Test\\"
FileName = Dir(PathName, vbDirectory)

Do While FileName <> ""
If GetAttr(PathName & FileName) = vbDirectory Then
    Debug.Print FileName
End If
FileName = Dir()
Loop
End Sub

Again, I am using Debug.Print to get the names in the immediate window. You can get these in a message box or in Excel (by modifying the code accordingly).

### Example 6 – Get the First Excel File from a Folder

With DIR function, you can specify the file extension or any suffix/prefix that you want in the file name that is returned.

The below code would display the name of the first Excel file in the Test folder.

Sub GetFirstExcelFileName()
Dim FileName As String
Dim PathName As String

PathName = "C:\\Users\\sumit\\Desktop\\Test\\"
FileName = Dir(PathName & "\*.xls\*")
MsgBox FileName
End Sub

Note that I have used \*.xls\* (asterisk sign on both sides). This will ensure that all the versions of Excel files are checked (.xls, xlsx, .xlsm, .xlsb).

### Example 7 – Get Names of All Excel File in a Folder

Use the below code to get the names of all the Excel files in the Test folder.

Sub GetAllFileNames()
Dim FolderName As String
Dim FileName As String
FolderName = "C:\\Users\\sumit\\Desktop\\Test\\"
FileName = Dir(FolderName & "\*.xls\*")

Do While FileName <> ""
    Debug.Print FileName
    FileName = Dir()
Loop

End Sub

While the DIR function returns the name of the first Excel file only, since we are calling it again in the loop, it goes through all the files and gives us the names of all the Excel files.

Hope you found this tutorial and the examples useful.

Let me know your thoughts in the comments section.

**You May Also Like the Following Excel Tutorials:**

*   [Excel VBA InStr Function](https://trumpexcel.com/excel-vba-instr/)
    .
*   [Excel VBA Split Function](https://trumpexcel.com/vba-split-function/)
    .
*   [Excel VBA TRIM Function](https://trumpexcel.com/vba-trim/)
    
*   [VBA LCASE Function.](https://trumpexcel.com/vba-lcase/)
    
*   [VBA UCASE Function.](https://trumpexcel.com/vba-ucase/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

8 thoughts on “VBA DIR Function – An Easy Explanation with Examples”
--------------------------------------------------------------------

1.  Gracias.
    
    [Reply](https://trumpexcel.com/vba-dir-function/#comment-41367)
    
2.  Below code is working for one particular file  
    How can I check multiple (.pdf) files whether exist in a folder or not? when I run the VBA code if the file exists it should return the value “file exists” or “File does not exist” in the next column where I define the file path.  
    I have more than two thousands pdf file in my folder could you please help to resolve this issue.
    
    Thanks in advance Dear Sumit.
    
    Sub CheckFileExistence()  
    Dim FileName As String  
    FileName = Dir(“C:UserssumitDesktopTestExcel File A.xlsx”)
    
    If FileName “” Then  
    MsgBox FileName  
    Else  
    MsgBox “File Doesn’t Exist”  
    End If
    
    End Sub
    
    [Reply](https://trumpexcel.com/vba-dir-function/#comment-14662)
    
3.  Hello,
    
    Can you please give a example of how to get the path of subfolder under the Main Folder?
    
    Thank you.
    
    [Reply](https://trumpexcel.com/vba-dir-function/#comment-12685)
    
4.  I use the following code in order to validate entered full filenames.
    
    Dir(sFullFileName) “”
    
    The problem is that some files (not all) stored in the Dropbox folder are not recognized as valid, even though the same file (with the same Full Name) opens the file opening procedure.
    
    Full filename example:  
    C:UsersandDropbox (ABC Croatia)blablatest\_file av.xlsm
    
    \*Note: This problem only manifests on one computer (new computer, win 10 pro 64 bit / Office 16 64 bit).  
    Non- Dropbox files are recognized.  
    Any suggestions?
    
    [Reply](https://trumpexcel.com/vba-dir-function/#comment-12479)
    
5.  Thanks for this explanation, I now understand some of my code which before I just accepted as “It works with it, don’t remove it”.
    
    Could I make a suggested change to your second example in the “example 2” section:
    
    “Sub CreateDirectory()  
    Dim PathName As String  
    Dim CheckDir As String
    
    PathName = “C:UserssumitDesktopTest”  
    CheckDir = Dir(PathName, vbDirectory)
    
    If CheckDir “” Then  
    MsgBox CheckDir & ” folder exists”  
    Else  
    MkDir PathName  
    ~ CheckDir = Dir(PathName, vbDirectory) ~  
    MsgBox “A folder has been created with the name” & CheckDir  
    End If
    
    End Sub”
    
    See the line of code between the ~~, I suggest this as without it the MsgBox does not return the name of the new folder created – works fine otherwise!
    
    [Reply](https://trumpexcel.com/vba-dir-function/#comment-12296)
    
6.  Hi, let’s say I have many files listed in different cells. From A1 to A50 y have 50 filenames and I want to check only those that exist
    
    [Reply](https://trumpexcel.com/vba-dir-function/#comment-11804)
    
    *   Just use DIR funtion on them. DIR return empty string if file dont exist
        
        [Reply](https://trumpexcel.com/vba-dir-function/#comment-11894)
        
7.  Hi, so clear and straight. Thanks for sharing with us.  
    Cheers.
    
    [Reply](https://trumpexcel.com/vba-dir-function/#comment-11644)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/vba-dir-function/#respond)

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