# Circular Reference and the DSRA

**Source:** https://edbodmer.com/circular-reference-dsra

---

This page discusses various circular references that arise because of the DSRA and alternative methods for breaking the circular references.  The circular references arise because the level and changes in the DSRA are a function of debt service. The DSRA creates at least four different circular reference problems as follows:

The DSRA creates circular references related to funding when the debt is driven by the debt to capital ratio.  The DSRA changes the size of the debt which in turn changes the project cost, but the project cost changes the size of the debt.

The DSRA creates a circular reference related to interest income when sculpting is used because interest income is part of CFADS which is in turn drives the amount of the debt.

The DSRA creates a circular reference related to a cash sweep.  This should really not happen but it is a big pain to resolve.

The DSRA creates a circular reference that is almost impossible to elegantly resolve when the DSRA releases or contributions are considered part of the DSCR.

Circular references associated with the DSRA are one of the biggest problems that arise from circular references.  One problem is that the DSRA effects the pro-rata percent and the equity balance, but these things affect the debt.  A second problem arises from how changes in the DSRA should affect the DSCR and scuplting.  Nobody does this, but the DSRA is lie net debt in the context of corporate finance.  Taking this analogy further means that changes in the DSRA should be in the denominator of the DSCR calculation and not the numerator.

The DSRA programming is tricky in a UDF.  Here are a few key points about it:

1.  You should put it in a separate loop because you need to look forward and find the prospective debt service.
2.  The second loop should begin one period forward and go to the number of periods that you are using for the prospective DSRA.
3.  Allocate the DSRA funding and the change in the DSRA between pre-COD and post-COD as you would in the financial model.
4.  Make sure the total uses includes the DSRA

Here is some of the code for the DSRA with the second loop.  When you do this you can put the change in the DSRA as a part of CFADS.  This will automatically reduce the debt repayments in the final period (at least factored by the DSRA).

dsra\_requirement\_p(i) = 0

' it is important that this is a new loop

For i = start\_repayment - dsra\_periods To end\_repayment ' Start before repayment so that you can add up the DSRA requirement

' This is like the SUM(OFFSET) in excel

For k = i + 1 To i + 1 + dsra\_periods
 dsra\_requirement\_p(i) = dsra\_requirement\_p(i) + total\_senior\_debt\_service\_p(k)
 Next k

dsra\_pre\_cod\_p(i) = 0
 If i = start\_repayment Then
 dsra\_pre\_cod\_p(i) = dsra\_requirement\_p(i)
 End If

dsra\_change\_p(i) = 0
 If i > start\_repayment Then
 dsra\_change\_p(i) = dsra\_requirement\_p(i) - dsra\_requirement\_p(i - 1)
 End If

dsra\_balance\_p(i) = dsra\_balance\_p(i - 1) + dsra\_pre\_cod\_p(i) + dsra\_change\_p(i)

dsra\_funded\_p(i) = 0
 dsra\_lc\_balance\_p(i) = 0

If DSRA\_letter\_of\_credit = False Then
 dsra\_funded\_p(i) = dsra\_balance\_p(i)
 End If

If DSRA\_letter\_of\_credit = True Then
 dsra\_lc\_balance\_p(i) = dsra\_balance\_p(i)
 End If

interest\_income\_p(i) = interest\_income\_rate(i) \* dsra\_funded\_p(i - 1)

dsra\_lc\_fee\_p(i) = dsra\_lc\_balance\_p(i - 1) \* dsra\_lc\_fee\_percent(i)

Next i ' End of the DSRA loop

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1080&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=8880&rand=0.25918308472865714)