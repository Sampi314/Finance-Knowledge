# How to Automatically Open Specific Excel File on Startup

**Source:** https://trumpexcel.com/automatically-open-excel-file-startup

---

[Skip to content](https://trumpexcel.com/automatically-open-excel-file-startup/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/automatically-open-excel-file-startup/#below-title)

Want some Excel files to open automatically when you start Excel?

These could be files the that you open every day in the morning (such as tracking sheet or [timesheet)](https://trumpexcel.com/excel-timesheet-calculator-template/)
, or some project related files that you need to open as soon as you start Excel.

While you always have the option to open these files manually, it’s just one of those small time savings things you can do by automating the process.

And this automation doesn’t need any VBA code or complex steps. It’s something you can do in a few seconds and keep saving time every day.

Now there are two ways you can automatically open Excel files:

1.  When you start Excel – **Recommended**
2.  When you start your system (Windows)
3.  When you open an Excel file, and it opens all the related files with it (this method uses VBA)

In this tutorial, I will show you how to open specific Excel files when you start Excel as well as when you start Windows.

Note: All the things that I cover in this tutorial are for a Windows operating system. If you use a Mac, you can give it a try but I have not tested this on Mac.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/automatically-open-excel-file-startup/#)

Automatically Open Files When You Start Excel
---------------------------------------------

With Excel, you can customize the startup behavior to:

1.  Start Excel and show the start screen (or open a blank workbook)
2.  Start Excel and open a specific workbook or template
3.  Start Excel and open all the Excel files in a folder

When you start Excel, the default behavior is that it opens the start screen that shows the recent workbooks and templates (as shown below).

![Excel Startup Screen you see when you start it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%20418'%3E%3C/svg%3E)

Note: This behavior of showing start screen on startup has become a default from Excel 2013 onwards

From the start screen, you can choose to open a new workbook or you can choose from the existing [templates in Excel](https://trumpexcel.com/free-excel-templates/)
 (there are some useful templates on this list).

Excel allows you to customize the startup behavior where you can specify if you want to open a new blank workbook (instead of the start screen), or a specific Excel file, or even all the files in a specific folder.

So let’s quickly go through the different options and learn how you can customize Excel startup.

### Open a Blank File when Excel Starts

When you enable this option, whenever you start Excel, it will open a new blank workbook.

Here is how to enable this:

1.  Start Excel and open a new workbook by clicking on Blank workbook in the start screen (or you can open any existing saved workbook)
2.  Click on File![Click on File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20370%20193'%3E%3C/svg%3E)
3.  Click on Options![Click on Options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20400'%3E%3C/svg%3E)
4.  In the Excel Options dialog box, make sure General is selected in the left pane![Selection General in Excel Options Pane](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20474%20321'%3E%3C/svg%3E)
5.  Scroll down and in the ‘Start up options’ and uncheck the one that says – ‘Show the start screen when this application starts’![Check the option - Show the start screen when Excel Starts](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20653%20243'%3E%3C/svg%3E)
6.  Click OK.

Done!

Now when you start Excel from now on, it will open a blank workbook and not show the start screen.

### Open a Specific Workbook when Excel Starts

There is an XLStart folder in your system that determines which files to open when Excel starts.

By default, this folder is empty, which is the reason that you see a start screen or a blank workbook when you start Excel.

So, if you want a specific Excel workbook (or even multiple workbooks) to open when Excel starts, you need to place this workbook in this XLStart folder.

And to do this, you first need to know where to find this XLStart folder.

Below are the steps to get the path of the XLStart folder:

1.  Open a new workbook or an existing workbook
2.  Click on File
3.  Click on Options
4.  In the Excel Options dialog box, click on Trust Center (in the left pane of the dialog box)![Click on Trust Center in Excel Options dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20388%20480'%3E%3C/svg%3E)
5.  Click on Trust Center Settings![Click on Trust Center Settings](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20781%20330'%3E%3C/svg%3E)
6.  In the Trust Center dialog box that opens, click on ‘Trusted Locations’. This will show you all the trusted locations (including the Excel StartUp location)![Click on Trusted Locations in the Trust Center dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20504%20452'%3E%3C/svg%3E)
7.  Double-click on the Excel StartUp location.![Double click on the XLStart folder path](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20399'%3E%3C/svg%3E)
8.  This will open the trusted location dialog box with the Excel StartUp folder location. Copy this location.![Copy the XLStart folder location](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20534%20357'%3E%3C/svg%3E)
9.  Open any folder and enter the copied location and hit Enter. This will open the Excel StartUp folder![Copy and Paste XLStart folder path in any folder to open it](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20755%20368'%3E%3C/svg%3E)
10.  Place the file (or the shortcut to the file) that you want to open in this folder. In the above example, I have the file called Main.xlsx in this folder, which would open automatically when I start Excel the next time.

Once you do all the above steps and place the file in Excel StartUp folder, this file would automatically open the next time you open Excel.

Also, if you want multiple files to open, you can place all the files in this folder.

Here are some important things to know when placing files in the XLStart folder:

*   Only those Excel files that are in the XLStart folder would open automatically when you start Excel. If there is any file in a sub-folder in the XLStart folder, those files would not open.
*   Note that you can only place the Excel file formats in this folder. If you place a file that can not be read by Excel, it will not open and you’ll see an error (file format is not valid).![Not a valid file format warning](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20335%20145'%3E%3C/svg%3E)
*   If you have an Excel file that has a macro that runs when you open the file, the macro would run even when the file opens when it’s in the XLStart folder. In case you don’t want the macro to run, hold the SHIFT key and then open Excel.

#### Overwriting Files in the Excel StartUp Folder

When you add a file to the Excel StartUp folder, you won’t be able to overwrite it.

This means that once you have added a file and you open Excel the next time, this file opens.  And now if you make some changes to it and then try to save it, it will ask you to save it at a different location. You will see a prompt as shown below:

![Can't save file in XLStart folder](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20665%20158'%3E%3C/svg%3E)

This works well as most of the time the files you add to the Excel startup folder would be templates/formats that you don’t want to change. So, when you work on a file that opened automatically and then want to save it, it will ask you to save it in some other location.

But what if you want to save the changes in the same file (in Excel Startup folder) and want these changes to reflect the next time you open Excel.

The trick would be to **save a shortcut of the Excel file in the XLStart folder and not the Excel file itself**.

### Automatically Open Workbooks in a Specific Folder

In the above example, I showed you how to place an Excel file or multiple files in the XLStart folder. And when you open Excel, these files automatically open.

But what if you want the files in a different folder to open automatically when Excel starts. This could be a project folder or template folder which has your everyday use files. Or this could be a folder on the network drive which has your current project files that you want to open whenever you open Excel.

Excel allows you to specify a folder and it will automatically open all the files in the folder when you start Excel.

Below are the steps to specify this alternate startup folder:

1.  Open a new workbook or an existing workbook
2.  Click on File
3.  Click on Options
4.  In the Excel Options dialog box, click on Advanced (in the left pane of the dialog box)![Advanced tab in Excel Options dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20489%20394'%3E%3C/svg%3E)
5.  Scroll down and within the General options, enter the location of the folder in the field with the description – “At startup, open all files in:”![Enter the Startup folder Address in the Advanced tab General options](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20760%20470'%3E%3C/svg%3E)
6.  Click OK

That’s it!

Now when you start Excel, it will automatically open all the files in this specified folder.

A few things to know when using this method:

1.  You can overwrite files that automatically get opened. So, if you open Excel, which opens all the files in the specified folder, and then you make a change in any of the file and save it, this change will be saved. And the next time you open Excel, it will open these files in the specified folder with the changes you made.
2.  It will only open files that are in Excel format. For example, if you have an MS Word file or a note pad, it will not get opened.
3.  Only files in the folder are opened (not in the sub-folders)

I personally believe this can be a source of the issue and sometimes you may end up making changes that you don’t want. To prevent this, you can use create a VBA code that saves the file with a different name (maybe timestamp) in a different folder whenever you save it.

[Here is an example](https://trumpexcel.com/vba-workbook/#Save-a-Copy-of-the-Workbook-with-Timestamp)
 where a VBA code is used to create backup copies of the workbook whenever you save it.

In case there is a file with the same name in the XLStart folder as well as in the folder you have specified to use to open workbooks, the file in the XLStart folder will get opened.

Also read: [Open Excel in Safe Mode](https://trumpexcel.com/safe-mode-excel/)

Open Workbook/Worksheet Templates when Excel Starts
---------------------------------------------------

If there is a specific template that you need to work on every day, you can save that template and open it automatically whenever you start Excel.

For example, if you have a template that has some pre-set font type/size, header/footer, company logo, row/column headers, etc., you can [save this as a template](https://trumpexcel.com/save-as-shortcuts-excel/)
 and open it automatically when Excel starts.

To do this, you need to save the Excel file as a template (covered in the steps below) and then put this template file in the XLStart folder or in the folder that you have specified as the alternate Startup folder.

Below are the steps to save a workbook as a template:

1.  Open a new workbook (or use an existing workbook that you want to save a template)
2.  Make the change that you want in the template (such as font size/type, header/footer, columns/row headers, place holder tables, etc.)
3.  Click the File tab
4.  Click on Save As
5.  In the Save As dialog box, click on the Save as type dialog box
6.  Click on Excel Template (\*.xltx)![Save as an Excel Template format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20489'%3E%3C/svg%3E)
7.  Locate the folder in which you want to save this template file
8.  Click Save

Note: In the above steps, I was not able to save the file directly to the XLStart folder. It showed a prompt as shown below saying I don’t have the permission to save in this folder. But I was able to save this template file in a regular folder and then copy/cut and paste in the XLStart folder. Alternately, you can also save this template file in the folder (and specify that folder to automatically open Excel files). Creating and using alternate folders is covered here.

![Cant save Excel file directly in the XLStart folder](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20603%20228'%3E%3C/svg%3E)

Also read: [How to Remove (Disable) Add-Ins in Excel](https://trumpexcel.com/remove-add-ins-excel/)

Prevent Excel Files from Opening Automatically
----------------------------------------------

If you open Excel and suddenly some workbook(s) open along with, you likely have one (or both) of the two below situation:

1.  There are files in your Excel Startup (XLStart) folder
2.  You have an alternate folder specified as the StartUp folder that has some Excel file(s).

So, if you want Excel to not open these files and resort to the default behavior of opening a blank workbook or the startup screen, you need to check the above two things.

The first thing to check is the XLStart folder and remove any files in it. If you know how to locate the XLStart folder, great.

Else follow the below steps to check if there are files in the XLStart Folder:

1.  Open a new workbook or an existing workbook
2.  Click on File
3.  Click on Options
4.  In the Excel Options dialog box, click on Trust Center (in the left pane of the dialog box)
5.  Click on Trust Center Settings
6.  In the Trust Center dialog box that opens, click on Trusted Locations. This will show you all the trusted locations (including the Excel StartUp location)
7.  Double Click on the Excel StartUp location. This will open the trusted location dialog box with the Excel StartUp folder location
8.  Copy the location path
9.  Open any folder and enter the copied location and hit Enter. This will open the Excel StartUp folder
10.  Delete any file in the folder.

This removes any files that automatically open when you start Excel because these were part of the XLStart folder.

You can check if this resolves the issue (close all Excel workbooks and start Excel again).

In case you still have files opening automatically, you likely have another folder specified as the Startup folder.

Below are the steps to remove any folder as the default StartUp folder:

1.  Open a new workbook or an existing workbook
2.  Click on File
3.  Click on Options
4.  In the Excel Options dialog box, click on Advanced (in the left pane of the dialog box)
5.  Scroll down and within the General options, delete any location of the folder in the field with the description – “At startup, open all files in:”![Delete Alternate Startup folder address in the Excel Options dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20645%20468'%3E%3C/svg%3E)
6.  Click OK

Open Excel Files Automatically When You Start Your Computer/Laptop
------------------------------------------------------------------

Just like we have an XLStart folder which automatically opens Excel files in it, there is a Startup folder for Windows as well.

This folder is often used to open specific programs that you want to open automatically when your system starts – such as browser or Microsoft programs such as Excel or PowerPoint.

You can also use this folder to open specific Excel files as soon as your computer starts.

To do this, you need to copy the file (or the shortcut of that file) and place it in the startup folder.

Below are the steps to open the startup folder in Windows 8 and 10:

1.  Open the Windows Run dialog box (use the keyboard short Windows Key + R or just type Run in the search bar at the bottom left of your system).
2.  In the Run dialog box, copy and paste the following path – _%AppData%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup![Windows Startup folder path in the Run dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20456%20272'%3E%3C/svg%3E)_
3.  Press the Enter key or click OK.

The above steps would open the Windows StartUp folder. Now place the Excel files or the shortcut to the Excel files that you want to open as soon as Windows starts.

You can also achieve the same thing by adding the file in the XLSart folder or using an alternate folder (both covered above in this tutorial), and then add a shortcut to the Excel program in the Windows startup folder. This makes Excel start when you start Windows (because you have the Excel shortcut in the Windows startup folder), which in turn open the files in the XLStart folder.

If you’re using Windows 7, you can find the [instruction to open the startup folder here](https://support.office.com/en-us/article/automatically-start-an-office-program-when-you-turn-on-your-computer-4a42ed45-c064-47b6-b497-119c870f7bab)
.

Open Related Excel Files When you Open a Specific Workbook (using VBA)
----------------------------------------------------------------------

In the sections above, I covered how to open files when you start Excel.

In this part of the tutorial, I will show you how to open all the related files when you open a specific Excel workbook.

For example, if you’re working on a project, you can open the master tracker and it will simultaneously open some related files (such as the project status worksheet or cost-benefit analysis of the project or the project planning workbook).

You get the idea!

To do this, you can use a simple VBA code and specify the files that you want to open.

Below is the code that will open a related file ‘Tracker.xlsx’ when you open the file in which this code resides:

Private Sub Workbook\_Open()
Workbooks.Open "C:\\Users\\sumit\\Desktop\\Test File A.xlsx"
End Sub

The above code uses the Workbook open event to run the code as soon as this workbook opens. You have to specify the exact path of the file (including the file extension).

If you want multiple files to open, you can add multiple lines of code with each line specifying the location of the file.

For example, the below code will open three files when you open the in which this code resides:

Private Sub Workbook\_Open()
Workbooks.Open "C:\\Users\\sumit\\Desktop\\Test New\\Test File A.xlsx"
Workbooks.Open "C:\\Users\\sumit\\Desktop\\Test New\\Test File B.xlsx"
Workbooks.Open "C:\\Users\\sumit\\Desktop\\Test New\\Test File C.xlsx"
End Sub

**Where to put this code?**

This code needs to be placed in the workbook, which when opened, would trigger opening the related workbook (the address of which are mentioned in the code).

Below are the steps to place the code in the workbook:

1.  With the workbook open, hold the ALT key and then press the F11 key. This will open the [VB Editor](https://trumpexcel.com/visual-basic-editor/)
    .
2.  In the VB Editor, double-click on ThisWorkbook object (which would be listed as one of the objects in the Project Explorer pane). This would open the code window for ThisWorkbook object. If you can’t see the Project Explorer pane, click on ‘View’ in the menu bar and then click on ‘Project Explorer’.![Double click on the ThisWorkbook object](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20367%20264'%3E%3C/svg%3E)
3.  In the code window, copy and paste the above code![Copy and paste code in the code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20779%20188'%3E%3C/svg%3E)
4.  Close the VB Editor

When you have placed the above code in the ‘ThisWorkbook’ code window, whenever this workbook is opened, this VBA code will get executed, which in turn will open the specified Excel files.

**You may also like the following Excel tutorials:**

*   [How to Recover Unsaved Excel Files](https://trumpexcel.com/recover-unsaved-excel-files/)
    
*   [How to Clean Data in Excel](https://trumpexcel.com/clean-data-in-excel/)
    
*   [Combine Data from Multiple Workbooks in Excel (using Power Query)](https://trumpexcel.com/combine-data-from-multiple-workbooks/)
    
*   [How to Create a Data Entry Form in Excel](https://trumpexcel.com/data-entry-form/)
    
*   [Split Each Excel Sheet Into Separate Files](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/)
    
*   [How to Turn On AutoSave in Excel](https://trumpexcel.com/turn-on-autosave-excel/)
    
*   [Microsoft Excel Won’t Open; How to Fix it!](https://trumpexcel.com/microsoft-excel-wont-open/)
    
*   [How to Open Excel Files Using VBA (Examples)](https://trumpexcel.com/open-excel-files-using-vba/)
    
*   [How to Mark an Excel Workbook as Final?](https://trumpexcel.com/mark-excel-workbook-as-final/)
    
*   [Bulk Create Folders (and Subfolders) Using Excel List](https://trumpexcel.com/bulk-create-folders-subfolders-excel-list/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

6 thoughts on “How to Automatically Open Specific Excel File on Startup”
------------------------------------------------------------------------

1.  Thank you, excellently presented!
    
    [Reply](https://trumpexcel.com/automatically-open-excel-file-startup/#comment-14167)
    
2.  FANTASTIC article. Super easy to follow, and I appreciate all the screen shots. I had 2 issues, and your guide enabled me to fix both on the first tries.
    
    [Reply](https://trumpexcel.com/automatically-open-excel-file-startup/#comment-12653)
    
3.  thank you very summit for teaching me
    
    [Reply](https://trumpexcel.com/automatically-open-excel-file-startup/#comment-12105)
    
4.  How to use macro in excel file
    
    [Reply](https://trumpexcel.com/automatically-open-excel-file-startup/#comment-12089)
    
    *   Alt+L+P+M
        
        Then  
        Select the Macro  
        And Press Enter to Run
        
        [Reply](https://trumpexcel.com/automatically-open-excel-file-startup/#comment-12520)
        
5.  Dear Sumit,
    
    As usual, an excellent article. Well done, I appreciate your effort to teach so many people, about hidden gems of Excel.
    
    One question for you: is there any possibility to open Excel, without displaying the splash screen, and also without opening an empty workbook ? If I remember well, this was possible on earlier versions of Excel, but I am not sure. I use Excel 2016. Thank you.
    
    [Reply](https://trumpexcel.com/automatically-open-excel-file-startup/#comment-12069)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/automatically-open-excel-file-startup/#respond)

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