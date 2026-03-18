# Excel Hyperlinks, What are they and how to use them in your workbooks.

**Source:** https://chandoo.org/wp/excel-hyperlinks

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Beam Me Up Scotty – Excel Hyperlinks
====================================

*   Last updated on March 31, 2011

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

**What are Hyperlinks ?**
-------------------------

A Hyperlink is a reference to a document, a location or an action that the reader can directly follow by selecting the link.

Hyperlinks are used extensively on the Internet and are generally Words highlighted in [Underlined Blue](http://en.wikipedia.org/wiki/Hyperlink "Hyperlink Definition")
 <– Like that.

The use of Hyperlinks in Excel has been extended to a number of areas and this includes:

*   Opening Files (of any type)
*   Opening Web Pages (Internet or Intranet)
*   Jumping/Navigating to locations within an existing document
*   Creating New Documents (Excel files only)
*   Sending Emails

Microsoft has added the ability to place Hyperlinks,

*   Directly on an Excel worksheet ,
*   Connected to a number of worksheet objects, including shapes, charts and wordart
*   Included as a worksheet formulas.
*   Programmatically using VBA

These 4 methods above will be discussed here.

**Inserting Hyperlinks**
------------------------

As described above there are 4 methods for inserting hyperlinks in an Excel Workbook.

### **Directly on an Excel worksheet**

There are 3 ways to insert a Hyperlink directly into a cell, either:

Right click on the cell and select Hyperlink; or

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-1.png "Hyperlinks 1")](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-1.png)

Use the Insert, Hyperlinks Tab; or

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-2.png "Hyperlinks 2")](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-2.png)

Use a Keyboard Shortcut – **Ctrl K**

### **Connected to a number of worksheet objects, including shapes, charts and wordart**

You can also add a Hyperlink to many objects within Excel including Pictures, Shapes, Text Boxes, Word Art and Charts.

Right clicking a lot of these objects brings up the Objects Shortcuts Menu, select **Hyperlink…**,

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-4.png "Hyperlinks 4")](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-4.png)

or

Select the object, Use the Insert, Hyperlinks Tab; or

Select the Object and Use the Keyboard Shortcut – **Ctrl K**

**Hint:** Right Clicking on Charts Doesn’t Show the Add Hyperlink option, so Select the Chart and **Ctrl K  
**

### **Adding Hyperlinks using Worksheet Formulas.**

Hyperlinks can be added using worksheet formulas.

**\=HYPERLINK( Link Location, Name)**

**Link Location:** This is the path and file name to the document to be opened.

The Link Location can refer to a place in a document – such as a specific cell or named range in an Excel worksheet or workbook, or to a bookmark in a Microsoft Word document. The path can be to a file that is stored on a hard disk drive. The path can also be the path on a server or a URL, HTTP or FTP and a location of an object, document, World Wide Web page, or other destination on the Internet or an intranet. The Link Location can be a text string enclosed in quotation marks or a reference to a cell that contains the link as a text string.

**Name**: This is the text or value that is displayed in the cell.  The Name is displayed in blue and is underlined.

Eg:

**Jump to a cell on Another sheet**

\=HYPERLINK(Sheet3!B3,”Monthly Budget”)

The above  will add a Hyperlink, titled “Monthly Budget” and link to Sheet3!B3 of the current workbook

**Jump to a Named Range on Another sheet**

\=HYPERLINK(Budget,”Yearly Budget”)

The above  will add a Hyperlink, titled “Yearly Budget” and link to the Named Range “Budget” of the current workbook

**Open a File on a network Drive**

\=HYPERLINK(“//Server01\\01 Administration\\Administration.docx”,”Open Admin File”)

The above  will add a Hyperlink, titled “Open Admin File” and link to the file at: //Server01\\01 Administration\\Administration.docx

**Open a File on a network Drive at a specific bookmark**

\=HYPERLINK(“\[//Server01\\01 Administration\\Administration.docx\]Contents”,”Open Admin File @ TOC”)

The above  will add a Hyperlink, titled “Open Admin File @ TOC” and link to the Named Section “Contents” of the file at: //Server01\\01 Administration\\Administration.docx

**Jump to a Web Page**

\=HYPERLINK(“http://chandoo.org/wp/”,”Goto Chandoo.org”)

The above  will add a Hyperlink, titled “Goto Chandoo.org” and link to [http://chandoo.org/wp/](http://chandoo.org/wp/ "Chandoo.org")

**Send an Email**

\=HYPERLINK(“mailto:chandoo.d@gmail.com”,”Email Chandoo”)

The above will add a Hyperlink, titled “Email Chandoo” and send an email to chandoo.d@gmail.com

### **Adding Hyperlinks Programmatically using VBA**

Hyperlinks can be added to a worksheet or a worksheet object programmatically using some simple code

Sheets(**SheetName**).Hyperlinks.Add Anchor:=Sheets(**SheetName**).Range(**Range**), Address:=””,  SubAddress:=”**Address!Range**“,  TextToDisplay:=**Name**

Where:

**SheetName**: The Name of the Sheet where the Hyperlink is to go

**Range**:  The Range where the Hyperlink is to go

**Address!Range**: The address and Range linked to in the Hyperlink

**Name**: The Display Name of the Hyperlink

**Types of Hyperlinks**
-----------------------

There are 5 Types of Hyperlinks which Excel offers, each is described below:

*   Existing File
*   Existing Web Page
*   Place in This Document
*   Create a New Document
*   Send an Email Link

### **Existing File**

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-5a.png "Hyperlinks 5a")](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-5a.png)

Select the existing File or Web Page icon in the Link to: area

Navigate to the existing file using the Look in: area of the dialog

Add your Display Text in the Text to display: area

Add a ScreenTip…, a Tip which is displayed when you hover the mouse over a Hyperlink

Use the **Bookmark…** button to jump to predefined Named Ranges and common Cell References dialog

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Bookmarks.png "Bookmarks")](https://chandoo.org/wp/wp-content/uploads/2011/03/Bookmarks.png)

### **Existing Web Page**

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-5b.png "Hyperlinks 5b")](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-5b.png)

Select the **Existing File or Web Page** icon in the Link to: area

Navigate to the existing file using the **Look in:** area of the dialog

Add your Display Text in the **Text to display:** area

Add a **ScreenTip**…, a Tip which is displayed when you hover the mouse over a Hyperlink

### ****Place in This Document****

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-5c.png "Hyperlinks 5c")](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-5c.png)

Select the **Place in this Document** icon in the Link to: area

Type in Cell Reference using the **Type in Cell Reference**: area of the dialog or select a Defined Names in the **Defined Names** area

Add your Display Text in the **Text to display**: area

Add a **ScreenTip**…, a Tip which is displayed when you hover the mouse over a Hyperlink

### 

### **Create a New Document**

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-5d.png "Hyperlinks 5d")](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-5d.png)

Select the **Create New Document** icon in the Link to: area

Type in the Name of the New Document in the **Name of the New Document**: area of the dialog.

Add your Display Text in the **Text to display**: area

Add a **ScreenTip**…, a Tip which is displayed when you hover the mouse over a Hyperlink

You can choose wether to Edit the File Now or Later in the **When to Edit** area

### **Send an Email Link**

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-5e.png "Hyperlinks 5e")](https://chandoo.org/wp/wp-content/uploads/2011/03/Hyperlinks-5e.png)

Select the **Email Address** icon in the Link to: area

Type in the Email Address in the **Email Address**: area of the dialog.

Add your Display Text in the **Text to display**: area

Add your Email Subject in the **Subject**: area

Add a **ScreenTip**…, a Tip which is displayed when you hover the mouse over a Hyperlink.

**Editing Hyperlinks**
----------------------

Once you have a hyperlink established you can edit the hyperlink by right click on the hyperlink and select Edit Hyperlink

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Edit-Hyperlinks.png "Edit Hyperlinks")](https://chandoo.org/wp/wp-content/uploads/2011/03/Edit-Hyperlinks.png)

The Edit Hyperlink dialog will vary depending on the type of Hyperlink as described above.

**Deleting Hyperlinks**
-----------------------

Once you have a hyperlink established you can delete the hyperlink by right click on the hyperlink and select Remove Hyperlink

[![](https://chandoo.org/wp/wp-content/uploads/2011/03/Remove-Hyperlinks.png "Remove Hyperlinks")](https://chandoo.org/wp/wp-content/uploads/2011/03/Remove-Hyperlinks.png)

**Hyperlink Uses**
------------------

Hyperlink can be used for a number of uses as described above.

### Tables of Contents

One common use of hyperlinks is the creation of Tables of Contents.

The construction of a Table of Contents page was discussed here [Table of Contents](http://chandoo.org/wp/2009/02/16/excel-table-of-contents-etc/ "Table of Contants at Chandoo.org")

The construction of Tables of Contents can also be automated using some simple VBA.

So instead of reinventing the wheel I will direct you to The Microsoft Office Blog where Tables of Conents were recently discussed.

[Table of Contents 1](http://blogs.office.com/b/microsoft-excel/archive/2010/04/07/add-a-table-of-contents-to-your-workbook.aspx "Table of Contents via VBA 1")
 or [Table of Contents 2](http://blogs.office.com/b/microsoft-excel/archive/2010/04/30/creating-a-toc-with-hyperlinks-programmatically.aspx "Table of Contents via VBA 2")

### **Dealing with Lots of Hyperlinks**

The following 2 posts at [http://chandoo.org/forums](http://chandoo.org/forums/ "Chandoo.org/Forums")
 have solved users problems and will easily be adapted to other Hyperlink issues

**Find Dead Hyperlinks**

[http://chandoo.org/forums/topic/check-broken-external-hyperlinks](http://chandoo.org/forums/topic/check-broken-external-hyperlinks "Find Dead Hyperlinks")

**Edit Hyperlinks**

[http://chandoo.org/forums/topic/marco-for-editing-link-in-workbook](http://chandoo.org/forums/topic/marco-for-editing-link-in-workbook "Edit Hyperlinks")

**How have you used Hyperlinks?**
---------------------------------

How have you used Hyperlinks?

Let us all know in the comments below:

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [85 Comments](https://chandoo.org/wp/excel-hyperlinks/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-hyperlinks/#respond)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousForm Controls – Adding Interactivity to Your Worksheets](https://chandoo.org/wp/form-controls/)

[NextMarch 2011 is best month ever and other newsNext](https://chandoo.org/wp/march-2011-is-best-month-ever-and-other-news/)

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
    
    [Reply](https://chandoo.org/wp/excel-hyperlinks/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-hyperlinks/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-hyperlinks/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ