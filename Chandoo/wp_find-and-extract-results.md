# Find them and Extract them - VBA Macro » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/find-and-extract-results

---

*   [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Find them and Extract them – VBA Macro
======================================

*   Last updated on February 10, 2017

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

I started a new consulting gig with NZ Ministry of Business _(aside: when I told my daughter about this, she widened her eyes and said, “ministry of MAGIC!!!”)_. On my first day, while having lunch in breakout area, I chatted with the gentleman sitting opposite me. We got talking about this and that and eventually the topic turned to What I do at MB. So I told him that I am helping the HR with some data analysis and reporting using Excel & SQL Server. He asks me, “So you must be familiar with Excel object model”. I said, “oh, why yes”. He then asks me, “I have this problem that is bothering me for years. You see, I get a lot of data. And I use Find (Ctrl+F) to find all the cells that contain certain code. But the results are all over the place. I want to know **how to extract all the finds to a target worksheet – value & address format**.”

I explained him how to do this while chewing mouthfuls of rice & veggies.

But once I am home, I thought, “hey, maybe there are others out in the world who want to do this”.

![find-and-extract-smith-v4](https://chandoo.org/wp/wp-content/uploads/2017/02/find-and-extract-smith-v4.gif)

So here we go.

### How to find and extract all matching values

Let’s say you have some data in a range like this.

![find-and-extract-data](https://chandoo.org/wp/wp-content/uploads/2017/02/find-and-extract-data.png)

And you want to find all cells with **comp** in them. If the values are all in one column, you could use auto-filter to quickly filter cells with **comp** in them and copy paste them to a target range.You can even automate the steps a bit with **[advanced filter](http://chandoo.org/wp/2011/10/10/how-to-use-advanced-filters/)
.** 

But what if the data can be in any column?

We can use Find (Ctrl+F) to find the values and click on “Find all” to see all results in the find box. But to extract them, we must take the red pill and escape the limitations of Excel to enter in to the exciting world of VBA.

**Here is a quick demo of what our find and extract macro does.**

![find-extract-all-macro-demo](https://chandoo.org/wp/wp-content/uploads/2017/02/find-extract-all-macro-demo.gif)

**Here is the code:**   

    
    Sub findAll()
        Dim findWhat As String, address As String
        Dim fsr As Range, rs As Range, fCount As Long
        
        findWhat = InputBox("Enter what you want to find?", "Find what...")
        
        If Len(findWhat) > 0 Then
            clearFinds
            Set frs = Range("b4").CurrentRegion
            Set rs = frs.Find(What:=findWhat)
            If Not rs Is Nothing Then
                address = rs.address
                Do
                    Range("I5").Offset(fCount).Value = rs.Value
                    Range("J5").Offset(fCount).Value = rs.address
                    Set rs = frs.FindNext(rs)
                    fCount = fCount + 1
                Loop While Not rs Is Nothing And rs.address <> address
            End If
        End If
    End Sub
    

### How does it work?

The code is inspired from [Bill Jelen’s excellent example on Find method on MSDN](https://msdn.microsoft.com/en-us/library/office/ff839746.aspx)
.

The logic goes like this.

1.  We start by asking the user what they want to find and store this in findWhat string variable.
2.  If the string to find is not empty,
3.  We clear any previous find results
4.  We grab the current region for cell B4 (change this to the top-left of your find range)
5.  We look for findWhat in this range using range.Find method
6.  As long as Find result is not empty and not same as the first result
    1.  We copy the value & address to I5 (change this to target range as per your workbook setup)

### Download the Find and Extract workbook

[**Click here to download the example workbook**](https://chandoo.org/wp/wp-content/uploads/2017/02/find-and-extract-all.xlsm)
. Play with the macro to learn its inner workings.

### The rabbit hole is deep, don’t stop just here…

If you enjoyed this little macro, you are going to love VBA. Check out our [free starter tutorial](http://chandoo.org/wp/2011/08/29/introduction-to-vba-macros/)
 or [extensive VBA section](http://chandoo.org/wp/excel-vba/)
 for more.

**How would you find and extract results?**

I thought the Find method approach would be slow, but I am surprised to see that on a medium sized dataset (12000 values), the macro produced results almost instantly. So I would be using it more often to iterate thru a range to find a value.

**What about you?** Do you have such problems at work? Do you use VBA to solve them or just ask colleagues during lunch break and hope for a miracle? Please share your approach in the comments.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [29 Comments](https://chandoo.org/wp/find-and-extract-results/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/find-and-extract-results/#respond)
    
*   Tagged under [do while loop](https://chandoo.org/wp/tag/do-while-loop/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [find](https://chandoo.org/wp/tag/find/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousDesigning awesome financial metrics dashboard \[tutorial\]](https://chandoo.org/wp/financial-dashboard-tutorial/)

[NextUse CTRL to make copies of worksheets quicklyNext](https://chandoo.org/wp/copy-worksheet-shortcut/)

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
    
    [Reply](https://chandoo.org/wp/find-and-extract-results/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/find-and-extract-results/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/find-and-extract-results/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ