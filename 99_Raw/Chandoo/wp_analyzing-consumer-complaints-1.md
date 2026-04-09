# Analyzing half a million consumer complaints [Part 1 of 3] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/analyzing-consumer-complaints-1

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Analyzing half a million consumer complaints \[Part 1 of 3\]
============================================================

*   Last updated on October 10, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_**How would you analyze data when you have lots of it?**_ That is the inspiration for this series.

![analyzing-consumer-complaints-interactive-treemap-th](https://chandoo.org/wp/wp-content/uploads/2016/02/analyzing-consumer-complaints-interactive-treemap-th.png)

This is the first part of 3 part series on this theme. Please use below links to access other parts.

1.  **What do they complain about – Part 1**
2.  [Regional trends – Part 2](http://chandoo.org/wp/2016/02/18/analyzing-customer-complaints-2/)
    
3.  [My bank vs. your bank in a scorecard – Part 3](http://chandoo.org/wp/2016/02/23/customer-satisfaction-scorecard/)
    

Let’s meet our data – Finance Industry Consumer Complaints
----------------------------------------------------------

As part of open data initiatives, US government & Consumer Financial Protection Bureau maintain a list of all consumer complaints made against financial institutions (banks, credit unions etc.) You can download this data from the [catalog page here](http://catalog.data.gov/dataset/consumer-complaint-database)
. I have obtained the data on 1st of February, 2016. The download has 513,824 records. Each row contains one complaint.

The data has these columns.

![about-the-consumer-complaint-data](https://chandoo.org/wp/wp-content/uploads/2016/02/about-the-consumer-complaint-data.png)

Analyzing with a blank slate – how to start?
--------------------------------------------

Here is how we can find things to analyze / discover / visualize / present in similar situations.

### Metrics & KPIs

All industries have metrics / KPIs. Can you identify the metrics that matter in a given situation? For example, if you are the CEO of Citi Bank and you want to understand your bank’s performance in the customer service area, you could define below metrics:

*   **Complaints per million transactions:** A high rate indicates poor customer experience.
*   **Average response time:** Low response times indicate smooth & well defined processes and empowered support staff.
*   **% of disputed resolutions:** A high percentage indicates customers are not happy with the solution offered by the bank.

### Top x items

Knowing which products / regions / customer groups are making most complaints (or most anything) can help you identify underlying issues and address them. Let’s say you found out that identity theft is a big issue, you could launch a campaign to educate customers about safe banking, offer additional security measures like 2 step verification etc.

### Trends

You could look at the trend of complaints (or any other metrics) over time to understand improvement in the performance. Let’s say you want to understand how your _safe banking_ campaign impacted number of complaints made in the **identity theft category.** A trend analysis will provide the information you want.

### Pareto Analysis

This is a variation of top x items. If you are short on resources and want to know which items are easy pickings to improve your customer service. A Pareto analysis on the issues raised by customers can tell you just that.

### Distribution

Knowing how things are spread on an axis can help you optimize your processes. For example, if you know that every Wednesday we get a lot of complaints, we can plan our contact center staffing in a such a way to reduce the average waiting time.

### Many more…

A blank canvas (in this case, raw data) offers many possibilities. As an analyst, our job is to dig out the information that helps our company succeed.

Ways to analyze this complaint data
-----------------------------------

As there are many options, I just picked three to showcase what we can do. Feel free to download the data and do your own analysis.

1.  **What do they complain about – Part 1**
2.  [Regional trends – Part 2](http://chandoo.org/wp/2016/02/18/analyzing-customer-complaints-2/)
    
3.  [My bank vs. your bank in a scorecard – Part 3](http://chandoo.org/wp/2016/02/23/customer-satisfaction-scorecard/)
    

What do they complain about?
----------------------------

There are 11 types of products & 48 sub-products spread across 3,496 companies. There are 95 types of issues faced by customers, further categorized in to 68 sub issues. And there is complaint narrative (only available on 50,902 complaints or roughly 10%).

Making sense of all this text can be hard and complex.

This is where pruning comes in to picture. If we can understand just top 25 issues and give user the power to drill down to any product / state / time frame, then users can discover issues that matter most.

### Analyzing top 25 issues

The first step is simple. We just make a pivot table from the data (make sure you add the pivot table to data model to capitalize on new Excel features) and drop the **issue in rows area** and **complaint ID in to values area.**

We get this:

![pivot-table-with-issue-and-count](https://chandoo.org/wp/wp-content/uploads/2016/02/pivot-table-with-issue-and-count.png)

Now, add below filters

*   Timeline on the Date Received
*   Slicer on Product
*   Slicer on State

**Sort the pivot table** by descending order of Complaint Count.

Although the sorted pivot table (first 25 rows) provides the answer we want, it is a tough  nut to chew. So let’s jazz it up.

### Visualizing top issues – Treemap

For the visualization, let’s use Tree map chart introduced in Excel 2016. _If you are using Excel 2013 or earlier, don’t worry. We will learn another way to visualize the data further down this page._

If you select the pivot data and try to insert a treemap chart, you get a message booing you.

![error-when-adding-treemap-from-pivot-data](https://chandoo.org/wp/wp-content/uploads/2016/02/error-when-adding-treemap-from-pivot-data.png)

No worries, we will trick Treemap to work with pivot data. Just copy the first 25 rows of the pivot and paste them as link in a blank sheet.

Now that the data is in a regular Excel range, we can create a Treemap from it. Before we do that, let’s just add 26th row to the data, with the issue label \[Other\], which is the total of any issues outside top 25.

Select all this data and insert a treemap from Insert ribbon.

### Polishing the visualization

Let’s move the chart, slicers & timeline to a separate sheet. Just cut and paste them.

Polish the slicers using styles and customization features (disabling the header, adjusting number of columns etc.) For more on slicer customization, read **[Introduction to slicers](https://chandoo.org/wp/introduction-to-slicers/)
**.

Adjust timeline granularity to Quarters.

**Our polished slicers**

![slicers-and-time-line-for-interactive-treemap](https://chandoo.org/wp/wp-content/uploads/2016/02/slicers-and-time-line-for-interactive-treemap.png)

Set up descriptive chart title & captions by harvesting the data from slicers, timeline & pivot. You may refer to download workbook for the actual formulas. Note, these work only in Excel 2013 or above.

The final visualization looks like this, click on it to enlarge.

[![analyzing-consumer-complaints-interactive-treemap](https://chandoo.org/wp/wp-content/uploads/2016/02/interactive-treemap-with-titles.png)](https://chandoo.org/wp/wp-content/uploads/2016/02/analyzing-consumer-complaints-interactive-treemap.png)

### Demo of the visualization

Check out the video demo of this interactive visualization & analysis.

### Alternative Visualization for Excel 2010

As Treemap is not available in Excel 2013 or earlier, we can use other visualizations like bar charts or conditional formatting heatmaps to visualize this data. Here is an attempt, using bar charts.  Click to enlarge the image.

![alternative-visualization-excel-2010](https://chandoo.org/wp/wp-content/uploads/2016/02/alternative-visualization-excel-2010.png)

Download Example Workbook
-------------------------

**[Please click here to download the consumer complaints analysis – part 1 workbook](https://files.chandoo.org/50w/consumer-complaints-vis.xlsx)
**. Play with the visualizations to learn more.

Note: this file is 100 + mb. So give it a few minutes to download.

### Next part – Regional trends & analysis

The 2nd part of this case study is now ready. **[Please click here to read regional trends & analysis of customer complaints data](http://chandoo.org/wp/2016/02/18/analyzing-customer-complaints-2/)
**.

### How would you analyze the complaint data?

**Go ahead and play with this data yourself.** How would you analyze it? Please share your ideas, analysis & charts in the comments section. _**If you wish to publish a chart,**_ email it to chandoo.d@gmail.com with the subject “Half a million complaints”. I will add your chart at the end of this post.

### Learn more about data analysis & reporting

I cover this topic and 50 other case studies in my online class **50 ways to analyze data.** If you are keen to learn advanced analytics and data science thru Excel, I highly recommend 50 ways course. [**Check it out here**](https://chandoo.org/wp/resources/50-ways-to-analyze-data/)
.

For something less intense, but still as much fun and detailed, check out Excel School program. This course teaches intermediate to advanced Excel with specific focus on Dashboard Reporting. [**Check out Excel School here**](https://chandoo.org/wp/excel-school-program/)
.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

*   [16 Comments](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/analyzing-consumer-complaints-1/#respond)
    
*   Tagged under [50 ways course](https://chandoo.org/wp/tag/50-ways-course/)
    , [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [bar charts](https://chandoo.org/wp/tag/bar-charts/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [excel 2016](https://chandoo.org/wp/tag/excel-2016/)
    , [heatmaps](https://chandoo.org/wp/tag/heatmaps/)
    , [no ads](https://chandoo.org/wp/tag/no-ads/)
    , [no-nl](https://chandoo.org/wp/tag/no-nl/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [slicers](https://chandoo.org/wp/tag/slicers/)
    , [time lines](https://chandoo.org/wp/tag/time-lines/)
    , [tree maps](https://chandoo.org/wp/tag/tree-maps/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousFormula Forensics 040 – Apportioning Sales by Criteria](https://chandoo.org/wp/formula-forensics-040-apportioning-sales-by-criteria/)

[NextAnalyzing half a million customer complaints – Regional Trends \[Part 2 of 3\]Next](https://chandoo.org/wp/analyzing-customer-complaints-2/)

![](https://chandoo.org/wp/wp-content/uploads/2019/12/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/introducing-advanced-excel-training-v1.png)](https://chandoo.org/wp/excel-school-program/)

Chandoo is an awesome teacher

__________ Rated 5 out of 5

_– Jason_

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![](https://chandoo.org/wp/wp-content/uploads/2019/12/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Complete Introduction to Power BI](https://chandoo.org/wp/powerbi-introduction/)

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
    

### 16 Responses to “Analyzing half a million consumer complaints \[Part 1 of 3\]”

1.  ![](https://secure.gravatar.com/avatar/bdbad733fc10aa7a8871d53ef0be19f2f1df930cda581fe2ddee13ab8cd543d4?s=64&d=mm&r=g) John says:
    
    [February 16, 2016 at 5:26 pm](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1133559)
    
    The only disappointments foreseen that keep me from enrolling in these courses (at my own personal expense, of course, no way my employer would fund it) are: 1) how long the course material is accessible, considering the price (it IS an online course, after all, so overhead can't be that high) 2) especially considering the price, it's a shame to see how much time I'll spend covering subjects I'm already familiar with, and 3) a lot of the stuff I've been seeing requires Excel later than 2007, which I currently have (sorry, but I got tired of repeatedly forking out hundreds of dollars at every new version, usually to find myself stuck having to relearn the new steps for old functions (the ribbons took a while, and finding macros was tedious, then the custom toolbar Ï had in 2003 for those functions I use all the time was suddenly impossible)
    
    [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1133559)
    
    *   ![](https://secure.gravatar.com/avatar/379e46dbd3095aae6ba1c5cdcaa798775f9f75068ea9b5535cb7e551eef9f274?s=64&d=mm&r=g) John Omohundro says:
        
        [February 16, 2016 at 9:58 pm](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1133613)
        
        Hi John. Like you, my (now former) employer would not have paid for these courses, and I was stuck at the 2007 version for similar reasons. One solution for upgrading Excel at minimal up-front expense is to get a Microsoft 365 Pro Plus subscription. It's about $12 a month, and you can get the latest updates from now until you decide to stop subscribing.
        
        Custom toolbars are possible in later versions of Excel, too...this may be worth your while.
        
        I greatly feared becoming obsolete, and I wanted to learn Power Pivot and Power Query, neither of which exist in 2007. Subscribing (yes, at my own expense) was the best choice. Chandoo's courses have also helped me in my quest to stay up-to-date. Yes, his courses are pricey, but (1) they are great courses, and (2) this is how Chandoo puts food on the table, and I don't blame him for not giving them away. He puts lots of effort into the content, and if I was him I would charge top dollar too.
        
        [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1133613)
        
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [February 17, 2016 at 3:37 am](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1133679)
        
        Hi John. Thanks for your comments. We offer full downloads of all lesson videos in our programs. These do not expire. It is something very few online training providers do, but I have made a conscious choice to give the downloadable videos so that users can refer to the content anytime. The online access is valid for an year but you can extend for 1 more by paying a fraction of the fee (usually $50 per 6 months and $100 per year). Although our cost for giving access is low, our costs on admin & tech support are high. As long as you remain a student in the classroom, you can post questions and doubts which we answer.
        
        Please note that there is no compulsion to join any of our courses. You can read all the free content, download example files, listen to podcasts and watch free videos I post on YouTube without even paying me a penny. The courses enable me to I support my family and work on my mission of making people awesome.
        
        All the best.
        
        [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1133679)
        
    *   ![](https://secure.gravatar.com/avatar/22b5c8a392832ec7c4d491054a133a2210a57a5dee802a70895c20e4cfb46caf?s=64&d=mm&r=g) Olivier says:
        
        [August 25, 2016 at 6:46 pm](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1266279)
        
        Hi John,  
        sorry to say this but you are too negative in your comments and focus too much on obstacles (and excuses).  
        Decide what you want and find ways to get it.  
        Focus your energy on overcoming obstacles rather than complaining.  
        Enjoy all the free stuff available online.  
        When you can afford it buy content that is relevant for you.
        
        [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1266279)
        
2.  ![](https://secure.gravatar.com/avatar/2e6abaf5ac49344b95f76181c0d2c52d1cb33bf95c3606caec5af112482bfc3d?s=64&d=mm&r=g) [MF](http://wmfexcel.com/welcome)
     says:
    
    [February 17, 2016 at 7:33 am](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1133720)
    
    Hi Chandoo,  
    FYI. The pivot table is not working if the file is opened with Excel 2010... 🙁  
    Here's the error message for your information:  
    This workbook contains an Excel data model that is created in a newer version of Excel. You can open this workbook in an older version of Excel, but you will be unable to load or work with PowerPivot when it coexists with a Excel data model.
    
    [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1133720)
    
3.  ![](https://secure.gravatar.com/avatar/e984428c6ab6c67aad48bfb43381a04d4043a46461be741b0cd690a9da19cae1?s=64&d=mm&r=g) James P says:
    
    [February 17, 2016 at 9:42 pm](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1133861)
    
    Chandoo -
    
    Thanks for this. Gave me a good working example of the cube functions with slicers.
    
    When I add the data to the data model to use the cube functions to identify slicer selections, the number formatting doesn't carry over to the slicer from the data table. Is that what you have found? Any ideas on why that is? If it's not part of the data model, whatever number format I set in my table shows up in the slicer buttons, no problem.
    
    Thanks.
    
    [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1133861)
    
4.  ![](https://secure.gravatar.com/avatar/f3b65a862978bf577462d216ea74ccfb7f9d02f008edabfea84f1ff1d1a8141a?s=64&d=mm&r=g) Jim says:
    
    [February 19, 2016 at 3:19 pm](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1134487)
    
    Chandoo,
    
    Your other readers might be interested to know that I too had an issue with being stuck in the dark ages of Excel 2007 (both at home and at work) until I discovered Office 2013 on eBay. There are plenty of reputable sellers offering valid licence keys taken from scrapped PCs which work well with downloaded versions of the software from Microsoft. At the end of last year I paid £66 (about $100) for 2 licence keys which both activated perfectly. Seems to me a much better deal than $12 per month, indefinitely, for Office 365.
    
    [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1134487)
    
5.  ![](https://secure.gravatar.com/avatar/d8f81a0ea38d9cce5538598ebd221d48d275a53a9fca642f43f982ff53e448d7?s=64&d=mm&r=g) Anthony says:
    
    [February 22, 2016 at 3:26 am](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1135157)
    
    How to determine the reputable sellers offering valid licensing keys on eBay? Would like to do this too. I cant follow along with Excel 2010 so I need to upgrade....
    
    [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1135157)
    
6.  ![](https://secure.gravatar.com/avatar/71b221d6b4a6bb5aefc117fba0da345fbe3590a3500b809e8872b26e27bdd011?s=64&d=mm&r=g) Richard says:
    
    [February 24, 2016 at 2:44 pm](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1135740)
    
    Hi Everyone,
    
    I've got Office Standard 2016 and when I opened it in Excel 2016 I still got the broken chart message. Not sure if it is a a 2016 update issue, as that is controlled by the Admins and it's only pushed out typically monthly if not a critical issue. I had been copying the steps so I had a working chart with some variances but was able to figure out my problems from looking at the download. Liked this part and moving on to 2 and 3 as my work allows me to work at 'em.
    
    [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1135740)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [February 24, 2016 at 3:54 pm](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1135755)
        
        Hmm.. I use standalone installation of Office 2016, but I am under the impression that O365 2016 versions are even more up to date (with newer features added frequently), so may be it was something else that caused the error.
        
        [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1135755)
        
7.  ![](https://secure.gravatar.com/avatar/5c1a1323dc09313975aec7dbfe5ef7035ef314e681397d2d55b67491fc00588d?s=64&d=mm&r=g) Mobilken says:
    
    [February 24, 2016 at 4:06 pm](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1135761)
    
    Chandoo,  
    I'm new to excel Pivot/BI. I have created the pivot table and slicers. what is meant
    
    Timeline on the Date Received -
    
    Thank you for your help and GREAT web site ,,,
    
    [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1135761)
    
8.  ![](https://secure.gravatar.com/avatar/00cced870c4d252c72674d70a107db1f067267f4a38eda3c3c8766c0dcf54f3d?s=64&d=mm&r=g) michael says:
    
    [May 12, 2017 at 8:12 pm](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1447955)
    
    Hi all. As an beginner/intermediate excel user I have been dipping in and out of Chandoo excel lessons and example downloads for the last year or so and have found both the lessons and examples invaluable. I cannot find any other site or group that provide such info and free examples. If your stuck and you need to get the right answer, it's the first place to go.
    
    Thanks Chandoo.
    
    [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1447955)
    
9.  ![](https://secure.gravatar.com/avatar/7493af2622bb828d8899a02c857bfa2710df4de6c4f8c59180ed284bc62d1487?s=64&d=mm&r=g) Marc says:
    
    [May 13, 2017 at 9:56 am](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1448123)
    
    Dear Chandoo,
    
    The negative comments here are sad but you should not be discouraged.I find your work fantastic and enriching. You do not have to apologize for any charges, it is up to everyone to decide to take it or not. Good work must be rewarded somehow and we all must make our living
    
    Top achievements, please procceed. I am delighted every time about the great ideas and solutions, you have helped me very much.
    
    Thanks Chandoo  
    Marc
    
    [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1448123)
    
10.  ![](https://secure.gravatar.com/avatar/717bb207f63e786657807b2b14d3236c63455885325b6295e585cec0c4c235cc?s=64&d=mm&r=g) shadreck says:
    
    [May 15, 2017 at 10:57 am](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1448852)
    
    Dear Chandoo  
    This has been awesome to me as I am new in excel.
    
    [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1448852)
    
11.  ![](https://secure.gravatar.com/avatar/46428e02f6af13a7340d11a209ffe736e9e19c92013fa4d8962ed8fae9ae742f?s=64&d=mm&r=g) Bob says:
    
    [May 15, 2017 at 8:06 pm](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1449273)
    
    Unfortunately, Excel does not handle massive data particularly well. I do extensive analysis on data like this daily. It is comprised of 20+ columns or fields, and upwards of 40,000 rows (complaints). There are over 100 different parts or possible failures and I add costs and dates and locations etc. I also calculate PPM (parts per million) so I pull a population under warranty which could be 270,000+ lines. As part of the analysis, I use a number of pivots, slicers, vlookups, links to other spreadsheets, and possibly several nested if/and formulas. It can nearly bring Excel to a standstill. This is not a negative comment, I appreciate your work, just saying Excel has its limitations.
    
    [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1449273)
    
12.  ![](https://secure.gravatar.com/avatar/c273134ff751ef45f76e61f91973ad12efccc3b77f9df1dc2bec97229a18f1ee?s=64&d=mm&r=g) [Kalyan Banga](http://fusionanalyticsworld.com/)
     says:
    
    [July 28, 2017 at 5:48 am](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1487219)
    
    Hi Chandoo,
    
    I am founder of Fusion Analytics World ([http://fusionanalyticsworld.com](http://fusionanalyticsworld.com/)
    ) , your materials are just amazing. I would like to invite you to feature in our top stories for month of August. If you can pen down an article on how to do analytics in excel since most believe they need to be great in R, Python etc undermining the value of excel and use in analytics. Let me know.
    
    Thank you,  
    Kalyan Banga
    
    [Reply](https://chandoo.org/wp/analyzing-consumer-complaints-1/#comment-1487219)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/analyzing-consumer-complaints-1/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ