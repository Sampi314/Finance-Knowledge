# How to Turn On AutoSave in Excel (An Easy Guide)

**Source:** https://trumpexcel.com/turn-on-autosave-excel

---

[Skip to content](https://trumpexcel.com/turn-on-autosave-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/turn-on-autosave-excel/#below-title)

While Excel has been continuously improved with each new version, there are still times when you may find it crashing once in a while (especially if you’re working with a large dataset).

And sometimes, it could be a factor outside of Excel – such as a power failure or your system hanging because of an issue other than Excel.

In such cases, to make sure you don’t lose your data, Excel has an AutoSave feature – which as the name suggests, will automatically save your work.

With autosave enabled, Excel will save your work at regular intervals, which will make sure you don’t lose a lot of your work (at max a few minutes of work can be lost).

In this tutorial, I will show you how to turn on AutoSave in Excel and all the important things you need to know about it.

**Note:** [AutoSave](https://support.office.com/en-us/article/turn-on-autosave-11c9f922-020b-439f-97f7-09b0041ed7cd)
 is a new feature in Office365, where it allows you to save real-time when files are saved in OneDrive or SharePoint. In case you’re using prior versions (Excel 2010/2013/2016/2019), you have the Save AutoRecover Information, which is not real-time but saves your work at regular intervals.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/turn-on-autosave-excel/#)

AutoSave Vs AutoRecover
-----------------------

**AutoSave is a new feature in Excel Office 365**, while AutoRecover has been in prior versions as well.

AutoSave allows you to save your work in real-time when you save your Excel files in OneDrive or SharePoint.

On the contrary, ‘Save AutoRecover Information’ is an option that automatically saves your work every 10 minutes (or whatever time period you specify). With this option enabled, it will keep a temporary copy of your work and keep saving it every 10 minutes.

In case your system shuts down unexpectedly, you will still be able to recover the temporarily saved file (using the Autorecover feature).

In this tutorial, I will cover both of these features.

Turn On AutoSave in Excel from the Options Dialog box
-----------------------------------------------------

You can enable AutoSave as well as save auto-recover information (i.e., to save files automatically at a certain time interval) in Excel from the Options dialog box. Once done, this would be turned on for all the workbooks you work on that system.

Remember that AutoSave is only available for Office365 users. If you don’t have O365, you can only use AutoRecover.

Below are the steps to turn on Auto-save in Excel:

1.  Click the File tab![Click the File tab in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20319%20181'%3E%3C/svg%3E)
2.  Click on Options![Click on Options in the Excel Backend](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20303%20564'%3E%3C/svg%3E)
3.  In the [Excel Options](https://trumpexcel.com/excel-options-hacks/)
     dialog box, click on the Save option on the left![Click on the Save Option](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20570%20270'%3E%3C/svg%3E)
4.  Check the option – ‘Save AutoRecover information every’ checkbox. By default, the value is 10 minutes, but you can choose a lower or higher value if you want.![Save Autorecover information every 10 minutes](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20785%20416'%3E%3C/svg%3E)
5.  Check the Option – “AutoSave OneDrive and SharePoint Online files by default in Excel’. This option works for Office 365 only and saves your work in real-time (every few seconds)![Turn On Autosave](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20785%20416'%3E%3C/svg%3E)
6.  Click Ok

The above steps would make sure that your work is automatically saved after every 10 minutes.

Note that for ‘AutoSave OneDrive and SharePoint Online files by default in Excel’ to work, your files need to be in the latest file format (i.e., XLSX and not XLS).

Other useful options you can use:

*   **Keep the last AutoRecovered version if I close without saving**: While Excel saves your work every 10 minutes (when AutoSave is turned on), enabling this option will ensure that you don’t lose even the work in between those 10 minutes (in case your system crashed or there is a power failure). When enabled, Excel will show you the option to [auto-recover any unsaved files/data](https://trumpexcel.com/recover-unsaved-excel-files/)
    .![Keep the last autorecovered version](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20785%20416'%3E%3C/svg%3E)
*   **AutoRecover File Location**: This is the location when Excel saves unsaved files. You can change this location if you want. In case you’re not the administrator, you may not be able to change this.![Autorecover file location](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20785%20416'%3E%3C/svg%3E)

When AutoSave is enabled (with files saved on Onedrive or SharePoint), you won’t see a prompt to save unsaved changes when you close the file (since these changes are being saved every few seconds).

Also, in case you’re adding a VB Code (macro) to the File, AutoSave would stop and will show you a prompt to save this file as a Macro-enabled fike (.xlsm format)

![AutoSave doesn't work when you have a macro in a xlsx file](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20782%20173'%3E%3C/svg%3E)

AutoSave now enables Excel users to share files and make changes in real-time. Also, you can see the version history and go back to any previous version if you want. When you open an old file using version history, it will be opened as Read-Only and you can save it with a new name if you want.

![Version history when using Autosave](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20754%20338'%3E%3C/svg%3E)

Also read: [How to Open Excel in Safe Mode?](https://trumpexcel.com/safe-mode-excel/)

Adding AutoSave to QAT (for Office 365)
---------------------------------------

If you’re using OneDrive or SharePoint, you can also add the AutoSave option in the [Quick Access Toolbar](https://trumpexcel.com/excel-quick-access-toolbar-options/)
 (available only in Office 365).

This allows you to enable autosave (in SharePoint or OneDrive) with a single click (it’s a toggle button).

While I found it to be available by default in my Office365 subscription, in case you don’t have it, you can add AutoSave to the Quick Access Toolbar using the below steps:

1.  Click on the Customize Quick Access Toolbar icon
2.  Click on Automatically Save option

![Add Automatically save in Quick Access Toolbar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20549%20321'%3E%3C/svg%3E)

In case you don’t see the ‘Automatically Save’ option in the drop-down, click on More Command and use the Excel Options dialog box to add the AutoSave option in the QAT.

An issue with AutoSave (Save As vs. Save a Copy)
------------------------------------------------

When you enable AutoSave and save the file in OneDrive or SharePoint, you will notice that you no longer see the ‘Save as’ option. Instead, you see the ‘Save a Copy’ option ([more on this here](https://support.office.com/en-us/article/what-is-autosave-6d6bd723-ebfd-4e40-b5f6-ae6e8088f7a5)
)

When AutoSave is enabled and your work is being saved every few seconds, it won’t be possible to make some changes and save it as a new file.

For example, if you start with an old file, work on it for 20 minutes and save a copy, you will have the old file as well as the new file with 20 minutes of latest work. But this isn’t possible with AutoSave enabled where it’s saving your work every few seconds.

This is why you now have the ‘**Save a Copy**‘ option, which you can use to create a copy and then make the changes.

In case your Excel files are not on OneDrive or SharePoint, you will still see the ‘Save As’ option.

Using Third-Party Tools such as DropBox or Google Drive
-------------------------------------------------------

You can also get the version history options for Excel files with storage options such as Dropbox and Google Drive.

These tools simply check if there have been any changes in the file and save the prior version. You can then go back to these versions if you want.

One of the benefits of using these third-party tools is that you can easily collaborate with people who don’t use OneDrive.

Since Google Drive and Dropbox are usually preferred over OneDrive by many, this helps when you’re working with teams/clients who use these options.

The only caveat is to make sure you don’t keep confidential data on these cloud storage services.

Automatically Save File Before Closing using VBA
------------------------------------------------

AutoSave is an amazing feature and makes working with Excel a lot stress-free – knowing that the data won’t be lost.

In case you don’t have Office 365 (which means you don’t have the AutoSave feature as well), you will have to rely on Excel’s AutoRecover feature.

Another option you can use is by having a simple VBA code in place that makes sure that your file is saved before you close it. This ensures you don’t lose your work because you closed the file before saving it.

Note: Using this would make sense only if you’re not using Office 365 with OneDrive or SharePoint. If you are, you can always go back to previous versions and your files are saved automatically anyway.

Below are the steps use VBA to save a file before closing the workbook:

1.  Open the workbook where you want to enable this VBA code to save before close.
2.  Hold the ALT key and press the F11 key (or Command + Option + F11 in Mac). This opens the VB Editor.
3.  Double-click on the ThisWorkbook object (for the file where you want to add this code) in the Project Explorer
4.  Copy and Paste the below code in the ThisWorkbook code window:
    
    Private Sub Workbook\_BeforeClose(Cancel As Boolean)
    ThisWorkbook.Save
    End Sub
    
5.  Close the VB Editor

![Copy and paste the code to Autosave in the Thisworkbook code window](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20780%20236'%3E%3C/svg%3E)

Now, when there is any change in the workbook and you close it before saving, it will first run this code (as this is a [VBA Event](https://trumpexcel.com/vba-events/)
 that runs based on an event – which is workbook closing in this case). This code will first save the workbook and then close it.

In case you haven’t saved the file before, this will show a prompt that will ask you to specify the location where the file should be saved.

In case you don’t want to overwrite your existing file, you can also modify the code so that it saves the file with a timestamp. This way, your work is not lost, and you can also go back to a previous version.

Below is the VBA code that will save the file with the date and time-stamp in the filename:

Private Sub Workbook\_BeforeClose(Cancel As Boolean)
wbname = ThisWorkbook.Name
timestamp = Format(Now, "ddmmmyyy-hhmmss")
ThisWorkbook.SaveAs timestamp & wbname
End Sub

This will save the new file with a [timestamp](https://trumpexcel.com/date-timestamp-excel/)
 in the name in the same location where the old file is saved. If you want the file to be saved in a specific folder, you can specify that location in the code.

So this is all that you should know about enabling AutoSave in Excel and using it efficiently. And if you’re not using Office 365 and hence don’t have AutoSave, you can still configure the AutoRecover options and recover any unsaved files. Also, the VBA code can be used to make sure the files are saved as a copy automatically when you close it.

Hope you found this tutorial useful!

**You may also like the following Excel tutorials:**

*   [How to Reduce Excel File Size](https://trumpexcel.com/reduce-excel-file-size/)
    
*   [Split Each Excel Sheet Into Separate Files](https://trumpexcel.com/split-each-excel-sheet-into-separate-files/)
    
*   [How to Automatically Open Specific Excel File on Startup](https://trumpexcel.com/automatically-open-excel-file-startup/)
    
*   [Get a List of File Names from Folders & Sub-folders (using Power Query)](https://trumpexcel.com/list-file-names-power-query/)
    
*   [Microsoft Excel Won’t Open; How to Fix it!](https://trumpexcel.com/microsoft-excel-wont-open/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/turn-on-autosave-excel/#respond)

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