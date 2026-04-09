# Unprotect Excel Sheets Without Password (It's Very Easy)

**Source:** https://trumpexcel.com/unprotect-excel-sheets-without-password

---

[Skip to content](https://trumpexcel.com/unprotect-excel-sheets-without-password/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/unprotect-excel-sheets-without-password/#below-title)

It’s not uncommon for many people to protect worksheets in their Excel files and then forget the password.

It has happened to me many times, and every now and then, I have people sending me their Excel files asking how to unlock the sheet without the password.

The good news is that Excel password protection is not very robust, and you can easily get around it.

You do not need any third-party software or website to do this. You can do it right there on your computer or laptop in less than a minute.

Let’s see how to unlock Excel sheets without knowing the password.

[**_Click here to download the example file and follow along_**](https://www.dropbox.com/scl/fi/1zvawx0zpvi4jn9dk3i4j/Call-Center-Dashboard.xlsx?rlkey=n2u8rp8h2vil4r3gboh4yzo42&dl=1)

Unprotect Excel Sheets Without Password

[Toggle](https://trumpexcel.com/unprotect-excel-sheets-without-password/#)

For this article, I am going to use one of the Excel Dashboard files I created called _Call-Center-Dashboard.xlsx_. It has three sheets, and all the sheets have been protected with a password.

If I try to make any change in the worksheet, I get a prompt as shown below:

![Prompt went trying to change protected worksheet](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20453%20261'%3E%3C/svg%3E)

Let’s now look at the steps that will unprotect a sheet even when you don’t have the password.

Step 1 – Make a Copy of your Excel Workbook (Highly Recommended)
----------------------------------------------------------------

While this is not a mandatory step, I highly recommend you create a copy of the Excel workbook from which you want to remove the worksheet protection.

Since we are going to temper with the code that makes up the Excel file, there is a possibility that things may go wrong, leading to the corruption of your Excel file or loss of data.

In my example, I will make a copy of the file Call-Center-Dashboard.xlsx.

This copied version of the file is named _**Call-Center-Dashboard-Copy.xlsx**_

![Make a copy of the file you want to unprotect](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20368'%3E%3C/svg%3E)

Make a copy of the file

Also read: [Remove Password from VBA Project in Excel](https://trumpexcel.com/excel-vba/remove-password/)

Step 2 – Change the Extension of the Workbook to ZIP
----------------------------------------------------

The next step is to change the extension of the file (in which you want to unprotect the worksheets) from .xlsx to .zip.

You will see a Rename dialog box as shown below. Click on Yes.

![Prompt when changing Excel file to zip](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20548%20188'%3E%3C/svg%3E)

Doing this will convert your Excel file into a zip folder, allowing you to access different worksheets separately.

![Excel file converted into zip folder by changing the extension](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20580%20348'%3E%3C/svg%3E)

In my example, I will change _Call-Center-Dashboard-Copy.xlsx_ to Call-_Center-Dashboard-Copy.zip_

If you don’t see the file extension in your Excel workbook, click on the View tab and make sure the _File Name Extensions_ option is checked.

![File Name extension to be visible](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20538'%3E%3C/svg%3E)

Step 3 – Locate the Worksheet XML File and Open in Notepad
----------------------------------------------------------

Now, double-click on the zip folder to open it. You should see a couple of folders as shown below.

![Folders inside the ZIP folder](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20177'%3E%3C/svg%3E)

Open the XL folder, which will show you more folders, as shown below.

![Folders inside the xl folder](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20802%20532'%3E%3C/svg%3E)

Open the Worksheets folder, which will then show you all the sheets in your Excel file as XML files.

![Sheets as xml files inside the worksheets folder](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20782%20217'%3E%3C/svg%3E)

In my example, I have three worksheets, which are shown as XML files.

Copy the sheet from which you want to remove the password, come out of the ZIP folder, and paste this file.

In this example, I will copy sheet3.xml file and paste it outside the zipped folder.

![Copy Sheet xml file outside the ZIP folder](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20500%20543'%3E%3C/svg%3E)

Since I need to make changes to this XML file, I cannot do this inside the zipped folder without extracting it. So I copied the file and pasted it outside the zip folder so I can make changes to it, and once I’m done, I can copy it back into the zip folder.

Step 4 – Remove the Worksheet Protection from the code
------------------------------------------------------

Now that we have the XML file outside of the zip folder, we can make changes to it and remove the worksheet protection.

Right-click on the XML file and open it with a Wordpad or Notepad.

![Open XML file in wordpad](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20553'%3E%3C/svg%3E)

This will show you the code as shown below:

![Code inside the XML file](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20574'%3E%3C/svg%3E)

Use Control + F to open the Find dialog box and search for the word ‘protection’.

![Search Protection in the code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20306'%3E%3C/svg%3E)

This will take you to the part where the code says _sheetProtection_.

Select the entire code starting from _<sheetProtection_ till the closing bracket >.

Delete this code and save the file.

![Delete the sheet protection code](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20314'%3E%3C/svg%3E)

The above steps have removed the worksheet protection from the worksheet. But we still need to put it back in the zip folder and convert the zip folder back into an Excel book.

So copy this XML file, Go back into the zipped folder –> xl folder –> worksheets folder, and then paste the file back.

Since the folder already has a file with the same name, you can first delete the original file and then copy the file where we have made changes in the code.

Step 5 – Convert the ZIP Folder Back into an Excel Workbook
-----------------------------------------------------------

Come out of the zip folder and then change the extension from .ZIP to .XLSX

And that’s it!

Now, if you open the Excel file, you will notice that the protection has been removed from Sheet 3.

In this example, I have shown you how to do this for one sheet only, but you can repeat the same process for all the sheets that have protection that you want to remove.

And as mentioned, you didn’t need to know the password to unprotect the worksheet, as we were able to go into the code and remove the entire part that was responsible for protecting the sheet.

**Use Responsibly**: While Excel protection is not very robust, and it’s quite easy to break worksheet protection without passwords, make sure you’re using it responsibly on either your files where you have forgotten the password or other people’s files where they ask for your help. Don’t use it to steal someone else’s work or unprotected worksheets that you’re not supposed to tamper with.

In this article, I showed you how to unprotect worksheets where you do not remember the password.

I hope you found this article helpful. If you have any questions or suggestions for me, please let me know in the comments section.

**Other Excel articles you may also like:**

*   [Protect and Unprotect Sheet Using VBA](https://trumpexcel.com/excel-vba/protect-unprotect-sheet/)
    
*   [How to Lock Formulas in Excel](https://trumpexcel.com/lock-formulas-excel/)
    
*   [How to Open Excel Files Using VBA](https://trumpexcel.com/open-excel-files-using-vba/)
    
*   [How to Lock Cells in Excel](https://trumpexcel.com/lock-cells-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/unprotect-excel-sheets-without-password/#respond)

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