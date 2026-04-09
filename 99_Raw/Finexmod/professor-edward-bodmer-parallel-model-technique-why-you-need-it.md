# Professor Edward Bodmer Parallel model technique: Why you need it? – Finexmod

**Source:** https://www.finexmod.com/professor-edward-bodmer-parallel-model-technique-why-you-need-it

---

[Skip to content](https://www.finexmod.com/professor-edward-bodmer-parallel-model-technique-why-you-need-it#content)

Professor Edward Bodmer Parallel model technique: Why you need it?

In my previous post, I answered the frequently asked questions about the UDF parallel model.

In this post, I will take you through a typical project finance model and show you how things can get ugly and difficult when you are dealing with a model with multiple copy and paste codes.

First of all, I am working with a standard model which is in compliance with the fundamental rules of financial modeling.

1.  Circular reference in sources and uses of funds:
2.  Circular Reference in Taxes
3.  Circular reference in debt sizing using CFADS
4.  Circular reference in debt sculpting

In order to solve the circular reference problems above, I have created 6 copy and paste modules.

![](https://www.finexmod.com/wp-content/uploads/2022/08/Image-copy-paste-codes.jpg)

I then created a global copy and paste macro code that runs all the copy and paste codes until there’s no difference between the calculated lines and the pasted as values lines.

![](https://www.finexmod.com/wp-content/uploads/2022/08/Image-copy-paste-code-all.jpg)

When I run the global copy and paste macro it takes almost 15 seconds for the macro to run.

[https://www.finexmod.com/wp-content/uploads/2022/08/2022-08-23\_10-04-46.mp4](https://www.finexmod.com/wp-content/uploads/2022/08/2022-08-23_10-04-46.mp4)

When I am in meeting and use the model to run scenarios live with other people, I disactivate the debt sculpting and debt sizing copy and paste macros so that the model runs faster. If however, I need to run a scenario using debt sizing then I need to ask my audience to either be patient or tell them that I will do it later and give them the results after the meeting.

For me this is a problem. Also this is not the most complex model, if I include re-financing, Bridge loan, shareholder loan, cash sweep, stand by debt and other calculation blocks then there will be a need for more copy and paste macros.

For every problem, there’s a solution and if you can’t find a solution yourself, you should find someone who has found the solution. In this case, when we all were happily pressing our copy and paste buttons. professor Edward Bodmer back in the early 2000 realized that there’s a problem and started developing a solution. His solution is to create a User Defined function that can do the calculation in VBA with a loop and we use the function in our excel model.

In the next post, I will show you how to insert the UDF parallel model in the same financial model that we went through together in this post.

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2022-08-23T08:39:47+00:00August 22nd, 2022|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fprofessor-edward-bodmer-parallel-model-technique-why-you-need-it%2F&t=Professor%20Edward%20Bodmer%20Parallel%20model%20technique%3A%20Why%20you%20need%20it%3F "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fprofessor-edward-bodmer-parallel-model-technique-why-you-need-it%2F&text=Professor%20Edward%20Bodmer%20Parallel%20model%20technique%3A%20Why%20you%20need%20it%3F "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/professor-edward-bodmer-parallel-model-technique-why-you-need-it/&title=Professor%20Edward%20Bodmer%20Parallel%20model%20technique%3A%20Why%20you%20need%20it%3F "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fprofessor-edward-bodmer-parallel-model-technique-why-you-need-it%2F&title=Professor%20Edward%20Bodmer%20Parallel%20model%20technique%3A%20Why%20you%20need%20it%3F&summary=In%20my%20previous%20post%2C%20I%20answered%20the%20frequently%20asked%20questions%20about%20the%20UDF%20parallel%20model.%0D%0A%0D%0AIn%20this%20post%2C%20I%20will%20take%20you%20through%20a%20typical%20project%20finance%20model%20and%20show%20you%20how%20things%20can%20get%20ugly%20and%20difficult%20when%20you%20are%20dealing%20with%20a%20model%20with%20 "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fprofessor-edward-bodmer-parallel-model-technique-why-you-need-it%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fprofessor-edward-bodmer-parallel-model-technique-why-you-need-it%2F&name=Professor%20Edward%20Bodmer%20Parallel%20model%20technique%3A%20Why%20you%20need%20it%3F&description=In%20my%20previous%20post%2C%20I%20answered%20the%20frequently%20asked%20questions%20about%20the%20UDF%20parallel%20model.%0D%0A%0D%0AIn%20this%20post%2C%20I%20will%20take%20you%20through%20a%20typical%20project%20finance%20model%20and%20show%20you%20how%20things%20can%20get%20ugly%20and%20difficult%20when%20you%20are%20dealing%20with%20a%20model%20with%20multiple%20copy%20and%20paste%20codes.%0D%0A%0D%0AFirst%20of%20all%2C%20I%20am%20working "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fprofessor-edward-bodmer-parallel-model-technique-why-you-need-it%2F&description=In%20my%20previous%20post%2C%20I%20answered%20the%20frequently%20asked%20questions%20about%20the%20UDF%20parallel%20model.%0D%0A%0D%0AIn%20this%20post%2C%20I%20will%20take%20you%20through%20a%20typical%20project%20finance%20model%20and%20show%20you%20how%20things%20can%20get%20ugly%20and%20difficult%20when%20you%20are%20dealing%20with%20a%20model%20with%20multiple%20copy%20and%20paste%20codes.%0D%0A%0D%0AFirst%20of%20all%2C%20I%20am%20working&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2022%2F08%2FCOver-UDF-Parallel-why.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fprofessor-edward-bodmer-parallel-model-technique-why-you-need-it%2F&title=Professor%20Edward%20Bodmer%20Parallel%20model%20technique%3A%20Why%20you%20need%20it%3F&description=In%20my%20previous%20post%2C%20I%20answered%20the%20frequently%20asked%20questions%20about%20the%20UDF%20parallel%20model.%0D%0A%0D%0AIn%20this%20post%2C%20I%20will%20take%20you%20through%20a%20typical%20project%20finance%20model%20and%20show%20you%20how%20things%20can%20get%20ugly%20and%20difficult%20when%20you%20are%20dealing%20with%20a%20model%20with%20multiple%20copy%20and%20paste%20codes.%0D%0A%0D%0AFirst%20of%20all%2C%20I%20am%20working "Vk")
[Email](mailto:?body=https://www.finexmod.com/professor-edward-bodmer-parallel-model-technique-why-you-need-it/&subject=Professor%20Edward%20Bodmer%20Parallel%20model%20technique%3A%20Why%20you%20need%20it%3F "Email")

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

[Page load link](https://www.finexmod.com/professor-edward-bodmer-parallel-model-technique-why-you-need-it#)

[Go to Top](https://www.finexmod.com/professor-edward-bodmer-parallel-model-technique-why-you-need-it#)