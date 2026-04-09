# Send mails using VBA and Outlook - How to send emails using Excel

**Source:** https://chandoo.org/wp/send-mails-using-excel-vba-and-outlook

---

*   [Automation](https://chandoo.org/wp/category/automation/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Send mails using Excel VBA and Outlook
======================================

*   Last updated on March 21, 2018

![Picture of Vijay Sharma](https://secure.gravatar.com/avatar/b8604c6f79c8db3f79e17c562e6f7cd888a268d59501100720b70a6c3046ee1f?s=300&d=mm&r=g)

#### Vijay Sharma

Share

Facebook

Twitter

LinkedIn

_This is a guest post by Vijay, our in-house VBA Expert._

![Send mails using Excel VBA and Outlook - how to](https://img.chandoo.org/vba/send-mail-using-excel-vba-outlook.png "Send mails using Excel VBA and Outlook - how to")

In this article we well learn how to use VBA and Microsoft Outlook to send emails with your reports as attachment.

Scenario
--------

We have an excel based reporting template for the Customer Service Dashboard. We want to update this template using VBA code to create a static version and email it to a list of people. We will define the recipient list in a separate sheet.

Features
--------

1\. Code will automatically create necessary folders to save the output file.  
2\. Email sheet to contain the list of people who are going to receive the report.  
3\. Sending mail using Microsoft Outlook, primary target is corporate people who are using Outlook as their mail program.  
   
![](https://chandoo.org/wp/wp-content/uploads/2012/04/control-sheet.png "control-sheet")  
   
On our VBA project we would need to add references to the below  
1\. Microsoft Outlook Object Library  
2\. Microsoft Scripting Runtime Library  
Please note the Outlook library will be available depending on the version of Microsoft Outlook installed on your system, in the example workbook the reference is towards version 14 as available with Outlook 2010. If you have a different version of Outlook installed on your system, you need to point to the correct library installed.  
   
![](https://chandoo.org/wp/wp-content/uploads/2012/04/vba-references.png "vba-references")  
   
We have assumed the data used to create the report is already available in the sheet called “rawData”.  
We have then updated the “rawData” sheet with 2 new columns having the Date and Time.  
Date has been calculated in the rawData sheets using the Date Function.  
\=DATE(YEAR(B2),MONTH(B2),DAY(B2))  
The time has been calculated by converting the actual time of the call into the relevant 30 minute interval.  
\=INT((TIME(HOUR(B2),MINUTE(B2),SECOND(B2)))/(1/48))\*(1/48)  
If you need to setup your report into 15 minutes interval then replace 1/48 with 1/96.  
We have then used the COUNTIFS and SUMIFS function to create the data view in the Interval Data sheet.  
   
![](https://chandoo.org/wp/wp-content/uploads/2012/04/interval-data-sheet.png "interval-data-sheet")  
 

Understanding the VBA code to send mails
----------------------------------------

I will be discussing only the key elements of the code here.  
`    Sheets(Array("Cover", "Interval Data", "rawData")).Copy    `  
This list will create a new workbook containing the 3 sheets that we have included within the Array() parameter. If your report has more sheets feel free to add them.  
`   Set objfile = New FileSystemObject`

`   If objfile.FolderExists(xDir & xMonth) Then   If objfile.FileExists(xPath) Then   objfile.DeleteFile (xPath)   newWB.SaveAs Filename:=xPath, FileFormat:=xlOpenXMLWorkbook, Password:="", WriteResPassword:="", ReadOnlyRecommended:=False _   , CreateBackup:=False  Application.ActiveWorkbook.Close   Else   newWB.SaveAs Filename:=xPath, FileFormat:=xlOpenXMLWorkbook, Password:="", WriteResPassword:="", ReadOnlyRecommended:=False _   , CreateBackup:=False   Application.ActiveWorkbook.Close   End If   Else   xNewFolder = xDir & xMonth   MkDir xNewFolder   newWB.SaveAs Filename:=xPath, FileFormat:=xlOpenXMLWorkbook, Password:="", WriteResPassword:="", ReadOnlyRecommended:=False _   , CreateBackup:=False   Application.ActiveWorkbook.Close   End If   `

The above code checks if the correct folder exists for the report to be saved or not and creates one if not existing. This also takes cares of overwriting the existing report in case you need to re-run the report again during the same day.  
Creating the List of recipients  
`   currentWB.Activate   Sheets("Email").Visible = True   Sheets("Email").Select`

`   strEmailTo = ""   strEmailCC = ""   strEmailBCC = ""  xStp = 1   `

`Do Until xStp = 4   Cells(2, xStp).Select   Do Until ActiveCell = ""   strDistroList = ActiveCell.Value   If xStp = 1 Then strEmailTo = strEmailTo & strDistroList & "; "   If xStp = 2 Then strEmailCC = strEmailCC & strDistroList & "; "   If xStp = 3 Then strEmailBCC = strEmailBCC & strDistroList & "; "   ActiveCell.Offset(1, 0).Select   Loop   xStp = xStp + 1   Loop   `  
The above code will create the list of people for whom the report is intended. We make use of the Do Until Loop here to update the 3 variables to hold the TO, CC and BCC list. The actual email addresses are captured from the Email sheet of the report template.  
Please note: there should be no blanks in the list when you are defining the same.  
`    Set olApp = New Outlook.Application   Dim olNs As Outlook.Namespace   Set olNs = olApp.GetNamespace("MAPI")   olNs.Logon   Set olMail = olApp.CreateItem(olMailItem)   olMail.To = strEmailTo   olMail.CC = strEmailCC   olMail.BCC = strEmailBCC   olMail.Subject = Mid(xFile, 1, Len(xFile) - 4)   olMail.Body = vbCrLf & "Hello Everyone," _   & vbCrLf & vbCrLf & "Please find attached the " & Mid(xFile, 1, Len(xFile) - 4) & "." _   & vbCrLf & vbCrLf & "Regards," _   & vbCrLf & "Chandoo.Org"    `  
The above code creates a new instance of Outlook and then logs in to your default mailbox, using which we will be sending the mail out to the recipients. We also create the body of the mail and specify the To, CC and BCC list.  
`    olMail.Attachments.Add xPath   olMail.Display    `  
Finally we add the attachment to the email we have created and then using the Display method bring it on the screen. You may also use the .Send method to send the mail directly.  
That is all the code we needed to create a copy of the report with selected few sheets and then send them out using VBA. There are a lot of other methods using which you may be able to send out mails, however this specifically helps out to create report templates to use within your organization and send out mails.  
Do you also use VBA and Other methods to send mails, if yes please share the same for the benefit of everyone.

Download Excel File
-------------------

[**Click here to download the file**](https://chandoo.org/wp/wp-content/uploads/2012/04/email.xlsm)
 & save it on your system and use it to understand this technique.

Do you use Excel to automate emails?
------------------------------------

I often use Excel to automatically email reports & messages. This is quite useful when you have to send a snapshot of a report to a large team, but need to customize the email for each recipient.  
**What about you?** Have you used Excel to automate emails? What is your experience like? Do you use VBA or some other technique? Please share using comments.

More on VBA & Macros
--------------------

If you want to learn more about using VBA to automate reporting & email tasks, read these:

*   [Automatically Generate Report Variations using Excel](http://chandoo.org/wp/2011/09/14/hui%E2%80%99s-excel-report-printer/)
    
*   [Birthday Reminder & Email in Excel](http://chandoo.org/wp/2010/10/26/birthday-reminder-template/)
    
*   [What is VBA & Macros? Introduction](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/)
    
*   [Excel VBA Example Macros](http://chandoo.org/wp/excel-vba/examples/)
    
*   [VBA tutorial videos](http://chandoo.org/wp/excel-vba/videos/)
    

Join our VBA Classes
--------------------

If you want to learn how to develop applications like these and more, please consider joining our VBA Classes. It is a step-by-step program designed to teach you all concepts of VBA so that you can automate & simplify your work.

[**Click here to learn more about VBA Classes & join us**](http://chandoo.org/wp/vba-classes/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [Ask a question or say something...](https://chandoo.org/wp/send-mails-using-excel-vba-and-outlook/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [advanced vba](https://chandoo.org/wp/tag/advanced-vba/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [email](https://chandoo.org/wp/tag/email/)
    , [learn](https://chandoo.org/wp/tag/learn/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [outlook](https://chandoo.org/wp/tag/outlook/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Automation](https://chandoo.org/wp/category/automation/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousFormula Forensic No 019. Converting uneven Text Strings to Time](https://chandoo.org/wp/formula-forensic-no-019/)

[NextLets meet when I am in AustraliaNext](https://chandoo.org/wp/lets-meet-when-i-am-in-australia/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![developer ribbon in Excel](https://chandoo.org/wp/wp-content/uploads/2025/06/screenshot-0138.png)](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

Excel Howtos

### [How to enable developer ribbon in Excel?](https://chandoo.org/wp/how-to-enable-developer-ribbon-in-excel/)

[![auto format excel values in thousands / millions / billions](https://chandoo.org/wp/wp-content/uploads/2024/07/SNAG-0072.png)](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

Charts and Graphs

### [Automatically Format Numbers in Thousands, Millions, Billions in Excel \[2 Techniques\]](https://chandoo.org/wp/format-numbers-in-thousands-millions-billions-in-excel/)

[![Get bolded portions of a column using getBoldText function](https://chandoo.org/wp/wp-content/uploads/2024/02/get-bold-text-excel.png)](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

Excel Howtos

### [Get all BOLD text out Excel Cells Automatically](https://chandoo.org/wp/get-the-bold-portion-of-a-cell-in-excel/)

[![dynamic-map-chart-excel](https://chandoo.org/wp/wp-content/uploads/2023/05/dynamic-map-chart-excel.gif)](https://chandoo.org/wp/interactive-map-chart-in-excel/)

Charts and Graphs

### [Make an Impressive Interactive Map Chart in Excel](https://chandoo.org/wp/interactive-map-chart-in-excel/)

[![Dynamic Business Dashboard](https://chandoo.org/wp/wp-content/uploads/2023/05/SNAG-2629.png)](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

Charts and Graphs

### [How to Create a Dynamic Excel Dashboard in Just 5 Steps](https://chandoo.org/wp/how-to-create-a-dynamic-excel-dashboard-in-5-steps/)

[![project management dashboard - interactive & dynamic](https://chandoo.org/wp/wp-content/uploads/2021/05/project-management-dashboard-full-image.png)](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

Charts and Graphs

### [How to create a fully interactive Project Dashboard with Excel – Tutorial](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/sand-pendulums-lissajous-patterns-in-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ