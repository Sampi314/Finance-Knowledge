# Interest Rate Implicit in the Lease under IFRS 16 | LeaseQuery

**Source:** https://finquery.com/blog/interest-rate-implicit-in-the-lease-ifrs-16

---

Interest Rate Implicit in the Lease under IFRS 16 Explained
===========================================================

by [Rachel Reed, Team Lead, Technical Accounting Consultants](https://finquery.com/author/rachel-reed/ "Posts by Rachel Reed, Team Lead, Technical Accounting Consultants")
 | Aug 27, 2020

1\. [What is the implicit interest rate under IFRS 16?](https://finquery.com/blog/interest-rate-implicit-in-the-lease-ifrs-16/#implicit-interest-rate-ifrs16)

*   [Implicit rate: ASC 842 vs. IFRS 16](https://finquery.com/blog/interest-rate-implicit-in-the-lease-ifrs-16/#asc842-vs-ifrs16)
    

2\. [Example: Calculate the interest rate implicit in a lease under IFRS 16](https://finquery.com/blog/interest-rate-implicit-in-the-lease-ifrs-16/#interest-rate-implicit-ifrs16)

3\. [Summary](https://finquery.com/blog/interest-rate-implicit-in-the-lease-ifrs-16/#summary)

4\. [Related articles](https://finquery.com/blog/interest-rate-implicit-in-the-lease-ifrs-16/#related-articles)

What is the implicit interest rate under IFRS 16?
-------------------------------------------------

The rate implicit in the lease is the interest rate charged by the lessor in the lease agreement. This is essentially the return or margin the lessor is receiving from the lease agreement, and as such, the lessor can be unwilling to name the rate outright. Since the rate of return for the lease is not stated, it is implied.

Under [IFRS 16](https://finquery.com/blog/ifrs-16-leases-summary-examples-entries-disclosures/)
, the [lessee](https://finquery.com/blog/lessee-vs-lessor-differences-accounting-and-more-explained/)
 will use the implicit rate to calculate the initial measurement of the lease liability, assuming the rate can be readily determined. More often than not, as a lessee, this rate is not readily determinable as it is driven by [lessor](https://finquery.com/blog/lessee-vs-lessor-differences-accounting-and-more-explained/)
 inputs such as costs and profit assumptions. If the rate is not readily determinable to the lessee, the lessee should use their own [incremental borrowing rate](https://finquery.com/blog/incremental-borrowing-rate-discount-rate-asc-842-ifrs-16-gasb-87/)
 in place of the implicit rate. The implicit rate is always known to the lessor since the lessor is the one drafting the terms of the lease, and therefore is aware of what interest rate they have incorporated within the lease agreement.

Under IFRS 16, the lessor will use the implicit rate to perform the lease classification test at lease inception or at the date of a modification, by calculating whether the [present value of the lease payments](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/)
 (discounted at the implicit rate) represents substantially all of the fair value of the underlying asset. Also under IFRS 16 lessors party to finance leases use the interest rate implicit rate in the lease to measure the net investment in the lease. The net investment in the lease is presented as a receivable on the statement of net position.

Within IFRS 16 Appendix A, the Glossary specifically defines the interest rate implicit in the lease as the rate of interest that causes the present value of:

*   The lease payments and,
*   the unguaranteed residual value to equal the sum of:
    1.  the fair value of the underlying asset and,
    2.  any initial direct costs of the lessor.

Remember that the lease payments the lessor uses to determine its implicit rate typically exclude most variable lease payments. Therefore, for leases with multiple components and variable consideration, the rate implicit in the lease does not represent the entire expected return for the lessor.

The graphic below further demonstrates the implicit rate as defined by IFRS 16:

![Implicit Rate Graphic](https://finquery.com/wp-content/uploads/2020/08/Implicit-Rate-Graphic.png)

### Implicit rate: ASC 842 vs. IFRS 16

The definition of the implicit rate as stated in IFRS 16 differs slightly from the definition of the rate implicit in the lease as defined within ASC 842. Within the glossary of terms in [ASC 842](https://finquery.com/blog/asc-842-summary-new-lease-accounting-standards/)
, the implicit rate is defined as:

> _“The rate of interest that, at a given date, causes the aggregate present value of (a) the lease payments and (b) the amount that a lessor expects to derive from the underlying asset following the end of the [lease term](https://finquery.com/blog/lease-commencement-date-start-date-under-us-gaap-explained/)
>  to equal the sum of (1) the fair value of the underlying asset minus any related investment tax credit retained and expected to be realized by the lessor and (2) any deferred [initial direct costs](https://finquery.com/blog/initial-direct-costs-under-asc-842-summary-example/)
>  of the lessor.”_

Under ASC 842, related investment tax credits retained and expected to be realized by the lessor are explicitly included in the calculation. This is not the case within the definition in IFRS 16, which only includes the fair value of the underlying asset within the implicit rate calculation.

For further discussion and an example of the implicit rate calculation within ASC 842, [review this article](https://finquery.com/blog/discount-rate-implicit-in-the-lease-asc-842/)
.

To demonstrate how the lessor can calculate the implicit rate in accordance with IFRS 16, we will take a look at an example and walk through how to calculate the rate implicit in a lease using the internal rate of return (IRR) function in Excel.

**Download our present value calculator to follow along:**

[![Present Value Calculator](https://finquery.com/wp-content/uploads/2019/11/PresentValueCalculator.jpg)](https://finquery.com/project/present-value-calculation-tool/)

Example: Calculate the interest rate implicit in a lease under IFRS 16
----------------------------------------------------------------------

The following is the set of facts we will use in our example of a tractor lease:

*   Lessor charges $5,000 annually, paid directly to the lessor at the start of each year
*   Lease commencement: 1/1/2020 (after transition to IFRS 16)
*   Lease end date: 12/31/2024
*   5 year lease term
*   The fair value of the tractor at lease commencement: $20,000
*   The lessor expects the fair value of the tractor at the end of the 5 year lease term (the unguaranteed residual value) will be $1,000
*   Lessor incurs initial direct costs of $1,500

Because the lessor knows all of the inputs required to calculate the implicit rate, they can use a simple calculation to determine this rate. As we discussed, the implicit rate is the rate that causes the present value of (a) the lease payments and (b) the unguaranteed residual value to equal the sum of (i) the fair value of the underlying asset and (ii) any initial direct costs of the lessor. We can demonstrate this calculation by utilizing the IRR function in Excel.

The table below represents the amounts the lessor will include in the cash inflows and outflows of the IRR calculation. The payments are due at the beginning of each period, so we have labelled period 0 to signify that there is a payment made at the beginning of the lease before interest is accrued. The initial direct costs and the implied cash outflow for the fair value of the asset that is transferred to the lessee also occur at the beginning of the lease.

In period 0, the fair value of $20,000 and initial direct costs of $1,500 cash outflows are netted against the $5,000 payment received in advance to arrive at a net cash outflow of $16,500 made at lease commencement.

In periods 1 through 4, the lessor receives payments of $5,000. Period 5 represents the end of the lease term, when the unguaranteed residual value was estimated at $1,000.

![Cash inflows and outflows of IRR calculation](https://finquery.com/wp-content/uploads/2020/08/Implicit-Rate-Table-1.png)

After calculating the cash inflows and outflows per period, the IRR function is used (as displayed below) on the net cash flows.

![Internal Rate of Return function](https://finquery.com/wp-content/uploads/2020/08/Implicit-Rate-Table-2.png)

The IRR function in Excel returns a rate of 9.92% based on the net cash flows.

![Result of Excel IRR function](https://finquery.com/wp-content/uploads/2020/08/Implicit-Rate-Table-3.png)

### Validating the calculated implicit rate

We are able to validate the calculation of the implicit rate we calculated using the IRR function above by using the free [LeaseQuery Present Value Calculator](https://finquery.com/project/present-value-calculation-tool/)
 tool. We will validate our calculation in two steps, first by calculating the present value of the lease payments and next by calculating the present value of the unguaranteed residual value.

As illustrated below, we populate within our present value calculator the IRR of 9.92% and input the same cash payments and same term we outlined at the beginning of this example, we calculate the present value of the lease payments to be $20,877.

![Implicit Rate Present Value Example](https://finquery.com/wp-content/uploads/2020/08/Implicit-Rate-PV-Example-1.png)

As a reminder, the implicit rate is the rate at which the present value of the lease payments and the unguaranteed residual value equal the sum of the fair value of the underlying asset and any initial direct costs of the lessor.

In the calculation above, we calculated the present value of the lease payments, and now we must calculate the present value of the unguaranteed residual value of $1,000. Using the present value calculator, as illustrated below, we calculate the present value of $1,000 paid five years in the future at a rate of 9.92% to be $623. To calculate the present value of the unguaranteed residual value, we use an end of period payment because the asset is returned to the lessor on the last day of the lease.

![Present value of unguaranteed residual value](https://finquery.com/wp-content/uploads/2020/08/Implicit-Rate-PV-Example-2.png)

The present value of the lease payments of $20,877 plus the present value of the unguaranteed residual value of $623 equals $21,500. The sum of the fair value of the tractor, $20,000, and the initial direct costs of $1,500, also equals $21,500, thus proving our Excel IRR calculation of the implicit rate of 9.92% to be correct.

The example we went through above is specifically related to a lessor. However, if you are a lessee and the required inputs for the IRR calculation are available, you can use the same formula and steps. In practice, it is not likely that the lessee will have the inputs required for this calculation readily available. When this is the case, the lessee can use the [incremental borrowing rate](https://finquery.com/blog/incremental-borrowing-rate-discount-rate-asc-842-ifrs-16-gasb-87/)
 (IBR).

Summary
-------

The rate implicit in the lease is the interest rate set by the lessor in the lease agreement. This is the rate at which the present value of the lease payments and the unguaranteed residual value equal the sum of the fair value of the underlying asset and any initial direct costs of the lessor. The lessor will always know, or be able to calculate, this rate since they are the ones preparing the lease. However, it is also beneficial for the lessee to understand how to calculate this rate so they are able to analyze the financial terms of the lease agreement to determine if they are mutually beneficial.

Related articles
----------------

[![Incremental Borrowing Rate for IFRS 16, ASC 842, and GASB 87: Discount Rates and When to Use Them](https://finquery.com/wp-content/uploads/2018/07/discount-borrowing-rates-under-ifrs-16-asc-842-explained-blogfeat.jpg)](https://finquery.com/blog/incremental-borrowing-rate-discount-rate-asc-842-ifrs-16-gasb-87/)

### [Incremental Borrowing Rate for IFRS 16, ASC 842, and GASB 87: Discount Rates and When to Use Them](https://finquery.com/blog/incremental-borrowing-rate-discount-rate-asc-842-ifrs-16-gasb-87/)

[![Lease vs. Buy Analysis and Calculator for Business – How to Determine When to Lease or Buy an Asset](https://finquery.com/wp-content/uploads/2022/08/lease-vs-buy-analysis-calculator-business-blogfeat.jpg)](https://finquery.com/blog/lease-vs-buy-analysis-calculator-business/)

### [Lease vs. Buy Analysis and Calculator for Business – How to Determine When to Lease or Buy an Asset](https://finquery.com/blog/lease-vs-buy-analysis-calculator-business/)

[![IFRS 16 Leases: Summary, Example, Journal Entries, and Disclosures](https://finquery.com/wp-content/uploads/2021/02/ifrs-16-leases-summary-examples-entries-disclosures-blogfeat.webp)](https://finquery.com/blog/ifrs-16-leases-summary-examples-entries-disclosures/)

### [IFRS 16 Leases: Summary, Example, Journal Entries, and Disclosures](https://finquery.com/blog/ifrs-16-leases-summary-examples-entries-disclosures/)

[![Interest Expense Calculation Explained with a Finance Lease Example and Journal Entries](https://finquery.com/wp-content/uploads/2021/06/interest-expense-finance-lease-blogfeat.jpg)](https://finquery.com/blog/interest-expense-calculation-explained/)

### [Interest Expense Calculation Explained with a Finance Lease Example and Journal Entries](https://finquery.com/blog/interest-expense-calculation-explained/)

[![ASC 842 Lease Accounting Guide](https://finquery.com/wp-content/uploads/2022/10/ultimate-lease-accounting-guide-sidebarwidget.jpg)](https://finquery.com/download-the-ultimate-lease-accounting-guide/)

![Rachel Reed](https://finquery.com/wp-content/uploads/2025/01/rachel-reed-author.jpg)

About the author
----------------

Rachel Reed, Team Lead, Technical Accounting Consultants

Rachel Reed holds both Bachelor's and Master's degrees in Accounting from the University of Mississippi. She began her career in Accounting as an Assurance Intern at Ernst & Young (EY), where she eventually progressed into a role working in the audit practice. With her background in accounting and financial services, she currently serves as a Technical Accounting Manager and Team Lead of Technical Accounting Consultants.