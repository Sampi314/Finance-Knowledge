# AI Blog: Building a Financial Model with AI: What Really Happens When You Let Claude Do the Work

**Source:** https://sumproduct.com/blog/ai-blog-building-a-financial-model-with-ai-what-really-happens-when-you-let-claude-do-the-work/

---

[Home](https://sumproduct.com/)

\> AI Blog: Building a Financial Model with AI: What Really Happens When You Let Claude Do the Work

*   February 6, 2026

AI Blog: Building a Financial Model with AI: What Really Happens When You Let Claude Do the Work
================================================================================================

_Welcome back. Over the past year, there has been growing excitement about artificial intelligence (AI) generated financial models. The premiss is attractive: describe a business, ask an AI tool to build a model from scratch and receive a complete three-statement forecast within a brief time._

However, in practice, financial modelling is not about producing a spreadsheet quickly.  It is about logic, structure, auditability and trust.  Indeed, some now hold the tenants of import to be refreshability _(sic)_, auditability and verifiability.  A model must be something an investor, lender or board can rely upon, not just something that balances.

To test how far AI can really go, we ran a controlled experiment.  We asked Claude to build a financial model for an imaginary brewery using a carefully engineered prompt and then reviewed the result as if it had been prepared by an experienced modelling analyst.

In this article, we explain how the model was generated, why the prompt mattered so much and what a detailed audit of the AI-built model revealed.

![](<Base64-Image-Removed>)

**_**_Starting with the Prompt, Not the Model_**_**

Rather than asking something vague such as “build me a brewery model”, we started by designing a highly detailed prompt.  In fact, we used ChatGPT first to help us draft that prompt before giving it to Claude.

The final prompt ran to 11 pages and opened with a very deliberate instruction:

_“You are an expert FMCG CFO and financial modeller with deep experience in beer manufacturing and distribution…”_

This wording was not cosmetic.  It was designed to force the AI to reason like a specialist rather than as a generalist.  Instead of behaving like a generic chatbot, the model was asked to adopt the mindset of someone who understands hectolitres, excise duty, packaging lines and capacity constraints.

The objective was framed just as carefully.  We did not ask for “a model”.  We asked for a consistent, robust and auditable three-statement model.  In financial modelling, those words matter: “robust and auditable” implies transparency and traceability, not just arithmetic consistency.  “Three-statement” signals a fully integrated Income Statement, Balance Sheet and Cash Flow Statement, rather than a ‘loose’ profit forecast.

Even the business language was chosen to anchor the AI in industry reality.  Volumes were described in hectolitres, not units.  Sales channels were defined as on-trade and off-trade, not simply retail and wholesale.  Costs were framed using ‘Bills of Materials’, which is standard in cost accounting.

Finally, the prompt explicitly instructed the AI to reason in a clear, structured and step-by-step way.  This served two purposes.  First, it made the output more readable.  Second, it made the logic easier to audit later, because we could see how each part of the model was constructed.

![](<Base64-Image-Removed>)

**_**_Asking the Right Questions Before Building Anything_**_**

A critical part of the prompt was that Claude was not allowed to start modelling immediately.  It first had to ask up to 15 clarification questions.

These questions covered areas any experienced modeller would care about.  This included:

*   the number of products and SKUs
*   the mix of bottles, cans and kegs
*   the split between on-trade and off-trade volumes
*   how excise duty should be calculated
*   whether capacity expands over time
*   how working capital should be treated
*   who the model was ultimately for (particularly important).

This mirrors real-world modelling “best practice”.  Building a model without understanding scope is like designing a building without knowing how many floors it needs.  The questions force discipline and prevent the AI from defaulting to generic assumptions.

The answers then shaped the model architecture.  Volumes were built up by brand and channel.  Revenue was calculated net of excise and discounts.  Capacity utilisation was explicitly linked to production volumes.  Working capital was expressed in days rather than absolute values.

These details matter.  Without them, a model may still balance, but it would not represent a real brewery business (even if it wasn’t!).

**_**_How the Model was Produced_**_**

Once scope and structure were agreed, Claude generated an Excel file covering a 10-year monthly forecast.  The model included volume build-ups, pricing and excise logic, cost build-ups for materials, packaging and labour, working capital, capital expenditure and financing.  It produced a fully integrated Income Statement, Balance Sheet and Cash Flow Statement, alongside operational KPIs such as hectolitres sold and capacity utilisation.

On the surface, this looked like a complete financial model.  From a speed perspective, it was genuinely impressive.  What would normally take many hours of human effort was produced in minutes.  However, appearance is not the same as reliability.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

****_Treating the AI Output Like a Junior Analyst’s Work_****

Rather than assuming the model was correct, we reviewed it in exactly the same way we would review work prepared by a graduate analyst.

Each issue was logged in an audit file, noting the sheet name, the cell reference and a classification.  Findings were labelled as definite errors, potential errors, best-practice improvements or queries where the logic was unclear.

This distinction is important.  A model may balance and still be wrong.  Revenue can be linked to volume in a simplistic way that ignores excise timing.  Depreciation can be calculated correctly in isolation but disconnected from capital expenditure logic.  Working capital can be expressed as a percentage of sales rather than days, reducing economic realism.

The audit showed that the AI was very strong on structure but weaker on maintaining economic meaning across the entire model.  Some relationships were mathematically correct but financially fragile.  Others relied on hidden assumptions that were not clearly documented.

In short, the model worked mechanically, but not always conceptually.

![](<Base64-Image-Removed>)

****_What AI Did Well and Where it Struggled_****

Claude performed well at building a complete framework.  It could create sheets for revenue, costs, capital expenditure, debt and statements, and link them together coherently.  It followed the architecture laid out in the prompt and respected the idea of a fully integrated three-statement model.

It also handled long and complex instructions far better than earlier generations.  Older models tended to lose context once prompts became too detailed.  Newer versions-maintained structure and completed the task more reliably.

Where it struggled was judgment.  It could not decide whether a cost driver made commercial sense.  It could not tell whether a margin looked realistic.  It could not judge whether the level of detail was appropriate for the intended audience.

These are not calculation problems.  These are professional judgment problems.

****_Why Prompt Design Mattered So Much_****

One of the clearest lessons from this exercise is that AI output quality is driven far more by prompt quality than most people expect.

Words such as “robust”, “auditable” and “three-statement” pushed the AI towards professional standards.  Industry-specific language constrained it to realistic logic.  Requiring step-by-step reasoning made the output easier to review and debug.

An important thing is that the structure of the prompt mirrored real modelling work: scope first, then architecture, then assumptions, then build, then outputs, then checks.  This “structure before content” approach reduced the risk of producing a spreadsheet full of disconnected calculations.

**_The Role AI Can Realistically Play_**

This experiment shows that AI can now generate something recognisably close to a real financial model.  That represents a genuine shift.  However, it also highlights a clear boundary. AI can draft a model quickly, but it cannot validate it.  It does not understand risk in the way a human does.  It does not know what would make a banker or investor uncomfortable.

In practice, the right workflow is not “ask AI and trust it”.  It is “ask AI, then audit it”.  The model becomes a starting point, not an end point.

**_Word to the Wise_**

The natural next step is iteration.  Audit findings can be fed back into the prompt to regenerate a better model.  Errors can be fixed systematically.  Logic may be tightened.  Over time, this creates a loop consists of prompt, build, review, improve.  This does not replace professional financial modelling.  It accelerates the first draft and shifts human effort towards review, judgment and communication.

AI can now produce spreadsheets that look like financial models.  However, our financial modelling is not about spreadsheets: it is about logic, transparency and trust.  General AI tools like Claude can help draft the model.  Humans still need to decide whether it is right.  And that is exactly where responsibility should remain.

_Join us next time for more exciting news of AI tools!_

*   [Log in](https://sumproduct.com/blog/ai-blog-building-a-financial-model-with-ai-what-really-happens-when-you-let-claude-do-the-work/#0)
    
*   [Register](https://sumproduct.com/blog/ai-blog-building-a-financial-model-with-ai-what-really-happens-when-you-let-claude-do-the-work/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/ai-blog-building-a-financial-model-with-ai-what-really-happens-when-you-let-claude-do-the-work/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/ai-blog-building-a-financial-model-with-ai-what-really-happens-when-you-let-claude-do-the-work/#0)

[](https://sumproduct.com/blog/ai-blog-building-a-financial-model-with-ai-what-really-happens-when-you-let-claude-do-the-work/#0 "close")

top