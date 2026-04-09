# Lease Modification Accounting for ASC 842: Operating to Operating

**Source:** https://finquery.com/blog/lease-modification-accounting-asc-842-operating-lease-to-operating-lease

---

Lease Modification Accounting under ASC 842: Operating Lease to Operating Lease
===============================================================================

by [George Azih, Founder](https://finquery.com/author/george-azih/ "Posts by George Azih, Founder")
 | Aug 28, 2019

In this blog, we will give an example of how to account for a lease modification [under ASC 842](https://finquery.com/blog/asc-842-summary-new-lease-accounting-standards/)
 that does not expand or add additional assets to the original lease, but rather increases the [lease term](https://finquery.com/blog/determining-correct-dates-lease-term-asc-842/)
 and changes the payment amounts. Because there isn’t an additional right of use (ROU) asset granted per 842-10-25-1, the [lessee](https://finquery.com/blog/lessee-vs-lessor-differences-accounting-and-more-explained/)
 would use the updated lease payments and [an updated discount rate](https://finquery.com/blog/incremental-borrowing-rate-discount-rate-asc-842-ifrs-16-gasb-87/)
 to [remeasure the lease liability](https://finquery.com/blog/right-of-use-asset-lease-liability-asc-842-ifrs-16-gasb-87/)
 and would recognize any difference between the new lease liability and the old lease liability as an adjustment to the ROU asset. If that sounds complicated, it is. It is complicated because there is no discussion on how to amortize the ROU asset after the modification. Here’s an example:

Assume a 10-year lease with annual payments in arrears of $100,000 increasing by 3% each year. Assume the discount rate is 6%, and for purposes of this example, [assume this is an operating lease](https://finquery.com/blog/operating-lease-accounting-asc-842-explained-example/)
. The initial amortization schedule for this lease is as follows:

![Initial Amortization Schedule](https://finquery.com/wp-content/uploads/2019/08/Initial_Ammortization_Schedule-min1.png)

You can [build your own amortization schedule](https://finquery.com/blog/lease-liability-amortization-schedule-excel/)
 like the one above using Excel or download our free present value calculator:

[![Present Value Calculator](https://finquery.com/wp-content/uploads/2019/11/PresentValueCalculator.jpg)](https://finquery.com/project/present-value-calculation-tool/)

Initial journal entry:
----------------------

Based on the amortization schedule above, the initial journal entry to make is as follows:

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| ROU Asset | 831,880.38 |     |
| Operating Lease Liability |     | 831,880.38 |

_To record the lease liability and corresponding ROU asset at [lease commencement](https://finquery.com/blog/lease-commencement-date-start-date-under-us-gaap-explained/)
_

Journal entry 2:
----------------

Please note that the journal entry above is made at the beginning of year one. At the end of year one when payment is made (recall that payments are made in arrears in this example), the journal entry to reflect the payment is as follows:

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| Rent Expense | 49,912.82 |     |
| Lease Liability | 50,087.18 |     |
| Cash |     | 100,000.00 |

_To record year one rent payment of 100,000_

Journal entry 3:
----------------

In addition to the entry above, the ROU asset must be amortized. It is amortized as the difference between [straight-line rent expense](https://finquery.com/blog/rent-expense-explained-example-straight-line-rent/)
 and liability expense. Straight-line rent expense is $114,638.79 while the liability expense for year one is $49,912.82. So, the ROU amortization journal entry is as follows:

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| Rent Expense | 64,725.97 |     |
| ROU Asset |     | 64,725.97 |

_To record amortization for the ROU asset in year one_

Journal entries 2 and 3 combined:
---------------------------------

Please note that journal entries 2 and 3 can be – and in practice usually are – combined to give the following entry:

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| Rent Expense | 114,638.79 |     |
| Lease Liability | 50,087.18 |     |
| Cash |     | 100,000.00 |
| ROU Asset |     | 64,725.97 |

_To record payment and ROU amortization for year one_

Journal entry 4:
----------------

Now, let us assume that at the end of year five, the lease is modified and extended by five years. Assume that the year six payment is now going to be $150,000 rather than $115,927.41 per the previous lease agreement. Also assume that the annual payments still increase by 3% each year. Finally, assume that the discount rate is now 7% rather than 6%. Based on these predicates, the amortization schedule for the modified lease is as follows:

![Modified Amortization Schedule](https://finquery.com/wp-content/uploads/2019/08/Modified_Ammortization_Schedule-min1.png)

At the end of year five under the old lease, the lease liability should be $516,738.59. After the modification, however, the new lease liability should be $1,188,078.97. The lease liability should then be credited by $671,340.38. The corresponding entry will be a debit to the ROU asset, as reflected below:

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| ROU Asset | 671,340.38 |     |
| Lease Liability |     | 671,340.38 |

_To record increase in lease liability and ROU asset due to lease modification_

Journal entry 5:
----------------

Please note that the entry above will be recorded at the time of the modification. When the payment is made at the end of year six, (once again, payments are made in arrears) the combined journal entry to reflect payment is as follows:

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| Rent Expense | 83,165.53 |     |
| Lease Liability | 66,834.47 |     |
| Cash |     | 150,000.00 |

_To record lease payment for year six_

Journal entry 6:
----------------

Like Journal Entry 3, the company needs to record amortization of the ROU Asset. Once again, it is amortized as the difference between straight-line rent expense and liability expense. The new straight-line rent expense (post modification) is $167,730.15 while the liability expense for year one is $83,165.53. So, the ROU amortization journal entry is as follows:

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| Rent Expense | 84,564.62 |     |
| ROU Asset |     | 84,564.62 |

_To record amortization for the ROU asset in year six_

There you have it – a comprehensive example showing how to modify an operating lease under ASC 842 when there is no additional ROU asset and the modified lease remains an operating lease. In a subsequent blog, we will give a comprehensive example showing the entries to make [when a modified operating lease results in a change in lease classification from operating to finance](https://finquery.com/blog/accounting-for-lease-modifications-asc-842-operating-to-finance/)
.

Related articles
----------------

[![Lease Modifications and Remeasurements under ASC 842](https://finquery.com/wp-content/uploads/2021/12/lease-modifications-remeasurements-blogfeat.jpg)](https://finquery.com/blog/lease-modifications-and-remeasurements-under-asc-842/)

### [Lease Modifications and Remeasurements under ASC 842](https://finquery.com/blog/lease-modifications-and-remeasurements-under-asc-842/)

[![Operating Lease Accounting under ASC 842 Explained with a Full Example](https://finquery.com/wp-content/uploads/2020/09/blogfeat-asc-842-operating-lease-accounting.jpg)](https://finquery.com/blog/operating-lease-accounting-asc-842-explained-example/)

### [Operating Lease Accounting under ASC 842 Explained with a Full Example](https://finquery.com/blog/operating-lease-accounting-asc-842-explained-example/)

[![Right-of-Use Asset (ROU Asset) and Lease Liability for ASC 842, IFRS 16, and GASB 87 Explained with an Example](https://finquery.com/wp-content/uploads/2021/08/rou-asset-lease-liability-asc-842-gasb-87-ifrs-16-blogfeat.jpg)](https://finquery.com/blog/right-of-use-asset-lease-liability-asc-842-ifrs-16-gasb-87/)

### [Right-of-Use Asset (ROU Asset) and Lease Liability for ASC 842, IFRS 16, and GASB 87 Explained with an Example](https://finquery.com/blog/right-of-use-asset-lease-liability-asc-842-ifrs-16-gasb-87/)

[![Lease Liability Amortization Schedule: How to Calculate It in Excel](https://finquery.com/wp-content/uploads/2019/11/lease-liability-amortization-schedule-excel.jpg)](https://finquery.com/blog/lease-liability-amortization-schedule-excel/)

### [Lease Liability Amortization Schedule: How to Calculate It in Excel](https://finquery.com/blog/lease-liability-amortization-schedule-excel/)

[![Free Lease Accounting Software](https://finquery.com/wp-content/uploads/2020/01/blog-sidebarwidget-guru-min.jpg)](https://leaseguru.com/)

![George Azih](https://finquery.com/wp-content/uploads/2025/01/george-azih-author.jpg)

About the author
----------------

George Azih, Founder

George Azih is the Founder of FinQuery. A leading expert on lease accounting, he holds a Bachelor's degree in Accounting from the Terry College of Business at the University of Georgia. He is a member of the American Institute of CPAs and the Georgia Society of CPAs. During his career, George served as a senior auditor at a CPA form and conducted accounting research and technical accounting for a Fortune 500 company. He founded LeaseQuery in 2011 to help companies of all sizes and across industries manage their leases efficiently under the new lease accounting standards.