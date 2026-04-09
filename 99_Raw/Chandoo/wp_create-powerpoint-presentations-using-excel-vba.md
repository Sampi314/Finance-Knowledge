# Create PowerPoint Presentations Automatically using VBA » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/create-powerpoint-presentations-using-excel-vba

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Create PowerPoint Presentations Automatically using VBA
=======================================================

*   Last updated on May 20, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is a guest post by Drew Kesler._ 

You’ve been there before. It’s almost 5:00, and you are going crazy trying to finish the presentation due for a monthly performance meeting the next morning. The model is refreshed, and now it just takes a LOT of copying, pasting, and positioning to get the PowerPoint ready. Finally, the slides are finished…, until you read a new message from your boss requesting a minor change. But of course her change means you have to start all over with the copy and pastes…

There is always a better way! In the Oil and Gas industry, I constantly have monthly reports to assess the performance of our operating assets. Excel VBA makes it a cinch to automate the entire process. So when a simple change is requested, the presentation is automatically generated with the click of a button. No more wasting time!

So, here it is – How to Save TONS of Time by Using an Excel VBA Macro to Build Your Presentation:
-------------------------------------------------------------------------------------------------

1\. Build your charts in Excel

2\. Create a new worksheet and paste in all the charts you need for the presentation.  
![Excel to PowerPoint using VBA - Step 2](https://chandoo.org/img/vba/Step2-Excel-to-powerpoint-vba.png)

3\. Open VBA. To do this, you can either press ALT + F11, or you can take the following steps:

a. To show the developer tab, click on the Microsoft Office Button and click Excel Options.  
![Excel to PowerPoint using VBA - Step 3a](https://chandoo.org/img/vba/Step3a-Excel-to-powerpoint-vba.png)

b. Click Popular and then select the Show Developer tab in the Ribbon.  
![Excel to PowerPoint using VBA - Step 3b](https://chandoo.org/img/vba/Step3b-Excel-to-powerpoint-vba.png)

c. Click on the Developer tab in the ribbon and click Visual Basic.  
![Excel to PowerPoint using VBA - Step 3c](https://chandoo.org/img/vba/Step3c-Excel-to-powerpoint-vba.png)

4\. In your VBA Editor window, click File => Insert => Module.  
![Excel to PowerPoint using VBA - Step 4](https://chandoo.org/img/vba/Step4-Excel-to-powerpoint-vba.png)

5\. Paste the [following code](https://img.chandoo.org/vba/Automatically_Create_PowerPoint_From_Excel_VBA_Code.txt)
 into the module (I included comments so you can customize it to your liking).  
![Excel to PowerPoint using VBA - Step 5](https://chandoo.org/img/vba/Step5-Excel-to-powerpoint-vba.png)

6\. Click Tools => References.  
![Excel to PowerPoint using VBA - Step 6a](https://chandoo.org/img/vba/Step6a-Excel-to-powerpoint-vba.png)

Add the Microsoft PowerPoint Library.  
![Excel to PowerPoint using VBA - Step 6b](https://chandoo.org/img/vba/Step6b-Excel-to-powerpoint-vba.png)

7\. Now all you need to do is go to Excel and run the CreatePowerPoint macro! To make this easy, draw a rectangle shape in your Excel worksheet which contains all the charts you want to export to PowerPoint.

![Excel to PowerPoint using VBA - Step 7](https://chandoo.org/img/vba/Step7-Excel-to-powerpoint-vba.png)

8\. Right click the rectangle and click Assign Macro.  
![Excel to PowerPoint using VBA - Step 8](https://chandoo.org/img/vba/Step8-Excel-to-powerpoint-vba.png)

9\. Click on the CreatePowerPoint macro and press Okay.  
![Excel to PowerPoint using VBA - Step 9](https://chandoo.org/img/vba/Step9-Excel-to-powerpoint-vba.png)

10\. That’s it! Just click your rectangle button then sit back and watch it run! You’ll have your presentation in no time!  
![Excel to PowerPoint using VBA - Step 10](https://chandoo.org/img/vba/Step10-Excel-to-powerpoint-vba.png)

Download the Example Workbook & Play with this Macro
----------------------------------------------------

[**Click here to download the example workbook and play with the macro**](https://img.chandoo.org/d/Automatically_Create_PowerPoint_From_Excel.xlsm)
.

_**Note:**_ If you have an error with Power Point application activation, use this code instead.

AppActivate ("Microsoft PowerPoint")  <-- if this doesn't work

AppActivate "PowerPoint" <-- use this

Thanks Drew
-----------

Thank you so much _**Drew**_ for writing this insightful article and showing us how to automate PPT Creation thru Excel VBA. I have really enjoyed playing this idea. And I am sure our readers will also like it.

**_If you like this technique, say thanks to Drew._**

How do you Automate PPT Creation?
---------------------------------

During my day job, I used to make a lot of presentations. But each one was different. So I used to spend hours crafting them.

And nowadays, I hardly make a presentation. But I know many of you make PPTs day in day out. And this technique presented by _**Drew**_ is a very powerful way to save time.

_Do you use macros to automate creation of presentations?_ What are your favorite tricks & ideas? **Please share using comments.**

Learn More VBA – Sign-up for our VBA Class Waiting List
-------------------------------------------------------

Chandoo.org runs a VBA Class that teaches you from scratch, how to build macros to save time & automate your work. We opened our first batch in May this year and had an excellent response. More than 650 students signed up and are now learning VBA each day.

If you want to learn VBA & advanced Excel, this is a very good class to join.

[**Click here for full information on VBA classes**](https://chandoo.org/wp/vba-classes/)
.

### **About the Author:**

_**Drew Kesler**_ specializes in process automation and data visualization. He currently performs analytics and modeling for the Oil and Gas industry. His most recent projects include using GIS mapping technology to visualize data and enhance interaction across organizations.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [212 Comments](https://chandoo.org/wp/create-powerpoint-presentations-using-excel-vba/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/create-powerpoint-presentations-using-excel-vba/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [Automation](https://chandoo.org/wp/tag/automation/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [macros](https://chandoo.org/wp/tag/macros/)
    , [powerpoint](https://chandoo.org/wp/tag/powerpoint/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousShift Calendar Template – FREE Download](https://chandoo.org/wp/shift-calendar-excel-template/)

[Next10 Excel Keyboard Shortcuts I can’t live without!Next](https://chandoo.org/wp/must-have-excel-keyboard-shortcuts/)

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
    
    [Reply](https://chandoo.org/wp/create-powerpoint-presentations-using-excel-vba/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/create-powerpoint-presentations-using-excel-vba/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/create-powerpoint-presentations-using-excel-vba/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ