# Data analysis worst practices - 18 things to watch out for

**Source:** https://chandoo.org/wp/analysis-worst-practices

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

18 ways to turn analysis projects into a nightmare
==================================================

*   Last updated: September 2016

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

Every week, we read news about failed analysis projects. If you listen carefully, you can hear the grunts, screams and curses of thousands of analysts all over the world about their analysis nightmares.

At Chandoo.org, we talk a lot about [best](http://chandoo.org/wp/2009/11/03/make-better-excel-sheets/)
 [practices](http://chandoo.org/wp/2012/08/29/best-practice-modeling-5tips/)
 [for](http://chandoo.org/wp/2014/09/04/cp019-best-practice-modeling-tips/)
 [data](http://chandoo.org/wp/2014/04/24/cp006-become-better-analyst/)
 [analytics](http://chandoo.org/wp/resources/ways-to-analyze-business-data/)
. So today, let’s peek in to the dark side and understand the mistakes that can turn your analysis project into a nightmare.

There are 3 parts in any analysis project
-----------------------------------------

To understand these _worst practices_ in analysis world, first let’s break analysis projects in to 3 parts.

*   Requirements
*   Data Structure
*   Tools & Construction

Let’s deep dive in to each area of the analysis projects to see what can go wrong.

### Requirements – Worst practices

Any analysis work must begin with requirement gathering. This is when you set out the _objective_ for your work. So what can go wrong at this stage?

![poor-requirements-analysis-worst-practices](https://chandoo.org/wp/wp-content/uploads/2016/09/poor-requirements-analysis-worst-practices.png)

1.  **Asking wrong questions:** Start with a wrong question and you will end up analyzing wrong stuff. Its that simple.
2.  **Asking wrong people:** In most analysis projects the people who will use outputs (consumers) are not the same people who may pay for it (buyers). For example, you may be designing a customer service dashboard that will be used by supervisors and store managers, but the people paying for it could be in marketing department. So if you ask the wrong people (ie buyers, gate keepers, figure heads) instead of right ones (end users), you will end up with wrong set of requirements.
3.  **Not enough whys:** Anytime you have a requirement from your user, you should follow up with, “Why do you need this…?”. Do it at least a few times until you hit the bottom. This will give you correct idea of the needs of your users.
4.  **Too much or too little detail:** If you gather too much detail during requirements phase, you will end up wasting a lot of time over tiny things and may loose the big picture. On the other hand, too little detail and you will end up making too many assumptions. So what is the right level detail? This comes with practice. The best way to tackle this is, collect too much, prioritize the needs and build only for top 5 / 10 requirements. Once you have a version ready, show case and iterate.

### Data Structure – Worst practices

Once you know what your user wants, you can start going thru data to prepare the analysis. So what can go wrong at this stage? Oh so much.

At this stage, there are usually 2 kinds of mistakes.

**Table level worst practices:**

![duplicate-data-analysis-worst-practices](https://chandoo.org/wp/wp-content/uploads/2016/09/duplicate-data-analysis-worst-practices.png)

1.  **Not using tables:** If your data is not structured in tables (could be ranges or [Excel tables](http://chandoo.org/wp/2009/09/10/data-tables/)
    ), then you are asking for trouble.
2.  **Separated data:** Data that should be together, but split in to multiple sets. For example, student data maintained by each class in a separate spreadsheet (or workbook) just makes the analysis work extra hard.
3.  **Duplicate data:** Same data appearing several times across various data sets is a common problem. If you don’t know what is duplicated, you end up doing lots of extra steps even before starting the analysis.
4.  **Wrong structure:** Tall and narrow. That is what works best for tables. Few columns, lots of rows. Anytime you have a structure that is not like this (ie a pivot _kind of_  table as source data, rows with variable number of columns etc.) you are in a for a long night and gallons of coffee.
5.  **Too much data:** Want to analyze the trends for 2016, but have data from 1990? You have too much data. Trim down to just what you need before starting your formula engine, or else you would be stuck in _calculating x%_ hell.

**Row / cell level worst practices:**

![blank-cells-analysis-worst-practices](https://chandoo.org/wp/wp-content/uploads/2016/09/blank-cells-analysis-worst-practices.png)

1.  **Multiple values in a cell:** IF(Cell has more than 1 value, analyst SAD, analyst HAPPY). Parsing cells and splitting values is tricky, error prone and a waste of time. If possible, avoid at the source by keeping one value per cell.
2.  **Inconsistent formats:** This is quite common for date values, but you can have it for others too. A date maintained as 1-SEP-2016 in first cell, 01/09/2016 in another and 01-09-2016 in another calls for lots of trouble.
3.  **Blanks:** Cells, rows or columns that have arbitrary blank values are hard to track and fix.
4.  **Merged cells:** These can cause a lot of heartache and slow down your workbooks. Keep merged cells to the headers / display part, but don’t merge things inside data section.

### Tools & Construction – Worst practices

Even if you have awesome requirements, perfect data, you can still screw up your analysis project by choosing wrong tools and following shabby construction practices. So let’s see what these are:

![recalculation-volatile-functions-analysis-worst-practices](https://chandoo.org/wp/wp-content/uploads/2016/09/recalculation-volatile-functions-analysis-worst-practices.png)

1.  **Using wrong tools for the job:** Imagine writing your own VBA code to find matching value in a column and to return corresponding value from another column. You would spend lots of time thinking about all scenarios for the code. But hey, why not use VLOOKUP() instead? By using  wrong tools for the job, you will end up doing extra work and getting poor results. Use below mapping to find best tools (from best to good in that order) for any part of your analysis work.![Recommended tools for data analysis work - Excel](https://chandoo.org/wp/wp-content/uploads/2016/09/recommended-tools-data-analysis-v2.png)
2.  **Loyalty:** If you become too loyal to a particular tool / concept of doing things, then you will end up with extra work for solving even simple problems. For example, if you are a super fan of Excel formulas and use them for everything, then you would end up writing long formulas for simple things like removing duplicates from a list. The same can be achieved with just a few clicks with either Power Query, Pivot Tables or [Remove Duplicates](http://chandoo.org/wp/2009/06/22/remove-duplicates/)
    . Likewise, if you want to use pivot tables for everything, then you may end up compromising for certain types of analysis because it is not possible with them.
3.  **Volatile Workbooks:** Using too many [OFFSET](http://chandoo.org/wp/2012/09/17/offset-formula-explained/)
    s, NOWs and other volatile functions in your complex workbook can slow things down to a grinding halt. Use [smarter functions](http://chandoo.org/wp/2013/09/18/index-formula-usage-and-tips/)
     where possible.
4.  **Spaghetti Spreadsheets:** You know the kind where the formulas are interconnected hot mess. Once you make a spaghetti with your workbook formulas, you can say goodbye to maintainability. Layer your workbooks like pizza instead. Build formulas / logic one on top of another in orderly fashion.
5.  **Lazy referencing:** writing your formulas with A:A, 1:1 etc. is lazy. Once you are lazy, your analysis gets crazy. Avoid lazy referencing by using either Tables or [dynamic references](http://chandoo.org/wp/2009/10/15/dynamic-chart-data-series/)
    .

50 ways to make your analysis projects awesome:
-----------------------------------------------

Of course, for every worst way to analyze data, there are dozens to make awesome analysis. If you want to learn the best way to analyze any kind of data along with a deep dive in to advanced Excel features and case studies, check out our [**50 ways to analyze data program**](http://chandoo.org/wp/resources/50-ways-to-analyze-data/)
. This online course will make you awesome in analytics.

[![50-ways-program-know-more](https://chandoo.org/wp/wp-content/uploads/2016/09/50-ways-program-know-more.png)](http://chandoo.org/wp/resources/50-ways-to-analyze-data/)

### Share your analytics worst practice:

Do you come across any of the above worst practices in your day to day work? What is the worst you have seen? Please share in the comments section so we all can learn from these mistakes.

Share on FB

Tweet this

Post to LinkedIn

![](https://chandoo.org/wp/wp-content/uploads/2019/12/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

*   [8 Comments](https://chandoo.org/wp/analysis-worst-practices/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/analysis-worst-practices/#respond)
    
*   Tagged under [50 ways course](https://chandoo.org/wp/tag/50-ways-course/)
    , [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [list posts](https://chandoo.org/wp/tag/list-posts/)
    , [solo](https://chandoo.org/wp/tag/solo/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousHourly Goals Chart with Conditional Formatting](https://chandoo.org/wp/hourly-goals-chart-with-conditional-formatting/)

[NextTell me about an analysis problem that you couldn’t solve with Excel?Next](https://chandoo.org/wp/tricky-analysis-problems-poll/)

### 8 Responses to “18 ways to turn analysis projects into a nightmare”

1.  ![](https://secure.gravatar.com/avatar/9041859041cd28e5aa9263fddc22e53b0075f637771e934134f1982b756bfab9?s=64&d=mm&r=g) [Kevin Lehrbass](https://www.youtube.com/user/MySpreadsheetLab)
     says:
    
    [September 5, 2016 at 1:12 pm](https://chandoo.org/wp/analysis-worst-practices/#comment-1275208)
    
    Excellent article Chandoo! Often times once the business requirements are finalized people tend to rush into the analysis phase without examining the data and doing any necessary normalization (aka unpivot data), consolidation, cleaning, etc.  
    When the analysis is built on top of such data structures then it's just a matter of time before things start to fall apart. A classic is when the same data-set is spread across many sheets (to keep it in presentation mode) and then heavy formulas are required to analyze it. Much easier to normalize and consolidate it before adding formulas. We can always create a quick pivot to display data for meetings/presentations.  
    Cheers,  
    Kevin Lehrbass
    
    [Reply](https://chandoo.org/wp/analysis-worst-practices/#comment-1275208)
    
2.  ![](https://secure.gravatar.com/avatar/b0baa1a46e9d7ed29872e9ca0b8154a0d08542a91d2b2e1ecacbbd24a88f6cd0?s=64&d=mm&r=g) Mark Freeman says:
    
    [September 5, 2016 at 7:09 pm](https://chandoo.org/wp/analysis-worst-practices/#comment-1275513)
    
    Great post! Thank you!
    
    [Reply](https://chandoo.org/wp/analysis-worst-practices/#comment-1275513)
    
3.  ![](https://secure.gravatar.com/avatar/9c164737a5a3494b218b0f78e7ed76b38428d82e1a9306c856c085f33a630f45?s=64&d=mm&r=g) Pavel says:
    
    [September 6, 2016 at 7:44 am](https://chandoo.org/wp/analysis-worst-practices/#comment-1276138)
    
    Good post. My experience or other bad practices I avoid:  
    • Did disposable analysis – if your analysis is good you may expect that you will do it every months.  
    • Adjust data manually – If you couldn’t change data structure in source you have to do it by VBA, formulas, Pivot tables, queries etc. Manually data cleaning/normalization is worse, then spaghetti spreadsheets because nobody describe them.  
    • Cleaning every blanks rows or columns – is better in April have 8 blank columns (for May to December) in stabile data/formula structure for whole year.  
    • Formulas and calculation in analysis – the only formulas in analysis that I use is for reaction on changes/inputs that I allow to user. For data collection, cleaning, manipulation and changing structure is working Workbook – if it is slow use manual calculation.
    
    [Reply](https://chandoo.org/wp/analysis-worst-practices/#comment-1276138)
    
    *   ![](https://secure.gravatar.com/avatar/6e814ec3f049ecaccb2af5c722f2715605e26c0ed0ed6bef758045502025559a?s=64&d=mm&r=g) Geoff says:
        
        [September 6, 2016 at 12:57 pm](https://chandoo.org/wp/analysis-worst-practices/#comment-1276357)
        
        What a great post!
        
        One of the "worst practices" I'll share is not providing an estimated return on investment in an analysis. If a business decides to follow through with your recommendations, track the performance of the business unit after the recommendations have been implemented! This is the best way to ensure your services are needed in the future (provided your analysis actually makes sense 🙂 ).
        
        [Reply](https://chandoo.org/wp/analysis-worst-practices/#comment-1276357)
        
4.  ![](https://secure.gravatar.com/avatar/ee6a2ce87785841a04ab1b6ee1c25509f692394347c330e462838653d0a37c50?s=64&d=mm&r=g) Harry says:
    
    [September 6, 2016 at 4:15 pm](https://chandoo.org/wp/analysis-worst-practices/#comment-1276582)
    
    Excellent article.
    
    My 0.02c would be that in order to generate operable analysis, a clear scope of the purpose of the analysis is vital.
    
    Too often we end up doing all of the analysis and calculation only to find that the client actually wasn't interesting in X metric and wanted Y metric. Regardless of whether X metric is the better measurement!
    
    [Reply](https://chandoo.org/wp/analysis-worst-practices/#comment-1276582)
    
5.  ![](https://secure.gravatar.com/avatar/2fcd7aec46116b6603378e17308ddafcdd0bd1f029986ab9df3407458874cebb?s=64&d=mm&r=g) f(x)dx says:
    
    [September 7, 2016 at 2:38 pm](https://chandoo.org/wp/analysis-worst-practices/#comment-1277831)
    
    For sure mixing source data, analysis and presentation in one sheet is one of the biggest mistakes I used to make.
    
    Another mistake is not critically assessing the results of the analysis.  
    Simply asking "Does it make sense?" or "Does it match other similar reports?" might reveal a fundamental mistake in your analysis.  
    Imagine a perfect analysis for ice cream sales in Europe showing peak in January and you will understand my point.
    
    [Reply](https://chandoo.org/wp/analysis-worst-practices/#comment-1277831)
    
6.  ![](https://secure.gravatar.com/avatar/ecf75ba5d518a210ce02de8d246b882bbcff127c913694768bcd9636fea07ebd?s=64&d=mm&r=g) Bhavani Seetal Lal says:
    
    [September 9, 2016 at 6:42 am](https://chandoo.org/wp/analysis-worst-practices/#comment-1279414)
    
    Lots of things to learn.
    
    Thanks,  
    Chandoo Sir.
    
    [Reply](https://chandoo.org/wp/analysis-worst-practices/#comment-1279414)
    
7.  ![](https://secure.gravatar.com/avatar/d7d4c1e128e7cf0f5c73f99d075b817b5546f8b209cfde608f7dec70d66d2329?s=64&d=mm&r=g) [George Mount](http://georgejmount.com/)
     says:
    
    [September 19, 2016 at 5:14 pm](https://chandoo.org/wp/analysis-worst-practices/#comment-1291830)
    
    Oh I love this article. How many times has Excel taken the bum rap for poor data quality and results when it is really poor requirements analysis and project management to blame?
    
    Love the way how you gradually dive deeper into the spreadsheet but warn analysts not to get into the actual development until they have a clear understanding of the users' needs. This is bigger than any spreadsheet!
    
    [Reply](https://chandoo.org/wp/analysis-worst-practices/#comment-1291830)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/analysis-worst-practices/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ