# Comparing Sales of One Product with Another [Excel Techniques] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/comparing-sales-excel-techniques

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Comparing Sales of One Product with Another \[Excel Techniques\]
================================================================

*   Last updated on April 25, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**This is a guest article by [Theodor](http://chandoo.org/wp/tag/theodor/)
**_ on how to Compare Sales of One Product with Another

Ok, now here’s one for you.

**Suppose you’d like to come up with a sales report on different products**, comparing their evolution on the same period of different years (say Jan ’09 vs. Jan Jan ’10). At the same time, you’d like to keep an eye on their yearly trend (entire 2009 vs. entire 2010).

**No big deal, you’ll say, but here’s the twist: _the products have not been available for the entire time span taken into consideration._** Let’s say you’ve only had Product 1 available for sale for Feb ’09 onwards, while it had been discontinued from October ’10. If you’re really looking for a Like-For-Like (LFL) comparison, you’d only want to compare the months where you have data for both years. It’s false to claim you’ve had a sales boost of 300% when you entered the market with Product X in October 2009, selling 1000 units over 3 months and compare that to the full results of 2010, when you’ve sold 3000 units. In the first scenario you were averaging some 333 units/month, while later you’ve dropped to a mere 250/month. Nothing to brag about there, is it?

**Ah, but we also have different product classes.** One is aimed for the high-profile buyer (A-Class products), the second for the middle level (B-Class) and so on. Given that different products were added to each class’s portfolio and then later discontinued, we should see the total LFL development of each product class in the same graphical representation.

**Hold on another second. One country is defining its quarters as Jan-Mar, Apr-Jun etc, while other** might relate a quarterly result to a specific day in the company history (such as the company launch date, or since the new CEO took over or whatever). Wouldn’t it be nice to be able to compare equivalent datasets in any user-defined time span?

### So how do you compare sales of one product with another?

**Now I’ve always said that the second hardest thing mankind has ever done was to send men on the Moon and safely return them home.** _**That’s only because the MOST difficult thing in the world has become to compare apples with apples.**_ There are so many subtle differences between one dataset and the other (even though they both relate to the same source), that if one reporting template is to have a long life, it should first and foremost come with the built-in ability to allow the end user to drill down through the data and change criteria in order to get relevant results for today’s issue. And all that will change tomorrow, as there will lay a new and unexpected issue on the table.

With that in mind, when I create my templates I follow the self-made golden rule (which later I found many others have applied for themselves long before I knew Excel ever existed) – keep the raw data in one sheet, preferably hidden; use a second sheet for calculation, ALWAYS hidden, and provide a simple and useful graphical interface for the end-user in the third sheet. This will avoid any mishaps such as “Could you please put your formulas back in, I donno which button I pressed and….!!”

### Comparing Sales of One Product with Another – Demo:

First see the demo of this technique. Then, we can learn how I created it.

![Comparing Sales of One product with Another - Demo](https://chandoo.org/img/c/comparing-sales-of-one-product-with-another-demo.gif)

### Coming to the attached example – which only works in Excel 2007 and later, by the way:

*   Your data is in sheet ‘data’, ordered by product and timeline (Jan-Dec, 2009 and 2010). I’ve created the values using the =randbetween() formula, and then copy-pasted the values only so they will not change anymore.
*   To keep things more clear, I’ve placed the calculation formulas in the same sheet as that with the graph, just so you can compare values and figure out formulas more quickly, without having to switch between sheets all the time.

![Comparing Sales - Data](https://chandoo.org/img/c/comparing-sales-data.png)

### How the Sales Comparison Chart is made?

_**Now, to bring up values of a particular product,**_ I’ve created a list in C44:C70 (values in column B are just for guidance). We can compare two products, which can be chosen from a couple of drop-down boxes linked to cells B6 and B8. Here’s where the values in column B help: basically, they tell me which item index from the drop-down corresponds to a product. I then placed the same item indexes in data!A7:A46. This is all because I am lazy and I find [the sumifs() formula](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/ "Introduction to Excel SUMIFS Formula")
 a blessing: all I have to do now is to add up the results that correspond to (1) the chosen Product in the drop-down, which is looked up by the index, and (2) the year, which is in data!E6:E45. \[[More on INDEX Formula](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)\
\]

![How does the sales comparison chart work](https://chandoo.org/img/c/how-does-sales-comparison-chart-work.png)

An alternative in Excel 2003 would have been to concatenate the value of “Product 1″&”2009” for example, to get a unique identifier and not return the sales value of 2010 by mistake. Then vlookup() after the concatenated value. \[Related: [How to lookup based on multiple conditions](http://chandoo.org/wp/2010/11/02/multi-condition-lookup/)\
\]

These calculations are placed in ‘Yr sls’!F51:Q54. Note there’s an initial IF() there, to only display the values if the respective month is selected. There are two sliders up in the second row, which can help you ‘cut’ your desired portion of the year for comparison.

‘Yr sls’!F61:Q68, using sumifs() again, I added the sales values for each product class. Finally, in ‘Yr sls’!F45:Q48 are the final calculation, where if an item index lower than 8 (corresponding to Product 1) is selected, the values in F61:Q68 are brought up, else the values in F51:Q54.

So now we see our resulting values above the chart, in cells F6:Q9. The deviation is calculated in F5:Q5. But for the yearly totals, I only want to compare apples with apples, i.e. months in which sales have been recorded in both years. For that I used cells U6:AF9. The totals in R6:R9 are based on these isnumber() results. This allows you to have the exact deviation between similar months over an user-defined time span.

Ok, time to close. But not before your boss knows the exact portfolio of each product class! Look shortly in data!B6:B45. This is where, using countif(), we have the number of occurrences for each product class. Knowing that product class “A” will be repeated say 3 times, we’ll use this knowledge to look up the third occurrence of “A” and bring up the product next to it. Now take a peak in sheet “Legend”. Knowing we have to lookup for A 1, that’s how I wrote the formula. But also knowing that “A” will be repeated twice for each product (once for 2009, another for 2010) and not wanting to see duplicates in my product list, there’s a very simple solution: just use odd numbers!! This will only bring up every 2nd occurrence of a product. As I said, I like it simple 🙂 I just left the numbers in C5:C15 visible so you don’t have to fish around for them, the rest are simply I the same color as the background. A bit of conditional formatting does the rest.

Of course, before presenting this to any decision maker, you’d hide the rows and columns they’re not supposed to touch and present them with a clean looking table.

### Download the Excel Workbook:

[**Click here to download the workbook**](https://img.chandoo.org/d/sales-trend-analysis.xlsx)
 with this example. Examine the formulas and chart in “Yr Sls” worksheet to understand how this is weaved together.

**\[Added by Chandoo\]**

### Thank you Theodor

Thank you so much _Theodor_ for teaching us some valuable techniques on how to compare apples with apples. I am sure our readers will find these ideas very useful.

If you like this post, say thanks to _Theodor_.

### Do you compare & analyze sales data?

I do this all the time. As part of running my small business, every couple of months, I would take up sales data and see if something odd is going on. I make line charts comparing sales of this year with previous year, understanding the overall trend and compare one product with another.

_**What about you?**_ Do you analyze sales data? What techniques do you use use? **Please share using comments.**

### Learn more from these pages:

_**If you work a lot with data & do similar work as above, go thru these articles to learn more.**_

*   [Comparison charts using Form Controls](http://chandoo.org/wp/2009/03/12/comparison-charts-1/)
    
*   [Introduction to Excel Form Controls](http://chandoo.org/wp/2011/03/30/form-controls/ "Form Controls – Adding Interactivity to Your Worksheets")
    
*   [Budget vs. Actual Charts in Excel](http://chandoo.org/wp/2009/04/05/budget-vs-actual-charts/ "Budget vs. Actual Charts – 14 Charting Ideas You can Use")
    
*   More: [Comparison Charts – Examples & Techniques](http://chandoo.org/wp/tag/comparison-charts/)
    
*   More: [Excel Dynamic Charts – Examples, Demos & Techniques](http://chandoo.org/wp/tag/dynamic-charts/)
    
*   Join: [**My Excel School Program to learn these and many other Excel techniques**](http://chandoo.org/wp/excel-school/)
    

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [15 Comments](https://chandoo.org/wp/comparing-sales-excel-techniques/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/comparing-sales-excel-techniques/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [Charts and Graphs](https://chandoo.org/wp/tag/charts-and-graphs/)
    , [comparison charts](https://chandoo.org/wp/tag/comparison-charts/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [drop down lists](https://chandoo.org/wp/tag/drop-down-lists/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [isnumber](https://chandoo.org/wp/tag/isnumber/)
    , [line](https://chandoo.org/wp/tag/line/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [na()](https://chandoo.org/wp/tag/na/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    , [theodor](https://chandoo.org/wp/tag/theodor/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousThere is an Easter Egg in Excel!](https://chandoo.org/wp/chandoo-org-startup-story-2/)

[NextUpdate Report Filters using simple macro – a Dynamic Pivot Chart ExampleNext](https://chandoo.org/wp/update-report-filter-macro/)

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
    
    [Reply](https://chandoo.org/wp/comparing-sales-excel-techniques/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/comparing-sales-excel-techniques/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/comparing-sales-excel-techniques/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ