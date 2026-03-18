# Quickly Fill Blank Cells in a Table [Reader Tip] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/fill-blank-cells-in-a-table

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

Quickly Fill Blank Cells in a Table \[Reader Tip\]
==================================================

*   Last updated on October 17, 2011

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This post is authored by **Martin**, one of our readers._

### Situation:

Sometimes I encounter data in my tables with blank cells where there is a repeated value from the cell directly above. See below:

![Quickly Fill Blank Cells in a Table - Excel Tip](https://chandoo.org/img/q/fill-blank-cells-1.png)

This can be annoying when it comes to interpreting the data and when sorting columns.

### Solution:

Here’s the solution I use.

1\. Select the whole table. I favor the shortcut Ctrl A to do this. Make sure you perform this shortcut from within the table though as otherwise the entire worksheet with be selected. This gives us Figure 2:

![Select all the cells in a table using CTRL+A](https://img.chandoo.org/q/fill-blank-cells-2.png)

2\. Next we will open the Go To dialog box. This is a very useful dialog for selecting certain types of cells, for example cells containing formulas, constant values, visible cells and so on. F5 or Ctrl G both work as keyboard shortcuts.

3\. Click the Special button (see Figure 3)

![Use Goto Dialog box to select the blank cells](https://chandoo.org/img/q/fill-blank-cells-goto-dialog-3.png)

4\. In the next screen select Blanks.

![Select all blank cells](https://img.chandoo.org/q/select-blank-cells-4.png)

5\. Click OK and notice that all blank cells are now highlighted in the table (Figure 5). Notice too, the position of the active cell. This is the one un-shaded cell in this selection. In this example it is cell D3. If the table were fully complete this cell would show the same value as the cell above it – cell D2 – the word Office.

![All the blank cells are now selected](https://chandoo.org/img/q/fill-blank-cells-5.png)

6\. Next we will use the fact that cell references in Excel by default behave in a relative manner. That means when you copy a formula to another cell, the cell reference in the formula change relative to the location in the worksheet it has been moved to unless they have been made absolute.

7\. Without clicking any of the cells in the data, simply enter the following simple formula:

\=D2

If you are following along here with a different table, then you will substitute the cell reference of the cell directly above your active cell. (Figure 6)

![Use a formula to copy the value from above](https://chandoo.org/img/q/copy-value-from-above-formula-6.png)

8\. Next the important part. We need to copy this simple formula to all the other blank cells which could number in the hundreds or thousands or greater still. How do we do it?

Simply by using one of the best keyboard shortcuts I know in Excel: **Ctrl & Enter.**

This shortcut when used in a single cell will enter the value inputted into the cell and keep that cell active, instead of performing a carriage return to the next row.

But, when used over a range of cells, Ctrl & Enter together will copy the value of the active cell into all cells in the selection.

In this case, we are not going to copy the value of D2 into all blank cells, but the relative cell that appears over each blank cell. In cell D3’s case this was D2. In A3’s case for example it is A2 and so on.

**After CTRL Entering the formula the worksheet now looks like:**

![After typing the formula, this is how the table looks like](https://chandoo.org/img/q/fill-blank-cells-7.png)

9\. There is one last important step. These pasted valued are, as we have seen, relative formulas. If I were to change the sort order in one of the columns, for example to identify which Cost in column E is the highest, my table would be completed distorted as the formulas in the changing rows are all retrieving the value in the cell above. See Figure 8.

![The formulas return incorrect values if the list is sorted differently](https://img.chandoo.org/q/fill-blank-cells-8.png)

I’ll Undo my flawed Sort by clicking Ctrl Z.

**The final step therefore is to change these formulas into constants** so that this type of problem can be avoided.

To do this, select the table, (or if the formula cells remain highlighted, you won’t need to select the table at all).

Now copy your selection with Ctrl C.

Next, perform a [Paste Special](https://chandoo.org/wp/fill-blank-cells-in-a-table/chandoo.org/wp/2008/07/02/17-excel-paste-special-tricks/)
 / Values to replace the formulas with their constant equivalents – Figure 9.

![Change formulas to values using Paste Special](https://chandoo.org/img/q/fill-blank-cells-9.png)

_**And that’s it!**_

### Thank you Martin

Many thanks to Martin for sharing this simple yet very beautiful trick with all of us. If you enjoyed this article, say thanks to Martin.

### How do you deal with Blank Cells

Barking dogs, bad bosses and blank cells are everywhere. I am eager to know how you deal with them. **Please share your tips & techniques with us using comments.**

### More on Blank Cells and other Unclean Data

If you constantly deal with blank cells or other types of unclean data, read these articles to learn few more tricks.

*   [Delete Blank Rows in Excel Tables](http://chandoo.org/wp/2010/01/26/delete-blank-rows-excel/)
    
*   [Removing Blank Items in a range of cells](http://chandoo.org/wp/2010/02/23/find-and-remove-blank-cells/)
    
*   [Cleaning up Dates in Excel](http://chandoo.org/wp/2010/03/23/text-to-date-convertion/)
    
*   [Merge Several Cells without Loosing Data](http://chandoo.org/wp/2010/12/07/merge-cells-without-loosing-data/)
     \[macros\]

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [55 Comments](https://chandoo.org/wp/fill-blank-cells-in-a-table/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/fill-blank-cells-in-a-table/#respond)
    
*   Tagged under [blank rows](https://chandoo.org/wp/tag/blank-rows/)
    , [cleanup data](https://chandoo.org/wp/tag/cleanup-data/)
    , [goto special](https://chandoo.org/wp/tag/goto-special/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [paste-special](https://chandoo.org/wp/tag/paste-special/)
    , [quick tip](https://chandoo.org/wp/tag/quick-tip/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    

[PrevPreviousCommercial Aspects of Project Management](https://chandoo.org/wp/commercial-aspects-of-project-management/)

[NextSplit an Excel File in to Many using VBA \[Videos\]Next](https://chandoo.org/wp/split-excel-file-into-many/)

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
    
    [Reply](https://chandoo.org/wp/fill-blank-cells-in-a-table/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/fill-blank-cells-in-a-table/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/fill-blank-cells-in-a-table/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ