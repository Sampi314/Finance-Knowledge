# Discount Rate Implicit in the Lease under ASC 842 | FinQuery

**Source:** https://finquery.com/blog/discount-rate-implicit-in-the-lease-asc-842

---

Discount Rate Implicit in the Lease under ASC 842
=================================================

by [Rachel Reed, Team Lead, Technical Accounting Consultants](https://finquery.com/author/rachel-reed/ "Posts by Rachel Reed, Team Lead, Technical Accounting Consultants")
 | Dec 18, 2025

1\. [What is the implicit rate under ASC 842?](https://finquery.com/blog/discount-rate-implicit-in-the-lease-asc-842/#what-is-implicit-rate-under-asc-842)

*   [Download our present value calculator to follow along](https://finquery.com/blog/discount-rate-implicit-in-the-lease-asc-842/#download-our-present-value-calculator)
    
*   [How to calculate the rate implicit in a lease under ASC 842](https://finquery.com/blog/discount-rate-implicit-in-the-lease-asc-842/#how-to-calculate-the-rate-implicit-in-a-lease-under-asc-842)
    
*   [If you are unable to calculate the implicit rate](https://finquery.com/blog/discount-rate-implicit-in-the-lease-asc-842/#if-you-are-unable-to-calculate-the-implicit-rate)
    

2\. [Summary](https://finquery.com/blog/discount-rate-implicit-in-the-lease-asc-842/#summary)

*   [Download our free lease vs. buy tool for simplified analysis](https://finquery.com/blog/discount-rate-implicit-in-the-lease-asc-842/#download-free-lease-vs-buy-tool)
    

3\. [Related articles](https://finquery.com/blog/discount-rate-implicit-in-the-lease-asc-842/#related-articles)

What is the implicit rate under ASC 842?
----------------------------------------

In [lease accounting](https://finquery.com/blog/lease-accounting-explained/)
, the rate implicit in the lease is the discount rate, or [interest rate](https://finquery.com/blog/interest-rates-asc-842-summary/)
, that the [lessor](https://finquery.com/blog/lessee-vs-lessor-differences-accounting-and-more-explained/)
 is charging the [lessee](https://finquery.com/blog/lessee-vs-lessor-differences-accounting-and-more-explained/)
. It is referred to as the implicit rate because it is not typically specified, or made explicit, in the lease agreement, so the lessee must attempt to infer the rate using additional information.

In order to calculate the [present value of the consideration in a lease contract](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/)
 and arrive at the opening lease liability or lease receivable amount, you must first know the amount of consideration, the [lease term](https://finquery.com/blog/determining-correct-dates-lease-term-asc-842/)
, and the [discount rate/interest rate](https://finquery.com/blog/interest-rates-asc-842-summary/)
. The total consideration and lease term are always explicitly defined in the lease agreement, but it’s unlikely that the discount rate is specified. The natural starting point, and what’s dictated under [ASC 842](https://finquery.com/blog/asc-842-summary-new-lease-accounting-standards/)
, would be to utilize the implicit rate within the lease agreement.

As a lessor, the implicit rate will be readily available since the lessor is the one drafting the terms of the lease and, therefore, is aware of what they are charging the lessee.

As the lessee, however, there can be complicating factors such as the lessee not being able to gather all the information that’s unique to a particular lease and needed to compute the rate the lessor is charging. In some instances, the lessor may be unwilling to share this information because it is the amount of profit they are making from the agreement.

In this article, we’ll walk through a step-by-step example of how to calculate the discount rate implicit in a lease and explain all the information necessary to accurately calculate the rate.

### Download our present value calculator to follow along:

[![Present Value Calculator](https://finquery.com/wp-content/uploads/2019/11/PresentValueCalculator.jpg)](https://finquery.com/project/present-value-calculation-tool/)

### How to calculate the rate implicit in a lease under ASC 842

The definition of the rate implicit in the lease from the glossary of key terms in ASC 842 is the rate the lessor is charging the lessee or that rate that causes the aggregate present value of:

*   the lease payments and
*   the amount the lessor expects to derive from the underlying asset at the end of the lease term

to equal the sum of the

1.  the fair value of the underlying asset minus any related investment tax credits retained and expected to be realized by lessor and
2.  any deferred [initial direct costs](https://finquery.com/blog/initial-direct-costs-under-asc-842-summary-example/)
     of the lessor

The graphic below further demonstrates the definition of the implicit rate:

![Definition of Implicit Rate](https://finquery.com/wp-content/uploads/2020/07/Definition-of-Implicit-Rate.png)While oftentimes the lessee will not have all of the inputs to calculate the rate implicit in the lease that is specifically being charged by the lessor, it can be helpful for a lessee to estimate what the rate implicit in the lease is. For that purpose, we will walk through an example here of how to estimate the rate implicit in the lease.

The lessee’s estimate of the implicit rate is typically more simplified than the definition in ASC 842 because in most instances, a lessee isn’t privy to information like the lessor’s initial direct costs, investment tax credits or even how much the lessor expects the asset to be worth at the end of the lease. In most cases, the lessee’s estimate of the rate implicit in the lease will solve for the rate that causes the present value of the lease payments and the expected residual value of the underlying asset at the end of the lease term to equal the fair value of the leased asset.

#### Example of calculating the rate implicit in a lease under ASC 842

Now, let’s look at a practical example. Assume Company X leases a piece of equipment for $4,000/year paid annually at the start of each year for a term of 6 years. Additionally, at the [commencement of the lease](https://finquery.com/blog/lease-commencement-date-start-date-under-us-gaap-explained/)
, Company X estimates the fair value of the leased asset to be $20,000 by utilizing various market resources. Remember, the fair market value is simply the price an asset would sell for under normal market conditions. For this example, assume that the lessee is not aware of any deferred initial direct costs of the lessor or investment tax credits retained by the lessor and the value of the asset is expected to be zero at the end of the lease.

*   **Lease Term**: 6 years
*   **[Base Rent](https://finquery.com/blog/prepaid-rent-other-rent-accounting-under-asc-842-explained/)
    **: $4,000/annually
*   **Fair Value**: $20,000

To arrive at the lessee’s estimate of the implicit rate, we’ll use the internal rate of return (IRR) function in Excel to calculate the rate that results in the present value of our lease payments equaling the fair value of the equipment in today’s dollars.

The table below represents the inputs to use in the IRR calculation in Excel. We start with period 0 to signify that the payments are made at the beginning of each period. The net cash outflows begin with the implied cash inflow for the receipt of the asset at the start of the lease (equal to asset’s fair value) and the lease payments over the term of the lease.

![Net Initial Investment](https://finquery.com/wp-content/uploads/2020/07/Net-Initial-Investment.png)The total net cash flows equal ($4,000), the sum of the inflow of the asset’s estimated fair value of $20,000 plus six years of ($4,000) annual payment outflows. The IRR function returns a rate of 7.93%.

![IRR Function](https://finquery.com/wp-content/uploads/2020/07/IRR-Function.png)

#### Validating the calculated implicit rate

To validate the appropriateness of the estimated implicit rate, we will perform a check [using the free LeaseQuery Present Value Calculator tool](https://finquery.com/project/present-value-calculation-tool/)
. Using the calculated implicit rate of 7.93% and the same cash payments over the same term, we calculate the present value of the payments to be $20,000 – the fair value of our asset.

![Validating the Calculated Implicit Rate](https://finquery.com/wp-content/uploads/2025/08/validating-the-calculated-implicit-rate.jpg)

### If you are unable to calculate the implicit rate

As mentioned above, while all of the inputs required to accurately calculate the implicit rate will not always be readily determinable by the lessee, it is useful to estimate the implicit rate to help evaluate a lease agreement. The fair value of the asset being leased can likely be estimated through online research, but as a lessee it’s unlikely you’ll know the amount of any investment tax credits retained by the lessor, any initial direct costs deferred by the lessor, or the expected future value that the lessor expects to receive from the asset at the end of your lease.

If these inputs are not available, ASC 842-20-30-3 provides an alternative to the calculation of the implicit rate: “A lessee should use the rate implicit in the lease whenever that rate is readily determinable. If the rate implicit in the lease is not readily determinable, a lessee uses its incremental borrowing rate.” Therefore, if you are a lessee, it’s likely you’ll use an [incremental borrowing rate (IBR](https://finquery.com/blog/incremental-borrowing-rate-discount-rate-asc-842-ifrs-16-gasb-87/)
) to calculate the present value of your lease payments. (Private entities have the additional option of using a [risk-free rate](https://finquery.com/blog/interest-rates-asc-842-summary/)
 that is commensurate with lease term).

#### Download our free implicit interest rate calculator:

We’ve created a free Excel calculator that can help you determine the discount rates implicit in your leases. You can easily enter all the necessary lease information into the fields at the top of the spreadsheet and obtain your implicit rate under ASC 842. Click the link below to get the calculator:

[![Implicit Interest Rate Calculator](https://finquery.com/wp-content/uploads/2025/04/implicit-interest-rate-calculator-banner.jpg)](https://finquery.com/project/lease-implicit-interest-rate-excel-calculator-tool/)

Summary
-------

The rate implicit in the lease is the interest rate the lessor is charging the lessee. This rate will always be known to the lessor since they are preparing the terms of the lease based on the profit they would like to earn. However, the lessee will not know the specific implicit rate of the lease. Knowing how to estimate the rate will help the lessee make an informed decision regarding the value of the lease agreement.

With the use of a simple Excel function, online research, and the payment terms of a lease, the lessee is able to easily estimate the rate implicit in any lease and then verify that rate with our present value calculator. Although, under ASC 842 the lessee will only use the implicit rate to calculate a lease liability (and related [ROU asset](https://finquery.com/blog/right-of-use-asset-lease-liability-asc-842-ifrs-16-gasb-87/)
) when they have all of the required information from the lessor, knowing how to calculate the implicit rate is beneficial to your organization. A reasonable estimate of the implicit rate of a lease will assist the lessee in a better understanding of the facts necessary to make a [lease vs. buy decision](https://finquery.com/project/lease-vs-buy-calculator-excel-tool/)
 for purchases of property and equipment.

### Download our free lease vs. buy tool for simplified analysis:

[![Lease vs Buy Calculator Excel Template](https://finquery.com/wp-content/uploads/2019/08/lease-vs-buy-calculator.jpg)](https://finquery.com/project/lease-vs-buy-calculator-excel-tool/)

Related articles
----------------

[![How to Calculate the Present Value (PV) of Future Lease Payments in Excel](https://finquery.com/wp-content/uploads/2020/06/blogfeat-how-to-calculate-present-value-of-future-lease-payments-in-excel.jpg)](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/)

### [How to Calculate the Present Value (PV) of Future Lease Payments in Excel](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/)

[![Interest Rates under ASC 842 Explained: Implicit, Incremental Borrowing, Risk-Free](https://finquery.com/wp-content/uploads/2021/10/asc-842-interest-rates-blogfeat.jpg)](https://finquery.com/blog/interest-rates-asc-842-summary/)

### [Interest Rates under ASC 842 Explained: Implicit, Incremental Borrowing, Risk-Free](https://finquery.com/blog/interest-rates-asc-842-summary/)

[![Lease vs. Buy Analysis and Calculator for Business – How to Determine When to Lease or Buy an Asset](https://finquery.com/wp-content/uploads/2022/08/lease-vs-buy-analysis-calculator-business-blogfeat.jpg)](https://finquery.com/blog/lease-vs-buy-analysis-calculator-business/)

### [Lease vs. Buy Analysis and Calculator for Business – How to Determine When to Lease or Buy an Asset](https://finquery.com/blog/lease-vs-buy-analysis-calculator-business/)

[![Incremental Borrowing Rate for IFRS 16, ASC 842, and GASB 87: Discount Rates and When to Use Them](https://finquery.com/wp-content/uploads/2018/07/discount-borrowing-rates-under-ifrs-16-asc-842-explained-blogfeat.jpg)](https://finquery.com/blog/incremental-borrowing-rate-discount-rate-asc-842-ifrs-16-gasb-87/)

### [Incremental Borrowing Rate for IFRS 16, ASC 842, and GASB 87: Discount Rates and When to Use Them](https://finquery.com/blog/incremental-borrowing-rate-discount-rate-asc-842-ifrs-16-gasb-87/)

[![Implicit Interest Rate Calculator](https://finquery.com/wp-content/uploads/2025/04/implicit-interest-rate-calculator-sidebarwidget.jpg)](https://finquery.com/project/lease-implicit-interest-rate-excel-calculator-tool/)

![Rachel Reed](https://finquery.com/wp-content/uploads/2025/01/rachel-reed-author.jpg)

About the author
----------------

Rachel Reed, Team Lead, Technical Accounting Consultants

Rachel Reed holds both Bachelor's and Master's degrees in Accounting from the University of Mississippi. She began her career in Accounting as an Assurance Intern at Ernst & Young (EY), where she eventually progressed into a role working in the audit practice. With her background in accounting and financial services, she currently serves as a Technical Accounting Manager and Team Lead of Technical Accounting Consultants.