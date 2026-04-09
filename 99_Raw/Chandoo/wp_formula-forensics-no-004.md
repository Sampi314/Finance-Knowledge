# Simplifying a very long formula using Sumproduct

**Source:** https://chandoo.org/wp/formula-forensics-no-004

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

Formula Forensics No.004 – Fred’s Problem
=========================================

*   Last updated on January 10, 2012

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

About 6 months ago, Fred asked a question on the Chandoo.org Forums: [I need idea on a simpler formula](http://chandoo.org/forums/topic/i-need-idea-on-a-simpler-formula "Fred's Problem")

_In column A I have the total sum product of C to AU  
Line one has all the names.  
A2 = (B2\*C2)+(D2\*E2)+(F2\*G2)+(H2\*I2)+(J2\*K2)+(L2\*M2)+…+(AT2\*AU2)  
A3 = (B3\*C3)+(D3\*E3)+(F3\*G3)+…+(AT3\*AU3)_

_Is there is simpler way by line to do this without clicking each cell on line 2?_

_I tried Sumproduct but I think I have received a wrong answer during testing._

[Hui](http://chandoo.org/wp/about-hui/ "About Hui")
 offered a Sumproduct Formula as a solution

\=SUMPRODUCT((B2:AT2) \* MOD(COLUMN(B2:AT2) -1, 2), (C2:AU2) \* MOD(COLUMN(C2:AU2), 2))

and then followed up with a simpler Sumproduct Formula a day later

\=SUMPRODUCT(B2:AT2 \* C2:AU2 \* (MOD(COLUMN(B2:AT2), 2) =0))

Let’s take a look at this second solution.

**Setup the Problem**
---------------------

Copy the numbers 10,20 into alternate Cells **A2:U2** or download the example file here: [Example File](https://chandoo.org/wp/wp-content/uploads/2011/11/Freds-Formula.xls "Fred's Problem Example File")
 (Excel 97-2010)

Copy this formula into **B6**: \=SUMPRODUCT(B2:U2 \* C2:V2 \* (MOD(COLUMN(B2:U2), 2)=0))

  

**Pull The Formula Apart**
--------------------------

Lets take a look inside this formula and see how it works.

\=SUMPRODUCT(B2:U2\*C2:V2\*(MOD(COLUMN(B2:U2),2)=0))

We can see that in the above formula the main function used in the formula is a Sumproduct Function.

\=SUMPRODUCT(B2:U2\*C2:V2\*(MOD(COLUMN(B2:U2),2)=0))

Within the Sumproduct function there are 3 arrays, which are multiplied together

**Array 1**: B2:U2

**Array 2**: C2:V2

**Array 3**: (MOD(COLUMN(B2:U2),2)=0)

What’s in these arrays?

**Array 1** is simply the range from B2:U2

**Array 2** is simply the range from C2:V2, note that it is offset from the first array by 1 Column.

This is so that the first value of the Second Array matches the first value of the First Array. That is they are both in position 1 within there respective arrays.

**Array 3** is where all the action is.

Enter  \=(MOD(COLUMN(B2:U2),2)=0) into a cell and press **F9**

Excel returns: ={TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE}

Lets look at what is happening here

\=(MOD(COLUMN(B2:U2),2)\=0)

Mod returns the remainder of the first value Column(B2:U2) after dividing it by the second value 2.

Column(B2:U2) returns the Column Number for each cell in the Range B2:U2.

Because this part of the formula is in a Sumproduct formula it is evaluated as an Array Formula and hence it does this for each cell in the range B2:U2, thus returning an Array as the answer.

We can see that if we enter \=MOD(COLUMN(B2:U2),2) into a cell and evaluate it with **F9**

\={0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1}

However in this case we want to convert this from an array of Numbers to an array of True/False

A simple addition of an =0 does the trick

\=(MOD(COLUMN(B2:U2),2)\=0)

Now causes the formula to return: \={TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE}

So How does this go together with the other 2 arrays?

We now have 3 arrays:

**Array 1**:  10,20,10,20,10,20,10,20,10,20,10,20,10,20,10,20,10,20,10

**Array 2**:  20,10,20,10,20,10,20,10,20,10,20,10,20,10,20,10,20,10,20

**Array 3**: TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE

When Multiplying arrays, Excel multiplies the first value of each array and then the second value of each array, etc, effectively doing

\={10\*20\*True, 20\*10\*False , 10\*20\*True, 20\*10\*False , 10\*20\*True, 20\*10\*False , 10\*20\*True, 20\*10\*False , 10\*20\*True, 20\*10\*False , 10\*20\*True, 20\*10\*False , 10\*20\*True, 20\*10\*False , 10\*20\*True, 20\*10\*False , 10\*20\*True, 20\*10\*False , 10\*20\*True}

You can see above that when the 3 arrays are multiplied it will only be the Odd entries in Arrays 1 & 2 which are evaluated by the Sumproduct, as all the even entries are multiplied by False which is equivalent to Zero

So the above evaluates to

\={200,0, 200,0, 200,0, 200,0, 200,0, 200,0, 200,0, 200,0, 200,0, 200}

Sumproduct then takes over and adds the values together returning, **2000**, the correct answer.

### **Problem Extension**

After solving the problem, Fred decided to add a column between each entry in the data set.

The solution is posted in the forum and is also shown in the example file.

You can work through that formula at your leisure, except to say that it is similar to the solution above.

### **Alternate Solution**

Luke correctly pointed out that the data was poorly arranged and the solution would be much simpler had the data been more logically arranged.

However as an Excel practioner we are often called to solve other peoples dirty work.

**HINTS**
---------

You will notice that in the solution of this problem I have done a few small things that make solving the problem easier.

### **Use Smaller Subsets of the Data.**

Instead of putting numbers from Columns B to AU as Fred has I have used a set from Column B to U.

This way I can see all the data on one Excel screen without scrolling as well as the formula links and extents when pressing F2 on the cell containing the formula.

### **Use Simple Numbers**

Use numbers that you can manually check. In this example I can easily, manually, check that the answer should be 2000.

### **Evaluate**

Where ever possible, enter sections of a formula in a cell and evaluate its output:

\=(MOD(COLUMN(B2:U2),2)=0) and press F9

\={TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE,TRUE,FALSE}

See how easily we can check that this section is returning the correct values.

**OTHER POSTS IN THIS SERIES:**
-------------------------------

You can learn more how to pull Excel Formulas apart in the following posts:

[http://chandoo.org/wp/category/formula-forensics/](http://chandoo.org/wp/category/formula-forensics/ "Formula Forensics")

The link above, will show you all the posts in this series

**WHAT FORMULAS WOULD YOU LIKE EXAMINED?**
------------------------------------------

If you have any formulas you would like explained please feel free to leave a post here or send me an email:

If the formula is already on Chandoo.org or Chandoo.org/Forums, simply send the link to the post and a Comment number if appropriate.

If sending emails please attach an Excel file with the formula and data

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [14 Comments](https://chandoo.org/wp/formula-forensics-no-004/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/formula-forensics-no-004/#respond)
    
*   Tagged under [column()](https://chandoo.org/wp/tag/column/)
    , [Formula Forensics](https://chandoo.org/wp/tag/formula-forensics/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [MOD()](https://chandoo.org/wp/tag/mod/)
    , [sumproduct](https://chandoo.org/wp/tag/sumproduct/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Formula Forensics](https://chandoo.org/wp/category/formula-forensics/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    

[PrevPreviousMaintenance Work Complete](https://chandoo.org/wp/maintenance-work-complete/)

[NextCongratulations Chandoo.org 1,000,000 Page HitsNext](https://chandoo.org/wp/congratulations-1000000-page-hits/)

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
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-004/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/formula-forensics-no-004/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/formula-forensics-no-004/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ