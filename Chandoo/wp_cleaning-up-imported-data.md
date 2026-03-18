# Cleaning Up Imported Data - A Brief Case Study

**Source:** https://chandoo.org/wp/cleaning-up-imported-data

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Cleaning Up Imported Data – A Recent Case Study
===============================================

*   Last updated on January 24, 2012

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Yesterday in Formula [Forensics 008](http://chandoo.org/wp/2012/01/24/formula-forensics-no-008/ "Formula Forensic No 8.")
 we looked at Elkhans **MaxIf** problem.

However the solution/formula as presented is the final solution to his problem.

Elkhans original worksheet contained other problems and today we will look at this:

I have attached the orginal file as a sample file you can [Download Here](https://chandoo.org/wp/wp-content/uploads/2012/01/Elkhan-Maxif-Original.xls "Original File")
.

You will see that the **MaxIf** cell **F13** is returning **0**, where it should be showing **0.246**

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD001.png "CUD001")](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD001.png)

Houston, We’ve Had a Problem!
-----------------------------

Cell **F13** has the same formula we looked at in yesterday’s Formula Forensics: \=MAX(IF((Parameter\_3=D13)\*(Parameter\_4=E13),Parameter\_5,0))

A quick check of the formula reveals that everything was technically right with the formula, yet the answer is wrong?

To solve this I tried several steps which is the topic of this post:

### **Examine the logic of the If’s Criteria**

The formula \=MAX(IF((Parameter\_3=D13)\*(Parameter\_4=E13),Parameter\_5,0)) works by calculating the maximum value from the If array.

So step 1 was to look at the logic in the If’s Criteria

That is (Parameter\_3=D13)\*(Parameter\_4=E13)

In cell **F15** I entered \= (Parameter\_3=D13)\*(Parameter\_4=E13) followed by **F9**

Excel returns: \= {0;0;0;0;0;0;0;0;0;0;0}

This tells me that none of the Cells match the criteria, strange?

Yet manually I can see 4 matching records, below:

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD002.png "CUD002")](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD002.png)

### **Check Cell Length**

The next quick step was to look at the length of the text in each cell.

In Column I, I added a \=Len(E2) and copied down, there was only 2 characters in each cell, this step eliminated leading or trailing spaces.

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD003.png "CUD003")](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD003.png)

### **Retype the Data**

Elkham supplied the source data in an Excel file.

But the Criteria was manually typed by me.

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD004.png "CUD004")](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD004.png)

So the next step was to retype some of the original data in Cell E2

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD005.png "CUD005")](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD005.png)

Wow an Answer, So obviously there was a difference?

What is Wrong Here?
-------------------

So obviously there was a difference between the C1 in cell E2 and the C1 in cell E13?

I checked this in 3 ways

### 1\. Type the value “C1” into Cell **E2**, without the quotes

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD005.png "CUD005")](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD005.png)

This returned an answer **0.08** from **F2** as it should have.

### 2\. Copy an old “C1” value to E13

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD006.png "CUD006")](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD006.png)

This resulted in the correct answer of **0.246** in **F13**

### 3\. Use a quick Formula

Entering a quick formula

In **F17** type \=E2=E13

Excel returns **False**

Showing that the value of cell E2 does not match E13

**So what is in E2:E12 ?**
--------------------------

As I had typed the values into the Criteria Cells D13:E13, I knew what they were, they were a plain and simple “C1”

So what was in E2:E12 ?

Next step was to look at the Ascii values of the 2 characters in Column E.

In **K2**: \=Code(Left(E2,1))

In **L2**: \=Code(Right(E2,1))

Copy both down to Row 13

[![](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD007.png "CUD007")](https://chandoo.org/wp/wp-content/uploads/2012/01/CUD007.png)

**Bingo !**

The Character **C** in cell E2 wasn’t the same as the Character **C** in E13 ?

Yet both cells contained a Calibri Font.

If I now type in a spare cells:

**F18** \=Char(63), Excel displays a “**?**”

**F19** \=Char(67), Excel displays a “**C**”

Yet Cell E2 is clearly displaying C1 with a First Character Ascii code of 63 which should be a **?** mark.

I suspected that it had been copied and pasted from MS Access, So I shot an email back to Elkhan, asking “What the source of the data was?”.

The response came back that “_The data had been copied from a Russian (Cyrillic) version of an MS Word File and pasted into an English version of Excel._”

I can’t explain what has happened but somehow the character sets and associated values got scrambled when copied the data from the Russian Word Document into Excel

If you have had experiences like this or can explain what has happened please do so in  the comments below:

Solution
--------

The Solution was now easy

**Use Search/Replace**

Copy the contents of cell E1,

goto Search/Replace or **Ctrl H**

Find: Paste the contents of Cell E1

Replace with: C1

**Conclusions:**
----------------

1.  Be careful when receiving data from foreign language files, including word and Excel files
2.  Check summations based on such data to ensure its integrity
3.  Be methodical in tracking down problem cells

Lets us know about your Data Transfer Nightmares
------------------------------------------------

Have you had any strange data transfer issues?

Let us know in the comments below.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [31 Comments](https://chandoo.org/wp/cleaning-up-imported-data/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/cleaning-up-imported-data/#respond)
    
*   Tagged under [char()](https://chandoo.org/wp/tag/char/)
    , [code](https://chandoo.org/wp/tag/code/)
    , [if()](https://chandoo.org/wp/tag/if/)
    , [left()](https://chandoo.org/wp/tag/left/)
    , [len()](https://chandoo.org/wp/tag/len/)
    , [max()](https://chandoo.org/wp/tag/max/)
    , [right()](https://chandoo.org/wp/tag/right/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousFormula Forensics No. 008 – Elkhan’s MaxIf](https://chandoo.org/wp/formula-forensics-no-008/)

[NextExcel Links – Live from Bangkok EditionNext](https://chandoo.org/wp/excel-links-live-from-bangkok-edition/)

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
    
    [Reply](https://chandoo.org/wp/cleaning-up-imported-data/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/cleaning-up-imported-data/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/cleaning-up-imported-data/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ