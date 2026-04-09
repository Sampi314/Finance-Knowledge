# Project Finance Storytelling: The one who is balancing the balance sheet – Finexmod

**Source:** https://www.finexmod.com/project-finance-storytelling-the-one-who-is-balancing-the-balance-sheet

---

[Skip to content](https://www.finexmod.com/project-finance-storytelling-the-one-who-is-balancing-the-balance-sheet#content)

Project Finance Storytelling: The one who is balancing the balance sheet

This story is about the struggle to get the balance sheet to balance. Through this story, the messages that I would like to convey are:

*   Although in a project finance transaction, at least at pre-financial close stage, you don’t need to necessarily do any ratio calculations based on balance sheet as all debt convenants and metric are mainly cash based, including a balance sheet in a model is a must. This is because first of all it is part of the 3 statements that needs to be included but most importantly having the balance sheet that balances is an additional check on the model mechanics and indicates that links are done properly. In this story, you will see that Imani (our financial modeler in this episode) will detect couple of errors in the model while trying to balance the balance sheet.
*   If the balance sheet is not balancing, then for each date when the balance sheet is out of balance then find the line item that is causing the imbalance. You can do this by:

– going through the cash flow items, P&L and sources and uses funds statements.

– or swtich on or off different elements and see if the imbalance changes while you are removing different components. If for example you completely remove taxes from the model and you see that the imbalance in the balance sheet changes, then it means that the problems is somehow directly or indirectly related to taxes.

all these is explained in this story.

————————————————————————————————————

Imani has been working on building a financial model for a toll bridge project for almost a week . the only thing left is to build the balance sheet. It’s a project finance deal so she is not doing any ratio calculation based on balance sheet however she knows that she can’t get away with not building it. Also it’s a good way to check the model.

A balance sheet that balances is another indication that the model mechanics and links are done properly.

Every time she builds a balance sheet she has hope that maybe this time she’ll get a balance sheet that balances in the first go. So with that in mind she build the assets, liabilities and equity account and builds the check for whether total asset equals total liabilities in each model period? and it fails!!! she’s too tired and it’s already 7 pm. She will take care of it tomorrow morning with a clear head.

Next day she starts the day by going for a walk in the park. She thinks to herself: “It’s a very good day, indeed, it’s a great day”. With that mindset she goes to her office, make herself a cup of coffee and get back to her model.

She has done this exercise many times before so she has come up with a system:

*   first if the issue rises during construction meaning there’s a difference in assets and liabilities during construction in the balance sheet, then it should be straight forward. Because she has already checked for another statement that covers the construction which is the sources and uses of funds. So if the sources and uses is matching then the issue with balance sheet not balancing might be because a cost or financing instrument is not linked in either the P&L or cash flow statement .So she checks and goes through all the uses of funds items during construction and indeed there’s an imbalance during construction.
*   Now step is to trace where the problem is coming from. She checks the sum total of the imbalance and see whether she can locate this amount in the project cost. she checks and indeed, the problem comes from financing fees. The total amount of imbalance is equal to financing fees payable during construction. She checks and indeed she forgot to include the financing fees in the cash flow waterfall statement. she includes it and the problem is solved for the first model period.
*   But there’s still an imbalance in the second and last construction period. she again tries to traces the amount and see if she can find the same amount in the P&L or Cash flow statement . She realized that the amount is exacty equal to the pre-funding of debt service server account (for more on reserve account, check this link )
*   So she tries to understand the logic.
*   DSRA is included in the current asset and the pre-funding is included in the debt and equity balance in the liabilities. So there must be a double counting in the asset of pre-funding of DSRA. SO most probably it is incuded in the total fixed assets and that is the double counting. SHe goes to the tax and accounting sheets and sees that indeed, pre-funding of DSRA is included in the calculation of total assets. she fixes it and the imbalance is gone in the balance sheet for the construction phase.
*   now she needs to deal with the operation phase. what’s she’s going to do as a first step is to switch on and off what she think is causing the imbalance and see if the problem is solved.
*   – She’s going to put the debt to o and see if the issue is somehow related to the modeling of the debt tranche. She put the gearing to 0 and runs the macro and the problems persists. so it’s not debt
*   she has a parameter to set the drawdown priority on debt and equity facilities during construction. she sets the up6from equity drawdown to 0, meaning she enforces a pro6rata drawdown on facilities and sees if this is sorting the problem. No that;s not it either.
*   she put all parameters related t DSRA to 0 and see if without DSRA the imbalance still remains, and yes the problem has nothing to do with DSRA.
*   She does the same thing with Tax and put all taxes to 0 and the problem is not with taxes either!
*   so last thing she sets the working capital requirement to 0 and runs the macro and yes! that;s it! the problem comes from working capital. something is wrong in either account receivable, account payable, Opex or revenues or combination of them.
*   so checks her revenues calculation,, it all seems ok. she checks Opex and account payable calculation, and it all seems fine as well! so what is it!
*   after a lot digging and a coffee break, she realizes that she made a mistake when linking the cash received in the cash flow statement, so the account receivable are not taken into consideration in the cash flow waterfall and therefore the balance sheet picks it up! she fixes the issue and the balance sheet is balancing

well done Imani!

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-10-17T09:23:07+00:00September 21st, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-is-balancing-the-balance-sheet%2F&t=Project%20Finance%20Storytelling%3A%20The%20one%20who%20is%20balancing%20the%20balance%20sheet "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-is-balancing-the-balance-sheet%2F&text=Project%20Finance%20Storytelling%3A%20The%20one%20who%20is%20balancing%20the%20balance%20sheet "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/project-finance-storytelling-the-one-who-is-balancing-the-balance-sheet/&title=Project%20Finance%20Storytelling%3A%20The%20one%20who%20is%20balancing%20the%20balance%20sheet "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-is-balancing-the-balance-sheet%2F&title=Project%20Finance%20Storytelling%3A%20The%20one%20who%20is%20balancing%20the%20balance%20sheet&summary=This%20story%20is%20about%20the%20struggle%20to%20get%20the%20balance%20sheet%20to%20balance.%20Through%20this%20story%2C%20the%20messages%20that%20I%20would%20like%20to%20convey%20are%3A%0A%0AAlthough%20in%20a%20project%20finance%20transaction%2C%20at%20least%20at%20pre-financial%20close%20stage%2C%20you%20don%27t%20need%20to%20necessarily%20do%20any%20 "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-is-balancing-the-balance-sheet%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-is-balancing-the-balance-sheet%2F&name=Project%20Finance%20Storytelling%3A%20The%20one%20who%20is%20balancing%20the%20balance%20sheet&description=This%20story%20is%20about%20the%20struggle%20to%20get%20the%20balance%20sheet%20to%20balance.%20Through%20this%20story%2C%20the%20messages%20that%20I%20would%20like%20to%20convey%20are%3A%0A%0AAlthough%20in%20a%20project%20finance%20transaction%2C%20at%20least%20at%20pre-financial%20close%20stage%2C%20you%20don%26%2339%3Bt%20need%20to%20necessarily%20do%20any%20ratio%20calculations%20based%20on%20balance%20sheet%20as%20all%20debt%20convenants%20and%20metric "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-is-balancing-the-balance-sheet%2F&description=This%20story%20is%20about%20the%20struggle%20to%20get%20the%20balance%20sheet%20to%20balance.%20Through%20this%20story%2C%20the%20messages%20that%20I%20would%20like%20to%20convey%20are%3A%0A%0AAlthough%20in%20a%20project%20finance%20transaction%2C%20at%20least%20at%20pre-financial%20close%20stage%2C%20you%20don%26%2339%3Bt%20need%20to%20necessarily%20do%20any%20ratio%20calculations%20based%20on%20balance%20sheet%20as%20all%20debt%20convenants%20and%20metric&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F09%2Fcover.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-is-balancing-the-balance-sheet%2F&title=Project%20Finance%20Storytelling%3A%20The%20one%20who%20is%20balancing%20the%20balance%20sheet&description=This%20story%20is%20about%20the%20struggle%20to%20get%20the%20balance%20sheet%20to%20balance.%20Through%20this%20story%2C%20the%20messages%20that%20I%20would%20like%20to%20convey%20are%3A%0A%0AAlthough%20in%20a%20project%20finance%20transaction%2C%20at%20least%20at%20pre-financial%20close%20stage%2C%20you%20don%26%2339%3Bt%20need%20to%20necessarily%20do%20any%20ratio%20calculations%20based%20on%20balance%20sheet%20as%20all%20debt%20convenants%20and%20metric "Vk")
[Email](mailto:?body=https://www.finexmod.com/project-finance-storytelling-the-one-who-is-balancing-the-balance-sheet/&subject=Project%20Finance%20Storytelling%3A%20The%20one%20who%20is%20balancing%20the%20balance%20sheet "Email")

Related Posts
-------------

![Unlocking the 3D Dimension of Financial Modeling: A Consultant’s Journey](https://www.finexmod.com/wp-content/uploads/2023/09/Unlocking-the-3D-Dimension-of-Financial-Modeling-A-Consultants-Journey-500x383@2x.png)

[](https://www.finexmod.com/unlocking-the-3d-dimension-of-financial-modeling-a-consultants-journey/)

#### [Unlocking the 3D Dimension of Financial Modeling: A Consultant’s Journey](https://www.finexmod.com/unlocking-the-3d-dimension-of-financial-modeling-a-consultants-journey/ "Unlocking the 3D Dimension of Financial Modeling: A Consultant’s Journey")

September 27th, 2023 | [0 Comments](https://www.finexmod.com/unlocking-the-3d-dimension-of-financial-modeling-a-consultants-journey/#respond)

![Project Finance Storytelling: The one who sets the price](https://www.finexmod.com/wp-content/uploads/2021/09/Cover-project-finance-storytelling-episode-2-500x383@2x.jpg)

[](https://www.finexmod.com/project-finance-storytelling-the-one-who-needs-to-set-the-tariff/)

#### [Project Finance Storytelling: The one who sets the price](https://www.finexmod.com/project-finance-storytelling-the-one-who-needs-to-set-the-tariff/ "Project Finance Storytelling: The one who sets the price")

September 26th, 2021 | [0 Comments](https://www.finexmod.com/project-finance-storytelling-the-one-who-needs-to-set-the-tariff/#respond)

[Page load link](https://www.finexmod.com/project-finance-storytelling-the-one-who-is-balancing-the-balance-sheet#)

[Go to Top](https://www.finexmod.com/project-finance-storytelling-the-one-who-is-balancing-the-balance-sheet#)