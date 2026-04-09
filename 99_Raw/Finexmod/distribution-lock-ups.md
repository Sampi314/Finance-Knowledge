# Project Finance Loan Term sheet: Distribution and Distribution Lock-Ups – Finexmod

**Source:** https://www.finexmod.com/distribution-lock-ups

---

[Skip to content](https://www.finexmod.com/distribution-lock-ups#content)

Project Finance Loan Term sheet: Distribution and Distribution Lock-Ups

In the discussion on the **[Cash flow waterfall](https://www.finexmod.com/waterfall/)
**, I showed you that any payment to shareholders come at the bottom of the Cash flow waterfall. Once all payment to operators and lenders are paid and cleared, what remains can be consider for distribution but there are still other conditions that needs to be met before any payment to investor is allowed.

![Cash Flow Waterfall or Cascade in a Project Finance and Distribution to investors ](https://www.finexmod.com/wp-content/uploads/2021/05/Lockup05-e1619951831650.jpg)

As John D. Rockefeller once said : “Do you know the only thing that gives me pleasure? It’s to see my dividends coming in.”. In this blog post, we are going to look at when and how we can make Mr. Rockefeller happy.

I am basically going to talk about another important measure imposed by lenders and enforced in the loan agreement which is _“Dividend lock-ups”; “Distribution lock-up “; or “Distribution Stops”._

What is a Dividend Lock-up and why it is needed?
------------------------------------------------

Previously I talk about [**Debt Service Reserve Account**](https://www.finexmod.com/negotiating-a-project-financing-term-sheet-key-issues-with-debt-service-reserve-account/)
 and [**Contingency Provision**](https://www.finexmod.com/negotiating-a-project-financing-term-sheet-contingency-provision/)
 among  measured imposed by lenders to secure the future debt service. Dividend lock ups are also measures that ensures that the project company has sufficient cash to repay debt before any distribution to shareholders is allowed. It’s basically a set of conditions that needs to be satisfied before any distribution to shareholder is allowed.

In a project finance type of transaction, the future project cash flows are the primary source of debt repayment and lenders have no or limited recourse to sponsors for the repayment of the loan. The project (SPV) can not start paying back the loan until the project is operational.  that is why making sure that the future cash flows under the base case are sufficient and there’s reasonable buffer in case of temporarily problems is what drives most of the clauses in a loan agreement and distribution lock-ups are also one of the measures.

Where to find the Dividend Lock-ups in a typical project finance loan agreement?
--------------------------------------------------------------------------------

Typically the distribution lock-ups are mentioned under the “Distribution” clause listing measures and conditions to be fulfilled before any payment to shareholder is allowed. The conditions dictated by lenders differs from project to project but here are the most common ones:

*   Distribution are allowed after the Project Financial Completion Date has occurred meaning that project is operational and the first principal repayment is paid (Typically distributions are not allowed during the grace period). For the definition of Financial Completion Date please refer to my blog post on **[key dates in a project finance loan agreement](https://www.finexmod.com/dates/)**.
*   the “Debt Service Reserve Account Required Balance” is met. For more on Debt Service Reserve Account please refer to [**my blog post on DSRA**](https://www.finexmod.com/negotiating-a-project-financing-term-sheet-key-issues-with-debt-service-reserve-account/)
    . You can also download the **[free template](https://www.eloquens.com/tool/nJeYHzd1/strategy/waterfall-chart-excel-templates/typical-cash-flow-waterfall-excel-template-and-pdf-manual?ref=FinExMod)
    **.
*   the “Maintenance Reserve Account Required Balance” is met (if Required)
*   the Historic DSCR on each Calculation Date is greater than , say,  1.15x
*   the Projected DSCR  on Calculation Date is greater than , say,  1.15x
*   the LLCR on each Calculation Date is greater than, say, 1.20

**How to Use the distribution lock-ups in the financial model?**
----------------------------------------------------------------

**Step 1:** Dividends-lock-up ratios and conditions in “Inputs”

If there’s already a term sheet, you should refer to the term sheet and reflect the distribution lock-ups as per the contract in the assumption section of your model. If the project is at early stage, you can make up assumption and put a note either next to the cells or in a separate sheet where you keep track of the sources of your data that “Internal Assumption and subject to lenders approval” ([**for more on that check my blog on databook**](https://www.finexmod.com/where-did-you-get-your-data/)
)

![Distribution Lock-ups or Distribution Stops or Dividend lock-ups in a Project Finance Loan agreement and Project Finance Financial Model ](https://www.finexmod.com/wp-content/uploads/2021/05/Lockup01.jpg)

**Step 2:** Create a distribution flag

Before calculating the lock-up ratio flags, you must calculate the Different Debt metric ([Check out my suggested template for calculating Debt Metrics in a typical Project Finance model](https://www.eloquens.com/tool/3BAzTyDp/finance/project-finance-models/project-finance-debt-metrics-manual-and-template?ref=FinExMod)
)

Once you have your DSCRs (Periodic, Historical & Project), you simply need to create a flag checking if the period debt ratios are higher than the ratio lock-ups.

You must then also include other checks like:

*   Check for Financial Completion Date and stop any distribution before Financial Completion is achieved
*   Check for the Balance of DSRA and Limit any distribution if DSRA is not fully funded

and any other condition required by lenders that can be modeled.

![Lockup Debt ratios and Distribution Flags in a Project Finance Financial Model and Loan Agreement](https://www.finexmod.com/wp-content/uploads/2021/05/Lockup03.jpg)

**Step 3:** Once you have all the flags, you then create an aggregate flag that you can call ” Distribution Flag” and use this flag when you are calculating any payment to shareholders including any payment as shareholder loan (interest and principal) and dividends.

![Lockup Debt ratios and Distribution Flags in a Project Finance Financial Model and Loan Agreement](https://www.finexmod.com/wp-content/uploads/2021/05/Lockup04.jpg)

I hope you found this information useful. Now, I would love to hear from you. Let me know:

*   What are the common Dividend Lock-up Ratios that you have come across?
*   Do you typically include a distribution flag in your Project Finance models?

Take care and hope to catch you next time.

Best regards,

Hedieh

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-05-04T05:35:10+00:00May 4th, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fdistribution-lock-ups%2F&t=Project%20Finance%20Loan%20Term%20sheet%3A%20Distribution%20and%20Distribution%20Lock-Ups "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fdistribution-lock-ups%2F&text=Project%20Finance%20Loan%20Term%20sheet%3A%20Distribution%20and%20Distribution%20Lock-Ups "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/distribution-lock-ups/&title=Project%20Finance%20Loan%20Term%20sheet%3A%20Distribution%20and%20Distribution%20Lock-Ups "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fdistribution-lock-ups%2F&title=Project%20Finance%20Loan%20Term%20sheet%3A%20Distribution%20and%20Distribution%20Lock-Ups&summary=In%20the%20discussion%20on%20the%20Cash%20flow%20waterfall%2C%20I%20showed%20you%20that%20any%20payment%20to%20shareholders%20come%20at%20the%20bottom%20of%20the%20Cash%20flow%20waterfall.%20Once%20all%20payment%20to%20operators%20and%20lenders%20are%20paid%20and%20cleared%2C%20what%20remains%20can%20be%20consider%20for%20distribution%20but%20the "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fdistribution-lock-ups%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fdistribution-lock-ups%2F&name=Project%20Finance%20Loan%20Term%20sheet%3A%20Distribution%20and%20Distribution%20Lock-Ups&description=In%20the%20discussion%20on%20the%20Cash%20flow%20waterfall%2C%20I%20showed%20you%20that%20any%20payment%20to%20shareholders%20come%20at%20the%20bottom%20of%20the%20Cash%20flow%20waterfall.%20Once%20all%20payment%20to%20operators%20and%20lenders%20are%20paid%20and%20cleared%2C%20what%20remains%20can%20be%20consider%20for%20distribution%20but%20there%20are%20still%20other "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fdistribution-lock-ups%2F&description=In%20the%20discussion%20on%20the%20Cash%20flow%20waterfall%2C%20I%20showed%20you%20that%20any%20payment%20to%20shareholders%20come%20at%20the%20bottom%20of%20the%20Cash%20flow%20waterfall.%20Once%20all%20payment%20to%20operators%20and%20lenders%20are%20paid%20and%20cleared%2C%20what%20remains%20can%20be%20consider%20for%20distribution%20but%20there%20are%20still%20other&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F05%2FCover-distribution-lock-up.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fdistribution-lock-ups%2F&title=Project%20Finance%20Loan%20Term%20sheet%3A%20Distribution%20and%20Distribution%20Lock-Ups&description=In%20the%20discussion%20on%20the%20Cash%20flow%20waterfall%2C%20I%20showed%20you%20that%20any%20payment%20to%20shareholders%20come%20at%20the%20bottom%20of%20the%20Cash%20flow%20waterfall.%20Once%20all%20payment%20to%20operators%20and%20lenders%20are%20paid%20and%20cleared%2C%20what%20remains%20can%20be%20consider%20for%20distribution%20but%20there%20are%20still%20other "Vk")
[Email](mailto:?body=https://www.finexmod.com/distribution-lock-ups/&subject=Project%20Finance%20Loan%20Term%20sheet%3A%20Distribution%20and%20Distribution%20Lock-Ups "Email")

Related Posts
-------------

![Accuracy in Financial Modeling](https://www.finexmod.com/wp-content/uploads/2025/06/2-500x383@2x.png)

[](https://www.finexmod.com/draft-post-2/)

#### [Accuracy in Financial Modeling](https://www.finexmod.com/draft-post-2/ "Accuracy in Financial Modeling")

June 12th, 2025

![My Intention When Reviewing a Financial Model: What I Can Improve and What I Can Learn](https://www.finexmod.com/wp-content/uploads/2024/09/Copy-of-White-Minimalist-Blog-Post-Linkedin-Article-Cover-500x383@2x.png)

[](https://www.finexmod.com/my-intention-when-reviewing-a-financial-model-what-i-can-improve-and-what-i-can-learn/)

#### [My Intention When Reviewing a Financial Model: What I Can Improve and What I Can Learn](https://www.finexmod.com/my-intention-when-reviewing-a-financial-model-what-i-can-improve-and-what-i-can-learn/ "My Intention When Reviewing a Financial Model: What I Can Improve and What I Can Learn")

September 27th, 2024

![Project Finance Construction Risk Mitigation Measures: Funded Contingency Provision](https://www.finexmod.com/wp-content/uploads/2024/09/contingency-Cover-500x383@2x.png)

[](https://www.finexmod.com/project-finance-contingency/)

#### [Project Finance Construction Risk Mitigation Measures: Funded Contingency Provision](https://www.finexmod.com/project-finance-contingency/ "Project Finance Construction Risk Mitigation Measures: Funded Contingency Provision")

September 13th, 2024 | [0 Comments](https://www.finexmod.com/project-finance-contingency/#respond)

[Page load link](https://www.finexmod.com/distribution-lock-ups#)

[Go to Top](https://www.finexmod.com/distribution-lock-ups#)