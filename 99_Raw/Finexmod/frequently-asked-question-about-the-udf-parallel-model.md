# Frequently asked question about the UDF parallel model – Finexmod

**Source:** https://www.finexmod.com/frequently-asked-question-about-the-udf-parallel-model

---

[Skip to content](https://www.finexmod.com/frequently-asked-question-about-the-udf-parallel-model#content)

Frequently asked question about the UDF parallel model

I have been talking about Professor Edward Bodmer’s parallel model to you since 2018 and I explained to you in a post about my journey meeting with Professor Edward Bodmer and leanining his technique that he now calls “Parallel model”. You can read the related article on my Linkedin Channel link below:

[https://www.linkedin.com/pulse/how-i-stopped-being-copy-paster-hedieh-kianyfard](https://www.linkedin.com/pulse/how-i-stopped-being-copy-paster-hedieh-kianyfard)

![](https://www.finexmod.com/wp-content/uploads/2022/08/copy-and-paster.jpg)

Today I want to answer some of the commonly questions I get when I talk about Ed’s parallel model:

**Q1: What is a parallel model?**

The parallel model technique is a user defined function that solves the circular references problem that in project finance models. The standard practice to resolve for circular reference is to use a copy and paste code. The copy and paste technique comes with its own problems as it creates a need to run the copy and paste codes anytime you change any inputs in the model and therefore making the model slow.

**Q2: Who made it?**

The UDF parallel model concept is developed by Professor Edward Bodmer. I personally learned about it from Professor Edward Bodmer’s book [Corporate and Project Finance Modeling: Theory and Practice](https://www.amazon.com/Corporate-Project-Finance-Modeling-Practice/dp/1118854365)
 published in 2014. Throughout the years he improved the concept and made it more user friendly.

**Q3: What does it solve for?**

the conventional copy and paste method to resolve for circular reference makes project finance models slow to run. with complex model that contains multiple tranches of debt, debt sizing, refinancing, P90 and P50 case, using the copy and paste method becomes timely. The time declined using the copy and paste method as compared to the UDF parallel model can be reduced in some cases by a factor of like 10 times.

It also helps to audit your model. The output sheet in the parallel model which is a UDF function provides the sources and uses of funds and the debt service on periodic basis. A verification can be made to compare the calculations in the model with the output of the UDF. Most of the time if there’s a mismatch between the two, the problem is in the main model and you can detect issues in your model by comparing the results of the UDF with your own calculations and formulas.

**Q4: Is it an Excel add-in? How can it be integrated with Excel?**

The UDF parallel model is composed of two worksheets and a VBA project containing multiple modules. You can transfer the 2 worksheets together with the VBA modules with a click of a button created by Professor Bodmer. Once the parallel model is included within your project finance model, then you just need to make the links in the “UDF Input” sheet and get the results you need in the “UDF Output” sheet. Once you have done that, you need to link the lines in your model that are causing circular reference to the “UDF output results”. In short, it is like an implant. You insert it, link it and it becomes part of your model.

**Q5: Is it difficult to work with the parallel model?**

It is simple but not easy. It is simple because throughout the years of trial and error and rework of the technique, Professor Bodmer have simplified it to the extent that even if you don’t know VBA, you should be able to understand and work with it. Once you start working with big models containing copy and paste, it will become so difficult to work with such models that you will see it is worth it to take the time to understand this new innovative technique.

**Q6: Does it work with any financial model or are they requirements to take into consideration before inserting the parallel model into the main financial model?**

First the version available today is for project finance models and it works best with models that are created based on best practice financial modeling standards. For example, if your model is not structures meaning you have hard coded inputs within formulas, you don’t have a timeline and necessary flags and counters, you have duplicate calculation blocks, then you first need to restructure your own model and then insert the UDF.

**Q7: Do I require to know VBA in order to be able to work with the parallel model?**

No. Let me ask you so you need to know HTML in order to use the internet? It is the same thing. You can be a pure user of the parallel meaning you insert it, make the links and use. If you need to make changes, then you need to get into the VBA project and with couple of steps make the necessary changes you need. The process of making changes to the code is not easy but follows some simple steps.

Q8: where can I find more information on the parallel model?

You can download the parallel model from Professor Edward Bodmer’s website at

[https://edbodmer.com/template-circular-reference-solution-a-real-innovation-in-project-finance-models/](https://edbodmer.com/template-circular-reference-solution-a-real-innovation-in-project-finance-models/)

You can also send an email to either me at **h.kianyfard@finexmod.com** or to professor Bodmer at **edwardbodmer@gmail.com**

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2022-08-19T12:30:26+00:00August 19th, 2022|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Ffrequently-asked-question-about-the-udf-parallel-model%2F&t=Frequently%20asked%20question%20about%20the%20UDF%20parallel%20model "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Ffrequently-asked-question-about-the-udf-parallel-model%2F&text=Frequently%20asked%20question%20about%20the%20UDF%20parallel%20model "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/frequently-asked-question-about-the-udf-parallel-model/&title=Frequently%20asked%20question%20about%20the%20UDF%20parallel%20model "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Ffrequently-asked-question-about-the-udf-parallel-model%2F&title=Frequently%20asked%20question%20about%20the%20UDF%20parallel%20model&summary=I%20have%20been%20talking%20about%20Professor%20Edward%20Bodmer%27s%20parallel%20model%20to%20you%20since%202018%20and%20I%20explained%20to%20you%20in%20a%20post%20about%20my%20journey%20meeting%20with%20Professor%20Edward%20Bodmer%20and%20leanining%20his%20technique%20that%20he%20now%20calls%20%22Parallel%20model%22.%20You%20can%20read%20the%20rel "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Ffrequently-asked-question-about-the-udf-parallel-model%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Ffrequently-asked-question-about-the-udf-parallel-model%2F&name=Frequently%20asked%20question%20about%20the%20UDF%20parallel%20model&description=I%20have%20been%20talking%20about%20Professor%20Edward%20Bodmer%26%2339%3Bs%20parallel%20model%20to%20you%20since%202018%20and%20I%20explained%20to%20you%20in%20a%20post%20about%20my%20journey%20meeting%20with%20Professor%20Edward%20Bodmer%20and%20leanining%20his%20technique%20that%20he%20now%20calls%20%26quot%3BParallel%20model%26quot%3B.%20You%20can%20read%20the%20related%20article%20on%20my%20Linkedin%20Channel%20link%20below%3A "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Ffrequently-asked-question-about-the-udf-parallel-model%2F&description=I%20have%20been%20talking%20about%20Professor%20Edward%20Bodmer%26%2339%3Bs%20parallel%20model%20to%20you%20since%202018%20and%20I%20explained%20to%20you%20in%20a%20post%20about%20my%20journey%20meeting%20with%20Professor%20Edward%20Bodmer%20and%20leanining%20his%20technique%20that%20he%20now%20calls%20%26quot%3BParallel%20model%26quot%3B.%20You%20can%20read%20the%20related%20article%20on%20my%20Linkedin%20Channel%20link%20below%3A&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2022%2F08%2FCOver-UDF-Parallel-QA-1.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Ffrequently-asked-question-about-the-udf-parallel-model%2F&title=Frequently%20asked%20question%20about%20the%20UDF%20parallel%20model&description=I%20have%20been%20talking%20about%20Professor%20Edward%20Bodmer%26%2339%3Bs%20parallel%20model%20to%20you%20since%202018%20and%20I%20explained%20to%20you%20in%20a%20post%20about%20my%20journey%20meeting%20with%20Professor%20Edward%20Bodmer%20and%20leanining%20his%20technique%20that%20he%20now%20calls%20%26quot%3BParallel%20model%26quot%3B.%20You%20can%20read%20the%20related%20article%20on%20my%20Linkedin%20Channel%20link%20below%3A "Vk")
[Email](mailto:?body=https://www.finexmod.com/frequently-asked-question-about-the-udf-parallel-model/&subject=Frequently%20asked%20question%20about%20the%20UDF%20parallel%20model "Email")

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

[Page load link](https://www.finexmod.com/frequently-asked-question-about-the-udf-parallel-model#)

[Go to Top](https://www.finexmod.com/frequently-asked-question-about-the-udf-parallel-model#)