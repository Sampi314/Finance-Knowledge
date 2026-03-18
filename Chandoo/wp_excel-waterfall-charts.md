# Excel Waterfall Chart - Tutorial and Template - Learn how to make waterfall charts using MS Excel

**Source:** https://chandoo.org/wp/excel-waterfall-charts

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    

Waterfall Charts using Excel
============================

*   Last updated on October 8, 2009

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is a guest post from **Aaron Henckler**._

**Waterfall charts are great, especially for visually showing the contribution of parts to a whole.** While there are several tutorials on how to make a waterfall chart online the end products of these tutorials rate low on the visually appealing scale.

The principle problem with these charts is the separation between the elements of the waterfall. They are always either pushed together (Example A) or left apart, without element connectors (Example B):  
Example A

![Example Waterfall chart using excel - 1 Tutorial & Download](https://chandoo.org/wp/wp-content/uploads/2009/08/excel-waterfall-chart-1.png)

Example B  
![Example Waterfall chart using excel - 2 ](https://chandoo.org/wp/wp-content/uploads/2009/08/excel-waterfall-chart-2.png)

Many users of waterfall charts employ the separated (default) version (example B) opting to add in element connectors manually via Insert>Shapes>Line on the Excel tool bar. The frustration with this approach is that all too often the values of the chart elements will need to be updated or changed forcing user to manually readjust each of their connector lines in turn.

**With some simple charting trickery in Excel 2007 one can easily make a waterfall chart with connectors that will update automatically as element values are changed.**

### A Better Waterfall Chart

![Ideal waterfall chart using excel ](https://chandoo.org/wp/wp-content/uploads/2009/08/excel-waterfall-chart-3.png)

Steps to Building a Better Waterfall Chart
------------------------------------------

**List of data series (columns) needed for your chart:**

*   **Horizontal Axis Labels**: in the example above North, East, South and West.
*   **Base Values:** What your element values will “sit on.” Essentially this is the white space beneath each charted element shown above.
*   **Element Values**: the meat and potatoes of your chart – the value of your elements as you want them to appear (above these are 40, 30, 20, 10 and 100).
*   **Label Spaces**: This is optional but it allows you to place the value of you data elements on top of their respective bars (this avoids the use of the annoying Label Position options available after one has used Add Data Labels).
*   **Label Connectors**: This is the key item needed to create the chart as shown above. You will need one column (series) for each of the data elements (excluding one for the total). For the chart above, four label connector series are needed.

### Step 1: Enter all of the required series in a worksheet:

![Data for the waterfall chart ](https://chandoo.org/wp/wp-content/uploads/2009/08/excel-waterfall-chart-4.png)

*   Horizontal Axis Labels – self explanatory
*   Base Values – A running total of the subsequent Element Values (Column C). Whereas nothing proceeds North in the example above leave its base value blank. Do the same for Total.
*   Element Values – These are whatever numbers you want to highlight in your chart. These are represented by the blue column segments in the above chart.
*   Label Spaces – Again this is optional. These will eventually hold text labels for the Element Values (Column C). The numbers here should all be the same and be some number about 1/4 to 1/3 the value of your lowest Element Value.
*   (to H. ) Connectors – Connectors 1 to 4 correspond to Axis Labels North to West in the example above. In the respective Connector column make the cell at the row corresponding to the related Axis Label equal to the sum of Column B + Column C (Base Value + Element Values). Enter the same value for the cell beneath.

### Step 2: Chart data and adjust

1\. **Select your data, here A2:H6, and go to Insert>Charts>Column>2-D Column>Stacked Column>OK** (to exit). Your chart should look like this:  
![Step 2.1 - waterfall chart using microsoft excel ](https://chandoo.org/wp/wp-content/uploads/2009/08/excel-waterfall-chart-5.png)

2\. **Switch column and row data** by right-clicking within the chart and going to Select Data…>Switch Row/Column>OK (to exit). Chart should now look something like this:  
![Step 2.2 - waterfall chart using microsoft excel ](https://chandoo.org/wp/wp-content/uploads/2009/08/excel-waterfall-chart-6.png)

3\. The top colored column element in each column (purple, aqua, orange and baby blue, respectively) is what will become that Element Value’s connector. To convert to these columns to connectors, in turn, right-click on the series (the first one is the purple column element) and go Change Series Chart Type…>Line>Line>OK (to exit). Repeat this process for the other connector column elements (aqua, orange and baby blue). After this step your chart should look like this:  
![Step 2.3 - waterfall chart using microsoft excel ](https://chandoo.org/wp/wp-content/uploads/2009/08/excel-waterfall-chart-7.png)

4\. Follow this up by formatting each connector in turn. Right-click on the connector and go Format Data Series…. Consider making the Line Color>Solid Line>Color black, Line Style>Width .25 pt and Line Style>Dash Type>Square Dot. Play around with these options as you see fit to get the best look. Again, do this for each connector.

5\. **Remove grid lines (optional), delete the Legend (necessary)**. Your chart should now look like this:  
![Step 2.5 - waterfall chart using microsoft excel ](https://chandoo.org/wp/wp-content/uploads/2009/08/excel-waterfall-chart-8.png)

6\. Go into you Base Values series (blue column element in the chart above) and eliminate the color fill and borders: right-click on a blue column element and go Format Data Series….>Fill>No Fill and Border Color>No Line>Close (to exit).

7\. Format your Element Values series (red above, using same process in Step 6 to change the fill color and add a border.

8\. Right-click on your Label Spaces series and go Add Data Labels…. Don’t worry about the value on the labels for now, they’ll be changed in the next step. Follow this up by formatting the Label Spaces series just like how the Base Values series was formatted (in Step 6). Make it so there is no fill and there are no borders. This is what you should now have:  
![Step 2.8 - waterfall chart using microsoft excel ](https://chandoo.org/wp/wp-content/uploads/2009/08/excel-waterfall-chart-9.png)

9\. All that remains is to convert your labels to the values of the Element Values. To do this for each label: click on the specific label twice (so that only the box for that label appears, as below).  
![Step 2.9 - waterfall chart using microsoft excel ](https://chandoo.org/wp/wp-content/uploads/2009/08/excel-waterfall-chart-10.png)

Click a third time on the edge of the box that appears and then type the equals sign “=”. Now go back to your data table and click on the cell of the Element Value that you want appear in the label. Then press enter. This links the value of the label to the Element Value (if your Element Value ever changes so too will the text in this label). Repeat this for the other data labels in turn. The result is your Better Waterfall Chart:

![Final waterfall charting - Microsoft Excel ](https://chandoo.org/wp/wp-content/uploads/2009/08/excel-waterfall-chart-11.png)

Download the Waterfall Chart Template:
--------------------------------------

Please download the waterfall chart template from [here](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/excel-waterfall-chart-template.xls)
 \[[.zip version here](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/excel-waterfall-chart-template.zip)\
\]

Final Thoughts
--------------

I hope you will agree that this waterfall chart is more visually appealing that the examples at the start of this tutorial. In addition to a more professional look this waterfall will fully update (step heights, labels, connector positions) automatically whenever you change your Element Values. While the process of implementing this form of waterfall chart may at first seem cumbersome it can be quickly implemented with some practice and is a great item to have in your charting toolkit. **Enjoy**.

### Note from PHD:

*   _**Thank you so much Aaron.**_ You have taught us a very valuable tutorial. I really appreciate your effort in putting this together.
*   If you need to make a lot of waterfall charts, I recommend trying [Jon Peltier’s Waterfall Chart Utility](https://www.e-junkie.com/ecom/gb.php?ii=372211&c=ib&aff=49044&cl=84674)
    .

Hello there, Reader: **If you like this waterfall chart tutorial, please drop a note of thank you to Aaron through comments**.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [106 Comments](https://chandoo.org/wp/excel-waterfall-charts/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-waterfall-charts/#respond)
    
*   Tagged under [bar charts](https://chandoo.org/wp/tag/bar-charts/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [column charts](https://chandoo.org/wp/tag/column-charts/)
    , [combination charts](https://chandoo.org/wp/tag/combination-charts/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [line charts](https://chandoo.org/wp/tag/line-charts/)
    , [microsoft](https://chandoo.org/wp/tag/microsoft/)
    , [tutorial](https://chandoo.org/wp/tag/tutorial/)
    , [visualizations](https://chandoo.org/wp/tag/visualizations/)
    , [waterfall charts](https://chandoo.org/wp/tag/waterfall-charts/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    

[PrevPreviousWhat would you do if a co-worker makes ugly chart? \[weekend poll\]](https://chandoo.org/wp/what-you-do-if-coworker-makes-ugly-chart/)

[NextMember of month, Excel links and Cooked HDDNext](https://chandoo.org/wp/excel-links-mom-edition/)

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
    
    [Reply](https://chandoo.org/wp/excel-waterfall-charts/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-waterfall-charts/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-waterfall-charts/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ