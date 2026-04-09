# How to predict cricket scores [Excel + Machine Learning] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/predict-cricket-scores-excel-ml

---

*   [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

How to predict cricket scores \[Excel + Machine Learning\]
==========================================================

*   Last updated on July 7, 2019

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**_Can we predict cricket match score in Excel?_** Using machine learning, ensemble modeling, multiple regression and Excel formulas we can. This tutorial explains how.

Cricket world cup is on. Both my homes (India & New Zealand) have done well so far in the tournament and if things go OK in the last couple of matches, they should qualify for semi-finals. The games are happening in UK, which is 12 hours behind New Zealand. You know that means?

![Sleepless in wellington - watching cricket matches](https://chandoo.org/wp/wp-content/uploads/2019/07/sleepless-in-wellington.png)

_Yes, lots of sleepless nights in Wellington._

As I watch these games, I notice that every once in a while they show a “**score predictor**“. It will tell you what the final score could be based on the proceedings of the game so far.

So I thought, hmm, May be I should make one of those in Excel?

That is what I did. I created a machine learning model in Excel to predict cricket score. Sounds interesting? Read on.

_Cricket?!? What now?_
----------------------

_If you are thinking “the only cricket that keeps me up all night is the damned chirping one in my basement”, then don’t worry._ You need very little knowledge of cricket to understand the techniques. Once you know the ideas you can apply them to many other real life problems like predicting sales next year or student absences next term or electricity usage in the new plant.

Defining the problem – Cricket Score Prediction
-----------------------------------------------

Just a quick note if you are not familiar with cricket. In a typical one-day match, two sides compete. The game starts with one of teams batting first and scoring some runs in 50 overs. The next team then tries to beat that target set by first team in 50 overs.

Let’s start by defining the problem. We want to create a cricket score predictor that takes the inputs:

*   Country playing – C
*   Runs scored so far in the match – Rs
*   Wickets remaining in the match – WR
*   Overs remaining – OR

Our predictor should tell us what could be the final score at end of 50 overs.

**For example,** we could ask, “Australia scored 52 runs in 10 overs losing 1 wicket. What would be the final score?” and our predictor can provide a guess – _say 305 runs_.

### Things we ignore:

The final score of a team in a cricket match depends on many things, including:

*   The playing team and their batsmen
*   The opposition team and their bowlers, fielders
*   The ground and pitch they play on
*   The weather and historical weather
*   Crowd attending the game and how much they are cheering
*   What the umpires had for lunch
*   etc.

If we try to incorporate every little thing that matters, we will never be able to construct our prediction model. So let’s ignore everything except those 4 parameters (C, Rs, Wr, Or) listed above.

Our model as an equation
------------------------

Let’s say **Rp denotes our predicted Runs**. We can define Rp as

Rp = p(C, Rs, Wr, Or)

where

*   C = Country
*   Rs = Runs already scored
*   Wr = Wickets Remaining
*   Or = Overs Remaining
*   p is a prediction function that does some magic to calculate Rp

**But we know that Rp = Rs +** _**something**_

This is because total runs at the end of 50 overs will be _something_ more than Runs Scored at the time of prediction.

If we can find _something_ our problem is solved. But how?

### Introducing Run Rate

Run rate is ratio between runs scored and overs completed. So if India scores 342 runs in 50 overs, their run rate is **6.84**. As our prediction model is for 50 overs, if we know the Run Rate, we will know final score.

Let’s define few more variables.

*   Os (Overs so far) = 50 – Or
*   RRs (Run Rate so far) = Rs / (50-Or)
*   RRr (Run Rate for remaining overs) – _this should be predicted_

Given these variables, we can rewrite Rp (Runs predicted) as

*   Rp (Runs Predicted) = Rs + Or \* **RRr**

So if we can build a model to predict RRr, we can calculate Predicted score.

We can argue that Run Rate in remaining overs will be a function of (country, run rate so far, overs remaining, wickets remaining)

RRr = f(C, RRs, Wr, Or)

Creating country specific prediction functions
----------------------------------------------

We can further argue that each country has specific strengths and abilities when it comes to batting. So, if we define a set of functions, f1(), f2()…, fn() where fn is

RRr for country n = fn(RRs, Wr, Or)

We can then call the relevant function based on which country we are predicting the score for.

So what is this magical prediction function?
--------------------------------------------

_Regression of course._ There are many sophisticated machine learning algorithms. But for something straight forward like Run Rate (remaining overs), we can create a simple multiple regression model.

Say RRr can be written as

RRr = m1\*RRs + m2\*Wr + m3\*Or + _const_

Given a set of training data with RRs, Wr, Or and RRr, we can use LINEST() function in Excel to calculate {m1, m2, m3, const} that fits the sample data. Once we have the multipliers and constant value for each country, we can predict the score for any situation. Its that simple.

Why just one equation per country? Why not more?
------------------------------------------------

As with everything else in life, cricket matches too have significant variability. For that reason, rather than one regression model per country, why not create 10 of them per country and the average the prediction?

As management consultants say,

> “When you are not sure what to say, just run a survey and tell them what they said.”

If this sounds like a bunch of bs, don’t worry. This is an actual machine learning technique known as **Ensemble Modeling**.

Ensemble Modeling
-----------------

The idea of ensemble modeling is simple. We build multiple models from the training data and then combine the results of all models when making predictions.

See this picture to understand how a typical Ensemble Model works.

![Ensemble modeling - illustration](https://chandoo.org/wp/wp-content/uploads/2019/07/how-ensemble-modeling-works.png)

This way, we can create more variation in input scenarios and create a robust model.

For the sake of simplicity, let’s say we want to build 10 regression models for each country.

**How to aggregate the ensemble model results?**

We will end up with 10 predicted Run Rates (Remaining overs). We can simply average these 10 to come up with final prediction. You can also assign weights to the models and do a weighted average. Let’s stick with simple average.

Let’s get building then.

Machine Learning 101
--------------------

**Learn first, Predict next**.

That’s it. But if you want more text, here we go. Almost all machine learning models follow this pattern. They look at some data to construct the model. Once that model is ready, we then test it on a _different_ data set to see how satisfactorily it performs. If the results are not up to scratch, we back to step one and fine tune the model.

The easiest of all these is a regression model. That is the same one we will be using too.

Where is the data?
------------------

There are many fine websites for finding current score or recent match results. But in order to train our model, we need a collection of historical match data by each over. This is notoriously hard to get. Thankfully, there is [cricksheet](https://cricsheet.org/)
. They have historical one day match data at ball by ball level for 1,400 + matches in CSV format. ([here is the downloads page](https://cricsheet.org/downloads/)
)

**_Note about data:_** I noticed that cricsheet doesn’t have all matches data. For example I could not find any 2018 games in the data set I downloaded few days ago. It doesn’t really matter as we are using a large sample of data spanning several years.

As you can see, this data is at a too detailed level than what we need.

**So I used Power Query to combine 1,400 files**, reshape the data to over by over scores and then calculate total score, overs and wickets at every 5 over interval until end of the game. I then took only the recent 300 games as very old performances have little impact on current scoring patterns.

_Sorry for not explaining the Power Query or Excel formula steps. That would get too technical and this post will never end._

Once reshaped, my data looks like this:

![training data for cricket score prediction model](https://chandoo.org/wp/wp-content/uploads/2019/07/input-training-data-cricket-score-prediction-model.png)

We can then derive additional columns,

1.  Last over of the game: =MAXIFS(\[Over\], \[Source.Name\],\[@\[Source.Name\]\], \[Country\], \[@Country\])
2.  **RRs –** Run Rate so far: =\[@\[Cum Runs\]\]/\[@Over\]
3.  **Or –** Overs Remaining: =\[@\[Max Over?\]\]-\[@Over\]
4.  **Wr –** Wickets Remaining: =10-\[@\[Cum Wickets\]\]
5.  Score at end: =SUMIFS formula
6.  **RRr** – Run Rate (remaining overs)  
    \=(\[@\[Score at end\]\]-\[@\[Cum Runs\]\]) / \[@\[Overs Remaining\]\]

Using 2,3,4 & 6 we can create our regression models.

But before we go there, let’s split the data in to training & test data sets. For this example, I choose the latest 50 games as test data set and everything older as training data. Instead of creating two separate tables, I just added a column at the end to look at \[Match ID\] to tell me whether something is test or training.

**Also, we do not need to use last over data for training.** At the end of game there is nothing left to predict, so there is no point of using last over data when training the model.

I have added a data point ID as column to this table so I can uniquely identify all data points when sampling training data. It is \[Data point number\]

Bagging & Bootstrapping
-----------------------

Don’t freak out. We are still on topic. Bagging is the _technical term_ for the concept of randomly sampling data, building models and then aggregating (ie bagging) at the end.

Bootstrapping refers to random sampling of data.

Our bootstrap approach is rather simple and naive.

*   For each country, we want 10 bags – 10 data sets
*   For each data set, we want a random sample of 50 data points
*   We then create a multiple regression model to fit  
    RRr = m1\*RRs + m2\*Wr + m3\*Or + _**const**_
*   We average all 10 model results when predicting outcomes.

**A note on const:** When I was building my cricket score prediction models, I realized that setting const=0 gave me a better R2 (ie the model fits well with training data). So I set the 3rd parameter of LINEST() to FALSE (ie no need for _const_). You may want to keep it on for other types of models.

In my training data from cricsheet, we have 16 countries. That means we need 16\*10\*50 = 8,000 data points to construct the models.

Using a bunch of RANDBETWEEN, INDEX+MATCH and COUNTIFS, I was able to construct this grid.

![ensemble model - input data](https://chandoo.org/wp/wp-content/uploads/2019/07/random-data-sampling-for-ensemble-model.png)

Constructing Multiple Regression Models
---------------------------------------

Once data grid is ready, we can create a bunch of LINEST() formulas to tell us the multipliers (m1, m2, m3) for each model. This can be done 160 times (each of the 16 countries need 10 models). But I am very lazy. So I used INDEX() formula to fetch arrays of 50 cells so that LINEST results can be tabulated nicely. This is how our multiple regression model looks:

![sample results from multiple regression - cricket score prediction](https://chandoo.org/wp/wp-content/uploads/2019/07/sample-results-ensemble-model-for-cricket-score-prediction.png)

sample-results-ensemble-model-for-cricket-score-prediction

As you can see, our model has very high _R2_ values. This is promising.

### Mind the F

_While high R2 values are good,_ you should not trust the model blindly. You should also check if the relationship between output (Run Rate in remaining overs) and inputs (RRs, Or, Wr) is chance. This can be done by looking at F statistic and F distribution probability. I have not bothered with this step for all of the data, but I did check for few samples to see if the F probability is low (low means relationship is not random).

[Learn more about F statistic and how to interpret the results](https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/f-statistic-value-test/)
.

Calculating final prediction
----------------------------

As you can see, each model predicts Run Rate (in remaining overs). But we need to predict the score. Given the inputs:

*   C = Country
*   Rs = Runs already scored
*   Wr = Wickets lost so far
*   Or = Overs Remaining

We can calculate predicted Runs (Rp) as

*   RRr = **_average_** of all 10 country specific predictions (RRs, Wr, Or)
*   Rp = Rs + RRr \* Or

In simple words, our final prediction is Runs already scored + average of 10 predicted run rates _times_ remaining overs.

Testing our ensemble model against some of the recent matches
-------------------------------------------------------------

Now that we have our shiny ensemble models, let’s go test them. I have extracted score data from last 50 games by innings. I then filtered away any games with less than 50 overs played (canceled due to rain, chased before the last ball etc.)

This is what we have.

![test data for testing cricket score predictor](https://chandoo.org/wp/wp-content/uploads/2019/07/test-data-for-cricket-score-prediction-testing.png)

test-data-for-cricket-score-prediction-testing

For prediction, we also need to know what were the runs scored and how many wickets they had in hand at certain over. I started by creating a scrollbar to select the over (any multiple of 5 between 5 and 40). Then we fetch the relevant inputs from test data and run the model against them to calculate predicted score. I then compared this against actual score to see what kind of error and accuracy our model is getting.

![ensemble model - test results explained](https://chandoo.org/wp/wp-content/uploads/2019/07/test-results-how-to-read-them-and-notes.png)

test-results-how-to-read-them-and-notes

This involved using some crazy, but fun MMULT and INDEX functions (ofcourse, TRANSPOSE too). It is 2:19 AM as I am typing this. That means, Unfortunately, it is too late in the game to explain the formula logic here, so I will leave it to your imagination.

Here is how our model compares with actual results at 15 overs.

![Actual vs. Predicted scores - cricket match score prediction model](https://chandoo.org/wp/wp-content/uploads/2019/07/actual-vs-predicted-score-15-overs.png)

actual-vs-predicted-score-15-overs

And this is how it works after 25, 35 and 40 overs. As you can see, accuracy improves the later in game you ask for prediction.

*   ![](https://chandoo.org/wp/wp-content/uploads/2019/07/actual-vs-predicted-score-25-overs.png)
    
    Actual vs. Prediction – 25 overs
    
*   ![](https://chandoo.org/wp/wp-content/uploads/2019/07/actual-vs-predicted-score-35-overs.png)
    
    at 35 overs
    
*   ![](https://chandoo.org/wp/wp-content/uploads/2019/07/actual-vs-predicted-score-40-overs.png)
    
    at 40 overs
    

Predicting India’s score against Bangladesh – 2nd July, 2019
------------------------------------------------------------

Right now, as I am typing this, India is playing against Bangladesh. India have score 314 in 50 overs. I wanted to see how our model predicts the score at various points in game. As you can see, it gets a little optimistic (as India didn’t loose a wicket until 30th over) but the prediction gets closer since 35th over.

![India vs. Bangladesh worldcup match - 2nd July 2019 - score prediction vs. actual](https://chandoo.org/wp/wp-content/uploads/2019/07/india-vs-bangladesh-2nd-july-2019-world-cup-game-predictions-vs-actual.png)

Download cricket score prediction model & play with it
------------------------------------------------------

If you want to examine the calculations, predict your own scores or just want to see how its all done, **[here is the file](https://chandoo.org/wp/wp-content/uploads/2019/07/cricket-score-prediction-model.xlsx)
**.

In the download:

*   You will find two models, not one. This is because I built two regression models to see which will give better prediction. The one presented in this article gives better results.
*   You will find a simple score predictor too. Enter inputs (Country, runs so far, wickets so far and overs) and it will tell you what the predicted score is.
*   All calculations and data.

Feel free to mash up the data to create your own prediction tool.

How I built the score predictor – video
---------------------------------------

I made a short (oh well, 37 minutes long) video explaining the process, machine learning concepts and Excel implementation. Watch it below or [see it on Chandoo.org youtube channel](https://youtu.be/7_mOQtRCBWA)
.

References – on Machine learning, Excel and statistics
------------------------------------------------------

This is an interesting topic and I am sure you want to know more. See below references to understand the concepts better.

*   **Ensemble modeling:**
*   [Ensemble modeling & learning](https://en.wikipedia.org/wiki/Ensemble_learning)
    
*   [Ensemble modeling basics, terminology and sample Python code](https://www.analyticsvidhya.com/blog/2018/06/comprehensive-guide-for-ensemble-models/)
    
*   [Understanding bootstarpping technique](https://towardsdatascience.com/an-introduction-to-the-bootstrap-method-58bcb51b4d60)
    
*   **LINEST() & Multiple Regression:**
*   [LINEST Function – Microsoft Help](https://support.office.com/en-us/article/linest-function-84d7d0d9-6e50-4101-977a-fa7abf772b6d)
    
*   [LINEST example and explanation from MIT](http://www.mit.edu/~mbarker/formula1/f1help/04-g-m60.htm)
    
*   [LINEST and other forecasting functions in Excel](https://chandoo.org/wp/trendlines-and-forecasting-in-excel-part-2/)
    
*   **F statistic:**
*   [Understanding F statistic](https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/f-statistic-value-test/)
    
*   **Excel features:**
*   [Power Query for combining files](https://chandoo.org/wp/combine-excel-files-using-power-query/)
    
*   [INDEX function](https://chandoo.org/wp/index-formula-usage-and-tips/)
    
*   **Also see:**
*   [Time series forecasting in Excel](https://chandoo.org/wp/forecasting-in-excel/)
    

How do you like the score predictor?
------------------------------------

I had so much fun creating this. I did have a few false starts and made models with wrong equations, but eventually came up with something that provides sensible prediction. I am happy with the way it turned out. Although I couldn’t explain every little thing about the model in this post, I hope you are able to fill those gaps in.

Do you like this prediction model in Excel? Are you surprised to see a complex machine learning algorithm implemented in good ol’ spreadsheet? **_Share your thoughts in the comments._**

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [18 Comments](https://chandoo.org/wp/predict-cricket-scores-excel-ml/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/predict-cricket-scores-excel-ml/#respond)
    
*   Tagged under [advanced excel](https://chandoo.org/wp/tag/advanced-excel/)
    , [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [cricket](https://chandoo.org/wp/tag/cricket/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [ensemble modeling](https://chandoo.org/wp/tag/ensemble-modeling/)
    , [Forecasting](https://chandoo.org/wp/tag/forecasting/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [Learn Excel](https://chandoo.org/wp/tag/excel/)
    , [Linest](https://chandoo.org/wp/tag/linest/)
    , [MMult()](https://chandoo.org/wp/tag/mmult/)
    , [transpose](https://chandoo.org/wp/tag/transpose/)
    
*   Category: [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    

[PrevPreviousShould finance people learn Power BI?](https://chandoo.org/wp/should-finance-people-learn-powerbi/)

[NextMake info-graphics with shape fill technique \[Charting Tip\]Next](https://chandoo.org/wp/infographic-charts-in-excel/)

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
    
    [Reply](https://chandoo.org/wp/predict-cricket-scores-excel-ml/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/predict-cricket-scores-excel-ml/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/predict-cricket-scores-excel-ml/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ