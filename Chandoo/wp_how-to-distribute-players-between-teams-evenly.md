# Learn how to use Solver to allocate players evenly to Teams. A Solver Tutorial.

**Source:** https://chandoo.org/wp/how-to-distribute-players-between-teams-evenly

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [Solver](https://chandoo.org/wp/category/solver/)
    

How to Distribute Players Between Teams – Evenly
================================================

*   Last updated on October 12, 2017

![Picture of Hui...](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=300&d=mm&r=g)

#### Hui...

Share

Facebook

Twitter

LinkedIn

In April 2017, **Shenricus**, posed a question in the [Chandoo.org Forums:](https://chandoo.org/forum/threads/a-challenge-for-someone-much-smarter-than-myself-please-help.34188/)

_“I have 24 people who each have their own score. I’ve been trying to figure out how I can divide these names into 3 even teams – or as close as possible.”_

I answered with a Solver Based solution, and Bosco Yip also added to my solution with a slightly different approach.  
This caused me to reconsider my first attempt and finally I posted a Final Solution, which was also a Solver based solution, but was a much more robust solution than my original solution or Bosco Yip’s solution.

This post will examine the thought process used to derive the solution and then implement that using solver.

As always a Sample file is provided so you can follow along: [Download Sample File here](https://chandoo.org/wp/wp-content/uploads/2017/10/Even-Teams.xlsx)
.

Approach
--------

Shenricus gave us a list of 24 players and a score for each player.

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams01.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams01.png)

The players are Ranked from Best to Worst.

We have no other information as to the Sport or Score.

The question posed by Shenricus is to distribute the players into teams so that each team is “As even as possible”.

Considering that we have 24 players and need to put them into 3 teams, we will assume each team has the same number of players and hence requires 8 players.

My initial though was to setup a Delta or Difference between each Players Score and the Mean (Average of all scores).

First calculate the Average of All the Scores

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams02.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams02.png)

Then calculate the Differences between the each players Score and the Average

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams03.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams03.png)

Next we need to distribute each player into one of 3 teams.

Solver will put a value of 1 when a Player is in a Team, and a 0 when the player is not in a Team.

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams04.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams04.png)

Next add a Formula to Calculate the Sum of the Variations from Mean for each Team

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams05.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams05.png)

and Finally Sum these up

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams06.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams06.png)

We should be able to get Solver to Minimise this value.

So lets look at how Solver is setup.

How Do Use Solver?
------------------

Solver is found in the **Data**, **Analyze** Tab.

Your screen may look different to mine depending on which version of Excel you are using and if you have your Excel window at a maximum size or not.

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams10.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams10.png)

If you cannot see it, you may not have Solver Loaded.

How Do We Install Solver?
-------------------------

**Right Click** on any part of the Ribbon

Select **Customize the Ribbon**

**[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams09.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams09.png)
**

Select **Add-ins** on the Left menu and

Manage **Excel Add-ins** in the Manage Dialog and press **Go**…

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams11.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams11.png)

Finally Select **Solver** and **Ok**

**[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams12.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams12.png)
**

Solver will now be visible in the Data, Analyze Tab

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams10.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams10.png)

How Do We Setup Solver?
-----------------------

Click anywhere in the model  
Goto the **Data**, **Analyze** Tab  
Select **Solver**

The Solver Dialog is show as:

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams20.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams20.png)

Lets look at each of the highlighted sections first and I will discuss this first as a plain English and then I will discuss how it is implemented in Solver

Solver is asking us to Set our Objective, to a Minimum, Maximum or Value, by changing some cells, Subject to some constraints.

### Set Objective

Solver is asking what our objective is?  
In our Even Teams example we want to minimise the variance in the average Team Scores

### By Changing variable Cells

We want to achieve our objective by setting Each Player to be a Member of 1 team  
That is Each player must have a 1 in a Column of Team 1, Team 2 or Team 3

### Subject to the Constraints

We have a Number of Constraints that our model will be subject to

Each player must have a 1 in a Column of Team 1, Team 2 or Team 3  
Each Team must have 8 players  
All 24 Players must be used only once each  
Each player can only be in a Team, he can’t be shared between teams

Solver operates using a number of techniques to Solve the above problem.  
Simplistically it iterates values into the Variable Cells, subject to meeting the constraints.  
It measures the output and re-iterates until a better solution is reached.

### In Solver Speak

Lets look at how our model is setup in Solver

### Objective

The Objective is to Minimise the Sum of the Team Scores  
That is to Minimize Cell **E27**

### Variable Cells

We will be changing the allocation of players into each team.

This is the Variable Cells **$E$2:$G$25**

### Subject to the Constraints

The variable cells will be changed by Solver subject to meeting our 4 criteria defined above  
a. That each team has 8 players, each cell in **$E$29:$G$29** is **8**  
b. That each player only plays in 1 team, that is cells **$E$2:$G$25** can only be **0** or **1** (**binary**)  
c. That all 24 players are used, ie: **$H$26 = 24**  
d. That all 24 players are used only once, each cell in **$H$2:$H$25 = 1**

We haven’t yet setup Conditions C or D above in our model yet

So add a Column H

**H2**: \=Sum(E2:G2) and copy that down to Row 25

This will add the Total of each Team per Player and should be 1

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams07.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams07.png)

And add up the total of these in H26, This is the Total of all allocated Players and should be 24

**H26**: \=Sum(H2:H25)

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams08.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams08.png)

In solver setup each of these sections then click **Solve**

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams21.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams21.png)

After a Minute or so, Solver will return to tell you that it has found a Solution

Select **Keep Solver Solution**  
[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams22.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams22.png)

Lets check things

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams23.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams23.png)

Firstly we can see that

1\. The sum of the Team Scores, E27, is a very small number, as we requested  
2\. Each player was only used once Column H, True  
3\. All 24 Players were used H26, True  
4\. Each Team has 8 players, E29:G29, True  
5\. Each player is not split between teams, E2:G25, True

So all our Criteria are met, however if we start to look at the solution in more detail we can see that Team 3 has been assigned the Best 8 players, where as Team 1 has mostly the worst players, Team 2 is in the middle.

Solver has solved our problem, but our problem obviously hasn’t been correctly specified.  
Solver has setup 2 teams with Low Negative Scores to Offset Team3 with a High Positive score, with the overall result being a low average Team Score

If we look at the Total Scores for each Team, **E31:G31**

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams24.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams24.png)
  
We can see that the Total Team Scores vary between 7.705 and 7.891  
A spread of 0.186

What we actually need to specify is that the **Variation in these Total Team Scores is Minimised.** That is the spread between the 3 scores is minimised.

There are Statistical Measurements called Variance and Standard Deviation  
Without going into too much detail, each is a measure of how far a set of numbers are spread out from their average value.  
Refer Wikipedia [Wikipedia Variance](https://en.wikipedia.org/wiki/Variance)
, [Wikipedia Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation)

Luckily we can easily calculate these using Excel

In cell **E33** \=STDEV.P(E31:G31)  
Excel displays **0.078969**

So the Standard Deviation of these 3 Team Scores is 0.0789

However we need to re-run the Solver Model with a new Objective

Firstly, reset all the players to 0, ie Players are not assigned to any Team  
Select **E2:G25** and type **0** **Ctrl Enter**

Click anywhere in the model,  
Goto the **Data**, **Analyze Tab**  
Select **Solver**

Set the Objective to **$E$33**

The Variable Cells and Constraints remain unchanged

Now Click **Solve**

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams25.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams25.png)

After a minute or so, Solver will announce it has a New Solution  
Accept that as before

Lets check things

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams26.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams26.png)

Firstly we can see that

1\. The sum of the Team Scores is a very small number, as we requested, Ok  
2\. Each player was only used once Column H, Ok  
3\. All 24 Players were used H26, Ok  
4\. Each Team has 8 players, E29:G29, Ok  
5\. Each player is not split between teams, E2:G25, Ok

If we look at the solution in more detail we can see that  
The three Teams now have a spread of both good and not so good players

But the important thing to notice is that the Standard Deviation of the 3 Team Scores is now **0.001699**, or **2.1%** of the previous Standard Deviation.

This shows the teams are much more “Evenly” matched

Solver has solved our problem.

Bosco’s Solution
----------------

During the thread Bosco proposed an alternative, algebraic solution.

It involved distributing players according to simple rules

The team who got the Best player also took the worst player,

The next team who got the Second best player also took the second worst player

The next team who got the Third best player also took the third worst player, etc

This is shown:

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams27.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams27.png)

We can see that it also meets all of the constraints of the model, but has a Standard Deviation 0.00368, that isn’t as low as the Solver solution 0.001699.

What are these Other Solving Methods?
-------------------------------------

When you were setting up Solver you may have noticed a dialog asking, **Select a Solving Method**:

[![](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams25-Copy.png)](https://chandoo.org/wp/wp-content/uploads/2017/10/EvenTeams25-Copy.png)

The best discussion I have found on these alternative Solver Techniques is shown on the link below

[http://www.engineerexcel.com/excel-solver-solving-method-choose/](http://www.engineerexcel.com/excel-solver-solving-method-choose/)

Closing
-------

We can see how Solver has been used to distribute players according to player ratings and even out teams.

Unfortunately, Shenicus never came back to the forums and so we don’t know how his teams went ?

How have you distributed players or anything else ensuring things are even ?

Let us know in the comments below:

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [19 Comments](https://chandoo.org/wp/how-to-distribute-players-between-teams-evenly/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/how-to-distribute-players-between-teams-evenly/#respond)
    
*   Tagged under [solver](https://chandoo.org/wp/tag/solver/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [Solver](https://chandoo.org/wp/category/solver/)
    

[PrevPreviousConditional Formatting – Chart Data Labels](https://chandoo.org/wp/conditional-formatting-chart-data-labels/)

[NextFormula Forensics 043: Rankifs or Conditional RankNext](https://chandoo.org/wp/formula-forensics-043-rankifs-or-conditional-rank/)

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
    
    [Reply](https://chandoo.org/wp/how-to-distribute-players-between-teams-evenly/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/how-to-distribute-players-between-teams-evenly/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/how-to-distribute-players-between-teams-evenly/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ