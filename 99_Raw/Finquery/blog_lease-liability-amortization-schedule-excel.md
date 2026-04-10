# Lease Liability Amortization Schedule: Calculating It in Excel

**Source:** https://finquery.com/blog/lease-liability-amortization-schedule-excel

---

Lease Liability Amortization Schedule: How to Calculate It in Excel
===================================================================

by [Rachel Reed, Team Lead, Technical Accounting Consultants](https://finquery.com/author/rachel-reed/ "Posts by Rachel Reed, Team Lead, Technical Accounting Consultants")
 | Nov 18, 2019

1\. [What is lease liability?](https://finquery.com/blog/lease-liability-amortization-schedule-excel/#lease-liability)

2\. [How to create the lease amortization schedule and calculate your lease liability](https://finquery.com/blog/lease-liability-amortization-schedule-excel/#lease-amortization-schedule-example)

*   [Create five-column spreadsheet](https://finquery.com/blog/lease-liability-amortization-schedule-excel/#create-spreadsheet)
    
*   [Enter the number of periods and cash payments](https://finquery.com/blog/lease-liability-amortization-schedule-excel/#cash-payments-period)
    
*   [Enter expense formula](https://finquery.com/blog/lease-liability-amortization-schedule-excel/#expense-formula)
    
*   [Fill expense column](https://finquery.com/blog/lease-liability-amortization-schedule-excel/#fill-expense)
    
*   [Enter liability reduction formula](https://finquery.com/blog/lease-liability-amortization-schedule-excel/#liability-reduction-formula)
    
*   [Enter liability balance formula](https://finquery.com/blog/lease-liability-amortization-schedule-excel/#liability-balance-formula)
    
*   [Fill remaining liability balance](https://finquery.com/blog/lease-liability-amortization-schedule-excel/#fill-liability-balance)
    
*   [Perform “What-If Analysis” on liability balance](https://finquery.com/blog/lease-liability-amortization-schedule-excel/#what-if-analysis)
    
*   [Set liability balance value to 0 with goal seek](https://finquery.com/blog/lease-liability-amortization-schedule-excel/#set-liability-balance-zero)
    
*   [Click “OK”](https://finquery.com/blog/lease-liability-amortization-schedule-excel/#click-ok)
    

3\. [Related articles](https://finquery.com/blog/lease-liability-amortization-schedule-excel/#related-articles)

Previously, we covered [how to calculate the present value of lease payments using Excel spreadsheets](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/)
. In this article, we will demonstrate how to calculate the present value of your lease payments as well as prepare the liability amortization schedule for the [lease liability](https://finquery.com/blog/right-of-use-asset-lease-liability-asc-842-ifrs-16-gasb-87/)
 in the same step, using Excel.

Private companies in particular may be tempted to try to use an Excel spreadsheet for lease accounting, but this information is important even if you plan to use [lease accounting software](https://finquery.com/lease-accounting-software/)
 for compliance with the new standard. You can use the information in this blog to ensure that your chosen software provider is performing this calculation accurately.

What is the lease liability?
----------------------------

The lease liability is defined as the present value of your future lease payments. This is calculated as the initial step in accounting for a lease under [ASC 842](https://finquery.com/blog/asc-842-summary-new-lease-accounting-standards/)
, and this amount is then used to calculate the [ROU (right-of-use) asset](https://finquery.com/blog/right-of-use-asset-lease-liability-asc-842-ifrs-16-gasb-87/)
, that is recorded in addition to the liability for [operating leases](https://finquery.com/blog/operating-lease-accounting-asc-842-explained-example/)
 and [capital leases](https://finquery.com/blog/capital-lease-accounting-finance-lease-accounting-example/)
.

> _A **lessee’s** obligation to make the **lease payments** arising from a **lease**, measured on a discounted basis._

How to create the lease amortization schedule and calculate your lease liability
--------------------------------------------------------------------------------

Download our free present value calculator to follow along:

[![Present Value Calculator](https://finquery.com/wp-content/uploads/2019/11/PresentValueCalculator.jpg)](https://finquery.com/project/present-value-calculation-tool/)

Follow the steps below to calculate the present value of lease payments and the lease liability amortization schedule using Excel when the payment amounts are not constant, illustrated with an example:

> _Calculate the present value of lease payments for a 10-year lease with annual payments of $1,000 with 5% escalations annually, paid in advance. Assume the rate inherent in the lease is 6%._

[![Operating Lease Accounting under ASC 842](https://finquery.com/wp-content/uploads/2020/07/discount-rate-implicit-in-the-lease-asc-842-featimg.jpg)](https://finquery.com/blog/discount-rate-implicit-in-the-lease-asc-842/)

### [Discount Rate Implicit in the Lease under ASC 842](https://finquery.com/blog/discount-rate-implicit-in-the-lease-asc-842/)

[![Interest Rate Implicit in the Lease under IFRS 16 Explained](https://finquery.com/wp-content/uploads/2020/08/interest-rate-implicit-in-the-lease-ifrs-16-blogfeat.jpg)](https://finquery.com/blog/interest-rate-implicit-in-the-lease-ifrs-16/)

### [Interest Rate Implicit in the Lease under IFRS 16 Explained](https://finquery.com/blog/interest-rate-implicit-in-the-lease-ifrs-16/)

### Step 1: Create an Excel spreadsheet with these five columns

Create a new Excel spreadsheet and title five columns with the following headers: Period, Cash, Expense, Liability Reduction, and Liability Balance, as shown below:

![Create Excel Spreadsheet with Five Columns](https://finquery.com/wp-content/uploads/2019/11/Step-1-Create-an-Excel-spreadsheet-with-these-five-columns.png)

### Step 2: Enter the number of periods and cash payments

Enter the number of periods corresponding to the [lease term](https://finquery.com/blog/lease-commencement-date-start-date-under-us-gaap-explained/)
 starting from 0, and enter the cash payments in each period. Because payments are made in advance, the first payment of $1,000 is made in period 0. The annual payments then escalate at a 5% rate. Please see illustration below:

![Enter Number Periods and Cash Payments](https://finquery.com/wp-content/uploads/2019/11/Step-2-Enter-number-periods-and-cash-payments.png)

### Step 3: Enter the expense formula

Enter “0” for expense in period 0 (because payments are made in advance). In Expense for period 1, enter the cell reference for the period 0 liability balance and multiply by 6%. See below.

![Enter Expense Formula](https://finquery.com/wp-content/uploads/2019/11/Step-3-Enter-the-expense-formula.png)

### Step 4: Fill the expense column

Copy the formula for expense in period 1 down for the remaining Expense rows.

![Fill Expense Column](https://finquery.com/wp-content/uploads/2019/11/Step-4-Fill-the-expense-column.png)

### Step 5: Enter the formula for liability reduction

The formula for each liability reduction amount is the corresponding cash payment minus the corresponding expense. See below.

![Enter Formula for Liability Reduction](https://finquery.com/wp-content/uploads/2019/11/Step-5-Enter-the-formula-for-liability-reduction.png)Copy the formula down the entire Liability Reduction column.

### Step 6: Enter the formula for liability balance

Enter “0” for the Liability Balance in the line above period 0. In liability balance for period 0, enter the formula for the above cell’s liability balance minus the liability reduction in period 0. This will equal the previous period’s liability balance, reduced by the current liability reduction (see below).

![Enter Excel formula for Liability Balance](https://finquery.com/wp-content/uploads/2019/11/Step-6-Enter-the-formula-for-liability-balance.png)

### Step 7: Fill the remaining liability balance column

Copy the formula for the liability balance in period 0 down for the remaining Liability Balance rows.

![Fill Liability Balance Columns](https://finquery.com/wp-content/uploads/2019/11/Step-7-Fill-the-remaining-liability-balance-column.png)

### Step 8: Perform “What-If Analysis” on the liability balance

Select the liability balance for period 9. In the top bar in Excel, go to the “Data” tab, then the “What-if Analysis” Tab, then select “Goal Seek.”

![What-If Analysis in Excel](https://finquery.com/wp-content/uploads/2019/11/Step-8-Perform-%E2%80%9CWhat-If-Analysis%E2%80%9D-on-the-liability-balance.png)

### Step 9: Set liability balance value to 0 by using goal seek

In the dialog box that follows, make sure “Set cell” is set to the cell representing the liability balance for period 9, in the “To Value” enter 0, and in “By changing cell” enter the cell reference representing the liability balance for the period above period 0. See below.

![Goal Seek in Excel](https://finquery.com/wp-content/uploads/2019/11/Step-9-Set-liability-balance-value-to-0-by-using-goal-seek.png)

### Step 10: Click “OK”

Click “OK” to have Excel run the goal seek analysis. Excel will provide the beginning liability balance and your amortization schedule will be completed automatically as a result of the formulas you input. See below.

![Lease Amortization Schedule](https://finquery.com/wp-content/uploads/2019/11/Step-10-Click-%E2%80%9COK%E2%80%9D.png)

For this example, the present value of a 10-year lease with payments of $1,000 annually, 5% escalations, and a rate inherent in the lease of 6% is $9,586.

### Summary

This schedule will provide you with the calculations for your journal entries for the entire life of the lease, if you’re using Excel. If you’re using a lease accounting software, the information above will help you cross-check the calculations performed by your provider so you can ensure accuracy.

Related articles
----------------

[![ASC 842 Lease Accounting: Summary, Examples, Effective Dates, and More](https://finquery.com/wp-content/uploads/2021/04/asc-842-lease-accounting-guide-blogfeat.jpg)](https://finquery.com/blog/asc-842-summary-new-lease-accounting-standards/)

### [ASC 842 Lease Accounting: Summary, Examples, Effective Dates, and More](https://finquery.com/blog/asc-842-summary-new-lease-accounting-standards/)

[![IFRS 16 Leases: Summary, Example, Journal Entries, and Disclosures](https://finquery.com/wp-content/uploads/2021/02/ifrs-16-leases-summary-examples-entries-disclosures-blogfeat.webp)](https://finquery.com/blog/ifrs-16-leases-summary-examples-entries-disclosures/)

### [IFRS 16 Leases: Summary, Example, Journal Entries, and Disclosures](https://finquery.com/blog/ifrs-16-leases-summary-examples-entries-disclosures/)

[![Incremental Borrowing Rate for IFRS 16, ASC 842, and GASB 87: Discount Rates](https://finquery.com/wp-content/uploads/2018/07/discount-borrowing-rates-under-ifrs-16-asc-842-explained-blogfeat.jpg)](https://finquery.com/blog/incremental-borrowing-rate-discount-rate-asc-842-ifrs-16-gasb-87/)

### [Incremental Borrowing Rate for IFRS 16, ASC 842, and GASB 87: Discount Rates](https://finquery.com/blog/incremental-borrowing-rate-discount-rate-asc-842-ifrs-16-gasb-87/)

[![Rent Expense Explained and an Example of Straight-Line Rent under US GAAP](https://finquery.com/wp-content/uploads/2022/06/rent-expense-blogfeat.jpg)](https://finquery.com/blog/rent-expense-explained-example-straight-line-rent/)

### [Rent Expense Explained and an Example of Straight-Line Rent under US GAAP](https://finquery.com/blog/rent-expense-explained-example-straight-line-rent/)

[![Present Value Calculator](https://finquery.com/wp-content/uploads/2020/12/present-value-calculator-blog-sidebarwidget.jpg)](https://finquery.com/project/present-value-calculation-tool/)

![Rachel Reed](https://finquery.com/wp-content/uploads/2025/01/rachel-reed-author.jpg)

About the author
----------------

Rachel Reed, Team Lead, Technical Accounting Consultants

Rachel Reed holds both Bachelor's and Master's degrees in Accounting from the University of Mississippi. She began her career in Accounting as an Assurance Intern at Ernst & Young (EY), where she eventually progressed into a role working in the audit practice. With her background in accounting and financial services, she currently serves as a Technical Accounting Manager and Team Lead of Technical Accounting Consultants.