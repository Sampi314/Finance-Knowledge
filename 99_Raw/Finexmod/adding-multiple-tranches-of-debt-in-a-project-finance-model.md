# Adding Multiple Tranches of Debt in a Project Finance Model – Finexmod

**Source:** https://www.finexmod.com/adding-multiple-tranches-of-debt-in-a-project-finance-model

---

[Skip to content](https://www.finexmod.com/adding-multiple-tranches-of-debt-in-a-project-finance-model#content)

Adding Multiple Tranches of Debt in a Project Finance Model

When you are at the early stage of the appraisal of a project finance deal and you haven’t yet approached any lenders, you might only need to model one tranche of debt in your project finance model. As you progress with the project and you start negotiating with different banks, you will need to test different financing instruments and different debt terms. 

I always recommend to at least include 2 tranches of debt in your financial model. You can use only one tranche at the early stage and activate the second tranche when needed. 

In this blog post, I want to show you how to build your models in such a way that if you need to add another tranche of debt, you could easily do it following couple of steps and you won’t need to spend half day to balance the balance sheet after adding a third tranche in your model. 

Let’s tell this with a story. Let’s say that you are working on a project for a couple of months now and you have a financial model with 2 tranches of debt. Up to now you could do with these two tranches of debt because you have a pool of lenders giving an 18 years tenor and another pool of lenders providing 15 years tenor. You just received an email from the Mandate lead arranger that one of the banks pulled out of the deal and there’s no possibility for any of the lenders to go beyond their current commitment to replace that lender and cover the gap. There’s a possibility for engaging with a local bank but the maximum tenor offered by this bank is 12 years. Now you need to add a third tranche in your existing model. 

When I was building the model in the first place I had this in mind that what if in future I need to add other tranches. So, I did the formulas, links and modules in such a way that I could copy one of the existing tranches and paste it, make a couple of adjustments and have my third tranche. Here is how:

1.  List all tranches in your inputs: In your Inputs sheet, in the financing section, list all the senior tranches and include the maximum commitment from each tranche. You can express it in percentages or in $ value. If the size of the debt is not yet fixed and is still limited to a certain gearing or achievement of a minimum DSCR then you need to keep one as the floating/balancing tranche. 

Just a side note regarding the format of my Input sheet, I am presenting my constant inputs (inputs that are not time dependent) in the form of scenarios. For more on that please check this link. 

[One Model Approach: A Single Integrated financial model for different stakeholders with Practical Real Life Examples](https://www.finexmod.com/one-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples/)

![](https://www.finexmod.com/wp-content/uploads/2021/01/Multiple-tranches-1.png)

This way user can see upfront how many tranches are available and how many of them are active in the model (if the %s or amount is 0 it means it is not active in the current case)

![](https://www.finexmod.com/wp-content/uploads/2021/01/Multiple-tranches-2.png)

2\. Step 2 is to start listing the specific terms of each debt tranche in your Input sheet. While building the Senior Debt terms for each tranche, also link the labels to the name of the tranche that you just listed above (step 1)

![](https://www.finexmod.com/wp-content/uploads/2021/01/Multiple-tranches-3.png)

3\. After you have done step 1 & 2, for the next tranche you just copy and paste all the inputs for tranche 1. Change the subheading to the cell where you have the name for tranche 2 and customize the inputs to match the terms you have for tranche 2. You repeat the same thing for tranche 3. 

This way if you need to add a 4th tranche you simply do step 1, meaning adding the tranche to the list of pooling lenders and then copy and paste any of the debt terms and customize it. 

![](https://www.finexmod.com/wp-content/uploads/2021/01/Multiple-tranches-3.png)

4\. Now that you are done with the inputs, you create a calculation sheet or if you already have one go there and start building the debt balance for tranche 1. But first start with the header and link the header to the name of senior tranche 1 in your input sheet.

![](https://www.finexmod.com/wp-content/uploads/2021/01/Multiple-tranches-4.png)

5\. Then carry one with building different calculator blocks for the debt, meaning:

*   Senior debt Tranche 1 timing flags and counters
*   Senior Debt Tranche 1 drawdown 
*   Senior Debt Tranche 1 Fees
*   Senior Debt Tranche 1 Interest payable during construction
*   Senior Debt Tranche 1 Interest payable during repayment
*   Senior Debt Tranche 1 Principal repayment
*   Senior Debt Tranche 1 balance 
*   Senior Debt Tranche 1 Check

– When you are making these calculations, always bring the input that you need from the input sheet to this calculation sheet. This has 2 benefits. One the auditor or user can see directly next to the formula what;s the value of the input that you are using and avoid the back and forth movement between inputs and calculations to trace the formula. Second, in the next step, when you want to replicate the tranche to create tranche 2 and 3, you simply need to change the inputs and link them to the relevant tranches. 

– Note that every time

that you are doing these calculations, in the labels instead of typing “Senior Debt Tranche 1”, link it to the cell in your Inputs where you put the name of the tranche (Step 1)

![](https://www.finexmod.com/wp-content/uploads/2021/01/Multiple-tranches-5.png)

6\. Now that you have one generic tranche, you simply:

*   Copy and paste it beneath the Senior Debt Tranche 1
*   Change the header to the cell referring to Senior Debt Tranche 2 
*   Change the links to refer to inputs related to tranche 2 (cells with green fonts are the one coming from Inputs sheet) 

Now you have created all calculation blocks for tranche 2. Go over them again to make sure that you have done all the links and there are no links to inputs from tranche 1 in tranche 2. 

And repeat the same thing for tranche 3. 

1.  You need to now make the links to the financial statements and sources and uses of funds. 

*   Interest during constructions and fees should go to the sources and uses of funds statement
*   Interest during repayment and principal repayments should go to calculation of Debt ratios as well as link to financial statements 
*   Ending balances should go to your balance sheet 
*   And checks should go to your master check sheet. 

However instead of individually linking these cash flows, i create another calculation block I call “Summary Senior Debt” and for each of these flows, I make the sum of the 3 tranches and link the sum to the relevant statements and calculation blocks, this way next time if I add a 4th tranche, I just need to include it in the summary debt calculations and trust me you’ll have less trouble balancing your balance sheet. 

![](https://www.finexmod.com/wp-content/uploads/2021/01/6Multiple-tranches-5.png)

This was not easy for me to explain, I hope all these made sense. I also made a video explaining the same, you can check it out here. 

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-01-19T08:35:47+00:00January 19th, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fadding-multiple-tranches-of-debt-in-a-project-finance-model%2F&t=Adding%20Multiple%20Tranches%20of%20Debt%20in%20a%20Project%20Finance%20Model "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fadding-multiple-tranches-of-debt-in-a-project-finance-model%2F&text=Adding%20Multiple%20Tranches%20of%20Debt%20in%20a%20Project%20Finance%20Model "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/adding-multiple-tranches-of-debt-in-a-project-finance-model/&title=Adding%20Multiple%20Tranches%20of%20Debt%20in%20a%20Project%20Finance%20Model "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fadding-multiple-tranches-of-debt-in-a-project-finance-model%2F&title=Adding%20Multiple%20Tranches%20of%20Debt%20in%20a%20Project%20Finance%20Model&summary=When%20you%20are%20at%20the%20early%20stage%20of%20the%20appraisal%20of%20a%20project%20finance%20deal%20and%20you%20haven%27t%20yet%20approached%20any%20lenders%2C%20you%20might%20only%20need%20to%20model%20one%20tranche%20of%20debt%20in%20your%20project%20finance%20model.%20As%20you%20progress%20with%20the%20project%20and%20you%20start%20negotiatin "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fadding-multiple-tranches-of-debt-in-a-project-finance-model%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fadding-multiple-tranches-of-debt-in-a-project-finance-model%2F&name=Adding%20Multiple%20Tranches%20of%20Debt%20in%20a%20Project%20Finance%20Model&description=When%20you%20are%20at%20the%20early%20stage%20of%20the%20appraisal%20of%20a%20project%20finance%20deal%20and%20you%20haven%26%2339%3Bt%20yet%20approached%20any%20lenders%2C%20you%20might%20only%20need%20to%20model%20one%20tranche%20of%20debt%20in%20your%20project%20finance%20model.%20As%20you%20progress%20with%20the%20project%20and%20you%20start%20negotiating%20with%20different%20banks%2C%20you%20will%20need "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fadding-multiple-tranches-of-debt-in-a-project-finance-model%2F&description=When%20you%20are%20at%20the%20early%20stage%20of%20the%20appraisal%20of%20a%20project%20finance%20deal%20and%20you%20haven%26%2339%3Bt%20yet%20approached%20any%20lenders%2C%20you%20might%20only%20need%20to%20model%20one%20tranche%20of%20debt%20in%20your%20project%20finance%20model.%20As%20you%20progress%20with%20the%20project%20and%20you%20start%20negotiating%20with%20different%20banks%2C%20you%20will%20need&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F01%2FMultiple-tranches-cover2.png "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fadding-multiple-tranches-of-debt-in-a-project-finance-model%2F&title=Adding%20Multiple%20Tranches%20of%20Debt%20in%20a%20Project%20Finance%20Model&description=When%20you%20are%20at%20the%20early%20stage%20of%20the%20appraisal%20of%20a%20project%20finance%20deal%20and%20you%20haven%26%2339%3Bt%20yet%20approached%20any%20lenders%2C%20you%20might%20only%20need%20to%20model%20one%20tranche%20of%20debt%20in%20your%20project%20finance%20model.%20As%20you%20progress%20with%20the%20project%20and%20you%20start%20negotiating%20with%20different%20banks%2C%20you%20will%20need "Vk")
[Email](mailto:?body=https://www.finexmod.com/adding-multiple-tranches-of-debt-in-a-project-finance-model/&subject=Adding%20Multiple%20Tranches%20of%20Debt%20in%20a%20Project%20Finance%20Model "Email")

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

![The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/adding-multiple-tranches-of-debt-in-a-project-finance-model)

[](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/)

#### [The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/ "The Art of Structuring Project Finance Models: A Personal Journey")

April 10th, 2025

[Page load link](https://www.finexmod.com/adding-multiple-tranches-of-debt-in-a-project-finance-model#)

[Go to Top](https://www.finexmod.com/adding-multiple-tranches-of-debt-in-a-project-finance-model#)