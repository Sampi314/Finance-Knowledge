# Parallel Model Case Examples

**Source:** https://edbodmer.com/circular-reference-on-line-course

---

The parallel concept works by adding a page to your model and then copying a template spreadsheet as well as the UDF code. With the new page, you connect a few input variables like EBITDA, depreciation, interest rates and DSRA inputs as well as the model timeline. I want to show you that it is not very difficult to implement the model.  I also want to show you that the parallel model can handle the vast majority of issues that you may deal with in your model. With the parallel model you can do all sorts of things you cannot do with other methods of solving circular model problems.  But that is not all. You can also verify your model.  There is still more. You can add features that you may not have imagined in your model. The really amazing thing to an old man like me is that you put a whole big template project finance model into a UDF and have this big model run in fractions of a second.

In the subsequent pages attached to this page, I illustrate how the model works using separate cases that demonstrate one project issue at a time.  I use three base models.  One model is pretty simple with annual flows and without balloon structures, alternative DSRA options, multiple debt issues or equity bridge loans.  With this example I demonstrate how the parallel model works and you can include different debt sizing options, debt repayment options, mezzanine debt, re-financing and changing interest rates.

Notes on the Parallel Model

1\. There is a video for each case which describes the issue and explains the concept with an excel file.  The excel file without the parallel model is provided on the website. Even if you do not use the parallel model, the exercise may be useful in explaining the project finance concept such as how to model DSRA changes as part of CFADS when sculpting debt.

2\. The one requirement from your model is that you establish a consistent time line that covers the construction period and the operation period.

Theory and Structuring of Project Finance Issues with Simple Model and One Debt Facility
----------------------------------------------------------------------------------------

I have made separate videos and case examples with model design and structure for the issues listed below using a simple annual model and the parallel model technique.  Even if you are not interested in the parallel model technique that resolves circular references, verifies your model and allows you to quickly evaluate advanced issues, the analysis can assist you in understanding the theory and the practical applications of a comprehensive set of project finance issues.  Using the simple model, these issues include:

1.  Evaluating sculpting, DSRA and alternative debt funding.  This first case works through resolving circular references for IDC, DSRA and taxes with sculpting. Methods of verifying the model are introduced.
2.  Demonstrating how to structure alternative debt sizing (fixed amount debt, debt to capital, sculpting and optimisation of methods) and funding methods (pro-rata and up-front equity) along with commitment fee and up-front fees.
3.  Creating a model with changing DSCR target levels over the tenure of the debt along with alternative debt sizing methods.
4.  Deriving the sculpted debt repayments when debt to capital ratio is used and where interpolation is made on DSCR for sculpting is used to derive minimum DSCR and average debt life constraint.
5.  Analysis of senior debt funding together with mezzanine debt with sculpting for both senior debt and mezzanine debt.
6.  Computing senior and mezzanine debt size, debt service and repayments using alternative debt size and debt repayment techniques for both senior and mezzanine debt.
7.  Evaluating how to structure and modelling debt re-financing including the effect of taxes and sculpting on the size of re-financing assumptions.
8.  Evaluating the issue of P90 for possible debt sizing and P50 for setting the tariff with the simple model and alternative debt structures.

I have tried to provide as many examples as possible of how the UDF works with different project finance issues.  Of course I may not cover anything, but these examples should illustrate that just about any issue can be covered using the method. Note that I have not posted my final version of the parallel model on the website that should be easily applied to your models.  If you want this model, you need to sign up for one of the advanced project finance structuring courses where I will show you how to modify the parallel model and apply the parallel concept to the models that you build.

Theory and Structuring of Project Finance Issues in Context of Periodic Model and Multiple Debt Facilities
----------------------------------------------------------------------------------------------------------

I have made a second set of videos and illustrative model design  for project finance issues using a morel complex model with monthly construction and multiple debt facilities applying the parallel model technique.  Again, even if you are not interested in the parallel model technique that resolves circular references, verifies your model and allows you to quickly evaluate advanced issues, the analysis can assist you in understanding the theory and the practical applications of a comprehensive set of project finance issues.  Using the periodic model with multiple debt facilities, these issues I work through include:

1.  Computing sculpted repayments on multiple debt issues where the debt IRR and the captured and non-captured debt service is used.
2.  Calculating sculpted repayments where some of the facilities have fixed repayments and other facilities are sculpted.
3.  Evaluating the effects of multiple mezzanine debt and multiple senior debt facilities with alternative sizing techniques.
4.  Verifying alternative pro-rata and equity up-front funding techniques in the context of multiple debt issues.

Theory and Structuring of More Advanced Project Finance Issues Using Detailed Model with Alternative DSRA Assumptions, Balloon Payments, Equity Bridge Loans and Grace Periods
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

I have made a third set of videos and illustrative model design  for project finance issues using a morel complex model with monthly construction and multiple debt facilities applying the parallel model technique.  Again, even if you are not interested in the parallel model technique that resolves circular references, verifies your model and allows you to quickly evaluate advanced issues, the analysis can assist you in understanding the theory and the practical applications of a comprehensive set of project finance issues.  Using the periodic model with multiple debt facilities, these issues I work through include:

1.  Equity bridge loans during the construction period
2.  Alternative development fee assumptions
3.  DSRA with alternative assumptions in the context of the DSCR.
4.  Balloon and re-financing assumptions.
5.  Evaluating the effects of multiple mezzanine debt and multiple senior debt facilities.

The cold hard fact is that excel is not a very good tool for project finance modelling.  This is because of natural circular references that occur in project finance structuring.  For example, Interest During Construction (IDC) depends on debt which can depend on project cost.  But IDC is a component of project cost.  This is a classic circular reference.

The copy and paste and the iteration button fail miserably in solving circular references.  Excel loses its ability to perform sensitivity analysis, target contract bids, and quickly demonstrate the effects of alternative structuring parameters.

The good news is that you can fix the circular reference with a user defined function (UDF).

The better news is the UDF can be used as a sophisticated method to audit many of the equations in your model.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=1070&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=9924&rand=0.8065872072194739)