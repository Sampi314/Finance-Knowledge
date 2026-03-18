# Sculpted, Annuity and Equal Installment Economics

**Source:** https://edbodmer.com/cash-trap-covenants-with-prospective-dscr-llcr

---

Depending on whether the debt to capital or DSCR constraint is the determinant of debt size, sculpting can make a big difference to equity returns. In particular, if level repayments are causing the DSCR constraint to be operative, sculpting can move from the DSCR constraint back to the debt to capital constraint. This is illustrated in the two excerpts below that were presented in the prior page.  In the first cast with level payments, the DSCR is limiting the amount of the debt.  On the other hand, when sculpting is used for repayment, the debt to capital is the constraint.  The first excerpt shows the DSCR constraint with a 1.35 constraint and level repayment.  The second excerpt shows the amount of debt that can be raised with 80% debt to capital constraint.  In the hypothetical example, the IRR is a lot higher in the second case.

![](https://edbodmer.com/wp-content/uploads/2018/04/Repayment-1.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/04/Repayment-2.jpg)

In a second case the sculpting issue makes much less of a difference because of the shape of the cash flow (the cash flow growth).  Here the pattern of cash flow is similar to the pattern of debt service in the first place. In this case, the sculpting does not change the constraint on the debt from DSCR to debt to capital and it does not have as big effect on the equity IRR.  This is demonstrated in the case below where the growth rate is negative in cash flow.

![](https://edbodmer.com/wp-content/uploads/2018/04/Repayment-6.jpg)

![](https://edbodmer.com/wp-content/uploads/2018/04/Repayment-7.jpg)

File to Download with Exercises on Sculpting versus Equal Installment
---------------------------------------------------------------------

The file below includes the exercies illustrated with the excerpts above.

[Excel Exercise for Analysis of Sculpting Repayment versus Level Repayment to Illustrate IRR Effects](https://edbodmer.com/wp-content/uploads/2018/04/Sculpting-vs-Equal-Installments.xlsm)

The videos associated with debt repayment and debt tenure include instructions on how to create project finance models that measure the effects of sculpting, length of debt, mini-perm and re-financing as well as adjustment of cash flow to meet a target DSCR. In addition to the long videos that describe how to make the models, a set of shorter videos discuss the nuances of repayment along with when the repayment structure and the repayment tenure really matters and when it does not matter very much. The shorter videos also describe when re-financing dramatically changes the analysis. I am in the process of finishing the shorter videos.

The difference between level repayment and sculpting depends on the pattern of cash flows and what is driving the debt constaint (i.e. the debt to capital constraint or the DSCR constraint).  If the pattern of cash flow is declining over time in a similar manner to the way level debt repayments results in declining debt service, then sculpting does not help much.  Similarly, the effect of sculpting or equal installment payments will be less if the debt to capital constraint is in effect rather than the debt to capital constraint.  You should fully understand these two methods of debt sizing before working through the issues presented on this page.

Complexities in Computing Level Repayments Using Dynamic Goal Seek
------------------------------------------------------------------

When you would normally compute level payments. you may create a goal seek or even a goal seek with a macro.  When I first did this I was proud of myself.  But this method is not adequate for evaluating the issue where you want to change a whole bunch of different parameters like the debt to capital ratio, the pattern of cash flow, the interest rate and so forth.  Then you want to click a button to change between equal installment and sculpting.

A video that explains how to create a dynamic goal seek using a user defined function.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1907&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=0&rand=0.9169876091040476)