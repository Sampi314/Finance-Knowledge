# UDF Circular Reference in Corporate Model

**Source:** https://edbodmer.com/udf-circular-reference-in-corporate-model

---

This page demonstrates how to make a User Defined Function (UDF) that solves the primary circular reference problem in a corporate model, where the interest expense is driven by cash flow but cash flow is driven by interest.  Here are some points about circular references in a corporate model:

1.  Iteration Button or Copy and Paste Macros Destroy a Model
2.  Making a UDF that solves all of this is easy, but you do need to make a few lines of VBA
3.  Start with a simple corporate model.  Use lines for EBIT, Net Debt, Interest, Net Cash Flow.
4.  Interest is from Average Debt, or interest = (opening debt – cash flow/2) \* interest rate

The higher the cash flow, the less the debt and the interest, but the interest affects the debt, causing the circular reference.  One of the things that is really messed up if you use the iteration button is the goal seek.  When you create the iteration button the goal seek works fine. There are many other problems with the iteration button that cause your model to be unstable.  For example, if you delete some lines and get the #VALUE, then you cannot use the undo key.  With the UDF key these issues are not a problem.

**First Video and Exercise**

In this short video, you make a UDF that starts with interest expense and moves back to cash flow.  The idea of the VBA code is to start at the back. You need inputs for the interest rate and the cash flow amount and the opening debt balance. 

The video and the associated files are below.

[Download File Associated with Video](https://edbodmer.com/wp-content/uploads/2018/03/Corporate-Modelling-Exercise-Not-Complete.xlsm)

[Go Website that Lists Course Offering](http://financeenergyinstitute.com/index.html)

**VBA Code for Simple Case**

1.  Function interest(int\_rate, opening, ebit)
2.  For i = 1 To 10
3.      cash = ebit – interest
4.      average\_bal = opening + cash / 2
5.      interest = average\_bal \* int\_rate
6.  Next i
7.  End Function

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=697&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9712&rand=0.7690063221043211)