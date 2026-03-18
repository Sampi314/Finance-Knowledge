# Files and Videos for Weekend Sessions

**Source:** https://edbodmer.com/files-and-videos-for-weekend-sessions

---

This page includes files and videos that we are using in our weekend sessions where a few people are so crazy that they would take a few hours out of their weekend to discuss various different modelling issues. I have tried to design the modelling sessions as a reasonablly advanced modelling course were we discuss some nuanced issues as well as the theoretical basis for the modelling. I begin with timeline issues and operating cash flow for a single project. With different time lines some issues related to IRR can be addressed. After that, I have tried to move to more and more complex issues. For each session I try to include some theory to begin the discussion and then we practice some excel so that you can learn the fundamentals of modelling and then progress to more advanced subjects. I try to mix corporate finance issues with project finance issues so you can get some experience with both. Even if you are beginning with modelling, please do not be intimidated by some of the more advanced subjects. You may have an advantage because you do not have to unlearn modelling techniques. I have put a little explanation for each session below. I have also attached various files that you can practice with.

I appreciate everybody who is using the materials or participating. Especially Hedieh, Brian, Jash, Abdulhaliack, Nicolia and everybody else. If you have any suggestions for subjects to cover in future sessions, please send me an email at edwardbodmer@gmail.com.

.

Files and videos for Session 1: IRR Calculation with Different Time Lines
-------------------------------------------------------------------------

In the first session I cover issues with time lines and use the alternative timelines to compute IRRs in different ways. I also introduced the generic macro file for formatting and not wasting time on various movements around excel. When working through timelines I show that IRR’s are growth rates where the growth includes re-investment of cash at the IRR itself. This results in some distortions where if there is a high IRR, the value of cash flows far into the future is low because the out year cash flow is discounted at the IRR itself. To demonstrate issues like this, I use flexible time lines which are part of any financial model. For a project finance model I demonstrate the importance distinguishing between the construction period and the operating period. I also want to show the effect of different cash flow on the IRR and to do this I introduce the concept of an InputC sheet. For the first session, we started from a blank model and then worked through timelines without the ridiculous complicated equations that are not necessary (the second video shows how you can incorporate the timelines in more complicated situations with partial year construction and partial year operation). The excel file that has been completed in the first session is attached to the blue button below.

.

 **[Excel File from First Modelling Session with Timeline, IRR calculation and Alternative Risk Premium Calculation](https://edbodmer.com/wp-content/uploads/2025/08/Cleaned-Financinal-modelling-class-09.08.2025.xlsm)
**

.

.

In the first session, somebody asked about more complex timelines where the project begins construction or operation in the middle of a period. In the video below I address the issue which again involves starting with a construction period flag. In this case, I suggest computing the amount of days in the period of the last month of construction and the first month of operation. There are a couple of added rows to add to the time line.

.

.

#### Files from the second session

In the second session we extend the file from the first session to include debt. We begin with a simple structure and illustrate the fundamental concepts of a cash flow waterfall. As part of the session we will compute and more importantly understand the LLCR and PLCR ratios and compute the equity IRR. In the second session we will not waste time on typing in titles and focus on the equations and the model structure. The file will be used for Monte Carlo analysis in section 3.

.

**[Excel File on Fundamental Debt Structuring with Blanks that will be Completed in the Session](https://edbodmer.com/wp-content/uploads/2025/08/File-for-Session-2-15.08.2025-Exercise-1.xlsm)
**

.

**[Filled In File with Debt Structuring and Monte Carlo Simmulation with Completed Equations for Demonstration](https://edbodmer.com/wp-content/uploads/2025/08/File-for-Session-2-15.08.2025-Filled.xlsm)
**

.

I will continue to make videos that recap each session. I go a little more quickly than the course and of course you can pause the video if you want work through the case.

.

Files and Videos for Session 3 – Completion of Ratios, Sensitivity with VBA, Monte Carlo Simulation
---------------------------------------------------------------------------------------------------

The third session will move to sensitivity and Monte Carlo simulation. We will do some VBA to complete the analysis. The file with blanks to complete the session is attached to the button below. I have also included a solar project finance model that uses the same kind of format, time lines, InputC and InputS and other things as the file we have been working on. The solar model is attached to the second button below. I have made an entire video of the third session because I think there was more discussion about the theory of how volatility and mean reversion affect the target DSCR to achieve a BBB- rating or equivalent.

.

.

 **[Excel File with Exercises for Session 3 - Ratios, Sensitivity Analysis with VBA and Monte Carlo to Compute DSCR](https://edbodmer.com/wp-content/uploads/2025/08/File-for-Session-3-22.08.2025-Exercise.xlsm)
**

.

**[Excel File with Updated Solar Model Using Flexible Time Line, VBA for Goal Seek and Sensitivity Analysis](https://edbodmer.com/wp-content/uploads/2025/08/India-Solar-Model-1.xlsm)
**

.

[Excel File with Updated Solar Model Using Flexible Time Line, VBA for Goal Seek and Sensitivity Analysis](https://edbodmer.com/wp-content/uploads/2025/08/India-Solar-Model-1.xlsm)

.

 **[Excel File with Completed Equations and Completed Sensitivity for Session Three with Monte Carlo](https://edbodmer.com/wp-content/uploads/2025/08/File-for-Session-3-22.08.2025-Exercise-after-class.xlsm)
**

.

Session 4 – Valuation of Projects, Transaction Analysis and Pro-Forma M&A Model
-------------------------------------------------------------------------------

.

In the fourth session we cover subject of valuation, constructing a transaction analysis with possible re-financing and accounting issues and finally a pro-forma analysis with in an M&A context. I emphasize the theory behind project finance valuation which depends entirely on the discount rate applied. I suggest that a big issue in valuation is the difference between the initial discount rate and the discount rate when the plant is sold. We will show that traditional corporate finance ratios are not useful and go even further to suggest how these ratios are distorted in other contexts. The session will cover basic debt sculpting and how you can quickly develop financial statements.

.

[Excel File for Session Four with Exercises for Valuation, Transaction Analysis and Pro-Forma M&A Model from Project Finance](javascript:void(0);)

.

 **[Power Point Slides with Theory Discussion and Introduction to Various Sessions for Weekend Course](https://edbodmer.com/wp-content/uploads/2025/09/Course-Outline.pptx)
**

.

.

*   Step 1: Start at end after stable period with required return for buyer
    *   Can get data from transactions
    *   If not can add a little bit to the interest rate
*   Step 2: Decide on a reasonable holding period
    *   Should have some history
    *   The shorter the period the higher the returns
*   Step 3: Make an estimate of how much higher an IRR you need for taking resolved risks
    *   Risks are development risks, construction over-run and delay, volume estimation, operating and maintenance levels etc.
    *   To think you can somehow quantify these risks with the Capital Asset Pricing Model and Beta is ridiculous
    *   For example, add 4% for initial risk to get the target equity IRR
*   Step 4: Run goal seek for price with target IRR
    *   Go to the portion of the model with the IRR after the plant sale and the holding period
    *   Compute the NPV of the holding period cash flow using the target IRR from Step 3
    *   Use goal seek to find price to meet the target return that covers these risks

.

![](https://edbodmer.com/wp-content/uploads/2025/09/image.png)

.

Session 5 – Debt Sculpting, Financing a Transaction and Re-Financing
--------------------------------------------------------------------

.

In the fifth session we continue the discussion of a transaction and we add debt financing to the transaction. We use debt sculpting to size the debt of the transaction using the formula that the size of the debt is the present value of cash flow and also that the debt service is the cash flow divided by the DSCR. The update to the point slides that discusses the debt sizing in the context of an acquistion with a transaction page are attached to the blue button below.

.

 **[Power Point Slides with Theory Discussion and Introduction to Various Sessions for Weekend Course](https://edbodmer.com/wp-content/uploads/2025/09/Course-Outline.pptx)
**

.

The key sculpting formulas that we will use also for re-financing and multiple debt issues are summarised below. You can compute the value of the debt with a goal seek macro, but it is much better to use the mathematics.

•Basic Formulas

*   DSCR = CFADS/Debt Service
*   Debt Service Target = CFADS/DSCR
*   PV of Debt Service over Repayment Period = Initial Debt Balance
*   Debt Service = Interest + Repayment
*   Repayment = Debt Service – Interest
*   If you have annual or semi-annual cash flow and constant interest rate you can use the NPV formula

•More Advanced Formulas

*   DSCR = CFADS/Debt Service Including Fees
*   Debt Service Including Fees = CFADS/DSCR
*   Repayment + Interest + Fees = CFADS/DSCR
*   PV of Repayment + Interest = Debt
*   Debt Balance = PV of CFADS/DSCR – PV of Fees

If interest rates not constant, use an interest rate index (monthly or semi-annual)

*   Multiple Issues: DSCR = CFADS/(DS1 + DS2 + DS3)
*   DS1 = CFADS/DSCR – DS2 – DS3
*   If DS2 and DS3 Given, PV of CFADS/DSCR – DS2 – DS3 = Debt Balance

.

.

Session 6 – Debt Sculpting Complications; Negative Repayment
------------------------------------------------------------

.

In this session we finish the discussion of debt sculpting and address the issue that occurs when debt service from the formula below is greater than the interst expense, which would imply negative repayment.

Debt Service = CFADS/DSCR produces a lower debt service than the interest expense.

The most common (and costly) solution is to try and set up a cash reserve account. This can be painful in models because you cannot simply evaluate the amount of negative payment. Instead, the amount set-up in the reserve must be adequate to provide the target DSCR. In addition there can be a problem with the repayment where the negative repayment is removed. If the negative repayment is eliminated, the repayment will increase and the tenure of the debt will be shorter.

•Start with the basic formula:

*   DSCR = CFADS/DS
*   DS = CFADS/DSCR
*   DS = Interest + Repayment

•In this case there are a couple things you can do.

*   You can set up a cash reserve account to cover the interest
*   You can use the cash reserve withdraws to cover the repayment
*   In this case there is higher repayment (non-negative) and the tenure of the debt declines
*   If the CFADS includes only the cash for repayment, the DSCR is below the target

•Solution

*   Amount withdrawn from the reserve account uses the formula
*   CFADS = EBITDA – Taxes + Amount Withdrawn
*   Target CFADS = Debt Service x DSCR
*   Debt Service = Interest Expense
*   **(EBITDA – Taxes + Amount Withdrawn)  = Interest Expense \* DSCR**

**Amount Withdrawn = Interest \* DSCR – EBITDA + Taxes**

You can then sum the amount withdrawn in each period to derive the amount of the reserve account (you could subtract the sum of interest income from this). As CFADS does or can drive the amount of debt and the amount of interest, there is circular reference related to this. The amount withdrawn can be thought of as a reserve account.

The blue button below is attached to the completed file that is referred to in the video at the end of this section. You can experiment with this file and see how the method produces the target DSCR as well as a debt size that results in a zero balance at the end of the debt tenure. You can also see problems with the iteration button with a large model — the goal seek does not work and the model can become very unstable. The video describes how to create a check box to turn the iteration button on and off.

.

 **[Excel File with Completed Equations for Case when Interest Expense is More than Debt Service (Negative Repayment)](https://edbodmer.com/wp-content/uploads/2025/09/Solution-for-Session-6-13.09.2025.xlsm)
**

.

If you want to see how I have done this and then try to do the exercise yourself with better methods you can work through the exercise file that has blanks that are in yellow. The video uses this file to illustrate how to create a debt structure that results in the target debt service coverage and also results in repayment of the debt consistent with the debt tenure. This involves computing debt service with CFADS that includes reserve withdrawls and CFADS without reserve withdrawls, computation of the reserve using interest expense \* DSCR – EBITDA and debt sizing using a goal seek with the final closing balance being zero.

.

**[Excel File with Exercises for Session Six for Computing Reserve Accounts for Sculpting when Interest > Debt Service](https://edbodmer.com/wp-content/uploads/2025/09/Exercise-for-Class-06.09.2025.xlsm)
**

.

In the video I use some clips from the course and I correct some of the mistakes I made in the course. Hopefully with this will allow you to work through the exerice and more fully understand the ideas of solving the problem (maybe you will find a more elegant way to do this).

.

.

.

Session 7 – Consolidating Projects to Model a Corporation
---------------------------------------------------------

.

The next session switches gears and moved to modelling of a consolidated portfolio of projects. To begin the discussion I note that any corporation is a portfolio of different investments. The investments could be factories, advertising, an internet website, investments in R&D, training of employees and many other things. The way I think about this portfolio of investments is a family tree where the family has a history and may last for many generations into the future. If we for some reason want to value the family we would need to not only value the current generation, but also future generations that will be there long after we are gone.

.

 **[Excel File with Exercises for Session Seven for Consolidation of Project Finance Files with Different Structures](https://edbodmer.com/wp-content/uploads/2025/09/Exercise-1-for-Session-7-Consolidation.xlsm)
**

.

 **[Excel File with Exercise for Session Seven for Consolidation of Project Finance with Completed Inputs for Combination](https://edbodmer.com/wp-content/uploads/2025/10/Session-7-Final-Version.xlsm)
**

.

In modelling the projects, there are a few key excel points.

*   Ultimately, when you consolidate you can use the SUM function which can sum the same range in cells between two sheets. This function has the form SUM(Start:End!F11) where Start and End are the name of sheets in excel and the F11 cell is summed between the sheets.
*   You can use the INDIRECT function to get cells from specific cells such as to get a list of returns from different projects.
*   You can use the INDEX function or the XLOOKUP function to make the transfer of variables from an INPUTC type sheet to a template model sheet. If you are transferring data from INPUTS, you need to use the INDIRECT function.
*   The power point slides that describe some of the finance theory and introduce the excel issues is part of the session.

.

 **[Power Point Slides with Theory Discussion and Introduction to Various Sessions for Weekend Course](https://edbodmer.com/wp-content/uploads/2025/09/Course-Outline.pptx)
**

.

The video for Session 7 is below.

.

Session 8 – Consolidation Part 2 – Corporate Finance and Debt Timing Complexities
---------------------------------------------------------------------------------

.

In this session we begin with review of the consolidation in the prior session. Then, we discuss the ROIC in the consolidated case. We demonstrate a few key points about the ROIC. First, we discuss the prinicple that value comes from earning a return on capital (ROIC) above the cost of capital combined with growth. Then we show that the ROIC is difficult to compute in project finance but that the weighted average return is the same as the ROIC. If economic depreciation is computed from the change in value and the initial value equals the balance of plant, then you can compute an alternative measure of depreciation which I call economic depreciation. With economic depreciation the ROIC is the same as the project IRR and you have a benchmark for evaluating performance and measuring value. The reconciliation is illustrated in the screenshot below.

.

![](https://edbodmer.com/wp-content/uploads/2025/10/image-1.png)

.

**[Excel File with Exercise for Session Eight for Consolidation of Project Finance with Initial Consolidation](https://edbodmer.com/wp-content/uploads/2025/10/Session-8-Exercise.xlsm)
**

.

The file works through valuation principles of a corporation using ROIC, Growth and Cost of Capital. After the corporate valuation exercise with finance equations and terminal value we work through some detailed issues in the consolidated model including converting monthly to semi-annual and circular references. The power point slides that describe some of the finance theory and introduce the excel issues is part of the session.

.

 **[Power Point Slides with Theory Discussion and Introduction to Various Sessions for Weekend Course](https://edbodmer.com/wp-content/uploads/2025/09/Course-Outline.pptx)
**

.

The video below works through issues for the session. You can use the file above for working along with the exercise.

.

.

.

Session 9 – Re-financing and Alternative Methods
------------------------------------------------

.

In this session we work through a model of re-financing. The re-financing mechanics involve first defining the timing of re-financing and other re-financing parameters in the InputC sheet. The modelling involves setting-up flags for the period of re-financing and a repayment flag for the re-financing. With the flags and the interest rate, you can define the debt size for the re-financing and then set-up a debt balance for the repayment period. Once the size and repayment of re-financing are derived, you can add the re-financing to a cash flow waterfall. Issues of the tax effect of re-financing and detailed timing issues are not addressed in this video.

The file that includes work in the session on re-financing is attached to the button below. It is part of the consolidation analysis.

.

**[Completed Excel File with Re-financing Analysis for Ninth Session (Included in Consolidation File)](https://edbodmer.com/wp-content/uploads/2025/11/Session-9-Re-finance-Completed.xlsm)
**

.

.

Session 10 – Three Methods for Resolving Circular References and Related Problems
---------------------------------------------------------------------------------

.

I have been a little reluctant to have a session on circular references with the UDF because it seems like a marketing pitch. But I did it anyway. In the video below you can first see how the UDF dramatically increases the speed of a large model. This is shown with a model that requires a copy and paste with a goal seek and then with the consolidation model that has become large and should have a circular resolution.

The session then turns to resolution of circular references with a simple and stylized example. In the discussion we cover making a check box to turn the iteration button on and off, making a goal seek along with a copy and paste macro and making a data table with a macro so that the copy and paste can be run with each sensitivity of a data table. The file for the analysis we completed in the session is attached to the button below.

.

**[Completed Excel File with Simple Analysis of Three Methods for Resolving Circular References for Tenth Session](https://edbodmer.com/wp-content/uploads/2025/11/Session-10-UDF-8-November-2025.xlsm)
**

.

.

Session 11 – Difficult Time Line Issues with Maintenance Reserve Accounts and Monthly to Semi-Annual Analysis
-------------------------------------------------------------------------------------------------------------

In this session we cover some time line issues that allow you to model things like re-surfacing of roads, major overhauls, augmentation of battery capacity and so forth. We create a flexible time line that can either be monthly, monthly/semi-annual, annual for all periods etc. The key to doing this is to have a variable that measures the number of periods of pre-cod periods. This variable is computed by the number of construciton months divided by the months in a period. For example, if the months in a period is one month per period for construction, and the construction months are 24 months, then there will be 24 months of construction. If there are 12 months in a period, then the number of construction periods is 2 which is 24 months divided by the 12 periods per year.

Construction Periods = Construction Months/Periods in Year During Construction

With the flexible construction and operating periods that are driven by this variable which is used to split up the model, the issue of maintenance reserve accounts are addressed. The amount of the inflated cost of the future maintenance is spread backwards over the time period used to put cash into the account. This is done through creating a counter and SUMIF rather than using OFFSET. When you create the counter you have to be careful with the period before the COD.

.

**[Session Eleven File with Timeline Analysis and Discussion for Maintenance Reserve Account using SUMIF](https://edbodmer.com/wp-content/uploads/2025/11/Session-11-MRA-15.10.2025_HK.xlsm)
**

.

**[Excel File with Completed Exercise Demonstrating How to Model Timing of Overhauls and Scheduled Outages](https://edbodmer.com/wp-content/uploads/2026/01/Overhaul-with-Variable-Timing-1.xlsm)
**

.

VIDEO WILL BE UPLOADED

.

Session 12 – Advanced Cash Sweeps – Using Cash Sweeps to Adjust the Debt Tail After COD Derived from Achieved Cash Flow
-----------------------------------------------------------------------------------------------------------------------

In this session we address a structuring potential for debt where the structuring begins with a downside case (in a tollway case, where the debt size is derived from a minimum traffic guarantee) and using a very short tail. For example, a case where the tail is only one year. This structuring can result in a high debt to capital ratio and result in a relatively low equity contribution. But the lender would like to adjust the tail so that there is ability to re-structure the debt in the long-run. Components of this section include:

*   Addressing an advanced and creative method to structure the debt repayment of projects where the projects have a minimum guarantee, but the sponsor expects traffic above the minimum level.
*   To analyse the issue of flexible structuring with a cash sweep, a model will be developed where the debt size is initially based on a short tail and the minimum traffic.
*   After project operation, if the traffic is established above the minimum level, a cash flow sweep is implemented where the cash sweep continues at 100% until a shorter tail is reached. If the traffic is higher, the cash sweep will be shorter and the investor IRR will increase.

In modelling this method, to allow the debt tail to be increased, a cash sweep of 100% is established which reduces the tail. This cash flow sweep continues at 100% until the tail reaches a target. When attempting to solve the problem of the length of the cash sweep necessary to reduce the tail, a goal seek formula does not work and there must be an adjustment to the final year of the sweep in order to develop an exact value. An illustration of how a cash sweep can be used is shown in the two screenshots below. The first screenshot shows a case with debt structuring and the second illustrates a case with higher traffic, a 100% cash sweep and a lengthened tail. After the screenshot a file that is used in the session is attached to the blue button.

.

![](https://edbodmer.com/wp-content/uploads/2025/12/image-1.png)

.

![](https://edbodmer.com/wp-content/uploads/2025/12/image-2.png)

.

**[Excel File with Completed File for Session 12 with Cash Sweep Used to Change the Debt Tail After Actual Cash Flow](https://edbodmer.com/wp-content/uploads/2025/12/Sweep-Analysis-Completed.xlsm)
**

.

.

Session 13: Measuring Costs and Benefits of Cash Sweep
------------------------------------------------------

.

In this session we evaluate risks analysis from different aspects of designing covenants and other aspects of debt agreements. The objective is to assess the risk and return aspects of a cash flow sweep. In paticular, how does a cash sweep lower the risk to lenders relative to debt agreements with no cash sweep. For a cash sweep to be effective, some dividends that would be paid are instead used to pay down debt earlier than the debt schedule. The repayment of debt lowers the amount of debt outstanding and protects the lenders in case of default.

A cash sweep lowers the equity IRR because of the delay in dividends. But it also protects lenders from out-year cash flows. The question is whether the cash sweep is effective for the lender and how much it can reduce the loss on debt. To measure the benefits, doing some kind of scenario analysis or break-even analysis is not effective because the value of the cash sweep depends on the postive cash flow used to repay debt early and then a later low cash flow with a default. The tool I use to do this is a monte carlo simulation where the loss on debt at the end of the project is assessed with different risk structures (volatility and mean reversion).

.

**[Financial Model with Exercise Evaluating Cash Flow Sweep to Demonstrate Cost and Benefits of Sweep](https://edbodmer.com/wp-content/uploads/2026/03/Sweep-Analysis-Exercise.xlsm)
**

.

.

Session 14: Measuring Risk and Return on Sub Debt and On Structured Equity
--------------------------------------------------------------------------

.

In this session, we address the fundamental risk and return issue associated with different tranches of debt and equity in a cash flow waterfall. The session includes assessing the risk and return characteristics of subordinated debt and different equity structures. There is a structuring section to the exercise where the subordinated debt is sized from the aggregate DSCR and the senior debt. The structuring portion of the exercise also demonstrates how to structure equity with different risk where more cash flow goes to the first equity tranche before a hurdle rate is met. To do this you can set up a tracking account that receives that dividends until a return is met.

In this case, the risk and return characteristics of the senior debt, subordinated debt and alternative equity tranches are evaluated through break-even analysis.

.

**[Excel File with Exercise for Session 14 with Subordinated Debt and Structured Equity Cash Flow](https://edbodmer.com/wp-content/uploads/2025/12/Sub-Debt-Analysis-Completed.xlsm)
**

.

The completed file is attached with equations for structuring the debt is attached to the blue button

.

 **[Excel File with Completed Analysis for Session 14 with Subordinated Debt and Structured Equity Cash Flow](https://edbodmer.com/wp-content/uploads/2025/12/Sub-Debt-Analysis-Completed.xlsm)
**

.

.

Session 15: Evaluation of Debt Structure with Multiple Debt Issues – Part 1
---------------------------------------------------------------------------

This session works through different ways to structure debt in the case where there are multiple debt issues with different interest rates and tenures. The session addresses how to use sculpting formulas and how to use the weighted average interest rate to determine the aggregated debt.

In discussing the aggregate debt I discuss a bisectional approach to computing the goal seek — thanks to Brian

.

**[Session 15 - Analysis of Sculpting Debt Issues Using Different Debt Structures with Alternative Methods](javascript:void(0);)
**

.

**[Excel File with Use of Bi-Sectional Method for Computing Goal Seek to Derive Debt Size and Sculpting](javascript:void(0);)
**

.

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=18621&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=10960&rand=0.8792002354284781)