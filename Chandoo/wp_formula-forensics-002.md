# How to Count the Number of words in a multi-word Range

**Source:** https://chandoo.org/wp/formula-forensics-002

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Formula Forensics No. 002 – Joyces Question
===========================================

*   Last updated on December 9, 2011

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

Last week Joyce asked a question on the [Chandoo.org](http://chandoo.org/wp/2011/10/31/using-array-formulas-to-find-count/#comment-211706 "Joyces problem")
, Comment 24.

_I’m wondering if there’s a way to count the number of occurrences of words when they’re all in a cell? Like this:  
A1: “Windows NT, Networking, Firewalls, Security, TL, Training”  
A2: “Networking, Networking, Training, Security, TL, Training”  
A3: “Security, TL, Firewalls, Security, Networking, Windows NT”_

_Joyce  
_

[Hui](http://chandoo.org/wp/about-hui/ "About Hui")
 responded with an Array Formula:

\=SUM(LEN(A1:A3)-LEN(SUBSTITUTE(A1:A3,C10,””)))/LEN(C10)

As the formula is an Array Formula it is entered with **Ctrl Shift Enter.**

### **Setup the Problem**

Copy the Data Above into Cells A1:A3 or download the example file here: [Example File](https://chandoo.org/wp/wp-content/uploads/2011/11/Joyce.xls "Joyces Sample File")
 (all Excel versions)

Enter the text string **Security** into cell C10

And array enter the formula

**D10:** \=SUM(LEN(A1:A3)-LEN(SUBSTITUTE(A1:A3,C10,””)))/LEN(C10)

Cell **D10** should now display the value **4**, which is the number of times the Word **Security**, appears in the Range **A1:A3.**

### **Pull The Formula Apart**

Lets take a look inside this and see how it works

We will break this formula apart and look at each section independently and then put the answers back together.

\=SUM(LEN(A1:A3)\-LEN(SUBSTITUTE(A1:A3,C10,””)))/LEN(C10)

In a cell below the data

**D13:** \=LEN(A1:A3) but **don’t** press Enter, Press F9

Excel displays ={57,56,57}

This is the number of characters in each cell A1:A3

ie: A1 has 57 characters, A2 has 56 characters, A3 has 57 characters,

You can check this manually by typing =Len(A1) into any spare cell

\=SUM(LEN(A1:A3)-LEN(SUBSTITUTE(A1:A3,C10,””)))/LEN(C10)

In another cell below the data

**D15:** \=LEN(SUBSTITUTE(A1:A3,C10,””)) but **don’t** press Enter, Press F9

Excel displays ={49,48,41}

What this section does is measure the length of each cell in A1:A3 but only after substituting the word being searched for from C10 with ””, which is a zero length string.

So the second array is shorter than the first Array, by X times the length of the word in C10

\=SUM(LEN(A1:A3) – LEN(SUBSTITUTE(A1:A3,C10,””)))/LEN(C10)

Next we add up the difference between the two arrays

So you can see we have two arrays of numbers

Array 1 = {57,56,57}

Array 2 = {49,48,41}

If we subtract Array 2 from Array 1

\= {57-49, 56-48, 57-41}

\= {8, 8, 16}

We can do this in Excel to Check

In Cell D17 enter

\=LEN(A1:A3)-LEN(SUBSTITUTE(A1:A3,C10,””)) and press F9

Excel displays: = {8, 8, 16}

\=SUM(LEN(A1:A3) – LEN(SUBSTITUTE(A1:A3,C10,””)))/LEN(C10)

The next part is to sum these up

Obviously the sum of 8, 8 & 16 is 32

We can check that

**D21:** \=SUM(LEN(A1:A3)-LEN(SUBSTITUTE(A1:A3,C10,””))) and press **F9**

Excel displays: 32

\=SUM(LEN(A1:A3) – LEN(SUBSTITUTE(A1:A3,C10,””)))/LEN(C10)

The final part of this is to divide the sum (32 in this case) by the length of the text in C10 “Security” = 8 Characters

\=**32 / 8**

\= **4**

**Correct** – The number of times **Security** appears in the cells **A1:A3** is **4**.

**OTHER POSTS IN THIS SERIES:**
-------------------------------

You can learn more about how to pull Excel Formulas apart in the following posts

[Formula Forensic 001](http://chandoo.org/wp/2011/10/31/using-array-formulas-to-find-count/ "Taruns problem")
 – Tarun’s Problem

**WHAT FORMULAS WOULD YOU LIKE EXAMINED ?  
**
----------------------------------------------

If you have any formulas you would like explained please feel free to leave a post here or send me an email:

If the formula is already on Chandoo.org or Chandoo.org/Forums or even forbid another web site, simply send the link to the post and a Comment or ID No. number if appropriate.

If sending emails please attach an Excel file with the formula and data

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [20 Comments](https://chandoo.org/wp/formula-forensics-002/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/formula-forensics-002/#respond)
    
*   Tagged under [Array Formula](https://chandoo.org/wp/tag/array-formula/)
    , [len()](https://chandoo.org/wp/tag/len/)
    , [substitute()](https://chandoo.org/wp/tag/substitute/)
    , [sum()](https://chandoo.org/wp/tag/sum/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousFancy Posts – using HTML Display Codes in Chandoo.org Posts](https://chandoo.org/wp/fancy-posts-using-html-display-codes/)

[NextExcel for Project Managers is coming up next Monday (14th), Details Inside…Next](https://chandoo.org/wp/excel-for-project-managers-details/)

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
    
    [Reply](https://chandoo.org/wp/formula-forensics-002/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/formula-forensics-002/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/formula-forensics-002/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ