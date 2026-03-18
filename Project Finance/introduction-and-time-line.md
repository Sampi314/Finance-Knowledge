# Modelling Religion, Criminal Behaviour and Time Lines

**Source:** https://edbodmer.com/introduction-and-time-line

---

The first part of  the project finance A-Z course just reviews some modelling principles and philosophy including being lazy with excel formulas; looking at some bad practices in other models; creating efficient and flexible time lines; structuring a project finance model; incorporating accuracy checks, insuring equations are easy to understand and discussing some project finance theory.  I begin the modelling discussion by making some suggestions on what not to do (I label these as impeachable crimes). As a historian of project finance models (I will later make a webpage on the exciting history of project finance models), I suggest the recent application of bureaucratic rules (FAST/SMART) have recently resulted in horrible models that have absurd amount of rows and can be anything but transparent, flexible or structured.  When you have to call your modelling consultant to make a new scenario or change the model, the model is a complete piece of crap and worthless. I complain a lot in the discussion below and I have written this page as a therapy while I have had the horrible task of restructuring models to remove the bureaucratic rubish .

I start with a time line discussion is one of the keys to making a model and which has become a disgusting practice.  When discussing time lines, I suggest a single master time line that with monthly periods pre-COD and semi-annual or quarterly periods post-COD. I also included a couple of files that you can use to prove if certain practices make a file “heavy” in this page and I demonstrate that there is no cost to using entire rows with LOOKUP.  As I am old, I have looked at a lot of models and I have opinions on what are better and worse models for analysis (good models are well organised and easy to read and do not have merged cells, changing formats, too many repeated lines and macro buttons).  In the file that you can download by clicking on the button below, you can test whether an excel practice of clicking on an entire line slows excel down or makes your file larger.  The answer is that using an entire row or column with LOOKUP and/or INDEX does not.  Files associated with the video that prove the size and the time issues can be downloaded by pressing the buttons below.

**[Excel File that Tests Size and Speed of Lookup Function Compared to INDEX and MATCH with Entire Lines Input](https://edbodmer.com/wp-content/uploads/2019/01/Index-MAtch-versus-Lookup-Test.xlsm)
**

**[Excel File that Tests Size and Speed of SUMIF Function with and Without Using Entire Lines Input](javascript:void(0);)
**

**[Excel File that Tests Size and Speed of LOOKUP Function with and Without Using Entire Lines Input](https://edbodmer.com/wp-content/uploads/2019/01/Lookup-Test-with-Complete-Lines.xlsm)
**

**[Power Point Slides that Accompany Project Finance Modelling A-Z Analysis and On-line Course](https://edbodmer.com/wp-content/uploads/2019/06/A-Z-Modelling-Course.pptx)
**

I am creating these exercises for a course I am teaching so that participants can review the subjects and test their knowledge. The very nice person who arranged the course also asked me to include some modelling behaviours that are disgusting. In the exercise below I hope that you see these practices have been avoided. I have also discussed these practices in more detail on the A-Z page that is linked to this sentence.  The only excel function to use in the first example is the LOOKUP function (VLOOKUP and HLOOKUP are illegal). En francais, cette function est RECHERCHER.  I have included a sheet with bad practices so you can correct them.

High Crimes and Misdemeanors in Project Finance Models (All of Us Have Been Guilty)
-----------------------------------------------------------------------------------

All of the financial modelling companies seem to have their blah, blah, blah acronyms and rules.  I have no doubt whatsoever that these bureaucratic rules have let to models which are not easy to work with and are very difficult to understand and change.  My guiding principle is to put yourself in the shoes of somebody who is reading your model for the first time.  You want the user to say “I understand what you are doing and where the numbers are coming from.” For what it is worth, here are my rules.  I don’t tell you what to do; I provide a few suggestions on what you should generally not to do.  I tell you this because I have made all of the mistakes and I have stole ideas from many other models.  After making mistakes, I believe a few excel practices really work. But one of my biggest complaints is paying too much attention to the rules and applying so-called best practice rules. A friend of mine (John Cassidy) who died in 1982 used to keep quoting the line that “foolish consistency is the hobgoblin of a petty mind” and I think this applies to my comments below.  There may be exceptions to all of rules I discuss below and concentrating too much on bureaucratic rules is the worst rule to break.

![](https://edbodmer.com/wp-content/uploads/2019/07/Foolish-Consistency.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/05/Jail-Picture.jpg)

*   _**Obviously, no hard-coded numbers after assumptions**_ in the model.  This is a clear crime and an even worse crime is mixing a formula with hard coded numbers like F5 \* 1.02.  The first can be solved with F5, paste special, constants or with Generic Macros.  The second problem is more difficult to find and mark with colours.  [To see how to use the F5 method with a little macro, go to the short-cut page.](https://edbodmer.com/useful-short-cuts/)
    
*   _**Not putting driving factors in the left column, fairly obvious.**_ Why in the hell do people not put the driving factors in the left column before the period by period formulas. I want to see what items drive the equation without looking at formulas that have references to other sheets in the model. See the example below if you are worried about putting titles on the driving factors.
*   _**Not making formulas the same across columns, another obvious one.**_ You can make the formulas the same across the columns with TRUE/FALSE or 1/0 flags, or whatever you call them. But don’t go crazy and not allow a starting point for things like inflation indices. Remember, being too bureaucratic about this stuff is about the worst thing you can do.
*   _**Wasting time on meaningful or meaningless colours**_ is one of the most irritating things I have to put u![](https://edbodmer.com/wp-content/uploads/2019/05/color-pane.jpg)p with when I watch people make a model in excel. That is why I made the colouring page that allows you to find the location of other sheets and stop wasting time. [Go to the link attached to this sentence to see the new stuff in generic macros.](https://edbodmer.com/using-generic-macros/)
    
*   _**Use IF instead of MAX and MIN functions to connect the cash flow with the debt schedule.**_ There is always a direct or indirect connection of the debt schedule with the balance sheet — no cash flow and no debt repayment.  The MIN and MAX (never IF statements) should be in the cash flow waterfall and not in the debt schedule.
*   _**The Assumptions should be in the same order and structure as the model and they should make sense.**_  Some models should begin with operational cash flow if it is possible to size the debt from the CFADS with sculpting.  In other cases you may start with development costs and capital expenditures if debt is set from a debt to capital ratio.
*   _**Putting too many flags, masks, switches (whatever you want to call them) in a separate page instead of where they are used right next to the calculations.**_ Flags or switches or masks are wonderful.  They are digital.  They turn things on and off.  They are a necessity in a project finance model.  It is not necessarily bad to have a separate page of flags, but if you are going to use them, put them right next to the place they are used.  Do not multiply some number by a flag in a different page. Why force people to make silly traces with those blue arrows to find things that are driving the model (even if they have a fancy add-in).![](https://edbodmer.com/wp-content/uploads/2019/05/smooth-flow.jpg)
*   _**Placing the forecast financial statements at the beginning of the model.**_  Structuring is the biggest deal of FAST and other blah, blah, blah acronyms. Structure comes from my hero, Merton Miller who won a noble prize for suggesting that financing should be separate from operations. You should begin your model with pretax cash flows, after-tax cash flows that have no debt.  Then you can move to construction financing with a summary sources and uses, then debt sizing, debt schedules with repayment and interest and then, finally the profit and loss and the cash flow statement (the flow should be natural). You can put the statements at the beginning, but the calculation is made after the other stuff.
*   _**Splitting up pages when you are designing the model instead of letting the model smoothly flow down a single page.**_ I even think you should leave the model on a single page after you are finished and not split it up. Please put yourself in the position of somebody trying to understand the model. Your model should have a natural flow and it is so much easier to follow a model on a single page. Use little columns on the left so you can see the structure of the model.
*   _**Deceiving yo**__**urself that you are smart because you make a long and complex formula.**_ Use of formulas that are too long is inexcusable and always avoidable. The key to making models transparent is separating formulas and making them short.
*   **_Please no bullshit excel stuff._** Don’t ever merge cells; no silly and useless macros to go to sheets; no useless pages with currency lists; one good graph on debt service and cash flow and not twenty useless graphs or no graphs; no hour by hour data with OFFSET when this is not necessary.  These are things that I have gone crazy about in reviewing models.  You can see some of the excel stuff that is not impressive at all at the bottom of this page.
*   _**Showing off your excel prowess by applying unnecessary functions.**_ You can do just about everything with three excel functions — LOOKUP, INDEX and SUMIF.  LOOKUP is more efficient and easier to use than INDEX, MATCH and OFFS![](https://edbodmer.com/wp-content/uploads/2019/05/Lookup-1.jpg)ET is unnecessary. When you use LOOKUP please click on the entire lines rather than wasting time fixing cells.
*   _**No formulas in the balance sheet.**_ When you make a model all or the balances for debt, DSRA, net plant and other things should be in various structured sections of the model.  The only balance that is not there in your model is the equity balance, which you should compute after the Formulas in the balance sheet rather than links to closing balance
*   _**Don’t go overboard to show off your auditing skills.**_ Use TRUE/FALSE switches for checking the balance sheet, debt balances and circular references, but you do not need to go overboard. I do think it is good to put sums in a column and check things as your are making your model.
*   _**Don’t pollute your fundamental models with multiple scenarios.**_ Put the scenarios in a separate sheet (except P99 or P50) and let the scenario sheet be a mess with the index function and code numbers.
*   _**Don’t make summary sheets complex**_. A simple rule is that output sheets can be deleted without affecting the model.  This is pretty obvious that you do not want to mix outputs and inputs. Put _**![](https://edbodmer.com/wp-content/uploads/2019/05/Summary.jpg)**_your summary on one page so you do not have to look around. Include IRR’s, DSCR, LLCR, a graph of cash flow versus debt service, a sources and uses summary and key drivers such as capacity factor, cost per kW, levelised O&M cost and the plant capacity.  Then you can even call it a dashboard if you need to.
*   _**Don’t use the NPV or XNPV formula when interest rates are changing.**_ Use a compound factor when interest rates are not constant and then compute the present value with the SUMPRODUCT function where you divide the cash flow by the compound factor.
*   _**Putting fourty flags in a separate sheet sucks.**_ You need an construction phase and operating phase at the top of your single sheet. But do not put too many of them at the top of a separate sheet (this will be very  controversial for the dushbags who believe they are following some kind of best practice standards like SMART). You can certainly have a page that carefully works through time lines and maybe even have different time lines on different pages.  But for the flags associated with debt repayment or contract length should be right next to where you are going to make the calculations.![](https://edbodmer.com/wp-content/uploads/2019/05/Time-Switches.jpg)
*   _**Find a good style and don’t listen too much to me.**_  I like the positive number convention. I like the using underlines for key items. I like using thin columns at the left and then reserving a lot of columns before the model starts for drivers.
*   _**Take the side of Anti-Range Namers.**_  The range name controversy could be a subject at an excel party that you may have on a Saturday night.  There should not be an argument.  Except for macros, and a couple of minor things range name suck. Some companies try to make you put range names in excel cell.  This adds a log of time and if you have simple formulas, it adds nothing to the accuracy or transparency of a model.
*   _**Don’t chimp on sub-totals in the cash flow waterfall.**_ Sub-totals are important in cash flow waterfalls so that you can use MIN and MAX functions. Connect the debt schedule with the sources and uses and also the cash flow waterfall.  I believe (and I am in a minority) that you should keep the accounts that will be connected to the debt schedule in the same page as the . Why would you make people search for basic and obvious links.
*   _**When using the goal seek tool, use the NPV = 0, rather than an IRR difference equals zero.**_  When, the IRR cannot be computed, the goal seek can go crazy like we all know.  As you know when the NPV is zero, the IRR is the discount rate. It is much better to use the NPV rule.
*   _**Don’t compute the project IRR from CFADS.**_  That is a basic mistake in finance theory; instead compute the project IRR before any finance equations are in the model.  The project IRR is supposed to measure the IRR that would be realised by investors if there was no debt financing — meaning no IDC, no fees, no tax effects of interest, no DSRA, no L/C fees etc.  Make this computation before you make the debt calculations.
*   _**Work on the nightmare blue lines from circular references last.**_  While working on your model, try to avoid circular references by doing things like using EBITDA instead of DSCR and construction expenditures instead of total funding uses.
*   _**Don’t Make a Crazy Complex Set of Inflation Indices.**_ It is really irritating to work through many different inflation indices with daily compounding and waste a lot of time checking the numbers.  Just keep the inflation consistent with exchange rates and interest rates and make it simple.  I am writing this because I am so pissed off about having to review four long sheets of different inflation indices for many items that are not even consistently computed.  This is real fortune telling and worthless modelling.

.

Setting-up Model Sheets and Structure (The S in FAST)
-----------------------------------------------------

In discussing modelling philosophy, I have chosen to be flexible rather than perfectly structured (if you think about your life, sometimes it is good to be structured, sometimes it is better to be flexible and many times these objectives conflict).  The people taking care of my 90 year old father tend to be very structured and only take him out bed at very distinct and distinct times.  But I think they should be more flexible and if he is moaning that he is tired, just let him relax and sleep.  It will not make much of a difference in the world. This is the conflict.  For modelling, you may want to begin with the Structuring part of a model.  Structuring issues essentially involve where should you start (with a time line) and how the model should progress.  These issues in turn drive the order of the assumptions in your model.

### Sheet Order – Depends on Debt Sizing Method and Your Opinion

Option 1 – Development, Construction, Sources and Uses, EBITDA, Debt: Time Order of Constructing and Financing Projects. Use the following order of items and put in different sheets.  This works when the financing is set from the capital expenditures and not from the CFADS. Start with development; move to EPC and construction; sources and uses of funds with financing; operations with revenues and expenses; depreciation, debt schedules and finally financial statements with a cash flow waterfall. In this case, the sheet order may be:

*   Input Scalars
*   Input Time Series
*   Sheet with Time Line Analysis (Simple Formulas)
*   Development and Capital Expenditure Analysis
*   Construction Financing with IDC, Fees and Other Thing that Cause Circular References
*   Operations Analysis starting with capacity and volumes including EBITDA
*   Debt Schedules with Repayment and Interest
*   Waterfall and Financial Statements

At the beginning of the model there should be standard summary sheets the present the IRR’s, DSCR’s and other data.  In addition there should be a scenario sheet and an annual summary sheet.  An example of the sheet order is shown in the screenshot below.  This table of contents was created from the generic macros file after you press CNTL, ALT, C.  You can go to the webpage for generic macros and see how this

![](https://edbodmer.com/wp-content/uploads/2019/07/Contents.jpg)

Option 2 – Merton Miller and Splitting up Operations from Financing: Begin with Operations and No cash; move to free cash flow without finance; then evaluate debt size from CFADS; then work on the sources and uses and finally taxes and cash flow waterfall. This works better when the debt size may occur from CFADS.  If the debt can come from cash flow, you need the cash flow as well as the capital expenditures before you can derive the debt. In this case I strongly suggest a debt sizing section that is different from the basic debt schedule in the model. The sheet order may be:

*   Input Scalars
*   Input Time Series
*   Sheet with Time Line Analysis (Simple Formulas)
*   Operations Analysis starting with capacity and volumes including EBITDA
*   Debt Sizing from CFADS (this will include a circular reference)
*   Construction Expenditures and Financing (with more circular references)
*   Debt Schedule and Waterfall
*   Summary of Financial Statements

As with the other structure above where debt is derived from the uses of funds, there should be standard summary sheets the present the IRR’s, DSCR’s and other data at the beginning of the sheet.  In addition there should be a scenario sheet and an annual summary sheet.

When you set-up sheets, you should put the order of the inputs in the same order as the way the assumptions are used in the model.  You should start with dates and then move to macro-economic data and operations.  You could also start with development costs and capital expenditures.  In my opinion the financing should be after all of the operations, capital expenditures and revenues. Some people separate time series inputs from scalar inputs and put the time series inputs in InputS while the scalar in InputC. An example of what not to do is shown in the screenshot below.  Here the inputs do not start with dates and the fancy colouring is in my opinion very irritating. The silly macros that go to the audit checks drive me crazy.  I hope you are not impressed by this type of idiocy.  I also object to the different fonts (where the name General has a larger size than the inputs, and the different colours that do not show you when you are moving to a different section of the model.

![](https://edbodmer.com/wp-content/uploads/2019/07/Input-problems.jpg)

A better example of an input structure is shown in the screenshot below. You should start with the timing inputs; separate inputs in that are constants in one sheet from inputs that are time series that should be in another sheet.  You should also use the generic macros file to colour the section headings and the inputs.  After this section, you could move to the development cost section or the operating inputs section depending on how the sheets of your model are structured.

![](https://edbodmer.com/wp-content/uploads/2019/07/Inputs-Better.jpg)

### Spreadsheet Structure in Model

In the model below, the sheet structure made my head spin and looking at it still makes me a little crazy.  The debt was sized from the CFADS, but you had to go to the control sheet to find the debt size, which in turn came from yet another sheet in the model and created a horrible to trace circular reference that was solved with the iteration button. To fix this I suggested beginning with a cash flow analysis and a section for evaluating debt size.  This debt goes into a summary sources and uses statement can construction financing after the cash flow statement.

![](https://edbodmer.com/wp-content/uploads/2019/07/No-Nice-Flow.jpg)

Formatting Sheets in a Project Finance Model (The T in FAST)
------------------------------------------------------------

After many years, I am more and more a believer in effectively and efficiently using the columns at the left of the sheet and using colours to point out where numbers come from.  It drives me crazy when people show off by very quickly pressing CNTL, 1 or some other short-cut and colour cells one by one.  Indeed, I see people very proud of their mastery of colouring cells with their mac. [I have made much of the generic macro program in response to this and you can go to the link to see how to use it efficiently.](https://edbodmer.com/excel-utilities-and-backpack/generic-macros-file/)
  I suggest efficiently using the columns to the left to make your model much more transparent and easy to read and understand. Many people only present the units and the sum column.  But when you put the drivers of each equation in the left column, the model becomes much more transparent.  In the example below the constants come from the input sheet and I have used the generic macro sheet to demonstrate when a number comes from another sheet. Note that in this case where numbers in the left come from another sheet, they are coloured in red.  This is done automatically with the generic macros file.

![](https://edbodmer.com/wp-content/uploads/2019/07/Revised-Format.jpg)

I have collected many examples of what not to do for the various formatting and excel issues.  The  example in the screenshot below shows what a pain it is when the drivers are not on the left.  Then, if you are auditing a model to understand what is going on, you will waste a lot of time with the trace precedent.  Instead, as in the second screenshot, you can out the drivers in the left columns.  Now the drivers are in the left column and not included in the formula where you cannot really see what is happening.  I hope you can see that it is much easier to understand what is happening in the second example where I have shown the formula.

![](https://edbodmer.com/wp-content/uploads/2019/07/Use-Left.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/07/fixed.jpg)
--------------------------------------------------------------

In the screenshot below, I show another another example of not putting the drivers in the left column because I am obsessive about this. The example in the screenshot below is a horrible formula where you refer to values from another sheet instead of putting the values over to the left. Clearly the Input P130 should be in the left hand columns so you can see what is going on.

![](https://edbodmer.com/wp-content/uploads/2019/07/Not-Impressive-4.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/07/IF-and-not-Min.jpg)

Timelines and Consolidating Periodic Periods into Annual or Quarterly Statements (The F in FAST)
------------------------------------------------------------------------------------------------

Developing dates and timelines and putting the timelines at the top of each sheet is a standard part of financial modelling and included in all of the regular old blah blah blah classes that you can get elsewhere.  Formulas for establishing dates and switches (or flags or masks or whatever you want to call them) is very standard.  One issue that is a bit tricky is being careful about annual analysis when moving from monthly to semi-annual cash flows. Another tricky issue is accumulating monthly data into semi-annual data or consolidating quarterly data.

Make a Master Time Line
-----------------------

At some point you will want to compute an IRR that includes monthly periods and semi-annual periods. So many models have many different time lines and this really messes up the model. A really horrible thing is to see all of the accounts put on a monthly basis in some sheets for the pre-cod periods and then put in a post-cod with different time lines.  Why in the hell would you not just make one master time line that is flexible enough to account for different situations.

### Timeline Examples – Keeping Useful Flags on the Top of the Sheet

In the next few paragraphs, I put some examples of what to do and what not to do when you are setting-up your time lines.  In the first screenshot below I suggest that you should fine the time line switches like and operating flag or a flag that is date when the availability period of a loan turns into a term loan.  You also often want to see the number of days for computing periodic interest rates. So, put key timelines that you will use over and over again at the top of the page as in the example below.

![](https://edbodmer.com/wp-content/uploads/2019/07/Using-Flags-at-top.jpg)

In the screenshot below I show a counter example where there is no time line at the top of the page and no useful switches.  You can see that the timeline is in line 21 and there are no 1/0 or TRUE/FALSE switches that you can use over again at the top.  For each page, it is basic modelling concept that a time line is at the top.  Further, the formulas should be simple and not like the formula shown in the screenshot.

![](https://edbodmer.com/wp-content/uploads/2019/07/Timeline-at-Top.jpg)

The next example of time lines is even worse.  Here the year is a fixed number as shown in the formula box.  This means that the date of the financial close or the commercial operation cannot be changed.  This is a simple and dramatic error rendering the model very inflexible (counter to the F in FAST modelling). Please do not ever do this.

![](https://edbodmer.com/wp-content/uploads/2019/07/Time-Line-Problems.jpg)

### Fiscal Year End and Accumulation of Periodic Data into Fiscal Years

For the fiscal year used in the annual page, you want to find the end of the month before the COD.  You can just use EOMONTH function and enter -1 for the month  — EOMONTH(COD,-1).  Then find the month of this date using the MONTH function.  Once you have the month end for the fiscal year, enter a switch that is true whenever the end month in the main time line is equal to that month.  You should create the year of the date with the formula that the year changes when the fiscal month is reached. To do this use an IF formula — IF(MONTH(end date in time line) = Month End defined above, Year = year +1, prior year).  This makes a year counter that increments whenever the fiscal year end is true.

The process is shown in the two screenshots below.  The first screen shot is really the key.  Note that the commercial operation date is 1 August 2023.  You need to find the prior month (including if the month happens to be December).  This month can be used to drive the SUMIF function.  Note that instead of using the function MONTH(COD) – 1 which would not work for January or December, you can use the EDATE with -1 for the month and then put the month around the EDATE.  The formula is:

Month of Fiscal Year End = MONTH(EDATE(COD,-1)).

![](https://edbodmer.com/wp-content/uploads/2019/02/A-Z-Define-Month-of-Fiscal-Year.png)

The second part of this method is shown in the screenshot below.  In this example, the COD date using the standard monthly analysis is 1-May-2018.  This means the fiscal year end will be April.  But when the model switches to semi-annual mode, the month of April is in the ending date and not the beginning date.  But you want the switch for a new year to start after the closing date.  So you should take the PRIOR closing month and use that in the test.  Once you have done all of this you can use the computed fiscal year end rather than the calendar year computed from the start or end date.  The fiscal year is computed from the prior fiscal year and changing the year when the switch is TRUE. This sheet uses the generic macro program to point out when a flag is on or off.  [Go to the generic macro discussion to see how to do this automatically.](https://edbodmer.com/excel-utilities-and-backpack/generic-macros-file/)
 In this example again, the numbers in the left (the dates) that come from another sheets are coloured in red (you could also colour the cells according to the sheet name).

![](https://edbodmer.com/wp-content/uploads/2019/07/Time-Line-Revised.jpg)

### User Defined Functions for Quarterly and Semi-Annual Time Lines

Most of the time, creating a timeline is pretty straightforward.  You can count the months pre-COD and create a timing switch that is 1 for the monthly periods and 6 for the semi-annual periods (or 3 for quarterly periods).  Then you can use the EOMONTH or EDATE function to count the months (if you use the EDATE function, subtract 1 for the end of the month.  If you use EOMONTH, subtract 1 inside the formula.  Sometimes when you use a half-year model, you may need to aggregate months into half years.  You can use the user defined functions below to compute the appropriate half year or quarterly date from the monthly date.  If you use quarterly time periods or monthly periods that will be converted to semi-annual flows, the following user-defined functions may be useful.  The first function returns the end of the half year period given the date.  The second function returns the end of the quarter.  These functions should be part of excel.

Function eohy(date1) 
month\_of\_date = Month(date1) 
If month\_of\_date = 1 Or month\_of\_date = 7 \_ 
     Then eohy = WorksheetFunction.EoMonth(date1, 5) 

If month\_of\_date = 2 Or month\_of\_date = 8 \_ 
     Then eohy = WorksheetFunction.EoMonth(date1, 4) 

If month\_of\_date = 3 Or month\_of\_date = 9 \_ 
      Then eohy = WorksheetFunction.EoMonth(date1, 3) 

If month\_of\_date = 4 Or month\_of\_date = 10 \_ 
    Then eohy = WorksheetFunction.EoMonth(date1, 2) 

If month\_of\_date = 5 Or month\_of\_date = 11 \_ 
     Then eohy = WorksheetFunction.EoMonth(date1, 1) 

If month\_of\_date = 6 Or month\_of\_date = 12 \_ 
     Then eohy = WorksheetFunction.EoMonth(date1, 0) 

End Function 



Function eoqtr(date1)

month\_of\_date = Month(date1)

If month\_of\_date = 1 Or month\_of\_date = 4 Or month\_of\_date = 7 Or month\_of\_date = 10 \_
Then eoqtr = WorksheetFunction.EoMonth(date1, 2)

If month\_of\_date = 2 Or month\_of\_date = 5 Or month\_of\_date = 8 Or month\_of\_date = 11 \_
Then eoqtr = WorksheetFunction.EoMonth(date1, 1)

If month\_of\_date = 3 Or month\_of\_date = 6 Or month\_of\_date = 9 Or month\_of\_date = 12 \_
Then eoqtr = WorksheetFunction.EoMonth(date1, 0)


End Function

A final issue is what happens when you have a model that does not end in months like December that is the fiscal year of the company.  In this case you may want to pro-rate the data and put some of the amounts in a prior period or a future period for annualisation.  I address this issue at the bottom of this webpage.

**[Generic Macro File that Allows you to Copy to the Right (Shift, CNTL, R) and to Colour and Format Sheets (CNTL, ALT, C)](https://edbodmer.com/wp-content/uploads/2019/07/Generic-Macros-1.xlsm)
**

Auditing with Tests and Balance Sheet (The A in FAST)
-----------------------------------------------------

This section addresses the A in FAST which I call accuracy. You should create some kind of checks when making your model which is really not a very elaborate thing to do. When making audits, you can overdo things.  One necessity is to make a balance sheet and test that it balances in each year. In this case I start with a bad example where a balance sheet was not included.  When you have a lot of MIN/MAX functions in the cash flow statement and multiple debt issues, the balance sheet check is important.  In the example below, there was no balance sheet.

![](https://edbodmer.com/wp-content/uploads/2019/07/No-Balance-Sheet.jpg)

The screenshot below illustrates how you can use one of the formulas to the left to make tests.  You could throw all of these tests into an audit page.  But when you make the audit tests too complex and too extensive, people will stop paying attention. The real tests are probably three.  First, the balance sheet must balance. Second, the debt must be fully repaid. Third, the circular references in the construction financing and created from debt sculpting must be resolved correctly. The example below is for a test in one of the left columns and makes sure there is only one flag that is on.  Note that the conditional TRUE/FALSE formatting also may help.  Note again, how the conditional formatting from the generic macros works where the flags that are on are in green and the flags that are off are in grey.

![](https://edbodmer.com/wp-content/uploads/2019/07/Example-of-Test.jpg)

A bad example of auditing is shown below. In this case a TRUE/FALSE is not used and there is an absurd use of quotes in the test as well as a long OR function.  Finally, the OK rather than a TRUE/FALSE is used as the output.

![](https://edbodmer.com/wp-content/uploads/2019/07/Bad-Audit.jpg)

Using LOOKUP with Entire Row or Column
--------------------------------------

In this section I discuss the LOOKUP function which is one of the few functions (including INDEX and SUMIF) that is really useful in your models.  When using this, please be one of the few people in the world who uses the entire row or column instead of wasting time pressing the F4 to lock in cells.  I promise that this will speed up your programming and it will not make your models heavy. The first example in the screenshot below illustrates the crime of using VLOOKUP where you have to input the row number 2. The screenshot shows that people still waste time with the VLOOKUP function — if you insert a line, the whole formula breaks down.

![](https://edbodmer.com/wp-content/uploads/2019/07/Vlookup-problems.jpg)

Almost as irritating as using VLOOKUP or HLOOKUP is wasting time by pressing the F4 when creating the lookup function.  This is illustrated in the next couple of screenshots.  The first screenshot makes me start to shake because of the utterly useless colours.  The formula shown above the sheet must have taken a long time to enter and it is not transparent. The second screenshot is almost as bad and is a typical thing that you see in models.  The general rule is that when you take items from the input sheet that is expressed in time series, then you should use one single lookup function.  In the lookup function, you can see the line that is used in the time series file.

![](https://edbodmer.com/wp-content/uploads/2019/07/Numbers-in-Left.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/07/Waste-of-Time-on-Lookup.jpg)

An efficient use of LOOKUP is shown in the screenshot below. In this case the entire line 68 from the time series is used and the line 70 is used.  This should be clear from the formula.  In general, the only time that you take things from an input file that are not in the left column should come from the LOOKUP formula.

![](https://edbodmer.com/wp-content/uploads/2019/07/Lookup.jpg)

Using SUMIF with Entire Row or Column
-------------------------------------

The SUMIF or SUMIFS functions are the third kind of function that should be used in an elegant manner in a model (other than LOOKUP and INDEX).  The most basic use of these functions is to aggregate periodic data (monthly, quarterly or semi-annual data) into data that you can read and interpret.  The screenshot below illustrates use of the SUMIF function.  Note that if you lock in the rows on the detailed period sheet (in this case IFS) and you lock in the row but not the column number and do not lock in anything for the entire row, you can create an annual sheet in seconds.  To create balance sheet accounts, you can use the SUMIFS function with a flag for the end of the period.

![](https://edbodmer.com/wp-content/uploads/2019/07/Annual-with-Sumif.jpg)

### SUMIF for Aggregating Across Debt Issues

Another use of the SUMIF is to aggregate debt issues using code names. My suggestion is to not engage in the torture and dangerous simple sum functions. Instead of this, you can use the SUMIF with code names. A big use of SUMIF is for the annual totals as shown in the example below.

![](https://edbodmer.com/wp-content/uploads/2019/07/Using-SUMIF-for-totals.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/08/Fiscal-Year-Analysis.jpg)

Why Range Names Suck
--------------------

There are many reasons not to use range names.  They are particularly painful when importing sheets from one file to another file and some of the range names in the two files are the same.  I think they can can be used for a very few items like the unit names or maybe dividing by 12 months per year or 360 days per year.  You can trace the location but it is a pain.  They can result in errors as shown below.

![](https://edbodmer.com/wp-content/uploads/2019/07/Why-Range-Names-Suck.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/07/Split-Screen-for-Inputs.jpg)

INDEX Function and Trying to Impress with Fancy Excel Formulas
--------------------------------------------------------------

I have repeated over and over again that all you really need to do is focus on the INDEX, LOOKUP and SUMIF. You can do just about anything with these functions and you do not need many added functions.  The example in the screenshot below uses OFFSET and is largely a waste of time. Why in the hell would you use the offset formula instead of a simple CHOOSE or INDEX formula.  The second example the OFFSET function is used again with hourly data that is useless in a financial model.

![](https://edbodmer.com/wp-content/uploads/2019/07/Why-Use-Offset-instead-of-Index.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/07/Proving-Prowess-in-Excel.jpg)

What is Not Impressive in a Model
---------------------------------

It is very nice that you can use the CNTL, 1 short-cut and then make the number 1 appear as yes or as “On” as shown in the example below.  Isn’t it much nicer to just use TRUE and FALSE where you can even attach a check box.  The same is for Yes and No below.  You can make this by pressing CNTL, 1 and then go to the general section and then put in “Oui”;;”Non”.

![](https://edbodmer.com/wp-content/uploads/2019/07/Not-Impressive-6.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/07/Not-Impressive-3.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/07/Fancy-Formatting-Waste-of-Time.jpg)

When you use an IF statement with 1 and 0 or TRUE and false, you should realise that IF(TRUE, true condition, false condition) results in TRUE and that any number other than 0 is true.  This means that when you want to test a denominator with an if statement, you can use IF (B,A/B).  When B is anything other than zero, this gives you the result A/B.  When B is zero, this gives you FALSE.

![](https://edbodmer.com/wp-content/uploads/2019/07/Not-Impressive-5.jpg)

Useless Macros and Inconsistent Formatting
------------------------------------------

Scenarios and the INDEX Function
--------------------------------

There are many ways to make scenarios in a model and I have an entire set of web pages discussing scenario analysis.  But there are a couple of things that are very basic for any scenario analysis.  First do not muck up your input sheets with a bunch of scenarios.  Second, always use a code number and the INDEX function.  An example of really messed scenarios is illustrated in the screenshot below.

![](https://edbodmer.com/wp-content/uploads/2019/07/Mixing-Up-Scenario.jpg)

![](https://edbodmer.com/wp-content/uploads/2019/07/Mixing-Formulas.jpg)

Don’t put some sheets with vertical layout and other sheets in horizontal format.

![](https://edbodmer.com/wp-content/uploads/2019/07/Dont-put-some-stuff-in-rows-and-others-in-columns.jpg)

.

Penalties
---------

### Crime                                                          Suggested Penalty

Use of Merge  Cells                                                          No Coffee for a Day

Fixed Cells in Financials                                                No Wine for Lunch During Day

Too Long Formulas                                                         No Cell Phone for a Day

VLookup or Hlookup                                                      Middle Seat on Next Flight

Changing Formulas in Column                                     Watch Three Bodmer Videos in a Day

Meaningless Colours                                                       Go to DisneyWorld without Laptop

Monthly Timing when Not Necessary                        Lay on Beach without Excel Book

Too Many Range Names                                                Not Allowed to Use Short-Cuts for a Week

Not Separating Funding and Operations                    Read Other Peoples 40 Page Models Every Night

Impressing People with OFFSET                                 Not allowed to use excel; only read documents

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=8367&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=12792&rand=0.5484628347566151)