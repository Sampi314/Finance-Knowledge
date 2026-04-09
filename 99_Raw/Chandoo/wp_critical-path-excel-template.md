# Excel Critical Path Calculator - FREE Template (Project Mgmt)

**Source:** https://chandoo.org/wp/critical-path-excel-template

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Project Management](https://chandoo.org/wp/category/project-management-2/)
    

Calculating Critical Path using Excel Formulas \[Project Management\]
=====================================================================

*   Last updated on October 2, 2023

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Do you know that we can easily _**calculate the critical path for a project using Excel formulas**_?

For a long time, it has been tricky to calculate the **Critical Path** using Excel formulas. But thanks to the arrival of new Dynamic Array functionality in Excel, we can now calculate critical path. In this article let me describe the approach with an example.

Put on your hardhats, this one is going to blow your minds.

What is Critical Path Method (CPM)?
-----------------------------------

Critical Path Method gives us a framework to analyze and optimize a project plan. Let’s say you have a project with 6 activities, as depicted below. Then we can find a critical path that determines the total duration of the project using Critical Path Method.

![](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2938.png)

> The critical path is the longest sequence of tasks that must be completed to execute a project. The tasks on the critical path are called critical activities because if they’re delayed, the whole project completion will be delayed.
> 
> [ProjectManager.com](https://www.projectmanager.com/guides/critical-path-method)

How do you calculate the Critical Path?
---------------------------------------

To calculate the critical path, you need below details about the project plan:

*   Complete list of all planned activities
*   Estimated duration for all activities (t)
*   Dependencies for each activity 

In many real-world scenarios, accurately listing all three of them is impossible. And that is why CPM technique is often criticized.

Once you have all of them, we need to apply **critical path algorithm** to calculate below 5 values.

*   Earliest Starting time (ES): This is maximum Earliest Finish (EF) of all predecessors of an activity. 
*   Earliest Finish time (EF): This is ES + duration of the activity (t)
*   Latest Finish time (LF): This is the minimum Latest Start time (LS) of all successors of an activity. 
*   Latest Starting time (LS): This is LF – duration of the activity (t)
*   Float or Slack (F): This is the gap between Latest Start (LS) and Earliest Start (ES). For activities on _**critical path**_ this value would be 0.

Learn more about Critical Path Method:

*   [ABCs of Critical Path Method (hbr)](https://hbr.org/1963/09/the-abcs-of-the-critical-path-method)
    
*   [Critical Path Method (ProjectManager)](https://www.projectmanager.com/guides/critical-path-method)
    

Critical Path Calculations with an Example
------------------------------------------

Let’s go back to our 6 activity project. We can assign durations for each activity like this:

![project plan (critical path analysis with Excel)](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2939.png)

We can use below notation when capturing this data in Excel table.

![Excel table format for critical path input data](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2940.png)

### Calculating ES, EF, LS, LF & Float with Formulas

Formulas need Excel 365! These formulas work only in Excel 365. ×

Adjacent to the input data table, add 6 columns for all our calculations. Our table should look like this:

![CPM Calculations in Excel - table format](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2941.png)

Now, lets understand the formulas for Successors, Early Start (ES), Early Finish (EF), Latest Start (LS) and Latest Finish (LF).

Early Start Formula (ES)

Early Start is the earliest an activity can begin. An activity can only start when all of its predecessors have finished. So this is same as the _**maximum**_ of **Early Finish (EF)** for all the predecessors. If an activity has no predecessors, then it can start right away.

As we have the list of predecessors in the cell \[@Predecessors\], we can loop thru them and find the maximum finish time for them.

Here is the formula I used.

				
					`=IF([@Predecessors]="",0, MAX(CHOOSEROWS([EF],TEXTSPLIT([@Predecessors],",")+0)))`
				
			

_**For activities without predecessors,**_ we set the value of ES as 0.

For all other activities, we split the \[@Predecessors\] by comma (using TEXTSPLIT) and convert these text values to numbers (by adding a 0 to them). We then pick the maximum of all these activity’s earliest finish time \[EF\] using MAX & CHOOSEROWS functions.

Early Finish Formula (EF)

**_This is easy._** We just add duration to early start (ES).

				
					`=[@ES]+[@[Estimated Duration]]`
				
			

🤔Did you notice the circular nature of these formulas?

![](https://chandoo.org/wp/wp-content/uploads/2023/09/frustrated-ugh.gif)

Even though ES formula depends on EF and EF formula depends on ES (head hurts, _innit_?), you need not worry. Excel will calculate both of these values fine as long as there are no _**loops**_  in your project data (_ie._ Activity 1 depends on 2 and 2 depends on 1)

Successors Formula

Before we calculate the Latest Start (LS) and Latest Finish (LF) times, it is a good idea to calculate the list of successors for each activity. 

I used this formula for that:

				
					`=TEXTJOIN(",",TRUE,FILTER([ID],IFERROR(BYROW([Predecessors],LAMBDA(a, OR(TEXTSPLIT(a, ",")+0=[@ID]))),FALSE),""))`
				
			

**How it works?**

For each activity, the list of successors is defined as all the activities that begin immediately after that activity.

So for example, going back to our image of project plan (see below),

![project plan (critical path analysis with Excel)](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2939.png)

the list of successors for _**activity 1**_ is {2,3}

To obtain this list for a given activity **x:**

*   We need to filter all the activities
*   where **x** is one of the predecessors

 We can use a cocktail of FILTER(), BYROW(), LAMBDA() and TEXTSPLIT() for this.

Here is the basic approach:

1.  We filter the \[ID\] column
2.  by checking for each row (hence BYROW)
3.  if the \[Predecessor\]s has the \[@ID\]
4.  To perform the check, we first split the _predecessors_ using TEXTSPLIT
5.  and then compare if any of them equal to \[@ID\]
6.  At the end of this BYROW looping, we end up with either TRUE or FALSE values against each \[ID\]
7.  After filter fetches all the _successors,_ we just apply TEXTJOIN to combine them to a list. For ex: 2,3

Latest Finish Formula (LF)

**Latest Finish (LF)** is defined as the latest an activity can finish without derailing the project.

_**For the activities without any successor****s,** this is same as **EF**._

For all other activities, we look for the minimum (earliest) LS value of all it’s successors.

Here is the formula:

				
					`=IF([@Successors]="",[@EF],MIN(CHOOSEROWS([LS],TEXTSPLIT([@Successors],",")+0)))`
				
			

**How this formula works?**

If an activity has no successors (**_ie_** _it is last activity in the project diagram)_ we set LF as EF.

For all other activities, we split the \[@Succssors\] by comma (using TEXTSPLIT) and convert these text values to numbers (by adding a 0 to them). We then pick the minimum of all these activity’s Latest Start time \[LS\] using MIN & CHOOSEROWS functions.

Latest Start Formula (LS)

This is Latest Finish (LF) minus Duration (T)

				
					`=[@LF]-[@[Estimated Duration]]`
				
			

Float (or Slack)

Now that we have all the calculations done, we can figure out the float (or slack) for each activity. This is the difference between Latest Start (LS) and Earliest Start (ES) for an activity. 

				
					`=[@LS]-[@ES]`
				
			

Findout out which activities are on Critical Path
-------------------------------------------------

![](https://chandoo.org/wp/wp-content/uploads/2023/09/2023-09-20_11-30-02.gif)

Any activity with ZERO (0) float is on the critical path. It means, there is no wiggle room for that activity. 

We can use Excel’s conditional formatting feature to visually identify all such activities.

1.  Select the table and add a new conditional formatting rule (formula based)
2.  Use the rule float\_column=0 and set the necessary formatting. (see my rule in the below screenshot).

![](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2951.png)

Here is my final project plan table with critical path activities identified.

![](https://chandoo.org/wp/wp-content/uploads/2023/09/SNAG-2952.png)

Critical Path Analysis with Excel - FREE Template
-------------------------------------------------

[![](https://chandoo.org/wp/wp-content/uploads/2023/10/SNAG-2987.png)](https://chandoo.org/wp/wp-content/uploads/2023/10/Critical-path-analysis-Excel.xlsx)

[Please download my FREE Critical Path Analysis Template](https://chandoo.org/wp/wp-content/uploads/2023/10/Critical-path-analysis-Excel.xlsx)
 and use your own data to calculate the _**critical path**_ _automatically._

Critical Path Calculations in Excel - Watch the Video
-----------------------------------------------------

Still confused about these calculations? I made a video explaining the CPM concept & Excel formulas. Check it out below or [on my YouTube Channel](https://youtu.be/hltpHtza0BU)
.

More on Project Management using Excel
--------------------------------------

If you are a project manager, you are going to love my site. I have articles & templates on all aspects of Project Management. Check them out below:

[![project management dashboard - finalized](https://chandoo.org/wp/wp-content/uploads/2021/06/project-management-dashboard-finalized.png)](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)

*   [Interactive Gantt Chart Template with Excel](https://chandoo.org/wp/drill-down-gantt-chart-template/)
    
*   [Quick & easy Gantt Chart in Excel](https://chandoo.org/wp/quick-gantt-chart-excel-template/)
    
*   [Project Timeline Chart with Excel](https://chandoo.org/wp/project-milestones-in-timeline/)
    
*   [Project Management Dashboard with Excel](https://chandoo.org/wp/interactive-project-dashboard-with-excel/)
    
*   [Project Portfolio Dashboard with Excel](https://chandoo.org/wp/design-project-portfolio-dashboard/)
    
*   [Complete Project Management Template Pack (Excel)](https://chandoo.org/pmt/pmt-index-1.html)
    

[![Project Management Template Bundle by Chandoo](https://chandoo.org/wp/wp-content/uploads/2023/10/SNAG-2986.png)](https://chandoo.org/pmt/pmt-index-1.html)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [13 Comments](https://chandoo.org/wp/critical-path-excel-template/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/critical-path-excel-template/#respond)
    
*   Tagged under [byrow](https://chandoo.org/wp/tag/byrow/)
    , [choosecols](https://chandoo.org/wp/tag/choosecols/)
    , [conditional formatting](https://chandoo.org/wp/tag/conditional-formatting-2/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic array functions](https://chandoo.org/wp/tag/dynamic-array-functions/)
    , [formulas](https://chandoo.org/wp/tag/formulas-2/)
    , [gantt charts](https://chandoo.org/wp/tag/gantt-charts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [project management](https://chandoo.org/wp/tag/project-management/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [textjoin](https://chandoo.org/wp/tag/textjoin-2/)
    , [textsplit](https://chandoo.org/wp/tag/textsplit/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Project Management](https://chandoo.org/wp/category/project-management-2/)
    

[PrevPreviousHow to make a pivot table when you have data in multiple sheets \[Tutorial\]](https://chandoo.org/wp/how-to-make-a-pivot-table-when-you-have-data-in-multiple-sheets-tutorial/)

[NextSQL vs. Power Query – The Ultimate ComparisonNext](https://chandoo.org/wp/sql-vs-power-query/)

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
    
    [Reply](https://chandoo.org/wp/critical-path-excel-template/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/critical-path-excel-template/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/critical-path-excel-template/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ