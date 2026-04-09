# How to Export Excel Dashboards to Web - 4 alternatives to save dashboards as HTML

**Source:** https://chandoo.org/wp/export-dashboards-to-web

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

4 Alternatives to Export Excel Dashboards as Web Pages
======================================================

*   Last updated on September 29, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This article is written by **Alex Kerin** from [Data Driven Consulting](http://www.datadrivenconsulting.com/)
._

![Exporting Excel Dashboards to Web Pages - How to Guide](https://chandoo.org/img/dashboards/excel-dashboards-to-web-how-to.png)

“[When expensive dashboard software doesn’t work, do it with Excel](http://www.perceptualedge.com/blog/?p=27)
” stated Stephen Few back in 2006. This was before the release of Tableau, and some of the other solutions now available for visualizing your data, **but Excel remains a great choice for [creating dashboards](http://chandoo.org/wp/excel-dashboards/)
 when you extend it with sparkline add-ins, clever chart hacks, and VBA or (relatively) simple formulas.**

Excel however isn’t regarded as a “serious” business intelligence tool for delivery of your metrics and charts. Perhaps some of this is that users expect dashboards to be deployed on the web not on a locally installed application.

**Today we will learn how to export excel dashboards to web pages.**

### Exporting Excel Dashboards to Web:

When it comes to exporting dashboards to web, 4 options come to my mind. I’ll quickly review these, culminating in a look at a new option – Excel 2010 and Microsoft’s  online version of Office – [Docs.com](http://docs.com/)

1.  **Save your workbook as a web page**. Text in cells is converted to text in html tables, while charts and other shapes are converted to images. Excel offers two formats – mhtml and normal html. The mhtml version saves as a single file with the images encoded as text. [Only IE](http://en.wikipedia.org/wiki/MHTML)
     can natively handle mhtml file while plug-ins exist for some of the other popular browsers. The normal html file option creates a folder full of images. By choosing this option you obviously lose any interactivity you had via drop down forms, pivot tables,  or VBA. The conversion of charts/shapes to images is imperfect, leading to fuzzy edged images, and in my (beta) version of 2010 sometimes resulted in blank or missing images. You also lose font  type information in 2007, so if you’re using any special fonts to [create in-cell charts](http://chandoo.org/wp/2010/01/21/excel-incell-chart-font/)
     they will end up looking odd. Excel 2010 preserves font information (as long as the font is installed on the user’s machine). Personally, I don’t think it’s a great option – you may as well just:![Save Excel Dashboard as Web page - example](https://chandoo.org/img/dashboards/dashboard-saved-as-html-s.png)  
    \[[click here for a larger version](http://chandoo.org/img/dashboards/dashboard-saved-as-html.pnghttp://chandoo.org/img/dashboards/dashboard-saved-as-html.png)\
    \]
2.  **Take a screenshot and post it to your website**. You could use contol-printscreen to take a snapshot of your dashboard. As this just dumps the screen to the clipboard you may want to use a [screen capture tool](http://www.google.com/search?hl=en&qscrl=1&q=screenshot+capture+free+programs&aq=f&aqi=&aql=&oq=&gs_rfai=)
     which can select a portion of the screen and save it to a file easily. You’ll want to make sure you crop appropriately, for looks, and so that your boss doesn’t see your taskbar with your browser on  Facebook. Excel 2010 has a new screenshot option, but that’s for inserting screenshots, not saving them out. You can’t save a file as jpg/png  like you can in Powerpoint, but you could [save as a PDF](http://www.cutepdf.com/)
     and upload that. But what if you want more interactivity?
3.  **Publish using Sharepoint**. Sharepoint is an MS server platform that among (lots of) other things, allows publication of Excel workbooks to the web. While some interactivity is preserved (like pivot tables), [many features](http://office.microsoft.com/en-gb/excel-help/differences-between-using-a-workbook-in-excel-and-excel-services-HA010021716.aspx?CTT=5&origin=HA010013775)
     are not (VBA, form dropdowns, images, and shapes). As some sparkline add-ins use VBA to generate a shape that depicts the data, even the static shape will not be shown as it will be stripped out. Other add-ins use VBA and a special font to depict the shape. As Excel 2010 preserves font information, these may show on a Sharepoint server, assuming the user has installed the font. Of course though, they will not update as VBA is not allowed. Linking to external data sources is allowed, so you can use your OLAP cubes or whatever else.  Sharepoint is a viable option, but requires servers and licenses, neither of which come cheap. What other options are there then?
4.  **Docs.com and Excel 2010.** [Docs.com](http://docs.com/)
     is Microsoft’s online version of the Office applications. At the time of writing (July 2010), it was still in private beta. Oddly, MS has chosen to release it with deep ties to Facebook (login, posting to your wall, and sharing documents amongst friends). I honestly have never needed to share a document with a friend, and equally I’m not friends with the people that I do want to share documents with. Despite this (and I’m sure plenty will change as Docs evolves past beta), Docs.com offers some interesting opportunities for web deployment of dashboards. It still suffers from no VBA or ability to show shapes – I suspect that docs.com is running in a Sharepoint environment, BUT, and this is a big but, Docs.com was built with Office 2010 in mind. This means that the [sparklines new to Excel 2010](http://chandoo.org/wp/2010/05/18/excel-sparklines-tutorial/)
     show up, and update when values change. Take a tour of one of my workbooks on docs.com [here](http://docs.com/17SD)
    .![Excel Dashboard exported to web thru Docs.com](https://chandoo.org/img/dashboards/dashboard-on-web.png)

### Problems with Excel Dashboards uploaded to Docs.com

You’ll see on the example that there are several warnings thrown up – I left some shapes in the file before uploading just to show you what the warning message looked like. Linking to external data is not allowed (as you would expect, compared to Sharepoint where you control the servers), so you’ll have to be clever about how you update the dashboards. If your goal is to deploy using Docs.com, you’ll probably design your dashboard with this in mind, making good use of pivot tables for example.

I could envisage using Docs.com in the following manner:

*   Develop a great dashboard in 2010 that instantly makes the user aware of any problems (but you’re doing that already aren’t you?) and upload it to Docs.com
*   Share the document with your users, and upload a new file as data is added to the dashboard
*   For any interactivity (e.g. simple data exploration to further investigate problems), the user can download the document  – even though things like dropdown list boxes are not shown on docs.com, they are preserved and will show and work on the local version (VBA is still a no-no as you can’t upload a xlsm file)

I would like to see some changes with Docs.com – for example being able to hide the “Who you are sharing this with” column, allowing full-screen viewing of just the sheet, and sorting out the sharing outside of Facebook.

Now this method will not be suitable for sensitive information where deploying to the cloud (albeit with careful sharing of access) would not be appropriate, but the concept of using Excel 2010 and Docs.com offers some interesting opportunities for web-deployed Excel dashboards, and for using on websites that teach us to become awesome in Excel…

### Added by Chandoo:

### How do you Export Excel Dashboards to Your Audience?

Do you save the dashboards as PDFs or email the workbook or save as web page? What is your way of exposing the dashboard to the audience?

_**Please share using comments.**_

### More Resources on Dashboards:

[Checkout our dashboards page](http://chandoo.org/wp/excel-dashboards/ "Excel Dashboard Templates, Tutorials & Downloads")
 which has lots of links, templates, downloads and tutorials on creating excel dashboards.

### Thank you Alex

I thank Alex for sharing these beautiful ideas with all of us. Exporting dashboards is a growing need and we all could use help like this to become better. _**Thank you Alex**_.

### About Alex Kerin:

Alex runs a kickass consulting business at [Data Driven Consulting](http://datadrivenconsulting.com/)
. He shares a lot of innovative ideas and information on dashboards, visualization and Excel [thru his blog](http://www.datadrivenconsulting.com/blog/)
 regularly. And of course, he is awesome with excel.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [Ask a question or say something...](https://chandoo.org/wp/export-dashboards-to-web/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [docs.com](https://chandoo.org/wp/tag/docs-com/)
    , [export to web](https://chandoo.org/wp/tag/export-to-web/)
    , [html](https://chandoo.org/wp/tag/html/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Office 2010](https://chandoo.org/wp/tag/office-2010/)
    , [office online](https://chandoo.org/wp/tag/office-online/)
    , [pdf](https://chandoo.org/wp/tag/pdf/)
    , [sharepoint](https://chandoo.org/wp/tag/sharepoint/)
    , [spraedsheets](https://chandoo.org/wp/tag/spraedsheets/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousGantt Box Chart Tutorial & Template – Download and Try today](https://chandoo.org/wp/gantt-box-chart-tutorial-template/)

[Next7 Personal Expense Trackers using Excel – Download TodayNext](https://chandoo.org/wp/download-expense-trackers/)

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
    
    [Reply](https://chandoo.org/wp/export-dashboards-to-web/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/export-dashboards-to-web/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/export-dashboards-to-web/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ