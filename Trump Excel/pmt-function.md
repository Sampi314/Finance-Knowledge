# Excel PMT function to Calculate Loan Payment Amount

**Source:** https://trumpexcel.com/pmt-function

---

[Skip to content](https://trumpexcel.com/pmt-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/pmt-function/#below-title)

Excel PMT function is one of the many financial [functions available in Excel](https://trumpexcel.com/excel-functions/)
.

It helps you calculate the payment you need to make for a loan when you know the total loan amount, interest rate, and the number of constant payments.

For example, suppose you buy a house for USD 200,000. Since you don’t have that kind of cash, you get a home loan at a 4% annual interest rate.

Now, you have to pay the loan installments every month for the next 20 years.

Excel PMT function can calculate the exact amount you need to pay every month.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/pmt-function/#)

PMT Function Syntax
-------------------

Below is the syntax of PMT function in Excel:

\=PMT(rate, nper, pv, \[fv\], \[type\])

*   **rate**: It is the interest rate you need to pay per period. For example, if it’s monthly payments, it will be rate/12. Similarly, if it’s quarterly, it will be rate/4.
*   **nper**: It is the number of periods in which the loan is to be paid back.
*   **pv**: It is the present value of the loan. In the above house loan example, this would be USD 200,000.
*   **fv**: \[optional argument\] It is the future value of your payments you want after the loan is paid off. In case you only want to get the loan paid and nothing else, omit it or make it 0.
*   **type**: \[optional argument\] If the payment is due at the end of the month, omit this or make this 0. In case the payment is due at the beginning of the month, make this 1. For example, if payment is due on 31st January, this will be 0, but if it’s due on 1st January, make this 1.

PMT Function Examples
---------------------

PMT function can be used in many different ways in Excel.

Below are some examples of using it.

### Example 1 – Calculating the Monthly Loan Amount in a House Mortgage

Suppose you have a house loan of $200,000 that needs to be paid back in 20 years when the payment is made every month, and the interest rate is 4%.

Here are details regarding the arguments:

*   rate –  4%/12 (since this the payment is monthly, you need to use the monthly rate).
*   nper – 20\*12 (since the loan is to be paid for 20 years every month)
*   pv – $200,000 (this is the loan value that I get today)

You can omit the optional arguments as these are not needed.

Below is the formula that will calculate the loan payment amount using the PMT function:

\=PMT(C3,C4,C2)

![Excel PMT Function - home loan payment calculation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20416%20249'%3E%3C/svg%3E)

Note that the loan payment is negative as it’s a cash outflow. If you want it to be positive, make the loan amount negative.

Also, remember that the interest rate remains constant throughout the period.

Also read: [Loan Amortization Schedule Template](https://trumpexcel.com/loan-ammortization-schedule-excel/)

### Example 2 – Monthly Payment to Grow Your Investment to USD 100,000

You can also use the PMT function to calculate how much you should invest per month to get a certain amount in the future.

For example, suppose you want to invest in a way to get USD 100,000 in 10 years when the annual interest rate is 5%.

Here is the formula that will calculate it:

\=PMT(C3,C4,,C2)

![Excel PMT Function - investment calculation](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20417%20249'%3E%3C/svg%3E)

Note that since the payments are monthly, the interest is taken as 5%/12.

In case the payments are made annually, you can use 5% as the interest rate (as shown below).

![Excel PMT Function - yearly investment](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20417%20254'%3E%3C/svg%3E)

**You May Also Like the Following Excel Tutorials:**

*   [Calculating Weighted Average in Excel](https://trumpexcel.com/weighted-average-in-excel/)
    
*   [Calculating CAGR in Excel](https://trumpexcel.com/calculate-cagr-excel/)
    
*   [Calculating Compound Interest in Excel](https://trumpexcel.com/compound-interest-calculator/)
    
*   [Calculating Standard Deviation in Excel](https://trumpexcel.com/standard-deviation/)
    
*   [Creating a Bell Curve in Excel](https://trumpexcel.com/bell-curve/)
    
*   [Calculating NPV (Net Present Value) in Excel](https://trumpexcel.com/npv-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

5 thoughts on “Using Excel PMT function to Calculate Loan Payment Amount”
-------------------------------------------------------------------------

1.  Templates are awesome. I needed a excel template autocalculated Bank Fixed deposit compund interest calculator for deposits of various banks, various interest, term in onr excel sheet along with financial year interest from 1-4-2018 to 31-03-2019. It may be middle of the deposit to FY. 10% interest deduction on fy interest for that period, if interest crosses INR Rs.50000/-for that FY for the deposits. Template is solicited to my email id submitted above. Thanks in advance with anticipating earliest as financial 2018-19 statement has to be submitted for income tax purpose.
    
    [Reply](https://trumpexcel.com/pmt-function/#comment-11780)
    
2.  I have a assuming problem in Excel (using PMT function) as below:
    
    “Mr. Adam wants to sign an insurance contract. He expects to earn $110000 after 18 years at 15% annual interest rate. How much money he must pay monthly for the insurance company, knowing that when signing the contract Mr. Adam paid $10000?”
    
    rate: 15%/12  
    nper: 18\*12  
    pv: 10000  
    fv: 110000
    
    I tried calculate PMT in 4 formulars:  
    1\. =PMT(15%/12,18\*12,10000,110000)  
    2\. =PMT(15%/12,18\*12,-10000,110000)  
    3\. =PMT(15%/12,18\*12,10000,-110000)  
    4\. =PMT(15%/12,18\*12,-10000,-110000)  
    I do not know which formular is right  
    I’m very confuse in using PMT function, especially using PV and FV parameter sign (- or +).  
    Could you explain to me the problem above?  
    I’ve found and read Excel’ help and other examples on the web but still not sure exactly.
    
    Thank you so much and looking forward to hearing from you!
    
    [Reply](https://trumpexcel.com/pmt-function/#comment-9436)
    
3.  I just shared it on facebook because it’s so useful and informative. I had to learn it the hard way, I wish that I knew about your website back then 😀
    
    Keep sharing these tips, I really appreciate your tips.
    
    [Reply](https://trumpexcel.com/pmt-function/#comment-9342)
    
    *   Thanks for sharing Shrikant! Glad you found it useful
        
        [Reply](https://trumpexcel.com/pmt-function/#comment-9343)
        
        *   Welcome Sumit, but you deserved it. Do you have some tips on how to print sub total on every page of an invoice? I’ve created an invoice template for a client in excel, but he wants that the subtotal should be printed on every page. I’d love to have your creative insights on it. Thanks
            
            [Reply](https://trumpexcel.com/pmt-function/#comment-9344)
            

### Leave a Comment [Cancel reply](https://trumpexcel.com/pmt-function/#respond)

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