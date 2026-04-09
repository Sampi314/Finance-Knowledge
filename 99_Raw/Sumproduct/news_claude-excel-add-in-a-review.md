# Claude Excel Add-in: A Review

**Source:** https://sumproduct.com/news/claude-excel-add-in-a-review/

---

[Home](https://sumproduct.com/)

\> Claude Excel Add-in: A Review

*   November 18, 2025

Claude Excel Add-in: A Review
=============================

Claude (by Anthropic) for Excel is available in Beta as a research preview through a waitlist for 1,000 Max, Team and Enterprise plan customers.  Anthropic has stated that they will continue to expand access as confidence is built in the product.

Claude for Excel is an add-in that integrates Claude into your Excel workflow.  It is designed for finance / accounting / banking professionals who work extensively with spreadsheets, particularly in the worlds of financial analysis and modelling.  So we thought we’d take a look!

Anthropic states that this tool works best for model analysis, assumption updates, error debugging, template population, formula explanations and multi-tab navigation.  It should be noted that it doesn’t have advanced Excel capabilities including PivotTables, conditional formatting, data validation, Data Tables and VBA, although these features are being developed.

According to the marketing website, Claude is trained to recognise common financial modelling patterns, formula structures and industry-standard calculations.  However, as with all AI tools, you should always verify the outputs match your specific methodologies.

Anthropic recommends Claude for Excel can:

*   ask questions about your workbook and get answers with cell-level citations
*   update assumptions while preserving formula dependencies
*   debug errors and identify their root causes
*   build new models or fill existing templates
*   navigate complex multi-tab workbooks seamlessly (something the **COPILOT** function cannot do presently).

So we had a play.  Our first prompt,

> _Build me a three-way integrated model using dynamic arrays_

might not be the most specific request ever uttered to an AI tool, but it did render the following after a few minutes:

![](https://sumproduct.com/wp-content/uploads/2025/11/image1-1.png)

We are not sure about the shading, but we did note that all the formulae were quite simple – and indeed, there were no dynamic arrays, since Anthropic acknowledges this feature is not yet supported.  Colour schemes aside, at least the Balance Sheet balanced and the model was reasonably transparent with short, succinct formulae throughout.  Unlike the **COPILOT** function, the formulae are displayed so results can be checked and verified quite easily.

So we thought we’d get more ambitious.  Next, we tried a large prompt in order to create a financial model.  This prompt began as follows:

![](https://sumproduct.com/wp-content/uploads/2025/11/image2.png)

The prompt took 11 pages in total to write, so almost bordered on a scoping document.  Claude went away to think about it – and sadly never came back.  After 24 hours or so of thinking, the file crashed.  Perhaps model consulting is safe from AI after all.

So we refined the premiss.  We wanted to assess whether AI embedded in Excel can build a robust, three-way integrated financial model that meets professional standards (even if no one fully agrees on them!).

We simplified the scope from our 11-page monster:

![](https://sumproduct.com/wp-content/uploads/2025/11/image3-682x1024.png)

Whilst the prompt was still reasonably long, the brief was simplified somewhat so that the intention was to build a monthly three‑statement model (Income Statement, Balance Sheet, Cash Flow Statement) with clean Inputs, calculations and outputs.  Furthermore, we detailed other requirements too:

*   **Control accounts:** each Balance Sheet line item, _e.g._ cash, receivables, inventory, prepayments, payables, accrued expenses, deferred revenue, PPE, debt, tax payable should be calculated via a control account (opening balance + increases – decreases = closing balance)

![](<Base64-Image-Removed>)

*   **No hard code:** all calculations derive from assumptions; no typed numbers should be contained within the calculation formulae
*   **Indirect Cash Flow Statement:** the Cash Flow Statement was to reconcile via movements with the Income Statement
*   **Integrity checks**: the Balance Sheet must always balance; the cash flow must reconcile opening to closing cash
*   **Inputs sheet:** must be created for revenue, COGS, operating expenses, capital expenditure, debt, tax and opening balances
*   **Control accounts sheet:** built to track each account’s opening balance, increases and decreases, _etc._

This time, Claude produced a model:

![](<Base64-Image-Removed>)

*   **Income Statement:** the monthly Income Statement linked back to the control accounts:

![](<Base64-Image-Removed>)

*   **Balance Sheet:** this was populated from control account closing balances, with a reconciliation line

![](<Base64-Image-Removed>)

*   **Cash Flow Statement:** this did use the indirect method; it started with net income (US terminology), it adjusted for working capital, capital expenditure and financing flows, and reconciled the cash changes:

![](<Base64-Image-Removed>)

*   **Dashboard:** Claude even added integrity checks and key metrics, plus model documentation

![](<Base64-Image-Removed>)

So perfect model then, yes?  Not quite.  During the build, we encountered and fixed several real‑world modelling problems:

1.  **Missing Tax Payable:**  the Balance Sheet did not balance originally and was out by $35,000, which was solved by adding a Tax Payable control account and linking it correctly.  Claude was forgetful!
2.  **Deferred Revenue placement:** misaligned rows broke formulae; we rebuilt the liabilities section and corrected references
3.  **Interest double counting:** the cash flow reconciliation did not reconcile by $2,500; this was fixed by separating interest and principal flows and updating the Cash Flow Statement for what was effectively a double count
4.  **Accounts Receivable:** there were problems with the collections logic, as the collections were not included due to misaligned columns; when challenged, Claude replaced the formula with a correct payment delay logic.

It was fair to say we went through a few iterations.  Once completed, the following were noted:

*   **Integrated:** all three statements link through control accounts; no hard‑typed numbers in calculation areas
*   **Balanced:** assets equal liabilities plus equity each month (albeit this is the US GAAP presentation method, but we will take it)
*   **Reconciled:** Indirect Cash Flow Statement tied exactly to the cash movement
*   **Auditable:** there was a clear separation of inputs, workings and outputs; control accounts provide traceable movements
*   **Documented:** notes were included, combined with dashboard checks and model notes to help reviewers understand the structure
*   **Volatile functions:** Claude seems to like volatile functions: **INDIRECT**, **COLUMN** and **ROW** functions were modelled which could break the structure should a row or column be included.

So what lessons did we learn?

![](<Base64-Image-Removed>)

Agent Mode is more useful to modellers than Copilot or the **COPILOT** function.  Claude in Excel takes it further – but still makes many mistakes and misunderstands what should be done.  But with iterations and perseverance, Claude is definitely on the right path.  Our key learning points were:

*   **AI accelerates the shell:** a well‑briefed AI can draft a control‑account model quickly
*   **Mechanics are fixable:** when checks / formulae failed, the AI can be set to trace and correct the root cause(s)
*   **Human judgment remains vital:** modelling treatments, scenario design and presentation still require human oversight
*   **Clear briefs matter:** specific instructions and Best Practice prompts about structure and standards will certainly improve AI output quality.

**_Word to the Wise_**

![](<Base64-Image-Removed>)

AI in Excel is not (yet) a replacement for experienced modellers, but it can help to automate repetitive setup and maintain structural integrity.  Claude uses the Excel engine to perform calculations which is where many large language models (LLMs) break down. 

We certainly felt we would have built the same model more quickly – currently.  However, if you use AI, remember, that is not the end of it.  The model is likely to contain errors, so you will need to check all formulae – and ironically, even draft a rebuilt model to check outputs.  Using AI to build models still takes longer than the tried and trusted “brute force and ignorance” manual methods.

Why not try it for yourself and see what you think?  Send your conclusions / non-confidential results to [contact@sumproduct.com](mailto:contact@sumproduct.com)
.

*   [Log in](https://sumproduct.com/news/claude-excel-add-in-a-review/#0)
    
*   [Register](https://sumproduct.com/news/claude-excel-add-in-a-review/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/claude-excel-add-in-a-review/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/claude-excel-add-in-a-review/#0)

[](https://sumproduct.com/news/claude-excel-add-in-a-review/#0 "close")

top