# Sculpting Basics – Non-Constant Interest Rates

**Source:** https://edbodmer.com/sculpting-fundamentals-and-non-constant-interest-rates

---

This page introduces debt sculpting in project finance where the DSCR and future cash flow drives the size of the debt in project finance. The sculpting models and videos on basic sculpting demonstrate that efficiently evaluating project finance debt structuring can be done with a couple of equations. The NPV of debt service and the Debt Service = CFADS/DSCR can resolve issues like sculpting with a changing interest rates, changing DSCR and can be modified for other evaluating other issued. This page introduces structuring and sculpting through addressing fundamentals of sculpting in the case where the DSCR drives debt and there are no taxes (taxes cause a circular reference).

There are a couple of key files where I put the financial formulas, modelling examples and the VBA code for cases where you run into circular references.  You can file these file on the google drive in the Project Finance Section under exercises and then Section D for the Sculpting course.  The files are available for download by pressing the button below.  The second file includes a function for determining the pattern of DSCR’s that achieve a target average loan life if the debt to capital constraint drives the size of the debt (sorry that this sounds like a foreign language).

**[Excel File with Focused Separate Sculpting Exercises and Analysis from Basic Debt Sizing to Advanced with VBA](https://edbodmer.com/wp-content/uploads/2018/04/Sculpting-Course-Final.xlsm)
**

Fundamental Case with No Taxes, No DSRA, No LC Fees, No Debt to Capital Constraint, a Single Debt Issue and Constant Interest Rates
-----------------------------------------------------------------------------------------------------------------------------------

Some put sculpting in your models with forced sculpting with some kind of solver equation or goal seek equation. I used to do this, where the repayment of debt can be derived to assure that the target DSCR equals the computed DSCR.  Instead, I strongly believe you should get used to implementing the two basic equations below.  In subsequent pages I demonstrate that variants of these two equations can be used to evaluate issues like on-going fees, witholding taxes, cases where the debt size is not driven by the DSCR, implementation of changes in the DSRA in the DSCR and other issues:

**Target debt service as : DS = CFADS/DSCR**

**Debt = NPV of the target debt service with the interest rate as the discount rate.**

If the interest rate is changing, you can change the way the NPV is computed.  You cannot use a manual equation where the discount factor is 1/(1+r)^t.  Instead you can compute the NPV by working in two steps.  The first step is to compute the compound interest factor where changes in previous discount rates affect the discount factor (unlike the equation 1/(1+r)^t).  To do this, create an index where you begin with 1.0 and then add the interest rate to this factor — 1.0 x (1+interest rate).  Further, when you compute the interest rate factor, begin the compounding at the commercial operation date and adjust the formula above — prior factor x (1+interest rate x operating flag).  When applying the interest rate factor, this could be with periodic rather than annual interest rates.

**Interest Factor(t) = Interest Factor(t) x (1+Current Interest Rate)**

Once you have computed the interest factor, you can compute the NPV of debt service using the SUMPRODUCT as follows — NPV = SUMPRODUCT(Debt Service/Compound Factor).  Note that you can use the divide sign in the SUMPRODUCT function (but you cannot click on the entire row or column when you do this).

The screenshot below demonstrates how you can work through the sculpting and structuring issues.  In this case you should create a debt switch (if you want to be fancy and call it a mask, you can but I have no idea why you call the true and false switch a mask).  With the flag established, the debt service is the CFADS divided by the DSCR multiplied by the switch.  The first period closing balance (i.e. the closing balance before the loan begins to be repaid) in the loan schedule is the present value of the debt service and the repayment is the target debt service minus the interest expense.

The video below walks through the fundamental sculpting equations. The video is designed so that you can fill in the blanks in yellow by yourself as discussed above.  This is the easiest case and it is the base for much more complicated situations that deal with debt to capital constraints, DSRA movements, L/C fees etc.

Sculpting Exercise 2: Non-Constant Interest Rates
-------------------------------------------------

Some term sheets include step-up credit spreads. Others allow a portion of the interest rate to be un-hedged.  In these cases, the first thing I hope you think about and understand is why structures such as a step-up structure occur.  What is generally happening is a strong incentive to re-finance. It is probably absurd for you to leave the step-up credit spread in the base case scenario.

In cases when the interest rate changes, a simple present value formula cannot be used. Instead, an interest rate index can be created that accounts for prior interest rate changes as follows:

Interest Rate Indext = Interest Rate Indext-1 x (1+Interest Ratet)

Debt Amount at COD = ∑ CFADSt/Interest Rate Indext

The video below walks through how to create an interest rate index and then use the SUMPRODUCT function to multiply the index by the target debt service.  You can use the SUMPRODUCT with a divide sign which is very helpful — SUMPRODUCT(Debt Service/Compound Factor). Note that you cannot use a discounting factor that separately values the debt service.  In general when discounting cash flows with different rates you should compute some kind of compounding factor.  To see this think about inflation Zimbabue.  You cannot discount a future cash flow without considering what happened to the currency in the past.

Further Information and Learning: Request Resource Library (Free), Find Details About In-Person Courses, Make Suggestions on Course Subjects and Locations
----------------------------------------------------------------------------------------------------------------------------------------------------------

The reason I have worked on this website is so that you consider an in-person class which is by far the best way you can become a top project finance analyst.  If you click on the button below, you will be forwarded to a website that describes some of unique courses.

[Click on this Button and See How to Create A Project Finance Model and Debt Structuring Analysis in A Couple of Days by Attending an Intensive, Hands-on In-Person Class](http://financeenergyinstitute.com/finance-theory.html)
   If you click on the right button you can quickly send an e-mail to edwardbodmer@gmail.com and request the resource library (no charge).  The google drives include more case studies, financial models, risk analysis files and other materials than are included on the website. I promise not to pester you if you do send me an e-mail.

I would really like to know what courses may be most interesting to you and where you would like the courses to be held. If you click on the left button below, I have a form that I will use to try and put together a class with a few people.

If you are a student, I would be honoured to come to your university or your business club and give you a hands-on guest lecture. If you click on the button on the left below, you can do me a big favor by giving me some information about your institution.

  
[Click on this Button to Send Me and E-mail and Request Resource Library that Contains Google Drives and Zipped Files (No Charge for this)](https://edbodmer.com/send-me-an-e-mail-and-i-will-send-you-resources/)
 [Click on this Button and Do Me a Favour by Suggesting Your Preferred Course Locations, Subjects and Possibilities of Guest Lectures and Your University](https://edbodmer.com/send-me-an-e-mail-and-i-will-send-you-resources/)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=3292&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=8576&rand=0.46583406279789186)