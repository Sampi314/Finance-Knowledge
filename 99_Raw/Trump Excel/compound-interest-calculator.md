# How to Calculate Compound Interest in Excel + FREE Calculator

**Source:** https://trumpexcel.com/compound-interest-calculator

---

[Skip to content](https://trumpexcel.com/compound-interest-calculator/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/compound-interest-calculator/#below-title)

_“Compound interest is the eighth wonder of the world. He who understands_ _it, earns it … he who doesn’t … pays it”. – **Albert Einstein**_

This Tutorial Covers:

[Toggle](https://trumpexcel.com/compound-interest-calculator/#)

What is Compound Interest?
--------------------------

Let me take a simple example to explain it.

Suppose you invest USD 1000 in a bank account that promises to give you 10% return at the end of the year.

So at the end of year 1, you get USD 1100 (1000+100).

Now since you didn’t have any immediate use of the money, you let it stay in the account. And the bank did its part and added 10% at the end of the year.

Since now you had USD 1100 in the account, the bank pays you 10% interest on 1100 (which includes the USD 1000 you invested at the beginning and the USD 100 interest you earned at the end of the first year). So you end up with USD 1210.

The benefit of compounding is that even your interest would earn interest.

![Calculating Compound Interest in Excel Calculator](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202000%201333'%3E%3C/svg%3E)

What is the difference between Simple Interest and Compound Interest?
---------------------------------------------------------------------

**Simple Interest** simply calculates the interest amount based on the initial investment, total number of years, and the rate of interest, For example, if you invest USD 1000 for 20 years at 10% rate, you will get USD 3000 a the end of 20 years (that is USD 100o of your initial investment and 2000 of the simple interest).

**Compound Interest**, on the other hand, calculates interest on the interest amount as well. So if you invest USD 1000 for 20 years at 10% rate, the first year your investment grows to USD 1100. In the second year, your investment grows to USD 1210 (this happens as in the second year, you earn interest on 1100 and not 1000). At the end of 20 years, compound interest will make your investment grow to USD 6727.5.

As you can note, the investment with compound interest grew twice as compared with the one with simple interest.

_‘Simple interest is calculated on the principal, or original, amount of a loan. Compound interest is calculated on the principal amount and also on the accumulated interest of previous periods, and can thus be regarded as “interest on interest.’ (**Source**: [Investopedia](http://www.investopedia.com/articles/investing/020614/learn-simple-and-compound-interest.asp)
)._

Calculating Compound Interest in Excel
--------------------------------------

Let’s see how investment grows year-on-year when calculating compound interest is Excel.

Suppose you invest USD 1000 at a 10% interest rate.

By the end of Year 1, your investment grows to USD 1100.

![Compound Interest at the end of Year 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20320%20159'%3E%3C/svg%3E)

Now in the second year, the interest is paid on USD 1100. So the investment grows to 1210.

![Compound Interest at the end of Year 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20320%20159'%3E%3C/svg%3E)

At the end of five years, the investment grows to 1610.51.

![Compound Interest at the end of Year 5](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20316%20232'%3E%3C/svg%3E)

The formula for compound interest at the end of five years is: =B1 \* 1.1 \* 1.1 \* 1.1 \* 1.1 \* 1.1

Or **\=B1\*(1.1)^5**

So here is the formula for calculating the value of your investment when compound interest in used:

**Future Value of Investment = P\*(1+ R/N)^(T\*N)**

*   P – This is the principal amount or the initial investment.
*   R – the annual interest rate. Note that the rate needs to be in [percentage in Excel](https://trumpexcel.com/calculate-percentages-excel/)
    . For example, when the compound interest is 10%, use 10% or .1, or 10/100 as R.
*   T – the number of years.
*   N – Number of time interest is compounded in a year. In the case where the interest is compounded annually, N is taken as 1. In the case of quarterly compounding, N is 4. In the case of monthly compounding, N is 12.

Now let’s have a look at different examples of calculating compound interest in Excel.

### Yearly Compounding

In the case of yearly compounding, compound interest can be calculated using the below formula:

**Compound Interest = P \*R^T**

The future value of the investment can be calculated using the following formula:

**Future Value of Investment = P\*(1+R)^T**

![Calculating Compound Interest in Excel when interest compounded yearly](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20367%20214'%3E%3C/svg%3E)

Note that you need to specify the rate as 10% or 0.1.

### Quarterly Compounding

In the case of quarterly compounding, compound interest can be calculated using the below formula:

**Compound Interest = P \*(R/4)^(T\*4)**

The future value of the investment can be calculated using the following formula:

**Future Value of Investment = P\*(1+R/4)^(T\*4)**

![Calculating Compound Interest in Excel when interest compounded quarterly](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20402%20216'%3E%3C/svg%3E)

### Monthly Compounding

In the case of quarterly compounding, compound interest can be calculated using the below formula:

**Compound Interest = P \*(R/12)^(T\*12)**

The future value of the investment can be calculated using the following formula:

**Future Value of Investment = P\*(1+R/12)^(T\*12)**

![Calculating Compound Interest in Excel when interest compounded monthly](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20409%20211'%3E%3C/svg%3E)

Note that the as the number of period increase, the value of your future investment grows. In the examples shown above, the value in monthly compounding is highest.

Similarly, you can calculate the investment value with weekly compounding (use Ns 52) or daily compounding (use N as 365).

Using Excel FV Function to Calculate Compound Interest
------------------------------------------------------

Apart from the formulas shown above, you can also use the FV function to calculate compound interest in Excel.

FV is a financial [function in Excel](https://trumpexcel.com/excel-functions/)
 that is used to calculate the future values of the investments.

Here is the formula that will give you the future value of the investments:

**\=FV(R/N,R\*N,,-P)**

*   R – the annual rate of interest.
*   N – Number of time interest is compounded in a year. In the case where the interest is compounded annually, N is taken as 1. In the case of quarterly compounding, N is 4. In the case of monthly compounding, N is 12.
*   P – the initial investment. Note that this is used with a negative sign as this is an outflow.

![using FV function to calculate compound interest in Excel2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20404%20215'%3E%3C/svg%3E)

Compound Interest Calculator Template
-------------------------------------

Here is a simple compound interest calculator template you can use to calculate the value of investments.

![Compounded Interest Calculator Template in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20676%20256'%3E%3C/svg%3E)

From the [drop-down](https://trumpexcel.com/excel-drop-down-list/)
, select the number of times the interest is to be compounded. The result will automatically update in cell E2.

**[Click here](https://trumpexcel.com/wp-content/uploads/2017/06/Compound-Interest-Calculator-in-Excel.xlsx)
** to download the compound interest calculator template.

**You May Also Find the Following Excel Tutorials Useful:**

*   [Calculating Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)
    .
*   [Age Calculation Template](https://trumpexcel.com/calculate-age-in-excel/)
    .
*   [Calculating Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    .
*   [Calculating CAGR in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    .
*   [Using PMT Function in Excel](https://trumpexcel.com/pmt-function/)
    .
*   [Calculating Moving Average in Excel](https://trumpexcel.com/moving-average-excel/)
    
*   [How to Calculate IRR in Excel](https://trumpexcel.com/calculate-irr-excel/)
    
*   [Calculating NPV in Excel](https://trumpexcel.com/npv-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “How to Calculate Compound Interest in Excel + FREE Calculator”
-----------------------------------------------------------------------------

1.  good lea  
    sons just found the page and it excite me alot
    
    [Reply](https://trumpexcel.com/compound-interest-calculator/#comment-12760)
    
2.  All these formula give a result after a period of years. How do I calculate by a period of days; e.g. February = 28 days; March = 31 days, etc?
    
    [Reply](https://trumpexcel.com/compound-interest-calculator/#comment-12752)
    
3.  Thank you very much for your effort..god bless you
    
    [Reply](https://trumpexcel.com/compound-interest-calculator/#comment-12742)
    
4.  It would be great to see an article on this topic in reverse, as an educational tool for borrowers. So many people with credit issues are forced or lured into compound interest contracts that seem simple, and are sold as “monthly payments” but are devastating in the long run, as the interest compounds on the interest… to be PAID by the consumer, while giant companies “EARN” (USURY) the ludicrous interest amounts… making the rich richer and the poor poorer. The financial giants in this country are out of control.
    
    [Reply](https://trumpexcel.com/compound-interest-calculator/#comment-12171)
    
5.  Nice article. What if you are calculating the interest for a series of equal deposits each month but the the compounding is daily? How do you use the PV formula and let it know you are making deposits each month but compounding is each day?
    
    [Reply](https://trumpexcel.com/compound-interest-calculator/#comment-11408)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/compound-interest-calculator/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK