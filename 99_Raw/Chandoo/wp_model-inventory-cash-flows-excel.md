# Modelling Inventory Run Rate & Cash Flows using Excel » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/model-inventory-cash-flows-excel

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

Modelling Inventory Run Rate & Cash Flows using Excel
=====================================================

*   Last updated: April 2017

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Imagine you run an office furniture company.** You want to stop reordering two brands of furniture – Relaxer (a type of chair) and Boca Top (a type of table). You currently have 20,000 Relaxer chairs and 5,000 Boca Tops. These are valued at $200,000 and $100,000 respectively. When sold, they will yield $100,000 and $25,000 gross profit. You are hoping to sell them off in 2 or 3 years. You forecast that we can sell off these as per below.

![yearly-sales-splits](https://chandoo.org/wp/wp-content/uploads/2017/04/yearly-sales-splits.png)

You need to analyze this and prepare a cash flow model.

**Let’s learn how to answer such open ended questions using various analysis techniques in Excel**.

_The case in this article is based on a [forum question](http://forum.chandoo.org/threads/what-if-analysis-scenario-manager-goal-seek-or-data-table.33881/#post-201464)
 by Proteus._

Setting up the problem
----------------------

Most business case problems will have following three kinds of parameters

*   Fixed Inputs – for example opening stock of chairs & tables, book value of these items
*   Variables – Number of chairs and tables sold every month (or year), profit expectation
*   Assumptions – We will be able to sell off all the items (ie no write offs), Profit per unit and book value per unit doesn’t change over time

_Of course, these three categories can overlap_. Use your experience and industry knowledge to define what items belong where.

### _Why bother – can’t everything be a variable?_

Of course, you can consider everything to be a variable in your model. This will give maximum flexibility, but comes with a lot of cost. Your model becomes complicated and can take a lot of time to develop. It might be overkill, so identify a few constants (fixed inputs).

Once your model is in Excel, all input cells can be edited. So _technically_ all are variables.

Define outputs
--------------

The next step is to identify outputs. In this case, we can calculate three kinds of outputs.

*   Number of chairs & tables sold by month
*   Revenue by month
*   Profit by month

We can add an optional output – **_visualization of the results._**

### How to go from inputs to outputs

This is where we figure out the business rules and calculation logic to arrive at outputs from inputs.

Let’s define formulas for each output

*   Units sold per month = this year’s portion of total stock / 12
*   Revenue per month = units sold per month \* book value per unit
*   Profit per month = units per month \* profit per unit

Initial Model
-------------

Set up the input area like below. The orange cells contain user inputs. Gray ones have calculated values.

![initial-model-inputs](https://chandoo.org/wp/wp-content/uploads/2017/04/initial-model-inputs.png)

Everything in the above picture is self-explanatory, so let’s move on to output section.

_Note:_ If your business problem is complex, you need to setup dedicated worksheets for each type of input (fixed, variable and assumption). This will let you play with various combinations and control outputs in a better way.

### Calculating outputs

The tricky part is figuring out units of chairs & tables sold per month. Once we have these numbers, calculating revenue & profit per month is easy.

**Let’s run the outputs for 60 months.** Although your initial estimates suggest that all stock will be sold in first 3 years, this allows you to monitor cash flows over 5 years, should there be a change in the inputs.

Let’s say month numbers are in column G, from G6 to G65.

Given,

*   the month number in G6
*   Yearly chair volume in range C$19:C$23

_Refer to inputs picture in above section for cell references._

We can calculate number of chairs sold in that month using below formula (call it formula 1)

1.  Units of chairs per month (cell H6) =INDEX(C$19:C$23,INT(($G6-1)/12)+1)/12

**How does this formula work?**

Simple, we pick the volume for year represented by month using INDEX formula. To calculate year from month (G6), we use simple arithmetic: INT(($G6-1)/12) + 1

Once yearly volume is picked, we just divide it by 12 to get monthly volume (ie units sold per month).

Notice the mixed referencing style used, this will help you drag and reuse the same formula for calculating table volume.

The calculated volume figures go in to columns H & I.

### Calculating Revenue, Profit & Total Profit

Now that we know units sold per month, calculating remaining three outputs is easy.

2.  Revenue of chairs (cell J6) = H6 \* C$8 _(Note: C$8 has the book value per chair)_
3.  Profit of chairs (cell L6) = H6 \* C$11
4.  Total Profit (cell N6) = L6 + M6

**Refer to below diagram to see sample results along with formula numbers.**

![model-outputs-and-formulas](https://chandoo.org/wp/wp-content/uploads/2017/04/model-outputs-and-formulas.png)

Let’s add scenarios to this model
---------------------------------

Our initial model is a simple formula driven tabulation of results. **But what if you want to see profit flow by different scenarios?** May be the initial yearly forecasts by marketing department are too optimistic and you want to see what happens if we sell fewer chairs in first year.

Let’s **assume  we have 10 such scenarios** and for each scenario, you want to define below inputs:

*   Profit per unit
*   Yearly breakdown of volumes for 5 years

This means, we have a total of 12 inputs per scenario (6 for tables and 6 for chairs)

### Set up scenario table like this in the spreadsheet:

![scenarios-for-model](https://chandoo.org/wp/wp-content/uploads/2017/04/scenarios-for-model.png)

Now that we have scenarios to define some of our inputs, let’s plug in scenario number in to input section, as shown below.

![using-scenario-to-drive-calculations](https://chandoo.org/wp/wp-content/uploads/2017/04/using-scenario-to-drive-calculations.png)

### Calculating Total Profit for each scenario

This is when we unleash the beast – [**Data Tables**](http://chandoo.org/wp/2010/05/06/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/)
. Using data tables, we can quickly calculate total monthly profit for each of the 10 + 1 scenarios.

**Set up an empty scenario grid** as shown below.

![empty-scenario-grid](https://chandoo.org/wp/wp-content/uploads/2017/04/empty-scenario-grid-v1.png)

Make sure first column refers to the monthly total profit calculated in column N (N6:N65) in our initial model. Once such a grid is setup, use below steps to calculate profit under each scenario.

![data-table-to-analyze-all-scenarios-in-one-go](https://chandoo.org/wp/wp-content/uploads/2017/04/data-table-to-analyze-all-scenarios-in-one-go.png)

1.  Select entire grid including first column (referenced one) and headers.
2.  Go to Data > What if analysis > Data tables
3.  Select Row input cell and point to scenario name in input area (cell C25 in my model).
4.  Click ok.
5.  Wham!!! Excel calculates profit for each of the 11 scenarios for all 60 months (total 660 values calculated before you could say six sixty 🙂 )

### That’s a lot of numbers, how to make sense?

While scenario based modeling is good, it presents a new challenge. How do you make sense of all this new data? Simple, make a chart.

There are many ways to visualize this data. Here is one:

![scenarios-visualized](https://chandoo.org/wp/wp-content/uploads/2017/04/scenarios-visualized.png)

I have visualized only first 5 scenarios (original + 4 more). You can change this depending on what each scenario represents.

Related: [**Introduction to Data Tables in Excel**](http://chandoo.org/wp/2010/05/06/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/)

Model 2 – What if we don’t sell same volume every month
-------------------------------------------------------

Now we all know that no business sells same volume every month. You will have a few high months and few low ones. So **how to add monthly variations to the model?**

Let’s say you have monthly % splits for Relaxer and Boca Top defined in range as shown below:

![monthly-splits](https://chandoo.org/wp/wp-content/uploads/2017/04/monthly-splits.png)

We can plug this new information in to our model by altering formula 1 (units per month). Everything else will work nicely once formula 1 is fixed.

Here is the new formula 1 (units per month). Figuring out how it works is your homework.

\=INDEX(C$19:C$23,INT(($G6-1)/12)+1) \* INDEX(C$30:C$41,MOD($G6-1,12)+1)

Please note:

*   C$19:C$23 has yearly volume for Relaxer
*   G6 has month number
*   C$30:C$41 has monthly % split for Relaxer

Once you alter formula 1, you can see how it effects the cash flow (revenues & profits per month) over 5 years.

Model 3 – What if we don’t know how much we can sell each year
--------------------------------------------------------------

You can buy a broomstick from Quality Broomstick Supplies in Diagon Alley before you can _accurately_ figure out how much you will sell each year. It is almost impossible.

But our entire model depends on this input. **What if we don’t know the yearly volumes?**

May be we can assume first month volume & monthly variations (as defined in Model 2 above)  and figure out yearly volumes. Since first month volume is a variable, we can alter it to see what kind of cash flow it would produce.

_**Something like this:**_

![cashflow-vis-model-3](https://chandoo.org/wp/wp-content/uploads/2017/04/cashflow-vis-model-3.gif)

### **Setting up a starting month based forecast model**

Let’s say we know first month volumes for Relaxer & Boca Top – Cells C43& D43 respectively.

We can calculate forecast in a few ways:

1.  We can calculate yearly volume by multiplying Q21 with first month’s percentage (as defined in Model 2)
2.  We can calculate successive month volumes by increasing / decreasing first month’s volume by monthly % changes (this requires new inputs)
3.  We can simulate monthly volumes by randomly varying first month’s number while following some sort of monthly split pattern

2 & 3 require new inputs or data tables to be set up. Since we have already beaten this problem to death, let’s just stick to approach 1.

We calculate yearly volumes by using simple formulas like this:

1.  Year 1 (cell C19) =MIN(C43/C28, C$6) (C43 has first month volume and C28 has first month %)
2.  Year 2 on wards:  =MIN(C$19,C$6-SUM(C$19:C19))  
    Note: C6 has total stock of Relaxer. We can only sell if there is any stock left. If first month volume is too high, then we may end up selling out quickly.

Once these volumes are calculated, we just visualize results (monthly profit columns L & M) in a line chart.

**If you link inputs C43 & D43 with two separate scrollbar form controls,** you can play with them in the chart and quickly analyze the results. _Now that is pretty cool._

_Related:_ [Introduction to Excel form controls](http://chandoo.org/wp/2011/03/30/form-controls/)
 | [Using scrollbar form control in Excel Models](http://chandoo.org/wp/2010/01/20/mortgage-payment-calculator/)

Download workbook with all models
---------------------------------

**[Click here to download Excel Workbook](https://chandoo.org/wp/wp-content/uploads/2017/04/chairs-tables.xlsx)** containing all the models discussed so far. Play with them or create your own models to analyze the problem. Learn and flourish.

50 more ways to analyze data like a rock star
---------------------------------------------

_**If you like this,**_ you are going to love my upcoming new course – **50 ways to analyze data.** Learn best ways to analyze any kind of data along with a deep dive in to advanced Excel features and case studies in this online class. Check out our [**50 ways to analyze data program**](http://chandoo.org/wp/resources/50-ways-to-analyze-data/)
. We are opening enrollments in First week of May 2017. Click below button to sign up to course waiting list and know more about the program.

[![50-ways-program-know-more](https://assets.chandoo.org/wp/wp-content/uploads/2016/09/50-ways-program-know-more.png)](http://chandoo.org/wp/resources/50-ways-to-analyze-data/)

Share on FB

Tweet this

Post to LinkedIn

![](https://chandoo.org/wp/wp-content/uploads/2019/12/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

*   [9 Comments](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/model-inventory-cash-flows-excel/#respond)
    
*   Tagged under [charting](https://chandoo.org/wp/tag/charting/)
    , [data tables](https://chandoo.org/wp/tag/data-tables/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [dynamic charts](https://chandoo.org/wp/tag/dynamic-charts/)
    , [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)
    , [form controls](https://chandoo.org/wp/tag/form-controls/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [modeling](https://chandoo.org/wp/tag/modeling/)
    , [multiway data tables](https://chandoo.org/wp/tag/multiway-data-tables/)
    , [scenarios](https://chandoo.org/wp/tag/scenarios/)
    , [screencasts](https://chandoo.org/wp/tag/screencasts/)
    , [Scroll Bar](https://chandoo.org/wp/tag/scroll-bar/)
    , [solo](https://chandoo.org/wp/tag/solo/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    

[PrevPreviousThere are 5 hidden cells in this workbook – Find them all \[Excel Easter Eggs\]](https://chandoo.org/wp/easter-eggs-2017/)

[NextRelative References in Excel TablesNext](https://chandoo.org/wp/relative-references-in-excel-tables/)

### 9 Responses to “Modelling Inventory Run Rate & Cash Flows using Excel”

1.  ![](https://secure.gravatar.com/avatar/99cfb77d41f7bf3013d5c38baf5aa34923e7dd079e2082ca088f079dc803227f?s=64&d=mm&r=g) [John](http://www.howtoexcel.org/)
     says:
    
    [April 19, 2017 at 12:20 pm](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1438467)
    
    Good read 🙂
    
    [Reply](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1438467)
    
2.  ![](https://secure.gravatar.com/avatar/bca2f78172d8aa56736d9f1b47d3cf2459e08bf013312a15010ef64b54e5e965?s=64&d=mm&r=g) Anant says:
    
    [April 20, 2017 at 3:18 am](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1438594)
    
    Very Interesting.
    
    [Reply](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1438594)
    
3.  ![](https://secure.gravatar.com/avatar/f166ef1af5eda3eeda12d9dcca489d90e77638ee2dbfd6c9eb064cdbcc0d8074?s=64&d=mm&r=g) [Achyutanand khuntia](http://www.chandoo.org/)
     says:
    
    [April 20, 2017 at 6:21 am](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1438618)
    
    Thank You, this idea is So Much interesting
    
    [Reply](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1438618)
    
4.  ![](https://secure.gravatar.com/avatar/16fa5e072a320bb54524053a92ee9da7749f197bbb21e531627d83da2e392bc7?s=64&d=mm&r=g) Uvasan G says:
    
    [April 20, 2017 at 7:39 am](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1438635)
    
    Brilliant Chandoo!!  
    Thank you for sharing.
    
    [Reply](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1438635)
    
5.  [#Excel Super Links #17 – shared by David Hager | Excel For You](https://dhexcel1.wordpress.com/2017/04/28/excel-super-links-17-shared-by-david-hager/)
     says:
    
    [April 28, 2017 at 4:19 pm](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1441070)
    
    \[…\] [http://chandoo.org/wp/2017/04/19/model-inventory-cash-flows-excel/](http://chandoo.org/wp/2017/04/19/model-inventory-cash-flows-excel/)
     \[…\]
    
    [Reply](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1441070)
    
6.  ![](https://secure.gravatar.com/avatar/948fdac53d8f72bc7f7b8cc94d0697e9d7fa99a1f6a9d0a2d5339f80f7095960?s=64&d=mm&r=g) samdthompson says:
    
    [May 4, 2017 at 8:25 pm](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1442679)
    
    Good model, I would suggest two enhancements:  
    1\. a cumulative profit line so we could see a breakeven point  
    2\. an option 4 where can define a assumption of stock minimum stock stock unsold. This would mean that a slow start month to sales would not necessarily mean a slow 5 years. its sort of a mixture of model 2 and 3.  
    Cheers,  
    Sam
    
    [Reply](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1442679)
    
7.  ![](https://secure.gravatar.com/avatar/285703803e7dd42f96b4525eaf9e80c6833a18c9ae61954e5c01c5abacfaf40b?s=64&d=mm&r=g) [Patrick](http://www.pvinfo.com.br/)
     says:
    
    [May 5, 2017 at 10:59 am](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1443316)
    
    Great!!!
    
    [Reply](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1443316)
    
8.  ![](https://secure.gravatar.com/avatar/fa9af5488c268a6dd1fe9cbcb4034f932f28236d5112e26bf93f20ac0fcb505b?s=64&d=mm&r=g) Uche Uche says:
    
    [July 19, 2017 at 4:14 pm](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1482426)
    
    I am a bit confused when reading the statement,"Now that we have scenarios to define some of our inputs, let’s plug in scenario number in to input section, as shown below."  
    It presented, “Formulas to calculate these inputs from scenario number in C26:” I wonder where Cells Q6:Q16; R6V16 comes from because they were not shown in the displayed worksheet used
    
    [Reply](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1482426)
    
9.  ![](https://secure.gravatar.com/avatar/426e532685449d5f5b372f5db3b5af86f1a292c71c9d435803a9093d91fe28d6?s=64&d=mm&r=g) doug says:
    
    [November 9, 2017 at 11:54 pm](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1521618)
    
    Hullo.  
    Very interesting! Thanks.
    
    [Reply](https://chandoo.org/wp/model-inventory-cash-flows-excel/#comment-1521618)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/model-inventory-cash-flows-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ