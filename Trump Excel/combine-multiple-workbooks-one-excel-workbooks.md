# How to Combine Multiple Excel Files into One Excel Workbook

**Source:** https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks

---

[Skip to content](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#below-title)

I got a call from a friend who wanted to combine multiple Excel files into one Excel workbook. He had a lot of files in a folder and he wanted to get all the worksheets from all the workbooks into one single workbook.

While this can be done manually, it would be time-consuming and error-prone.

However, a simple VBA code can do this in a few seconds.

![Combine Multiple Workbooks into One Excel Workbook - Image Orange](https://trumpexcel.com/wp-content/uploads/2016/05/Combine-Multiple-Workbooks-into-One-Excel-Workbook-Image-Orange.png)

Combine Multiple Excel Files into One File
------------------------------------------

Here is the code that can combine multiple Excel workbooks in a specified folder into a single Excel workbook:

Sub ConslidateWorkbooks()
'Created by Sumit Bansal from https://trumpexcel.com
Dim FolderPath As String
Dim Filename As String
Dim Sheet As Worksheet
Application.ScreenUpdating = False
FolderPath = Environ("userprofile") & "DesktopTest"
Filename = Dir(FolderPath & "\*.xls\*")
Do While Filename <> ""
 Workbooks.Open Filename:=FolderPath & Filename, ReadOnly:=True
 For Each Sheet In ActiveWorkbook.Sheets
 Sheet.Copy After:=ThisWorkbook.Sheets(1)
 Next Sheet
 Workbooks(Filename).Close
 Filename = Dir()
Loop
Application.ScreenUpdating = True
End Sub

How to Use this Code?
---------------------

Here are the steps to use this code:

*   Put all the Excel files that you want to combine into a folder. For the purpose of this tutorial, I have created a folder named Test and have six files in it (4 Excel workbooks and 1 Power Point and Word each).![Combine Multiple Workbooks into One Excel Workbook - test Folder](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20636%20225'%3E%3C/svg%3E)
*   Open a new Excel workbook.
*   Press ALT + F11 (or go to Developer –> Code –> Visual Basic). This will open the Visual Basic Editor.
*   In the VB Editor, in the Project Editor, right-click on any of the objects for the workbook and go to Insert –> Module. This will insert a module for the workbook.![Combine Multiple Excel files into One Excel Workbook - insert module](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20422%20342'%3E%3C/svg%3E)
*   Double click on the module. It will open the code window on the right.
*   Copy and paste the above code into the code window.![Combine Multiple Excel files into One Excel Workbook - code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20543%20236'%3E%3C/svg%3E)
*   In the code, you need to change the following line of code:
    
    FolderPath = Environ("userprofile") & "**DesktopTest**"
    
    In this line, change the part in double quotes (highlighted in orange) with the location of the folder in which you have the files that you want to combine. In the code used above, the folder is on the Desktop. In case you have it in some other location, specify that path here.
    
*   Place the cursor anywhere in the code and click on the green play button in the Toolbar options (or press the F5 key).![Combine Multiple Workbooks into One Excel Workbook - run code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20495%20107'%3E%3C/svg%3E)

This will run the code and all the worksheets from all the Excel files in the folder would get consolidated into a single workbook.

![Combine Multiple Excel files into One Excel Workbook - demo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20360'%3E%3C/svg%3E)

How this Code Works?
--------------------

*   The code uses the [DIR function](https://trumpexcel.com/vba-dir-function/)
     to get the file names from the specified folder.
*   The following line assigns the first excel file name to the variable ‘Filename’.  
    Filename = Dir(FolderPath & “\*.xls\*”)
*   Then the [Do While loop](https://trumpexcel.com/vba-loops/)
     is used to check whether all the files have been covered.
*   Within the ‘Do While’ loop, ‘For Each’ loop is used to [copy all the worksheets](https://trumpexcel.com/how-to-copy-a-worksheet-in-excel/)
     to the workbook in which we are running the code.
*   At the end of the Do Loop, following line of code is used: Filename = Dir(). It assigns the next Excel file name to the Filename variable and the loop starts again.
*   When all the files are covered, DIR function returns an empty string, which is when the loop ends.

Here is an explanation of the DIR function in the [MSDN library](https://msdn.microsoft.com/en-us/library/office/gg278779(v=office.15).aspx)
:

_**Dir** returns the first file name that matches pathname. To get any additional file names that match pathname, call **Dir** again with no arguments. When no more file names match, **Dir** returns a zero-length string (“”)._

Have you ever tried something of this sort using VBA? Do share what you did and we all can learn from it.

Save a Crazy Amount of Time Using VBA. Check out the **[Excel VBA COURSE](https://trumpexcel.com/excel-vba-course/)
**.

**You May Also Like the Following Excel Tutorials:**

*   [How to Combine Data from Multiple Workbooks into One Excel Table (using Power Query)](https://trumpexcel.com/combine-data-from-multiple-workbooks/)
    .
*   [Create Summary Worksheet with Hyperlinks in Excel](https://trumpexcel.com/create-summary-worksheet-in-excel/)
    .
*   [How to Create and Use an Excel Add-in](https://trumpexcel.com/excel-add-in/)
    .
*   [How to Run a Macro](https://trumpexcel.com/run-a-macro-excel/)
    .
*   [Useful Excel Macro Examples](https://trumpexcel.com/excel-macro-examples/)
    .
*   [VBA Copy Sheet](https://trumpexcel.com/excel-vba/copy-sheet/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

98 thoughts on “How to Combine Multiple Excel Files into One Excel Workbook”
----------------------------------------------------------------------------

1.  Brilliant thanks!
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-14720)
    
2.  Highly frustrating – simply can’t get the damn thing to work….
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-14712)
    
    *   I had this problem as well but fixed it as follows,
        
        1\. Save the document as .xlxm  
        2\. Make sure you have a “/” at the end of your directory path
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-14721)
        
        *   sorry .xlsm
            
            [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-14722)
            
3.  The code works but the filepath string requires all of the “” in the complete file path. For example: C:UsersUser1DesktopExcelfiles\*.xls\*. This best way to solve this is:
    
    When you modify the FolderPath = Environ(“userprofile”) & “DesktopTest” make sure you include the pre and post forward slashes “” to the folder path containing the excel sheets to be imported.
    
    When you are debugging right click on the Folderpath and Filename variable and set them to the Watchlist with the Break when value changes box checked. When you run the program you can verify those two variables are updating correctly.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-14506)
    
4.  Thanks so much, worked perfectly.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-14335)
    
5.  Not working,It is showing debugg at Filename = Dir(FolderPath & “\*.xlsx\*”).  
    Can you please provide a fix
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-14312)
    
6.  For this code to work some of you will likely need more than the suggested file path of:
    
    FolderPath = Environ(“userprofile”) & “DesktopTest”
    
    Environ(“userprofile”) will only provide the first part of a filepath. In my case it was: C:UsersWF. There were several subfolders “along the path” before getting to the folder I used for the files to be combined. Use this example as the path to the correct folder:
    
    folderpath = “C:UsersWFDocumentsFolder1Folder2Folder3FolderWithFiles
    
    For a convenient way to get the correct path use this code to place the path on a worksheet. Then copy/paste into the sub procedure.
    
    Sub Path\_FileName()  
    Dim strPath As String  
    strPath = ActiveWorkbook.FullName  
    ActiveCell.Value = strPath  
    End Sub
    
    Make this adjustment if you need to. This is some very useful code.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13937)
    
7.  I was getting error 52 as well.
    
    “DESKTOP TEST” = LOCATION OF FILE
    
    I changed this string of code (moved the parenthesis) from the below and it worked:
    
    CHANGED FROM  
    FolderPath = Environ(“userprofile”) & “DesktopTest”
    
    CHANGED TO  
    FolderPath = Environ(“userprofile” & “DesktopTest”)
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13775)
    
8.  Big thank you!! I had found various other versions of this code but this is the first one that worked for my version of Excel. Needed to combine over 30 spreadsheets and it saved me lots of time!
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13761)
    
9.  I am getting error 52 when I run the code.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13698)
    
10.  Thanks alot. It was very helpful. I am a options trader needed it to backtest the things. So thanks again. Let me know how can I give it back to you.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13645)
    
11.  Many thanks for this! Forty spreadsheets … into one without copy/pasting each sheet. Phew.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13634)
    
12.  how can i add in the header in the active worksheet before I run this code? or i can do it at the same time?
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13571)
    
13.  I have followed the instructions carefully but i get an error of Bad filename 52
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13461)
    
14.  Great code and works! One thing though that may be tripping people up. The string Filename also is part of the Workbooks.Open Filename:= command. Anyone having issues with the Filename variable should try attempting to rename the string to something else to avoid issues. Least what I had to do for this to properly work for me.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13393)
    
    *   I am having filename issues
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13699)
        
15.  fabulous!!! works amazing
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13262)
    
16.  Filename = Dir(FolderPath & “\*.xls\*”)
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13257)
    
17.  Sorry not working for me, gives me error on file dir.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13256)
    
18.  Cant combine multiple files…no error shown,can we send you the sample files-please share your email id
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13004)
    
19.  Worked for me. Thank you so Much! saved me much time for a work project. Thank you so much for uploading
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-12949)
    
20.  Like so many in this thread, this did not work for me – suggest it is taken down as a waste of valuable time!
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-12688)
    
21.  That worked amazing! Thank you, thank you, thank you!
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-12622)
    
22.  Heaps thanks worked just perfect.. you saved my time.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-12195)
    
23.  Hi , how can I combine the first worksheet of multiple Excel workbooks in a specified folder into a single Excel workbook ?
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-12022)
    
24.  I have used this code but its is creating multiple tabs for the sheet with same name like Name (1); Name(2); Name(3)
    
    Any solution
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11776)
    
25.  I am getting Run-time error Bad file name or number  
    I have used the path “H:Sheets”  
    Please advise
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11639)
    
    *   Delete the :
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-12787)
        
26.  it didnt work, this came back as an error  
    Filename = Dir(FolderPath & “\*.xls\*”)
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11634)
    
    *   have you solve this case ? I have same error …
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11769)
        
    *   try putting “” at the end of folder path (note that in dos, between file name and the directory there has to be “” sign
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13263)
        
27.  I want to combine individual timesheets into one master file, but the t/s are protected. Will I still be able to enter data and save it?
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11621)
    
28.  I am getting debug in filename. Please help me
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11601)
    
    *   Remove the Environ(“userprofile”) & from your code. This just tells VBA to go to folders under your user. But if you already have something like “C:UsersVarunDocuments” in the folder path, this will throw the error you get.
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11609)
        
29.  Excellent !!!
    
    Is it possible to name the sheets accordingly to their filenames?
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11598)
    
    *   Hi, i am getting debug in Filename.  
        Can you help me ?
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11600)
        
30.  Hie I have many workbook and i want to combine every second sheet from workbook together
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11544)
    
31.  Thanks for this tip Sumit………….
    
    But it create multiple sub sheets of multiple files…what should to do if we need all multiple files into only one single sub sheet and i also want that the data copy should be in sequence
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11535)
    
32.  Not working for me. I followed all the steps mentioned above.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11472)
    
    *   juse WPS office
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-12745)
        
    *   sorry i just want to say. Use WPS Office
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-12746)
        
33.  error 1004:  
    method ‘copy’ of object ‘ \_worksheet’ failed
    
    Debug =
    
    Sheet.Copy After:=ThisWorkbook.Sheets(1)
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11344)
    
    *   Same issue with me.
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13620)
        
34.  not working this coding,  
    error on  
    Filename = Dir(FolderPath & “\*.xls\*”)  
    kindly slove this problem
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11326)
    
    *   I am getting the same error
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11602)
        
    *   I used ” ” and entered folder path where the file is located inside the quotation and it worked for me.
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-13258)
        
35.  Hi I need some help in developing an extinction tool. Where 80 Percent can be done through formulas. Bit I need some help on remaining things. Will appreciate your help.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11205)
    
36.  not working 🙂  
    need smart support
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11179)
    
    *   I am making an estimation tool. The first method worked, but that’s not dynamic.  
        I want the list to refresh if a new file is added to the folder.
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11206)
        
37.  Thanx a lot !!!!! Saved lot of time
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11161)
    
38.  Super!!!  
    Saved lot of time
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11020)
    
39.  hi can i update daily log sheets / material use sheet, warehouse sheet and combining into 1 for KPI ? daily folks save in same folder with different date and shift
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11015)
    
40.  Hi Sumit  
    It does’nt work for me after peressing the F5 I got ERE “BAD FILE NAME”  
    As I see numer of people here have had the same ERE plz explain the reason for it
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-10954)
    
41.  What about copying different sheets from different excel files to one sheet by adding the new data to the old one ?
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-10850)
    
42.  Thank you so much for this VBA code! Excellent time-saver!
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-10831)
    
43.  Hi, I have to copy 4 sheets from different excel files in one excel.  
    Excel name in which i have to copy my data= Summary
    
    Data copy from below listed excels  
    Excel 1= Los Angeles CCAP ASE Job Log Backup 15-11-18  
    Excel 2= Anaheim CCAP ASE Job Log Backup 15-11-18  
    Excel 3= BAY-North CCAP ASE Job Log Backup 15-11-18  
    Excel 4= San Diego CCAP ASE Job Log Backup 15-11-18
    
    Now from every file, I have to copy only 1 sheet. names of sheets are mentioned below.  
    Excel 1 sheet name= LA  
    Excel 2 sheet name= Anaheim  
    Excel 1 sheet name= SD  
    Excel 1 sheet name= BayNorth
    
    Please help I have to submit a report to my manager.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-10758)
    
44.  I have over 2000 files to combine. I did a test run of 100 and the result was garbage.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-10724)
    
    *   Did you ever find a solution? I am in a similar boat.
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-12528)
        
45.  how to combine three workbook in one workbook easy and quick
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-10701)
    
46.  I am getting error mentioning Run time error 52. Bad file name or number. For your information I have saved the files on my Desktop with a folder name as Test. Please suggest
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-10628)
    
47.  I am getting an error as bad file name,can someone help me with this error,would be really thankful!
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-10583)
    
48.  It doesn’t work for me, I have “bad file name or number”. do you know how to fix it?
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-10567)
    
49.  helpful
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-10538)
    
50.  very useful ,I like it very much !
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-10473)
    
51.  When i press f5, nothing happens -! can anyone pls help ?
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-10468)
    
52.  Attempting with CSV files. =) will let you know.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-10140)
    
53.  I have a query . Suppose I have to merge 652 workbooks into one. The filenames are 1.xlsx to 652.xlsx and i want to merge them in ascending order of their filenames only . Will this code merge it according to their sorted name in the folder or not ??
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-9987)
    
54.  Hi Sumit, need your assistance with the above macro.
    
    This works good if you want to combine multiple sheets in 1 workbook.
    
    I need a solution where the following steps need to be done :
    
    1\. There are around 4000 employees and the workbook will be each employee code wise  
    2\. There are 18 folders with workbooks with 1 worksheet for each employee.. there is a possibility that for an employee one of the workbooks will not be there  
    3\. The macro should create a workbook with the emp code then across the 18 folders should check whether workbook is available for the employee ID and if yes  
    4\. Copy and paste it in the created workbook and save.  
    5\. Additionally there are 3 workbooks by default which need to be added for all employees
    
    What i do not know to edit the above macro is:
    
    1\. How do i build a For loop for an employee list  
    2\. If there is no specific excel workbook in one of the folder then it should not throw an error
    
    Please help. I can communicate on your official email id too and will be happy if you can provide a solution at the earliest even if it is chargeable.
    
    Regards
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-9837)
    
55.  That’s great thanks. It would be even better if it named the sheets after the original file names.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-9738)
    
    *   yes
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-11596)
        
56.  Still usable. You need to place a “/” after your path if you copy it in.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-9605)
    
    *   Thank you, this worked along with removing the Environ(“userprofile”) & code segment for FolderPath where I was able to combine 13 single sheet Excel files that I placed in a test folder on a mapped network drive (example: FolderPath = “Z:20198 – AUGMeeting AttendeesTest/”
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-12425)
        
57.  The code is really work for me using in Excel 2016 after few experiments.  
    Some tips for those who are struggling about getting error message:  
    1) The code is worked for both xls and xlsx, don’t need to modify it.  
    2) The code ONLY works for worksheet, do try to move chart, you will get error. (anyone know how to move all together?)  
    3) Try 1 or 2 workbooks first to see whether it is work for you or not.
    
    Hope these help you all 🙂
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-9550)
    
58.  Wow first one actually worked:)
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-9424)
    
59.  This did not work. Yes it combines 2 workbooks, but it destroys the functionality of the formulas in the process. Now, this could be me making some bad choices when it prompts me while the macro is running. Idk. Example: while macro was running I got several “name ‘use lists’ already exists. Yes to keep no to rename it something else” messages (sub ‘use lists’ with various other names). And regarding other formulas being destroyed, example: a simple =’TAB’!A1&” “&’TAB’!A2 type of formula is now bloated with file directory info. So it reads like:  
    \=’C:UserEtcpathTAB’!A1&” “&’C:UserEtcpathTAB’!A2  
    That last one I can fix by deleting the stupid file directory info, formula by formula. As for the whole yes or no to renaming stuff that already exists… I’m at a loss.
    
    TL;DR I don’t know VBA & this formula didn’t work in my scenario.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-9375)
    
60.  Sumit Bansal you Rock <3
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-9356)
    
61.  Thanks for posting this! I’m getting “Run-time error ’52’: Bad file name or number” – anyone know how I can overcome this?
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-9174)
    
    *   change .xls to .xl  
        I removed the “environment” as well
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-9337)
        
62.  Need multiple files into one single sheet.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-9003)
    
63.  Hi, I was able to get the script above to work.
    
    How can I modify this script to combined Sheets with the name “Sheet1” from multiple file into one file.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-8827)
    
    *   so how did you ended up making it work???
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-8989)
        
64.  What am I missing? I keep getting a run time error 52 (bad file name or number) on this line: Filename = Dir(FolderPath & “\*.xlsm\*”). I changed it to .xlsm for Excel 2013 for macro.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-8825)
    
    *   Ugh…me too!!!
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-8988)
        
65.  also, can I only combine page 1 of the workbooks to be combined into a single workbook?
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-8659)
    
66.  If my files are on a network drive, do I remove the “Environ” part of the FolderPath?
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-8658)
    
67.  It’s not working for me..!! When i am pressing F5…no combination of sheets..>!!
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-3319)
    
68.  Thank you for the tip.  
    I have a question related to the handling the files with macros (\*.xlsm) since the code will pick these files as well during the run. It seems that the macros will not be copied along with the worksheets and therefore some of the formulas may not work in the new workbook.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-3269)
    
    *   Thanks for commenting Lazarus.. You’re right! This wouldn’t pick up the macros while copying the sheets
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-3275)
        
        *   is there any way if the multiple files can be consolidated into one single tab instead of multiple tabs?
            
            [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-3708)
            
        *   Hi Sumit,  
            Also it is not working for me for “xlsx” file. It is showing debugg at Filename = Dir(FolderPath & “\*.xlsx\*”). Please get a solution. Thanks
            
            [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-8655)
            
            *   I am getting the same error…..
                
                [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-8987)
                
                *   Here When the Path In the Folder Is Copied It Must Start Form The “Desktop” & Not As “C:”
                    
                    If Rectify This Then It Automatically Works When pressing “F5”
                    
            *   Here When the Path In the Folder Is Copied It Must Start Form The “Desktop” & Not As “C:”  
                If Rectify This Then It Automatically Works When pressing F5
                
                [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-9645)
                
69.  Thanks for this tip Sumit………….
    
    But it create multiple sub sheets of multiple files…what should to do if we need all multiple files into only one single sub sheet…………
    
    Pls. help.
    
    [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-3261)
    
    *   Hello Anand, By what I understand, You want to combine all the sheets from all the workbooks into a single sheet. This may be limited by the number of rows in a worksheet. It would be helpful if you could share a sample file
        
        [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-3268)
        
        *   Hi Sumit,
            
            Firstly Thanks for concern.
            
            I have send an email to you for further clarification on it. Pls. have a look.
            
            [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-3272)
            
            *   Hi Sumit………..
                
                Pls. help on this…………
                
                [Reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#comment-3292)
                

### Leave a Comment [Cancel reply](https://trumpexcel.com/combine-multiple-workbooks-one-excel-workbooks/#respond)

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