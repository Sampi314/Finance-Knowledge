# Show pop-up calendar upon right click [Excel VBA] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/pop-up-calendar-excel-vba

---

*   [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Show pop-up calendar upon right click \[Excel VBA\]
===================================================

*   Last updated on November 13, 2013

![Picture of Vijay Sharma](https://secure.gravatar.com/avatar/b8604c6f79c8db3f79e17c562e6f7cd888a268d59501100720b70a6c3046ee1f?s=300&d=mm&r=g)

#### Vijay Sharma

Share

Facebook

Twitter

LinkedIn

_This is a guest post by Vijay, our in-house VBA Expert._

There are times when we are entering dates into several columns and would like to select a date from a popup calendar instead of manually typing.

Today, lets understand how we can set up a pop-up calendar in Excel so that your users can easily input dates by right clicking on a cell and inserting a date.

**Keep in mind:**

1\. This code is only supported on the 32-Bit versions of Excel.  
2\. You need to have admin rights to be able to install the ActiveX Control

First, take a look at pop-up calendar
-------------------------------------

Here is a short demo of how our pop-up calendar behaves.

![right_click_context_menu_example](https://chandoo.org/wp/wp-content/uploads/2013/11/right_click_context_menu_example.gif)

What we need to do this
-----------------------

1\. Design user form that contains our calendar.  
2\. Create a Data Table  
3\. Put some VBA code to get this done

### Design user form that contains our calendar.

First let’s design the user form, so start up Excel and bring up the Visual Basic editor and add an user form in the project.

We would need the Microsoft Date and Time Picker control for this project, so please ensure that you have the required file available on your system. If it is not available you may download the MSCOMCT2.OCX from this link.

[http://activex.microsoft.com/controls/vb6/mscomct2.cab](http://activex.microsoft.com/controls/vb6/mscomct2.cab)

Installing this file is pretty simple, you need to extract the contents form the CAB file and then copy this into your System32 folder and then register using the REGSVR32 utility.

If you are using Windows 7 or above you would need to copy this file into the SysWOW64 folder and then register.

For Windows 7 and above, please make sure you are running the Command Prompt (Admin) to be able to successfully register the ActiveX control.

Windows 7: Click on Start, All Programs, Accessories, Command Prompt (right click and choose Run as Administrator  
Windows 8: Windows Key + X, then choose Command Prompt (Admin)

![command_prompt_example](https://chandoo.org/wp/wp-content/uploads/2013/11/command_prompt_example.png)

Okay, let’s get back to designing the user form.  
Insert a new Userfrom on the VBA project and then click on Addition Controls on the Tools menu.  
![additional_controls](https://chandoo.org/wp/wp-content/uploads/2013/11/additional_controls.png)  
Once the Additional controls dialog box is on the screen, locate the above highlighted entry and then select the same by clicking the box on the left. Now click Ok to close this dialog box.  
Now place one Monthview control on the userform and one Command button.  
Below are the properties that we need to change for the Commandbutton  
• Caption = “Close”  
• Cancel = True  
• Name = cmdClose  
Place this command button anywhere you like on the userfrom, we will place the Monthview on top of this to avoid show this to the user.  
Since we have specified the Cancel = True for the commandbutton, the click event can be triggered by pressing the Escape key to handle the code that we will write for the Close button.

Now place the Monthview control as show in the picture below  
![userform](https://chandoo.org/wp/wp-content/uploads/2013/11/userform.png)

We are done designing the Userform, now we need to write the code to handle the events.  
Below is the code  
**Close Button**  
`    Private Sub cmdClose_Click()   Unload Me   End Sub    `  
**Userfrom**  
`   Private Sub UserForm_Initialize()   'matching the date in the calendar with the date of the active cell   'if there is a date,   If IsDate(ActiveCell.Value) Then   Me.MonthView1.Value = ActiveCell.Value   Else   Me.MonthView1.Value = Now   End If   End Sub`

`Private Sub MonthView1_DateClick(ByVal DateClicked As Date)   On Error Resume Next   Dim cell As Object   For Each cell In Selection.Cells   cell.Value = DateClicked   Next cell   Unload Me   End Sub   `

What the above code does?
-------------------------

1\. The close button code will simply unload the userform and take it off the screen.  
2\. The userform initialize event code will check if the current cell on which we are right clicking the mouse contains any date, if there is a date then it will set the date on the calendar as the one on the cell, otherwise it will show today’s date.  
3\. The dateclick event of the Monthview control occurs when we click on any date, this code is responsible for populating the cell with the date we have selected. If there are multiple cells selected the code will populate all of them with the date selected.

Adding the context menu option
------------------------------

Now comes the interesting part of adding the context menu option, one thing I would like to specify here as the name suggests “Context menu” these options change depending on what and where we are right clicking the mouse. You will see a different context menu when you right click on a cell, table, shape etc. as shown in the example below  
![sample_right_click_context_menu](https://chandoo.org/wp/wp-content/uploads/2013/11/sample_right_click_context_menu.png)

Since every object has a different type of context menu associated we need to make site we are adding our option to the right place.  
I would recommend reading this article to know more about the types of commandbars available and how to use them. [http://msdn.microsoft.com/en-us/library/office/aa141001(v=office.10).aspx](http://msdn.microsoft.com/en-us/library/office/aa141001(v=office.10).aspx)

Also this link provides a list of available names [http://www.mrexcel.com/forum/excel-questions/525939-visual-basic-applications-list-available-commandbars-excel-2010-a.html](http://www.mrexcel.com/forum/excel-questions/525939-visual-basic-applications-list-available-commandbars-excel-2010-a.html)

We wanted to add the right click context option to a data table which is called as “List Range Popup”.

### Create a Data Table

Type the heading in Cells  
B2 = ID  
C2 = Start Date  
D2 = End Date  
E2 = Name

Now click on cell B2, and press CTRL + T shortcut from the keyboard. Make sure to select the option My Table has headers and then click Ok.

We would need the add the below code to the Open event of our workbook so that this option is available to us every time we need to work here.

`    Private Sub Workbook_Open()   On Error Resume Next   Dim NewControl As CommandBarControl   Application.OnKey "+^{C}", "Module1.OpenCalendar"   Application.CommandBars("List Range Popup").Controls("Insert Date").Delete   Set NewControl = Application.CommandBars("List Range Popup").Controls.Add(Before:=1)   With NewControl   .Caption = "Insert Date"   .OnAction = "Module1.OpenCalendar"   .BeginGroup = True   End With   End Sub    `  
We have also assigned a shortcut key of CTRL + SHIFT + C to this, for those who love to work more using the keyboard.

The above code will add the “Insert Date” context menu option to our data table(s) in the active workbook whenever we open this file.

Next is cleanup  
We need to make sure that the context menu we have added is also removed when the file is close, the below code will do that for us.  
`    Private Sub Workbook_BeforeClose(Cancel As Boolean)   On Error Resume Next   Application.OnKey "+^{C}"   Application.CommandBars("List Range Popup").Controls("Insert Date").Delete   End Sub    `  
**Note:** I have seen the project code left over in the VBA project explorer even after we have close this file, and did some research on the same. The common reason for this is having some COM addins installed. Please share if you also run into this issue and if you were able to find any other reasons or ways to eliminate this issue.

Download Demo File
------------------

[Click here to download the demo file](https://chandoo.org/wp/wp-content/uploads/2013/11/right_click_context_menu.xlsm)
 & use it to understand this technique.

**What about you?** Do you use them often? Please share your experiences, techniques & ideas using comments.

If you are new to VBA, Excel macros, go thru these links to learn more.

*   [What is VBA & Macros? Introduction](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/)
    
*   [Excel VBA Example Macros](http://chandoo.org/wp/excel-vba/examples/)
    
*   [VBA tutorial videos](http://chandoo.org/wp/excel-vba/videos/)
    

Join our VBA Classes
--------------------

If you want to learn how to develop applications like these and more, please consider joining our VBA Classes. It is a step-by-step program designed to teach you all concepts of VBA so that you can automate & simplify your work.

[**Click here to learn more about VBA Classes & join us**](http://chandoo.org/wp/vba-classes/)
.

About Vijay
-----------

Vijay (many of you know him from VBA Classes), joined chandoo.org full-time this February. He will be writing more often on using VBA, data analysis on our blog. Also, Vijay will be helping us with consulting & training programs. You can email Vijay at sharma.vijay1 @ gmail.com. **If you like this post, say thanks to Vijay.**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [41 Comments](https://chandoo.org/wp/pop-up-calendar-excel-vba/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/pop-up-calendar-excel-vba/#respond)
    
*   Tagged under [advanced vba](https://chandoo.org/wp/tag/advanced-vba/)
    , [Automation](https://chandoo.org/wp/tag/automation/)
    , [calendar](https://chandoo.org/wp/tag/calendar/)
    , [context menu](https://chandoo.org/wp/tag/context-menu/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [userform](https://chandoo.org/wp/tag/userform/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousReplace formulas with values using this shortcut \[quick tip\]](https://chandoo.org/wp/replace-formulas-with-values/)

[NextThank you Sachin \[a small tribute\]Next](https://chandoo.org/wp/srt200/)

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

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/pop-up-calendar-excel-vba/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/pop-up-calendar-excel-vba/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/pop-up-calendar-excel-vba/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ