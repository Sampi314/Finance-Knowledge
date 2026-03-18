# Consolidate data from different excel files (VBA)

**Source:** https://chandoo.org/wp/consolidate-data-from-different-excel-files-vba

---

*   [Automation](https://chandoo.org/wp/category/automation/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Consolidate data from different excel files (VBA)
=================================================

*   Last updated on April 9, 2012

![Picture of Vijay Sharma](https://secure.gravatar.com/avatar/b8604c6f79c8db3f79e17c562e6f7cd888a268d59501100720b70a6c3046ee1f?s=300&d=mm&r=g)

#### Vijay Sharma

Share

Facebook

Twitter

LinkedIn

_This is a guest post by Vijay, our in-house VBA Expert._

Last week, we learned how to [use SQL and query data inside Excel](http://chandoo.org/wp/2012/04/02/using-excel-as-your-database/ "Using Excel As Your Database")
. This week, lets talk about how we can **use VBA to consolidate multiple data sheets from different workbooks into one single worksheet.**

Consolidate Data Demo
---------------------

First, lets take a look at the consolidate data VBA code.

![Consolidate data from different excel files](https://chandoo.org/wp/wp-content/uploads/2012/04/Consolidate-data-from-different-excel-files.gif "Consolidate-data-from-different-excel-files")

Consolidating Data from different Excel files – the setup
---------------------------------------------------------

There is one master file (or sheet) which needs to be consolidated by pulling data from multiple source files containing raw data (having the same data structure).

_**Lets try to make a generic consolidation macro so that we can use this almost anywhere.**_

We start of by creating a simple table on our sheet, we will call this List.

![Definition List](https://chandoo.org/wp/wp-content/uploads/2012/04/macro-to-copy-table-image.png "macro-to-copy-table-image")

*   On this table essentially we are defining everything that our VBA code needs to know to copy and paste data.
*   We start by telling the name of the Excel workbook and then the complete path (location) of the file.
*   In the next 2 cells we define what are the starting cell and the ending cell that contains our data.
*   Next we are put the name of the worksheet where the data will be pasted. In our example the sheet remains the same however as per your requirements you may put a different sheet name.
*   The last option is to specify where to paste the copied data and we only need to tell the start cell address, the code will automatically select the next empty cell in that column and then paste the data from that point onwards.

Let’s understand the code.
--------------------------

Sub GetData()  
Dim strWhereToCopy As String, strStartCellColName As String  
Dim strListSheet As StringstrListSheet = “List”

On Error GoTo ErrH  
Sheets(strListSheet).Select  
Range(“B2”).Select

‘this is the main loop, we will open the files one by one and copy their data into the masterdata sheet  
Set currentWB = ActiveWorkbook  
Do While ActiveCell.Value <> “”

strFileName = ActiveCell.Offset(0, 1) & ActiveCell.Value  
strCopyRange = ActiveCell.Offset(0, 2) & “:” & ActiveCell.Offset(0, 3)  
strWhereToCopy = ActiveCell.Offset(0, 4).Value  
strStartCellColName = Mid(ActiveCell.Offset(0, 5), 2, 1)

Application.Workbooks.Open strFileName, UpdateLinks:=False, ReadOnly:=True  
Set dataWB = ActiveWorkbook

Range(strCopyRange).Select  
Selection.Copy

currentWB.Activate  
Sheets(strWhereToCopy).Select  
lastRow = LastRowInOneColumn(strStartCellColName)  
Cells(lastRow + 1, 1).Select

Selection.PasteSpecial xlPasteValues, xlPasteSpecialOperationNone  
Application.CutCopyMode = False  
dataWB.Close False  
Sheets(strListSheet).Select  
ActiveCell.Offset(1, 0).Select  
Loop  
Exit Sub

ErrH:  
MsgBox “It seems some file was missing. The data copy operation is not complete.”  
Exit Sub  
End Sub

We have used the Workbook object to accomplish this task and also the Error handler to trap any errors that may come in case any file is missing.

The current code will display a message box when it is not able to open any file and will stop.

We start by assigning the workbook where we want to consolidate the date to the variable currentWB by using the statement:

_Set currentWB = ActiveWorkbook_

After this a looping construct has been used to go through all the inputs provided one by one and open the workbooks, it has been assumed these workbooks to contain on the data that we need to copy hence I did not specify the source sheet name, however this can be easily added to this code to add more functionality.

Inside our loop are the 4 variables which are assigned the  
1) File name,  
2) Copy Range,  
3) Where To Copy and  
4) Which Column contains the starting cell to paste data.

We open the data workbook by using the **Application.Workbooks.Open** method.  
Once we have our first data workbook open, we assign this to the dataWB variable so that we can easily switch between the two workbooks and close them when the operation has been completed.

Next we select the data that has been assigned to the copy range and copy to the clipboard.

We then switch back to our main workbook and select the sheet where we want to paste the data, I have assigned this to the variable called “strWhereToCopy”. This allows us to paste data onto separate sheets within the same workbook.

I have also made use of UDF (user defined function) to find the last cell in the column that we specify.

Once we have found the last row we then select the next empty cell below that and paste our data then.

Additional things that may be used to enhance this code

1\. Since we are using the same instance of Excel we may allow the user to preserve the format of the data being pasted.  
2\. Allow the user with the option to clear data before new is pasted.

Download Consolidate Data from different files Demo file
--------------------------------------------------------

[**Click here to download the workbook**](https://img.chandoo.org/vba/vba-macro-to-copy-data-from-multiple-files.xlsm)
.

Please Note: You would need to create the data files on your system, this download only contains the code template to consolidate.

More on VBA & Macros
--------------------

If you are new to VBA, Excel macros, go thru these links to learn more.

*   [More Examples on Consolidation](http://chandoo.org/wp/tag/consolidation/)
    
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

*   [71 Comments](https://chandoo.org/wp/consolidate-data-from-different-excel-files-vba/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/consolidate-data-from-different-excel-files-vba/#respond)
    
*   Tagged under [advanced vba](https://chandoo.org/wp/tag/advanced-vba/)
    , [consolidate](https://chandoo.org/wp/tag/consolidate/)
    , [consolidation](https://chandoo.org/wp/tag/consolidation/)
    , [copy data](https://chandoo.org/wp/tag/copy-data/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [workbooks](https://chandoo.org/wp/tag/workbooks/)
    
*   Category: [Automation](https://chandoo.org/wp/category/automation/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousThere are Easter eggs in this file!!!](https://chandoo.org/wp/easter-eggs-2012/)

[NextCreating Cash Flow Statement by Indirect Method – INext](https://chandoo.org/wp/creating-cash-flow-statement-by-indirect-method-i/)

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
    
    [Reply](https://chandoo.org/wp/consolidate-data-from-different-excel-files-vba/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/consolidate-data-from-different-excel-files-vba/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/consolidate-data-from-different-excel-files-vba/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ