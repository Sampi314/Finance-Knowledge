# How to find a balance sheet error

**Source:** https://www.financialmodellinghandbook.org/how-to-find-a-balance-sheet-error

---

Earlier in the book, I recommended that one of the first things we should do when starting a model is put our retained cash and retained earnings balance in place and link them to the appropriate lines from our cash flow and income statement. Doing this means we have a balancing balance sheet right from the start of the process. When we add new line items, if the balance sheet stops balancing, we know it's down to the lines we just added. We can then fix any internal accounting issues within the group we just added to correct the problem.

If we find a balance sheet that doesn't balance, we can use this concept of groups of line items to diagnose the problem.

An example of a group of line items is Revenue (income statement), cash received from invoices (cash flow), and Accounts receivable (balance sheet). As long as the Accounts Receivable balance correctly tracks the timing difference between Revenue and Cash received from invoices, the "internal accounting" within this group of line items is consistent and won't cause a balance sheet problem.

To diagnose a balance sheet problem, we can remove line items from the financial statements in groups until the balance sheet mismatch disappears. This allows us to isolate the "group" causing the problem. We still have to investigate the modelling of this group to find the cause of the problem, but it narrows down the search considerably.

The two kinds of balance sheet error
------------------------------------

There are two different types of balance sheet errors. Knowing the difference will also help you isolate the source of the problem.

### Type 1: A constant/unchanging balance sheet difference.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/04/1-2.jpg)

You can see from the balance sheet difference that the error starts at the transaction date, and the quantum of the error doesn't change. This indicates that the problem lies with the opening balance sheet. In this example, it's pretty easy to see the cause - there is $100m of asset on the opening balance sheet but only $23m of financing. The senior debt balance is missing entirely. Fixing this type of error requires you to look at the opening balance sheet and find the source of the problem there.

### Type 2: A balance error that changes over time.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/04/2-1.jpg)

In the above example, we have added back the senior debt balance. The opening balance sheet now balances. Now there is a balance sheet difference that changes over time. This tells us that there is an issue with the line items going through the income statement or cash flow. In this case, the senior debt repayment is missing from the cash flow. And so the senior debt balance is reduced by the amount of the debt repayment, but the cash is not, causing our balance sheet problem.

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

* * *

How to find a balance sheet error
---------------------------------

Before you do anything, carefully inspect the financial statements checking two things:

1.  Are the correct line items connected to the financial statements? You can tell this by looking at the labels. (Assuming you have been consistent in your linking and all the links start on the row label column and are copied across correctly).
2.  Are the intermediate totals on the cash flow statement correct? I've had countless students stare at their balance sheets for hours trying to find the problem, only to discover that the total on the financial statements wasn't adding up correctly. It's easy to introduce this error when you add a new item to the financial statements but don't update the totals to ensure it's included. See the example below; the tax line has not been included in the sum range. This is a common error.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/04/3-1.jpg)

If you completed both of these steps and have not found the error, it's time to unleash the big dogs; removing line items from our financial statements.

### Remove line items in groups.

In our first worked example model, the balance sheet difference looks like this:

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/04/4-2.jpg)

We can see that it's a Type 2 error - it changes over time. It's therefore related to a mismatch of forecast period line items and isn't related to our opening balance sheet.

We start by systematically removing line items by group. We will begin with line items related to revenue. We will remove the Revenue, Cash received from invoices, and Accounts receivable line items.

When removing line items, start from column J, select all the time series data and press delete.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/04/5-2.jpg)

We leave all the linked data before the time series in columns E to I. This allows us to easily add back the line item when we're done.

Mark the removed cells with Yellow to be sure not to forget you've done this.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/04/6-2.jpg)

We now do the same with cash received from invoices:

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/04/7-2.jpg)

And the Accounts Receivable balance:

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/04/8-1.jpg)

We then fully recalculate the model while looking at the balance sheet difference. (It helps to be in manual calculation mode for this to see the changes happening when we recalculate).

In this example, the balance sheet difference has not changed. The balance sheet problem is not related to the group we have just removed.

### Reinstate the line items.

For each line you removed, go to column I in that line and hit Ctrl+Shift+a and copy the link back over the timeline. We made this easy by not deleting the entire line, just J onwards.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/04/10.jpg)

### Move to the next group and start the process again.

We now move to Operating costs and remove the lines from the income statement, cash flow and balance sheet.

After we remove Accounts Payable from the balance sheet and recalculate, the balance sheet difference goes to zero. Therefore, we can be sure that this group of line items is causing the balance sheet problem.

When we reinstate the links, we can see that the cause is that the O&M expense (income statement line items) is on both the income statement and the cash flow. The cash paid line should be on the cash flow. When we correct this error, we have solved the problem.

![](https://www.financialmodellinghandbook.org/content/images/size/w2400/2022/04/11.jpg)

### Download the practice file.

_To obtain the worked example file to accompany this chapter [buy the financial modelling handbook](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)
._

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--59.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

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
Subscribe](https://www.financialmodellinghandbook.org/how-to-find-a-balance-sheet-error#/portal/signup)