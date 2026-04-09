---
type: concept
title: "Debits and credits"
aliases: ["Debit", "Credit", "Debit and credit"]
tags: ["accounting", "financial statements", "bookkeeping", "double-entry accounting"]
difficulty: beginner
prerequisites: ["[[The accounting equation]]", "[[Double-entry bookkeeping]]"]
related: ["[[The income statement]]", "[[The balance sheet]]", "[[The cash flow statement]]"]
sources: ["[[Wall Street Prep - Double Entry Bookkeeping - Debit vs. Credit System]]", "[[A Simple Model - Debit and Credit Review - A Simple Model]]", "[[CFI - Journal Entries Guide]]", "[[CFI - Double Entry - Overview, History, How It Works, Example]]"]
status: draft
updated: 2026-04-09
---

# Debits and credits

> **TL;DR.** Debits and credits are the fundamental language of double-entry accounting, where a debit represents an entry on the left side of a ledger, and a credit represents an entry on the right side.

## When you'd use this

You will use debits and credits constantly when building, interpreting, or analyzing financial statements. Any transaction recorded by a business—such as purchasing inventory, paying wages, issuing debt, or recognizing revenue—must be tracked using debits and credits. This system ensures that the fundamental accounting equation (Assets = Liabilities + Equity) always remains in balance. In financial modeling or investment banking, an intuitive grasp of how transactions flow through the three statements via debits and credits is essential for modeling scenarios, adjusting for non-recurring items, or understanding a company's cash position.

## The 30-second version

Every financial transaction has two sides. In double-entry accounting, this duality is recorded using debits (DR) and credits (CR).

A debit is simply an entry made on the left side of an account, while a credit is an entry on the right side. They do not inherently mean "good" or "bad", nor do they simply mean "increase" or "decrease." Their effect depends on the type of account.

Debits increase asset and expense accounts, but decrease liability, equity, and revenue accounts. Credits do the exact opposite: they decrease asset and expense accounts, but increase liability, equity, and revenue accounts. For every transaction, the total dollar amount of debits must always equal the total dollar amount of credits.

## The full explanation

### The Foundation: The Accounting Equation

To understand debits and credits, you must first understand the fundamental accounting equation:
**Assets = Liabilities + Shareholders' Equity**

This equation dictates that everything a company owns (Assets) must be financed by either borrowing money (Liabilities) or by the owners' invested capital and retained earnings (Equity). Because this equation must always balance, every transaction must affect at least two accounts. This is the core principle of double-entry bookkeeping.

### What are Debits and Credits?

In their simplest form, debits and credits are directional markers used in a general ledger or "T-account":
- **Debit (DR):** An entry on the **left side** of an account.
- **Credit (CR):** An entry on the **right side** of an account.

The most common misconception is that a debit is inherently positive and a credit is inherently negative, or vice versa. This is incorrect. Whether a debit or a credit increases or decreases an account balance depends entirely on the type of account being adjusted.

### The DEAD Rule

A helpful mnemonic device for remembering the normal balances of accounts is the **DEAD** rule:
- **D**ebit
- **E**xpenses
- **A**ssets
- **D**ividends

These account types (Expenses, Assets, Dividends) naturally carry a debit balance. Therefore, to increase them, you debit them. To decrease them, you credit them.

Conversely, the accounts on the opposite side of the accounting equation—Liabilities, Equity, and Revenue—naturally carry a credit balance. To increase them, you credit them. To decrease them, you debit them.

### Impact on the Five Main Account Types

1. **Asset Accounts:** (e.g., Cash, Accounts Receivable, Inventory, PP&E). Assets are on the left side of the accounting equation.
   - **Debit:** Increases an asset. (e.g., receiving cash).
   - **Credit:** Decreases an asset. (e.g., paying cash).

2. **Liability Accounts:** (e.g., Accounts Payable, Debt, Accrued Expenses). Liabilities are on the right side of the accounting equation.
   - **Debit:** Decreases a liability. (e.g., paying off a loan).
   - **Credit:** Increases a liability. (e.g., borrowing money).

3. **Equity Accounts:** (e.g., Common Stock, Retained Earnings). Equity is on the right side of the accounting equation.
   - **Debit:** Decreases equity. (e.g., paying a dividend).
   - **Credit:** Increases equity. (e.g., issuing new stock, generating net income).

4. **Revenue Accounts:** Revenue ultimately increases Retained Earnings (which is an Equity account). Therefore, revenue follows the same rules as equity.
   - **Debit:** Decreases revenue (rare, usually for returns or corrections).
   - **Credit:** Increases revenue. (e.g., making a sale).

5. **Expense Accounts:** Expenses ultimately decrease Retained Earnings. Because they reduce equity, they follow the opposite rules of equity accounts.
   - **Debit:** Increases an expense. (e.g., incurring a cost like rent or salaries).
   - **Credit:** Decreases an expense (rare, usually for corrections).

### The Golden Rule of Journal Entries

When recording a journal entry, the golden rule is absolute: **Total Debits must equal Total Credits**. If a transaction results in a $10,000 debit, there must be corresponding credits that sum to $10,000. If they do not balance, the accounting equation will break, and the balance sheet will not tie.

## Formula

(none)

## Worked example

[[Double-entry journal example]]

## Excel and modeling notes

- When building three-statement models, it is crucial to use consistent sign conventions. Typically, assets are modeled as positive numbers, and liabilities/equity are positive. However, when building the cash flow statement, an increase in an asset (a debit) is a *use* of cash (modeled as a negative number), while an increase in a liability (a credit) is a *source* of cash (modeled as a positive number).
- If your balance sheet does not tie in Excel, it usually means a journal entry was modeled with either an unbalanced debit and credit, or the signs were flipped (e.g., treating a debit to an asset as a source of cash instead of a use of cash).
- You can create a simple check in your model: `Total Assets - Total Liabilities - Total Equity`. This cell should always equal zero. If it doesn't, your debits and credits are out of balance.

## Interview-ready answer

[[Walk me through the journal entries for a credit sale]]

## Pitfalls and gotchas

- **Confusing banking terms with accounting terms:** In personal banking, when money is added to your account, the bank says they "credited" your account. This is because, from the *bank's* perspective, your deposit is a liability (they owe you the money), so they credit their liability account. However, on *your* company's books, cash is an asset. When you receive money, you *debit* cash. Do not let banking terminology confuse the corporate accounting rules.
- **Forgetting that expenses reduce equity:** It can be tricky to remember why expenses are debited to increase them. Remember that the ultimate goal of the income statement is to flow into the balance sheet via Retained Earnings (an equity account). Equity normally has a credit balance. Because expenses reduce equity, they must have the opposite sign: a debit balance.
- **Failing to balance a journal entry:** It is easy to record a debit and forget the offsetting credit, especially in complex transactions involving taxes, depreciation, or multi-part financing. Always verify that DR = CR before moving on.

## Sources

- [[Wall Street Prep - Double Entry Bookkeeping - Debit vs. Credit System]]
- [[A Simple Model - Debit and Credit Review - A Simple Model]]
- [[CFI - Journal Entries Guide]]
- [[CFI - Double Entry - Overview, History, How It Works, Example]]