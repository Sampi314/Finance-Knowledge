# How to Calculate the Present Value of Lease Payments in Excel

**Source:** https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel

---

How to Calculate the Present Value (PV) of Future Lease Payments in Excel
=========================================================================

by [Rachel Reed, Team Lead, Technical Accounting Consultants](https://finquery.com/author/rachel-reed/ "Posts by Rachel Reed, Team Lead, Technical Accounting Consultants")
 | May 2, 2023

1\. [Present value of lease payments explained](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/#pv-lease-payments)

*   [PV (Present Value) vs. NPV (Net Present Value)](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/#pv-vs-npv)
    
*   [Minimum lease payments and future lease payments](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/#minimum-lease-payments)
    

2\. [How to calculate the present value of a payment stream using Excel in 5 steps](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/#excel-calculate)

*   [Step 1: Create your table with headers](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/#step-1)
    
*   [Step 2: Enter amounts in the Period and Cash columns](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/#step-2)
    
*   [Step 3: Insert the PV function](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/#step-3)
    
*   [Step 4: Enter the Rate, Nper Pmt, and Fv](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/#step-4)
    
*   [Step 5: Sum the Present Value column](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/#step-5)
    

3\. [Present value calculator](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/#pv-calculator)

4\. [Summary](https://finquery.com/blog/how-to-calculate-present-value-of-future-lease-payments-in-excel/#summary)

Present value of lease payments explained
-----------------------------------------

Present value, commonly referred to as PV, is the calculation of what a future sum of money or stream of cash flows is worth today given a specified rate of return over a specified period of time.

Under the [new lease accounting standards](https://finquery.com/blog/asc-842-summary-new-lease-accounting-standards/)
, [lessees](https://finquery.com/blog/lessee-vs-lessor-differences-accounting-and-more-explained/)
 are **required** to calculate the present value of any future lease payments to determine the obligation recorded on the balance sheet for both [operating leases](https://finquery.com/blog/operating-lease-accounting-asc-842-explained-example/)
 and [finance leases](https://finquery.com/blog/capital-lease-accounting-finance-lease-accounting-example/)
. This recognition provides more visibility of lease obligations to the users of the financial statements.

The calculation is performed using the terms and payments specified in the lease and a rate of return, or [interest rate](https://finquery.com/blog/interest-rates-asc-842-summary/)
, specific to either the lease or the organization. The present value of the lease payments is used to establish both a [lease liability and a right-of-use (ROU) asset](https://finquery.com/blog/right-of-use-asset-lease-liability-asc-842-ifrs-16-gasb-87/)
.

### PV (Present Value) vs. NPV (Net Present Value)

Accountants occasionally use the terms present value and net present value interchangeably, but they have distinct meanings. PV, or present value, is used to calculate today’s value of future payments or receipts, but **not combined** payments and receipts. In [lease accounting](https://finquery.com/blog/lease-accounting-explained/)
, we use present value to establish the assets or liabilities related to lease obligations or lease receivables.

Net present value, or NPV, is commonly used in [capital budgeting decisions](https://finquery.com/blog/capital-budgeting-decisions-finance-accounting-tools/)
 and other types of financial analyses as a way to determine the benefit of investing in a particular capital asset. In this usage, “net” means the calculation is using both inflows and outflows of cash. A potential investor may use this calculation to analyze the value of combined payments and receipts to understand what the cumulative profit or loss of an investment will be over time.

### Minimum lease payments and future lease payments

Under the new lease accounting standards, how we calculate the present value of lease payments has not changed. What has changed, however, is that under [ASC 842](https://finquery.com/blog/asc-842-summary-new-lease-accounting-standards/)
, [IFRS 16](https://finquery.com/blog/ifrs-16-leases-summary-examples-entries-disclosures/)
, and [GASB 87](https://finquery.com/blog/gasb-87-explained-example-new-lease-accounting/)
, the calculation of the present value of lease payments is required for all in-scope leases. Lessees reporting under IFRS 16 or GASB 87 will only have finance leases upon transition and will continue to discount the future lease payments for these types of leases to their present value. ASC 842, however, continues to [distinguish between operating and finance leases](https://finquery.com/blog/capital-finance-lease-vs-operating-lease-asc-842/)
 but requires obligations for both to be recorded on the balance sheet.

Therefore, under ASC 842, lease payments for both operating and finance leases will need to be discounted to their present value. Furthermore, the definition of lease payments under ASC 842 changed slightly from the definition of minimum lease payments under [ASC 840](https://finquery.com/blog/asc-840-vs-asc-842-old-lease-accounting-standard-vs-new/)
.

#### Minimum lease payments

Under the legacy lease accounting standard, ASC 840, the FASB required lessees to establish a lease liability and lease asset for all leases meeting the [criteria for a capital lease](https://finquery.com/blog/capital-finance-lease-vs-operating-lease-asc-842/)
. For leases classified as capital, lessees performed a calculation to determine the present value of the minimum lease payments which was used as the basis for the capital lease asset and liability values. Within ASC 840-10-25-6, the standard defines minimum lease payments as the financial obligations a lessee must make in connection with the leased asset.

#### Future lease payments

Under ASC 842, lessees are required to establish a lease liability and ROU asset for both operating and finance leases (previously capital leases). Lessees perform a present value calculation on future lease payments to determine the initial lease liability recorded on their balance sheet.

Future lease payments are defined in ASC 842-10-30-5 as payments that relate to the use of the underlying asset during the [lease term](https://finquery.com/blog/determining-correct-dates-lease-term-asc-842/)
. These payments include:

*   Fixed payments required by the lease agreement, such as [base rent](https://finquery.com/blog/prepaid-rent-other-rent-accounting-under-asc-842-explained/)
    
*   In-substance fixed payments required by the lease agreement. (In-substance fixed payments are payments that may appear to be variable, but are, in effect, fixed.)
*   Variable lease payments that depend on an index or rate, initially measured using the index or rate at the [lease commencement date](https://finquery.com/blog/lease-commencement-date-start-date-under-us-gaap-explained/)
    
*   The exercise price of a purchase option if the lessee is reasonably certain to exercise that option
*   Penalties for [terminating the lease](https://finquery.com/blog/lease-termination-accounting/)
     if the lease term reflects the lessee exercising the option to terminate the lease
*   Fees paid by the lessee to the owners of a special purpose entity for structuring the transaction
*   Amounts probable of being owed by the lessee as the result of a residual value guarantee

Future lease payments are reduced by incentives paid to or payable to the lessee and exclude amounts allocated to non-lease components, any guarantee of the lessor’s debt by the lessee, and variable lease payments, other than those specified above.

Read our article [Lease Payments: Establishing the Initial Lease Liability and ROU Asset under ASC 842](https://finquery.com/blog/lease-payments-establishing-initial-lease-liability-under-asc-842/)
 for more details on what is considered a lease payment and how to extract that information from your lease agreement.

How to calculate the present value of a payment stream using Excel in 5 steps
-----------------------------------------------------------------------------

As discussed above, under the new lease accounting standards, lease capitalization is required for the vast majority of leases. The capitalized amount is calculated as the present value of the lease payments. Therefore, to comply with the new lease standards, you will need to know how to calculate the present value of the lease payments. This is especially true if you are not using software and prefer to use Excel spreadsheets to manage your leases.

This article will address how to calculate the present value of the lease payments using Excel. While we believe [accounting for your leases in Excel](https://finquery.com/blog/lease-accounting-in-excel-will-set-you-up-for-non-compliance/)
 leaves too much room for error, if you prefer Excel, we can at least help you use it correctly. LeaseQuery also offers a free [Present Value Calculator](https://finquery.com/project/present-value-calculation-tool/)
 to perform this calculation for you.

**Get the free Present Value Calculator to follow along:**

[![Present Value Calculator](https://finquery.com/wp-content/uploads/2019/11/PresentValueCalculator.jpg)](https://finquery.com/project/present-value-calculation-tool/)

### Step 1: Create your table with headers

In an Excel spreadsheet, title three columns with the following headers: Period, Cash, and Present Value, as shown below:

![Excel table with period, cash, and present value](https://finquery.com/wp-content/uploads/2023/05/period-cash-present-value.png)

### Step 2: Enter amounts in the Period and Cash columns

Enter the number of payment periods in the Period column. The period represents the length of time over which interest is accrued, typically a month, quarter, or year. In this example, we are calculating the present value of **ten years/periods** of payments due at the **beginning of the period**, so the periods are numbered 0 to 9. Note, if payments were made in arrears, the numbering would be 1 to 10.

Next, enter the cash payment amount for each period in the Cash column. Let’s assume this lease is written as annual payments of $1,000, due at the beginning of the year, increasing 5% annually. See the below illustration:

![Excel table with period and cash in columns](https://finquery.com/wp-content/uploads/2023/05/period-and-cash.png)

### Step 3: Insert the PV function

In the first row of the Present Value column, click on the “insert function” button. From the dialogue box that pops up, select “financial” in the dropdown, then scroll down and select “PV”.

![Inserting the PV function in Excel](https://finquery.com/wp-content/uploads/2023/05/pv-function-excel.png)

### Step 4: Enter the Rate, Nper Pmt, and Fv

After you click OK, another dialogue box will pop up into which you will insert the function arguments needed for Excel to perform the calculation. Enter **6%** as the [discount rate](https://finquery.com/blog/interest-rates-asc-842-summary/)
 we are using in this example. In the Nper field, enter the cell reference for the first period. Enter 0 for Pmt, and in the field for Fv enter the cell reference for the first cash payment amount. Select type as 0 (though it doesn’t matter if you select 0 or 1 here because we are discounting via the period column). Once the formula dialogue box is completed, click OK for the formula to populate the first row in the Present Value column. Copy the formula down the column to the last period listed.

![Rate, Npr, Pmt, and Fv fields in Excel](https://finquery.com/wp-content/uploads/2023/05/rate-npr-pmt-fv-excel.png)

### Step 5: Sum the Present Value column

Once you have calculated the present value of each periodic payment separately, sum the values in the Present Value column. This sum equals the present value of 10 annual payments of $1,000 with 5% escalations and an interest rate of 6%, or **$9,586.**

![Sum of the present value column in Excel](https://finquery.com/wp-content/uploads/2023/05/sum-present-value-column.png)

This example shows one way to calculate the present value of lease payments using Excel.

Present value calculator
------------------------

If this seems like too many steps, we have created a [free, downloadable present value calculator in Excel](https://finquery.com/project/present-value-calculation-tool/)
 that performs this calculation for you. To use the tool, populate the items in dark blue at the top of the template and select values for the drop-down records:

1.  Enter the number of periods
2.  Enter the discount rate
3.  Enter the payments
4.  Indicate whether the periods are monthly, quarterly, or annual
5.  Specify if the payments are made at the beginning of the period or the end of the period

The tool will then calculate the present value for you automatically. (See the image of the template below with inputs from this example).

![Present Value Calculator](https://finquery.com/wp-content/uploads/2023/05/present-value-calculator.png)

If you are using Excel to calculate both the present value of lease payments and the [lease liability amortization schedule, read our additional blog](https://finquery.com/blog/lease-liability-amortization-schedule-excel/)
 that illustrates how to calculate the present value of lease payments and generate the lease amortization schedule in one step with Excel. With this method, you will have the basic calculations needed to comply with the new lease accounting standards.

Summary
-------

Knowing how to calculate the present value of lease payments is necessary to comply with the new lease accounting rules. This calculation is required to record lease liabilities and the related asset balances on the balance sheet, and all entities required to comply with any of the new lease accounting standards need to accurately perform the calculation of the present value of the future lease payments.

[![ASC 842 Lease Accounting Guide](https://finquery.com/wp-content/uploads/2022/10/ultimate-lease-accounting-guide-asc-842-banner.jpg)](https://finquery.com/download-the-ultimate-lease-accounting-guide/)

Related articles
----------------

[![Lease Liability Amortization Schedule: How to Calculate It in Excel](https://finquery.com/wp-content/uploads/2019/11/lease-liability-amortization-schedule-excel.jpg)](https://finquery.com/blog/lease-liability-amortization-schedule-excel/)

### [Lease Liability Amortization Schedule: How to Calculate It in Excel](https://finquery.com/blog/lease-liability-amortization-schedule-excel/)

[![Lease Payments: Establishing the Initial Lease Liability & ROU Asset under ASC 842](https://finquery.com/wp-content/uploads/2022/05/lease-payments-establish-initial-lease-liability-asc-842-blogfeat.jpg)](https://finquery.com/blog/lease-payments-establishing-initial-lease-liability-under-asc-842/)

### [Lease Payments: Establishing the Initial Lease Liability & ROU Asset under ASC 842](https://finquery.com/blog/lease-payments-establishing-initial-lease-liability-under-asc-842/)

[![Interest Rates under ASC 842 Explained: Implicit, Incremental Borrowing, Risk-Free](https://finquery.com/wp-content/uploads/2021/10/asc-842-interest-rates-blogfeat.jpg)](https://finquery.com/blog/interest-rates-asc-842-summary/)

### [Interest Rates under ASC 842 Explained: Implicit, Incremental Borrowing, Risk-Free](https://finquery.com/blog/interest-rates-asc-842-summary/)

[![Determining the Correct Dates & Lease Term from a Lease Agreement under ASC 842](https://finquery.com/wp-content/uploads/2022/04/determine-date-lease-term-asc-842-blogfeat.jpg)](https://finquery.com/blog/determining-correct-dates-lease-term-asc-842/)

### [Determining the Correct Dates & Lease Term from a Lease Agreement under ASC 842](https://finquery.com/blog/determining-correct-dates-lease-term-asc-842/)

[![Present Value Calculator](https://finquery.com/wp-content/uploads/2020/12/present-value-calculator-blog-sidebarwidget.jpg)](https://finquery.com/project/present-value-calculation-tool/)

![Rachel Reed](https://finquery.com/wp-content/uploads/2025/01/rachel-reed-author.jpg)

About the author
----------------

Rachel Reed, Team Lead, Technical Accounting Consultants

Rachel Reed holds both Bachelor's and Master's degrees in Accounting from the University of Mississippi. She began her career in Accounting as an Assurance Intern at Ernst & Young (EY), where she eventually progressed into a role working in the audit practice. With her background in accounting and financial services, she currently serves as a Technical Accounting Manager and Team Lead of Technical Accounting Consultants.