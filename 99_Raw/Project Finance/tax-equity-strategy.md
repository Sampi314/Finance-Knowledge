# Tax Equity Overview and Strategy

**Source:** https://edbodmer.com/tax-equity-strategy

---

On this page I try to provide a general overview of tax equity modelling. I hope I have come at this from a little different perspective than you may have if you are working for a big company or a big accountig firm with all of their rules.

There are different ways to finance a project with tax equity. Strategies can include a tax partnership, a sale leaseback, direct transfer of ITC, and an inverted or sandwich lease. In addition, there are different ways to add debt leverage to a project including back leverage, debt at the project level and including debt in a project that is financed with an inverted lease or a project that includes a direct sale of the ITC. Added strategies can consider the level of the fair marked value write-up and what happens when the tax investor exits the project. Strategies can also include evaluating different tax equity structures with different income and cash flow allocations as well as PAYGO and considering a yield base flip rather than a time based flip. On this webpage I make some suggestions as to how you can evaluate different strategies with a financial model. But when you model the different strategies, you should understand the point that modelling tax equity is just incorporating a bunch of rules. More interesting questions about how you should assess risks to different investors; how you should value a project; what are equitable returns to tax equity investors are should be addressed.

In thinking about issues associated with tax equity and modelling tax equity, I divide the issues into three categories with different importance:

*   Least Important: Modelling the tax rules – this is mechanical and accounting
*   More Important: Understanding why the tax rules exist – this allows you to put some context on modelling the rules
*   Even more Important: Modelling and understanding different strategies such as partnership structures (distribution of cash flow and income); negotiation of pre-tax and after-tax yields to partners; different financing strategies (back leverage or project debt); different corporate structures (partnership; sandwitch lease; direct transfer of ITC); tax options (ITC, PTC, 45Q); risk transfer options with yield or time based flips and PAYGO.
*   Very Important: Structure and present results of model so you clearly see how the taxes work; so you can see the drivers of the IRR and value to each partner; so you can quickly see the effects of different strategy on after-tax IRR for tax equity; so you can clearly see the effects of different financing strategy; you can understand the risks to different investors and financiers; you can see risks and returns with different strategies ….

General Issues in Tax Equity Modelling and Analysis

1.  Understand key tax rules like 50% basis, ITC and PTC
2.  Understand how to model balance sheet of partnership (without ITC)
3.  Understand modeling and implication of inside basis and outside basis
4.  Understand the computation of IRR to partners to assess the distributions of cash flow and income
5.  Understand the general idea of back leverage
6.  Understand the difference between ITC and PTC
7.  Understand why yield based flips are used in PTC and not with ITC
8.  Understand Tax Equity Bridge Loan and Financing Issues with Partnerships
9.  Understand Alternatives to Tax Equity Partnerships like Sandwich Leases and Sale Leasebacks and Direct ITC transfer
10.  Understand the Effects of front Leverage Relative to Back Leverage and how the minimum gain comes into play when project debt is used rather than back leverage.

.

Perspective of Tax Authority
----------------------------

.

#### Two Considerations for the Tax Authority

Pretend you are working for the tax authority (the IRS). You are faced with the following two constrants.

1.  You cannot allow taxpayers with high taxable income and tax rates to use deductions of taxpayers. If you did, everybody with a high tax bracket could use deductions from a low tax bracket and the government would lose a whole lot of money. I illustrate this by considering the tax deduction for your teenager in the picture below.
2.  As the tax authority, you cannot prevent companies from establishing partnerships or using two classes of shares with different dividend structures. For example you could not say that one partner must pay the same proportion of income as another partner.

![](https://edbodmer.com/wp-content/uploads/2023/09/image-5.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2023/11/image-10.png)

.

#### Resolution of Not Allowing a Bare Transfer of Tax Benefits without Taking Project Risk

In my silly example above, you as the tax authority would not allow the transfer of the deduction for the teenager without the tax payer taking the risk of dealing with problems of the teenager. But how could you do this with the limited information you have.

You do have some financial data on how much income is produced by the asset and how much depreciation deduction there is. So you can make the taxpayers compute some financial statments. If the equity balance for one tax payer is negative, you may surmise that this tax payer has not taken risk in the project. This is a very crude solution but it is about all you can do.

.

Point Number 1: Start with Pre-Tax Pre-Leverage Cash Flows and Evaluate the Pre-tax IRR
---------------------------------------------------------------------------------------

The first step in evaluating the project you can compute the cash flow from things like solar production, PPA rates and degradation etc. There are some general benchmarks that you can use for the project IRR. If project IRR is below zero or around 1% to 2%, then it will probably be difficult to make the project work. If the project IRR is already around 18%, then the project is so profibable that you will not to need to take advantage of tax incentives make it work (you should ask why other people cannot do the same thing and why the IRR is so high). If the project IRR without tax and without leverage is somewhere around 4%, then you can probably get it to work with equity returns for both the tax investor and the sponsor/developer. Note that in the discussion below I use these terms.

.

#### Mechanics of Computing Project IRR and Timing Issues in Tax Equity Models

When you work through the project finance model for a renewable project seasonality can be an issue. This means that there it can be a good idea to construct a monthly model. When you construct a monthly model, you can then consolidate the time line and use the SUMIF function so that you can convert the model into periods that are quarterly for taxes.

I have included a comprehensive model with monthly cash flows and a monthly pre-tax IRR as well as a simple case that starts with one period (year) of construction and a very simple flat EBITDA without any detail. These two models are illustrated below and attached to the two buttons. The first screenshot is for the very simple model. While this model is simple, most of the tax equity equity issues can be demonstrated with a really simple model that generates a pre-tax IRR of around 4%. The trick is to evaluate whether you can make a project with this kind of return work for investors and be financable. This sheet is named simple ITC model in the workbook below.

.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-7-2048x416.png)

.

**[Excel File with a Lot of Relatively Simple Examples with Work Through Many Issues with Issues for Tax Equity](https://edbodmer.com/wp-content/uploads/2023/08/Tax-Equity-Cases-1.xlsm)
**

.

#### Setting up Inputs and Pre-tax Cash Flow in a Simple Model

The next screenshot illustrates the more comprehensive model. This model is structured like other big models with InputC and InputS and it has monthly analysis with a lot of details. You can compute a pre-tax IRR as you should in any model and the operation part of the model can be the same as other models. Please when you compute the debt sizing from something like P90, do not mess up your model by putting both the P50 and the P90 in the project IRR section. You can address the debt sizing separately in the back leverage or project leverage separately.

The first screenshot below illustrates the set-up of the InputC page and the second screenshot illustrates the pre-tax project IRR page. As an aside, I think you should not keep to bureaucratic rules with respect to what is in the InputC and InputS. For example, I suggest it is good to have separate input sheets for the tax rules, for the tax partnership allocation and for the financing part of the analysis. It will be essential to keep the input sheets and the calculation sheets carefully structured. The more detailed model is attached to the model below.

.

**[Excel File with Comprehensive Solar and Battery Model that Includes Tax Equity Issues and Timing](https://edbodmer.com/wp-content/uploads/2023/08/Solar-Model-with-Tax-Equity-and-Financing-27-07-2023-Filled.xlsm)
**

.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-8-2048x892.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-9-2048x911.png)

.

The button below is attached to the detailed model. In the remaining analysis I will go through both the simple cases and the more complex cases.

.

**[Excel File with Comprehensive Solar and Battery Model that Includes Tax Equity Issues and Timing](https://edbodmer.com/wp-content/uploads/2023/08/Solar-Model-with-Tax-Equity-and-Financing-27-07-2023-Filled.xlsm)
**

.

.

Point Number 2: Don’t Be Impressed with People who Recite Tax Code Regulations
------------------------------------------------------------------------------

.

A lot of the modelling is simply about tax rules. These rules can be painful, but they are just rules and should be staightforward to establish in a model. The strategic options such as partnership allocations, financing at the project or back leverage, use of different strctures sandwich leases are more interesting and should be modeled with flexible scenarios.

There are tax rules include details associated with how the timing of ITC works; how depreciation is adjusted for ITC; how inside and outside captial are computed, how the PTC works. To repeat, these are all just rules. As a modeller you need to know these rules and unfortunately some of them like the minimum gain calculation can be confusing. But if you know the rule you can make the model. For this, one of my suggestions is to get ahold of some actual models (send me an email at edwardbodmer@gmail.com) to look through them.

I add here that you should not be impressed with people who can recite portions of the tax code such as 734b. It is so much more important to evaluate what to do in the context of the rules. Here are some of examples of rules that you will come up against in modelling:

*   Rules for Computing Fair Market Value
*   Computing ITC on Fair Market Value
*   Rules for PTC on Production and Inflation Adjustments in the PTC
*   Tax Basis Differential for Computing Depreciation when you take ITC
*   Rules for the way the IRS Computes the Balance Sheet with ITC
*   Rules for Computing Partner Capital — the Inside Basis and Outside Basis
*   Rules for ITC Transfer Option in the IRA
*   Rules for Computing Re-allocation of Income to Partners from Negative Capital
*   Rules for Allowing Allocation of Capital
*   Rules for Computing Suspended Loss and Later Allowance
*   Rules for Computing Excess Dividends

In addition to computing the numbers it is good to think about why some of the rules exist. Examples include:

*   Fundamental Idea of Negative Capital as Evidence of At-Risk
*   Why is inside and outside capital computed
*   Is the DRO cash or non-cash
*   What does suspended loss mean
*   What does the re-allocation of income mean
*   What does surplus dividends mean in the outside capital account
*   What does the minimum gain mean and how is it computed
*   Rules for Partner At Risk (IRR) and what is Bare Transfer of Tax Benefits

I think you have to have a minimum understanding of these rules. One way to try to understand the rules is to read some artilces. These are in Chapter 8 of the library. Otherwise you can look at examples of actual models. When you look at actual models, please understand the difference between cases with ITC and with PTC. Send me an email at edwardbodmer@gmail.com to get the example models and the articles.

In the the sheet attached to the model below, I have some exercises where you can work through the basic issues with computing taxes and with struturing a balance sheet. The screenshot below illustrates the computation of taxes and the computation of a balance sheet perscribed by the IRS without ITC and finally a balance sheet for the outside with sub-totals. For purposes of this section, I have used a simple model to illustrate how things work. You can see a carefully structured financial model later.

The screenshot below reviews the calculation of fundamental tax questions in the ITC case in the simple case. Note how the ITC is computed from the fair market value of the asset; how the basis difference is computed; how the gain on the sale from the FMV is computed. Note also there is negative income from the accelerated depreciation in the first years. People seem to use the 5-year tax depreciation with a 1/2 year convention whereas in the old days you had an option. The MACRS (modified accelerated recovery system) rates are often directly input.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-4-2048x975.png)

.

An illustration of including the inputs for tax rules is illustrate in the screenshot below. You can include other assumptions for the net operating loss and the tax position of the tax equity that is discussed in other sections below.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-10-2048x895.png)

.

The ITC and the PTC parameters are summarized in a table that is inlcuded in both the detailed and the simple file. The three screenshots illustrate the different inputs that you can use in your models. The tax depreciation and the PTC and the ITC depend on many factors and change accross years.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-12-2048x1111.png)

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-13-2048x1040.png)

.

.

Point Number 4: Compute a Simple Three Statement Model as the Basis for Equity Capital that is Allocated to the Partners
------------------------------------------------------------------------------------------------------------------------

.

Once you have the tax parameters defined — tax depreciation, ITC and PTC — you can compute financial statements for the partnership. I become very irritated when people talk about three statement financial models as this is a big deal. There is very little to computing the income statement, balance sheet and the cash flow for partnership project. In the case of a project with no debt and no working capital (you could add working capital), the Capital Expenditure are the equity financing, the EBITDA is the dividends and the income is computed using tax depreciation. There are couple of tricky issues with adjusting for the tax basis adjustment for ITC and also for working through the gain on sale to establish the fair market value.

The screenshot below illustrates what you are doing. You are making a model of the yellow partnership company. This company does not pay taxes but you can compute a hypothetical IRR assuming that the company does realize the tax benefits. The screenshot is meant to illustrate what we are doing. You do not have to make this in excel although you can.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-31.png)

.

The screenshot below shows some basic rules for computing the balance sheet and a three statement financial model. The first balance sheet is computed for the partnership if a partnership is used. Note there is no tax depreciation, note the gain on the sale that should go eventually to one of the partners. Finally, note the way that the basis differential is handled and that the FMV is the put on the asset side of the balance sheet.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-5-2048x811.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-11-2048x554.png)

.

The ITC and PTC for hydrogen projects is shown below. In the case of Hydrogen the situation is more complex because of the 45Q incentive and the steps in the PTC and ITC incentives.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-14-1024x522.png)

.

.

Point Number 5: Understand PTC and ITC by Making Comparison of Different Projects
---------------------------------------------------------------------------------

#### .

When thinking about tax equity issues, it is good to understand the difference between the ITC and the PTC. Some differences include:

*   ITC is based on plant cost without uncertainty why PTC is based on production which is uncertain
*   PTC includes inflation adjustments and uncertainty with respect to the future inflation while ITC is set in advance
*   ITC involves a basis adjustment that goes to the balance sheet while PTC does not have an adjustment
*   Realizing tax depreciation benefits is difficult for ITC because of capital constraints while this issue is not important for the PTC.

.

The file with the simple exercises includes analysis of the economics of the PTC and the ITC for different projects. The analysis depends on the amount of the up-front cost relative to the production. It the up-front cost is high and the production is low, then the ITC is more advantageous. If the production is high and the cost is relatively low like wind and hydrogen then the PTC is better. The comparison is illustrated in the graphs below and an example of how the analysis is made.

.

The first screenshot illustrates a portion of the analysis for solar where the ITC is computed with the basis differential and assumptions for the cost of solar and the yield for solar.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-15-1024x421.png)

.

The screenshot below illustrates the relative difference between the present value of the ITC and the PTC for different yields and costs. Note that in the case of solar, the ITC is generally advantageous relative to the PTC.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-16-600x430.png)

.

In the case of wind, I have modelled different capacity factors and costs. For the case of Wind, I show the computation of the PTC. The PTC has a term of 10 years and includes inflation. The present value of the PTC depends on the discount rate.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-18-2048x851.png)

.

The comparison is made by making a VBA macro instead of a data table. For the case of Wind, this is shown below and is in the file. You can find instructions on how to make the graph and the data table in the data table section of this website. The graph for the wind case is illuatrated on the graph below.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-19.png)

.

.

Point Number 6: Establish Allocations (again don’t focus on particular rules) and then Compute Initial IRRs for Negotiation
---------------------------------------------------------------------------------------------------------------------------

#### .

When working through the issues for the partnership I name the developer or the sponsor of the project (i.e. the non-tax investor) as the developer/sponsor. Now we move to negotiation between the tax equity investor and the sponsor. As with any negotiation you should see both sides so you can come up with fair equity contributions, distributions and income allocations. When thinking about allocations, think about two classes of common shares or preferred stock. It is always possible to have one share of general ownership of a corporation like minority interest and another share of the dividends that can have a simple or a complex structure. For example, maybe the corporation is owned by two partners who each own 50% of the company. It is not the case that you necessarily pay out 50% of the cash flow to each partner. In a similar way, you can allocate income on one basis and cash flow or dividends on another basis.

Please do not be impressed by people who recite the typical allocation percentages and structures. You can find some typical rules and model these, but the important thing is to here is not one answer like computing pre-tax IRR for the sponsor. Again, do not become tied to rules that do not matter.

To evaluate the structure of the partnership you can compute IRR’s. The IRR for the tax investor should always be after tax and include effects of the inside basis and the outside basis limits on deductiblity explained below.

The develoer IRR can be trickier. The developer IRR is often computed on a pre-tax basis but please do not believe silly rules. The pre-tax IRR implicitly assumes that the developer has a big net operationg loss from other activities. If the developer pays taxes then the answer is very different and the strategy should be different.

In the case of a solar project a time based flip makes more sense while in the case of PTC, a yield based flip makes more sense.

Some of the items I try to addressed below in computing these returns include:

*   The importance of the tax position of the sponsor/developer
*   Don’t simply follow rules and say that the developer should always be measured at a pre-tax rate
*   In a partnership for a solar model it will be very difficult to realise the full benefits of the tax depreciation
*   Depending on the tax position of the developer/sponsor, different allocations may be beneficial in a tax partnership.
*   The timing of the flip can be longer so that the tax equity partner will be able to use the suspended losses.

We are now focusing on the green ovals in the diagram. You can see that the IRR’s are computed and put into the green boxes. So the next step is how do we compute these IRR’s in the green boxes.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-32.png)

.

At this point you can compute the pre-tax IRR to the developer and the after-tax IRR to the tax investor as shown in the screenshot below. The tax investor gets the benefit of the tax losses and the developer IRR is computed with no taxes. Both IRR’s are wrong because the tax investor hits negative income and has absorption problems and the sponsor/developer may not be in a postion of having a really big net operating loss. But it is still a good starting point. In this case both the IRR of the tax investor and the developer are higher than the hypothetical IRR. It sounds too good to be true because you would think that the returns should be some kind of weighted average of the hypothetcal IRR. And it is too good to be true.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-30.png)

.

.

Point Number 7: Inside Basis and Re-Allocation of Income to Tax Equity when Capital is Negative with Absorption Problems
------------------------------------------------------------------------------------------------------------------------

#### .

Imagine you are working for the tax autority and you want to come up with something that can assure that a bare transfer of tax benefits is not occuring. You could try to compe up with some kind of IRR rule, but that would ultimately be subjective. About the only thing you could really do is use the financial statements. When using the financial statements you could make the conculusion that if the equity balance is negative, that means you have taken more out of the company than you put into the company. The amount you take out depens on negative income and dividends. So that is what happens. I am not sure about the logic but it is a rule.

When the IRS does this, they make you compute two balance sheets. The first balance sheet called the inside basis or the inside capital or some tax number that I don’t care about. For the inside basis, you can mess around with and you can transfer amounts (please not cash) to from one partner to another. The big transfer is from the sponsor to the tax invetor. This can be in the form of a Deficit Reduction Obligation DRO although I am reluctant to call it that. There are some issues with the DRO because if the project goes bankrupt, then the tax inestor can be liable to pay taxes on the transfer. But this allows you to get around the problem of negative capital.

Now when you compute the equity capital, you can use the same rules as the balance sheet for the overall partnership. But at the end you can make a sub-total and allow for the re-allocation of amounts (again not real money) from one partner to another. You can see the sub-total in the screenshot below. Again, do not be afraid of putting a sub-total in a balance sheet. The opening balanc should be tha number at the end. If you do not make a reallocation, then the IRR on the tax equity partner goes down dramatically. The screenshot below illustrates this accounting which seems painful at first but is really not that bad. Please please the formulas do not have to be complicated and please keep the inside equity balance on a differnt page.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-33.png)

.

The next screenshot shows the inside capital account for the sponsor/developer. In this case the capital balance is positive because the large negative income is not taken away and the basis adjustment is much smaller. In actual models there can be a capital gain and depreciation on the capital gain. You can see this in the more detailed analysis. So if somebody is shouting, I do know what is going on. Also I realize that the balance sheets only kick in on an annual basis.

Finally, at the bottom of the balance sheet for the developer, note that the equity balance of the sum of the partnerships is equal to the balance sheets of both investors.

.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-34.png)

.

.

Point Number 8: Outside Basis where the real action is and Suspended Loss and Excess Dividends
----------------------------------------------------------------------------------------------

#### .

The IRS makes you compute another balance sheet where you cannot play with the allocations that go from one partner to another. In this case, the IRS makes two tests that are arguably a bit arbitrary. The first test for some reason distinguishes between positiive and negative income on the top (see the video) and then makes a test of the amount of divideds paid versus the equity balance. If you have paid more dividends than the equity balance, these excess dividends are not added back to taxable income and labled a taxable gain. Again, this is just a rule.

Then, after the dividend test is made, a second test is made for a negative balance of capital. But this time, if there is a negative balance, it works like an NOL account that is carried forward. The problem is that if the balance is carried forward, you must have taxable income in the future to use the carryforward.

To model these things you can look at my other page, but the key is to use sub-totals and the MIN and MAX functions. An illustration of the outside basis is shown on the screenshot below.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-35.png)

.

Note in the above screenshot that the amount of the excess dividend called the imputed capital gain is much less than the amunt of the suspended loss that kicks in in the second period. The suspended loss balance is shown below the equity capital account and uses a MAX and MIN function. Finally, the IRR with the outside basis is shown below. Note that there is certainly an IRR penalty but it is not as bad as without the recovery of the suspended loss. I encourage you now to look through real models that I have put in my library. Send me an email to get the library at edwardbodmer@gmail.com.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-36-1040x583.png)

.

.

Point Number 10: Play with Contribution, Income and Cash Distributions to Negotiate Allocations
-----------------------------------------------------------------------------------------------

#### .

For the ITC case we are now finished except for the financing which is covered later. Not we can play with the parameters. I have put in spinners that some spreadsheet burecuratic technicians may object to. But screw them. You can see that because of the suspended loss it may be better to have a longer time based flip You can see that because of the problem in year 2 you may want to change the income allocation that is not usable anyway. You can adjust the contribution and the preferred yield to come up with a fair allocation.

The spreadsheet technocrats may say that you cannot make such a presentation and you only can compute the developer IRR on a pre-tax basis. How idiotic. Note finally, that you do not need to confuse things with financing yet.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-37.png)

.

I encourage you to go to the simple model and play with the parameters and focus on different IRR’s to the developer.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-6-2048x936.png)

.

In the above case, the hypothetical IRR after tax with ITC is 7%. But without tax constraints, the tax equity IRR and the sponsor IRR are each higher than this return. This is a trick because the developer IRR is pre-tax and the tax equity IRR is after tax.

I suggest that you should compute a whole lot of IRR’s and you can present the results something like this. These include pre-tax IRR’s and post-tax IRR’s to the developer and the sponsor. You can also compute other metrics like the NPV or my idea of computing the earned risk premium.

.

.

Point Number 11: Yield Based Flips for PTC and Production Risk
--------------------------------------------------------------

#### .

With the PTC, the tax investor’s cash flow depends on the amount of production. Unlike the case of the ITC, this means the tax investors cash flow is less certain. The tax investor may need more time to recover the cash if the capacity factor is lower. To do this you can use a yield based flip or alternatively you can also use a PAYGO structure which is like an earn out in an M&A transactions.

The yiled based flip structure means that when the tax investor receives a relatively more cash flow before a given level of IRR is reached. On the other hand the developer takes more risk because he gets less cash flow if the production is lower. As discussed below, this is aggrivated for back leverage to the lender.

To consider a yield based flip you can start with a very simple example. in the example below one investor gets all of the cash flow until a 7% return is received. After that, the second investor receives all of the cash flow. In this simple example there are no taxes. The senior investor puts 20% into the project and then gets 30% until a 7% target IRR is reached. Note that in this example the overall IRR is 10.96%.

The key to modelling this is to set up a tracking account which is like a senior debt facility with a 100% cash swee and capitalization of interest. As with the cash sweep facility that accrues interest, the tracking account continues until the facility is repaid with interest. This can be done through setting up an account and keeping track of the target IRR instead of the interest rate as shown below.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-20.png)

.

.

A second case includes taxes with different allocations of tax (income) and cash flow. The tax equity partner wants to receive the after tax cash flow so you must make some adjustments. But the example is essentially the same.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-21.png)

.

.

Point Number 12: Back Leverage and Yield Based Flips
----------------------------------------------------

#### .

As stated above, back leverage is financed by the cash flow that goes to the developer and not to the tax equity provider. In the extreme you could pretend that all of the operating cash flow goes to the developer and all of the tax related cash flow goes to the tax equity investor. If this would happen, you would have a very simple loan with pre-tax cash flows. But if some of the cash flow goes to tax equity as must happen, then the yield based flip can cause some credit issues.

The issue with yield based flips is that the developer cash flow can change if the yield based flip changes. With lower production, not only is the cash flow lower to everybody, but with a yield based flip, the cash flow share to the developer is delayed. The file with the simple example illustrates this case with different capacity factors. To illustrate the case, in the first case debt is assumed to be sized with a P50 case and with a DSCR of 1.35.

To illustrate how the yield based flip works, start with a case where the there is no tax equity and consider a simple debt sizing. In the example, I set the debt size and fix the debt size. Then with the fixed debt, I test the DSCR, LLCR and PLCR with alternative scenarios. With no tax equity financing, the debt service and the cash flow are illustrated below.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-22-1024x396.png)

.

After establishing the debt size from the P50 and 1.35 case, in the next case we assume that the debt is still sized with the P50 case and the 1.35, but the actual case turns out to be P90. In this case, the project just makes in because the PLCR is above 1.0 (the LLCR is a little below 1 implying a bit of restructuring.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-23-2048x887.png)

.

.

Now we can include tax equity with a yield based flip. You can switch the case to the P50 and include tax equity. Now the cash flow to the tax equity is structured differently with a decline after the flip. The debt is sculpted based on the cash flow to the developer. This also causes the debt size to be lower as expected from the NPV of the cash flow.

.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-25-1040x412.png)

Because of the flip structure, when the case is changed to the P90 case, the flip occurs later ant the LLCR and PLCR now are not sufficient to repay the debt. Notice that this time the PLCR and the LLCR are below 1.0.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-27-2048x812.png)

.

.

Point Number 13: Financing Solar Project with ITC and Tax Equity Bridge Loan
----------------------------------------------------------------------------

#### .

The financing of tax equity projects with ITC can have a tax equity bridge loan and back leverage and even equity bridge loans. This may seem complex but please to not worry. Understand that during the construciton period there is generally no tax equity investment. So a tax equity bridge loan just allows the developer who is funding the entire project to fund the project with money that will come from a tax equity bridge loan. The loan is not paid off by the tax equity but by the project that repays the loan.

As with any financing there is a funding order. In other projects the funding can be pro-rata or it can be computed using a cascade. In the example below, the cascade begins with the tax equity funding that funds the first funding needs (that include interest during construction and fees). As this loan is directly computed from the tax equity, there is no circular reference unless the fees and IDC are used in computing the ITC (which they can).

The rest of the financing can be structured with a cascade. In the screenshot below, I assume that equity is funded before the tax leverage. When sizing the debt you can use standard debt sizing. As the debt is typically repaid on a pre-tax basis, computing the size of the debt with the NPV of debt service at the interest rate is pretty simple and there are no circular references for taxes as is typical in other transcations. The only circular references come from the potential to cap the debt to capital, fees on a letter of credit, and IDC and fees in the computation of the FMV for the ITC. Otherwise the debt is fixed from future cash flow and the circular references are not a big issue.

The financing equations are illustrated in the screenshots below. The first screenshot illustrates the simple assumptions for the tax equity bridge loand and the back leverage.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-38.png)

.

.

The next screenshot illustrates the debt sizing for the tax equity bridge loan (in this case simply the size of the tax equity financing) and the back leverage loan that is computed from the net present value of the debt service to the developer. Note how the preferred yield and the cash to the tax investor are subtracted from the project cash flow. You can see more complexities in sculpting in different parts of this website.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-39-2048x912.png)

.

Once you size the debt, you can struture the financing of the project during construction. I suggest not worrying about the equity split and concentrate on how the project is financed. The financing comes from the The way you can structure the financing is illustrated in the screenshot below. The issue with yield based flips is that the developer cash flow can change if the yield based flip changes. With lower production, not only is the cash flow lower to everybody, but with a yield based flip, the cash flow share to the developer is delayed. The file with the simple example illustrates this case with different capacity factors. To illustrate the case, in the first case debt is assumed to be sized with a P50 case and with a DSCR of 1.35.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-40-2048x923.png)

.

.

The cash flow cascade equations and the equity cash flow to the developer are shown below. It is all not too complicated and it is really silly to make something that is simple into something complicated by the excel technocrats.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-41-2048x911.png)

.

.

![](https://edbodmer.com/wp-content/uploads/2023/08/image-42-2048x900.png)

.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=16586&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9588&rand=0.7674115278376522)