# How to Calculate IRR in Excel (Easy Formula)

**Source:** https://trumpexcel.com/calculate-irr-excel

---

[Skip to content](https://trumpexcel.com/calculate-irr-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/calculate-irr-excel/#below-title)

When working with capital budgeting, IRR (Internal Rate of Return) is used to understand the overall rate of return a project would generate based on its future series of cash flows.

In this tutorial, I will show you how to **calculate IRR in Excel**, how is it different from another popular measure NPV, and different scenarios where you can use in-built IRR formulas in Excel.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/calculate-irr-excel/#)

Internal Rate of Return (IRR) Explained
---------------------------------------

IRR is a discount rate that is used to **measure the return of an investment based on periodical incomes**.

The IRR is shown as a [percentage](https://trumpexcel.com/calculate-percentages-excel/)
 and can be used to decide whether the project (an investment) is profitable for a company or not.

Let me explain IRR with a simple example.

Suppose you’re planning to buy a company for $50,000 that will generate $10,000 every year for the next 10 years. You can use this data to calculate the IRR of this project, which is the rate of return you get on your investment of $50,000.

In the above example, the IRR comes out to be 15% (we will see how to calculate that later in the tutorial). This means that it is equivalent to you investing your money at a 15% rate or return for 10 years.

Once you have the IRR value, you can use it to make decisions. So if you have any other project where the IRR is more than 15%, you should invest in that project instead.

Or, if you’re planning to take a loan or raise capital and buy this project for $50,000, make sure that the cost of the capital is less than 15% (else you pay more as the cost of the capital than you make from the project).

IRR Function in Excel – Syntax
------------------------------

Excel allows you to calculate the internal rate of return using the IRR function. This function has the following parameters:

\=IRR(values, \[guess\])

*   **values** – an array of cells that contain numbers for which you want to calculate the internal rate of return.
*   **guess** – a number that you guess is close to the result of the IRR (it’s not mandatory, and by default is 0.1 – 10%). This is used when there is a possibility of getting several results, and in that case, the function returns a result closest to a guess argument value.

Here are some important prerequisites for using the function:

*   IRR function will only consider numbers in the specified range of cells. Any logical values or text strings in the array or reference argument would be ignored
*   The amounts in the values parameter must be formatted as **numbers**
*   The ‘guess’ parameter must be a percentage, formatted as decimal (if it’s provided)
*   A cell where the function result is displayed must be formatted as a **percentage**
*   The amounts occur at **regular time intervals** (months, quarters, years)
*   One amount must be a **negative** cash flow (representing the initial investment), and other amounts should be **positive** cash flows, representing periodical incomes
*   All amounts should be in **chronological order** because the function calculates the result based on the order of the amounts

In case you want to calculate the IRR value where the cash flow comes at different time intervals, you should use the **XIRR function in Excel**, which also allows you to specify the dates for each cash flow. An example of this is covered later in the tutorial

Now, let’s have a look at some example to better understand how to use the IRR function in Excel.

Calculating IRR For Varying Cash Flows
--------------------------------------

Suppose you have a dataset as shown below, where we have the initial investment of $30,000 and then varying cash flow/income from it for the next six years.

![Dataset to calculate IRR](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20529%20341'%3E%3C/svg%3E)

For this data, we need to calculate the IRR, which can be done using the below formula:

\=IRR(D2:D8)

![IRR formula in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20530%20394'%3E%3C/svg%3E)

The result of the function is **8.22%**, which is the IRR of the cash flow after six years.

_Note:_ If the function returns a **#NUM!** error, you should fill the ‘guess’ parameter in the formula. This happens when the formula thinks that multiple values can be correct, and needs to have the guess value, in order to return the IRR nearest to the guess we provided. In most cases, you won’t need to use this though

Find Out When the Investment Yields Positive IRR
------------------------------------------------

You can also calculate the **IRR for every period** in a cash flow and see when exactly the investment is starting to have a positive internal rate of return.

Suppose we have the below dataset where I have all the cashflows listed in column C.

![Dataset to calculate when IRR turns positive](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20662%20309'%3E%3C/svg%3E)

The idea here is to find out the year in which the IRR of this investment turns positive (indicating when the project breaks even and becomes profitable).

To do this, instead of calculating the IRR for the entire project, we will find out the IRR for each year.

This can be done by using the below formula in cell D3 and then copying it for all the cells in the column.

\=IRR($C$2:C3)

![Yearwise IRR](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20663%20356'%3E%3C/svg%3E)

As you can see, the IRR after year 1 (values D2:D3) is -80%, after year 2 (D2:D4) -52%, etc.

This overview shows us that the investment of $30.000 with given cash flow has a positive IRR after the fifth year.

This can be useful when you’ve to choose from two project that have a similar IRR. It would be more lucrative to choose a project where the IRR turns positive faster, as it means less risk of recovering your initial capital.

Note that in the above formula, the reference of the range is mixed, that is the first [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
 ($C$2) is locked by having dollars signs before the row number and the column letter, and the second reference (C3) is not locked.

This makes sure that when you copy the formula down, it always considers the entire column till the row where the formula is applied.

Using IRR Function to Compare Multiple Projects
-----------------------------------------------

The IRR function in Excel can also be used to compare several projects’ investments and returns and see which project is the most profitable.

Suppose you have a dataset as shown below, where you have three projects with an initial investment (which is shown in negative as it’s an outflow) and then a series of positive cash flows.

![Data for comparing multiple projects](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20699%20324'%3E%3C/svg%3E)

To get the best project (that has the highest IRR, we will have to calculated the IRR for each project using the simple IRR formula:

\=IRR(C2:C8)

The above formula will give the IRR for project 1. Similarly, you can also calculate the IRR for the other two projects.

As you can see:

*   Project 1 has an IRR of **5.60%**
*   Project 2 has an IRR of **1.75%**
*   Project 3 has an IRR of **14.71%**.

![IRR for multiple projects](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20740%20341'%3E%3C/svg%3E)

If we suppose that the cost of capital is 4.50%, we can conclude that investment 2 is not acceptable (as it will lead to a loss), while Investment 3 is the most profitable, with the highest internal rate of return.

So if you have to make a decision to invest in only one project, you should go with Project 3, and if you could invest in more than one projects, you can invest in Project 1 and 3.

_**Definition**: If you’re wondering what’s is a cost of capital – it’s the money you will have to pay to get access to the money. For example, if you take $100K on a loan at 4.5% per year, your cost of capital is 4.5%. Similarly, if you issue preferential shares promising a_ 5% return to get 100K, your cost of capital would be 5%. In real-life scenarios, a company usually raises money from various sources, and its _cost of capital is a [weighted average](https://trumpexcel.com/weighted-average-in-excel/)
 of all these capital sources._

Calculating IRR for Irregular Cashflows
---------------------------------------

One of the limitations of the IRR function in Excel is that the cashflows must be periodic with the same interval between them.

But in real life, there can be instances where your projects pay off in irregular intervals.

For example, below is a dataset where the cashflows take place at irregular intervals (see dates in column A).

![Dataset for IRR with Dates](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20369%20342'%3E%3C/svg%3E)

In this example, we can not use the regular IRR function, but there is another function that can do this – the **XIRR function**.

XIRR function takes the cashflows as well as the dates, which allows it to account for irregular cashflows and give the correcyt IRR.

In this example, the IRR can be calculated using the below formula:

\=XIRR(B2:B8,A2:A8)

![XIRR formula in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20480%20394'%3E%3C/svg%3E)

In the above formula, the cashflows are specified as the first argument and the dates are specified as the second argument.

In case this formula returns a #NUM! error, you should enter the third argument with an approximate IRR that you expect. Don’t worry, it doesn’t have to be exact or even very close, just an approximation of what IRR you think it would yield. Doing this helps the formula iterate better and gives the result.

IRR vs NPV – Which is Better?
-----------------------------

When it comes to evaluating projects, both NPV and IRR are used, but **NPV is the more reliable method**.

[NPV is the Net Present Value](https://trumpexcel.com/npv-excel/)
 method where you evaluate all the future cash flows and calculate what will be the net present value of all those cashflows.

If this value comes out to be higher than your initial outflow, then the project is profitable, else the project is not profitable.

On the other hand, when you calculate IRR for a project, it tells you what would be the rate of return all the future cash flow so that you get the amount equivalent to the current outflow. For example, if you’re spending $100K today on a project which has an IRR or 10%, it tells you that if you discount all the future cash flows at 10% discount rate, you will get $100K.

While both methods are used while evaluating projects, using the NPV method is more reliable. There is a possibility that you may get conflicting results when evaluating a project using the NPV and the IRR method.

**In such a case, it is best to go with the recommendation you get using the NPV method.**

In general, IRR method has some drawbacks, which make NPV method more reliable:

*   Higher or method assumes that all the future cash flows generated from a project would be reinvested at the same rate of return (i.e., the IRR of the project). in most cases, this is an unreasonable assumption, as most of the cash flows would be reinvested into other projects which can have a different IR or insecurity such as bonds which would have a much lower rate of return.
*   In case you have multiple outflows and inflows in the project, there would be multiple IRRs for that project. This again makes comparison a lot difficult.

Despite its shortcomings, IRR is a good way to evaluate a project and can be used in conjunction with the NPV method when you are deciding on which project(s) to choose.

In this tutorial, I showed you how to use the **IRR function in Excel**. I also covered how to calculate the IRR in case you have irregular cash flows using the XIRR function.

I hope you found this tutorial useful!

**Other Excel tutorials you may also like:**

*   [How to Calculate Average Annual Growth Rate (AAGR) in Excel](https://trumpexcel.com/calculate-average-annual-growth-rate-excel/)
    
*   [How to Calculate Compound Interest in Excel + FREE Calculator](https://trumpexcel.com/compound-interest-calculator/)
    
*   [How to Calculate Correlation Coefficient In Excel](https://trumpexcel.com/correlation-coefficient-excel/)
    
*   [How to Calculate Standard Deviation In Excel](https://trumpexcel.com/standard-deviation/)
    
*   [Calculating Moving Average in Excel \[Simple, Weighted, & Exponential\]](https://trumpexcel.com/moving-average-excel/)
    
*   [How to Calculate Compound Annual Growth Rate (CAGR) in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    
*   [Loan Amortization Schedule in Excel (Free Template)](https://trumpexcel.com/loan-ammortization-schedule-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

1 thought on “How to Calculate IRR in Excel (Easy Formula)”
-----------------------------------------------------------

1.  I found that listing cash flows and using Excel’s IRR function makes checking an investment’s return straightforward. Switching to XIRR for uneven cash flows gave me a more accurate picture of the numbers.
    
    [Reply](https://trumpexcel.com/calculate-irr-excel/#comment-43850)
    

### Leave a Comment [Cancel reply](https://trumpexcel.com/calculate-irr-excel/#respond)

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