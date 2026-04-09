# How to lookup and extract multiple occurrences using Excel VLOOKUP & other formulas

**Source:** https://chandoo.org/wp/multiple-occurrences-lookup-and-extraction

---

*   [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Excel to the Next Level by Mastering Multiple Occurrences
=========================================================

*   Last updated on December 9, 2014

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is a guest post by **Sohail Anwar**._

**August 29, 1994**. A day that changed my life forever. Football World Cup? Russia and China de-targeting nuclear weapons against each other? Anniversary of the Woodstock festival?

No, much bigger: Two Undertakers show up at WWE Summerslam for an epic battle. Needless to say: MIND() = BLOWN().

![Excel to next level by mastering multiple occurrences - Pic1](https://img.chandoo.org/g/MO1.jpg)

And thus begun one boy’s journey into understanding the **phenomenon of Multiple Occurrences**.

My journey continued, when just a few years later my grandfather handed me down a precious family heirloom: A few columns of meaningless data that I could take away and analyze in Excel. You may laugh but in the 90’s, every boy only wanted two things 1) Lists of pointless data and 2) To be as bad ass as this guy:

![Excel to next level by mastering multiple occurrences - Pic2](https://img.chandoo.org/g/MO2.jpg)

Ohhh yeah.

All good but how best to deal with multiple occurrences? Well, it broadly involves a cunning collusion of **SMALL, LARGE, IF** and our good friend the Array formula. To explain, let’s have a look at one of granddad’s prized pointless lists:

![Excel to next level by mastering multiple occurrences - Pic3](https://img.chandoo.org/g/MO3.png)

All kinds of repetition of names exist here, so how, for example, can we look up the pointless things about ‘Das Hoff’?

![Excel to next level by mastering multiple occurrences - Pic4](https://img.chandoo.org/g/MO4.jpg)

A typical VLOOKUP or INDEX/MATCH combo will give us the first entry (‘Talented’), but what about the rest? The following ARRAY formula will saves us:

`SMALL(IF(Lookup Range = Lookup Value, Row(Lookup Range),Row ()-# of rows below start row of Lookup Range)`

Entered with Ctrl + Shift + Enter because it’s an Array formula

In this case:

`SMALL(IF($A$1:$A$20=$E$2,ROW($A$1:$A$20)),ROW()-2)`

Bear in mind this will give us **the position numbers of the multiple occurrences** in our main list. That’s a good start. Now we drag this formula down so we end up with another list since our need to find multiple occurrences will necessitate creating another shorter subset of the main list, even if there are just two entries. How far do we drag it down? It doesn’t matter too much but enough to capture the likely number of multiple occurrences. we’ll come back to this point in a bit.

I just want to bring your attention to the last part of our SMALL formula, in this case ROW()-2. This creates a rank; think of it as 1st occurrence, 2nd occurrence…as you are dragging the formula down.

_**Why did I put Row()-2?**_ Well I placed it in a cell which is in the 3rd row and as a rule the first instance of the formula you write, you want the Row()-x to equal 1 (assuming your lookup range starts from row 1). So if your looukup range is in A1:D20 and your first SMALL formula is in cell E5 then you will write ROW()-4 at the end .

Let’s see what happens when we put the formula in E3, search for ‘Michael Bluth’ and drag down to E7:

![Excel to next level by mastering multiple occurrences - Pic5](https://img.chandoo.org/g/MO5.png)

We can visually see there are just two entries in the main list and their position numbers have come through nicely (4 and 7). Beyond that we are met with the #NUM! error. So from here, we need to do two things

1.  Utilize the position number to give us value or related value from the list (i.e. do what the lookup is supposed to do!)
2.  Conceal the errors.

To accomplish (1) we can just put this whole thing into an [INDEX formula](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/ "7 reasons why you should get cozy with INDEX()")
, define an array size (same vertical dimensions as our main table), use our SMALL formula to provide the row number, then define whatever column number we want, in this case we want column 2:  
`   INDEX($B$1:$B$20,SMALL(IF($A$1:$A$20=$E$2,ROW($A$1:$A$20)),ROW()-2),1)`

Which yields:

![Excel to next level by mastering multiple occurrences - Pic6](https://img.chandoo.org/g/MO6.png)

Now, the final bit involves wrapping all this in our trusted friend [IFERROR](http://chandoo.org/wp/2011/03/11/iferror-formula/ "IFERROR Excel Formula – What is it, syntax, examples and howto")
 for some easy tidying up:  
`   IFERROR(INDEX($B$1:$B$20,SMALL(IF($A$1:$A$20=$E$2,ROW($A$1:$A$20)),ROW()-2),1),"")`

![Excel to next level by mastering multiple occurrences - Pic7](https://img.chandoo.org/g/MO7.png)

Ta da! Let’s have a quick recap of how we evolved the formula.

![Comparison of multiple occurrence formulas in Excel](https://img.chandoo.org/g/comparison-of-multiple-occurrence-formulas-table.png)

### What else can we do?

Let’s extend this bad boy formula and make it really work for us. Here are some select ways I have extended the Multiple Occurrence formula to help extract from challenging text data.

[**Please download the workbook**](https://img.chandoo.org/g/Multiple%20Occurrences.xlsx)
, since it contains the examples for your learning pleasure.

Note: Temporarily for this next section, I am going to ignore the IFERROR and the INDEX parts purely to make the formula slighter shorter and thus a bit easier to read. Instead, what we will get are the position numbers (which are good enough to demonstrate how the formulas work). Relax, in the final section, I’ll bring them back in!

### Descending List

Okay, not very exciting, but if we wanted our list to be in a descending order, we simply switch the SMALL with LARGE!

`LARGE(IF($A$1:$A$20=$E$2,ROW($A$1:$A$20)),ROW()-2)`

![Excel to next level by mastering multiple occurrences - Pic8](https://img.chandoo.org/g/MO8.png)

### Partial Text Search

What if just want to look for part of the text? Easy!

`SMALL(IF(IFERROR(SEARCH($G$2,$A$1:$A$20)>0,FALSE),ROW($A$1:$A$20)),ROW()-2)`

![Excel to next level by mastering multiple occurrences - Pic9](https://img.chandoo.org/g/MO9.png)

The urge to use a wildcard just won’t work due to the mechanism of an Array. Arrays require like for like comparisons and a partial text won’t correspond to a range. So we need to create TRUE and FALSE outputs, which is what wrapping the SEARCH(…)>0 in an IFERROR does.

### Left side of Text

Let’s say we are looking for a first name in a cell with a full name, we can do:

`SMALL(IF(LEFT($A$1:$A$20,LEN($I$2))=$I$2,ROW($A$1:$A$20)),ROW()-2)`

![Excel to next level by mastering multiple occurrences - Pic10](https://img.chandoo.org/g/MO10.png)

Some of you are thinking, well this can be achieved with a partial text search and most of the time you are right. But I routinely deal with tens of thousands of rows of data with varying text and used to fall foul of not preparing for every permutation or combination. It’s subtle but it can be very useful.

### Partial text in the right side

‘Now you’re just being silly Sohail! Who needs this?’ I’ll stand by what I said, when you work with lots of data and need to extract all kinds of things, this sort of formula soon finds a place! Unfortunately I can’t reproduce data that I’ve worked with to show you the reality of needing something like this. It’s not often but once in a while it comes and it’s quicker then VBAing!

`SMALL(IF(IFERROR(SEARCH($K$2,RIGHT($A$1:$A$20,LEN($A$1:$A$20)-SEARCH(" ",$A$1:$A$20)))>0,FALSE),ROW($A$1:$A$20)),ROW()-2)`

![Excel to next level by mastering multiple occurrences - Pic11](https://img.chandoo.org/g/MO11.png)

So we’re just searching for things past the first space, this sort of thing would need to be extended as more spaces crop up but you get the point.

### Multiple Occurrences and Multiple Criteria!

What?! This is more confusing than making Time Traveling Flux Capacitors.

![Excel to next level by mastering multiple occurrences - Pic12](https://img.chandoo.org/g/MO12.jpg)

Okay, to make this work, let’s increase our data set, I’m going to throw in a region column for all the patriots in da house.

![Excel to next level by mastering multiple occurrences - Pic13](https://img.chandoo.org/g/MO13.png)

So now things are getting interesting. ‘Das Hoff’ is a great example; we can see from a visual inspection he covers two regions (discussing the dual German and US citizenship of the Hoff is out of the scope of this article, but just know how awesome he is!). How can we lookup the two different occurrences of ‘Das Hoff’?

Easy, but first if we harken back to [the ultimate VLOOKUP trick](http://chandoo.org/wp/2014/10/28/multi-condition-vlookup/)
 I suggested the use of CHOOSE in an array to create ‘virtual’ helper columns, the good news is since we are in an Array format, its pretty straightforward do this without messing with VLOOKUP or CHOOSE. So we simply concatenate the Person and Region ranges and we concatenate the Person and Region lookup cells:

`=SMALL(IF($A$1:$A$20&$B$1:$B$20=$E$2&$F$2,ROW($A$1:$A$20)),ROW()-2)`

So now if we look up ‘Das Hoff’ in ‘Germany’ and ‘US’ we get:

![Excel to next level by mastering multiple occurrences - Pic14](https://img.chandoo.org/g/MO14.png)

_Das ist gut, nein? Ja, Über gut._

Let’s go a step further; what if we wanted to separately lookup the First and Last names? Easy, same concatenation but also concatenate a space in between, like so:

`=SMALL(IF($A$1:$A$20=$K$2&" "&$L$2,ROW($A$1:$A$20)),ROW()-2)`

So if we are searching for the first name ‘Thom’ and surname ‘Morello’ we get:

![Excel to next level by mastering multiple occurrences - Pic15](https://img.chandoo.org/g/MO15.png)

There you have it. Multiple Occurrences WITH Multiple Lookups, take that to the bank!

### Autofiltering without an Autofilter!

So, now we have seen the power of what can be done with Multiple Occurrences, how else might we use this in our work? Well, in the Chandoo tradition of [creating awesome dashboards](http://chandoo.org/wp/2014/07/10/cp014-create-awesome-dashboards/)
 let’s build a bit of interactivity in a dashboard. Now I’m not going to build a dashboard, the web’s finest materials on dashboards can already be found on Chandoo.org! No point me recreating. What if we want to create a makeshift Autofilter in the middle of a dashboard/report? We can use everything we’ve learned about Multiple Occurrences and with a bit of conditional formatting we can cook up something pretty decent.

![Excel to next level by mastering multiple occurrences - Pic16](https://img.chandoo.org/g/MO16.jpg)

How about we poach the multiple criteria technique from the previous section: First Name, Surname and also Region as drop downs (by using simple [data validation lists](http://chandoo.org/wp/2008/08/07/excel-add-drop-down-list/ "Excel Basics: How to add drop down list to validate data")
) to control a table of formulas:

![Excel to next level by mastering multiple occurrences - Pic17](https://img.chandoo.org/g/MO17.png)

Let’s just look at the formula in each column of the table:

**Column 1: Person**

`IFERROR(INDEX($A$1:$C$20, SMALL(IF($A$1:$A$20&$B$1:$B$20=$F$3&" "&$F$4&$F$5, ROW($A$1:$A$20)),ROW()-2),1),"")`

**Column 2: Region**

`IFERROR(INDEX($A$1:$C$20, SMALL(IF($A$1:$A$20&$B$1:$B$20=$F$3&" "&$F$4&$F$5, ROW($A$1:$A$20)),ROW()-2),2),"")`

 **Column 3: Pointless Thing**

`IFERROR(INDEX($A$1:$C$20, SMALL(IF($A$1:$A$20&$B$1:$B$20=$F$3&" "&$F$4&$F$5, ROW($A$1:$A$20)),ROW()-2),3),"")`

The only difference between these is the Column number in the INDEX formulas. Now, I am fully aware of the absurdity of having your search criteria (Name and Region) appear in the results table but it’s cool, I’m just illustrating with minimal pointless made up data. Let’s try using this:

![Excel to next level by mastering multiple occurrences - Pic18](https://img.chandoo.org/g/MO18.png)

Selecting Thom, Yorke and UK gives us a nice chunky result. And how did we get it looking so slick with expanding/contracting borders and alternating colored rows?! Easy, let’s take a closer look at the conditional formatting:

![Excel to next level by mastering multiple occurrences - Pic19](https://img.chandoo.org/g/MO19.png)

Pay close attention to the order of the conditions, it won’t work properly otherwise. The formulas used are:

For the first condition, I have selected ‘No Color’ for fill:

![Excel to next level by mastering multiple occurrences - Pic20](https://img.chandoo.org/g/MO20.png)

For the second condition, the formula is:

`=NOT(MOD(ROW(),2))` – Choose a white fill AND complete Border around the cell.

For the last condition, the formula is:  
`   =AND(MOD(ROW(),2)=1,H3<>"")` – Choose a colored fill (I’ve gone with blue) AND complete Border around the cell.

The last thing is to **turn the grid-lines off** or at least paint the cells in and around the table white. Have a look in the workbook if it doesn’t make sense.

### Download Example Workbook

[**Click here to download Multiple Occurrences workbook**](https://img.chandoo.org/g/Multiple%20Occurrences.xlsx)
. It contains all the examples. Play with the formulas to learn more.

Conclusions
-----------

So there you go. I hope you have taken away a number of things about the value of extracting multiple occurrences from a list and a technique for enhancing interactive reporting. If there is one thing I really wanted to convey during this article, its how much I love the Hoff and we can never have enough occurrences of this Germanic demigod. If you enjoyed this article then please share it and let’s get a discussion going in the comments to see what other multiple occurrence madness we can come up with!

### Added by Chandoo

Thank you so much Sohail for another wonderful, intelligent & useful article. I had loads of fun reading & learning from it.

_**If you enjoyed this**_, please say thanks to Sohail in the comments section.

### Keen to learn Advanced Formulas?

Check out [Formula Forensics](http://chandoo.org/wp/formula-forensics-homepage/)
 & [Array Formula](http://chandoo.org/wp/tag/array-formulas)
 pages.

**About the author: Sohail Anwar** is a Londoner who has spent over 10,000 hours applying Excel in his professional life and earns well over 6 figures as a result. Now he is on a mission to teach professionals how to massively increase their earnings by learning and applying Excel like never before. Find out more about Sohail on [Earnwithexcel](http://earnwithexcel.com/)
 and connect with him on [LinkedIn](http://uk.linkedin.com/pub/sohail-anwar/75/b46/a46)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [60 Comments](https://chandoo.org/wp/multiple-occurrences-lookup-and-extraction/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/multiple-occurrences-lookup-and-extraction/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [filters](https://chandoo.org/wp/tag/filters/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [iferror](https://chandoo.org/wp/tag/iferror/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [large](https://chandoo.org/wp/tag/large/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [small](https://chandoo.org/wp/tag/small/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousExcel Links – 2014 Holiday Sale Edition](https://chandoo.org/wp/excel-links-2014-holiday-sale-edition/)

[NextCompare 2 sets of data by letter or word & highlight mismatches \[vba\]Next](https://chandoo.org/wp/compare-data-highlight-mismatched-letters-words/)

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
    
    [Reply](https://chandoo.org/wp/multiple-occurrences-lookup-and-extraction/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/multiple-occurrences-lookup-and-extraction/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/multiple-occurrences-lookup-and-extraction/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ