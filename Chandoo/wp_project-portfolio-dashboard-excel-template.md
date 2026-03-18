# Download Project Portfolio Dashboard Excel Template & Manage multiple projects with ease

**Source:** https://chandoo.org/wp/project-portfolio-dashboard-excel-template

---

*   [products](https://chandoo.org/wp/category/products/)
    , [Project Management](https://chandoo.org/wp/category/project-management-2/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Project Portfolio Dashboard in Excel \[Part 2 of 2\]
====================================================

*   Last updated on November 19, 2012

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**In this 2 part tutorial, we will learn how to design a project portfolio dashboard.** [Part 1](http://chandoo.org/wp/2012/10/25/design-project-portfolio-dashboard/)
 discussed user needs & design. Part 2 will show you Excel implementation.

Project Portfolio Dashboard Pack is now available.  
**[Click here to get your copy](http://chandoo.org/pmt/pmt-index-1.html)
.**

Background: Designing a Project Portfolio Dashboard
---------------------------------------------------

As discussed in part 1, the biggest challenge when it comes to designing project portfolio (program) level dashboards is that, _**End users want it very concise yet powerful**._

We have identified important needs of our end users & come up with a mock up design that meets all these. [Refer to part 1 for that discussion](http://chandoo.org/wp/2012/10/25/design-project-portfolio-dashboard/ "Designing a Project Portfolio Dashboard [Part 1 of 2]")
.

Final Implementation – Project Portfolio Dashboard
--------------------------------------------------

First lets take a look at the finalized dashboard implementation. Click on it to enlarge.

[![Project Portfolio Dashboard using MS Excel - Download now](https://img.chandoo.org/pm/project-portfolio-dashboard-small.png "Project Portfolio Dashboard using MS Excel - Download now")](https://img.chandoo.org/pm/project-portfolio-dashboard-large.png)

Construction of Project Portfolio Dashboard
-------------------------------------------

### Design philosophy for the dashboard

First let us understand the design philosophy for this dashboard, because that is what drives all the Excel work. Here is a mind map that explains how I approached the design of this dashboard.

[![Designing Project Portfolio Dashboard - Mindmap](https://img.chandoo.org/pm/project-portfolio-dashboard-design-mindmap.png "Designing Project Portfolio Dashboard - Mindmap")](https://img.chandoo.org/pm/project-portfolio-dashboard-design-mindmap-large.png)

### Data Entry

Majority of data in this dashboard is captured [using Excel Tables](http://chandoo.org/wp/2009/09/10/data-tables/)
. This has several advantages:

*   Users can easily add more rows of data without worrying about the formulas.
*   Formulas are self-explanatory, thanks to structural references.
*   Data entry is easy, thanks to banded rows, headers & table styles.

There are 6 important tables:

1.  High level project details table
2.  People details table
3.  Each project’s plan details go in to a table, named _plan1, plan2…plan10_
4.  Risks table
5.  Issues table
6.  Holidays table

### Calculations

Explaining each and every formula in this would take us until next years Christmas. So I will highlight key formulas & challenges faced:

**Fetching relevant project plan from all plans:**

This was one of the trickiest things. Since each plan has its own table, getting selected project’s table is necessary to drive all calculations. This is how its done.

1.  **Define lstPlans** as a list of all tables =plan1,plan2…,plan10
2.  Use INDEX to fetch one of the tables from this array like this =INDEX(lstPlans, _activity-row-number, column-number, plan-number_)

**Sorting Projects:**

This is done using 3 steps:

1.  Extract relevant data for all projects based on sort criteria (for example, sort by done % means we need done %s for all projects)
2.  De-duplicate this data by adding a small running fraction to them
3.  Sort using RANK formula

This is essentially same technique Robert taught us in 2008 in [KPI Dashboards article](http://chandoo.org/wp/2008/08/27/excel-kpi-dashboard-sort-2/)
.

**Showing Daily, Weekly or Monthly Gantt view:**

This is achieved by using below logic:

1.  For Daily gantt, see if date in the column is between start & end dates (more: [Between formula in Excel](http://chandoo.org/wp/2010/06/24/between-formula-excel/)
    )
2.  For Weekly gantt, see if the week start & week end in the column fall between start dates’ week start and end dates’ week end. (more: [Date overlap in Excel](http://chandoo.org/wp/2010/06/01/date-overlap-formulas/)
    )
3.  For Monthly gantt, see if the month’s start & end in the column fall between start dates’ month start and end dates’ month end.

**Other important formulas:**

*   [WORKDAY](http://chandoo.org/wp/tag/workday/)
     for all date related calculations so that holidays & weekends are omitted
*   INDEX for all dynamic ranges so that dashboard remains responsive.
*   No UDFs .
*   Very few array formulas so that users can understand what is going on.
*   Structural references as much as possible so that formulas are readable, editable & dynamic. \[[More on Excel tables](http://chandoo.org/wp/2009/09/10/data-tables/)\
    \]
*   Used lots of named ranges to keep formulas readable.

### Dashboard Display

This dashboard display follow box layout with simple colors, easy charts, picture links & lots of conditional formatting goodness.

To understand the important Excel features used in this, see below image & following list.

![Excel features used in Project Portfolio Dashboard - Explanation](https://img.chandoo.org/pm/project-portfolio-dashboard-excel-features-explanation.png "Excel features used in Project Portfolio Dashboard - Explanation")

1.  [Hyperlinks](http://chandoo.org/wp/2011/03/31/excel-hyperlinks/)
    : for accessing other parts of the workbook & data
2.  [Boxes & Text boxes](http://chandoo.org/wp/2009/12/03/use-shapes-in-dashboards/)
    : to show data & provide layout.
3.  [Thermometer chart](http://chandoo.org/wp/2009/12/17/quick-thermometer-chart/)
     to show budget vs. actual performance
4.  Simple Column charts to show distribution of values
5.  [Combo boxes](http://chandoo.org/wp/2011/03/30/form-controls/)
     for selecting sort & view options
6.  [Scroll bars](http://chandoo.org/wp/2008/08/20/create-kpi-dashboards-excel-1/ "Using Scroll bars in Dashboard")
     for seeing more
7.  [Conditional formatting](http://chandoo.org/wp/tag/conditional-formatting/)
     for icons, highlighting & gantt chart
8.  [Picture links](http://chandoo.org/wp/2010/10/19/how-to-use-picture-links/)
     to embed project summaries & gantt chart views
9.  [Option buttons](http://chandoo.org/wp/2011/03/30/form-controls/)
     to select a particular project

### Dashboard Usability

**Color Scheme:**

Use default Office 2007 (2010) theme. This provides very good contrast, excellent color mix & does not surprise many people.

**Fonts:**

Only 2 fonts are used thru out dashboard. Franklin Gothic Book for content & Franklin Gothic Demi for headers.

![Fonts used in Project Portfolio Dashboard](https://img.chandoo.org/pm/fonts-used-in-project-portfolio-dashboard.png "Fonts used in Project Portfolio Dashboard")

These fonts are specified in dashboard’s theme so that they apply by default when opened in any computer.

**Printable:**

The dashboard is optimized for print. All form controls & links are disabled for printing. This ensures that you get a clean printout with just data & charts.

Tip: You can disable printing for any object by right clicking > format > properties and un-checking the print option.

**Macros:**

Since the workbook uses macros, I have added a warning message that shows up when macros are disabled. A [technique](http://datapigtechnologies.com/blog/index.php/forcing-your-clients-to-enable-macros/)
 I picked up from _Mike Alexander_.

How this dashboard works \[Video\]
----------------------------------

Since all this explanation might not do justice to the work, I made a short video \[12 mins\] explaining how the dashboard works. See it below:

Download Project Portfolio Dashboard
------------------------------------

Now you can get this and 4 other project portfolio management templates (including simplified portfolio dashboard, time line chart, gantt chart templates). All these files are easy to use, beautiful to present, fully customizable, unlocked and designed to make you awesome.

[**Click here to get a copy of the project portfolio portfolio dashboard**](http://chandoo.org/pmt/pmt-index-1.html)
.

*   Download locked version of this dashboard and see how this works – [Excel 2007 & above](https://img.chandoo.org/pm/project-portfolio-dashboard-VBA-v1-2010-trial.xlsm)
    .
*   [**Download unlocked version of this and more templates**](http://chandoo.org/pmt/pmt-index-1.html)
    .

How do you like this dashboard?
-------------------------------

I really enjoyed making this dashboard. It was challenging & entertaining experience for me. I think the final workbook summarizes performance of a bunch of projects in a concise yet powerful way.

**What do you think?** Do you like this dashboard? Do you often work with project portfolio / program level dashboards? How do they look and behave? _Please share your feedback, suggestions & ideas using comments._

Thank you for your suggestions & feedback
-----------------------------------------

Thanks everyone who sent suggestions thru emails & comments. I feel very happy about the way this dashboard has turned out. Thanks for your continued support for Chandoo.org.

PS: Go ahead and [pick up Project & Portfolio Management template pack](http://chandoo.org/pmt/pmt-index-1.html)
 today, because you want to be awesome.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

*   [68 Comments](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [conditional formatting icon sets](https://chandoo.org/wp/tag/conditional-formatting-icon-sets/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [no ads](https://chandoo.org/wp/tag/no-ads/)
    , [products](https://chandoo.org/wp/tag/products/)
    , [project management](https://chandoo.org/wp/tag/project-management/)
    , [project management templates](https://chandoo.org/wp/tag/project-management-templates/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [products](https://chandoo.org/wp/category/products/)
    , [Project Management](https://chandoo.org/wp/category/project-management-2/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousProject Portfolio Dashboard – Official Trailer](https://chandoo.org/wp/ppd-trailer/)

[NextFinancial Ratios – Cappuccino or Latte?Next](https://chandoo.org/wp/introduction-to-financial-ratios/)

![](https://chandoo.org/wp/wp-content/uploads/2019/12/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/introducing-advanced-excel-training-v1.png)](https://chandoo.org/wp/excel-school-program/)

Chandoo is an awesome teacher

__________ Rated 5 out of 5

_– Jason_

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Complete Introduction to Power BI](https://chandoo.org/wp/powerbi-introduction/)

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
    

### 68 Responses to “Project Portfolio Dashboard in Excel \[Part 2 of 2\]”

1.  [Project Portfolio Dashboard – Official Trailer | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2012/11/15/ppd-trailer/)
     says:
    
    [November 19, 2012 at 8:53 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-311891)
    
    \[...\] Few days ago, we learned how to design a project portfolio dashboard. The next part talks about how to create this dashboard using Excel. \[...\]
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-311891)
    
2.  [Designing a Project Portfolio Dashboard \[Part 1 of 2\] | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2012/10/25/design-project-portfolio-dashboard/)
     says:
    
    [November 19, 2012 at 8:55 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-311896)
    
    \[...\] That is all for this installment. In the next part, Learn how to create a project portfolio dashboard using Excel. \[...\]
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-311896)
    
3.  ![](https://secure.gravatar.com/avatar/f3f12d49879cb6df2f8a2b344ff5a5ecf981b47f9a8c2411e888c7ebc329b3a3?s=64&d=mm&r=g) [romelsb](http://yahoo/)
     says:
    
    [November 20, 2012 at 3:48 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-312814)
    
    **What do you think?** Do you like this dashboard? Do you often work with project portfolio / program level dashboards? How do they look and behave? _Please share your feedback, suggestions & ideas using comments._  
    _Hi Chandoo,  
    _  
    _Thanks for sharing. Your portfolio dashboard with mindmap is Awesome !  
    _  
    _Please explain more about the dynamics/changes/results (# of project ends, etc) on status box i.e.  
    _  
    _"**Next 6 months in below projects**"_  
    _in relation to input taken from_   
    _"**Settings**"_
    
    Sort Types
    
    % Done (0 -> 100%)  
    Due Date (Now -> Later)  
    % Budget Spent (100 -> 0)  
    Open Issues (a lot -> a few)  
    Risks (a lot -> a few)  
    Original Order
    
    _\-----_  
    _thank you very much !  
    _
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-312814)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 20, 2012 at 3:14 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-313443)
        
        The basic logic of this is explained in the KPI dashboard sort article here:
        
        In this dashboard, the logic is like this:
        
        *   Based on the sort parameter, we extract one of the several columns of data for all projects and load in a large list (100 rows or so)
        *   Then, deduplicate all items by adding a very very small unique fraction to them.
        *   And apply rank() to extract ranked projects 1 thru n
        *   Extract the first 5 corresponding Project IDs and feed them to calculations for rest of the display.
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-313443)
        
        *   ![](https://secure.gravatar.com/avatar/f3f12d49879cb6df2f8a2b344ff5a5ecf981b47f9a8c2411e888c7ebc329b3a3?s=64&d=mm&r=g) [romelsb](http://yahoo/)
             says:
            
            [November 21, 2012 at 3:55 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-314069)
            
            thanks for your reply,  
            When I like to show to my GM  
            "relevant data for all projects" in the Dashboard Header, besides or other than the KPI sort criteria...Can we insert another row of Header boxes as Top summary for All "n" project being tracked in the portfolio.  
            How can we do this ?  
            thanks again
            
            [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-314069)
            
4.  ![](https://secure.gravatar.com/avatar/369787678ee751d1d80afd0a88c6746363cf05a6ef01e08de24ad11482abd632?s=64&d=mm&r=g) Michel says:
    
    [November 20, 2012 at 7:51 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-313044)
    
    Holy Nice-moly! This is awesome! Going to put lots of this to use!   
    Thanks in advance! 
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-313044)
    
5.  ![](https://secure.gravatar.com/avatar/5f08fefd51f5199cb7e52617d796aea29ac59da7dfff2b054f613e8d2a8c8f0b?s=64&d=mm&r=g) Red Shirt Ensign says:
    
    [November 20, 2012 at 5:37 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-313595)
    
    Received the Email with discount for previous PM purchases after I already placed my order, can you refund 20%   wasn't sure where to contac tyou directly  I can provide Transaction information when you contact me!
    
    Thanks Dan
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-313595)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp/)
         says:
        
        [November 21, 2012 at 5:32 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-314154)
        
        Hi RSE.. Thanks for your purchase. I have issued 20% refund to you 🙂
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-314154)
        
        *   ![](https://secure.gravatar.com/avatar/0f61cdb807deb6d4cea8f442d7649bd7e87b756042c908350e75709c8383cdb2?s=64&d=mm&r=g) Red Shirt Ensign says:
            
            [November 21, 2012 at 5:40 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-314158)
            
            Thanks for your quick attention, the templates are awesome... I plan to change mine up to focus on Sales/Business Development projects and how to track them to our needs.... includes more verbage and periodic status updating to track progress of each initiative  
            Will be happy to share with you once I progress (Hoping to start revamp during the weekend  
            Thanks again  
            RSE
            
            [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-314158)
            
6.  ![](https://secure.gravatar.com/avatar/03e906844ff60f18f2d547ba695a230bb7a0f7c9d3bf6dda3afa97cf542012c4?s=64&d=mm&r=g) Michael Lucas says:
    
    [November 21, 2012 at 7:44 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-315006)
    
    I love it! The only issue I'm having is, when I change an activity to 100%, it's showing ##### on the Dashboard Gannt. Am I missing something?
    
    LOVE IT though. I can't wait to show these off!
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-315006)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 22, 2012 at 2:06 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-315332)
        
        Hi Michael... Thank you.
        
        To fix this issue follow below steps:
        
        1.  Right click on any sheet and choose unhide
        2.  Unhide gantt view tab
        3.  Go to it and make sure the column width for column D is enough to fit in 100%. It is set up to show 100% value. But due to your computer settings, you may have slightly larger fonts.
        4.  Once adjusted, follow the same steps for column CZ and EO as well
        5.  Hide the gantt view tab again.
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-315332)
        
        *   ![](https://secure.gravatar.com/avatar/03e906844ff60f18f2d547ba695a230bb7a0f7c9d3bf6dda3afa97cf542012c4?s=64&d=mm&r=g) Michael says:
            
            [November 22, 2012 at 2:37 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-315362)
            
            That worked! Thanks.
            
            [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-315362)
            
7.  ![](https://secure.gravatar.com/avatar/b071c1951fd7111379de2d0ce1520d04dac5edb33ae81e85a6af6a6def5d7629?s=64&d=mm&r=g) Matei says:
    
    [November 21, 2012 at 7:50 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-315013)
    
    Is a demo available ?
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-315013)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 22, 2012 at 2:07 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-315334)
        
        Yes, please download it from here:
        
        [http://img.chandoo.org/pm/project-portfolio-dashboard-VBA-v1-2010-trial.xlsm](http://img.chandoo.org/pm/project-portfolio-dashboard-VBA-v1-2010-trial.xlsm)
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-315334)
        
8.  ![](https://secure.gravatar.com/avatar/cb1a793dfce6037ec2fcf2148c5b2bc49464900ff33397f07c8525ce3a648e97?s=64&d=mm&r=g) [Matthew Clapp](http://www.nautis.com/)
     says:
    
    [November 26, 2012 at 12:05 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-320675)
    
    Thanks for offering a demo. This is really amazing work. Applications half this good cost well into the thousands of dollars (US). I think the roll-up KPI view is worth the price alone. Do you recommend this be owned by 1 manager or could this be stored on SharePoint and be updated by several people?  
    Thanks!
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-320675)
    
9.  ![](https://secure.gravatar.com/avatar/dc136629a09b44839c7944c404f5404c81eb28aa9953bef9b71a61f08bf9098a?s=64&d=mm&r=g) Amit Gupta says:
    
    [November 28, 2012 at 6:04 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-322854)
    
    Awesome....I am quite impressed with the Mind map Presentation. It seems like the foundation for each project. Could you share the software used
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-322854)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 28, 2012 at 7:57 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-322939)
        
        Hi Amit, I use a website called bubbl.us to create these mindmaps
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-322939)
        
        *   ![](https://secure.gravatar.com/avatar/dc136629a09b44839c7944c404f5404c81eb28aa9953bef9b71a61f08bf9098a?s=64&d=mm&r=g) Amit Gupta says:
            
            [November 28, 2012 at 4:15 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-323451)
            
             thka a lot!!!
            
            [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-323451)
            
10.  ![](https://secure.gravatar.com/avatar/035ae14084c3b1409facad5cec4963358c70698e66d80cc9574be18a75d36fad?s=64&d=mm&r=g) Adam G says:
    
    [January 11, 2013 at 2:21 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-388878)
    
    Hi Chandoo,Your PM dashboards impressed me so much that I’ve downloaded the Portfolio and Project Management package. All of the documents look very professional.I was going through the Portfolio dashboard and I had a question.When I enter in additional holidays they are highlighted in the gantt chart. Is it possible so that the name of the holiday shows up in the highlighted area of the gantt chart.ThanksAdam
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-388878)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [January 11, 2013 at 3:03 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-388922)
        
        Thanks for your lovely comments & purchase Adam.
        
        Unfortunately, there is no easy way to display holiday names in the highlighted portion. One alternative is to show list of holidays that occur in the filtered date range in legend area of the dashboard. For this you need to use formulas. As a start, I suggested looking at range lookup article. - [http://chandoo.org/wp/2010/06/30/range-lookup-excel/](http://chandoo.org/wp/2010/06/30/range-lookup-excel/)
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-388922)
        
11.  ![](https://secure.gravatar.com/avatar/38b8cf4e8b4f4356e5933bfd4d6cb50859f7f964c16bdd3755497fdd1aebd24b?s=64&d=mm&r=g) smax says:
    
    [February 23, 2013 at 4:23 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-415599)
    
    Can the portfolio management dashboard  be translated to spanish?   can the translation affect the functionality?  
       
    thanks  
     
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-415599)
    
12.  ![](https://secure.gravatar.com/avatar/969859cb36a2ca385034cb9616ae38deff9f5e385e81a129c61e110206abb2b7?s=64&d=mm&r=g) lstanley says:
    
    [March 12, 2013 at 6:26 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-419381)
    
    I have two questions:  
       
    1\. In Project Plan tab, Is the Duraction column in hours or days?  
    2\. In Dashboard tab, the scroll bar displays each project, but in my case,  the entry Months displays ZERO. Why ? Which data is missing?  
       
    Thank you for your answers.
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-419381)
    
13.  ![](https://secure.gravatar.com/avatar/0e2fbb5c5f978c184efbc54fc70dea75eae9776524cabfd0a35ce45eb39daedc?s=64&d=mm&r=g) Renato says:
    
    [March 26, 2013 at 5:37 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-421199)
    
    Hi,  
    I acquired a project portfolio dashboard, but i have a doubt:  
    The Duration is in hour ou day ?  
    I´m asking because i have activities in my projects in hours.  
    Tanks.
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-421199)
    
14.  ![](https://secure.gravatar.com/avatar/888db2fd3c167ee2796a243cdb6aa9ba3aca0e95f9ee22452ea845ec0fd29923?s=64&d=mm&r=g) Martyn says:
    
    [May 30, 2013 at 8:49 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-433749)
    
    Hi,
    
    I want to know if I will always have to convert the reports to pdf before I sent them to the project team or I am able to e-mail them on an excel format?
    
    Martyn
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-433749)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [May 30, 2013 at 9:32 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-433752)
        
        @Martyn  
        This is not really an Excel question, but more of a Company Policy style question.  
        You can email any files including Excel and PDF files to others.  
        With PDF the end user can only browse the worksheets, they cannot change/edit the data or results
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-433752)
        
15.  ![](https://secure.gravatar.com/avatar/5d0ace799beff0095c2060fe897a6fbf50f5f0e2c6e53576901d50fd1f22e78e?s=64&d=mm&r=g) manu says:
    
    [June 11, 2013 at 10:51 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-436165)
    
    This is awesome .. Nice work chandoo !  
    Is there a integration with mpp? I put all my data in mpp and would be nice if there is away to integrate this with mpp. thanks !
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-436165)
    
16.  ![](https://secure.gravatar.com/avatar/0f6ff7f9764e4297d4e33a769cbab27d443dc7f0ac1b27fa7622af2991029fb0?s=64&d=mm&r=g) James says:
    
    [June 27, 2013 at 8:38 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-437929)
    
    Hi Chandoo,  
    Great spreadsheet, but how do i change the currency in the dashboard?  
    thanks.
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-437929)
    
17.  ![](https://secure.gravatar.com/avatar/3c0798e92d4cb77d5d25eebcb1b3a26eea33c8ebae13e4f37bd1462f889733f3?s=64&d=mm&r=g) manolito says:
    
    [July 2, 2013 at 2:38 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-438468)
    
    Hi Chandoo,
    
    Very useful and powerful tool!
    
    I'm trying to add an 11th. project and I followed your instructions of copy-paste the table and rename it as plan11. However, the dashboard is not bein updated with the activities... doing some research looks like in the Calculations tab, the IFERROR formula is getting an error from the values in the lstPlans Matrix (starting on cell D29).
    
    Don't know how to move forward, could you please give some advice on it?
    
    Thanks for your help!
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-438468)
    
    *   ![](https://secure.gravatar.com/avatar/a5620aab6b6ed3b150667a372aa6579caccd8aefeddec01088327d959e4ad021?s=64&d=mm&r=g) Dale Braden says:
        
        [April 14, 2014 at 6:50 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-478677)
        
        Have you been able to resolve this? I am having the same issue with adding additional projects. I believe this is a great product and very easy to digest from an executive point of view but unfortunately support related emails have gone unanswered for me since running into this issue.
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-478677)
        
        *   ![](https://secure.gravatar.com/avatar/4c3601bd957055cf935e708de3118a85db22192c653073849f5556811175daec?s=64&d=mm&r=g) BUNIT says:
            
            [October 17, 2015 at 5:19 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1064074)
            
            I am having the same problem. what was the resolution?
            
            [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1064074)
            
18.  ![](https://secure.gravatar.com/avatar/5e731c81d8fc64d1878276e0cd882ba5276250157d9f113d2bc90ed759bf25b8?s=64&d=mm&r=g) Amit Roy Choudhary says:
    
    [July 2, 2013 at 4:46 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-438480)
    
    Hi Chandoo, I have made the payment a few hours back for your dashboard. I koow you have mentioned that it takes upto 24 hrs to send the link but could you send it to me at the earliest. I need to use it tomorrow for a presentation
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-438480)
    
19.  ![](https://secure.gravatar.com/avatar/07fee60b5bd25dd1704663e92a763eaa16ec4ac24d6d5bc08581a1cbb58e2b79?s=64&d=mm&r=g) Nicolas says:
    
    [August 25, 2013 at 10:45 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-444161)
    
    Hi Chandoo,  
    I have bought the entire pack and I am very happy with it. I was not looking at the project dashboard portfolio.  
    On the gantt daily view, the "today" line does not appear.  
    Besides that, I understand there is conditional formatting but I was wondering how the reference to the cell valGantstart links to show the "today line" for the gantt chart when the formula to show the "today line" on conditional formatting refers to this valGantstart.
    
    Thank you  
    Kr  
    Sacha
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-444161)
    
20.  ![](https://secure.gravatar.com/avatar/948813b715eb8216fd1bf74f0a7c745e3fa4c11922bd36b0398b60df98463e65?s=64&d=mm&r=g) Mrs N says:
    
    [September 20, 2013 at 12:33 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-446579)
    
    Hello Dear Shandoo,
    
    Ineeed to know more information about how to purshase this dashboard.
    
    Thank you.
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-446579)
    
21.  ![](https://secure.gravatar.com/avatar/36ec84e67c96b15a6b430cc0c350871eeb8107d21d958db97e97f5fb801c34cc?s=64&d=mm&r=g) Zahir says:
    
    [October 11, 2013 at 10:10 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-448790)
    
    Hi Chandoo, your portfolio template is great, the one issue is the progress on teh project, if 100% is added in progress, it does not fully display, All that I see is ##### on teh dashboard. I would like to show your example to my colleagues and management. Is there a way to fix this issue?
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-448790)
    
22.  ![](https://secure.gravatar.com/avatar/9ada16fe40787a7a2ca938bdbb213264a2cd638fe483e5923d256caa3e70c98b?s=64&d=mm&r=g) Paul says:
    
    [November 6, 2013 at 4:04 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-452437)
    
    Hi
    
    Have downloaded the trial portfolio template to see how the various elements work but the 'calculations' worksheet is hidden so I am unable to establish how the data is calculated? How can I access the hidden worksheets?
    
    Thanks  
    ps. great job by the way!!
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-452437)
    
23.  ![](https://secure.gravatar.com/avatar/a0b605ee74b3ae8dd22d3278e2e93cb9e99509cbc829b8fabc8a0ce02925e15f?s=64&d=mm&r=g) kenneth says:
    
    [November 12, 2013 at 4:43 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-454296)
    
    Dear Chandoo,
    
    Kindly explain how your percentage of Projects done on the dashboard is calculated as this seems to depend on the budget?
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-454296)
    
24.  ![](https://secure.gravatar.com/avatar/86ec38a005a064229c41b81b92bdc88c81ef95988ba3d4cfc69cbfd580d958ce?s=64&d=mm&r=g) vijay says:
    
    [November 16, 2013 at 10:28 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-455672)
    
    I just purchased this tool and am trying it for my immediate need. It looks lean and effective. Have a few critical questions to be able to use this.  
    1\. project status is indicated  
    using Green, Amber & Red colors based on many many factors. such as scope, cost and schedule status. The excel seems to use colors to indicate the percentage complete. A project could have been 75% complete but still be over budget, delayed in  
    timelines etc. And such a project should be indicated in RED and not Green. How can I set the status color without linking to the  
    percentage complete?  
    2.How do i do this for Activities too?  
    3.How do i map the team members to the  
    projects?  
    4\. My portfolio has more than 5 projects. I added 5 more. But when i preview the print it only displays 5 projects NOT 10. How do I get to print all 10?
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-455672)
    
25.  [Quick and easy Gantt chart using Excel \[templates\] - TechBloggers](http://techbloggers.de/2014/02/quick-and-easy-gantt-chart-using-excel-templates/)
     says:
    
    [February 18, 2014 at 7:20 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-470432)
    
    \[…\] Project Portfolio dashboard using Excel \[…\]
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-470432)
    
26.  ![](https://secure.gravatar.com/avatar/2b011a7fb19f8f5b43f33ba3873b788fd2035d510f08c4696369fe93c00ff40e?s=64&d=mm&r=g) [Shiva](http://phone/)
     says:
    
    [February 28, 2014 at 6:12 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-471946)
    
    Do you have contact number to reach you over the phone
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-471946)
    
27.  ![](https://secure.gravatar.com/avatar/edc03ef3e1083412516dfd64d4a12d3def31d4c9358421ba2ae6864fd7b6ac1b?s=64&d=mm&r=g) Rakesh says:
    
    [March 5, 2014 at 2:20 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-472624)
    
    Chandoo,
    
    Is there way to display a line to show the 'Baseline' within the dashboard under the Plan section? Or can you do this??
    
    How we log and track Dependencies??? May be like Risk and Issue you need sow Dependencies.
    
    I want to show RAG status for Risk & Issue (e.g. RED = High, AMBER = Medium and GREEN = Low)
    
    Chandoo...please respond to my query as I want to purchase.
    
    Thanks
    
    Rakesh Mistry
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-472624)
    
28.  ![](https://secure.gravatar.com/avatar/fd8556262b10524db8b629fa16fc2362fe2a163e9ddba468a98873ab052c0889?s=64&d=mm&r=g) Agustin says:
    
    [March 18, 2014 at 5:16 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-474498)
    
    I try downloading the trial from  
    [http://img.chandoo.org/pm/project-portfolio-dashboard-VBA-v1-2010-trial.xlsm](http://img.chandoo.org/pm/project-portfolio-dashboard-VBA-v1-2010-trial.xlsm)
     to evaluate a potential using for my proyects but  
    the downloaded files have no xlms format (only xml and bin files) extension so is no posible for me to test it.....maybe I am doing somethin wrong...
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-474498)
    
29.  ![](https://secure.gravatar.com/avatar/54c749f62686b9e8b7843e74845daf65e21aaf855d65faf4156addbc47076bed?s=64&d=mm&r=g) Dan K says:
    
    [April 4, 2014 at 12:50 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-477231)
    
    I purchased, nice presentation on the Port Dash, seems basic on the data entry side of things. I was a bit thrown back on the entire data package contents, as there are some old templates in there, and repetitiveness in form. I was expecting a bit more, in comparison to what else is out there. Also in the fact that you have a great rep... I love your site, and input... so great job on that side of things. This is usually my first stop for examples....!
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-477231)
    
30.  ![](https://secure.gravatar.com/avatar/8be4c564ee96270bcda07f1e2c30709b98f52d3d768585fc4c791bcb10db35ac?s=64&d=mm&r=g) Karl says:
    
    [November 11, 2014 at 7:19 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-845838)
    
    Hi Chandoo,
    
    Are there any issues in running this template in Excel 2007? Has the template held up good with Excel updates?
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-845838)
    
31.  ![](https://secure.gravatar.com/avatar/52694a994e81b40cf6214ce04e767b119eea2c0e9731175fd65ba51c6163d73a?s=64&d=mm&r=g) Venkata says:
    
    [January 4, 2015 at 5:46 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-888450)
    
    Hi Chandoo,
    
    I would like to know apart from the Dashboard usage, can we have a facility to extract as a report showing all Projects status report as read only to all Stakeholders, I am not interested in sharing the whole Dashboard as it comprises of complex code.
    
    All I am looking is a button, which extract whole dashboard as a report in PDF or jpg format to share it with all stake holders.
    
    Please advise?
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-888450)
    
    *   ![](https://secure.gravatar.com/avatar/edbc150b1148061b1d31884a999db8d447cbb063f9a12018bfd6f95758e07ebc?s=64&d=mm&r=g) Chintua says:
        
        [July 24, 2015 at 10:41 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1013094)
        
        Dear Chandoo,
        
        Please can you reply to the question above (by Venkata).
        
        I'm about to get the dashboard but will need to have that feature as the Stakeholders will not be needing all the info the Prog Mgr sees.
        
        Thanks.
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1013094)
        
32.  ![](https://secure.gravatar.com/avatar/b38cc17c35baf9243f2cbd43fe68b526c66d603f89a37eb422c74ee40baee52a?s=64&d=mm&r=g) Zafar says:
    
    [February 10, 2015 at 5:27 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-910557)
    
    Thanks Chandoo for sharing your excellent portfolio template with us.
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-910557)
    
33.  ![](https://secure.gravatar.com/avatar/0941af9b2ffd9d3bdbb50f5bdd534aab0713ef367a8fcbac9fba53a5804b65c2?s=64&d=mm&r=g) Phil says:
    
    [April 8, 2015 at 1:49 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-949119)
    
    Dear Chandoo,
    
    I purchased Portfolio dashboard yesterday; I am trying to modify it by adding Customer in front of Project name, estimated hours, and hours spent - I tried replacing Budget and spent title, and $$ format to number - the dashboard choked.
    
    Then I just tried to add columns in Project details, Customer, estimated hours, and hours spent. Obviously, I knew it wouldn't show up, so I tried modifying calculations table by adding these columns to the similar table spaces - yes, the page says, please do not edit.
    
    My need on this dashboard is more time, than money, although the money is secondary.
    
    How can I add these columns so I can view them on dashboard? Replacing the $$ in the left box would be acceptable; making it swappable would be even better
    
    Best Regards
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-949119)
    
34.  ![](https://secure.gravatar.com/avatar/0941af9b2ffd9d3bdbb50f5bdd534aab0713ef367a8fcbac9fba53a5804b65c2?s=64&d=mm&r=g) Phil says:
    
    [April 8, 2015 at 3:13 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-949150)
    
    One more thing. When I make an activity in Project Plan 100% complete; the dashboard shows ####
    
    By the way; this dashboard is brilliant...
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-949150)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [April 9, 2015 at 3:23 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-949362)
        
        @Phil  
        Make the column wider
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-949362)
        
        *   ![](https://secure.gravatar.com/avatar/0941af9b2ffd9d3bdbb50f5bdd534aab0713ef367a8fcbac9fba53a5804b65c2?s=64&d=mm&r=g) Phil says:
            
            [April 9, 2015 at 1:27 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-949579)
            
            hui,
            
            I have made column wider (dragged column D in Gantt View), and the dashboard still shows ####. is there another place where I need to do this? I cant seem to edit the dashboard...
            
            Best
            
            [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-949579)
            
            *   ![](https://secure.gravatar.com/avatar/0941af9b2ffd9d3bdbb50f5bdd534aab0713ef367a8fcbac9fba53a5804b65c2?s=64&d=mm&r=g) Phil says:
                
                [April 9, 2015 at 2:16 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-949599)
                
                Just realized, there were more than one Gantt in Gantt View. thanks @Hui
                
                [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-949599)
                
35.  ![](https://secure.gravatar.com/avatar/0941af9b2ffd9d3bdbb50f5bdd534aab0713ef367a8fcbac9fba53a5804b65c2?s=64&d=mm&r=g) Phil says:
    
    [April 30, 2015 at 1:01 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-962573)
    
    Has anyone tried Publishing this on a SharePoint website? If you have, what steps did you take to have the dashboard open without reverting opening with excel?
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-962573)
    
36.  ![](https://secure.gravatar.com/avatar/2894d6dd74ddd5200cb6e7270a0e5b6dc64e24eafa9e3a1b61eeac49e48cc03c?s=64&d=mm&r=g) Nick says:
    
    [August 6, 2015 at 10:20 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1019850)
    
    Just realized that on the Dashboard screen under "Projects" it says 8 Projects and instead of saying "% Done" it says "DIV/O! Done". any clue how to fix it so it says overall % Done?  
    Regards
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1019850)
    
37.  ![](https://secure.gravatar.com/avatar/9ec31086a04a240b5dcc8375afe759acbfb19384a685e685f53000ff5028bd8a?s=64&d=mm&r=g) John says:
    
    [September 20, 2015 at 9:23 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1048183)
    
    Can the template be customized to be used for other purposes or other fields added to the dashboard? For example I want to track project value instead of project budget
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1048183)
    
    *   ![](https://secure.gravatar.com/avatar/fec9c5aae940cb14463728804c6127da4b3732f65e542d237d7d459effd5efbe?s=64&d=mm&r=g) Connie says:
        
        [July 29, 2016 at 1:28 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1242115)
        
        Dear John,
        
        I was wondering if you got a response to your question and if so whether you could share the answer.
        
        Thank you
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1242115)
        
38.  [document your work | Document converter](http://10document-urgen.cf/document-your-work/)
     says:
    
    [November 6, 2015 at 6:22 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1076596)
    
    \[…\] | Read Sources \[…\]
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1076596)
    
39.  ![](https://secure.gravatar.com/avatar/364aca05e883cef1b3aed4569139b782e02c2effe4bb7a790ea213e41685abc3?s=64&d=mm&r=g) Johan Dekker says:
    
    [August 24, 2016 at 7:50 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1265071)
    
    I purchased the whole package online however the dashboard only allows me 10 projects. Is it possible to get one that can handle 50 projects or more?
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1265071)
    
    *   ![](https://secure.gravatar.com/avatar/ec2ba3f4be9449fab811795794389b5e870678260db1cb23b3bd8efe8b7d431e?s=64&d=mm&r=g) Matthew Coffin says:
        
        [April 11, 2017 at 7:31 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1435657)
        
        Johan - If you have not seen , the video explains how to add in more projects . However , my approach would be to try and group the projects , so that I would have a master Project dashboard for the groups, and then a group master dashboard for the projects.
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1435657)
        
40.  ![](https://secure.gravatar.com/avatar/d00610c1815c846b71b2c525eb18f9efebb18c4124f5565716c4811eb2180178?s=64&d=mm&r=g) [John Fomusa](http://www.fomusaconsulting.com/)
     says:
    
    [September 2, 2017 at 2:57 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1506295)
    
    Mr. Chandoo,
    
    I have a friend that is building the same Dashboard as your "Project Portfolio Dashboard" ( [https://chandoo.org/wp/2012/11/19/project-portfolio-dashboard-excel-template/](https://chandoo.org/wp/2012/11/19/project-portfolio-dashboard-excel-template/)
     )
    
    My friend needs help implementing some of the features which requires one on one phone and remote desktop consultation. Are you available and what would be your rate?
    
    Regards,
    
    John Fomusa  
    (T) 980.263.2051  
    Fomusa Consulting Services, LLC  
    [http://www.FomusaConsulting.com](http://www.fomusaconsulting.com/)
    
    Fomusa Consulting Services | IT Solutions | Website Solutions
    
    An IT solutions company for networking, software, computer, and website services tailored to small and medium size businesses.
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1506295)
    
41.  ![](https://secure.gravatar.com/avatar/aa4d7015577cc6101a983928ccced8157677ad4ecf60d81e93f36ca2eeefeff8?s=64&d=mm&r=g) Markus says:
    
    [September 17, 2019 at 7:03 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1688165)
    
    Hi
    
    I am using your Excel file for high level Project Controlling and Portfoliomanagement.  
    I really like it a lot but I have a small issue:  
    I can not change anything on the dashboard itself as the page is protected.  
    For me the Budget needs to be formatted differently: Smaller Font and no decimal places are needed. My budgets for (ERP) Projects are relatively high and it is very difficult to read the figures in the Budget box.  
    How could I change this?
    
    Thx a lot for any answer in advanced.
    
    Viele Grüße / Best Regards
    
    Markus
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1688165)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [September 17, 2019 at 8:15 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1688182)
        
        @Markus...  
        You can purchase unprotected version of the templates from here: [https://chandoo.org/pmt/pmt-index-1.html](https://chandoo.org/pmt/pmt-index-1.html)
          
        You can easily edit every aspect of the files.
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1688182)
        
42.  ![](https://secure.gravatar.com/avatar/41ba32b4b6f46800abade614c62fa9d30e093827bfa24e1817445e9db6d1c10b?s=64&d=mm&r=g) Padmaraj S says:
    
    [October 11, 2019 at 8:58 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1694750)
    
    I had purchased unprotected version today, EBS Payment ID: 140686093. Do let me know when would i receive the pack
    
    Regards,
    
    Padmaraj.S
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1694750)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [October 12, 2019 at 7:53 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1695280)
        
        Thanks for purchasing this Padmaraj. I have already emailed you the download link.
        
        [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1695280)
        
43.  ![](https://secure.gravatar.com/avatar/b389fa025a573252c3e9afd1cde907284df5d999cc6cd09d3e91e46f71d5b7a6?s=64&d=mm&r=g) Christophe Leribaux says:
    
    [November 17, 2020 at 10:21 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1929000)
    
    Hi,
    
    to accomodate our project managers and the portfoliomanagers in the company (JSR, Belgium) I'm interested to test version of the portfoliomanagement files you present in the PDF.  
    It the one with an overview of all projects and visibility of the details when you click on a project. (Page 5 of the PDF). I wonder if is possible to send me a BLOCKED version. If this would be acceptable for the users, I'd order the full package.
    
    best regards and thank you for you quick response,  
    Christophe
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-1929000)
    
44.  ![](https://secure.gravatar.com/avatar/6022b9c9aab996503f8c8b113ba807b5bf68b39daa885b1a666d2dacadae9892?s=64&d=mm&r=g) Freddie Wofford says:
    
    [June 4, 2021 at 5:32 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-2004878)
    
    I just purchased the project portfolio templates. On the dashboard in the Ganett chart view the scroll bar on the right hand side does not appear. How can I fix that.
    
    Thank you.
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-2004878)
    
45.  ![](https://secure.gravatar.com/avatar/6022b9c9aab996503f8c8b113ba807b5bf68b39daa885b1a666d2dacadae9892?s=64&d=mm&r=g) Freddie Wofford says:
    
    [June 4, 2021 at 5:36 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-2004879)
    
    I am having another problem on the dashboard. The block for the "next 6 months in the below projects" is not calculating any information. How can I fix it?
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-2004879)
    
46.  ![](https://secure.gravatar.com/avatar/ae1c873f1ee1a7f3ad374a7b841e0561478d46b45c2af45792c8d6f82d77036d?s=64&d=mm&r=g) Marco says:
    
    [April 17, 2022 at 8:30 am](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-2074401)
    
    Hi.
    
    Great template, however, there should be an option for the traffic light.  
    Currently you can set the colors only by completion ratio which makes not much sense.
    
    The traffic lights should be used to show if the project is on track, potentially delayed or in delay. If a project is scheduled to start only next month the progress is 0% it deserves a green light....
    
    Suggest to have a option for traffic lights:  
    \- based on completion ratio  
    \- based on task delay  
    \- based on risk status
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-2074401)
    
47.  ![](https://secure.gravatar.com/avatar/0b6efe93300f7fba1d9bf461ef5c986adb464aaf74159147e3fdad8740eecc5f?s=64&d=mm&r=g) George says:
    
    [January 14, 2024 at 9:20 pm](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-2164398)
    
    Hello Chandoo,
    
    This looks to be exactly what I need to establish a portfolio framework for my organization. With my affinity with Excel and Mind Mapping I am looking forward to using the software.
    
    I have already purchased the full bundle pack. However, I would like to be able to view your 12 min overview video as I start to unlock the tool features. The video link on the website is not available for me. Can you please send me the video url or other means to access the video.
    
    Thank you,  
    George
    
    [Reply](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#comment-2164398)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/project-portfolio-dashboard-excel-template/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ