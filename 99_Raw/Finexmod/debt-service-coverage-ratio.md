# Debt Service Coverage Ratio in Simple words and different perspective – Finexmod

**Source:** https://www.finexmod.com/debt-service-coverage-ratio

---

[Skip to content](https://www.finexmod.com/debt-service-coverage-ratio#content)

Debt Service Coverage Ratio in Simple words and different perspective

When you see that you’ve got used to a concept, I believe it is important to go back and questions it and have a fresh look at things every once in a while. In my case, I have been working on project finance deals and have dealt with project finance models for more than a decade so I want to go back and have a fresh look at the basic concept and metrics that I deal with on day to day basis. In this post, I want to forget about all I already know about Debt Service Coverage Ratio and put myself in the shoes of someone who is hearing about this concept for the first time.

Me: What is Debt Service Coverage Ratio?

My higher self: It is a debt metrics for lenders to understand and monitor the financial viability of the project from their point of view. It’s an indicator that tells lenders whether the cash in project’s account is sufficient and going to be sufficient in the future to pay back their debt service.

Me: How do I calculate it?

My higher self: The formula is and this is an extract from a project loan agreement.

![](https://www.finexmod.com/wp-content/uploads/2022/05/DSCR-definition-loan-agreement.jpg)

For the nominator, you need to take the cash flow available for debt service (CFADS) and for that you need to take it from the cash flow waterfall statement. Typically the order of a cash flow waterfall is documented in the loan agreement so you know exactly how to get from project revenues to CFADS. I have another blog on cash flow waterfall and a template that I invite you to go and check after this conversation.

Me: You mentioned that the definition is included in the loan agreement so it is contractual, isn’t?

My higher self: yes, you will find the definition in the loan agreement and thresholds will be also defined in the agreement. in each milestone for example at signing, at financial completion date, at each disbursement and repayment date, these ratios will be monitored by lenders and minimum requirements needs to be satisfied. Look at the below extracts:

![](https://www.finexmod.com/wp-content/uploads/2022/05/DSCR-ratio-termsheet.jpg)

Me: Ok, so this is useful. It is giving me the formula for calculating this things called DSCR. So in mathematical terms, it is basically the ratio of cash flow that is available to pay for what is due to lenders in each period. But what does it mean? When for example DSCR in the first operating period of the model is 1.5x what does it mean?

My higher self: It means that the ratio of cash flow available for debt service over debt service for that period is 1.5x.

Me: Ok, but you didn’t tell me what it means, you explained how you calculate it! can you explain better?

My higher self: I apologies, that explanation was useless. Let me give you a simple example, if let’s say your CFADS is 100 and you debt service is 50, so what is your DSCR for that period?

Me: 100 divided by 50, it’s 2, 2x.

My higher self: Exactly! This means that you have a cash buffer of around 50%. Meaning that if something unexpected comes up and eats 50% of your cash, then you will be left with just enough cash to cover for your debt service.

Me: but 50% buffer is huge! lenders usually require a minimum periodic DSCR of 1.3x. So let’s me see if I can get this right. So with the way you explained, if lenders say I require to see a 1.3x in your base case model, this means that lenders require a minimum cash buffer of around 23%. It’s like an additional layer of security for them to make sure that even if things go wrong and the project loses up to 23% of its cash, lenders are still getting their money back. right?

My higher self: That’s exactly it.

Me: Perfect. You know I like this concept of interpretation of DSCR as cash buffer and express it in percentage. Where did you learn this?

My higher self: I learned it from Professor Edward Bodmer, here’s the link:

> [LLCR and PLCR Complexities and Meaning for Break Even](https://edbodmer.com/llcr-and-plcr-complexities-and-meaning-for-break-even/)

Me: You know what? I’m going to add this interpretation in my financial model too. Let me show you how:

|     |     |     |
| --- | --- | --- |
|     |     | Exemple: |
| DSCR = CFADS/DS |     | CFADS = 100 |
| CFADS \* α / DS = 1 |     | DS = 77 |
| α  = 1/(CFADS/DS) |     | DSCR =1.3x |
| α  = 1/DSCR |     | α = 1/1.3 = 77% |
| β = 1 – α |     | β = 1 – 77% = 23% |

β: Break-even point: %s decrease in CFADS that is bringing DSCR down to 1x.

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2022-05-27T18:45:59+00:00May 27th, 2022|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fdebt-service-coverage-ratio%2F&t=Debt%20Service%20Coverage%20Ratio%20in%20Simple%20words%20and%20different%20perspective "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fdebt-service-coverage-ratio%2F&text=Debt%20Service%20Coverage%20Ratio%20in%20Simple%20words%20and%20different%20perspective "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/debt-service-coverage-ratio/&title=Debt%20Service%20Coverage%20Ratio%20in%20Simple%20words%20and%20different%20perspective "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fdebt-service-coverage-ratio%2F&title=Debt%20Service%20Coverage%20Ratio%20in%20Simple%20words%20and%20different%20perspective&summary=When%20you%20see%20that%20you%27ve%20got%20used%20to%20a%20concept%2C%20I%20believe%20it%20is%20important%20to%20go%20back%20and%20questions%20it%20and%20have%20a%20fresh%20look%20at%20things%20every%20once%20in%20a%20while.%20In%20my%20case%2C%20I%20have%20been%20working%20on%20project%20finance%20deals%20and%20have%20dealt%20with%20project%20finance%20models "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fdebt-service-coverage-ratio%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fdebt-service-coverage-ratio%2F&name=Debt%20Service%20Coverage%20Ratio%20in%20Simple%20words%20and%20different%20perspective&description=When%20you%20see%20that%20you%26%2339%3Bve%20got%20used%20to%20a%20concept%2C%20I%20believe%20it%20is%20important%20to%20go%20back%20and%20questions%20it%20and%20have%20a%20fresh%20look%20at%20things%20every%20once%20in%20a%20while.%20In%20my%20case%2C%20I%20have%20been%20working%20on%20project%20finance%20deals%20and%20have%20dealt%20with%20project%20finance%20models%20for%20more%20than%20a "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fdebt-service-coverage-ratio%2F&description=When%20you%20see%20that%20you%26%2339%3Bve%20got%20used%20to%20a%20concept%2C%20I%20believe%20it%20is%20important%20to%20go%20back%20and%20questions%20it%20and%20have%20a%20fresh%20look%20at%20things%20every%20once%20in%20a%20while.%20In%20my%20case%2C%20I%20have%20been%20working%20on%20project%20finance%20deals%20and%20have%20dealt%20with%20project%20finance%20models%20for%20more%20than%20a&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2022%2F05%2FDSCR-Cover.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fdebt-service-coverage-ratio%2F&title=Debt%20Service%20Coverage%20Ratio%20in%20Simple%20words%20and%20different%20perspective&description=When%20you%20see%20that%20you%26%2339%3Bve%20got%20used%20to%20a%20concept%2C%20I%20believe%20it%20is%20important%20to%20go%20back%20and%20questions%20it%20and%20have%20a%20fresh%20look%20at%20things%20every%20once%20in%20a%20while.%20In%20my%20case%2C%20I%20have%20been%20working%20on%20project%20finance%20deals%20and%20have%20dealt%20with%20project%20finance%20models%20for%20more%20than%20a "Vk")
[Email](mailto:?body=https://www.finexmod.com/debt-service-coverage-ratio/&subject=Debt%20Service%20Coverage%20Ratio%20in%20Simple%20words%20and%20different%20perspective "Email")

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

[Page load link](https://www.finexmod.com/debt-service-coverage-ratio#)

[Go to Top](https://www.finexmod.com/debt-service-coverage-ratio#)