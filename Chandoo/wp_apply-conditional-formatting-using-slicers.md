# Apply Conditional Formatting using Slicers

**Source:** https://chandoo.org/wp/apply-conditional-formatting-using-slicers

---

*   [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Apply Conditional Formatting using Slicers
==========================================

*   Last updated on May 13, 2016

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Have you ever wondered about applying different Spreadsheet Formats to reports which may be send to different people and so the styling may be different for each recipient?  The Boss may get a Formal report where the Art department may get a Funky version of the same data?

No, Neither had I until recently when somebody asked me for just that:

#### Boss Style

[![CFUS01](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS01.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS01.png)

#### Black & White Style

[![CFUS02](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS02.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS02.png)

#### Funky Style

[![CFUS03](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS03.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS03.png)

#### Blue Style

[![CFUS15](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS15.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS15.png)

Of course using Conditional Formats you can highlight cells based on criteria, so why not extend that to the Whole Report Styling?

This tutorial will detail just that.

Lets get started

Download the Sample File (Excel 2013 & 2016 + only): [Download Sample File](https://chandoo.org/wp/wp-content/uploads/2016/05/CF-Using-Slicer2.xlsx)

### **Firstly Identify your Report Area**

In this case it is B8:E28

[![CFUS04](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS04.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS04.png)

Note: The area above includes the header row, Row 8, but you can actually apply different CF’s to hat independently of the data area if you require

### **Make a list of Style Names**

I have used four namely: **Boss, Blue, Black & White and Funky**.

[![CFUS06](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS06.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS06.png)

Add an Id next to each from 1 to x in this case 4 as there are 4 entries

Convert the Table to a Table by selecting the area **E2:F6**

**Goto Insert, Table**

[![CFUS05](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS05.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS05.png)

### **Add a Style Link cell**

In a spare cell **H2**: add a formula like: \=SUBTOTAL(4,Style\[Id\])

This will extract the Maximum value from the Table when the non-selected rows are hidden.

I have also Named the cell **Style\_Link**

[![CFUS07](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS07.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS07.png)

### Add a Slicer

Select any cell in the Style Table and goto the **Insert**, **Slicer** menu

An **Insert [Slicers](http://chandoo.org/wp/2015/06/24/introduction-to-slicers/)
** dialog pops up, Select **Style**

[![CFUS08](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS08.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS08.png)

You will now have a Slicer linked to the Styles table

[![CFUS09](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS09.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS09.png)

You can format the slicer as appropriate, Resize and Rename it if required

[![CFUS10](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS10.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS10.png)

### Apply Conditional Formats to the Report

Now select the report area and apply four Conditional Formats which will be styles according to the Useage

You normally only apply 3 styles as the default is already a style

Select **B8:E28**

Goto the **Conditional Format**, **New Rule**, **Use a Formula** menu

Apply the formula and format to suit your needs

**Boss**

This is my Default style when Style\_Link = 1

Hence I don’t need to apply a specific style

**Blue**

This is my Conditional Format style when Style\_Link = 2

[![CFUS11](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS11.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS11.png)

Note: the formula used is \=AND(B8<>””, Style\_Link=2)

So the Conditional Format will only apply this to cells in the area with a value in them and when the Style\_Link cell = 2

**Black & White  
**

This is my Conditional Format style when Style\_Link = 3

[![CFUS12](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS12.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS12.png)

Note: the formula used is \=AND(B8<>””, Style\_Link=3)

So the Conditional Format will only apply this to cells in the area with a value in them and when the Style\_Link cell = 2

**Funky**

This is my Conditional Format style when Style\_Link = 4

[![CFUS13](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS13.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS13.png)

Note: the formula used is \=AND(B8<>””, Style\_Link=4, ISODD(Row))

So the Conditional Format will only apply this to cells in the area with a value in them and when the Style\_Link cell = 4 and the Row Number is Odd

Obviously we need to apply a second Conditional Format  for when the even numbered Rows

It will use the Conditional Format formula: \=AND(B8<>””, Style\_Link=4, ISEVEN(Row))

You should end up with four Conditional Formats listed as:

[![CFUS14](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS14.png)](https://chandoo.org/wp/wp-content/uploads/2016/05/CFUS14.png)

### Closing Notes

Although in this post I have used a Slicer to supply the user a list of Styles for choice, you could simply use a single cell with a Data Validation Drop Down or a Combo Box to control the style selection process.

The client for which this technique was applied had a dashboard and wanted to have the control appear similar to other slicers on the dashboard hence maintaining the look and feel of the dashboard.

### Conclusion

You now have a tool which allows you to dynamically change the styling of your worksheet reports.

You can add extra formatting by using the **Style\_Link** cell to say change the Decimal Places of the numbers in Column E of the report

eg: Assuming my Sales Data is in Column **AA**, which it is.

In **E9**:  \=TEXT(AA9,CHOOSE(Style\_Link,”$A 0,000.00″,”A$ 0,000″,”AU\\D 0,000″,”F$ 0,000″)))

Copy down

This will apply 2 decimals to Column E when the Boss Style (1) is chosen and zero decimals for everybody else

It will also apply different currency leaders for the different styles

Style 1: Boss $A

Style 2: Black & White A$

Style 3: Boss AUD

Style 4: Funky $F

As mentioned in one of the notes above, you can apply Conditional Formatting independently to the Headers, Footers or Summary areas of the Report, your imagination is the limit.

I’m sure you can think of other modifications to the layout that can be implemented using these techniques

**Other Style Links**

You may be interested in these other links to worksheet styling functionality:

[http://datapigtechnologies.com/blog/index.php/getting-fancy-with-your-excel-slicers/](http://datapigtechnologies.com/blog/index.php/getting-fancy-with-your-excel-slicers/)

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [12 Comments](https://chandoo.org/wp/apply-conditional-formatting-using-slicers/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/apply-conditional-formatting-using-slicers/#respond)
    
*   Tagged under [Pivot Table](https://chandoo.org/wp/tag/pivot-table/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    
*   Category: [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [hacks](https://chandoo.org/wp/category/hacks/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousExtract the 10 digit number \[formula homework\]](https://chandoo.org/wp/extract-the-10-digit-number-formula-homework/)

[NextExcel Tips, Tricks, Cheats & Hacks – Readers Edition PrequelNext](https://chandoo.org/wp/excel-tips-tricks-cheats-hacks-readers-edition-prequil/)

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
    
    [Reply](https://chandoo.org/wp/apply-conditional-formatting-using-slicers/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/apply-conditional-formatting-using-slicers/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/apply-conditional-formatting-using-slicers/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ