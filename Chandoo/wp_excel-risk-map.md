# Excel Project Risk Map Generator - using VBA » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-risk-map

---

*   [Automation](https://chandoo.org/wp/category/automation/)
    , [Project Management](https://chandoo.org/wp/category/project-management-2/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Excel Project Risk Map Generator – using VBA
============================================

*   Last updated on August 26, 2019

![Picture of Vijay Sharma](https://secure.gravatar.com/avatar/b8604c6f79c8db3f79e17c562e6f7cd888a268d59501100720b70a6c3046ee1f?s=300&d=mm&r=g)

#### Vijay Sharma

Share

Facebook

Twitter

LinkedIn

_This is a guest post by Vijay, our in-house VBA Expert._

Hello Everyone,

This post shows how to make project risk maps using VBA. _**If you have modern versions of Excel**_ (365, 2019 or 2016 with TEXTJOIN() function), see **[the Excel Risk Map Template page](https://chandoo.org/wp/excel-risk-map-template/)
**.

We all have some projects to manage every now and then and there are needs of various trackers that help us in gauging the progress of the same. One of the most important things are heat maps that quickly help us in visually displaying the names of the projects that need special attention and resolve issues that are impacting them.

So go ahead and grab a cup of coffee and read this article that would help you in creating a Risk Heat Map in excel (will use some double shot espresso in the form of VBA code) to help us to the target.

### Before we begin – Data for Project Risk Maps

First of all we will understand what we are trying to create here by looking at the image below.

![risk-map-project-risks-in-excel](https://chandoo.org/wp/wp-content/uploads/2013/05/risk-map-project-risks-in-excel.png)

You would have seen a picture like this while managing project risks.

So today we will be learn how to create this in Excel to become more awesome in managing projects.

What is important here is how your data for the projects/entities being tracked laid out. We will use the Excel data tables \[[structured references](https://chandoo.org/wp/data-tables/)\
\] to help us here.

![risk_map_data_table](https://chandoo.org/wp/wp-content/uploads/2013/05/risk_map_data_table.png)

There is a Setup sheet in the excel file where we can add the names of the projects that we will use on the data table, as well as the Probability and Impact have been defined as data tables. This helps us in using their contents as drop down options in the data table.

![risk_map_setup_sheet](https://chandoo.org/wp/wp-content/uploads/2013/05/risk_map_setup_sheet.png)

### Adding Named Ranges

We need to use the Name Manager to create named ranges to be able to use the data table columns as drop down items, this is show below.

1.  1.Type this in a blank cell and then copy “=tblProject\[Project\]”.
2.  2.Bring up the Name Manager by pressing CTRL + F3, or by going to the Formula’s Tab and clicking on Name Manager.
3.  3.Click on New
4.  4.Type the name lstProject in the Name box
5.  5.Paste “=tblProject\[Project\]” in the Refers To box and the click on OK.

Repeat this process for “=tblProbability\[Probability\]” and “tblImpact\[Impact\]”

Now you can go the actual risk data table and select the Project columns first blank cell and put in Data Validation List here, choose List and put the Source as lstProject. Repeat this for Probability and Impact cells. You will only need to this one time for the first row, new rows when added to the table will automatically contain these settings.

After we have created the above data table, we need to add 3 columns to the right side where we will setup the calculation that will be used to update the risk map.

a) First Column is named as “ProbabilityScore” Since probability has been marked as “A, B, C or D”, we would need to convert this into a number. This is done by using the below formula.  
\=IFERROR(CHOOSE(MATCH(\[@Probability\],lstProbability,0),4,3,2,1),””)

b) Second Column is named as “SearchString”  
\=IF(\[@Status\]=”Open”,CONCATENATE(“x”,\[@ProbabilityScore\]^4+\[@Impact\]),””)

c) Third column is named as “DisplayName”  
\=CONCATENATE(\[@ID\],” “,LEFT(\[@Project\],20),IF(LEN(\[@Project\])>20,”…”,””))

### Understanding the SearchString Table

When creating the SearchString we are raising the probability score to the power of 4, this is what I have chosen you may select any number that you need. Below is the resulting matrix of numbers that we obtain by doing this.

![risk_map_score_table](https://chandoo.org/wp/wp-content/uploads/2013/05/risk_map_score_table.png)

The last columns in only used for trimming the name of the project to 20 characters of there is a big name, else the actual name of the project is used to display in the Risk Map.

### Understanding the Code

So now we are ready to look into the VBA code that helps us in creating the Risk Map.

`   Public Function showRiskMap(inputRange As Range, searchString As String, dataRange As Range, separator As String)   Dim cntr As Long   Dim tempArray() As Variant   Dim tempDataArray() As Variant   Dim tempString As String`

tempArray = inputRange.Value  
tempDataArray = dataRange.Value

`   `

`For cntr = LBound(tempArray) To UBound(tempArray)   If tempArray(cntr, 1) = searchString Then   tempString = tempString & tempDataArray(cntr, 1) & separator   End If   Next   showRiskMap = tempString   End Function   `

We are sending 4 parameters to this function which are

1.  inputRange – this is the SearchString columns data
2.  SearchString – this is a manual enrty such as “x257”
3.  dataRange – this is the Display Name column from where we will pick the name of the project to display
4.  separator – this is CHAR(10) which is a line break in case we have multiple projects falling in the same category

We are making use of Array’s here to pass the data from the Table column into the array and then a simple For loop to parse them and show us the results.

I hope you will enjoy this article and this assist in managing your projects in a much efficient way.

Download Excel Risk Map File
----------------------------

[**Click here to download the file**](https://chandoo.org/wp/wp-content/uploads/2013/05/Risk_Register_Article_Template.xlsm)
 & use it to understand this technique.

[Click here for Risk Map Template for new versions of Excel](https://chandoo.org/wp/excel-risk-map-template/)
.

Do you use Excel for creating Risk Maps?
----------------------------------------

**Do you also user Excel for creating Risk Maps?** If yes please put in the comment below how do you use the same and what has been your experience. **Leave a comment.**

More on VBA & Macros
--------------------

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

*   [29 Comments](https://chandoo.org/wp/excel-risk-map/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-risk-map/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [project management](https://chandoo.org/wp/tag/project-management/)
    , [risk management](https://chandoo.org/wp/tag/risk-management/)
    , [risk map](https://chandoo.org/wp/tag/risk-map/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    
*   Category: [Automation](https://chandoo.org/wp/category/automation/)
    , [Project Management](https://chandoo.org/wp/category/project-management-2/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousHow to find sum of top 3 values based on filtered criteria](https://chandoo.org/wp/sum-of-top-3-values-meeting-criteria/)

[NextA quick Excel tip while on bike…Next](https://chandoo.org/wp/a-quick-excel-tip-while-on-bike/)

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
    
    [Reply](https://chandoo.org/wp/excel-risk-map/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-risk-map/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-risk-map/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ