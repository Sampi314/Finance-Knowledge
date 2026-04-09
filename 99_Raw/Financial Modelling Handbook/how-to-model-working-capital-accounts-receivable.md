# How to model Accounts Receivable

**Source:** https://www.financialmodellinghandbook.org/how-to-model-working-capital-accounts-receivable

---

Working capital has an enormous impact on the cash flow of any business. You must look carefully at the operating reality of the company you are modelling to understand the working capital dynamics.

What is Accounts Receivable?
----------------------------

Accounts receivable is a balance. It is the value of invoices that have been issued to customers but not yet paid.

Issuing invoices increases Accounts Receivable.
-----------------------------------------------

When an invoice is issued, the company records the amount of the invoice in its accounts as Revenue.

Think back to how we connected up our financial statements. If you don't change anything else, increasing revenue increases retained earnings.

Retained earnings appears on the liability side of the balance sheet. If you increase the liability side of the balance sheet and nothing else, the balance sheet will no longer balance. This situation is what we saw at the end of the last chapter.

When an invoice is issued, we record it as an Account Receivable, an invoice issued but not yet paid. This is money due to the business and is recorded as an asset.

The impact on the model is, therefore:

*   Increase in Revenue (increase in retained earnings - increased liability)
*   Increase in Accounts Receivable (increased asset)

Since both the liability and the asset side of our balance sheet increase by the same amount, our balance sheet continues to balance.

Customers paying invoices decreases Accounts Receivable
-------------------------------------------------------

When the customer pays its invoice, the company records this as an increase in cash and a decrease in the Accounts Receivable. The impact on our model is, therefore:

*   Increase in cash (asset)
*   Decrease in accounts receivable (asset)

These are both asset accounts. Therefore the changes cancel each other out, and the balance sheet continues to balance.

Forecasting Cashflow & Accounts Receivable
------------------------------------------

Let's look at a couple of examples.

Assuming a quarterly model, our model looks like this:

![](https://www.financialmodellinghandbook.org/content/images/public/images/78d9e3b9-cc60-4346-88a5-efc7db301e02_2042x822.jpeg)

Example 1: Continuous invoicing
-------------------------------

Let's imagine this business has lots of customers and is issuing invoices every day. On average, it takes 30 days for each customer to pay its invoice. The company wants to forecast its cash flow and accounts receivable.

For the first couple of months, all invoices issued get paid within the same quarter:

![](https://www.financialmodellinghandbook.org/content/images/public/images/75bc1641-624d-4344-a90f-90c7a05a07d5_2072x864.jpeg)

The company will not receive payment within the quarter for any invoices it issues less than 30 days before the end of the quarter. Customers won't pay those invoices until the next quarter. They will appear as Revenue for the current quarter but not in cash flow.

![](https://www.financialmodellinghandbook.org/content/images/public/images/e3251c0c-7abb-4e95-812f-d09720816dc2_2056x882.jpeg)

When it comes to forecasting Cash Received and the Accounts Receivable balance, we can see that these will look like this:

![](https://www.financialmodellinghandbook.org/content/images/public/images/61afea6e-87b3-4c82-8dae-8e5df89f2923_2060x866.jpeg)

In the first period:

Accounts receivable balance = Revenue / Days in Period \* 30

Cash received = Revenue less Accounts Receivable balance.

In the second period:

Cash received = Revenue less Accounts Receivable (Period 2) plus Accounts Receivable (Period 1).

Example 2: Monthly invoicing
----------------------------

Our solar acquisition case study is a little different from this. There is only one customer. Invoices will be issued monthly, not continuously. Invoices will be issued within 15 days of the end of each month and paid within 30 days of being issued.

Our business looks like this:

![](https://www.financialmodellinghandbook.org/content/images/public/images/16669fc4-8624-455d-88e4-a1711518a1a3_2108x852.jpeg)

Our business issues its monthly invoice 15 days after month-end. It then takes 30 days for the customer to pay. Therefore, our company doesn't receive its month one Revenue until month three.

The invoices for months two and three are not paid in the same quarter. They are paid the following quarter.

![](https://www.financialmodellinghandbook.org/content/images/public/images/a821684e-6606-41d9-8dd3-582b18e2e6d1_2064x836.jpeg)

Therefore at the end of the quarter, the cash received is only that for the first month.

The invoices issued for months 2 and 3 will be sitting in Accounts Receivable at the end of the quarter.

![](https://www.financialmodellinghandbook.org/content/images/public/images/7abd9baf-75be-4cac-a985-4c1cd7a1ddcc_2092x878.jpeg)

From the information in the case, it appears that we have 45 days of Receivables. However, to forecast cash flow and accounts receivable, an assumption of 60 days is more appropriate.

In the next chapter, we'll look at the steps to model this.

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--171.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

Comments
--------

Sign in or become a Financial Modelling Handbook member to join the conversation.  
Just enter your email below to get a log in link.

 Send a log in link Great! Please check your inbox (or spam folder) for a log in link. Something didn't work. Please try again.

Sorry, comments couldn't be loaded. It looks like this account is not currently active.

### Subscribe to Financial Modelling Handbook

Don’t miss out on the latest financial modelling guides. Sign up now to get access to the library of members-only guides.

[jamie@example.com\
\
Subscribe](https://www.financialmodellinghandbook.org/how-to-model-working-capital-accounts-receivable#/portal/signup)