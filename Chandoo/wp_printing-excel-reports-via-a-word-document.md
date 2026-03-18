# Printing Excel data via a Word Document

**Source:** https://chandoo.org/wp/printing-excel-reports-via-a-word-document

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Printing Excel Reports via a Word Document
==========================================

*   Last updated on February 18, 2011

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Printing Excel Reports via a Word Document
------------------------------------------

**Using Microsoft Excel & Word  
**

This post will detail the process of establishing a simple database in excel and then linking that to a Standard Report in word and saving the data as a new Word file.

**Why use Word?**

Some organisations will only accept files in Word format and may have specific formats which are used internationally (International shipping I’m looking at you!)

In these cases although you may be able to setup an Excel file to look exactly like its Word equivalent. But if they wont accept it…

You have to change.

**Requirements:**

\+ A database source in Excel  
\+ A Word file (to be used as a template, not to be confused with a Word template)  

**The Process**
---------------

The process is simply a matter of:

\+ Setup a Control sheet  
\+ Setup a Transfer Sheet  
\+ Setup a Word template  
\+ Run the Report

This process will be explained step by step with the help of a worked example:  [2007/10 Sample](https://chandoo.org/wp/wp-content/uploads/2011/02/Transfer-Excel-Data-to-Word-07-10.zip "2007/10 Sample")
 or [1997/03 Sample](https://chandoo.org/wp/wp-content/uploads/2011/02/Transfer-Excel-Data-to-Word-97-XP.zip "1997/XP Example")

This tutorial will only be using the 2007/10 files as examples but feel free to follow along if you are using previous versions.

The 2007/10 Sample has been tested on both Office 2007 & 2010  
The 1997/03 Sample has been tested on Office XP (and I make no claim that it will work in prior versions but it might/should)

Open the example workbook (Production records.xlsm from the above links) or your own data file.

Notice that there are 3 worksheets in the workbook:

\+ Control:   The master sheet which allows selection of your filter or summation criteria and a button to execute a macro  
\+ Transfer: The transfer sheet, the entry or summation here will be transferred to word  
\+ Data:        The database

### **Setup a Control Sheet**

The control sheet is a simple data validation or selection tool and a button which will run a macro.

It can be as simple or as complex as you need to make it.

Example

[![](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord01.png "ExceltoWord01")](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord01.png)

In the example above there is simply a Data Validation cell which is linked to a list of shipment numbers and a Button to run the reports VBA subroutine.

You can make yours as simple or as complex as you need to extract the data from your data source.

The **Produce Word Report** button is linked to the MergeMe VBA subroutine.

### **Setup a Transfer Sheet**

The Transfer sheet requires 2 rows

Row 1: Has a list of field names, These will be used in Word later so use something meaningful.  
Row 2: Has a list of the records which will be transferred to Word. The cells will contain sufficient formulas to extract the relevant records from the Data sheet using the Data validation on the Control Sheet.

You need to setup sufficient fields to ensure that all records required in Word are setup or retrieved.

The order of the fields isn’t important as the field names are used for the transfer not the order.

Also you don’t have to use all the fields in Word, but if the Field isn’t made here you can’t retrieve it later.

The format or layout doesn’t matter as this is controlled in Word.

Example

Notice on the Transfer sheet that the Top Row is a list of field names

The second row uses an **Index(Match( ))** combination to retrieve the relevant records from the Data sheet.

[![](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord02.png "ExceltoWord02")](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord02.png)

Save the Excel file.

In the sample file I have made a simple retrieval of a matching records and associated fields, but the Transfer sheet could have just as easily sumarised multiple rows of data from your data source.

### **Setup a Word template**

Setup in word a file which will be used as a template for the import.

Leave gaps where your fields values will go.

Save the file

Example

Open the example file (**Shipping Template.docx**)

If this is the first time you have opened the example file it may prompt you

“Opening this file will run the following SQL File …”

[![](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord03.png "ExceltoWord03")](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord03.png)

This is ok so accept Yes

You can either accept that and then follow the links to connect the file to the **Production records.xlsm** file

It will then prompt you for the Data Table which in our case is **Transfer$** ie: the Sheet Name with a $ sign at the end

[![](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord04.png "ExceltoWord04")](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord04.png)

If it didn’t prompt you above or you answered No to the “Opening this file will run the following SQL File …” prompt we will connect again later anyway.

Now setup the file in word with all the text graphics, lines colors etc required for your form/report.

Leave gaps for the fields which we will add next.

**Adding fields**

Use mail merge to open the data source (**Production records.xlsm**)

Goto Mailings, Select Recipients, Use Existing List…

[![](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord07.png "ExceltoWord07")](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord07.png)

Navigate to the **Production Records.xlsm** file after which it will prompt you for the table which in our case is **Transfer$** ie: the Sheet Name with a $ sign at the end (as discussed above)

Move to the 4 missing Field Locations as per the following table and insert the Field Names using the

Mailings, Insert Merge Field tab

[![](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord06.png "ExceltoWord06")](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord06.png)

Insert Fields as per the following table and highlights above:

|     |     |
| --- | --- |
| **Location** | **Field Name (from Production Records.xlsm)** |
| Shipment No : | Shipment\_No |
| Material : | Cargo |
| Tonnes : | Tonnes |

The other fields Destination, Form and Date have already been pre-entered and are shown in Blue

You can format the fields as required, select the entire field and change the font, colors etc to suit.

You can view the field values using the Preview Results Button, see below

[![](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord09.png "ExceltoWord09")](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord09.png)

Make any other changes to the file

Save the file as a Word File **Shipping Template.docx** (not as a Word Template \*.dotx)

Close Word

**Run the Report**

In the **Production records.xlsm** file we will now link the macro to the button on the control sheet

We need to check 3 lines in the macro before we execute it.

Goto VBA using Alt F11

[![](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord10a.png "ExceltoWord10a")](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord10a.png)

Select the **Production Records.xlsm**, **Modules** on the left and find the

Sub MergeMe() Subroutine on the right

Near the top of the subroutine are 2 lines which list both the file which Word will use as a template and what the new file will be saved as after merging.

‘ Setup filenames

Const WTempName = “**Shipping Template.docx**“ ‘This is the Word Templates name, Change as req’d

Const NewFileName = “**New Certificate.docx**” ‘This is the New Word Documents File Name, Change as req’d

Change these values as appropriate

The code will overwrite the existing output file if it exists so once executes save it to another name/location.

If you are using your own data file copy this subroutine to your own VBA Module and edit as above.

You can now go back to Excel (Alt F11) and execute the macro using the button on the control page.

You should now have a new file called New Certificate.docx in the same directory as the Sample files.

[![](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord11.png "ExceltoWord11")](https://chandoo.org/wp/wp-content/uploads/2011/02/ExceltoWord11.png)

Future Extensions
-----------------

The above macro which does this transfer is a simple and easily scalable to 50+ fields without any modification.

Future enhancements would be:

\+ Sourcing the New Word File name from the Control sheet

\+ Incremental numbering of the word document each time the transfer is done

\+ Numbering of the word document based on a Field value each time the transfer is done

\+ Export of Multiple records at one time

\+ Conditional formatting in Word based on field values

\+ Improved error checking

If you are interested I encourage you to modify and post these enhancements here for all to benefit.

### Macro

You can copy the Macro into any Excel file and save it as an \*.xlsm file and link it to a Button and be up and running in minutes

The macro has a very small number of changes that need making internally to work anywhere.

What have been your Excel to Word transfer experiences ?
--------------------------------------------------------

What have been your Excel to Word transfer experiences, let us know in the comments below:

What do you think of this approach to data transfer ?

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [87 Comments](https://chandoo.org/wp/printing-excel-reports-via-a-word-document/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/printing-excel-reports-via-a-word-document/#respond)
    
*   Tagged under [Automation](https://chandoo.org/wp/tag/automation/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [hui](https://chandoo.org/wp/tag/hui/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [print](https://chandoo.org/wp/tag/print/)
    , [Reports](https://chandoo.org/wp/tag/reports/)
    , [Transfer](https://chandoo.org/wp/tag/transfer/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [Word](https://chandoo.org/wp/tag/word/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousModeling Interest During Construction (IDC) – Excel Project Finance](https://chandoo.org/wp/modeling-interest-during-construction/)

[NextDetails about upcoming Financial Modeling SchoolNext](https://chandoo.org/wp/financial-modeling-school-b2-details/)

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
    
    [Reply](https://chandoo.org/wp/printing-excel-reports-via-a-word-document/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/printing-excel-reports-via-a-word-document/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/printing-excel-reports-via-a-word-document/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ