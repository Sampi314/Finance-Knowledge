# Calculating NPV (Net Present Value) in Excel (Easy Formulas)

**Source:** https://trumpexcel.com/npv-excel

---

[Skip to content](https://trumpexcel.com/npv-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/npv-excel/#below-title)

Net Present Value (NPV) is a method to analyze projects and investments and find out whether these would be profitable or not.

It’s widely used in the financial world and is considered a robust way to make accurate investment decisions.

To give you an example, if you’re considering an investment plan, where you invest $100 every month for the next 10 years and get $20,000 at the end of 10 years, you can use the NPV method to find out whether this is a profitable investment decision or not.

Don’t worry, things will get a lot clearer as I cover some examples later in the tutorial.

In this tutorial, I will show you different examples of calculating NPV in Excel. I’ll also cover two formulas to calculate NPV in excel – **NPV** and **XNPV function**.

So let’s get started!

What is NPV – An Easy Explaination
----------------------------------

Before I get into calculating the NPV value next cell, let me quickly explain what it really means.

NPV (short for Net Present Value), as the name suggests is the net value of all your future cashflows (which could be positive or negative)

For example, suppose there’s an investment opportunity where you need to pay $10,000 now, and you will be paid $1000 per year for the next 20 years.

If you know what is the current discount rate (also called the cost of capital or the interest rate), you can use that in the NPV formula in Excel to calculate the net present value of all the future inflows that you will have in the next 20 years with this investment.

If that value is more than $10,000, then this is a profitable investment and you should go ahead and do it. And in case it is less than 10,000, then you end up with a loss and you shouldn’t do this investment (and instead invest the money at the current discount rate in government bonds or index funds).

NPV value is also used when comparing different projects or investment opportunities.

If you have 3 different projects with expected outflow and inflow values, you can use the net present values of all these to see which project has the best profitability.

Now that you have a decent understanding of what NPV is, let’s see a couple of examples on how to calculate in Excel.

Excel NPV Function
------------------

Excel has an in-built NPV function with the following syntax:

\=NPV(rate, value1, \[value2\],...)

The above formula takes the following arguments:

*   **rate** – this is the discount rate for one time period. For example, if your cashflows are happening every year, this would be the annual discount rate. If these are quarterly, this would be quarterly discount rate
*   **value1, value2…** – these are the cashflow values and could be positive (inflow/income) or negative (outflow/payment). You can have a maximum of 254 values

Some important things to know when using the NPV function in Excel:

*   The NPV function considers all the these values are evenly spaced out (i.e., have the same time interval between each value).
*   The order of the values matter, so if you change the order and keep the same values, the final result would be different
*   The formula considers that the inflow/outflow takes place at the end of the period
*   It only considers the numeric values, and if there are blanks or text values, these would be ignored

The most important thing to keep in mind is that you can only use this formula when your regular flow of inflows and outflows. For example, if the inflow/outflow happens at the end of the year, it should be the same for all the values.

In case you have a dataset where the inflow/outflow happens on specific dates (and is not evenly spaced), you can not use the NPV formula. In that case, you need to use the XNPV formula.

Now that we know about the syntax of the NPV function, let’s have a look at some practical examples.

Also read: [Excel Weighted Average Formula](https://trumpexcel.com/weighted-average-in-excel/)

Calculating Net Present Value (NPV) in Excel
--------------------------------------------

When working with the NPV formula in Excel, there could be two scenarios:

*   The first outflow/inflow happens at the end of the first period
*   The first outflow/inflow happens at the beginning of the first period

For example, if I am evaluating a project which would need an initial outlay of $100,000 and then yearly returns, the two scenarios would be:

1.  Outflow of $100,000 at the end of Year 1, and then inflows from end of Year 2 onwards
2.  Outflow of $100,000 at the beginning of Year 1, and then inflows from end of Year 1 onwards

You can use the NPV function in both scenarios with a minor adjustment.

Let’s have a look at each example!

### First Outflow/Inflow Happens at the End of the First Period

Suppose I need to evaluate a project where the cash flows are as follows and the discount rate is 5%:

![Dataset for calculating NPV](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20665%20306'%3E%3C/svg%3E)

In this example, the first outflow of $100,000 happens at the end of year 1.

You can use the below formula to calculate the NPV value for this data:

\=NPV(D2,B2:B7)

![Formula to calculate NPV](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20666%20430'%3E%3C/svg%3E)

The above formula gives the NPV value of $15,017, which means that based on these cash flows and the given discount rate (also called the cost of capital), the project will be profitable and generate profit worth $15,017.

This is the straightforward use of the NPV function, but in most cases, you will be dealing with cases where the inflow happens in the beginning.

So let’s see an example of that.

### First Outflow/Inflow Happens at the Beginning of the First Period

Below I have the data to evaluate a project where the cash flows are as follows and the discount rate is 5%:

![Dataset when cashflow is at the beginning](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20633%20309'%3E%3C/svg%3E)

You can use the below formula to calculate the NPV value for this data:

\=B2+NPV(D2,B3:B7)

![Formula to calculate NPV when cashflow at beginning](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20633%20432'%3E%3C/svg%3E)

In the above formula, I have excluded the initial outflow, as it happens at the beginning of the first year.

Since the NPV function is programmed in such as way that it considers each value as an inflow/outflow at the end of each period, I excluded the initial outflow and calculated the NPV for all the other future cash flows.

And then the result of the NPV function is then added back to the initial outflow.

This gives us a value of $15,768, which is the profit we will make by investing in this project.

So in case you need to evaluate projects/investments where the first cash flow happens at the beginning of the first period, exclude it from the formula and add it back to the result.

Comparing Projects Using NPV to Find the Best One
-------------------------------------------------

In real life, it often happens that you need to analyze multiple projects/investment opportunities and see which ones are the best for you or your company.

NPV is often the best and most accepted way to compare different projects where you can the cashflows.

Suppose you have the dataset as shown below and you want to find out which project(s) are worth investing in.

![Data to compare projects using NPV](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20737%20301'%3E%3C/svg%3E)

For the purpose of this example:

*   I am considering that the first cashflow happens at the end of first year
*   The initial outflow for each project is $100,000
*   The discount rate for evaluating all the projects is 5%

Below are the formulas that will give me the NPV value for each project.

**Project 1:**

\=NPV(5%,B2:B7)

**Project 2:**

\=NPV(5%,C2:C7)

**Project 3:**

\=NPV(5%,D2:D7)

![NPV values for three different projects](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20740%20391'%3E%3C/svg%3E)

Based on the results, we can see that the return on Project 3 is the highest, and if you have to choose between one of these, you should choose Project 3.

Similarly, if you need to choose any two, you should choose Project 3 and 1, as these have a higher NPV.

When evaluating projects using the NPV method is that it works on projected future cash flows. With projections, there is always a risk that it may not turn out as we expected (could be higher or lower). Also, the risk of error in forecasting increases as the duration increases. We can forecast income in the next two years with far more accuracy than that of the income in the year 19 and 20.

Calculating NPV for Irregular Interval – Using XNPV Formula
-----------------------------------------------------------

NPV formula works great if you have regular cash flows (i.e., the time period between the cash flow is the same).

But in case it’s not, you can’t use the NPV function.

For such cases, Excel gives you the **XNPV function**.

The XNPV function is similar to the NPV function, with one improvement, you can specify dates for cashflows and it will calculate the present value for each cash flow based on it.

Below is the syntax of the XNPV formula:

\=XNPV(rate, values, dates)

The above formula takes the following arguments:

*   **rate** – this is the discount rate for one time period. For example, if your cashflows are happening every year, this would be the annual discount rate. If these are quarterly, this would be quarterly discount rate
*   **value1, value2…** – these are the cashflow values and could be positive (inflow/income) or negative (outflow/payment).
*   **dates** – these are the dates for each cashflow

One important thing to remember when using the XNPV formula in Excel is that the first date is considered as the beginning of the time period.

Suppose you have a dataset as shown below and you want to calculate the net present value for this data:

![Dataset with cashflow and dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20622%20305'%3E%3C/svg%3E)

Below is the formula that will give us the net present value:

\=XNPV(D2,B2:B7,A2:A7)

![XNPV formula to get NPV when there are dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20621%20434'%3E%3C/svg%3E)

In the above example, the formula considers the first transaction (outflow of $100,000 on 01-01-2021) as the starting point and then calculates the overall net present value.

So in cases where you have cash flows/investments happening at irregular time intervals, you should use the XNPV formula.

NPV vs IRR – Which One Should you Use?
--------------------------------------

When analyzing project and investment decisions, NPV and IRR are the two most used methods.

Where NPV is Net Present Value and [IRR is Internal Rate of Return](https://trumpexcel.com/calculate-irr-excel/)
.

While both the methods would give you similar results in most cases, **NPV is considered a superior method when it comes to calculating the present value and viability of projects and investments**.

IRR has a few shortcomings that make it less accurate, and in some cases, the NPV method and the IRR method will give you different results.

In case of different results, the NPV method is considered right.

In this tutorial, I have covered how to calculate net present values in Excel using NPV and XNPV methods.

In case you have evenly spaced-out cash flows, you can use the NPV method. And in case you have irregular cash flows then you can use the XNPV method (which also uses the dates of the cash flow for the calculation).

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [How to Calculate Average Annual Growth Rate (AAGR) in Excel](https://trumpexcel.com/calculate-average-annual-growth-rate-excel/)
    
*   [How to Calculate Compound Interest in Excel + FREE Calculator](https://trumpexcel.com/compound-interest-calculator/)
    
*   [How to Calculate Correlation Coefficient In Excel](https://trumpexcel.com/correlation-coefficient-excel/)
    
*   [How to Calculate Standard Deviation In Excel](https://trumpexcel.com/standard-deviation/)
    
*   [Calculating Moving Average in Excel \[Simple, Weighted, & Exponential\]](https://trumpexcel.com/moving-average-excel/)
    
*   [How to Calculate Compound Annual Growth Rate (CAGR) in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    
*   [Loan Amortization Schedule in Excel](https://trumpexcel.com/loan-ammortization-schedule-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

### Leave a Comment [Cancel reply](https://trumpexcel.com/npv-excel/#respond)

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