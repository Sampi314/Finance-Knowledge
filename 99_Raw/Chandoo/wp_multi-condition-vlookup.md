# The ultimate VLOOKUP trick - Multi-condition Lookup » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/multi-condition-vlookup

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

The ultimate VLOOKUP trick – Multi-condition Lookup
===================================================

*   Last updated on October 29, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is a guest post by Sohail Anwar._

Let’s not bore you with an intro. You are about to learn a [VLOOKUP](http://chandoo.org/wp/2010/11/01/vlookup-excel-formula/)
 trick that Lucifer himself would not want you to know. It’s so absurdly powerful that it was developed in a lab and had to be tested on Rocky’s arch nemesis Ivan Drago.

![VLOOKUP Trick for Multi-condition lookups](https://img.chandoo.org/f/vw/vlookup-multi-condition-trick-01.jpg)

Presenting the Multiple criteria VLOOKUP!

…boring…pass, we’ve seen it.

Oh, have you? Not like this you haven’t. This will change the way you work with Excel.

Let me start with an easy example. Here’s some data and we would love to know what Bb and Dd is.

![Example data - Multi criteria lookup in Excel](https://img.chandoo.org/f/vw/vlookup-multi-condition-trick-02.png)

Easy. Let’s put a helper column in that concatenates the two inputs and do a basic VLOOKUP.

![Multi-condition lookup using helper columns](https://img.chandoo.org/f/vw/vlookup-multi-condition-trick-03.png)

_**Puh-lease. How boring.**_

### Bye Bye Helper Column, it was nice while it lasted.

With a dash of CHOOSE and sprinkling of Array formulas, we’re about to change the game:

`=VLOOKUP($E2,CHOOSE({1,2},$A$2:$A$7&$B$2:$B$7,$C$2:$C$7),2,0)` and press Ctrl + Shift + Enter

![Multi-conditional VLOOKUP with CHOOSE - Explained](https://img.chandoo.org/f/vw/vlookup-multi-condition-trick-04.png)

Without getting into too many details, using the Array creates a makeshift virtual helper column. You don’t have to understand Array formulas to make them work for you. I will lay out the simple structure that you can replicate

`VLOOKUP(lookup value, CHOOSE({1,2,...N},Column1 & Column 2 &…& Column N, Result Column),2,0)`

Where the lookup value is either something pre-concatenated (like Bb or Dd above) or you are using multiple criteria that you concatenate when entering the lookup value. The CHOOSE structure is easy. Always {1,2} then concatenate (with &) as many columns as you want (that the lookup values will need to look in) and the VLOOKUP’s column number is always 2. Let’s explore another example:

![Multi-condition vlookup - another example](https://img.chandoo.org/f/vw/vlookup-multi-condition-trick-05.png)

Let’s say we want to look up the Savings Produced for a Director of Grade D who started in 2014. That’s 3 lookup criteria. Let’s follow the structure.

`=VLOOKUP(A13&A14&A15,CHOOSE({1,2},A2:A10&B2:B10&C2:C10,D2:D10),2,0)` and press Ctrl + Shift + Enter

The two key things to note is that our lookup value is a concatenation of the criteria, in this case I have put the criteria in A13, A14 and A15 (hence A13&A14&A15 is our lookup value). Secondly, in the CHOOSE formula, the ranges in the middle part (A2:A10&B2:B10&C2:C10) have to be concatenated in the same order that the lookup value was concatenated. So we concatenated:

Start Year & Grade & Role

In both the lookup value and lookup columns within the CHOOSE.

I stumbled on this many years ago at work and it is the easiest way to do multiple criteria lookups. Play around and add more criteria…but that’s just the beginning!

### When I get that feeling, it’s like Textual Healing

So how can we take this concept and make it even more useful?

First, let me share my story of pain and anguish.

Often when dealing with volumes of text data I make numerous helper columns to deal with the multitude of ways I am presented with names. Anyone who’s reconciled HR data to Finance data for example can appreciate that pain. Finance write their names First Name (column 1) Surname (column 2), then HR provide a spread with Last Name, Surname (column 1), then all of a sudden the Project team join in the fun with First Name, Surname (column 1)! Arrghh!

So I am now left to deal with this chaos via numerous text formulas involving SEARCH, LEFT, RIGHT, MID, LEN and MYSANITY (okay perhaps that last one is my own UDF, my volatile UDF). So, maybe it’s not that bad, but when you’ve been doing it for as long as I have, it gets tedious and you begin to search for efficiency. So, one day like the rebellious closing scene from Dead Poet’s society, I stood on my desk and declared ‘Oh Captain, My Captain’ as I refused to create another ‘helper’ column.

![No more inconsistent data - using multi-condition lookups to handle inconsistent data](https://img.chandoo.org/f/vw/vlookup-multi-condition-trick-06.jpg)

After my colleagues talked me down from the table and reassured me (“There there Sohail, I don’t mind inserting new columns for you occasionally”…”Sure you don’t John, sure you don’t”), I went about finding a less ‘helpful’ way. Would you believe, our new friend the multiple criteria lookup was the answer.

You see, not only can our criteria be cell references but also extra characters! Let’s say we have First Name(Column A), Surname (Column B) and Unique Reference (Column C). Someone gives us a spreadsheet with the names in either a First Name + Surname or Surname, First Name format. We can look this up by including the extra characters in our lookup columns within the CHOOSE.

![Handling inconsistent data with multi-condition array lookup formulas](https://img.chandoo.org/f/vw/vlookup-multi-condition-trick-07.png)

Look closely at the middle of the CHOOSE since that’s where the magic is. Download the workbook to see the example in action.

![Multi-condition array lookup formula in action](https://img.chandoo.org/f/vw/vlookup-multi-condition-trick-08.png)

We have pretty much instructed the two columns we are looking up to join up in a specific way. First we want them to join up with a space in between. Then the second formula has asked them to join up Surname, comma and space in between, then finally the First Name. So as far as Excel is concerned we have created two virtual helper columns that look like this:

![How virtual helper columns work - Multi-condition lookup formula](https://img.chandoo.org/f/vw/vlookup-multi-condition-trick-09.png)

This makes it straightforward for us to look up John Johnson or Johnson, John in them.

**There are virtually no bounds to how you can use this Multiple Criteria VLOOKUP.** It made my life tremendously easy and I’m sure it makes yours easier too. **Do me a favor and let me know in the comments some of the crazy ways you are applying it.**

And then if you haven’t already grabbed a copy of Chandoo’s [VLOOKUP book](http://chandoo.org/wp/resources/the-vlookup-book/)
 I cannot recommend it enough as the ultimate resource in VLOOKUP mastery

### Download Example Workbook

[**Click here to download the example workbook**](https://img.chandoo.org/f/vw/Ultimate%20VLOOKUP%20trick.xls)
 prepared by Sohail. Play with it to learn more.

Added by Chandoo
----------------

### Thank you Sohail

Thank you Sohail for writing this very useful, incredibly fun tutorial. I am sure our readers will enjoy it as much as I do. Thanks.

_If you like this, please say thanks to Sohail._

### Related discussion on Multi-conditional lookups

As you can guess, this is not the first time we talked about using multiple conditions in VLOOKUP. Check out below articles for more ideas & tips:

*   [Multi-condition lookup using Excel](http://chandoo.org/wp/2010/11/02/multi-condition-lookup/)
    
*   [Using CHOOSE formula to make VLOOKUP go left](http://chandoo.org/wp/2012/09/06/formula-forensics-no-028/)
    
*   Introduction to [SUMIFS](http://chandoo.org/wp/2010/04/20/introduction-to-excel-sumifs-formula/)
     & [CHOOSE](http://chandoo.org/wp/2014/07/16/introduction-to-choose-function/)
     formulas

_**About the author: Sohail Anwar** is a Londoner who has spent over 10,000 hours applying Excel in his professional life and earns well over 6 figures as a result. Now he’s on a mission to teach professionals how to massively increase their earnings by learning and applying Excel like never before. Find out more about Sohail on [Earn With Excel](http://earnwithexcel.com/)
 or  [LinkedIn](http://uk.linkedin.com/pub/sohail-anwar/75/b46/a46)
_

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [173 Comments](https://chandoo.org/wp/multi-condition-vlookup/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/multi-condition-vlookup/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [choose()](https://chandoo.org/wp/tag/choose/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [sumifs](https://chandoo.org/wp/tag/sumifs/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousBack after a while & 3 announcements](https://chandoo.org/wp/back-after-a-while-3-announcements/)

[NextCP024: Customize Excel to boost your productivityNext](https://chandoo.org/wp/cp024-customize-excel-to-boost-your-productivity/)

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
    
    [Reply](https://chandoo.org/wp/multi-condition-vlookup/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/multi-condition-vlookup/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/multi-condition-vlookup/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ