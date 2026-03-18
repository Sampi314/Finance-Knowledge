# Get the List of File Names from a Folder in Excel (with and without VBA)

**Source:** https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel

---

[Skip to content](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#below-title)

On my first day in my job in a small consulting firm, I was staffed on a short project for three days.

The work was simple.

There were many folders on the network drive and each folder had hundreds of files in it.

I had to follow these three steps:

1.  Select the file and copy its name.
2.  Paste that name in a cell in Excel and hit Enter.
3.  Move to the next file and repeat step 1 & 2.

Sounds simple right?

It was – Simple and a huge waste of time.

What took me three days could have been done in a few minutes if I knew the right techniques.

In this tutorial, I will show you different ways to make this entire process super fast and super easy (with and without VBA).

This Tutorial Covers:

[Toggle](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#)

**Limitations of the methods shown in this tutorial:** With the techniques shown below, you will only be able to get the names of the files within the main folder. You will not get the names of the files in the sub-folders within the main folder. Here is a way to get names of files from folders and sub-folders [using Power Query](https://trumpexcel.com/list-file-names-power-query/)

Using FILES Function to Get a List of File Names from a Folder
--------------------------------------------------------------

Heard of **FILES function** before?

Don’t worry if you haven’t.

It is from the childhood days of Excel spreadsheets (a version 4 formula).

While this formula does not work in the worksheet cells, it still works in [named ranges](https://trumpexcel.com/named-ranges-in-excel/)
. We will use this fact to get the list of file names from a specified folder.

Now, suppose you have a folder with the name – ‘**Test Folder**‘ on the desktop, and you want to get a list of file names for all the files in this folder.

Here are the steps that will give you the file names from this folder:

1.  In cell A1, enter the folder complete address followed by an asterisk sign (\*)
    *   For example, if your folder in the C drive, then the address would look like  
        C:\\Users\\Sumit\\Desktop\\Test Folder\\\*![Folder address in a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20436%2065'%3E%3C/svg%3E)
    *   If you are not sure how to get the folder address, use the following method:
        *   *   In the folder from which you want to get the file names, either create a new Excel Workbook or open an existing workbook in the folder and use the below formula in any cell. This formula will give you the folder address and adds an asterisks sign (\*) at the end. Now you can copy-paste ([paste as value](https://trumpexcel.com/convert-formulas-to-values-excel/)
                ) this address in any cell (A1 in this example) in the workbook in which you want the file names.
                
                **\=[REPLACE](https://trumpexcel.com/excel-replace-function/)
                (CELL("filename"),[FIND](https://trumpexcel.com/excel-find-function/)
                ("\[",CELL("filename")),[LEN](https://trumpexcel.com/excel-len-function/)\
                (CELL("filename")),"\*")**\
                \
                _\[If you have created a new workbook in the folder to use the above formula and get the folder address, you may want to delete it so that it doesn’t feature in the list of files in that folder\]_\
                \
2.  Go to the ‘Formulas’ tab and click on the ‘Define Name’ option.![File Names from a Folder in Excel - Define Name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20334%2094'%3E%3C/svg%3E)\
3.  In the New Name dialogue box, use the following details\
    *   Name: FileNameList (feel free to choose whatever name you like)\
    *   Scope: Workbook\
    *   Refers to: \=FILES(Sheet1!$A$1)![File Names from a Folder in Excel - Define Name Refres to](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20286%20204'%3E%3C/svg%3E)\
4.  Now to get the list of files, we will use the named range within an [INDEX function](https://trumpexcel.com/excel-index-function/)\
    . Go to cell A3 (or any cell where you want the list of names to start) and enter the following formula:\
    \
    \=[IFERROR](https://trumpexcel.com/excel-iferror-function/)\
    (INDEX(FileNameList,[ROW()](https://trumpexcel.com/excel-rows-function/)\
    \-2),"")\
    \
5.  Drag this down and it will give you a list of all the file names in the folder\
\
![Getting the File Names from a folder using the FILES function Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20539%20360'%3E%3C/svg%3E)\
\
**Want to Extract Files with a Specific Extension??**\
\
If you want to get all the files with a particular extension, just change the asterisk with that file extension. For example, if you want only excel files, you can use \*xls\* instead of \*\
\
So the folder address that you need to use would be **C:\\Users\\Sumit\\Desktop\\Test Folder\\\*xls\***\
\
Similarly, for word document files, use \*doc\*\
\
**How does this work?**\
\
FILES formula retrieves the names of all the files of the specified extension in the specified folder.\
\
In the INDEX formula, we have given the file names as the array and we return the 1st, 2nd, 3rd file names and so on using the [ROW function](https://trumpexcel.com/excel-row-function/)\
.\
\
Note that I have used **ROW()-2**, as we started from the third row onwards. So ROW()-2 would be 1 for the first instance, 2 for the second instance when the row number is 4, and so on and so forth.\
\
**Watch Video – Get List of File Names from a Folder in Excel**\
\
Using VBA Get a List of All the File Names from a Folder\
--------------------------------------------------------\
\
Now, I must say that the above method is a bit complex (with a number of steps).\
\
It’s, however, a lot better than doing this manually.\
\
But if you’re comfortable with using VBA (or if you’re good at following exact steps that I am going to list below), you can create a custom function (UDF) that can easily get you the names of all the files.\
\
The benefit of using a **U**ser **D**efined **F**unction (UDF) is that you can save the function in a personal macro workbook and reuse it easily without repeating the steps again and again. You can also [create an add-in](https://trumpexcel.com/excel-add-in/)\
 and share this function with others.\
\
Now let me first give you the VBA code that will create a function to get the list of all the file names from a folder in Excel.\
\
Function GetFileNames(ByVal FolderPath As String) As Variant\
Dim Result As Variant\
Dim i As Integer\
Dim MyFile As Object\
Dim MyFSO As Object\
Dim MyFolder As Object\
Dim MyFiles As Object\
Set MyFSO = CreateObject("Scripting.FileSystemObject")\
Set MyFolder = MyFSO.GetFolder(FolderPath)\
Set MyFiles = MyFolder.Files\
ReDim Result(1 To MyFiles.Count)\
i = 1\
For Each MyFile In MyFiles\
Result(i) = MyFile.Name\
i = i + 1\
Next MyFile\
GetFileNames = Result\
End Function\
\
The above code will create a function GetFileNames that can be used in the worksheets (just like regular functions).\
\
**Where to put this code?**\
\
Follow the steps below to copy this code in the VB Editor.\
\
*   Go to the Developer tab.![Developer tab in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20611%20135'%3E%3C/svg%3E)\
*   Click on the Visual Basic button. This will open the VB Editor.![Visual Basic button in the ribbon](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20611%20134'%3E%3C/svg%3E)\
*   In the VB Editor, right-click on any of the objects of the workbook you’re working in, go to Insert and click on Module. If you don’t see the Project Explorer, use the keyboard shortcut Control + R (hold the control key and press the ‘R’ key).![insert Module in VB Editor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20387%20363'%3E%3C/svg%3E)\
*   Double click on the Module object and copy and paste the above code into the module code window.![Copy code in module to get the file list name from a folder](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20820%20329'%3E%3C/svg%3E)\
\
**How to Use this Function?**\
\
Below are the steps to use this function in a worksheet:\
\
*   In any cell, enter the folder address of the folder from which you want to list the file names.\
*   In the cell where you want the list, enter the following formula (I am entering it in cell A3):\
    \
    **\=IFERROR(INDEX(GetFileNames($A$1),ROW()-2),"")**\
    \
*   Copy and paste the formula in the cells below to get a list of all the files.\
\
![Get List of File Names from Folder using VBA function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20588%20380'%3E%3C/svg%3E)\
\
Note that I entered the folder location in a cell and then used that cell in the **GetFileNames** formula. You can also hard code the folder address in the formula as shown below:\
\
**\=IFERROR(INDEX(GetFileNames("C:\\Users\\Sumit\\Desktop\\Test Folder"),ROW()-2),"")**\
\
In the above formula, we have used ROW()-2 and we started from the third row onwards. This made sure that as I copy the formula in the cells below, it will get incremented by 1. In case you’re entering the formula in the first row of a column, you can simply use ROW().\
\
**How does this formula work?**\
\
The GetFileNames formula returns an array that holds the names of all the files in the folder.\
\
The INDEX function is used to list one file name per cell, starting from the first one.\
\
IFERROR function is used to return blank instead of the #REF! error which is shown when a formula is copied in a cell but there are no more file names to list.\
\
Using VBA Get a List of All the File Names with a Specific Extension\
--------------------------------------------------------------------\
\
The above formula works great when you want to get a list of all the file names from a folder in Excel.\
\
But what if you want to get the names of only the video files, or only the Excel files, or only the file names that contain a specific keyword.\
\
In that case, you can use a slightly different function.\
\
Below is the code that will allow you get all the file names with a specific keyword in it (or of a specific extension).\
\
Function GetFileNamesbyExt(ByVal FolderPath As String, FileExt As String) As Variant\
Dim Result As Variant\
Dim i As Integer\
Dim MyFile As Object\
Dim MyFSO As Object\
Dim MyFolder As Object\
Dim MyFiles As Object\
Set MyFSO = CreateObject("Scripting.FileSystemObject")\
Set MyFolder = MyFSO.GetFolder(FolderPath)\
Set MyFiles = MyFolder.Files\
ReDim Result(1 To MyFiles.Count)\
i = 1\
For Each MyFile In MyFiles\
If InStr(1, MyFile.Name, FileExt) <> 0 Then\
Result(i) = MyFile.Name\
i = i + 1\
End If\
Next MyFile\
ReDim Preserve Result(1 To i - 1)\
GetFileNamesbyExt = Result\
End Function\
\
The above code will create a function ‘**GetFileNamesbyExt**‘ that can be used in the worksheets (just like regular functions).\
\
This function takes two arguments – the folder location and the extension keyword. It returns an array of file names that match the given extension. If no extension or keyword is specified, it will return all the file names in the specified folder.\
\
_Syntax: =GetFileNamesbyExt(“Folder Location”,”Extension”)_\
\
**Where to put this code?**\
\
Follow the steps below to copy this code in the VB Editor.\
\
*   Go to the Developer tab.\
*   Click on the Visual Basic button. This will open the VB Editor.\
*   In the VB Editor, right-click on any of the objects of the workbook you’re working in, go to Insert and click on Module. If you don’t see the Project Explorer, use the keyboard shortcut Control + R (hold the control key and press the ‘R’ key).\
*   Double click on the Module object and copy and paste the above code into the module code window.\
\
**How to Use this Function?**\
\
Below are the steps to use this function in a worksheet:\
\
*   In any cell, enter the folder address of the folder from which you want to list the file names. I have entered this in cell A1.\
*   In a cell, enter the extension (or the keyword), for which you want all the file names. I have entered this in cell B1.\
*   In the cell where you want the list, enter the following formula (I am entering it in cell A3):\
    \
    **\=IFERROR(INDEX(GetFileNamesbyExt($A$1,$B$1),ROW()-2),"")**\
    \
*   Copy and paste the formula in the cells below to get a list of all the files.\
\
![Get File Names from a Folder in Excel by Extension keyword](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20492%20336'%3E%3C/svg%3E)\
\
_**How about you?** Any [Excel tricks](https://trumpexcel.com/24-excel-tricks/)\
 that you use to make life easy. I would love to learn from you. Share it in the comment section!_\
\
**You May Also Like the Following Excel Tutorials:**\
\
*   [Filter cells with bold font format.](https://trumpexcel.com/filter-bold-font-formatting-in-excel/)\
    \
*   [How to Combine Multiple Excel Files into One Excel Workbook](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/)\
    .\
*   [Creating a Drop Down Filter to Extract Data Based on Selection](https://trumpexcel.com/extract-data-from-drop-down-list/)\
    .\
*   [Using VBA FileSystemObject (FSO) in Excel](https://trumpexcel.com/vba-filesystemobject/)\
    \
*   [Bulk Create Folders (and Subfolders) Using Excel List](https://trumpexcel.com/bulk-create-folders-subfolders-excel-list/)\
    \
\
Sumit Bansal\
\
Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)\
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!\
\
122 thoughts on “Get the List of File Names from a Folder in Excel (with and without VBA)”\
------------------------------------------------------------------------------------------\
\
1.  thanks a lot for this neat trick – but i couldn’t help improving it.\
    \
    simply writing =FileNameList gives the result, but as one file per column. however, adding the transpose function spits out the exact same list at your code =transpose(FileNameList), only you dont have to worry about placing the list at a specific row\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-17609)\
    \
2.  Awesome, Thanks. really helpful….Though i guess this works only for local drive folders. Is there a way to get the sever location work? As, if there are huge amounts of data it’s not wise to copy paste on my local drive and then do this. There should be a way to get the files names from the severs connected. Could you please help me out with that?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-14667)\
    \
3.  Fantastic, thanks many tonnes.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-14638)\
    \
4.  1\. select file in folder  \
    2\. hold shit and right click  \
    3\. select “copy as path”  \
    4\. paste in excel  \
    5\. Use find/replace to find “folder path” and replace with ” “\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-14622)\
    \
5.  Amazing solutions both with/without VBA.  \
    It works in my PC but I would like to know why is doesn’t work if the folder is in Onedrive?  \
    I´m using in cell A1 =REPLACE(CELL(“filename”),FIND(“\[“,CELL(“filename”)),LEN(CELL(“filename”)),”MyFolder/”)  \
    to obtain the folderpath that is in One drive and in B1=INDEX(GetFileNames(A1,1),””)\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-14140)\
    \
6.  This is awesome!! Thanks\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-14042)\
    \
7.  Super bro! worked out correctly for me (using the Excel formula). Many thanks for sharing your knowledge.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-13987)\
    \
8.  Very well. I like the code of vba. But i think you have some issue with ReDim Result(1 To MyFiles.Count) and with the ReDim Preserve Result(1 To i – 1). Because i run the code and 1 of files i can’t see.  \
    I think the best to change  \
    ReDim Result(0 To MyFiles.Count)  \
    ReDim Preserve Result(0 To i – 1).  \
    And after this all works.  \
    Thanks for great job.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-13439)\
    \
9.  i have more sub folder in one folder in need formula to get all folder name in excl\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-13409)\
    \
10.  Awesome!!! Thanks a lot, man! Got it done, what I needed to, following your video. Kudos to you!\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-12836)\
    \
11.  Is there a way to select file names based on their created date or last modified date? For example, I want files created in the last 24 hrs, 36 hrs, and 5 days?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-12831)\
    \
12.  Hi, this is great, but I need a list of the file names without their extension.. how to do this in one step?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-12297)\
    \
    *   You can use below formula\
        \
        \=IFERROR(LEFT(INDEX(FileNameList,ROW()-2),FIND(“.”,INDEX(FileNameList,ROW()-2))-1),””)\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-12420)\
        \
13.  is that any way to update excel list when one of the file in the folder delete ?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-12181)\
    \
14.  if one of the file in the folder delete this program can not update that and old file name remain in the list\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-12180)\
    \
15.  I find it faster to stick the folder path into a browser and then copy and paste into excel.  \
    But yes, even better when excel is set up to extract the data with a click of the button.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-12141)\
    \
16.  Great!  \
    Why doesn’t it work?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-12063)\
    \
17.  Hi, what i like to know is….  \
    i have a cell A1 in sheet1, and i like to output the highest file number of a folder in that cell.  \
    So when the folder name = userinvoice and the file name in pdf and xlsm is for example 20190001.pdf range 20190199 and 20190001.xlsm to 20190199 i like to display the value of the highest number in that folder to cell A1 in sheet1. In this example it would be 20190199.pdf and 20190199.xlsm\
    \
    Thank you very much for you effort.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-11824)\
    \
18.  Thanks very much. Saved me hours of manual entry!\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-11696)\
    \
19.  hi\
    \
    thankyou for the post\
    \
    I need a macro which can automate the work of renaming the pdf with amount within the pdf, instead of depending on a software\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-11610)\
    \
20.  I want to see Respective File Name with Save Time & Date…  \
    Please help for the Macro Code for the same.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-11556)\
    \
21.  Thank you for this wonderful post !!!\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-11458)\
    \
22.  I see the method for only listing specific extensions but is there a way to exclude extensions?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-11412)\
    \
23.  Thanks a lot for your tip. it’s helped me a lot.. 🙂 ..\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-11230)\
    \
24.  Thanks for the tip – worked like a charm!\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-11147)\
    \
25.  I need to get at the place to make a file name and go where I took pictures at yesterday\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-10951)\
    \
26.  Nice work\
    \
    it made our work very easy with our macro\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-10922)\
    \
    *   oh\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-11088)\
        \
27.  Amazing ! i’m mind blown here,  \
    I knew of to do it with marco but with a simple formula! wonderful!\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-10885)\
    \
28.  DEVE\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-10858)\
    \
29.  hoping someone could help, hoping I could automate my excel list using VBA or other procedure,\
    \
    For A, the idea is I have a PDF file, let say rev. 1,2,3,4 etc, and I will put it in one folder, what I need is I need to capture the latest revision with hyperlink using formula.\
    \
    For B, the idea is almost same as above except for one revision, let say rev. 01 and I will put it in one folder (same folder as formula A), what I need is I need to capture the exact revision with hyperlink using formula.\
    \
    I get this this formula but i don’t know how it will work- thanks in advance.\
    \
    A) Formula for latest “rev number” column\
    \
    \=IF(Bfile(“Z:3 M+ MWC3.1 M+\_RSSM+ (CC\_2015\_3A\_022)3\_DrawingsUSBM+ WS4\_Drawings”&MIDB($A50,11,3)&”PDF”&MIDB($A50,1,35)&”-“&LOOKUP(1,0/($K50:$DF50” “),$K50:$DF50)&”.PDF”),HYPERLINK(“Z:3 M+ MWC3.1 M+\_RSSM+ (CC\_2015\_3A\_022)3\_DrawingsUSBM+ WS4\_Drawings”&MIDB($A50,11,3)&”PDF”&MIDB($A50,1,35)&”-“&LOOKUP(1,0/($K50:$DF50” “),$K50:$DF50)&”.PDF”,LOOKUP(1,0/($K50:$DF50″ “),$K50:$DF50)),”\*”&LOOKUP(1,0/($K50:$DF50” “),$K50:$DF50))\
    \
    B) Formula for latest “rev number individual” column\
    \
    \=IF(Bfile(“Z:3 M+ MWC3.1 M+\_RSSM+ (CC\_2015\_3A\_022)3\_DrawingsUSBM+ WS4\_Drawings”&MIDB($A52,11,3)&”PDF”&MIDB($A52,1,35)&”-00.PDF”),HYPERLINK(“Z:3 M+ MWC3.1 M+\_RSSM+ (CC\_2015\_3A\_022)3\_DrawingsUSBM+ WS4\_Drawings”&MIDB($A52,11,3)&”PDF”&MIDB($A52,1,35)&”-00.PDF”,”00″),”\*00″)\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-10719)\
    \
30.  I only tried the first method and it works perfectly for me… thank you so much for saving me days of boring inputing!!\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-10592)\
    \
31.  How to get the file name list in Date Modified order in this excel workbook ??\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-10528)\
    \
32.  Umm its not working on MAC 🙁  \
    The formula you’ve provided (in column A) gives me this:  \
    /Volumes/Data/Reports/\*\
    \
    So the INDEX formula (in column B) gives #N/A  \
    🙁\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-10458)\
    \
    *   Remove the first “/” (the one before Volumes) and change the rest of the slashes to colons.\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-11235)\
        \
33.  I used the code above to obtain a list of files. The files names are as below:  \
    Diesel\_\_\_1234567\_\_\_NIR\_cuvette\_\_\_20180912\_234811.0  \
    Diesel\_\_\_1234567\_\_\_NIR\_cuvette\_\_\_20180912\_235510.0  \
    The code only pulls the first file for each sample and fails to list the second (or third file). Is there a way to correct for this? Thanks.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-10442)\
    \
34.  Hey,  \
    I have a ecxel sheet which have some product names, and also have a folder which have some pdf files named same as in cell data, like if cell A2 value is apple1, Pdf file name is apple1.pdf, i want to know which name file is missing, can we get that in excel somwhow..\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-10118)\
    \
35.  Hi Sumit,\
    \
    I want to list the names and duration of all videos in a folder and its subfolders using Excel VBA. From the code below I can get the duration of video files, but I can’t exclude all other files. This gives me a list of all the file names, which I don’t need. Also I am failing to loop through subfolders.  \
    What I want to achieve is for the macro to loop through all subfolders in the the given root folder and list only video names and duration in columns A and B.  \
    Some help with this is truly appreciated.  \
    Option Explicit\
    \
    Dim i As Long, SourceFldr  \
    Dim c As Range, rng As Range  \
    Dim sFile As Variant  \
    Dim oWSHShell As Object  \
    Dim WS As Worksheet  \
    Dim lRow As Long\
    \
    Sub GetDuration()\
    \
    Dim fldr As FileDialog  \
    Set fldr = Application.FileDialog(msoFileDialogFolderPicker)  \
    Set oWSHShell = CreateObject(“WScript.Shell”)\
    \
    With fldr  \
    .Title = “Select a Source Folder”  \
    .AllowMultiSelect = False  \
    .InitialFileName = oWSHShell.SpecialFolders(“Desktop”)  \
    If .Show -1 Then GoTo NextCode  \
    SourceFldr = .SelectedItems(1)  \
    NextCode:  \
    End With\
    \
    Dim oShell: Set oShell = CreateObject(“Shell.Application”)  \
    Dim oDir: Set oDir = oShell.Namespace(SourceFldr)\
    \
    i = ActiveSheet.Range(“A” & Rows.Count).End(xlUp).Row + 1\
    \
    For Each sFile In oDir.Items  \
    Cells(i, 1).Value = oDir.GetDetailsOf(sFile, 0) ‘File Name  \
    Cells(i, 2).Value = oDir.GetDetailsOf(sFile, 27) ‘File Lenght  \
    i = i + 1  \
    Next sFile\
    \
    Set oDir = Nothing  \
    Set oShell = Nothing\
    \
    End Sub\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9959)\
    \
36.  what about this one? I really need it 🙁 hope you can help  \
    [https://www.reddit.com/r/vba/comments/7g3el8/catalog\_files\_from\_folderssubs\_using\_excel\_vba/](https://www.reddit.com/r/vba/comments/7g3el8/catalog_files_from_folderssubs_using_excel_vba/)\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9933)\
    \
    *   [https://www.youtube.com/watch?v=mvYYZNUe\_9ss](https://www.youtube.com/watch?v=mvYYZNUe_9ss)\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9934)\
        \
37.  Wow! That’s ingenious and too much for free 😀 May Allah bless you brother. Thanks a lot.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9907)\
    \
38.  Hey! Sumit Bansal right? As a matter of fact you are my excel HERO. I’ve been following your blog for quite a while now and everything you thought was amazing. Even though I’m still a student, I know one day this knowledge is going to save me a lot of time. I thought I was an excel expert with my one semester training So I created a blog to publish my skills on ([http://excel-programming.com](http://excel-programming.com/)\
    ). But upon discovering your skills and experience I think I still have a a long way to go. Thank you very much for this blog.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9872)\
    \
39.  You are doing wonderful work Sumit to educate Excel users. God bless you.  \
    Please try the Excel Addin called ASAP Utilities by downloading it. There is a free (Home&Student) and paid version. File listing in Excel sheet of any directory and nested sub directories, with many properties of the files is so easy with many menu driven options (Menu-File & System-Item 24) This is just one of more than 300 utilities. It will be very useful for all Excel users and saves tons of time and effort. Current version is 7.4 and the link to the site is [http://www.asap-utilities.com/](http://www.asap-utilities.com/)\
     . I do not have any pesronel intrest in the product except to make it known to many Excel users to benifit in their work. It was developed by Bastien Mensink from Netherlands way back in 1999. I am using it since that time. Feed back on your experience is appreciated.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9862)\
    \
40.  Sumit this one deserves a kudos!!\
    \
    Some time back i was working on its VBA and m non VBA guy……….\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9861)\
    \
41.  I was also wondering if there is a way to extract additional properties information at the same time  \
    ie  \
    “File Name”  \
    “Created”  \
    “Owner”  \
    “Author”  \
    “Title”  \
    “Comments”  \
    “Tags”\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9859)\
    \
    *   This would be fabulous.\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-11236)\
        \
42.  nice. really interesting. thanks a lot\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9856)\
    \
43.  Hmm, nowadays I would go with a Power Query ( Get and Transform) solution. Read from folder, and delete all columns except file name. Save and load to table. No macro, no formula involved.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9852)\
    \
44.  Thank you for this repost. Is there a way to list folders in a directory?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9850)\
    \
    *   I just saw a post below that this function does not work with folders. Too bad 🙁\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9851)\
        \
45.  Since it has not been corrected I assume that it has not been reported yet. The first version of this formula: =IFERROR(INDEX(FileNameList,ROW()-2,””) should actually be: =IFERROR(INDEX(FileNameList,ROW()-2),””). The trick won’t work until the right formula is used.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9845)\
    \
    *   Thanks for pointing out Charles.. have corrected it!\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9847)\
        \
46.  Hi Sumit, Great trick. Thanks a lot. However I was wondering if there is a way to extract the file path as well along with the file name\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9786)\
    \
47.  I copied everything exactly but my cells are blank in the B column and it doesn’t populate the file names. any reason why? Also I’m using office 2010.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9764)\
    \
    *   I figured out the issue, i didn’t have a slash before the asterisk \* at the end. But I have one more question. Can this be used to get a value from a cell in these docs as well? e.g. I get a list of all docs in a given folder, can I then get a value from a cell in each of those docs if its all the same cell in each doc?\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9767)\
        \
48.  Hi  \
    Was wondering if there is a way to extract properties information at the same time  \
    ie  \
    “File Name”  \
    “Created”  \
    “Owner”  \
    “Author”  \
    “Title”  \
    “Comments”  \
    “Tags”\
    \
    Much appreciated\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9723)\
    \
49.  Hi Sumit, great tutorial. I used this because files are constantly being added to a specific folder. This allows for the names of those new folders to show. Since I do not know the names of the new files that will be created I was hoping to then use the results of this in an external reference formula. Do you know if this is possible?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9448)\
    \
50.  Please take a look at [https://isystems-it.azurewebsites.net/2017/04/23/fs-utilities/](https://isystems-it.azurewebsites.net/2017/04/23/fs-utilities/)\
      \
    for a more comfortable approach.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9302)\
    \
51.  One method I have used before uses the command prompt. Navigate to the folder you want to extract file names from. Type (dir /b > “sample.txt”) minus the parenthesis. This will create a text file in the same directory that you can then open in Excel for further processing.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-9008)\
    \
52.  how to have excel list all the file in one row instead of using multiple rows\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-8943)\
    \
53.  dear sir,  \
    how can i Get a List of File Names from a Folder in Excel without extension like . jpg, .pdf\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-8835)\
    \
54.  Amazing! Thanks for this Great Trick!!!\
    \
    Question: When the New File Names come in, they Start Over from the Top-Shifting File Names Down, how can I get them to come in at the bottom of the list (based on date/time modified)?\
    \
    Make File Name Hyperlink? If I Select the Column with your Formula, Insert Hyperlink and Add Folder Location, this links them to the folder, but how can I make it open the file directly? Also If you can Help: I have a Folder Filled with Email Messages (.msg Files) that I am keeping a Running List of in Excel and have to manually enter data from each Email such as Name (Email Address before @) + Company (Email Address after @), Date Received etc. – Is there a way to Auto Populate this information into Excel from the .msg File following the Automated File Name you have created here?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-4194)\
    \
55.  I have a single folder with multiple sub-folders each with multiple files, can I extract at the highest folder level?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-3265)\
    \
56.  Hi, Is there a way i can get the time the file is created in addition to the file name?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-3252)\
    \
57.  Hei Sumit. I got Folder name in A1. But INDEX will not work properly, I get only #N/A, (I define A1 as “NM”)  \
    Can you plz look at screenshot and give me some guide lines that where i do wrong?  \
    And my required folder is on Sharepoint.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-3201)\
    \
58.  Amazingly quick response. I will re-check. Thank you.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2834)\
    \
59.  I tried Getting a List of File Names from a Folder in Excel. Why did I get #NAME? instead of the name of the first file? I like your video lesson. Thank you.  \
    Husen Kabeer, [myaquadome@yahoo.com](mailto:myaquadome@yahoo.com)\
    \
    c:This PCDocumentsHusen Data Files – 2014Word\*  \
    \=INDEX(FileNameList,1)  \
    #NAME?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2832)\
    \
    *   Hello Husen.. Check the named range reference. It seems your named range is not referring to the cell that has the folder path.\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2833)\
        \
60.  Thank you very much. This is amazing ..:)\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2691)\
    \
    *   Thanks for commenting.. Glad you liked it 🙂\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2692)\
        \
61.  Sumit, is there a way for this formula to look within a series of sub-folders for the same results.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2680)\
    \
    *   Thanks for commenting David.. With this method, you can only get file names from a specified folder\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2682)\
        \
62.  Hi, Sumit  \
    Googled for a few minutes just now. I love your work. As a newbie you’ve helped me so much but for the life of me I just couldn’t get this working. Found an alternative method that actually lists the file names as hyperlinks. Thought I’d share the link here, in case you or your other fans/followers were interested –\
    \
    [http://www.extendoffice.com/documents/excel/627-excel-list-files.html](http://www.extendoffice.com/documents/excel/627-excel-list-files.html)\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2462)\
    \
63.  if this done with a folder that gets updated a lot, will this auto update with the new file names or will you have to start all over\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2456)\
    \
    *   It would automatically update if you open the workbook or you press F9 (to force a calculation), or even if you make any change in the worksheet.\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2457)\
        \
        *   Thanks, its working just the way that i was wanting it to\
            \
            [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2458)\
            \
        *   Hello Sumit, thank you for your post. Made my life easier. Never the less I still have a problem with the update. It does not update automatically. I have to drag the formula again each time I open the document, or either double click the cell to updated itself. Do you know what I might do wrong? For your information I used your formula in combination with other formulas as bellow :\
            \
            \=LEFT($B$3;LEN($B$3)-1)&IFERROR(INDEX(FileList0916;ROWS($B$4:B33));””)\
            \
            [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-3871)\
            \
64.  Hi. I have been here for more than an hour and for some reason I can’t get this to work. Know I’m going to love it and use it a lot, once I can get the first one working. Any chance you can take a look at mine and tell me what I’m doing wrong? I would so much appreciate it!\
    \
    [https://www.dropbox.com/s/ex6rtxpgr2twyne/Excel%20Index.xlsx?dl=0](https://www.dropbox.com/s/ex6rtxpgr2twyne/Excel%20Index.xlsx?dl=0)\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2451)\
    \
    *   Hello Brenda. You have created a named range with the name “ExcelList”, while the formula uses “FileNameList”. Change the formula to =IFERROR(INDEX(ExcelList,ROWS($B$1:B1)),””)\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2452)\
        \
        *   Thanks so much for replying. And so quickly! Awesome. Unfortunately that didn’t work.\
            \
            [https://www.dropbox.com/s/ebd0bbh1exwkw8y/Excel%20Index.xlsx?dl=0](https://www.dropbox.com/s/ebd0bbh1exwkw8y/Excel%20Index.xlsx?dl=0)\
            \
            [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2453)\
            \
            *   Are you using the formula to get the folder address. Use this formula =REPLACE(CELL(“filename”),FIND(“\[“,CELL(“filename”)),LEN(CELL(“filename”)),”\*”)\
                \
                It shouldn’t look something as shown in your spreadsheet. Also, make sure the excel file (in which you are extracting the file names) is saved in the same folder.\
                \
                [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2454)\
                \
                *   Morning,  \
                    At it again this am. Losing my mind. Want this so bad and I just can’t get it to work. Tried everything. Must be something really small and stupid hanging me up. Heading to work. Little bit OCD – lol. I will get back at it when I get home but not too optimistic.\
                    \
65.  hi sumit! i followed the instructions but all i got was a blank cell..\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2430)\
    \
66.  Hi  \
    The function of FILES does not exist in my version of excel 2010! May be it originated from some Add-Ins?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2219)\
    \
67.  That is an awesome way. Thanks a lot!!…  \
    Also, is there a way to get the list of all the folders,subfolders and filenames along with file size and modification date columns.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2141)\
    \
    *   Thanks for commenting.. Using this method, you can only get file names from a specified folder\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2681)\
        \
68.  Another way to get the directory.  \
    Portuguese version of formula =INFORMAÇÃO(“DIRECTÓRIO”)  \
    I guess in English will be =INFO(“DIRECTORY”)  \
    Even easier!\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2107)\
    \
69.  Hi Sumit, thanks a lot for that.. is there any way I can also get the tabs within each excel file that I am looking up in a drive to populate in the columns next to file names? Please let me know it will be really helpful\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2100)\
    \
    *   Hi Bharat. You won’t be able to get tab names using the FILES function. For that, you would need to resort to a VBA code\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2104)\
        \
        *   HI Sumit, thanks for the quick response. is there anyway you can help with that code? I have been trying to search for it online but nothing seems to pop up.\
            \
            [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2106)\
            \
70.  Never seen this trick before. Great stuff.\
    \
    i think this formula should also work for retrieving the file path, looks shorter 🙂  \
    \=LEFT(CELL(“filename”),FIND(“\[“,CELL(“filename”))-1)&”\*”\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2067)\
    \
    *   Thanks for sharing the formula Victor.. Yours is much better 🙂\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2069)\
        \
71.  I was able to follow your instructions, but when i save it and go back it isnt there it just has name#. I am not familiar with Macros and it ask me to save Macros-Free and when I do my list isnt there. how can I save it. apologize in advance.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2054)\
    \
    *   Hi Elisa.. Thanks for commenting. Try and save your file as a macro-enabled workbook (with .xlsm extension) and it would work. Since FILES is an old macro formula, it requires the workbook to be saved in .XLSM format. And don’t worry about not knowing macros, it would still work\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2055)\
        \
72.  Awesome solution thank you! However I could only register 256 files (rows). After that I get #¡REF!. Do you know a way to make it work for larger number of files. I need it for 2.000 files aprox. Thank you again. Jacobo\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2042)\
    \
    *   Thanks for commenting.. Could you share the sample file you are using. Since FILES is an old formula it may have some limitations, need to check on it.\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2043)\
        \
73.  Once I wanted to do the same so I wrote an Excel Add-in for doing that.\
    \
    It can get filenames, folders, file extensions and other information regarding files.\
    \
    This tool can write up to excel limit number of rows in just a few minutes.\
    \
    In a stress test I did, I got more than 1,000,000 file names in just about 3 minutes.\
    \
    Here is a link to try:\
    \
    [http://excel.gegprifti.com](http://excel.gegprifti.com/)\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2041)\
    \
74.  Dear Sumit,  \
    Suppose i want to do same for folder name than how we can do?\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2039)\
    \
    *   Hi, I am waiting for your revert.\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2065)\
        \
        *   Hi Narayandatta.. FILES can not be used to get the folder names within in folder. It only works for files that have an extension\
            \
            [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2066)\
            \
75.  This was a great time saver Sumit, thanks. ? is there a way to make them a hyperlink without going through every single one?  \
    Thanks\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-2008)\
    \
76.  fantastic\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1672)\
    \
    *   A formula that only works in named range?!!..this is great find.\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1727)\
        \
77.  That is really useful, thanks very much!\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1670)\
    \
    *   Thanks for commenting.. Glad you found this useful 🙂\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1689)\
        \
78.  Interesting.\
    \
    Before dragging down, we may use\
    \
    \=COUNTA(FileNameList)\
    \
    to get a sense of how far we need to go down.\
    \
    btw, another approach in getting the directory for consideration.\
    \
    \=REPLACE(CELL(“filename”),FIND(“\[“,CELL(“filename”)),LEN(CELL(“filename”)),”\*”)\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1660)\
    \
    *   Thanks for commenting.. Your formula is much better 🙂\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1661)\
        \
79.  Thanks this will be useful  \
    We can also do the same thing with Power Query\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1659)\
    \
80.  Wow, this is great. Easier than the VBA code I wrote to do the same thing!\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1656)\
    \
    *   Yeah.. this old macro4 formula does makes it quite easy to do this\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1658)\
        \
81.  you save my life.\
    \
    thnx a lot for such a great trick.\
    \
    [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1655)\
    \
    *   Thanks for the comment. Glad you liked it 🙂\
        \
        [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1657)\
        \
        *   Dear Sumit,\
            \
            Is “Files” function is valid only Excel 2013.\
            \
            I am trying to make it in Excel 2010 but could not find the Turkish of “Files” in Excel?\
            \
            Do you have an idea?\
            \
            [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1693)\
            \
        *   Dear Sumit,\
            \
            I am dying here to try above trick but still waiting your reply about the function FILES ?  \
            🙁\
            \
            [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1695)\
            \
            *   Hey.. this formula is valid for all versions of Excel. However, I could not find its equivalent for Turkish Excel. Since it’s an old function, even the help is not available for it now.\
                \
                [Reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#comment-1699)\
                \
                *   Dear Sumit,\
                    \
                    Thnx for your reply.\
                    \
                    I made it but unfortunately when I drag down, it gives only the first file name ?\
                    \
                    Do you have any idea?\
                    \
                *   It seems the second argument of INDEX is not changing. Can you try changing it to see if it work. Also, would be great if you could share the file (a link to dropbox or onedrive)\
                    \
                *   Hi again,\
                    \
                    I changed all names, but stll same…\
                    \
                    Here it is:\
                    \
                    [https://www.dropbox.com/sh/inwriaq0ttocwzu/AACSB1-ox5z6Z5rm2MaxsYpva?dl=0](https://www.dropbox.com/sh/inwriaq0ttocwzu/AACSB1-ox5z6Z5rm2MaxsYpva?dl=0)\
                    \
                *   I think I got the issue.. Replace the function ROW with ROWS, and it should work for you. Hope this helps.\
                    \
                *   omg!  \
                    how dumb! I am…  \
                    Thnx a lot and sorry for wasting your time!\
                    \
                *   Glad it worked 🙂\
                    \
                *   I need those macros in Polish, and find this way:\
                    \
                    In VBA I write and run simple macro like:\
                    \
                    Sub Makro1()  \
                    ActiveWorkbook.Names.Add Name:=”Test”, RefersToR1C1:=”=FILES(Sheet1!R2C1)”  \
                    End Sub\
                    \
                    Then in Name Menager I have 4.0 Macro Function name in my Excel language (for my it’s Polish)\
                    \
\
### Leave a Comment [Cancel reply](https://trumpexcel.com/list-of-file-names-from-a-folder-in-excel/#respond)\
\
Comment\
\
Name Email Website\
\
  \
\
![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)\
\
**FREE EXCEL E-BOOK**\
\
Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster\
\
   \
\
Name \
\
Email \
\
SEND ME THE EBOOK\
\
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)\
\
**FREE EXCEL E-BOOK**\
\
Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster\
\
   \
\
Name \
\
Email \
\
SEND ME THE EBOOK\
\
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)\
\
**FREE EXCEL E-BOOK**\
\
Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster\
\
   \
\
Name \
\
Email \
\
SEND ME THE EBOOK\
\
![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)\
\
**FREE EXCEL E-BOOK**\
\
Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster\
\
   \
\
Name \
\
Email \
\
SEND ME THE EBOOK\
\
![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)\
\
**FREE EXCEL E-BOOK**\
\
Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster\
\
   \
\
Name \
\
Email \
\
SEND ME THE EBOOK\
\
![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)\
\
**FREE EXCEL E-BOOK**\
\
Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster\
\
   \
\
Name \
\
Email \
\
SEND ME THE EBOOK