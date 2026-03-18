# Direct vs indirect cash flow

**Source:** https://www.financialmodellinghandbook.org/direct-vs-indirect-cashflow

---

Accountants and modellers like to give things fancy names and make them appear more complicated than they are.

You might hear people talking about direct vs indirect cashflows.

What we have in the model so far is a direct cash flow; we put the cash receipts and cash payments directly onto the cash flow statement.

With an indirect cash flow, we are going to start from profit, EBITDA to be exact, and then show the movement in working capital on the cash flow statement.

Let’s see what that looks like:

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/11/1.jpg)

This is where we are starting. We have cash received from invoices and cash paid for operating costs on our cash flow statement. The Accounts Receivable and Accounts Payable balances track the differences between what’s going through the income statement and these lines on our cash flow statement.

With an indirect cash flow, we are going to start by linking to EBITDA on the income statement and then adding a line that shows the movement in working capital. I’ve started with a placeholder on the cash flow statement:

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/11/2.jpg)

To do that, we are going to look at the increase and decrease in Accounts Receivable and Accounts Payable balances.

The key to getting this right is to think about what those movements mean for cash.

An increase in Accounts Receivable means that we have more customer invoices which have not been paid. This is going to be negative for cash.

An increase in Accounts Payable means that the business has more invoices that it has not paid. This is going to be positive for cash.

Let’s start with Accounts Receivable.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/11/3.jpg)

I’ve created a block which looks at the beginning and closing balances of Accounts Receivable. My formula to get the movement is beginning balance minus closing balance. That way, an increase in the balance will result in a negative cash flow. I’m using inflow/outflow convention for this line, and so I have indicated what the movements mean in the label

We’ll do the opposite for Accounts Payable.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/4.jpg)

  
Here our formula is closing balance minus the beginning balance. That way, an increase is positive for cash.

To get the net movement in working capital, we add those two cash movements together.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/5.jpg)

In all of these blocks, the row total for the calculation should be zero since these differences should all unwind over time.

We then link the Net movement in working capital line to the cash flow statement. Bingo, our balance sheet balances again, and all is good in the world.

![](https://www.financialmodellinghandbook.org/content/images/2022/11/6.jpg)

  
Indirect cash flow nailed.

The solution for this bonus chapter is available in the file pack you'll receive when you [purchase the handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
. See file _4.55 FMH direct END 01a._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero-5.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/direct-vs-indirect-cashflow#/portal/signup)