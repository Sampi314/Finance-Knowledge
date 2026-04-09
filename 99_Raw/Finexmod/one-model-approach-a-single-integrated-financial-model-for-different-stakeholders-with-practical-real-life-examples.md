# One Model Approach: A Single Integrated financial model for different stakeholders with Practical Real Life Examples – Finexmod

**Source:** https://www.finexmod.com/one-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples

---

[Skip to content](https://www.finexmod.com/one-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples#content)

One Model Approach: A Single Integrated financial model for different stakeholders with Practical Real Life Examples

If you ever had to deal with 2 separate financial models for one deal, you know how hard it is to aligne those two models. I not talking about different versions of the same model but two completely different models with different model mechanics.

I had to deal with this issue once in my life back in 2013. I was working as part of the appraisal team for lenders for a mega project. The project was at a quite advanced stage and was almost about to close. The one remaining issue was to come up with a Minimum Revenue Guarabntee mechanism, and we needed to run some MonteCarlo simulations to come up with that mechanism. The existing model which was also edited and accepted by all parties could not be used for running Monte Carlo simulation. It had different blocks using copy and paste macro. Doing a simple change and running the macro was taking 4 to 5 minutes to run. So imagine running at least 500 simulations to get a reasonably well defined distribution was impossible.

So as lenders we decided to build our own version of the model. I had to first build a standard model while minimizing the copy and paste macro to one for financing only. Then after rebuilding the model, I had to do a line by line comparison of my model with the original model to make sure that we are getting the same results under the base case. Any time we receiving a new model from sponsors, I had to repeat the same process and understand what were the changes and try again align the two model. So since then, at least when I am building a model, first of all, I make sure that the model is compliant with best practices and also can be easily used by different stakeholders without a needs to have a seperate model for each party involved in the deal.

If I want to summarize the ideas and tricks that enables me to have this quality in my model, it will in 3 steps:

### Step 1: Present Inputs in form of Scenarios

*   The layout of the “Inputs” sheet should be designed in such a way to enable the user to run multiple scenarios.
*   For example, differentiate between Sponsor, lenders base case and dedicate column J for sponsor base case assumptions and column K for lenders base case.

![](https://www.finexmod.com/wp-content/uploads/2020/11/Picture1.png)

### Step 2: Hybrid sheets

*   Hybrid sheet is a single sheet that contains inputs, calculations and output
*   It’s not a stand-alone sheet and it is linked to the model but you can just remove from the model and it will not have any impact on other sheets within your model.

![](https://www.finexmod.com/wp-content/uploads/2020/11/Picture2.png)

### Step 3: Use Ed’s Scenario reported to swiftly generate a report comparing different scenarios

The scenario reporter created and shared by Edward Bodmer allows you to record multiple scenarios in a sheet in an automatic fashion.

Download Ed’s tool from [here.](https://www.eloquens.com/tool/24amSX1n/finance/scenario-analysis-excel-templates-and-models/how-to-use-the-scenario-reporter?ref=FinExMod)

![](https://www.finexmod.com/wp-content/uploads/2020/11/3.jpg)

What are the benefits of One Model Approach

![](https://www.finexmod.com/wp-content/uploads/2020/11/4-1.jpg)

Now let’s look at 2 practical example using the One Model Approach

### **Case 1: EPC Bid evaluation**

Let’s say you received 4 offers from 4 different EPC contractors and here’s the summary of the EPC offers:

![](https://www.finexmod.com/wp-content/uploads/2020/11/5.jpg)

As part of financial evaluation of the EPC offers, you are asked to plug in the above parameters into your financial model and report to your management what are the total project cost, Equity IRR and minimum DSCR under each of the above offers.

If you don’t use the one model approach, you need to plug in the Bidder 1 offer in the model and save it under another name, repeat the same for teh other bidder so you’ll have 4 model version. You can avoid this by simply using the one model approach.

So following the step, you first need to present your inputs in form of scenario analysis and make sure you have at least 4 columns.

![](https://www.finexmod.com/wp-content/uploads/2020/11/6.png)

Once you have the set up for the inputs you simply input the parameters as per the table for each bidder.

Then use the scenario reporter (edbodmer.com) to record different scenarios.

![](https://www.finexmod.com/wp-content/uploads/2020/11/7-1.jpg)

Then you have a solid base to take to your management for discussion on the selection of the EPC.

### Case 2: Lender versus sponsor base case

Let’s say that you are working as a financial modeller for lenders and you have received the following table from your task manager asking you to change the following parameters and present it as the lenders base case and compare the main project metrics under sponsor versus lenders case.

![](https://www.finexmod.com/wp-content/uploads/2020/11/8.jpg)

Of course you can save the model under another name and change the inputs. However for comparison sake, it is easier to build the Inputs in form of scenarios and have both scenarios together within the same file.

Hopefully the model you have received a standard model and you have dedicated sheet of all inputs going into the model. If the inputs are not presented in form of scenarios, you simply build it in the model by adding columns and using the index/match function to pick up the selected scenario.

![](https://www.finexmod.com/wp-content/uploads/2020/11/9.jpg)

Now using Ed’s scenario reported, you can easily generate the comparison table.

![](https://www.finexmod.com/wp-content/uploads/2020/11/10.jpg)

I hope you found this post useful. Also make sure you check out my two related YouTube videos and if you like what I do, please consider subscribing to both my YouTube Channel and on my blog. This way we’ll be in touch.

In the meantime, happy modeling.

Hedieh

[](https://www.finexmod.com/one-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples#)

[](https://www.finexmod.com/one-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples#)

[Hedieh Kianyfard](https://www.finexmod.com/author/hedi/ "Posts by Hedieh Kianyfard")
2020-11-09T14:56:23+00:00November 9th, 2020|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fone-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples%2F&t=One%20Model%20Approach%3A%20A%20Single%20Integrated%20financial%20model%20for%20different%20stakeholders%20with%20Practical%20Real%20Life%20Examples "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fone-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples%2F&text=One%20Model%20Approach%3A%20A%20Single%20Integrated%20financial%20model%20for%20different%20stakeholders%20with%20Practical%20Real%20Life%20Examples "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/one-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples/&title=One%20Model%20Approach%3A%20A%20Single%20Integrated%20financial%20model%20for%20different%20stakeholders%20with%20Practical%20Real%20Life%20Examples "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fone-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples%2F&title=One%20Model%20Approach%3A%20A%20Single%20Integrated%20financial%20model%20for%20different%20stakeholders%20with%20Practical%20Real%20Life%20Examples&summary=If%20you%20ever%20had%20to%20deal%20with%202%20separate%20financial%20models%20for%20one%20deal%2C%20you%20know%20how%20hard%20it%20is%20to%20aligne%20those%20two%20models.%20I%20not%20talking%20about%20different%20versions%20of%20the%20same%20model%20but%20two%20completely%20different%20models%20with%20different%20model%20mechanics.%0D%0AI%20had%20t "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fone-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fone-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples%2F&name=One%20Model%20Approach%3A%20A%20Single%20Integrated%20financial%20model%20for%20different%20stakeholders%20with%20Practical%20Real%20Life%20Examples&description=If%20you%20ever%20had%20to%20deal%20with%202%20separate%20financial%20models%20for%20one%20deal%2C%20you%20know%20how%20hard%20it%20is%20to%20aligne%20those%20two%20models.%20I%20not%20talking%20about%20different%20versions%20of%20the%20same%20model%20but%20two%20completely%20different%20models%20with%20different%20model%20mechanics.%0D%0AI%20had%20to%20deal%20with%20this%20issue%20once%20in%20my%20life%20back "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fone-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples%2F&description=If%20you%20ever%20had%20to%20deal%20with%202%20separate%20financial%20models%20for%20one%20deal%2C%20you%20know%20how%20hard%20it%20is%20to%20aligne%20those%20two%20models.%20I%20not%20talking%20about%20different%20versions%20of%20the%20same%20model%20but%20two%20completely%20different%20models%20with%20different%20model%20mechanics.%0D%0AI%20had%20to%20deal%20with%20this%20issue%20once%20in%20my%20life%20back&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2020%2F11%2Fcover.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fone-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples%2F&title=One%20Model%20Approach%3A%20A%20Single%20Integrated%20financial%20model%20for%20different%20stakeholders%20with%20Practical%20Real%20Life%20Examples&description=If%20you%20ever%20had%20to%20deal%20with%202%20separate%20financial%20models%20for%20one%20deal%2C%20you%20know%20how%20hard%20it%20is%20to%20aligne%20those%20two%20models.%20I%20not%20talking%20about%20different%20versions%20of%20the%20same%20model%20but%20two%20completely%20different%20models%20with%20different%20model%20mechanics.%0D%0AI%20had%20to%20deal%20with%20this%20issue%20once%20in%20my%20life%20back "Vk")
[Email](mailto:?body=https://www.finexmod.com/one-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples/&subject=One%20Model%20Approach%3A%20A%20Single%20Integrated%20financial%20model%20for%20different%20stakeholders%20with%20Practical%20Real%20Life%20Examples "Email")

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

[Page load link](https://www.finexmod.com/one-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples#)

[Go to Top](https://www.finexmod.com/one-model-approach-a-single-integrated-financial-model-for-different-stakeholders-with-practical-real-life-examples#)