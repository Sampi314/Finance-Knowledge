# Analyzing half a million complaints - Customer Satisfaction Scorecard [Part 3 of 3] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/customer-satisfaction-scorecard

---

*   [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

Analyzing half a million complaints – Customer Satisfaction Scorecard \[Part 3 of 3\]
=====================================================================================

*   Last updated on October 10, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

This is the final part of our series on _**how to analyze half a million customer complaints.**_ Click below links to read part 1 & 2.

1.  [Complaint reason analysis](http://chandoo.org/wp/2016/02/16/analyzing-consumer-complaints-1/)
     – Part 1
2.  [Regional trends & analysis](http://chandoo.org/wp/2016/02/18/analyzing-customer-complaints-2/)
     – Part 2

Customer satisfaction scorecard
-------------------------------

In the previous parts of this case study, we understood what kind of complaints were made and where they came from (states). For the customer satisfaction scorecard, let’s focus on individual companies.

![customer-satisfaction-scorecard-analysis-complaints-data](https://chandoo.org/wp/wp-content/uploads/2016/02/customer-satisfaction-scorecard-analysis-complaints-data.png)

### Gathering the data

As there are 3,946 companies in the data, we could end up making a ton of scorecards. So first step is to cull down the company list to a meaningful number. Let’s go with top 15 companies (which account for 61% of all complaints).

As we have data between 2011 to 2016, selecting top 15 companies based on grand total of complaints across all years may skew the names. So let’s select the top 15 companies by complaint count in 2015.

Using a simple pivot table, sorted by complaint count we can figure out the names.

_**But how do you filter the original data so only these 15 companies data remains?**_

We can use,

*   [Advanced Filters](https://chandoo.org/wp/how-to-use-advanced-filters/)
     (set up filter on top 15 company list and copy the filtered values to another location)
*   [Power Query](https://chandoo.org/wp/resources/introduction-to-power-query/)
    

I have used advanced filters to do the job. Once we have a new data set with just top 15 company data, let’s turn it in to a table named _top.15_

Also, as we have partial data for years 2011, 2012 and 2016, let’s use only 2013 to 2015 data for this analysis.

### Defining scorecard criteria

If we have access to data like how many customers each business had, how many products they sold, how many transactions the customers made in each month, we can combine that with complaint data to arrive at truly remarkable satisfaction score. Unfortunately, we don’t know have that kind of data. We only know about the complaints. So based on what we know, I have defined the below 5 criteria to measure customer satisfaction.

1.  **Nasty issue %:** Although there are 95 different issues about which customers complaint, not all of them are nasty. We could define a subset of complaints that are particularly nasty and measure what percentage they constitute. Example of nasty issues: _Incorrect information on credit report,_ _Cont’d attempts to collect debt not owed_ etc.
2.  **Frustration %:** Customers have a choice to add _narrative_ to their complaints. This is an option available only since 2015. Out of 91,399 complaints received by top 15 companies in 2015, only 25,482 complaints had this narrative (ie 28%). If we examine this free text narrative for words like _frustrated, bad, hate, disappointed etc._ we can calculate **frustration score.** 
3.  **YoY Complaint Growth:**  If a company is improving its complaint volume YoY (between 2013 to 2015), it is certainly worth investigating. One reason could be more customers are not happy with the company. _Other factors like adding new customers, change in compliance / regulations, more customers knowing about the complaint facility_ could contribute to complaint growth rate. As we don’t have the data about these _other factors_, let’s assume YoY complaint growth affects customer satisfaction rate.
4.  **Negative resolution %:** Each complaint has a resolution offered by the company. The resolutions are usually – Closed, Closed with explanation, Closed with monetary relief, Closed with non-monetary relief, In progress and Untimely response. Out of these 6 responses, we can consider a few to be negative resolutions and calculate what percentage of all resolutions are negative. For example any complaint that is **closed** without any explanation or relief can be considered negative resolution.
5.  **Disputed complaint %:** Customers have a choice to dispute the resolution offered by the company. If a customer disputes what the company says, it can be considered as a non favorable resolution. We can calculate what percentage of complaints are disputed and use it as a factor in calculating the customer satisfaction score.

### Weights & customization of the criteria:

In order to calculate the final customer satisfaction score, we need a few more things:

*   Weight for each criteria
*   Parameters for certain criteria (ie list of negative resolutions, list of nasty issues etc.)
*   **Benchmark for each criteria:** This can be used to set absolute minimum for each criteria. Any company scoring less than this will get a lower overall rating.

We can define all these in a _settings worksheet_ so that our scorecard is dynamic.

### Calculating satisfaction criteria

This is where things get tricky. I have summarized the calculation techniques below. For more, you need to examine the downloadable workbook. You need to also read about array formulas, pivot tables, weighted averages and text formulas.

**Nasty Issue %:**

*   First we set up a [pivot table](http://chandoo.org/wp/2009/08/19/excel-pivot-tables-tutorial/)
     of complaint count by year, company & issue.
*   We also set up a table with list of nasty issues.
*   We then use an array SUM formula to calculate the total count of nasty issues in the pivot table for each company in each year.

**Frustration %:**

*   We define a list of negative words.
*   Then for each company, we calculate how many complaint narratives had the given negative word in the year of 2015.
*   For this we use **COUNTIFS formula with wildcards.**
*   We calculate total complaints with any narrative and then figure out the frustration %.

**YoY complaint growth:** 

*   This is easy. We just look at the yearly complaint numbers for each company and figure out how many YoY growths the company had.

**Negative resolution %:** 

*   Set up a pivot table of complaint count by year, company and resolution.
*   We define a list of negative resolutions too.
*   Then calculate how many complaints had negative resolutions using array SUM formula

**Dispute %:**

*   Using a COUNTIFS formula, we calculate how many complaints had \[Consumer Disputed?\]=”Yes” for a given year & company combination.

**Calculating the final satisfaction score**

Now that all of the individual components are calculated, we need to calculate one final score (out of 10).

For this we need to:

*   Calculate PERCENTRANK for each factor among all the top 15 companies. This will give you a percentage (0 to 100%).
*   We then weight each factor by the weightage assigned to them
*   We then add up all these weighted factors and multiply by 10 to get a number from 0 to 10.
*   This is the final satisfaction score of each company.

Designing the scorecard
-----------------------

For the scorecard, let’s go with the theme of _My bank vs. Your bank._ This will allow us to compare 2 companies at a time and understand their customer satisfaction scores along with few other details.

Apart from the score, rank, break-up by criteria, let’s also add:

*   Summary of complaints – 2015 count, 3 year trend, 12 month trend.
*   Complaints by state heatmap
*   Complaint mode summary

We can use COUNTIFS formula to calculate the complaint totals by state & mode.

**Few other things that need:**

*   Selection of two companies [using combo box form control](http://chandoo.org/wp/2011/03/30/form-controls/#combo-box)
    .
*   Annual & monthly complaint trend [using sparklines](http://chandoo.org/wp/2010/05/18/excel-sparklines-tutorial/)
    .
*   State level complaints [using conditional formatting heatmaps](http://chandoo.org/wp/2010/01/22/flu-trends-chart-in-excel/)
     & [picture links](http://chandoo.org/wp/2010/10/19/how-to-use-picture-links/)
    .
*   Complaint mode summary using conditional formatting data bars

Customer Satisfaction Scorecard
-------------------------------

Here is the final version of the scorecard.

![statisfaction-scorecard-customer-complaints-v2](https://chandoo.org/wp/wp-content/uploads/2016/02/statisfaction-scorecard-customer-complaints-v2.png)

### Quick video demo of the scorecard

Check out a quick demo & explanation of the scorecard below. You can also see this on our YouTube channel.

Download Satisfaction Scorecard workbook
----------------------------------------

[**Click here to download customer satisfaction scorecard workbook**](https://files.chandoo.org/50w/consumer-complaints-vis-3.xlsx)
. Play with the form controls, modify the settings, examine the calculations & pivots to learn more.

**Note:** this file is 55 MB. So give it a few minutes to download.

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

*   [13 Comments](https://chandoo.org/wp/customer-satisfaction-scorecard/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/customer-satisfaction-scorecard/#respond)
    
*   Tagged under [50 ways course](https://chandoo.org/wp/tag/50-ways-course/)
    , [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [advanced filters](https://chandoo.org/wp/tag/advanced-filters/)
    , [array formulas](https://chandoo.org/wp/tag/array-formulas/)
    , [charting](https://chandoo.org/wp/tag/charting/)
    , [countifs](https://chandoo.org/wp/tag/countifs/)
    , [dashboards](https://chandoo.org/wp/tag/dashboards/)
    , [data bars](https://chandoo.org/wp/tag/data-bars/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [heatmaps](https://chandoo.org/wp/tag/heatmaps/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Microsoft Excel Conditional Formatting](https://chandoo.org/wp/tag/conditional-formatting/)
    , [no ads](https://chandoo.org/wp/tag/no-ads/)
    , [no-nl](https://chandoo.org/wp/tag/no-nl/)
    , [percentrank](https://chandoo.org/wp/tag/percentrank/)
    , [pivot tables](https://chandoo.org/wp/tag/pivot-tables/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Cool Infographics & Data Visualizations](https://chandoo.org/wp/category/cool-infographics/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousAnalyzing half a million customer complaints – Regional Trends \[Part 2 of 3\]](https://chandoo.org/wp/analyzing-customer-complaints-2/)

[NextAutosum many ranges quickly with Multi-select & ALT= \[quick tip\]Next](https://chandoo.org/wp/autosum-quickly-with-multi-select/)

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
    

### 13 Responses to “Analyzing half a million complaints – Customer Satisfaction Scorecard \[Part 3 of 3\]”

1.  ![](https://secure.gravatar.com/avatar/d4eb401143b7857d8366d729fddf69e94135f5c8ac6faa5b0dcb07cea9cc805d?s=64&d=mm&r=g) Ardraaken says:
    
    [February 23, 2016 at 10:54 am](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135479)
    
    Thanks Chandoo, another great tutorial.
    
    I was particularly interested in the text analysis and the way you did this.
    
    I looked at sentiment analysis using my fairly basic VBA knowledge a while ago and created a UDF to calculate a satisfaction score based on analyising all the words in the sentence. I found a list of positive and negative words online and used these as my lookup lists with positive scores for good words and negative scores for bad words. I also analysed the preceeding two words when I found a match to see if one of the words increased the sentiment (e.g. words like 'very' and 'extremely') and if the words flipped the sentiment (e.g. 'not' bad = good). Due to the large list of words populating the document it's not exactly portable but it worked okay (although it doesn't deal well with sarcasm!).
    
    [Reply](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135479)
    
2.  ![](https://secure.gravatar.com/avatar/9d7c263689445fd2fb04deb594a79be6843ab7de903a053a98fd165d37ca7b40?s=64&d=mm&r=g) PhilC says:
    
    [February 23, 2016 at 9:11 pm](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135561)
    
    Hi, wondering why in the Summary of Complaints section the 2015 Count is formatted the way it is? Typo or valid reason?
    
    [Reply](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135561)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [February 24, 2016 at 3:47 am](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135635)
        
        No typo. As I could not fit the full number in column, I formatted it in thousands.
        
        [Reply](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135635)
        
3.  ![](https://secure.gravatar.com/avatar/97bfe6f2cc55d184b6142c9892fe63c0648b2b67838f85d435efdb20c16c67f2?s=64&d=mm&r=g) Joe Thompson says:
    
    [February 23, 2016 at 11:45 pm](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135590)
    
    Awesome stuff! Is there a single file (pdf, for example) with the text of the 3 parts available?
    
    [Reply](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135590)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [February 24, 2016 at 3:45 am](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135634)
        
        Not yet Joe. I plan to give single PDF along with additional commentary and companion videos as part of the 50 ways program course content.
        
        [Reply](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135634)
        
4.  ![](https://secure.gravatar.com/avatar/bdb6d30271376ebd28124c2eaa5a511234e80d7767099a9f3b9b199212034177?s=64&d=mm&r=g) Mayur Gijam says:
    
    [February 24, 2016 at 2:57 pm](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135744)
    
    Hi I am wondering how you guys can keep inspiring with the knowledge you have 🙂  
    I have one small question, In Pivot tabs how the Row Labels for Year Received are duplicated as in I know from Field Setting we can set Show item Labels in tabular form but It couldn't duplicate them down. I tried hell out me but couldn't reflect the exact pivot that you guys have created. I use Excel 2007. Can you please tell me 🙂
    
    [Reply](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135744)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [February 24, 2016 at 3:55 pm](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135757)
        
        I no longer have Excel 2007 or 2010 on my work computers to test, but I am using a feature called "repeat row labels" in pivot design ribbon. May be it was added in 2010...?
        
        [Reply](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135757)
        
        *   ![](https://secure.gravatar.com/avatar/bdb6d30271376ebd28124c2eaa5a511234e80d7767099a9f3b9b199212034177?s=64&d=mm&r=g) Mayur Gijam says:
            
            [February 25, 2016 at 11:09 am](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135950)
            
            Thanks alot for your comment... You are awesome as always 🙂
            
            [Reply](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135950)
            
5.  ![](https://secure.gravatar.com/avatar/23805f122dac5452d1f806a5fc607bc679908e5b202137f8d23a95777804292d?s=64&d=mm&r=g) Prasad says:
    
    [February 25, 2016 at 12:50 pm](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135968)
    
    After saw your excel file understand that, How better we can use the formula to get better result.
    
    countifs with finding disappointing count.  
    In Heatmap sheet using name bring company name Dynamic  
    Index formula with conditional formatting
    
    really awesome, this make me to feel associate with you always. If I get changes to work along with you, that will be great.
    
    [Reply](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1135968)
    
6.  ![](https://secure.gravatar.com/avatar/97bfe6f2cc55d184b6142c9892fe63c0648b2b67838f85d435efdb20c16c67f2?s=64&d=mm&r=g) Joe Thompson says:
    
    [February 27, 2016 at 6:05 pm](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1136524)
    
    Can you explain why the benchmark is included in the percentile ranking formula? In other words, why is Calc!I76 =PERCENTRANK.INC(C$76:C$92,C76) and not =PERCENTRANK.INC(C$76:C$90,C76)?
    
    [Reply](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1136524)
    
7.  ![](https://secure.gravatar.com/avatar/2234e3f2755af2fd4279fb77c8dede1578c94875dbbffbc4be9d06a3c8b94d62?s=64&d=mm&r=g) Cap D says:
    
    [March 31, 2016 at 6:49 am](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1160389)
    
    .God Bless You Chandoo!
    
    [Reply](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1160389)
    
8.  ![](https://secure.gravatar.com/avatar/5320370651c2676fb0950c340e70ae3e57819fe717e7488634cd058385be9b17?s=64&d=mm&r=g) [Lucinda](http://www.gambling2.com/)
     says:
    
    [January 23, 2019 at 10:42 am](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1616196)
    
    After a few years, once the succeeding consequences  
    were over, we halted collectively.
    
    [Reply](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1616196)
    
9.  ![](https://secure.gravatar.com/avatar/a067c23bc824d386efb917bfa7884008556542c2720369207753d4098706bd76?s=64&d=mm&r=g) Elizabeth says:
    
    [March 16, 2021 at 6:15 am](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1982033)
    
    Love this website. I am wondering how these types of  
    dashboards can be used in court hearings to help the judge visualize how one person is telling the truth (based on evidence) and how another person is lying (based on forged evidence, how many times they filed  
    Frivolous court motions, changing statements they made at different hearings based on transcript, etc. I would probably have to add calendars or timelines?
    
    [Reply](https://chandoo.org/wp/customer-satisfaction-scorecard/#comment-1982033)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/customer-satisfaction-scorecard/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ