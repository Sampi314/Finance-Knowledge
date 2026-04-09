# My journey dealing with circular reference in project finance models – Finexmod

**Source:** https://www.finexmod.com/my-journey-dealing-with-circular-reference-in-project-finance-models

---

[Skip to content](https://www.finexmod.com/my-journey-dealing-with-circular-reference-in-project-finance-models#content)

My journey dealing with circular reference in project finance models

A friends asked me to talk about circular reference and since you can only teach what you know, I decided to tell you my experience with circular reference and show you how I deal with it in my project finance models.

![](https://www.finexmod.com/wp-content/uploads/2022/07/message-from-S.jpg)

![](https://www.finexmod.com/wp-content/uploads/2022/07/P1220852_resize.jpg)

When I first started building financial models back in 2007, it was mainly for training purposes. I was working as a trainer for executive programs in Investment Appraisal and risk analysis. Because the focus of the trainings were to teach the concepts and not really the model mechanics, the model templates I was building and using for the trainings did not include any circular references. We were fixing the debt in the case study so that participants could build the sources and uses of funds, sculpt the debt and other simplification not to face circularity in the financial model template.

In 2011, I started working as a consultant at the African Development Bank and was responsible for building and reviewing financial models. The first real project finance model that I reviewed was a complicated financial model with 100+ lines of copy and paste. The project was at an advance stage but there was a need for a risk analysis in order to set up a revenue guarantee mechanism for the project. This was only doable with Monte Carlo simulation but the heavy model with the multiple blocks of copy and paste was not making it possible to run the monte carlo simulation on the model. That is why I was assigned to build a more simplified version of the model and complete the analysis. Long story short, this was the first time that I was exposed to copy and paste. Now that I think about it, it is strange that my first encounter with a model containing copy and paste code was a painful experience so I understood that there’s something significantly wrong with curing this problem using copy and poste. However, at the time, I was busy understanding how deals work in reality and couldn’t think further about the inefficiencies of the copy and paste method and I started applying it in my own project finance model.

I remember clearly the first time I inserted a copy and paste code in my financial model. I first did a recording and stepped into the VBA editor for the first time and looked at the code with astonishment.

Then soon I understood that in order for me to be able to run the macro from any worksheet in the model, I had to create name ranges for my copy and paste ranges and also to include a check and a loop to stop the code and the loop from running when the difference between the fixed and copied amounts are not significant. I was so proud of myself that I created a button in my summary sheet calling it “optimization” and this was doing nothing but copying and pasting. Now that I think about it, I tell myself, how can copy and pasting a cell in values be considered as an optimization? I started experimenting with the buttons and adding a Sun shaped button for solar projects, lightning bolt, adding shadows and fancy colors to the button.

![](https://www.finexmod.com/wp-content/uploads/2022/07/Silly-buttons.gif)

After a while, when I started getting involved in more complex projects and had to build model to reflect the complexity of those deal, I hit the wall. I realized that with the copy and paste, I am not able to use basic excel function like Goal Seek and Data Table. I had to create another macro and call the copy and paste within the Goal Seek and create more copy and paste codes for running sensitivities. Soon my financial models started becoming running slow.

That’s when I started looking for a solution. They say if you are faced with a problem, either you have to come up with a solution or find someone who can come up with a solution for you. That’s how I came across Professor Edward Bodmer’s website and book. I remember the day I discovered his website, I was up all night downloading as many materials as I could but there was no end to it. I was just scared that what if tomorrow all these resources just disappear ? and this was because I could not believe my eyes that someone could so generously share all these precious materials that others were and still today are charging thousand of dollars for, free to public. I read his book and followed his youtube videos to understand his technique for solving the circular reference problem. I understood the basic idea that he is creating a User Defined function which is mimicking the equation in excel and looping it to solve the issue. You just replace your fixed or pasted values with the user defined function. The idea was brilliant and I was so excited to apply it in my own project models. I tried several times but I couldn’t make it. In 2018, I got the privilege to have a one to one training with Professor Bodmer in Istanbul. We took one of my financial models for a project that was ongoing at the time and he made me write the UDF from A to Z. At the time, I only had models with circular reference in the funding plan. This is because I was sizing the debt with the maximum gearing method only so I did not had issue with sizing the debt with future project cash flow. The UDF we wrote together was just reading the inputs related to construction phase, was creating flags and counters to depict construction phase and calculating the total project cost.

This worked for me for 2 years. I started adopting Ed’s code in my other project finance models and I was even comfortable making tweaks and adding variables and calculation blocks to it until I hit the wall again for the second time.

I realized that if I really want to have an optimized model, I need to size the debt with the future cash flow and find the right sculpted profile. This became complicated when I was faced with multiple tranches of debt with different debt terms. That is when I contacted Professor Bodmer again and asked for his help.

I knew that he was working on an extended UDF that covers almost all calculations necessary to get all cash flow items but I weren’t inserting it in my own financial model. It was just in the beginning of the pandemic in 2020 that we started working together again. He took me through the code and explained to me the different blocks. During our communication, he understood that my brain can not process all the information at once. So he broke it down into different modules. He came to me and said:” I see that you and Kenny and many others have certain ways of building your models. You define your inputs and sometime you separate constants inputs from time based inputs. Then you have a seperate worksheets for your calculation blocks and you present your results in separate sheets you call output sheet.” he then showed me the new code which was exactly mimicking the way my excel models are built.

![](https://www.finexmod.com/wp-content/uploads/2022/07/Worksheet-Structure.jpg)

He showed me how I can add a variable and write down the formulas and present output in the UDF. We worked on some real project finance model and everytime we were coming across new issues Ed was adding it to the UDF template. It came to a stage that the UDF was so comprehensive that we realized it can almost match and accommodate the needs of most of my projects. This is when Ed called his technique Parallel model because this is exactly what is. It is a shadow model sitting in your model to help you solve for circular reference, size your debt, sculpt your debt and cross check your excel calculation with the robust formulas included in his code.

![](https://www.finexmod.com/wp-content/uploads/2022/07/UDF-structure.jpg)

Today, where possible I include Ed’s UDF in my project finance model but also provide the ability to user to switch back to copy and paste. Ed also include a switch within the UDF input sheet that can be turned on and off.

I hope you are not disappointed that you learn much about Ed Bodmer’s Parallel technique in this post. My aim was mainly to encourage you to get started with applying Ed’s method into your own project finance models. Me and Ed ar eboth curious to see what you will do with it and how you will be using it in your financial model.

1.  Any change is always accompanied by resistance and most probably some cost.
2.  There is no need for complexity. Actually ,same principals of best practice modeling applicable to financial models also applies to VBA code. You make the code simple, readable, flexible.
3.  Don’t worry about the audit. I am sure reputable model audit firms have people who have knowledge of VBA and can review simple codes.
4.  This method might not be industry norm now but it will be once more people start applying it in their models.

We have done a webinar in the past and Ed explained the basic of his method. We will do more webinar in the future and if you are interested to learn more about it, drop us an email or contact us through social media and let’s discuss it.

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2022-07-06T06:06:14+00:00July 6th, 2022|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fmy-journey-dealing-with-circular-reference-in-project-finance-models%2F&t=My%20journey%20dealing%20with%20circular%20reference%20in%20project%20finance%20models "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fmy-journey-dealing-with-circular-reference-in-project-finance-models%2F&text=My%20journey%20dealing%20with%20circular%20reference%20in%20project%20finance%20models "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/my-journey-dealing-with-circular-reference-in-project-finance-models/&title=My%20journey%20dealing%20with%20circular%20reference%20in%20project%20finance%20models "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fmy-journey-dealing-with-circular-reference-in-project-finance-models%2F&title=My%20journey%20dealing%20with%20circular%20reference%20in%20project%20finance%20models&summary=A%20friends%20asked%20me%20to%20talk%20about%20circular%20reference%20and%20since%20you%20can%20only%20teach%20what%20you%20know%2C%20I%20decided%20to%20tell%20you%20my%20experience%20with%20circular%20reference%20and%20show%20you%20how%20I%20deal%20with%20it%20in%20my%20project%20finance%20models. "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fmy-journey-dealing-with-circular-reference-in-project-finance-models%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fmy-journey-dealing-with-circular-reference-in-project-finance-models%2F&name=My%20journey%20dealing%20with%20circular%20reference%20in%20project%20finance%20models&description=A%20friends%20asked%20me%20to%20talk%20about%20circular%20reference%20and%20since%20you%20can%20only%20teach%20what%20you%20know%2C%20I%20decided%20to%20tell%20you%20my%20experience%20with%20circular%20reference%20and%20show%20you%20how%20I%20deal%20with%20it%20in%20my%20project%20finance%20models. "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fmy-journey-dealing-with-circular-reference-in-project-finance-models%2F&description=A%20friends%20asked%20me%20to%20talk%20about%20circular%20reference%20and%20since%20you%20can%20only%20teach%20what%20you%20know%2C%20I%20decided%20to%20tell%20you%20my%20experience%20with%20circular%20reference%20and%20show%20you%20how%20I%20deal%20with%20it%20in%20my%20project%20finance%20models.&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2022%2F07%2FMy-experience-with-Circular-Reference-cover.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fmy-journey-dealing-with-circular-reference-in-project-finance-models%2F&title=My%20journey%20dealing%20with%20circular%20reference%20in%20project%20finance%20models&description=A%20friends%20asked%20me%20to%20talk%20about%20circular%20reference%20and%20since%20you%20can%20only%20teach%20what%20you%20know%2C%20I%20decided%20to%20tell%20you%20my%20experience%20with%20circular%20reference%20and%20show%20you%20how%20I%20deal%20with%20it%20in%20my%20project%20finance%20models. "Vk")
[Email](mailto:?body=https://www.finexmod.com/my-journey-dealing-with-circular-reference-in-project-finance-models/&subject=My%20journey%20dealing%20with%20circular%20reference%20in%20project%20finance%20models "Email")

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

[Page load link](https://www.finexmod.com/my-journey-dealing-with-circular-reference-in-project-finance-models#)

[Go to Top](https://www.finexmod.com/my-journey-dealing-with-circular-reference-in-project-finance-models#)