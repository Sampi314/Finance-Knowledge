# Monday Morning Mulling: August 2018 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-august-2018-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: August 2018 Challenge

*   September 2, 2018

Monday Morning Mulling: August 2018 Challenge
=============================================

Monday Morning Mulling: August 2018 Challenge
=============================================

3 September 2018

_On the final Friday of each month, we set an Excel problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

**_Final Friday Fix: August Challenge Recap_**

As explained on Friday, imagine you have five business units: Alpha, Bravo, Charlie, Delta and Echo and data for each business unit under five scenarios, displayed using a clustered chart similar to the following:

![](<Base64-Image-Removed>)

It was important to note the consistent colouring of the business units for each scenario.

Next, you decide you want to create an interactive chart, so you add a slicer:

![](<Base64-Image-Removed>)

Selecting ‘Alpha’ generates

![](<Base64-Image-Removed>)

Alpha’s data is in blue – as in the summary chart. Then you decide to select ‘Bravo’ and ‘Echo’:

![](<Base64-Image-Removed>)

Again, the colours are consistent with the original chart and there is no unnecessary spacing.

The challenge was “simply” to replicate this chart’s behaviour – so how did you do?

**_Suggested Solution_**

One obvious thing to notice in this challenge was the absence of a displayed dataset, which sort of gave the game away:

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

It’s in a _Table_. And that happens to be important. But more on that shortly.

What most people would do is take their data

![](<Base64-Image-Removed>)

and create a PivotChart or a PivotChart with a PivotTable, depending upon preferences and what version of Excel they had:

![](<Base64-Image-Removed>)

Putting the ‘Business Unit’ field on the Axis and all five scenarios in the Values section, with a little bit of tinkering you can get a chart looking like this:

![](<Base64-Image-Removed>)

If you click anywhere inside the source PivotTable and choose ‘Insert Slicer’ from the ‘Filter’ grouping of the ‘Analyze’ tab in the ‘PivotTable Tools’ section of the Ribbon, you can select a ‘Business Unit’ slicer. Without bothering to format it, if I click on ‘Alpha’,

![](<Base64-Image-Removed>)

I get the following chart displayed:

![](<Base64-Image-Removed>)

Rats. I have inconsistent colouring, which is not what I required. Users now spend hours trying to change these colours so that they will work when the slicer inputs are changed. Maybe there is a solution out there this way, but there is a much simpler way of doing this.

Let’s scrap the PivotChart idea.

Instead, I go back to the original data and highlight it all (**CTRL + A**). Then, I convert the data into a Table (**CTRL + T**). You can find out more about [Tables](https://www.sumproduct.com/thought/tables)
 here. Ensure that you check the ‘My table has headers’ check box, _viz._

![](<Base64-Image-Removed>)

The aim is to insert a clustered column chart:

![](<Base64-Image-Removed>)

With a little bit of formatting, it won’t take long to create a chart looking like the following:

![](<Base64-Image-Removed>)

Then, click anywhere inside the Table to active the context specific ‘Design’ tab for ‘Table Tools’ in the Ribbon. In the ‘Tools’ grouping, click on ‘Insert Slicer’ and again select ‘Business Unit’.

Simple manipulation will generate your slicer:

![](<Base64-Image-Removed>)

Without any further work, selecting ‘Alpha’ generates the required chart:

![](<Base64-Image-Removed>)

Furthermore, if you select ‘Bravo’ and ‘Echo’ you will get the required chart too:

![](<Base64-Image-Removed>)

It’s that easy. It just need you to create a Table – not a PivotTable – to begin with.

**_Word to the Wise_**

Slicer filters first appeared with the 2010 release of Excel and at that time, you could only use them to filter data in PivotTables. However, beginning with the 2013 release of Excel, you could then use Slicers also to filter data in tables. Apologies if you are reading this and have an earlier version of Excel – time to upgrade!

Further, slicers only filter fields in a table of data and fields must always be in a column. Therefore, any field you wish to filter on must be in a column – hence we can only slice on business units not scenarios here (as they go across a row). If we wanted to slice on the scenarios instead, we must transpose the table of data first.

You can read more about slicers [here](https://www.sumproduct.com/thought/slicer-of-good-fortune)
.

_The Final Friday Fix will return on Friday 28 September with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-august-2018-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-august-2018-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-august-2018-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-august-2018-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-august-2018-challenge/#0 "close")

top