# The economy should be circular. Your debt sizing shouldn’t.

**Source:** https://pivotal180.com/the-economy-should-be-circular-your-debt-sizing-shouldnt

---

[Skip to content](https://pivotal180.com/the-economy-should-be-circular-your-debt-sizing-shouldnt/#fl-main-content)

The economy should be circular. Your debt sizing shouldn’t.
===========================================================

By Matt Davis | February 10, 2025

We’ve all been there.

The ominous three-tone _ping_ of doom. The maze of blue arrows crisscrossing each other like a failed [Tobias Fünke](https://www.youtube.com/watch?v=axHe_BVY_9c) cat’s cradle. The pop-up dialog box that haunts our dreams and wakes us from our fitful sleep, sweat-drenched and screaming:

![Circular Reference](https://pivotal180.com/wp-content/uploads/2025/02/Screenshot-2025-02-11-073926.jpg)

The dreaded circular reference.

What is a circular reference in Excel?
--------------------------------------

A circular reference in Excel occurs when a formula refers to itself. This may happen directly – for example, entering **\=A1 in cell A1** – or indirectly, that is, when two or more sequential formulas eventually link back to their starting point. **If A1 is set to equal B1, B1 is set to equal C1, and C1 is set to equal A1**, the combination of those three formulas is circular.

Within project finance models, **there are some calculations which are inherently circular**. Pivotal180 students will recognize two of such instances: construction funding costs and yield-based flip tax equity sizing.

### How to fix a circular reference

When a circular reference occurs, modelers have three choices:

1.  Replace the circular formula(s) with a non-circular alternative. Though not 100% correct, this provides an answer accurate enough for decision-making.
2.  Build a macro to automate a process (usually copy-and-paste) which removes the circularity.
3.  Enable iterations within Excel’s ‘Options’ menu, allowing to calculate circular formulas.

Depending on modeler preferences and the impact of the circularity in question, either of option 1 or 2 may be an appropriate choice. But to choose option 3 and enable iterations? To paraphrase The Bard: that way madness (and errors) lies.

### Should you allow for circular formulas in Excel?

Microsoft Excel can solve circular models. It calculates over and over until reaching equilibrium. Some modelers feel comfortable with circularities, but Pivotal180 strongly recommends against them. There are several reasons:

*   Circular models, especially big ones, can take a **long** time to solve. Excel has to repeat calculations over and over to reach a final result.
*   Data tables – hallmarks of any well-designed model – will take even longer to update. Each case requires Excel to resolve again.
*   Goal seeks may not work, or may solve to many different solutions on different computers or starting points.

Above all, **most circular references are created accidentally**, with the modeler not realizing the relationship between all the calculations involved. With iterations enabled, Excel will no longer show its friendly box to warn the user about any new circularities. This can lead to new circularities the modeler is unaware of, which almost always results in errors down the line.

One calculation that is often circular in many models is a most critical one: debt sizing. Many of us in the renewable energy industry aim to enable a less wasteful and more [circular economy](https://en.wikipedia.org/wiki/Circular_economy)
. But any Pivotal180 **[Renewable Energy Project Finance Modeling](https://pivotal180.com/course-type/renewable-energy-project-finance-modeling/)
** graduate can attest that debt sizing need not be circular at all.

**Circular debt sizing explained**
----------------------------------

Spreadsheets may be two-dimensional, but you don’t need to understand [Membrane Theory](https://www.youtube.com/watch?v=RKRksnjSxWI&t=1s)
 to see that debt sizing shouldn’t be a flat circle. Many modelers, though – beginners and experienced alike – make that mistake.

Most calculations run forward (left to right) through the financial model timeline. By contrast, **circular debt sizing runs in reverse, from right to left**. This becomes evident within the debt account.

With forward calculations, each period’s opening debt balance would equal the prior period’s closing balance. But in a circular debt sizing model each closing debt balance is equal to the next period’s opening balance. In the last model period, for example, the closing balance is equal to the (blank) opening balance in the next column. And so on from right to left, until the first period closing debt balance is equal to the second period opening balance.

Traditional project finance debt sizing starts with Cash-Flow Available for Debt Sizing (CADS or CFADS), which is then divided by a lender-assigned Debt Service Coverage Ratio (DSCR) to determine the total maximum debt service in each period. The next step is to determine how much of that maximum debt service is needed to pay interest in each period, and thus how much is left to repay principal on the loan. Interest expense is a function of the interest rate multiplied by the opening loan balance in each period. Interest is then deducted from the maximum debt service to determine how much principal can be repaid. This is where the circular approach breaks down.

### Why should you avoid circular debt sizing?

Using the first period as an example, the closing balance would be equal to the period 2 opening balance. To calculate the opening debt balance in period 1 – which is, ultimately, the size of the loan – we add debt repayments to that period’s closing balance. Debt repayments, though, are calculated as maximum debt service (CADS/DSCR) less interest, and interest is calculated on the opening debt balance – the very value we were trying to solve at the start! In other words, **the (A) opening balance depends on (B) repayments, (B) repayments depend on (C) interest, and (C) interest depends on the (A) opening balance**. This circularity, as shown in Exhibit 1, repeats in every year of the debt account.

![Excel spreadsheet showing circular debt sizing](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201244%20348'%3E%3C/svg%3E)

Exhibit 1: Circular debt sizing; red arrows indicate circular calculations, while green arrows indicate non-circular ones

While this approach – deriving the opening balance in each period from the sum of that period’s closing balance and scheduled principal repayments – seems logical, it is inherently circular. Debt sizing is often the first financing calculation done in a model. **Enabling circular calculations at such an early stage is likely to result in new ones being built later without the modeler noticing**.

Benefits of non-circular debt sizing
------------------------------------

So, it seems like we are simple beings who experience time in a linear way. Fortunately, this linear approach works well for sizing debt without circular references.

### **The present (value) is a gift**

Equity investors feel at home with the concept of Present Value (PV). When evaluating an investment opportunity, modelers often calculate the Net Present Value of the forecasted project cash-flows with the NPV function. The NPV of a project’s future cash-flows discounted at the investor’s hurdle rate yields the Present Value of the project to that investor. In other words, how much would they be willing to buy the project for?

Here’s what practitioners of circular debt sizing models might not realize. Lenders are, like equity, investors who earn a guaranteed hurdle rate – their interest rate. The trick to sizing debt simply becomes discounting a set of future cash-flows promised to the lender at the interest rate.

As mentioned earlier, project finance debt sizing always starts with dividing CADS by a DSCR to determine the total maximum debt service in each period. That maximum debt service number – which will then be split into interest and principal – is the **total cash-flow paid to the lender in each period!** Armed with that understanding, debt sizing is just the present value of those cash flows.

![Excel spreadsheet showing non-circular debt sizing](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201207%20338'%3E%3C/svg%3E)

Exhibit 2: Non-circular debt sizing; all calculations are non-circular

As you can see, this method calculates the same debt size, but avoids the trap of circular references.

#### **But wait, my model is quarterly and has a variable interest rate – what should I do?**

To learn more about debt sizing and other critical concepts for world-class project finance modelers, enroll in a Pivotal180 course! We offer a range of training programs for different backgrounds and experience levels:

*   **[Renewable Energy Project Finance Modeling](https://pivotal180.com/course-type/renewable-energy-project-finance-modeling/)
    **
*   **[Infrastructure & Project Finance Modeling](https://pivotal180.com/course-type/project-finance-modeling/)
    **
*   **[Introduction to Project Finance Modeling](https://pivotal180.com/course-type/introduction-project-finance-modeling/)
    **

Looking to take your modeling skills up a notch? Our **[Advanced Debt](https://pivotal180.com/course-type/customizable-partial-day-modeling/)
** short course covers a range of debt modeling concepts including:

*   leverage limits
*   cash sweeps
*   leverage sensitivities
*   multiple covenant debt sizing
*   sources and types of debt
*   loan agreements and terms
*   loan life coverage ratio (LLCR) and debt covenants
*   debt service reserve accounts (DSRA).

Check out the links below to learn more about Pivotal180. This includes all our financial modeling courses and services. Come model with us!

*   Additional **[Short Courses](https://pivotal180.com/course-type/customizable-partial-day-modeling/)
    ** – including our new program on post-IRA tax equity!
*   **[Tax Equity Modeling](https://pivotal180.com/courses/tax-equity-modeling/)
    **
*   **[Intro to Battery Storage & Financial Modeling](https://pivotal180.com/courses/battery-storage-financial-modeling-course/)
    **
*   **[Financial Modeling Advisory & Consulting Services](https://pivotal180.com/advisory/)
    **

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fthe-economy-should-be-circular-your-debt-sizing-shouldnt%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fthe-economy-should-be-circular-your-debt-sizing-shouldnt%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fthe-economy-should-be-circular-your-debt-sizing-shouldnt%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#536c313c372a6e3b27272320766012766115766115233a253c27323f626b637d303c3e766115273b367e36303c3d3c3e2a7e203b3c263f377e31367e303a2130263f32217e2a3c26217e373631277e203a293a3d347e203b3c263f373d27766115)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Matt Davis

[](https://pivotal180.com/the-economy-should-be-circular-your-debt-sizing-shouldnt/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/the-economy-should-be-circular-your-debt-sizing-shouldnt/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA