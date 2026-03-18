# Image Lookup - How-to show dynamic picture in a cell [Excel Trick] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/excel-image-lookup

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Image Lookup – How-to show dynamic picture in a cell \[Excel Trick\]
====================================================================

*   Last updated on December 16, 2020

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Do you ever want to have an image or picture lookup in Excel? Something like below.

![Demo of Excel Image Lookup - Search and display matching image](https://chandoo.org/wp/wp-content/uploads/2020/12/image-lookup-demo.gif)

In this article, learn how to set up an image lookup using Excel. You can use this to display staff details, product images or machine parts etc.

Video - Dynamic Image Lookups in Excel
--------------------------------------

If you want to understand the picture lookup technique and see it in action, check out my YouTube video below. For text instructions and images, please read on.

Step 1: Set up your data
------------------------

To get image lookups, you need to set up your data, ideally in a separate worksheet. **The trick is to have one image per cell**. Something like this:

![image lookup - sample data](https://chandoo.org/wp/wp-content/uploads/2020/12/image-lookup-sample-data.png)

**Tip:** _**Do not** **use Tables**_ for storing your data. Instead keep them in a spreadsheet range.

Your images need to **fit snugly inside the cell**, without touching the boundaries for best results.

Also make sure to turn off gridlines on that spreadsheet tab.

You can do this from View ribbon, as depicted below.

![disable gridlines for image lookups](https://chandoo.org/wp/wp-content/uploads/2020/12/disable-gridlines-for-image-lookups.png)

Step 2: Write formula to lookup the image
-----------------------------------------

In a separate worksheet, we will write formula to lookup images. Let’s say we have an input cell with employee name in **C5**.

We need to get the matching employee picture.

The trick is to writ**e a formula that returns a reference** to the image of employee in C5.

You can use either [INDEX+MATCH](https://chandoo.org/wp/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
 or [XLOOKUP](https://chandoo.org/wp/xlookup-examples/)
. 

Let’s use XLOOKUP:

\=XLOOKUP(C5, data!$D$3:$D$14, data!$C$3:$C$14) 

This will return a **reference to the cell** with the image of employee in C5.

Of course the result of the formula would be 0, as column C (data!$C$3:$C$14) has no values (just pictures) in it.

Step 3: Insert a named range with the formula
---------------------------------------------

Now that we know what formula to write, go to Formula ribbon and click on Define name button. 

*   Name will be “employee\_picture”
*   Refers to will be our XLOOKUP formula from above

See below illustration to understand how the name can be created.

![](https://chandoo.org/wp/wp-content/uploads/2020/12/xlookup-or-indexmatch-formula-for-getting-the-image.png)

Step 4: Set up a picture link to show **image lookup** result
-------------------------------------------------------------

This is the last step folks. Go to the data worksheet where you have all the pictures.

1.  Select any one cell with image and copy it (CTRL+C).
2.  Go back to the results worksheet, right click anywhere and select **linked picture** from Paste Special options. See below picture to understand.

![linked picture (camera tool) option in Excel paste special menu](https://chandoo.org/wp/wp-content/uploads/2020/12/linked-picture-camera-tool-option-in-Excel-paste-special-menu.png)

3.  You will get a picture of the selected employee. But this one is special. It is _linked to the cell you copied._ 
4.  Select the picture and formula bar will show the address of the cell to which it refers.
5.  Now comes the most important step. Go to formula bar and edit the reference. Type _**\=employee\_picture**_ and press enter.

Bingo, you have just created a picture lookup. 

If you change the input cell and type a different person name, the lookup image will show that person.

Related: [Learn more about Picture Links](https://chandoo.org/wp/how-to-use-picture-links/)

Tips on using Image Lookup Technique
------------------------------------

Image lookup through **picture links** offers exciting possibilities. Here are some tips & gotchas you want to keep in mind.

*   The picture link images are just like any other images in Excel. So when you select them, you can use **picture format** ribbon to apply various formatting options to them. For example, you can crop them to shape or apply shadow effect to them.
*   Picture links work best if all images are of same size. 
*   While picture links look great on screen, they tend to be grainy when printed.
*   They work well with dashboards too. For example, You can use picture links to display top 3 products or bottom 5 sales persons in dashboards.
*   For image lookup scenarios, consider adding a _missing person_ image and use that in XLOOKUP _if\_not\_found_ parameter. It looks amazing.

⬇ Download Picture Lookup Example File
--------------------------------------

[**Click here to download sample file with the picture lookup example**](https://chandoo.org/wp/wp-content/uploads/2020/12/image-in-a-cell.xlsx)
. It has few different XLOOKUP formulas, an additional image lookup trick to show team members and more. Examine the named ranges to learn how it works.

Got questions about image lookups? Fire away...
-----------------------------------------------

Give picture lookups a try and if you face any issues during implementation, please post a comment here so I can help you.

Also, check out these other types of lookups:

*   [Range lookup, find matching range based on input value](https://chandoo.org/wp/range-lookup-excel/)
    
*   [Lenient lookup – get the _almost matching_ value](https://chandoo.org/wp/lenient-lookup-advanced-trick/)
    
*   [Pricing tier lookup problem](https://chandoo.org/wp/pricing-tier-lookup-formula/)
    
*   Important lookup functions in Excel
    *   [XLOOKUP](https://chandoo.org/wp/xlookup-examples/)
        
    *   [VLOOKUP](https://chandoo.org/wp/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
        
    *   [INDEX+MATCH](https://chandoo.org/wp/vlookup-match-and-offset-explained-in-plain-english-spreadcheats/)
        
    *   [OFFSET](https://chandoo.org/wp/offset-formula-explained/)
        

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [15 Comments](https://chandoo.org/wp/excel-image-lookup/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/excel-image-lookup/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [images](https://chandoo.org/wp/tag/images/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [picture links](https://chandoo.org/wp/tag/picture-links/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    , [xlookup](https://chandoo.org/wp/tag/xlookup/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPrevious9 Box grid for talent mapping – HR for Excel – Template & Explanation](https://chandoo.org/wp/9-box-talent-map-template/)

[NextMerry Christmas & Happy New Year 2021Next](https://chandoo.org/wp/holiday-card-2020/)

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
    
    [Reply](https://chandoo.org/wp/excel-image-lookup/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/excel-image-lookup/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/excel-image-lookup/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ