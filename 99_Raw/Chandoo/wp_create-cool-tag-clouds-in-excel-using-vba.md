# Create Cool Tag Clouds in Excel using VBA » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/create-cool-tag-clouds-in-excel-using-vba

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [technology](https://chandoo.org/wp/category/computer/)
    

Create Cool Tag Clouds in Excel using VBA
=========================================

*   Last updated on April 22, 2008

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

![](https://chandoo.org/wp/wp-content/uploads/2008/04/create_tag_clouds_excel.png "create_tag_clouds_excel")

I was toying with the idea of **creating a tag cloud in excel – as a form of new visualization,** this could be useful when you have medium amounts of data (eg: 50-300 rows) and you want to emphasize on what is important and what is not. I would imagine using a tag-cloud,

*   When you are listing features of your software
*   When you are listing your sales figures across top 1000 cities of your country
*   When you are analyzing visitor data to your web start up

My goal is to generate a tag cloud from a selected data table (with just 2 columns, one with text to display, the other with any number on it) as shown below:  
![tag clouds in excel how to?](https://chandoo.org/wp/wp-content/uploads/2008/04/tag_cloud_table_format.gif "tag_cloud_table_format")

* * *

**[Download and play with a sample tag cloud visualization I have created](https://chandoo.org/wp/wp-content/uploads/2008/04/tagcloud-in-excel.xls)
**

* * *

Since anything related to changing cell formats is not possible using functions, I had to write a VBA Macro (a subroutine that you would write in your excel sheet to achieve a task). The logic is simple:

> 1\. Read the selected table and create 2 arrays, 1 with tags and another with the numeric data  
> 2\. Select an empty cell in the work book (I choose E10)  
> 3\. For each item in tags array:  
> – Add text to the selected cell  
> – set its font size based on normalized value between 6 and 20

_**The code is shown below:**_

> Sub createCloud()  
> ‘ this subroutine creates a tag cloud based on the list format tagname, tag importance  
> ‘ the tag importance can have any value, it will be normalized to a value between 8 and 20
> 
> On Error GoTo tackle\_this
> 
> Dim size As Integer
> 
> size = Selection.Count / 2
> 
> Dim tags() As String  
> Dim importance()
> 
> ReDim tags(1 To size) As String  
> ReDim importance(1 To size)
> 
> Dim minImp As Integer  
> Dim maxImp As Integer
> 
> cntr = 1  
> i = 1
> 
> For Each cell In Excel.Selection
> 
> If cntr Mod 2 = 1 Then  
> taglist = taglist & cell.Value & “, ”  
> tags(i) = cell.Value  
> Else  
> importance(i) = Val(cell.Value)  
> If importance(i) > maxImp Then  
> maxImp = importance(i)  
> End If  
> If importance(i) < minImp Then minImp = importance(i) End If i = i + 1 End If cntr = cntr + 1 Next cell ' paste values in cell e10 Range("e10").Select ActiveCell.Value = taglist ActiveCell.Font.size = 8 strt = 1 For i = 1 To size With ActiveCell.Characters(Start:=strt, Length:=Len(tags(i))).Font .size = 6 + Math.Round((importance(i) - minImp) / (maxImp - minImp) \* 14, 0) .Strikethrough = False .Superscript = False .Subscript = False .OutlineFont = False .Shadow = False .Underline = xlUnderlineStyleNone .ColorIndex = xlAutomatic End With strt = strt + Len(tags(i)) + 2 Next i Exit Sub tackle\_this: ' errors handled here 'MsgBox "You need to select a table so that I can create a tag cloud", vbCritical + vbOKOnly, "Wow, looks like there is an error!" End Sub

This code is totally reusable. Just right click on the sheet name at bottom & select “view code”. In the VBA Editor create a new module (Menu > Insert > module) and Paste the above code there. Go back to your excel sheet and select a 2 columned data table and run the createCloud macro. The cloud will be created and pasted in cell E10. You can change this by modifying the line _Range(“e10”).Select_.

* * *

**[Download the above code and an example in an excel](https://chandoo.org/wp/wp-content/uploads/2008/04/tagcloud-in-excel.xls)
**

* * *

**Happy charting 🙂**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [43 Comments](https://chandoo.org/wp/create-cool-tag-clouds-in-excel-using-vba/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/create-cool-tag-clouds-in-excel-using-vba/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [cool](https://chandoo.org/wp/tag/cool/)
    , [howto](https://chandoo.org/wp/tag/howto/)
    , [ideas](https://chandoo.org/wp/tag/ideas/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macro](https://chandoo.org/wp/tag/macro/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [MS](https://chandoo.org/wp/tag/ms/)
    , [tag cloud](https://chandoo.org/wp/tag/tag-cloud/)
    , [technology](https://chandoo.org/wp/tag/technology/)
    , [tips](https://chandoo.org/wp/tag/tips/)
    , [tricks](https://chandoo.org/wp/tag/tricks/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [visualiztion](https://chandoo.org/wp/tag/visualiztion/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [ideas](https://chandoo.org/wp/category/ideas/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [technology](https://chandoo.org/wp/category/computer/)
    

[PrevPreviousDo not disturb : I am scheduling a meeting](https://chandoo.org/wp/do-not-disturb-i-am-scheduling-a-meeting/)

[NextHot Fuzz – must watch for comedy loversNext](https://chandoo.org/wp/hot-fuzz-must-watch-for-comedy-lovers/)

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
    
    [Reply](https://chandoo.org/wp/create-cool-tag-clouds-in-excel-using-vba/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/create-cool-tag-clouds-in-excel-using-vba/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/create-cool-tag-clouds-in-excel-using-vba/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ