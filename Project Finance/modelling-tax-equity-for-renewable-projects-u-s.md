# Yield Based Flip and Partnership Allocation (Generally for Wind Projects)

**Source:** https://edbodmer.com/modelling-tax-equity-for-renewable-projects-u-s

---

This page describes how to model tax equity partnership structure that receives tax credits bases on the amount of production rather than the amount of investment — i.e., the production tax credit. As the tax credit is received over time and the production is not a certain amount like the investment tax credit, a yield based flip rather than a time based flip which often arises. On this page I show you how to set up a tracking account to automatically evaluate when the allocations of cash flow and income change for different investors. I think working through the yield based flip with a simple example is a good way to start the whole analysis of tax equity modelling. In this example I do not work through the capital accounts and some of the more painful details. The tax equity transactions with flips structures are used to achieve tax benefits from U.S. renewable energy investments. Many U.S. renewable projects have tax equity structures created to take advantage of tax incentives that cannot be fully used by investors under standard project finance structures.  These structures involve partnerships owned by a tax investor and the sponsor (sometimes called the developer). 

On this page I describe how to model flip structures, tax depreciation and distribution of partnership cash flow.  I start with a simple case where income and cash flow are both distributed in the same manner in the context of an annual model to explain the basics of computing cash flow flips. Next, I move to situations in which the operating cash flow of the partnership (not including depreciation effects) is distributed in a different manner than income (which allows the party to take advantage of accelerated tax depreciation) and where the analysis is developed on a periodic basis.  On the next webpage I move to various complex tax rules such as stop loss accounts, deficit restoration obligations (at liquidation), qualified income offsets, excess depreciation, outside capital accounts and other horrible stuff.  The principle question addressed on the next page is how do these things affect cash flow distributions to the partners.

Partnerships established for tax in the U.S. distribute cash flow in a different proportion than the proportion of income (income is just about always a big negative in early years). This is not all that different than when a corporation has different types of common stock with different characteristics — for example Class A stock and Class B stock. Because the tax depreciation deductions generally exceed the level of EBITDA at the parternership by a wide margin, the tax benefits could not be realised by a standalone SPV tax paying corporation (there is a big NOL). Instead, the tax benefits would result in a tax loss carry forward that dramatically reduces the value of the tax advantages to investors unless various strategies are implemented.

Various financial structures that have been developed to deal with the tax losses can involve a few issues from a modelling and/or finance theory perspective. The primary structure is to set up a partnership that does not pay taxes. This partnership is financed by two parties — a Developer/Sponsor Investor and a Tax Equity Investor. Each investor contributes to fund capital expenditures of the partnership. The partnership distributes cash (it does not pay tax). In addition, the partnership also distributes taxable income. Distribution of taxable income and cash are on a different basis to the two investors and the distributions vary over time. One structure uses a yield flip where the Tax Equity Investor partner that can use the tax benefits receives much of the negative taxable income. After a target yield is met, the allocation changes and cash flow accrues to the second developer/sponsor investor. The flip can be designed with a fixed time flip or an IRR target (known as a yield) flip. This yield based flip structure can be modelled using a little trick with MAX and MIN where you set-up the tax equity investment in two pieces. The first piece is represented a lot like subordinated debt that does not receive cash interest but instead receives a cash sweep. The diagram below is supposed to illustrate this structure.  The button below the diagram is associated with a power point file the explains some of my thoughts on the issue.

![](https://edbodmer.com/wp-content/uploads/2018/10/Partnership-Diagram.jpg)

.

[Power Point Slides that Work Through Modelling and Accounting Issues Associated with Tax Equity Financing](https://edbodmer.com/wp-content/uploads/2018/04/Tax-Equity.pptx)

.

Step by Step Time Based Flip
----------------------------

.

Step 1: Compute the Cash Flows to the Tax Equity on an After-tax Basis and Include the PTC. Note that it is better to have a time based calculation of the income

Step 2: Compute the total after-tax cash flow for the tax investor at the pre-flip cash flow percentage

Step 3: Set-up a tracking account for the pre-flip tax investor cash flow and use a subtotal account that will be used to test the distribution of cash during the

Simple Example with Yield Based Flip
------------------------------------

Note in this case the tax equity investment is more than 50%. The cash flow percent is very high before the flip.

.

![](https://edbodmer.com/wp-content/uploads/2020/11/image-4.png)

What is the purpose of a tax equity partnership flip financing structure?  
•Monetize the tax benefits available to renewable energy projects by raising third party equity from tax oriented investors  
•Tax equity investors typically include large financial institutions with significant recurring annual taxable income  
•Examples of investors include JP Morgan, GE, Bank of America, US Bank, Google, etc.

Goals of a partnership flip structure:  
•Maximize the allocation of available tax benefits to the tax equity investors  
•Tax benefits include accelerated MACRS depreciation and PTCs or ITC  
•Minimize the amount of cash that is allocated to the tax equity investor  
•How do we create a structure that achieves our goals?  
•Allocate a majority of income (and PTCs) to tax equity, typically for a period of 10 years  
•Minimize the amount of cash allocated to tax equity  
•After the flip date is achieved, minimize the amount of income and cash allocated to tax equity  
•Size the upfront tax equity investment by targeting a 10-year after tax IRR hurdle rate

.

The second example has a dramatically different distribution from the first example. Note on the bottom of the screenshot the tax equity receives 20% of the pre-tax cash. After the flip, the tax equity receives 5% of the cash flow.

In terms of income, the tax exuit begins with 99% and then ends with 5%.

.

![](https://edbodmer.com/wp-content/uploads/2019/07/Structure-Tax-Equity-Inputs.jpg)

.

Simple Flip Case with One Cash Flow Item (Not a Realistic Case)
---------------------------------------------------------------

To explain how the partnerships are structured I have created a few case exercises.  The initial set of exercises are quite simple and subsequent examples move to more complex issues. The first exercise demonstrates the basic idea of structuring a flip structure (a yield based flip rather than a time based flip) with a hurdle rate. Cash flow goes to the senior investor with a defined payout until a target yield is met. In this case, an unrealistic assumption is made that the distribution of EBITDA is the same as the distribution of income. The key is to create a tracking account (not a capital account) that accumulates the cost of capital (like capitalised interest) and use the MIN function.  Once you have the the tracking account for the tax investor before the flip, you can make a separation between four cash flows as follows:

*   Tax Investor Cash Flow before Flip — this is the cash flow that is used for assessing the flip rate
*   Sponsor Cash Flow before Flip — this is a tricky cash flow to compute in the final flip year
*   Tax Investor Cash Flow After Flip — this is easy to compute from the cash flow subtotal
*   Sponsor Cash Flow After Flip — this is easy to compute from the cash flow subtotal

The model that illustrates the simple case is available for download by clicking the button below.  This first file is used to demonstrate how to make a basic capital tracking account.  The second file includes construction funding and has similar methods for computing the distribution of cash flow with a cash flow flip.  The screenshot below the buttons shows the set-up of assumptions for the tax investor (partner 1) and the sponsor (partner 2)

**[Excel File with Fundamental Issue of Computing the Cash Flow to Two Investors with Senior Investor Tracking Account](https://edbodmer.com/wp-content/uploads/2019/02/Exercise-27-Cash-Flow-Flip-Exercise.xlsm)
**

**[Excel File with Fundamental Issues of Computing Flip Including Financing During Construction Period](https://edbodmer.com/wp-content/uploads/2019/02/Exercise-27-Cash-Flow-Flip-Exercise.xlsm)
**

.

![](https://edbodmer.com/wp-content/uploads/2019/02/Tax-Equity-Inputs.png)

The next screenshot below taken from the example files illustrates how to set up the tracking account to evaluate when the cash flow flip occurs. The key is to set-up a tracking account for the senior tax equity investor who will continue to receive cash flow until a target IRR is met.  This tracking account is something like a subordinated debt balance account where interest is capitalised instead of paid and a cash flow sweep is used to repay the debt.  Dividends received before the flip occurs are subtracted from the tracking account and accrued cost of capital at the flip rate increase the balance of the account.  The amount of capital invested is added to the account.

In the screenshot below, the tracking account is computed as a negative balance rather than a positive balance (I did this ages ago and I would strongly suggest you apply positive balances).  The only tricky item to compute in this simple example is cash flow received shown in line 38 below.  This can be modelled like a cash flow sweep where it is the minimum of the amount of cash from the partnership (including tax benefits) or the amount of the opening balance plus the accrued cost of money in the tracking account.  Note that it is the same as line 30 until column k.  In column k the opening balance of 105.6 plus the accrued cost of money at the hurdle rate of 10.56 that sums to 116.5 is less than the partnership cash flow of 170.  So in this period, the minimum is 116.5 rather than 170.  After column K, the opening balance is zero and the accrued cost of capital is also zero.  And zero is less than the partnership cash flow. This means the dividends are also zero.  This can be represented by the formula:

Distributions to Senior Tax Equity Before Flip =

MIN(Cash Flow to partnership, opening balance + accrued cost of capital)

.

![](https://edbodmer.com/wp-content/uploads/2019/02/Tax-Equity-Annual.png)

.

The screenshot below illustrates computation of the cash flow using the MIN function.  In line 41 the pre-flip senior cash flow is computed.  Note that the percent that the cash flow is of the pre-flip cash flow is shown below.  This is the pre-flip cash flow divided by the pre-flip percent.  In column K, you can see that the pre-flip cash flow is 60% of the total cash flow.  This means 40% of the cash flow is associated with the post-flip percentages.

.

![](https://edbodmer.com/wp-content/uploads/2019/02/Tax-Equity-Annual-2.png)

.

Tracking Accounts with Multiple Different Cash Flows
----------------------------------------------------

PTCs also transferred to sponsor in same ratio as the final income allocation

Set-up order

Second item — tax income — has the first adjusted

Need to include a minimum on the opening balance

Partnership Flip Rate and Term  
•Typically target a 10-year AT flip for tax equity ranging from 7.00% -8.00%  
•Cost of tax equity can fluctuate with market conditions (deal flow, interest rates, etc.) or project conditions (credit quality of off-taker, riskiness of offtake structure, etc.)  
•ITC Partnership flip would target IRR of ~7.25% in 7 years

More Complex Flip Case with Multiple Cash Flow Series
-----------------------------------------------------

In this exercise, there are two different distributions to partners and two different allocations.  The first allocation of income and therefore tax benefits is the standard 99%/1%.  The second allocation is for the cash flow produced by the partnership. This ratio is assumed to be 35% to the tax investor and 65% to the sponsor/developer.  This case is assumed to be a solar project with investment tax credit.  The first screenshot below demonstrates that the tax investor puts in 55% of the investment, but that 29.1% of the investment is ITC which comes straight back to the investor.

![](https://edbodmer.com/wp-content/uploads/2019/02/Tax-Equity-ITC-in-Sources.png)

The second screenshot demonstrates how you can structure a tracking account when there are two different distributions.  In this case, the MIN should be in a cash flow waterfall rather than in the tracking account as I showed above for the simpler cases.

![](https://edbodmer.com/wp-content/uploads/2019/02/Tax-Equity-Cash-Flow-Waterfall.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2019/02/Tax-Equity-Cash-Flow-Waterfall-2.png)

.

.

Periodic Cash Flows Rather than Annual Cash Flows
-------------------------------------------------

The first example uses annual cash flows and a one period construction period.  The second case example is a little more realistic with periodic cash flows. If a partnership is established, then taxes can be allocated in alternative ways to the partners where the amount of the income attributed to the partners must be tabulated along with the dividends that are not related to the tax benefits themselves.

![](https://edbodmer.com/wp-content/uploads/2019/02/Tax-Equity-Periodic-One.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2019/02/Tax-Equity-Periodic-Two.png)

.

.

Comprehensive Example with A-Z Structuring of a Model that Includes ITC, PTC, MACRS Depreciation, Bridge Loans and Bonus Depreciation
-------------------------------------------------------------------------------------------------------------------------------------

I have made an example that includes different types of technologies — solar, wind and battery along with the associated tax assumptions.  The central idea to create a model like this is to keep things structured and to maintain a transparent and flexible model.  Please note that this does not mean following some blah blah blah rules without solving circular references.

Start with pre-tax cash flows and project IRR.  You can find this file in the battery section and the discussion of cash flow.

.

![](https://edbodmer.com/wp-content/uploads/2019/03/Tax-Equity-Pre-tax-Cash-Flow.jpg)

Before working through allocations, work on the overall taxes.  The assumptions are shown below.

.

![](https://edbodmer.com/wp-content/uploads/2019/03/Tax-Equity-Tax-Assumptions.jpg)

.
-

.![](https://edbodmer.com/wp-content/uploads/2019/03/Tax-Equity-Financing-Assumptions.jpg)
------------------------------------------------------------------------------------------

![](https://edbodmer.com/wp-content/uploads/2019/03/Tax-Equity-Sources-and-Uses-Summary.jpg)

.

.

![](https://edbodmer.com/wp-content/uploads/2019/03/Tax-Equity-Cash-Flow-Allocation.jpg)

.

.

![](https://edbodmer.com/wp-content/uploads/2019/03/Tax-Equity-Tracking-Account.jpg)

.

Tax Equity Structures in the U.S. and the Amazing way that Incentives for Renewable Energy Accrue to Large and Rich Companies with a Big Tax Bill
-------------------------------------------------------------------------------------------------------------------------------------------------

The structure uses a flip structure where the Tax Equity Investor partner that can use the tax benefits receives much of the negative taxable income. After a target yield is met, the allocation changes and cash flow accrues to the second developer/sponsor investor. The flip can be designed with a fixed time flip or an IRR target (known as a yield) flip. This yield based flip structure can be modelled using a little trick with MAX and MIN where you set-up the tax equity investment in two pieces.

The first piece is represented a lot like subordinated debt that does not receive cash interest but instead receives a cash sweep. The second issues involves esoteric issues associated with the tax code. If a partnership is established, then taxes can be allocated in alternative ways to the partners where the amount of the income attributed to the partners must be tabulated along with the dividends that are not related to the tax benefits themselves.

If capital that is computed using the pre-tax income (less depreciation deductions) and the non-tax related dividends falls to zero, the tax equity partner may have some problems. It is not surprising that the partner that is exposed to limits on tax is the tax equity investor. To compute the potential exposure, two different capital accounts can be be set-up and something called deficit reduction obligations may be used.

The complex finance structures and complex tax rules mask what I think is the most important and third issue. The tax equity investment has two characteristics that are particularly favourable to the Tax Investor. First, the repayment structure is often like a cash flow sweep or a senior debt with very low risk. Second, as much of the cash flow to the tax equity investor is after-tax the required returns should be less than the pre-tax returns. These two points suggest the return to the tax investors should be very low. But the returns to the tax equity investors have been surprisingly high, suggesting that the whole idea of the tax benefits to renewable energy which was supposed to reduce costs for consumers in fact primarily benefits a small group of very rich large companies.

Analysis of Tax Equity Investments
----------------------------------

I have created a number of files that model tax equity transactions. The first file is associated with the videos and also has detailed capital accounts that evaluate constraints on the ability to use credits. Other files include sensitivity analysis without constraints and demonstrate the fundamental ideas.

Transaction with ITC instead of PTC  
• Tax equity funds 1.3x ITC amount  
• Tax Investor priority cash distributions based on % of investment – 2.0% pre-flip, 4.3% post-flip  
• Tax Investor common cash allocations – 0.0% pre-flip, 5.0% post-flip  
• Tax Investor taxable income allocations – 99% pre-flip, 5.0% post-flip

Files in Resource Library Not Yet Uploaded with Explanation
-----------------------------------------------------------

I am in the process of uploading a number of files with a little explanation of how they work.  This takes some time.  In the meantime you can get the files in the resource library under the advanced project finance issues folder.  If you send me an e-mail to edwardbodmer@gmail.com I will send you the files.

*   Tax Equity Model and Exercises.xlsm
*   Partnership Template Solar.xls
*   Yield Flip Scenarios.xlsm
*   IRR Flip with Mulitple Investors.xlsm
*   Yield and Time w Documenation.xlsm
*   Exercise 27 – Cash Flow Flip Exercise.xlsm

The basic point is that capital for the Tax Equity goes to zero using the first capital calculation (not the outside capital calculation)

Capital is computed with 50% of ITC

Capital is computed with only dividends from operations (it does not include tax distributions)  
Net Income for capital computation is allocated using tax allocation factors  
Compute a subtotal so you can see how much DRO is needed  
DRO is capped at the level of dividends and does not help that much  
Compute another sub-total after interim calculation  
Stop loss is computed after DRO and constrains the use of tax benefits for tax equity partner  
Final closing balance is after the stop loss and should be zero

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=268&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=12200&rand=0.4703972933988816)