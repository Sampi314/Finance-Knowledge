# Accounting for Lease Modifications under ASC 842, Part 2

**Source:** https://finquery.com/blog/accounting-for-lease-modifications-asc-842-operating-to-finance

---

Accounting for Lease Modifications under ASC 842, Part 2: Operating to Finance
==============================================================================

by [Abdi Ali, Senior Technical Accounting Consultant](https://finquery.com/author/abdi-alileasequery-com/ "Posts by Abdi Ali, Senior Technical Accounting Consultant")
 | Oct 2, 2019

This is the second blog in our series on lease modifications and addresses a modification where the lease classification changes as a result of the modification.

In this blog, we will give a comprehensive example [under ASC 842](https://finquery.com/blog/asc-842-summary-new-lease-accounting-standards/)
 illustrating how to account for a lease modification that _does not expand or add additional assets_ to the original lease, but rather increases the [lease term](https://finquery.com/blog/determining-correct-dates-lease-term-asc-842/)
, changes the payment amounts, as well as changes in [classification from an operating lease to a finance lease](https://finquery.com/blog/capital-finance-lease-vs-operating-lease-asc-842/)
.

As covered in the [previous lease modifications blog](https://finquery.com/blog/lease-modification-accounting-asc-842-operating-lease-to-operating-lease/)
, per ASC 842-10-25-1, at modification, because there isn’t an additional [ROU asset](https://finquery.com/blog/right-of-use-asset-lease-liability-asc-842-ifrs-16-gasb-87/)
 granted, the [lessee](https://finquery.com/blog/lessee-vs-lessor-differences-accounting-and-more-explained/)
 would use the updated lease payments and an updated [discount rate](https://finquery.com/blog/discount-rate-implicit-in-the-lease-asc-842/)
 to remeasure the lease liability and would recognize any difference between the new lease liability and the old lease liability as an adjustment to the ROU asset. Additionally, the lessee is required to re-evaluate lease classification if there is a change to the lease term as a result of the modification.

This blog uses the same financial inputs for the original lease as our first modification blog, however, we will add a wrinkle where due to the modification of the lease, its initial classification is reassessed to be a [finance lease](https://finquery.com/blog/capital-lease-accounting-finance-lease-accounting-example/)
 as of the effective date of the modification.

Accounting for lease modifications under ASC 842: Operating to finance example
------------------------------------------------------------------------------

Assume a 10-year lease for equipment with annual payments in arrears of $100,000 increasing by 3% each year. Assume the discount rate is 6%, and for purposes of this illustration, assume this is an operating lease to begin with. The initial amortization schedule for this lease is as follows:

![Initial Amortization Schedule](https://finquery.com/wp-content/uploads/2019/09/Initial-Amortization-Schedule.png)

[Click here to learn how to create the schedule above using Excel](https://finquery.com/blog/lease-liability-amortization-schedule-excel/)
 and download our free present value calculator:

[![Present Value Calculator](https://finquery.com/wp-content/uploads/2019/11/PresentValueCalculator.jpg)](https://finquery.com/project/present-value-calculation-tool/)

### Journal Entry 1: To record the lease liability and corresponding ROU asset at lease commencement

Based on the amortization schedule above, the initial journal entry to make is as follows:

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| ROU Asset | 831,880.38 |     |
| Operating Lease Liability |     | 831,880.38 |

  

### Journal Entry 2: To record Year 1 rent payment of 100,000

Please note that the journal entry above is made at the beginning of year 1. At the end of year 1 when payment is made (recall that payments are made in arrears in this example), the journal entry to reflect the payment is as follows:

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| Rent Expense | 49,912.82 |     |
| Lease Liability | 50,087.18 |     |
| Cash |     | 100,000.00 |

  

### Journal Entry 3: To record amortization for the ROU asset in Yr. 1

In addition to the entry above, the ROU asset has to be amortized. It is amortized as the difference between [Straight Line Rent Expense](https://finquery.com/blog/rent-expense-explained-example-straight-line-rent/)
 and the Liability Expense. Straight-Line Rent Expense is 114,638.79 while the Liability Expense for Year 1 is $49,912.82. So, the ROU amortization journal entry is as follows:

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| Rent Expense | 64,725.97 |     |
| ROU Asset |     | 64,725.97 |

  

### Journal Entries 2 and 3 combined:

Please note that Journal entries 2 and 3 can be (and in practice usually are) combined to give the following entry:

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| Rent Expense | 114,638.79 |     |
| Lease Liability | 50,087.18 |     |
| Cash |     | 100,000.00 |
| ROU Asset |     | 64,725.97 |

  

### Journal Entry 4: To record increase in lease liability and ROU asset due to lease modification

Now, let us assume that at the end of year 5, the equipment lease is modified and extended by 5 years. Assume the year 6 payment is now going to be $150,000 rather than $115,927.41 per the previous lease agreement. Also assume that the annual payments still increase by 3% each year. Finally, assume that the discount rate is now 7% rather than 6%.

The equipment has a 12-year remaining economic life at modification. In comparison to the remaining lease term of 10 years, this lease represents a “major part” of the remaining economic life of the asset and therefore, the lease will now be classified as a Finance Lease rather than an Operating Lease upon modification date. Based on these predicates, the amortization schedule for the modified lease is as follows:

![Modified Amortization Schedule](https://finquery.com/wp-content/uploads/2019/09/Modified-Amortization-Schedule.png)

At the end of year 5 under the original lease, the lease liability should be 516,738.59. After the modification, however, the new lease liability should be 1,188,078.97.

Since the lease is changing in classification from Operating to Finance, the accounts we are booking the entries to will also reflect that change. First, we must remove the remaining operating lease liability under the original lease by debiting the pre-modification balance at the end of year 5 of $ 516,738 and record the finance lease liability under the modified lease via a credit of $1,188,078.97. This entry recognizes the increase in the liability combined with the change in lease classification as a result of the modification. The net difference is the increase in the liability of $671,340.39 due to the modification.

[To calculate the ROU asset](https://finquery.com/blog/right-of-use-asset-lease-liability-asc-842-ifrs-16-gasb-87/)
, the modification amount of $671,340.39 is added to the ROU Asset balance at the end of year 5 pre-modification of $474,458.20. As a result, a debit should then be booked for $1,145,798.59 to a new ROU Asset account for the Finance lease, and a credit to remove the existing ROU Operating Asset.

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| Lease Liability (Operating) | 516,738.59 |     |
| ROU Asset (Finance) | 1,145,798.59 |     |
| Lease Liability (Finance) |     | 1,188,078.97 |
| ROU Asset (Operating) |     | 474,458.20 |

  

### Journal Entry 5: To record lease payment for year 6

Please note that the entry above will be recorded at the time of the modification (in this case, at the end of Year 5).

At the end of Year 6 (when the payment is made), combined Journal Entry to reflect Payment is as follows:

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| Rent Expense | 83,165.53 |     |
| Lease Liability | 66,834.47 |     |
| Cash |     | 150,000.00 |

  

### Journal Entry 6: To record depreciation for the ROU asset in year 6

Since this is now a finance lease, the company now needs to depreciate the ROU Asset over the remaining lease term. The monthly depreciation is computed as the straight-line of the Beginning ROU Asset balance post-modification over the remainder of the lease term (1,145,798.59/10 years). The New [Straight-Line Depreciation Expense](https://finquery.com/blog/straight-line-method-depreciation-explained-example/)
 (post modification) is 114,579.86.

| Account | Debit (DR) | Credit (CR) |
| --- | --- | --- |
| Depreciation Expense | 114,579.86 |     |
| Accumulated Depreciation |     | 114,579.86 |

  

This blog presents a comprehensive example under ASC 842 illustrating how to modify an operating lease when there is no additional ROU asset and the modified lease changes to a Finance Lease as a result of the modification.

Related articles
----------------

[![Operating Lease Accounting under ASC 842 Explained with a Full Example](https://finquery.com/wp-content/uploads/2020/09/blogfeat-asc-842-operating-lease-accounting.jpg)](https://finquery.com/blog/operating-lease-accounting-asc-842-explained-example/)

### [Operating Lease Accounting under ASC 842 Explained with a Full Example](https://finquery.com/blog/operating-lease-accounting-asc-842-explained-example/)

[![Lease Modification Accounting under ASC 842: Operating Lease to Operating Lease](https://finquery.com/wp-content/uploads/2019/08/lease-modifications-under-asc-842-operating-lease-to-operating-lease-blogfeat.jpg)](https://finquery.com/blog/lease-modification-accounting-asc-842-operating-lease-to-operating-lease/)

### [Lease Modification Accounting under ASC 842: Operating Lease to Operating Lease](https://finquery.com/blog/lease-modification-accounting-asc-842-operating-lease-to-operating-lease/)

[![Capital/Finance Lease vs. Operating Lease Explained: Differences, Accounting, & More](https://finquery.com/wp-content/uploads/2022/12/capital-finance-vs-operating-lease-explained-blogfeat.jpg)](https://finquery.com/blog/capital-finance-lease-vs-operating-lease-asc-842/)

### [Capital/Finance Lease vs. Operating Lease Explained: Differences, Accounting, & More](https://finquery.com/blog/capital-finance-lease-vs-operating-lease-asc-842/)

[![Right-of-Use Asset (ROU Asset) and Lease Liability for ASC 842, IFRS 16, and GASB 87 Explained with an Example](https://finquery.com/wp-content/uploads/2021/08/rou-asset-lease-liability-asc-842-gasb-87-ifrs-16-blogfeat.jpg)](https://finquery.com/blog/right-of-use-asset-lease-liability-asc-842-ifrs-16-gasb-87/)

### [Right-of-Use Asset (ROU Asset) and Lease Liability for ASC 842, IFRS 16, and GASB 87 Explained with an Example](https://finquery.com/blog/right-of-use-asset-lease-liability-asc-842-ifrs-16-gasb-87/)

[![Ultimate Lease Accounting Guide](https://finquery.com/wp-content/uploads/2022/10/ultimate-lease-accounting-guide-sidebarwidget.jpg)](https://finquery.com/download-the-ultimate-lease-accounting-guide/)

![Abdi Ali](https://finquery.com/wp-content/uploads/2025/01/abdi-ali-author.jpg)

About the author
----------------

Abdi Ali, Senior Technical Accounting Consultant

Abi-Khadar Ali is a Senior Technical Accounting Consultant at FinQuery and holds both Bachelor's and Master's degrees in Accounting from Georgia State University. With prior experience as an Accounting Associate, he brings a wealth of expertise to his current role. His commitment to excellence and strategic mindset drive efficiency and accuracy in financial reporting.