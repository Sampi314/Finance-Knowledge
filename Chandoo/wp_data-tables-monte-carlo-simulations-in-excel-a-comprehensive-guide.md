# Data Tables & Monte Carlo Simulations in Excel - A Comprehensive Guide » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide

---

*   [All Time Hits](https://chandoo.org/wp/category/alltime-best/)
    , [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [simulation](https://chandoo.org/wp/category/simulation/)
    

Data Tables & Monte Carlo Simulations in Excel – A Comprehensive Guide
======================================================================

*   Last updated on June 27, 2013

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

_This is a Guest Post by [**Hui**](http://chandoo.org/wp/about-hui/ "About Hui")
, an Excel Ninja and One of the Moderators of our Forums. Please note that this post is unusually large by Chandoo.org standards._

_\============================================================  
_

If anybody asks me what is the best function in excel I am drawn between [Sumproduct](http://chandoo.org/wp/2009/11/10/excel-sumproduct-formula/)
 and Data Tables, Both make handling large amounts of data a breeze, the only thing missing is the Spandex Pants and Red Cape!

How often have you thought of or been asked “I’d like to know what our profit would be for a number of values of an input variable” or “Can I have a graph of Profit vs Cost vs …”

This post is going to detail the use of the Data Table function within Excel, which can help you answer those questions and then so so much more.

*   [Introduction](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/#introduction)
    
*   [1 Way Tables](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/#1way-tables)
    
*   [2 Way Tables](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/#2way-tables)
    
*   [Monitor Multiple Variables](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/#monitor-multiple-vars)
    
*   [Multiway Tables](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/#multiway-tables)
    
*   [Monte Carlo Analysis](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/#montecarlo-simulations)
    
*   [Iterative Functions and Fractals](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/#iterative-functions)
    
*   [Download Example Workbooks](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/#download-examples)
    

INTRODUCTION
------------

_How often have you thought “**I’d like to know what our profit would be for a +/- 10, 20 and 30 % variance in the costs**” ?  
_

This post is going to detail the use of the Data Table function within Excel, which can help you answer that question.

The Data Table function is a function that allows a table of what if questions to be posed and answered simply, and is useful in simple what if questions, sensitivity analysis, variance analysis and even Monte Carlo (Stochastic) analysis of real life model within Excel.

The Data Table function should not be confused with the [Insert Table function](http://chandoo.org/wp/2009/09/10/data-tables/)
.

DATA TABLE BASICS
-----------------

The Data Table function is hidden away in different locations within different versions of Excel but apart from the menu location the functionality is the same throughout.

### **Where is the Data Table Function**

**Excel 2007/10**

In Excel 2007 & 2010 go to the Data Tab, What If Analysis panel and select Data Table

![Data Tables - Excel 2007 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-1.png)

**Excel 97-03**

In Excel up to 2003 go to the Data Menu and select Table…

![Data Tables - Excel 2003 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-2.png)

Both Excel 97-03 and 2007/10 then bring up the same **Data Table** dialog box.

![Input Dialog - Data Tables [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-3.png)

… and this simple dialog box is all empowering ?

**Yes !**

### Blue Sky Mine Co

For demonstration of the Data Table function I am going to use a simple profit model of a Gold Mine, “The Blue Sky Mine Co”. This is a fictitious mine but provides a simple model which we can use the data Table function to analyse.

It consists of 6 input variables and a simple cost and revenue model to produce a profit.

![1 way Data Tables - Example - 1 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-4.png)

In our Blue Sky Gold Mine Co model, we can see that if we mine and treat 1,000,000 t of gold ore containing 1.68 g/t gold, we will make A$ 5.452M profit. But what if the inputs change ?

1 WAY DATA TABLES
-----------------

Lets make a 1 Way Table with our Blue Sky Gold Mine Co example.

_This is shown in the attached Excel Workbook on the “1 Way” Tab or [1 Way Example](https://chandoo.org/wp/wp-content/uploads/2010/05/1.-1-Way.xlsx)
  
_

![1 way Data Tables - Example - 1 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-4.png)

In our Blue Sky Gold Mine profit calculation example, we can see that if we mine and treat 1,000,000 t of gold ore containing 1.68 g/t gold, we will make A$ 5.452M profit. But what if the grade is more or less than that value of 1.68 g/t ? After all it is only a geological estimate.

This is what the Data Table function is made for.

Next to the model add a couple of columns as shown in blue

**Note:** Throughout this post you will see the use of 1E6 in formulas which is simpler to write than 1,000,000.

![1 way Data Tables - Example - 2 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-5.png)

The first column is a list of values that will be applied to each iteration of the Column Input Cell

The Top Cell of the second Column contains a formula which will retrieve the answer you want to watch, in this case Profit. It will be displayed as M$.

Now select the entire Blue Area and Select Data Table

This is the Data Table input screen.

![Input Dialog - Data Tables [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-3.png)

The tricky/confusing part here is that in our example we are changing the input value to our Gold Mine Profit model using a Column of Numbers, so enter $C$6 in the Column Input Cell, Leave the Row Input Cell blank.

![1 way Data Tables - Example - 3 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-6.png)

Click Ok

You can now see a Table of Profit Values for each Grade Value.

![1 way Data Tables - Example - 4 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-7.png)

The variance in the Profit can easily be graphed against the Gold Grade and we can now see that if the Gold Grade is below about 1.55 g/t Au we will not make a profit and conversely if it is above 2.0 g/t Au we will make a large profit.

![1 way data tables - outputs in a chart [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-8.png)

Before we move onto 2 Way Data Tables it is worth exploring small variations on One Way Tables.

### What if my Data is in Rows?

Had our input data been arranged horizontally in Rows, we could have used a Row Input Cell to process the data.

![1 way data tables in a row [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-9.png)

### What if I want to vary the inputs by a certain Percentage ?

Another Scenario is often where you want to vary an input by a Fixed Percentage.

This is easily done using Data Tables

Setup the input cells with the percentage variations you want to examine, noting that the values don’t have to be evenly spread.

Setup a Temporary Input Cell, This will hold the Percentage Variance briefly whilst calculations are happening. Set a default value of 0 (zero)

Change your Main Input Cell, Gold Grade in our case, to Multiply the fixed answer by 1+ the temp Input Cell.

Run the Data Table with a **Column Input Cell**, which will refer to the **Temp Input Cell**.

![1 way data tables - inputs in %s [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-10.png)

2 WAY DATA TABLES
-----------------

So the Boss comes in and asks, what Happens if the Gold Grade changes as well as the A$/U$ Exchange Rate?

You guessed it, Two Way tables to the rescue.

_This is shown in the attached Excel Workbook on the “2 Way” Tab or [2 Way Example](https://chandoo.org/wp/wp-content/uploads/2010/05/2.-2-Way.xlsx)
  
_

Two way data Tables work the same as One Way Data Tables except that you can vary 2 parameters at once.

With Two Way Data Tables you need to setup a Column of data for one Input and a Row of data for the second Input. The answer is returned at the intersection of the Row and Column.

Here we have setup a Column of Gold Grades ranging from 1.5 to 2.1 g/t Au and a Row of Exchange rates =varying from 0.70 to 1.00 A$/U$

![2 way data tables - Example 1 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-11.png)

Note at the intersection of the Row and Column there is a Reference to the variable you want to monitor in this case profit.

![2 way data tables - Example 2 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-12.png)

You can now see the variance in Profit for variations in Gold Grade and Exchange Rate.

### What about varying by Percentages?

Once again we can re-arrange the input variables to examine percentage changes in the inputs via a Temporary Input Cell.

![2 way data tables - Example 3 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-13.png)

MONITORING MULTIPLE VARIABLES
-----------------------------

So you have a complex model and want to monitor a number of input and output variables at once. No problems, Data Tables to the rescue.

In this example we are varying one input variable but monitoring 3 Output variables, 2 input variables and then doing a calculation all as part of the Data Table.

This is shown in the attached Excel Workbook on the “Monitor Multi variables” Tab or [Monitor Multi Variables Example](https://chandoo.org/wp/wp-content/uploads/2010/05/3.-Monitor-Multi-Variables.xlsx)

![2 way data tables - Example 4 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-14.png)

The first 3 columns, Total Cost, Revenue and Profit are output variables even though Total Cost doesn’t change, we can still monitor it to make sure our model is working correctly

The next 2 columns, Gold Grade and Gold Price are input variables even though only Gold Grade is being varied.

The last column Cost per Oz is not calculated as part of the model (ok sometimes we forget don’t we), but it can be calculated on the fly as part of the Data Table.

The result is:

![2 way data tables - Example 5 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-15.png)

MULTIWAY DATA TABLES
--------------------

But I hear you thinking, “_**If Data Tables are so good why can I only Change 2 variables at Once? I want to change more!**_ “.

No Problems

Data Tables in fact allow you to Change any Number of input variables at once and monitor any number of input and output variables. It does however require a slight of hand.

This is shown in the attached Excel Workbook on the “Multi Way Tables” Tab or [Multiway Table Example](https://chandoo.org/wp/wp-content/uploads/2010/05/4.-Multiway-Table.xlsx)

First things first,

Setup a table of what scenarios you want to examine:

![Multi-way Data tables - Example [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-16.png)

Setup the Data Table area to monitor Inputs, Outputs and Calculated Fields

![Multi-way Data tables - Example 2 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-17.png)

Note that the Input Data Column will be used to select the Scenario No.

Also note that we have setup F2 to retrieve the Scenarios Name.

And in H6 we will put the Scenario name into the Data Table, who said Data Tables were only for Numbers!

Next Link the Model to the scenario

![Multi0way Data Tables - Setting up Scenarios [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-18.png)

And run the Data Table

![Multi-way Data tables - Example 3 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-19.png)

Note how the Description Column is populated with the Scenario’s Name (Text values)

So now when your boss asks you what effect the price of … has on the budget, you know where to turn.

MONTE CARLO SIMULATIONS IN EXCEL
--------------------------------

Monte Carlo simulation (or analysis) as its name suggests puts an element of gambling into the scenarios, or more correctly allows you to measure the effect of variability on input parameters.

This is done by running scenarios against your model hundreds or thousands of times and changing the inputs each time and then measuring the effects at the end of the runs.

And Data Tables can do that? Absolutely!

### First some statistics.

Everything in life has variability, from the size of Zebra’s Strips, The height of people and the Arrival times of trains, the time that people read this post, the time that it takes people to read this post.

Most things are variable around a central or mean (average) value. The spread of variability is commonly known as the distribution.

Distributions can have many names and shapes, but common ones are

*   **Normal:** Bell shaped around a mean
*   **Uniform:** All values have an even chance of selection
*   **Exponential:** Low or High values have a much higher probability that the other values

In life most distributions are Normal in nature indicating that the distribution is Bell shaped around a mean with a known method of describing the variability around this.

Excel has 2 functions that produce Random numbers, Rand() and Randbetween(). These 2 functions both have a Uniform Distribution, that is any value between the minimum and maximum values will have the same probability of being chosen.

We can convert a uniform distribution to a Normal distribution by some simple maths (simple to do, not simple to explain).

**\=norminv(rand(),_mean_,_standard\_dev_)**

**Example =NORMINV(rand(),_100_,_10_)**

Will generate a distribution of random numbers centred on 100 with a spread having a bell shaped curve with a standard deviation of 10. This means that the function will produce a number with a 99.7% probability of being between 70 and 130 and on average will have a mean of 100.

### Monte Carlo simulations

So how can I use this and Data Tables to do Monte Carlo simulations.

Before we go any further the author wants to explicitly state that he is not suggesting that the use of Normal Distributions for the variables modeled below is appropriate, except for the purpose of demonstration of the principles behind Monte Carlo Modelling.

As with all models you need to have a good understanding of the distribution of inputs before you start playing with simulations or of which Monte Carlo is but one type. ie: Rubbish In Rubbish Out.

We can model an input vaiable, in this case Exchange rate with a distribution instead of a fixed value and then run the model a number of times and see what impact the variation has on the output.

This is shown in the attached Excel Workbook on the “Monte Carlo (Simple)” Tab or [Monte Carlo (Simple) Example](https://chandoo.org/wp/wp-content/uploads/2010/05/5.-Monte-Carlo-Simple.xlsx)

[![](https://chandoo.org/wp/wp-content/uploads/2010/05/data-tables-monte-carlo-analysis-20a1.png "data-tables-monte-carlo-analysis-20a")](https://chandoo.org/wp/wp-content/uploads/2010/05/data-tables-monte-carlo-analysis-20a1.png)

The formula =NORMINV(RAND(),0.92,0.02), will generate a Random Exchange Rate with a distribution based on a mean on 0.92 A$/U$ and a spread of approximately 6 cents each way ie: there will be a 99.7% probability of the exchange rate being between 0.86 and 0.98 A$/U$.

[![](https://chandoo.org/wp/wp-content/uploads/2010/05/data-tables-monte-carlo-analysis-21a1.png "data-tables-monte-carlo-analysis-21a")](https://chandoo.org/wp/wp-content/uploads/2010/05/data-tables-monte-carlo-analysis-21a1.png)

Copying the formula down from H6 to H1005 will allow our data table to generate 1000 iterations of the model each with a randomly generated Exchange Rate.

In the model above, you can see that for a Base case exchange rate of 0.92 the profit is $M 5.452, however after running 1000 simulations the profit is actually $M 5.7134. More important is that you can now run statistics on the model to tell what is the probability of the profit being greater than 0.00 based on variance in the exchange rate etc.

**Note 1:** You will note that in the above data table that the Input Column (darker blue) has the formula for calculating a random input grade from a distribution.  =NORMINV(RAND(),0.92,0.02)

This is a Volatile Formula , ie: It recalculates every time the worksheet changes.

What this means for the worksheet is that when the Data Table goes to Calculate Row 2 of the Data Table it will recalculate the Input value for Row 1.

On Calculation of Row 2, It doesn’t change the Table Values for Row 1, just the Input Column value.

So after 1,000 calculations of the Data Table, the Input Column values will have no relationship to the data from the original Calculations stored in the Data Table body area.

To make up for this we also add an Input variable to the Data Table.

Doing this allows the Data Table to capture and store both the Input variable and corresponding Output variable in the Data Table’s Body.

**Note 2**: Always run at least 1000 iterations of Monte Carlo models. This is to ensure that you have a statistical chance of getting sufficient outliers (extreme values) to make the variance analysis meaningful. This is important because as the number of iterations increases the variance of the average output decreases.

Press F9 a few times and watch the average H6:H1005 change.

Try changing the Data table from 1,000 rows to 10, 20 or 100,0000 rows. As the number of iterations increases the variance in the average of the output decreases.

### Advanced Monte Carlo Simulations

We can now put our knowledge of Data Tables and Monte Carlo Simulation to the test by varying 4 input variables at the same time.

This is shown in the attached Excel Workbook on the “Monte Carlo (Advanced)” Tab or [Monte Carlo (Adv) Example](https://chandoo.org/wp/wp-content/uploads/2010/05/6.-Monte-Carlo-Adv.xlsx)

In the example below we have inserted distributions for 4 input variables.

|     |     |     |
| --- | --- | --- |
| Ore Tonnes | Mean 1,000,000 tonnes | Standard Deviation of 100,000 tonnes |
| Gold Grade | Mean 1.68 g/t Au | Standard Deviation of 0.1 g/t Au |
| Gold Price | Mean 1,200 U$/Oz | Standard Deviation of 100 U$/Oz |
| Exchange rate | Mean 0.92 A$/U$ | Standard Deviation of 0.02 A$/U$ |

![Monte-carlo Simulations in Excel - 3 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-22.png)

And setup a data Table for the 4 Input Variables and main output variable, Profit.

![Monte-carlo Simulations in Excel - 4 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-23.png)

**Note:** When this model is run through the Data Table, note that the Row or Column input cells can be set to anywhere. The Model is not using the value of the Input Cell (Row or Column) and isn’t even using the Run No (Column F) for the model, the data table is simply being used to run lots of iterations of the model, with the variability coming from the Random Numbers in the 4 input cells.

ITERATED FUNCTIONS INCLUDING FRACTALS
-------------------------------------

At a meeting in early 2005, the company I was working for was looking at an integrated Scheduling & Budgeting system.

The salesman gave a great demo except that the system would take approx. 30 mins to calculate our budget as opposed to a half a second in Excel.

Complaining I mentioned that our current, Excel based, system could do the job in seconds.

And he returned stating that “the system was doing a lot of things Excel couldn’t do”.

I responded “but Excel can do anything”

and he immediately shot back that “Excel can’t do a Mandelbrot”

To which I responded “Yes it can”

And he responded “Not without VB Code”

Without too much thinking I responded that I would accept the Challenge.

The attached file, which is described below is my response.

### Excel Mandelbrot

![Mandelbrot Fractals in Excel - 1 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-24.png)

The attached file is an implementation of the classic Mandelbrot implemented in Excel without the use of VBA code.

A Mandelbrot is a graphical display of the simple equation Zn+1 = Zn2 + c, where Z is a complex number (x +iy).

Which is described at [http://en.wikipedia.org/wiki/Mandelbrot\_set](http://en.wikipedia.org/wiki/Mandelbrot_set)

This can be solved in the real X-Y domain using:

Xnew = Xold2 – Yold2 + X\_Orig and

Ynew = 2 \* Yold \* Xold+ Y\_Orig

Study of iterated functions reveals that these functions will either converge on an answer or diverge once a boundary has been breached

In the case of the Mandelbrot, this function diverges after the function Z2 \> 4

So to construct a Mandelbrot a program needs simply to

1.  Loop from Xmin to Xmax in small steps and
2.  Loop from Ymin to Ymax in small steps and
3.  For every X, Y Point in the above 2 loops, solve the above equations until the answer is > 4
4.  Color the screen according to how many iterations it took to diverge or not

Simple…

Except that Excel doesn’t have any looping functions unless you use VBA Code

The calculation of the solution for any X, Y starting point is simple enough using a series of Rows and Columns where each Cells is the starting iteration of the solution for each various X, Y co-ordinate.

This is shown in the Calculations page in the Xnew, Ynew, Xold, Yold, Rsq and Count columns.

The iterations are simply done in the Xnew and Ynew columns

For each iteration we check that the Z2 value hasn’t diverged (not > 4) (Xnew2 + Ynew2)

And keep track of how many iterations it took to diverge, the Count Column

The above 5 lines I refer to below as the Calculator.

![Mandelbrot Fractals in Excel - 2 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-25.png)

The trick to working out how to do this for a X-Y Grid was the use of the Table Function to send the starting positions to the Calculator and return the Count for that location.

This is the large Yellow Area.

![Mandelbrot Fractals in Excel - 3 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-26.png)

The Large yellow area (Data Table Area) is flanked on the Top and Left by the X and Y co-ordinates for a grid encompassing the area which we want to plot.

The Table Function extracts the Top and Left values and puts them in the X Orig and Y Orig positions of the calculator.

The Calculator returns the Count of the Divergence of the Calculator to the H2 position (Top Left corner of the Grid) and that value is stored at the Grid Location.

![Mandelbrot Fractals in Excel - 4 [Data Tables & Monte Carlo Simulations in Excel]](https://img.chandoo.org/l/mc/data-tables-monte-carlo-analysis-27.png)

The Data Table repeats this for each position in the X-Y Grid.

An Excel Surface Chart can then Chart the Large Yellow area in effect creating a Traditional Mandelbrot plot by joining up adjacent areas of equal value (Contouring).

The Chart can also be displayed as a 3D-Surface rather than a Contour Chart for a dramatic effect.

Zooming In can be added by adding code that allows the user to say Right click in the Large Yellow area and the code will then take the Co-ordinates and Zoom in by a fixed factor

Zooming Out can be added by adding code that allows the user to say Double click in the Large Yellow area and the code will then take the Co-ordinates and Zoom out by a fixed factor

DOWNLOAD EXAMPLE WORKBOOKS
--------------------------

Download the complete example workbooks described above and practice data tables on your own.

*   [Click here to download](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/gold-mine-monte-carlo-analysis.xlsx)
     Gold Mine Monte Carlo Simulations & Data Tables workbook. \[[XL 2003 version here](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/gold-mine-monte-carlo-simulation-xl2003.xls)\
    \]
*   [Click here to download](http://cid-b663e096d6c08c74.skydrive.live.com/self.aspx/Public/excel-mandelbrot.xls)
     Excel Mandelbrot workbook.

**Note:** A few people have said the above files either Hang or Freeze there PC’s. This is probably because they have a number of large Data Tables within them.

I have uploaded each Tab as a separate Excel 2007 file, see below:

1\. [1 Way.xlsx](https://chandoo.org/wp/wp-content/uploads/2010/05/1.-1-Way.xlsx "1 Way Tables")
  
2\. [2 Way.xlsx](https://chandoo.org/wp/wp-content/uploads/2010/05/2.-2-Way.xlsx "2 Way Tables")
  
3\. [Monitor Multi Variables.xlsx](https://chandoo.org/wp/wp-content/uploads/2010/05/3.-Monitor-Multi-Variables.xlsx "Monitor Multi Variables")
  
4\. [Multiway Table.xlsx](https://chandoo.org/wp/wp-content/uploads/2010/05/4.-Multiway-Table.xlsx "Multiway Tables")
  
5\. [Monte Carlo Simple (updated)](https://chandoo.org/wp/wp-content/uploads/2010/05/5.-Monte-Carlo-Simple-update.xls)
  
6\. [Monte Carlo (Adv).xlsx](https://chandoo.org/wp/wp-content/uploads/2010/05/6.-Monte-Carlo-Adv.xlsx "Monte Carlo (Advancd)")

In the Example Files some of the Data Tables have been removed and there are instructions on how to re-instate them included in the file.

FINAL THOUGHTS
--------------

### Speed

If you start adding a number of Data Tables to Complex Models you will rapidly cause even the fastest machines to grind to a halt.

### VBA

The best way around the above speed issue is to setup a number of Data Tables for whatever analysis you wish to undertake. Then as you run each analysis copy the Data Table Data Area, The area between the Rows and Columns and paste it as values over itself. Then move onto the next data table and run it.

This allows the Data Tables to be quickly recalculated if required.

This process can be automated via 3 lines of VBA code for each Data Table.

‘Calculate Data Table in F5:H18, using Column Input cell C9  
_Range(“F5:H18”).Table ColumnInput:=Range(“C9”)_

‘Copy Data Area as Values  
_Range(“G6:H18”).Copy_  
_Range(“G6:H18”).PasteSpecial Paste:=xlPasteValues_

‘Repeat Above for each Data Table

‘Deselect Current Range  
_Application.CutCopyMode = False_

### Cell Contents

If you look at a cell in a Data Table you will see something like:

*   **{=TABLE(,E5)}**: for a Column Input Cell
*   **{=TABLE(E4,)}**: for a Row Input Cell
*   **{=TABLE(E4,E5)}**: for a Row and Column Input Cell

Although these appear like Array Formula, they cannot be manually set.

So setting up a data table and typing =TABLE(,E5) Ctrl-Shift-Enter, only produces an error message.

Further Reading & References
----------------------------

*   [http://www.exceluser.com/explore/statsnormal.htm](http://www.exceluser.com/explore/statsnormal.htm)
    
*   [http://www.vertex42.com/ExcelArticles/mc/GeneratingRandomInputs.html](http://www.vertex42.com/ExcelArticles/mc/GeneratingRandomInputs.html)
    
*   [http://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm](http://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm)
    
*   [http://en.wikipedia.org/wiki/Mandelbrot\_set](http://en.wikipedia.org/wiki/Mandelbrot_set)
    
*   [http://chandoo.org/wp/2011/06/20/analyse-data-like-a-super-hero/](http://chandoo.org/wp/2011/06/20/analyse-data-like-a-super-hero/ "Analyse Data Like a Super Hero")
    

Added by Chandoo
----------------

This post is by far one of the most comprehensive posts on Chandoo.org. And each of the 3100+ words in it show the passion and knowledge that _**Hui**_ has. Thank you so much Hui for sharing this wealth of knowledge with our members.I have learned a lot of interesting and useful things from this article.

If you have enjoyed this article, _**please say thanks to [Hui](http://chandoo.org/wp/about-hui/ "About Hui")
**_.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [206 Comments](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/#respond)
    
*   Tagged under [1way tables](https://chandoo.org/wp/tag/1way-tables/)
    , [2way tables](https://chandoo.org/wp/tag/2way-tables/)
    , [Analytics](https://chandoo.org/wp/tag/analytics/)
    , [data tables](https://chandoo.org/wp/tag/data-tables/)
    , [downloads](https://chandoo.org/wp/tag/downloads/)
    , [fractals](https://chandoo.org/wp/tag/fractals/)
    , [guest posts](https://chandoo.org/wp/tag/guest-posts/)
    , [hui](https://chandoo.org/wp/tag/hui/)
    , [mandelbrot](https://chandoo.org/wp/tag/mandelbrot/)
    , [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)
    , [modeling](https://chandoo.org/wp/tag/modeling/)
    , [monte carlo simulations](https://chandoo.org/wp/tag/monte-carlo-simulations/)
    , [multiway data tables](https://chandoo.org/wp/tag/multiway-data-tables/)
    , [scenarios](https://chandoo.org/wp/tag/scenarios/)
    , [simulation](https://chandoo.org/wp/tag/simulation/)
    , [spreadsheets](https://chandoo.org/wp/tag/spreadsheets/)
    , [what-if analysis](https://chandoo.org/wp/tag/what-if-analysis/)
    
*   Category: [All Time Hits](https://chandoo.org/wp/category/alltime-best/)
    , [Analytics](https://chandoo.org/wp/category/analytics/)
    , [Charts and Graphs](https://chandoo.org/wp/category/visualization/)
    , [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [Featured](https://chandoo.org/wp/category/best-of-phd/)
    , [Huis](https://chandoo.org/wp/category/huis/)
    , [Learn Excel](https://chandoo.org/wp/category/excel/)
    , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
    , [simulation](https://chandoo.org/wp/category/simulation/)
    

[PrevPreviousChange Data Labels in Charts to Whatever you want \[Quick Tip\]](https://chandoo.org/wp/change-data-labels-in-charts/)

[NextImportant Update: Dilbert is gone!Next](https://chandoo.org/wp/change-to-chandoo-org/)

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
    
    [Reply](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ