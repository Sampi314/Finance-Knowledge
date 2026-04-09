# Disbursement Order in a Project Finance deal – Finexmod

**Source:** https://www.finexmod.com/disbursement-order-in-a-project-finance-deal

---

[Skip to content](https://www.finexmod.com/disbursement-order-in-a-project-finance-deal#content)

Disbursement Order in a Project Finance deal

In a project finance deal which is by its nature a non-recourse or limited recourse transaction, lenders still require that sponsor provide some of the funding require for the project completion. Regarding the sizing of equity and debt, it is both a technical and negotiation point with lenders. It is technical because depending on projected cash flows, the project may be limited by how much debt it can raise. It’s also a negotiation point because lenders require sponsor to have some skin in the game and enforce a maximum gearing (Debt to capital radio). There might be cases where the project can support 100% debt funding but the maximum gearing or let’s 70% DE ratio might limit the borrowing to 70%.

So the question of having equity to fund the construction is almost true for all projects. However, another point of negotiations between lenders and sponsors in the timing of equity contribution.

During construction because the SPV is cash flow negative, then the drawdowns from different funding instruments should match that of the expenses (Uses of funds) and no matter how you drawdown on your funding instruments, the base case financial model should ensure that there’s no cash deficit in any of the construction period and that sources and uses of funds match in each model period. This is actually one of the important financial model integrity checks that is recommended to have in your financial models. For more on Integrity checks, please refer to the below link:

[Building Integrity Checks in Project Finance Models (Manual & Template)](https://www.eloquens.com/tool/wmjEi0N4/finance/project-finance-models/building-integrity-checks-in-project-finance-models-manual-template?ref=FinExMod)

Alternative Drawdown schedules
==============================

Here are the different Drawdown options between debt and equity:

*   Pro-rata drawdown on all facility
*   Full up-front equity drawdown
*   Partial up-front equity drawdown and the remaining pro-rata with debt

Because the timing of drawdowns affects the financing costs, total project cost under different drawdown scenarios will not be the same. Before you look at the below table, can you guess which of the 3 above scenarios is going to result in a higher total project cost?

The answer is scenario 1 where you don’t have any up-front equity and that is because you start drawing down of debt faster than a scenario where lenders require an upfront equity injection.

![The impact of different drawdown schedules in a project finance deal and points of negotiations](https://www.finexmod.com/wp-content/uploads/2021/03/Drawdown-Image-01-1.jpg)

Catch-up Period
===============

In Scenario 3 above, you might asked yourself what’s happening between month 2 to month 3? there’s no equity and we only drawdown on debt? is this a mistake?

The answer lies in the row with the title “% debt in TPC”, which stands for Total debt to total project cost which is sometimes called gearing or debt to capital ratio. As you can see because in case 3 we had 50% up-front injection from equity, we have a debt to equity ratio inferior to the required gearing of 70%. So in this case in Q2 and Q3, we can only draw on debt until we reach 70%. This is sometimes called catch-up period. Of course, this mechanism is subject to negotiation with lenders and need to get approved and included in the loan agreement.

Impact of Timing of Drawdowns on Equity IRR
===========================================

Next question is, can you guess which of the 3 scenarios would result in a lower equity IRR?

The answer is scenario 2. Everything else remaining the same, the equity IRR will be lower as you accelerate the equity injection.

![The impact of different drawdown schedules in a project finance deal and points of negotiations](https://www.finexmod.com/wp-content/uploads/2021/03/Drawdown-Image-02-1.jpg)

Points of negotiations
======================

Given the answer to the above question, it is clear that sponsor are more in favor of a situation where they are not required to put any up-front equity into the SPV. As we lenders on the other hand want to make sure that sponsors are committed to the project (skin in the game) so they will be in favor of having full equity up-front. The middle case which is subject to negotiations is to have a portion of equity up-front and remaining to be injected pro-rata with debt.

![This blog post discusses impact of timing of injection of different financing facilities on the main project metrics](https://www.finexmod.com/wp-content/uploads/2021/03/Drawdown-Image-03.jpg)

Flexible timing of drawdowns in a financial model
=================================================

Now let’s get into Excel.

**Step 1: Inputs** 
-------------------

In order to provide flexibility to users to test different drawdown schedules, you just need one parameter in your “Inputs” and that is:

“Up-front Equity drawdown requirement” expressed in percentage of Total Base Equity Commitment. For example in below snapshot, in the financing section of Inputs, user can test the impact of different timing of injection of equity by simply changing the switch (For more on this structure, please refer to “[One Model Approach](https://www.finexmod.com/one-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples/)
“)

![This blog post discusses impact of timing of injection of different financing facilities on the main project metrics](https://www.finexmod.com/wp-content/uploads/2021/03/Drawdown-Image-04.jpg)

Now modeling the periodic drawdowns requires some algebra.

Step 2: Up-front Equity
-----------------------

First of all based on the input defined in Step 1, you size how much of equity is upfront and how much is to be disbursed pro-rata with debt and then calculate how the up-front portion of the equity needs to be injected. For this you need to create an available balance and the up-front equity drawdown will be the minimum of funding requirement and available balance in the up-front equity account.

![This blog post discusses impact of timing of injection of different financing facilities on the main project metrics](https://www.finexmod.com/wp-content/uploads/2021/03/Drawdown-Image-06.jpg)

Step 3: Pro-rata Equity
-----------------------

Now let’s do some algebra. Let’s say maximum gearing is 70-30 meaning that in each model period the Debt to Equity Ratio should not exceed 70:30.

∑Equity= 30% \* ∑TPC

∑Equity = ∑Up-front equity + ∑Pro-rata equity

**∑Pro-rata equity = 30% \* ∑TPC – ∑Up-front equity**

![This blog post discusses impact of timing of injection of different financing facilities on the main project metrics](https://www.finexmod.com/wp-content/uploads/2021/03/image-01.jpg)

Step 4: Total Equity
--------------------

The sum of Step 2 and Step 3 will give you total equity drawn on periodic basis.

∑Equity = ∑Up-front equity + ∑Pro-rata equity

![This blog post discusses impact of timing of injection of different financing facilities on the main project metrics](https://www.finexmod.com/wp-content/uploads/2021/03/Drawdown-Image-08.jpg)

DOWNLOAD
========

Download the workbook here ► [https://www.eloquens.com/company/hedieh](https://www.eloquens.com/company/hedieh)

[](https://www.finexmod.com/disbursement-order-in-a-project-finance-deal#)

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-03-24T08:07:37+00:00March 23rd, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fdisbursement-order-in-a-project-finance-deal%2F&t=Disbursement%20Order%20in%20a%20Project%20Finance%20deal "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fdisbursement-order-in-a-project-finance-deal%2F&text=Disbursement%20Order%20in%20a%20Project%20Finance%20deal "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/disbursement-order-in-a-project-finance-deal/&title=Disbursement%20Order%20in%20a%20Project%20Finance%20deal "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fdisbursement-order-in-a-project-finance-deal%2F&title=Disbursement%20Order%20in%20a%20Project%20Finance%20deal&summary=In%20a%20project%20finance%20deal%20which%20is%20by%20its%20nature%20a%20non-recourse%20or%20limited%20recourse%20transaction%2C%20lenders%20still%20require%20that%20sponsor%20provide%20some%20of%20the%20funding%20require%20for%20the%20project%20completion.%20Regarding%20the%20sizing%20of%20equity%20and%20debt%2C%20it%20is%20both%20a%20techni "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fdisbursement-order-in-a-project-finance-deal%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fdisbursement-order-in-a-project-finance-deal%2F&name=Disbursement%20Order%20in%20a%20Project%20Finance%20deal&description=In%20a%20project%20finance%20deal%20which%20is%20by%20its%20nature%20a%20non-recourse%20or%20limited%20recourse%20transaction%2C%20lenders%20still%20require%20that%20sponsor%20provide%20some%20of%20the%20funding%20require%20for%20the%20project%20completion.%20Regarding%20the%20sizing%20of%20equity%20and%20debt%2C%20it%20is%20both%20a%20technical%20and%20negotiation%20point%20with%20lenders.%20It%20is%20technical%20because%20depending%20on%20projected "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fdisbursement-order-in-a-project-finance-deal%2F&description=In%20a%20project%20finance%20deal%20which%20is%20by%20its%20nature%20a%20non-recourse%20or%20limited%20recourse%20transaction%2C%20lenders%20still%20require%20that%20sponsor%20provide%20some%20of%20the%20funding%20require%20for%20the%20project%20completion.%20Regarding%20the%20sizing%20of%20equity%20and%20debt%2C%20it%20is%20both%20a%20technical%20and%20negotiation%20point%20with%20lenders.%20It%20is%20technical%20because%20depending%20on%20projected&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F03%2FDrawdown-cover.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fdisbursement-order-in-a-project-finance-deal%2F&title=Disbursement%20Order%20in%20a%20Project%20Finance%20deal&description=In%20a%20project%20finance%20deal%20which%20is%20by%20its%20nature%20a%20non-recourse%20or%20limited%20recourse%20transaction%2C%20lenders%20still%20require%20that%20sponsor%20provide%20some%20of%20the%20funding%20require%20for%20the%20project%20completion.%20Regarding%20the%20sizing%20of%20equity%20and%20debt%2C%20it%20is%20both%20a%20technical%20and%20negotiation%20point%20with%20lenders.%20It%20is%20technical%20because%20depending%20on%20projected "Vk")
[Email](mailto:?body=https://www.finexmod.com/disbursement-order-in-a-project-finance-deal/&subject=Disbursement%20Order%20in%20a%20Project%20Finance%20deal "Email")

Related Posts
-------------

![Using Macros in your financial models: Quick tips](https://www.finexmod.com/wp-content/uploads/2025/07/Cover-Learning-VBA-500x383@2x.png)

[](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/)

#### [Using Macros in your financial models: Quick tips](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/ "Using Macros in your financial models: Quick tips")

July 3rd, 2025

![Accuracy in Financial Modeling](https://www.finexmod.com/wp-content/uploads/2025/06/2-500x383@2x.png)

[](https://www.finexmod.com/draft-post-2/)

#### [Accuracy in Financial Modeling](https://www.finexmod.com/draft-post-2/ "Accuracy in Financial Modeling")

June 12th, 2025

![The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/disbursement-order-in-a-project-finance-deal)

[](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/)

#### [The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/ "The Art of Structuring Project Finance Models: A Personal Journey")

April 10th, 2025

[Page load link](https://www.finexmod.com/disbursement-order-in-a-project-finance-deal#)

[Go to Top](https://www.finexmod.com/disbursement-order-in-a-project-finance-deal#)