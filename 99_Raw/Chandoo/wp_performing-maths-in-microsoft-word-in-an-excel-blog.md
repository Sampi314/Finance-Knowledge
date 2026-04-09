# Performing Maths in Microsoft Word (In an Excel Blog) » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/performing-maths-in-microsoft-word-in-an-excel-blog

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [Word](https://chandoo.org/wp/category/word/)
    

Performing Maths in Microsoft Word (In an Excel Blog)
=====================================================

*   Last updated on August 31, 2018

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Ok, Ok, Chandoo.org is clearly a Microsoft Excel centric Blog.

But a week ago Pradeep asked the question in a post, “_How do I add up a Table of Numbers in Word?_”

There are 3 easy answers, which will all be addressed in this post:

1.  Transfer the Data to/from Excel
2.  Embed a Table in Word from Excel
3.  Do the Maths in Word

Transfer Data To/From Excel
---------------------------

The easiest and sometimes quickest way to do maths on a table of numbers is to:

*   Copy the Table from Word and paste the Table into an Excel Workbook
*   Perform the Maths in Excel
*   Copy and paste the results back

Here is a typical Table within Word

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW00.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW00.png)

Select the Table in Word and press either **Ctrl+C** or use the Copy [![](https://chandoo.org/wp/wp-content/uploads/2018/08/Copy.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/Copy.png)
 icon.

Open Excel or switch to Excel using **Alt+Tab**

Select a cell and press Paste **Ctrl+V** or use the Paste [![](https://chandoo.org/wp/wp-content/uploads/2018/08/Paste.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/Paste.png)
 Icon

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW001.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW001.png)

Excel shows the Table as above.

Next add formulas to perform the calculations you need

In this case in **C9:** **=SUM(C4:C8)**

Copy the formula in **C9** across to **D9**

In **E4:** **\=D4/C4**

Copy the formula in **E4** down to **E9**

Format the new results as appropriate

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW02.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW02.png)

Next select either the full table or a section, ie: The Numbers and Copy using either **Ctrl+C** or use the Copy [![](https://chandoo.org/wp/wp-content/uploads/2018/08/Copy.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/Copy.png)
 icon.

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW03.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW03.png)

Switch to Word using **Alt+Tab**

Select the same area in the Word Table as what you copied in Excel

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW04.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW04.png)

and press Paste **Ctrl+V** or use the Paste [![](https://chandoo.org/wp/wp-content/uploads/2018/08/Paste.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/Paste.png)
 Icon [![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW05.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW05.png)

**When to use this technique**

This technique is useful for doing one of reports where the data is provided to you as is.

It is also good when you need to perform complex formulas.

However when you control the data source there is an easier way and this is discussed next.

Embed the Table in Word from Excel
----------------------------------

In cases where you manage the data source, you can link the table in Word directly to the data source in Excel.

By doing this the Word Table is updated as soon as changes are made in the Excel Table.

In Excel find your source data:

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW10.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW10.png)

Select the range you want to embed into the word Document

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW11.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW11.png)

Copy this range using either **Ctrl+C** or use the Copy [![](https://chandoo.org/wp/wp-content/uploads/2018/08/Copy.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/Copy.png)
 icon.

Open **Word** or Switch to **Word** using **Alt+Tab**

Locate and click in the area in the Word Document where you want to place the report

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW12.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW12.png)

Goto the Home Tab and press Paste **Ctrl+V** or use the Paste [![](https://chandoo.org/wp/wp-content/uploads/2018/08/Paste.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/Paste.png)
 Icon

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW13.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW13.png)

Select the **Paste and Keep Source Formatting** option

**Note 1**: As you move across the 6 paste options word will show you what the Pasted range will look like using each format

**Note 2**: Notice in the example above the pasted range also includes the grey grid lines. If you don’t want these you need to disable them in Excel before you copy the range

Now that we have our Word Document with the new Range pasted in, you notice that there is a mistake in the data

Return to Excel by Using **Alt**+**Tab**

Change the Date to the 18 Aug 2018 and change the Revenue on Tuesday to 3000

Return to Excel by Using **Alt**+**Tab**

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW14.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW14.png)

Notice that the Date, Tuesday Revenue and Unit Revenue have all changed to reflect the changes in the excel Document.

You can reformat the Table in Word and only the numbers and text will change in response to changes in the Excel Document

The Excel and Word Files must be open for the link to be updated dynamically.

If the Excel file is closed the Word file will not update.

**When to use this technique**

This is a great technique when you have a large data source with mutiple tables used in Word, Like a Monthly Report.

But there is an alternative…

Perform the Maths in Word
-------------------------

Microsoft Word has limited arithmetic abilities built in.

These abilities only apply to data stored in Tables, not to data stored in tabular format within normal text

Open a word file and enter a Table of Data like below

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW20.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW20.png)

This is the same table we have seen before.

It requires a Total Line as well as Unit Revenue calculations

Click into the Sales Quantity Weekly Totals cell.

Now goto the Layout Tab and select the Formula icon.

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW21.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW21.png)

In the Formula: dialog Word will have inserted a Formula **=SUM(ABOVE)**

This is what we want to do, so leave it

Select an appropriate Number format from the Number format drop down. These number formats are in the same style as Excel Custom Number Formats.

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW22.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW22.png)

Click **OK**

Word puts the total **750** in this case in the Total cell

Change a Number above and watch as the Total changes

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW23.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW23.png)

Repeat the previous step in the revenue Weekly Total cell

The Unit Revenue will be the Revenue for each day divided by the Sales Quantity that day.

That is, for Monday, we want to divide the Sales Revenue of $2,000 by the Sales Quantity 100 to return a Unit Revenue of 200

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW33.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW33.png)

Luckily Word has the facility to treat Cells in a Table in a similar fashion to **Excel !**

We can use either **R1C1** or **A1** formula formats.

In **R1C1** each column and row is simply numbered as shown below

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW25.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW25.png)

In **A1** each column is Labelled alphabetically as in the default view in Excel and row is numbered as shown below

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW26.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW26.png)

And Word is actually more advanced than Excel as you can use either format at the same time without having to change the format in settings.

In our example we want to divide the Cell in Row 2 Column 3 (**R2C3**) by the value in Row 2 Column 2 (**R2C2**)

Click in the Cell under the **Unit Revenue** column header in Row **2**

Goto the Layout Tab and select the Formula icon

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW36.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW36.png)

By default Word will display a **\=SUM(LEFT)** formula

Overwrite this with your own formula **\=R2C3/R2C2**

Select an appropriate Number format and press **OK**

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW28.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW28.png)

You can use the **A1** formula style by simply using it

Click in the Cell under the **Unit Revenue** column header in Row **2**

Goto the Layout Tab and select the Formula icon

By default Word will display a **=SUM(LEFT)** formula

Overwrite this with your own formula **\=C2/B2**

Select an appropriate Number format and press **OK**

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW27.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW27.png)

Repeat this for the other cells in the **Unit Revenue** column.

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW32.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW32.png)

Voila !

You now have a Table in Word, the Total and Unit Rates are Formulas.

But wait there is a mistake, The Revenue on Tuesday should be $5,000

Select the cell and change the value to 5,000

Depending on which version of Word you have the Table will either Update Automatically or you can force it to recalculate

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW31b.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW31b.png)

If you Change the Value and the Table updates itself, Enjoy it

If your Table hasn’t updated itself you have a few options

Select the cells by Left Click and Drag ie: From 5,000 Down to the base of the table and across to the Right

Now Right click the selection and select **Update** or press **F9**

You can also click on an individual cell within the Table and Right Click and **Update**

Or you can press **Ctrl+A** outside the Table and Right Click and **Update** or Press **F9**

### What Other Functions are Available?

We saw in the example above that we can use basic operands of **+**, **–**, **\*** and **/**

We used the function Sum()

But there are about a dozen other functions available to us to construct formula to process our data

To see and use these Goto the **Layout** Tab and select the Paste function dropdown on the Formula Dialog.

[![](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW31.png)](https://chandoo.org/wp/wp-content/uploads/2018/08/MIW31.png)

Scroll down to see other functions

You can build up a function as you do in Excel using parenthesis and these functions.

In the example above we used the special **Above** range to specify that we wanted to **Sum** the values **Above** the active cell.

You can also use the **LEFT**, **RIGHT**, **ABOVE**, **BELOW** positional arguments

If you have defined Bookmarks within the Word document you can also use these to return values

**\=ROUND(NPV,0)**

Where NPV is a Bookmark to the value of the NPV elsewhere in your Document.

Further Help
------------

Word has a good discussion on the techniques available in the online help

[Microsoft Word – Formula in a cell help](https://support.office.com/en-us/article/use-a-formula-in-a-word-or-outlook-table-cbd0596e-ea8a-485e-a35d-b2cb2c4f3e27?NS=WINWORD&Version=16&SysLcid=1033&UiLcid=1033&AppVer=ZWD160&HelpId=225&ui=en-US&rs=en-US&ad=US)

Final Comments
--------------

How have you performed maths on data in Word?

Let us know in the comments below:

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [No Comments](https://chandoo.org/wp/performing-maths-in-microsoft-word-in-an-excel-blog/#respond)
    
*   [Ask a question or say something...](https://chandoo.org/wp/performing-maths-in-microsoft-word-in-an-excel-blog/#respond)
    
*   Tagged under [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [maths](https://chandoo.org/wp/tag/maths/)
    , [Word](https://chandoo.org/wp/tag/word/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [Word](https://chandoo.org/wp/category/word/)
    

[PrevPreviousWhat is Power BI, Power Query and Power Pivot?](https://chandoo.org/wp/what-is-power-bi-power-query-and-power-pivot/)

[NextWhen is the next Monday? \[Homework\]Next](https://chandoo.org/wp/next-monday-excel-formula/)

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
    
    [Reply](https://chandoo.org/wp/performing-maths-in-microsoft-word-in-an-excel-blog/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/performing-maths-in-microsoft-word-in-an-excel-blog/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/performing-maths-in-microsoft-word-in-an-excel-blog/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ