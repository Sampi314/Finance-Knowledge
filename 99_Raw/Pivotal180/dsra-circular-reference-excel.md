# DSRA Circular Reference in Excel | 3 Ways to Fix It

**Source:** https://pivotal180.com/dsra-circular-reference-excel

---

[Skip to content](https://pivotal180.com/dsra-circular-reference-excel/#fl-main-content)

DSRA Circular Reference in Excel – 3 Ways to Fix It
===================================================

By Alison Leckie | February 9, 2026

#### **How to Fix DSRA Circular References in Your Project Finance Model**

You have spent hours building your project finance model. The debt is sculpted. The waterfall is flowing. Then you add the DSRA and everything breaks.

Excel throws a circular reference warning. Your numbers go to zero, or worse, they look correct but are not. If this sounds familiar, you are not alone. The DSRA circular reference is one of the most common headaches in project finance modeling.

In this post, we will explain why DSRA circular references happen, walk through three practical methods to fix them, and help you decide which approach works best for your model.

#### **Why Does the DSRA Create a Circular Reference?**

If you have read our post on [what a DSRA is and how it works](https://pivotal180.com/what-is-a-dsra-what-it-is-and-how-it-works-in-project-finance/)
**,** you know the Debt Service Reserve Account holds enough cash to cover upcoming debt service for a defined period, typically six months.

The problem is that the DSRA target balance depends on future debt service. But debt service itself can depend on the DSRA.

Here is how the loop forms. The DSRA target balance is typically calculated based on the next six months of principal and interest payments. If the DSRA earns interest on its cash balance, that interest becomes part of the project’s cash flow and income. That income affects tax. Tax further affects cash flow. Cash flow affects how much debt the project can support. And the amount of debt determines the debt service that the DSRA target balance was based on in the first place.

Your model ends up going in circles, and Excel does not know where to start.

This circularity also shows up when the DSRA is funded from debt during construction. More construction debt draws mean more interest, which increases total project costs, which may require even more (or faster) debt draws. The DSRA is caught in the middle of it.

Now that we understand the circularities DSRAs can cause, let’s think about how we can fix them.

#### **Method 1: Turn On Iterative Calculations**

This is the quickest fix and the one most people try first. In Excel, go to File, then Options, then Formulas. Check the box that says “Enable iterative calculation.” You may need to adjust the maximum iterations to something like 100 and the maximum change to a small number like 0.0001.

What happens next is that Excel will loop through the circular formulas repeatedly until the numbers converge on a stable answer. For some models, this works in seconds. For larger ones, it may be minutes.

**When to use it:** This method is fine for quick internal analysis or when you are building a model for your own use. It is fast and requires no changes to your formulas.

**When to avoid it:** Most lender-facing and audit-ready models do not allow iterative calculations. The reason is transparency. With iterations turned on, it can become difficult to trace how a number was calculated. If you send a model to a bank and they open it with iterations turned off, the whole thing breaks. That is not a great first impression.

Enabling iterations to solve circularities can also introduce a host of other [complications and challenges](https://pivotal180.com/the-economy-should-be-circular-your-debt-sizing-shouldnt/)
 that smart modelers may wish to avoid.

#### **Method 2: Use a Simple Copy-Paste Macro**

This is the industry standard approach for transaction models. The idea is straightforward. You break the circular chain by replacing one of the live formulas with a static value, then use a macro to update that static value.

Here is how it works in practice. You calculate the DSRA target balance using your normal forward-looking formula. Below that row, you create a second row called something like “DSRA Target (Pasted).” This row contains only hard-coded numbers, not formulas.

You then write a short VBA macro that copies the values in the calculated row and pastes those values as hardcodes into the static row. The rest of your model references the static row instead of the live formula.

When you run the macro, Excel copies the calculated values, pastes them as hardcodes, and the circularity disappears. A well-built macro will repeat the copy-paste a few times until the values in the copied and pasted rows converge. Most models converge (within a reasonable rounding error) after two or three runs.

**When to use it:** This is usually the right choice for any model that will be reviewed by lenders, auditors, or third parties. It keeps your formulas transparent and your model auditable. You can see exactly where the break in the circular chain occurs, and can even set up checks to inform the user when the macro needs to be run again.

**When to avoid it:** Some organizations have strict policies against macros. If your model needs to be completely VBA-free, this approach will not work. Re-running macros repeatedly while building or editing a model over the course of a project development or financing process can also become repetitive and time consuming.

#### **Method 3: Use a Lagged Target Balance**

This method avoids both iterations and macros entirely. Instead of calculating the DSRA target balance based on the next six months of debt service, you base it on the previous six months.

The logic is simple. Debt service in most project finance deals does not change dramatically from one period to the next, especially when the debt has been sculpted against a relatively stable revenue profile. Using a lagged value as a proxy for the forward-looking target introduces a small approximation, but it eliminates the circular reference completely.

You can add a tolerance check in your model to flag any period where the lagged balance differs from the true forward-looking balance by more than a set threshold. This gives you the best of both worlds. Clean formulas with a built-in safety net.

**When to use it:** This is ideal when macros are not permitted and iteration is not acceptable. It works particularly well for models with fixed or sculpted debt service profiles where period-to-period changes are small. It’s also a great choice for models that are being frequently updated throughout a deal process and are not yet in a “final” form.

**When to avoid it:** If debt service is highly variable from period to period, or if the deal has unusual repayment structures, the lagged value may not be a close enough proxy. In those cases, the macro approach is more reliable.

#### **Which Method Should You Use?**

It depends on who will see your model.

For a quick internal check or sensitivity run, turn on iterative calculations and move on with your day. For a model going to lenders or through a model audit, use the copy-paste macro. It is the most widely accepted solution in the industry. If you are working in a macro-free environment, the lagged target balance approach will get the job done cleanly, with results close enough for most applications.

Whatever method you choose, document it. Add a note in your assumptions sheet explaining how the DSRA circularity is handled, or even a switch to choose between options. Reviewers will thank you for it.

#### **Common Mistakes to Watch For**

Even with the right method in place, there are a few things that trip people up. Leaving iterative calculations turned on by accident is the most common one. If you used iterations during development but plan to deliver a macro-based model, make sure you switch it off before sending.

Another frequent issue is forgetting to run the macro after making changes to the model. If you update an assumption and the DSRA values look stale, hit the macro button. Checks are a great way to avoid this problem.

Finally, check that your model does not have other circular references hiding beneath the DSRA one. Sometimes fixing the DSRA reveals a second loop elsewhere in the model, often in the tax or interest income calculations.

#### **Start Building With Confidence**

A DSRA circular reference is not a sign that your model is broken. It is a natural consequence of how project finance works. The cash flows loop back on themselves because the deal structure requires it.

The key is knowing how to manage that circularity cleanly. If you understand the [requirements of a DSRA](https://pivotal180.com/dsra-requirements/)
 and where it sits in the cash flow waterfall, you already have the foundation.

**Training With Pivotal180**

If you want hands-on practice building these mechanics from scratch, our [Renewable Energy Project Finance Modeling](https://pivotal180.com/course-type/renewable-energy-project-finance-modeling/) and [Project Finance Modeling](https://pivotal180.com/course-type/project-finance-modeling/) courses walk you through the DSRA module step by step, including how to handle the circularity. Come model with us!

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fdsra-circular-reference-excel%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fdsra-circular-reference-excel%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fdsra-circular-reference-excel%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#99a6fbf6fde0a4f1edede9eabcaad8bcabdfbcabdfe9f0eff6edf8f5a8a1a9b7faf6f4bcabdffdeaebf8b4faf0ebfaecf5f8ebb4ebfcfffcebfcf7fafcb4fce1fafcf5bcabdf)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Alison Leckie

[https://www.linkedin.com/in/alison-leckie-56023364/](https://www.linkedin.com/in/alison-leckie-56023364/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/dsra-circular-reference-excel/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA