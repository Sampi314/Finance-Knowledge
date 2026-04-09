# Analyzing 300,000 calls for help [case study] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    

Analyzing 300,000 calls for help \[case study\]
===============================================

*   Last updated: May 2017

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Over the weekend, I got an email from Mr. E, one of my students. Mr. E works at a police department in California and as part of his work, he was looking at calls received by police. Whenever police get a call for help, multiple teams can respond to the call and go to the location. All of these dispatches are recorded. So a single call can have several such dispatches. And Mr. E wanted to findout which team responded the first. The problem?

_**Finding the first responded team is tricky.**_

Today let’s take up this problem as a case study and understand various methods to solve it.  We are going to learn about writing better lookups, pivot tables, power pivot and optimization. Put on your helmets, cause this is going to be mind blowingly awesome.

### A little background

We are re-opening enrollments in to the 50 ways to analyze data program in two weeks (on 10th of May, 2017, Wednesday). I want to share the process, techniques and visualizations you can use to analyze any business data with a case study. In this series of articles, let’s analyze fairly complex and large data set to derive insights.

**Please join our Analytics Email Newsletter to get all three parts of this series** and information about 50 Ways to Analyze Data program.

Let’s look at the data
----------------------

Since the original data shared by Mr. E is confidential, I made up some random call data in Excel. Here is a sample.

![raw-data-first-onscene](https://chandoo.org/wp/wp-content/uploads/2016/08/raw-data-first-onscene.png)

The calls data is maintained in an [Excel table](http://chandoo.org/wp/2009/09/10/data-tables/)
, named _calls._ 

We have 288,625 rows in this table. Let’s examine the columns in detail.

*   Call number – a unique identifier for the call
*   Unit id – Name of unit responding to call
*   Call time – Time stamp when we got the call. This is repeated for all rows with same call number
*   Enroute DTS – Time stamp when unit left to attend call
*   Onscene DTS – Time stamp when unit reached scene

The problem – How soon do we help?
----------------------------------

We need to answer the question – **how soon are we helping the callers?**

This can be answered in a variety of ways.

*   Calculate the earliest response time for each call by,
    *   difference between call time and earliest Onscene DTS
    *   difference between earliest Enroute DTS (ie first unit to respond) and corresponding Onscene DTS
*   Analyzing the response times
    *   finding key statistics – _ie_ average, median, quartiles and outliers
    *   Slicing the stats by month, call region (data not available) or team

Mr. E’s email was about **how to calculate the earliest Enroute DTS and corresponding Onscene DTS** values.

In this article, we will explore ways to calculate these values using various Excel techniques. In the next article, we will analyze response times by various dimensions to understand the trends better.

Calculating earliest enroute time – so many ways to get there
-------------------------------------------------------------

We can use a variety of techniques to calculate the earliest enroute time.

*   MIN IF formula to find the minimum time among all for a particular call number
*   VLOOKUP exact match on sorted data table
*   INDEX + _approximate_ MATCH on sorted data table
*   Pivot tables
*   Power Pivot

Let’s review each of these techniques and see which ones are easy, fast and accurate (_ie_ awesome)

### MIN IF formula

This is where Mr. E got stuck and emailed me. He was implementing an array formula to fetch the earliest enroute time using MIN and IF formulas.

Assuming a call number is listed in cell **H4**, we can fetch earliest enroute time using below MINIF formula.

`=MIN(IF(calls[Call Number]=H4,calls[Enroute DTS]))`

While this formula is _technically_ correct, Mr. E faced a curious problem. Not all units chose to attend a call even after taking it. This could be because they chose to go on another call or realized that another team is already on the way. So quite a few items in \[Enroute DTS\] are blanks _ie 0._ Now, because we are using MIN formula, it fetches 0 as the earliest Enroute DTS, _which is clearly a wrong answer._

We can add an additional check to handle blank \[Enroute DTS\] entries.

`=MIN(IF((calls[Call Number]=H4)*(calls[Enroute DTS]>0),calls[Enroute DTS]))`

Now this works.

Related: [Excel MAXIF & MINIF formulas – explained](http://chandoo.org/wp/2012/01/24/formula-forensics-no-008/)

**Verdict on MINIF formula approach**

While MINIF formula is a simple & elegant solution to this problem, it is **not scalable**. Mr. E had close to 300,000 calls spread among 400,000 rows in the calls table. This means when you want to calculate earliest Enroute DTS for all the 300,000 calls using MINIF, you can take a very looooong coffee break.

### VLOOKUP approach

We can use [VLOOKUP](http://chandoo.org/wp/2012/03/30/comprehensive-guide-excel-vlookup/)
 to return _first occurrence_ of Enroute DTS for a given call number. We needed _earliest value_ of Enroute DTS, not the _first value._ 

Problem?

Well, what if we sort the calls table by call number and Enroute DTS?

![sort-settings-first-onscene](https://chandoo.org/wp/wp-content/uploads/2016/08/sort-settings-first-onscene.png)

Now, VLOOKUP should fetch earliest Enroute DTS.

`=VLOOKUP(M4,calls,4,FALSE)`

should fetch the earliest Enroute DTS for a call number in M4.

**Verdict on VLOOKUP approach**

While VLOOKUP is easier than MINIF and gives us the answer we want, it too is not scalable. On my sample data of 300,000 rows, the VLOOKUP approach took more than 2 minutes. On a production data set, this approach could mean disaster.

### INDEX + _approximate_ MATCH approach

Why bother with _exact_ lookups when an _approximate_ one would do? That is logic behind this approach.

Assuming the call numbers are listed in M4 onwards,

*   We find the first call’s earliest Enroute DTS using regular VLOOKUP method as mentioned above.
*   From second call number onwards, we use an approximate MATCH method like below

`=INDEX(calls[Enroute DTS],MATCH(**M4**,calls[Call Number],1)+1)`

Notice that we refer M4 to fetch earliest Enroute DTS for M5.

Related: [INDEX formula](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/)
 – [INDEX + MATCH formulas](http://chandoo.org/wp/2010/11/02/how-to-lookup-values-to-left/)

**Verdict on INDEX + MATCH approach**

This approach is significantly faster than VLOOKUP or MINIF solution. On test runs with same dataset, this approach took _just a fraction of second._ That is roughly 100 times improvement in speed.

If you must use a formula approach, use this.

### Pivot Tables

[Pivot tables](http://chandoo.org/wp/excel-pivot-tables/)
 are a great way to answer questions like these. You can create a quick pivot to find earliest Enroute DTS for all calls by,

![pivot-table-report-first-onscene](https://chandoo.org/wp/wp-content/uploads/2016/08/pivot-table-report-first-onscene.png)

*   Insert a pivot from the calls table
*   Add call number & unit ID to row labels area
*   Add Enroute DTS and Onscene DTS to values column
*   Change calculation for these value fields to SUM (as by default dates are COUNTed)
*   Sort the pivot by Enroute DTS – Oldest to newest
*   Change the report layout to tabular view
*   Go to value filter for Unit ID and filter by **bottom 1 value by Enroute DTS**
*   Now you get a sparkly clean pivot with what we need.

![pivot-table-filter-first-onscene](https://chandoo.org/wp/wp-content/uploads/2016/08/pivot-table-filter-first-onscene.png)

**Verdict on Pivot Table approach**

This is the quickest of them all. Very simple and scalable upto a million rows (although when you have so many rows, Pivot calculations can be slow). I recommend that you use Pivot Table approach whenever you are solving problems like this.

### Power Pivot

While pivot table approach gives us the answer we want in a quick and efficient fashion, it has few limitations.

*   Pivot tables cant work when you have more than a million calls
*   Doing further analysis by slicing and dicing the data on various dimensions can be hard

This is where Power Pivot truly shines.

Related: [Introduction to Excel Power Pivot](http://chandoo.org/wp/2013/01/21/introduction-to-power-pivot/)
.

Let’s build a Power Pivot model around the problem.

We load calls data in to PP as linked table (but in a production environment, you can directly hookup to database containing the data, thus making your workbook smaller)

Now create below measures.

Enroute Time:= min(calls\[Enroute DTS\])

Onscene Time:= min(calls\[Onscene DTS\])

Response Time:= \[Onscene Time\] – \[Enroute Time\]

_Additionally, we can also create Earliest Enroute Time measure as,_

Earliest Enroute Time:= calculate (\[Enroute Time\], all(calls\[Unit ID\]))

Now, add the first 3 measures to a pivot table. Place call number & unit id in row labels area. Set up tabular layout for the pivot and viola, our answer is ready.

![powerpivot-report-first-onscene](https://chandoo.org/wp/wp-content/uploads/2016/08/powerpivot-report-first-onscene.png)

So there you go.

**Verdict on Power Pivot approach:**

If you have Power Pivot on your Excel, use this method all the time. This allows you lots of flexibility. You can also build additional measures to analyze the data. We will see some of these ideas in next part of this article.

Download Example Workbook
-------------------------

**[Click here to download sample workbook](https://files.chandoo.org/50w/first-on-scene-pp.zip)
** containing all these solutions. Play with various formulas and measures to learn more. Beware, some of the formulas can take lot of time to re-calculate.

What next?
----------

The purpose of any analysis is to uncover patterns, information and decision pointers buried in data. We explore more themes and techniques for analyzing data in 50 ways to analyze data program. Do check it out.

### A testimonial from Mr. E …

After helping Mr. E, he sent me below email. This is one of the reasons why I run Chandoo.org. Everytime I read a testimonial like this, I get a big bright smile on my face.

> I just wanted to say thank you very much. Although some of my columns are still calculating (holy smokes it takes a long time), the ones I’ve applied this solution to are working brilliantly.
> 
> You’ve helped me solve a very big problem for the xxxx county sheriff’s office in California; serving some 400k people. I thought that might be a nice feather to put in your hat.

Thank you E for emailing an interesting problem.

### Sign up to know more about 50 ways to analyze data course

If you like this and want to learn more about data analytics, understand how our 50 ways to analyze data program can help you, sign up for our course newsletter. [**Please click here**](https://forms.aweber.com/form/95/1834602295.htm)
.

Share on FB

Tweet this

Post to LinkedIn

![](https://chandoo.org/wp/wp-content/uploads/2019/12/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

*   [11 Comments](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [MATCH()](https://chandoo.org/wp/tag/match/)
    , [minif](https://chandoo.org/wp/tag/minif/)
    , [no ads](https://chandoo.org/wp/tag/no-ads/)
    , [no-nl](https://chandoo.org/wp/tag/no-nl/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [power pivot](https://chandoo.org/wp/tag/power-pivot-2/)
    , [reader questions](https://chandoo.org/wp/tag/reader-questions/)
    , [solo](https://chandoo.org/wp/tag/solo/)
    , [vlookup](https://chandoo.org/wp/tag/vlookup/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Pivot Tables & Charts](https://chandoo.org/wp/category/pivot-tables-charts/)
    , [Power Pivot](https://chandoo.org/wp/category/power-pivot/)
    

[PrevPreviousWeekend open mic – Share your one hand Excel shortcuts](https://chandoo.org/wp/share-your-one-hand-shortcuts/)

[NextPSA: Don’t let auto correct spoil your partyNext](https://chandoo.org/wp/psa-dont-let-auto-correct-spoil-your-party/)

### 11 Responses to “Analyzing 300,000 calls for help \[case study\]”

1.  ![](https://secure.gravatar.com/avatar/af327b45480d0b0df193c12b96d9f01f48f1cd020c8e8411f4383a10ec06ab6b?s=64&d=mm&r=g) Mr. E~ says:
    
    [August 24, 2016 at 6:52 pm](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1264996)
    
    THANK YOU! 😀
    
    [Reply](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1264996)
    
2.  ![](https://secure.gravatar.com/avatar/4d22adaea210563549a74c38ae4e24369da7d527274b411eee6db326f8217cf1?s=64&d=mm&r=g) Sarath says:
    
    [August 25, 2016 at 3:21 pm](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1266159)
    
    This was nice a very much helpful  
    Awaiting this type of posts
    
    [Reply](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1266159)
    
3.  ![](https://secure.gravatar.com/avatar/b576f4f1458b74b38710840d655dc31c96d03d64274af8fb9445f86cbd9581ce?s=64&d=mm&r=g) m-b says:
    
    [August 26, 2016 at 7:37 am](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1266896)
    
    "Pivot tables cant work when you have more than a million calls"
    
    I'm pretty shure they can as long as you hook up the pivot table directly to a database (so the data isn't loaded into a worksheet).
    
    In 2013/16 you can also load data > 1m records directly into the data model without needing Power Pivot.
    
    [Reply](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1266896)
    
4.  ![](https://secure.gravatar.com/avatar/ab457cc6efd267db9f5caf0297c0e8d5693409dc56b6ffac83627bb0147c00c3?s=64&d=mm&r=g) [Tobias](http://www.changethislimited.co.uk/)
     says:
    
    [August 26, 2016 at 9:29 am](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1266951)
    
    This is good advice, but as much as I love Excel, I would drop the whole data set into Power BI and analyse it there if I had the option. 🙂
    
    [Reply](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1266951)
    
    *   ![](https://secure.gravatar.com/avatar/0254258765d00f319f262770750b0c99309c49191425071320ad3b54282b449f?s=64&d=mm&r=g) Khedidja Bratlien says:
        
        [May 4, 2017 at 10:55 pm](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1442805)
        
        Since I discovered Power BI, Tableau & SpotFire, I enjoy playing with data & discovering patterns.
        
        [Reply](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1442805)
        
5.  ![](https://secure.gravatar.com/avatar/acb9c5dc0a62f21bd7ef36ef24a8a905f6b9d1b304b63af442a7108efdc838d4?s=64&d=mm&r=g) Ali says:
    
    [August 31, 2016 at 4:40 pm](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1270043)
    
    Does this course require advance statistic knowledge
    
    [Reply](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1270043)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [September 1, 2016 at 1:01 am](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1270587)
        
        @Ali
        
        No
        
        [Reply](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1270587)
        
6.  ![](https://secure.gravatar.com/avatar/de881b846fc784768b92545b4addb1b690bcb74fcb3f755f0aa0b4ba25f8c699?s=64&d=mm&r=g) Bruce says:
    
    [January 19, 2017 at 6:02 pm](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1395042)
    
    One thing to check also is in the raw CAD data there is typically a column with some vague name that indicates the order of the time stamps and that can be used to filter the initial query down better.
    
    [Reply](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1395042)
    
7.  ![](https://secure.gravatar.com/avatar/2e34fa74a83df00c70a41e3c0bc2212a228d24cf4d2614888a2febf9c806ca21?s=64&d=mm&r=g) Pranav J. says:
    
    [May 7, 2017 at 6:09 pm](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1444384)
    
    Great article as usual! I was thinking 2 nice variables to add to this analysis would be the nature of call and the location of each unit from caller location.
    
    I think it might be beneficial to know if certain types of calls are being responded to faster or slower than others keeping distance as a constant.
    
    Any thoughts?
    
    [Reply](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1444384)
    
8.  ![](https://secure.gravatar.com/avatar/ef98efde964362b2f76344c319b903a48daf0b28e4c826d1ac3009379617effa?s=64&d=mm&r=g) Ron says:
    
    [February 11, 2018 at 1:19 pm](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1535706)
    
    Hello Chandoo,
    
    I'm a bit of dilemna with my tasks. I have a table which tells me how long a room was out of service due to refurb. It has a column for From and To.
    
    Example  
    Desc Rm Num Room Type Status Return Status From To  
    Ref 2033 SUIX OO Dirty 13/07/2017 31/12/2017
    
    My aim is to create a new table where it gives me daily entries when SUIX was out of service instead of From and To
    
    So in the example above, my new table should be  
    Ref 2033 SUIX OO Dirty 13/07/2017  
    Ref 2033 SUIX OO Dirty 14/07/2017  
    Ref 2033 SUIX OO Dirty 15/07/2017  
    .  
    .  
    .  
    .  
    until it meets the To criteria  
    I'm thinking of doing an array but also thinking of VBA macro...  
    The formula or macro must check each row and perform the action. Once done, it moves to the next row.
    
    What are your thoughts? Would you recommend any other way?
    
    Appreciate your help!
    
    Kind Regards,
    
    Ron
    
    [Reply](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-1535706)
    
9.  ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
    
    [August 12, 2025 at 8:01 pm](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-2436875)
    
    I'm on a roll for replying to older posts with newer solutions, so here's one more.
    
    While Excel 365 now has MINIFS and won't require CSE (Ctrl+Shift+Enter), there's still a faster way for a dataset this large. If H5# represents =UNIQUE(calls\[Call Number\]), then MINIFS took roughly 25 seconds on my computer...
    
    \=MINIFS(calls\[Enroute DTS\],calls\[Call Number\],H5#)
    
    ...whereas XLOOKUP with SORT took less than 1 second...
    
    \=LET(  
    ord,SORT(HSTACK(calls\[Call Number\],calls\[Enroute DTS\]),{1,2}),  
    XLOOKUP(H5#,CHOOSECOLS(ord,1),CHOOSECOLS(ord,2),,,2)  
    )
    
    [Reply](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#comment-2436875)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/analyzing-300000-calls-for-help-case-study/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ