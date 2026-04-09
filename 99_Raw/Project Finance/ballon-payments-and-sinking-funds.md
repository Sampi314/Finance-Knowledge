# Ballon Payments and Sinking Funds

**Source:** https://edbodmer.com/ballon-payments-and-sinking-funds

---

Some project finance transactions include a balloon payment at the end of the debt tenure.  The balloon payment in project finance poses some tricky analysis issues — how much benefit does the balloon payment really have for equity investors.  It also introduces some difficult modelling issues as the size of a balloon payment expressed as a percent of the debt outstanding affects the amount of the sculpted debt which then turns back and affects the amount of the balloon payment.

In working through issues with balloon payments, a focused model that evaluates the effects of balloon payments with different cash flow patterns, tenures, interest rates, DSCR and debt to capital criteria is presented.  This model does not complicate things with either taxes or with a multiple construction period.  I hope I have stated this elsewhere, but studying some of the complex issues in project finance can be accomplished much better with a focused small model.

In looking at this page you may be thinking about what I find an incredibily irrating phrase named TLNR (too long not read).  The issues and the modelling below are both complex and nuanced.  In some cases the balloon payment may not make much of a difference.  In other cases the balloon option can be dramatic.  You cannot understand this with just a couple of sentences.

In working through issues with balloon payments in project finance, the analysis is discussed first with some examples from an exercise file that you can download below.  Next, I present technical issues with a few excerpts and a video explanation.

**[Excel File with Analysis of Balloon Payment in Project Finance and Sinking Fund (Without Taxes and Circular References)](https://edbodmer.com/wp-content/uploads/2018/04/Debt-Structuring-and-Balloon-Payments-1.xlsm)
**

Analysis of Ballon Payments
---------------------------

In analysing balloon payments using the model that you can download above, you could make a big sensitivity and scenario analysis or just look at the first page with the CFADS and debt service graph and then evaluate a few key ratios using some spinner boxes.  Spinner and dropdown boxes may violate some of the blah blah stuff about model structure, but the more I try to demonstrate stuff, the better tools they seem to be.

So lets start with a case where the DSCR is driving the debt size and then evalute how much a balloon structure can help.  In the diagram below you can see the debt repayment structure and the equity IRR.  Rule number one is that the project IRR must be higher than the interest rate (in this case with no tax it is completely obvious).  The case with no balloon payment is demonstrated below.  I would recommend that you open the file and try some of this.

![](https://edbodmer.com/wp-content/uploads/2018/04/Balloon-1.jpg)

If the same parameters for project IRR, debt tenure and debt cost are used together with a big balloon payment of 20%, the equity IRR increases from 8.9% to 12.33%. A big increase.  The balloon payment allows more debt to be issued with the DSCR constraint as shown at the bottom of the excerpt.  The debt to capital increases from 77.17% to 86.85% because the more debt can be fit underneath the cash flow line.

![](https://edbodmer.com/wp-content/uploads/2018/04/Balloon-2.jpg)

A ballon payment introduces re-financing risk.  To mitigate this risk a sinking fund can be introduced.  The sinking fund has a negative effect on IRR because dividends are delayed.  The sinking fund can be started a few years before the balloon payment is scheduled.  The effect of the sinking fund is illustrated below.  You can try different levels of sinking funds, different levels of balloon payments and different other parameters to evaluate what is happening.  A diagram and results of the case with a sinking fund is presented below. With the sinking fund, the IRR declines from 12.33% to 11.69%, but it is still far ahead of the starting level of 8.90%.  I hope when looking at these diagrams you are thinking about how can you make effective presentations to explain really what is going on with all of this stuff.

![](https://edbodmer.com/wp-content/uploads/2018/04/Balloon-3.jpg)

In a second case the Debt to Capital is the constraint rather than the DSCR.  In this case when the balloon payment occurs, the level of debt does not change.  To introduce the case, I have change the project IRR and some of the DSCR and debt to capital constraints (the DSCR is increased and the the debt to capital is reduced).  Without the balloon payment, these assumptions result in an equity IRR of 9.78% as shown below.  Note that the debt to capital is the target of 85%.

![](https://edbodmer.com/wp-content/uploads/2018/04/Balloon-4-1.jpg)

When the balloon is added in this case the debt level does not change but the IRR increases.  The equity IRR increases to 13.71% because the balloon payment allows dividends to be paid earlier. It DSCR also increases because the amount of repayment is reduced.

![](https://edbodmer.com/wp-content/uploads/2018/04/Balloon-5-1.jpg)

Mechanics of  Ballon Payments, Cash Sweeps and Sculpting
--------------------------------------------------------

To understand the balloon structure and implications I think it is helpful to work through the modelling mechanics.  Assumptions that are used in the example include the percent of debt that is paid with a ballon payment as wel as the tenure, the debt sizing parameters.

![](https://edbodmer.com/wp-content/uploads/2018/04/Balloon-6.jpg)

Once the assumptions are established, you should begin with the sources and uses of funds as ususal.  To model the balloon payment you can split the debt into the balloon portion and the non-balloon normal portion which is assumed to be sculpted.

![](https://edbodmer.com/wp-content/uploads/2018/04/Balloon-7.jpg)

Like with any debt in any model, begin with balances (in PF from sources and uses).  Make balloon a separate issue.

![](https://edbodmer.com/wp-content/uploads/2018/04/Balloon-8.jpg)

Then put the debt balance with opening and closing balance before the cash flow analysis.

![](https://edbodmer.com/wp-content/uploads/2018/04/Balloon-9.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/04/Balloon-10.jpg)

Videos on Balloon Payments
--------------------------

Mechanics of Circular Resolution for Balloon Payments
-----------------------------------------------------

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=2063&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9216&rand=0.94672717396242)