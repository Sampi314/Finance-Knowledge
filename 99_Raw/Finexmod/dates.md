# Key dates in a loan term sheet – Part 1 – Finexmod

**Source:** https://www.finexmod.com/dates

---

[Skip to content](https://www.finexmod.com/dates#content)

Key dates in a loan term sheet – Part 1

In my previous blog post and video, I talked about the importance of building a flexible timeline in a project finance model. You can read it here. There’s also a free to download template.

[https://www.finexmod.com/timeline/](https://www.finexmod.com/timeline/)

In this blog post and accompanying videos I want to go back to the series of discussions I started earlier related to loan term sheet negotiations and how the financial model and a financial modeler can help in the process. Since the financial model is a contractual document referenced in the term sheet, it should reflect the key terms reflected in the loan agreement and key dates are among the important definitions.

![In this blog post and accompanying videos I want to go back to the series of discussions I started earlier related to loan term sheet negotiations and how the financial model and a financial modeler can help in the process. Since the financial model is a contractual document referenced in the termsheet, it should reflect the key terms reflected in the loan agreement and key dates are among the important definitions. ](https://www.finexmod.com/wp-content/uploads/2021/04/dates1.jpg)

As you can see from the above extract from a real loan agreement, the financial model is referenced in the loan term sheet and the base case financial model assumptions is annexed to the agreement.

So here I want to mix the two topics of key timeline in project financial model with the issues related to loan term sheet agreement. If you search for the word “Date” in a contract you’ll find many dates that are references in the agreements so I’ll have to make a part 2 or maybe even 3. Let’s see but now let’s start with the Signing date.

![the Commercial Operations Date As the name says, it’s the date on which the commercial operation of the project occurs. If the project is under a concession or has signed any sort of purchase agreement then the definition might refer to the contract between the purchaser and the project. Example from a real loan contract:](https://www.finexmod.com/wp-content/uploads/2021/04/dates2-1.jpg)

**Singing date:**
-----------------

### Definition and Notes:

*   This is the date when the parties involved celebrate the achievement of a big milestone which can lead to a financial close date that will be discussed next. It’s the date that parties sign the loan agreement.
*   Typically the availability period is counted starting from the signing date up. That is why all parties push for a short time lag between signature and financial close date which allows for drawdown on facilities. We will see the definition of financial close in the next sections.
*   Some of the fees like up-front fees and commitment fees might be payable at signature date or a number of days after signature date.

Extract from Loan term sheet:

![Extract from Loan term sheet: ](https://www.finexmod.com/wp-content/uploads/2021/04/dates3.jpg)

How to use it in the financial model?

*   Need to be reflected in the key dates for debt tranches included in the financial model
*   Some fees like up-front fees and commitment fees might be payable from this date. However it’s a subject of negotiation. In some cases, fees are due at financial close.
*   Typically the final maturity date and availability period are calculated from the signing date.

![How to use it in the financial model? Need to be reflected in the key dates for debt tranches included in the financial model Some fees like up-front fees and commitment fees might be payable from this date. However it’s a subject of negotiation. In some cases, fees are due at financial close. Typically the final maturity date and availability period are calculated from the signing date. ](https://www.finexmod.com/wp-content/uploads/2021/04/dates4.jpg)

**Financial Close date**
------------------------

Definition and Notes:

*   The date on which all conditions have been fulfilled; all documents have been executed, and all contracts come into effect.
*   After the financial close, drawdowns are allowed.
*   It’s also known as “Effective date”.
*   At this date parties freeze the base case financial model and the construction budget and operating budget reflected in the reference model at financial close are the reference for sizing the financing instrument and determination of max commitments. Any deviation from this budget will be considered as “Increase costs” and will have consequences.

Extract from an a real project loan agreement:

![Financial Close date Definition and Notes: The date on which all conditions have been fulfilled; all documents have been executed, and all contracts come into effect. After the financial close, drawdowns are allowed. It’s also known as “Effective date” At this date parties freeze the base case financial model and the construction budget and operating budget reflected in the reference model at financial close are the reference for sizing the financing instrument and determination of max commitments. Any deviation from this budget will be considered as “Increase costs” and will have consequences. Extract from an a real project loan agreement: ](https://www.finexmod.com/wp-content/uploads/2021/04/dates5.jpg)

As you can see the definition refers to another clause in the agreement and that clause itself refers to a schedule in the annex with a very long list of requirements for first disbursement or financial close.

How to use this date in the model?

*   It should be reflected in the timing assumptions and the construction start date or drawdown start date should be at or after financial close date.

![As you can see the definition refers to another clause in the agreement and that clause itself refers to a schedule in the annex with a very long list of requirements for first disbursement or financial close. How to use this date in the model? It should be reflected in the timing assumptions and the construction start date or drawdown start date should be at or after financial close date. ](https://www.finexmod.com/wp-content/uploads/2021/04/dates6.jpg)

*   Some of the lenders fees like up-front fees and commitment fees might be payable at or from financial close date. So you need to make the link when calculating these fees.

**the Commercial Operations Date**
----------------------------------

Definition and Notes:

As the name says, it’s the date on which the commercial operation of the project occurs. If the project is under a concession or has signed any sort of purchase agreement then the definition might refer to the contract between the purchaser and the project.

Example from a real loan contract:

![the Commercial Operations Date As the name says, it’s the date on which the commercial operation of the project occurs. If the project is under a concession or has signed any sort of purchase agreement then the definition might refer to the contract between the purchaser and the project. Example from a real loan contract: ](https://www.finexmod.com/wp-content/uploads/2021/04/dates7.jpg)

How to reflect and use this date in the model?

*   It should be reflected in the timing assumptions and linked to calculation of operation flag and counters.

![How to reflect and use this date in the model? It should be reflected in the timing assumptions and linked to calculation of operation flag and counters. ](https://www.finexmod.com/wp-content/uploads/2021/04/dates8.jpg)

**The Technical Completion Date**
---------------------------------

Definition and Notes:

*   Also known as “Physical Completion Date” or simply “Completion Date”
*   Scheduled completion dates occurs or defined as 3 to 6 months of scheduled commercial operation date

Example from a real loan contract:

![the Commercial Operations Date As the name says, it’s the date on which the commercial operation of the project occurs. If the project is under a concession or has signed any sort of purchase agreement then the definition might refer to the contract between the purchaser and the project. Example from a real loan contract:](https://www.finexmod.com/wp-content/uploads/2021/04/dates9.jpg)

How to reflect and use this date in the model?

I don’t see how this date can be used in the model. I have never reflected it in my models. However, you need to check if any fees or any financial tests are due at this date then you need to include it in the financial model.

**The Financial Completion Date**
---------------------------------

Definition and Notes:

*   The financial completion date should be after the technical completion date
*   Typically the release of sponsor support and the payment of any distributions including repayment of shareholder loans are permitted after the financial completion date.
*   For some deals, there may not be a separate Financial Completion concept but just one under completion date.
*   This is a date where financier test the technical and financial performance of the project to make sure that the base case is still valid meaning everything goes as scheduled and that there are no abnormalities
*   a rerun of an updated financial model with revised assumptions is performed at this date and DSCR and LLCR test are performed based on the new model version.

Example from a real loan contract:

![the Commercial Operations Date As the name says, it’s the date on which the commercial operation of the project occurs. If the project is under a concession or has signed any sort of purchase agreement then the definition might refer to the contract between the purchaser and the project. Example from a real loan contract:](https://www.finexmod.com/wp-content/uploads/2021/04/dates10.jpg)

There’s a long list of requirement and tests attached to this date and reported in the term sheet under the definition of financial completion date. These requirements are project specific but the below terms are common among these requirements.

*   Technical Completion Date has occurred
*   the First Repayment Date under each Loan has occurred
*   the Debt to Equity Ratio as at Financial Completion Date does not exceed the maximum gearing defined in the term sheet (for example 75:25)

How to reflect and use this date in the model?

Unless the DSCR and LLCR criteria at the financial completion date is different than the financial ratios that monitored throughout the life of loans, there’s no necessity to include this date in the model however it’s still useful to report the ratios at the financial completion date in the dashboard.

![the Commercial Operations Date As the name says, it’s the date on which the commercial operation of the project occurs. If the project is under a concession or has signed any sort of purchase agreement then the definition might refer to the contract between the purchaser and the project. Example from a real loan contract:](https://www.finexmod.com/wp-content/uploads/2021/04/dates11.jpg)

Be sure to also watch our accompanying video tutorial:

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-04-21T06:49:15+00:00April 20th, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fdates%2F&t=Key%20dates%20in%20a%20loan%20term%20sheet%20%E2%80%93%20Part%201 "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fdates%2F&text=Key%20dates%20in%20a%20loan%20term%20sheet%20%E2%80%93%20Part%201 "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/dates/&title=Key%20dates%20in%20a%20loan%20term%20sheet%20%E2%80%93%20Part%201 "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fdates%2F&title=Key%20dates%20in%20a%20loan%20term%20sheet%20%E2%80%93%20Part%201&summary=In%20my%20previous%20blog%20post%20and%20video%2C%20I%20talked%20about%20the%20importance%20of%20building%20a%20flexible%20timeline%20in%20a%20project%20finance%20model.%20You%20can%20read%20it%20here.%20There%E2%80%99s%20also%20a%20free%20to%20download%20template.%20%0Ahttps%3A%2F%2Fwww.finexmod.com%2Ftimeline%2F%0AIn%20this%20blog%20post%20and%20accompan "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fdates%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fdates%2F&name=Key%20dates%20in%20a%20loan%20term%20sheet%20%E2%80%93%20Part%201&description=In%20my%20previous%20blog%20post%20and%20video%2C%20I%20talked%20about%20the%20importance%20of%20building%20a%20flexible%20timeline%20in%20a%20project%20finance%20model.%20You%20can%20read%20it%20here.%20There%E2%80%99s%20also%20a%20free%20to%20download%20template.%20%0Ahttps%3A%2F%2Fwww.finexmod.com%2Ftimeline%2F%0AIn%20this%20blog%20post%20and%20accompanying%20videos%20I%20want%20to%20go%20back%20to%20the "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fdates%2F&description=In%20my%20previous%20blog%20post%20and%20video%2C%20I%20talked%20about%20the%20importance%20of%20building%20a%20flexible%20timeline%20in%20a%20project%20finance%20model.%20You%20can%20read%20it%20here.%20There%E2%80%99s%20also%20a%20free%20to%20download%20template.%20%0Ahttps%3A%2F%2Fwww.finexmod.com%2Ftimeline%2F%0AIn%20this%20blog%20post%20and%20accompanying%20videos%20I%20want%20to%20go%20back%20to%20the&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F04%2Fcover-dates.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fdates%2F&title=Key%20dates%20in%20a%20loan%20term%20sheet%20%E2%80%93%20Part%201&description=In%20my%20previous%20blog%20post%20and%20video%2C%20I%20talked%20about%20the%20importance%20of%20building%20a%20flexible%20timeline%20in%20a%20project%20finance%20model.%20You%20can%20read%20it%20here.%20There%E2%80%99s%20also%20a%20free%20to%20download%20template.%20%0Ahttps%3A%2F%2Fwww.finexmod.com%2Ftimeline%2F%0AIn%20this%20blog%20post%20and%20accompanying%20videos%20I%20want%20to%20go%20back%20to%20the "Vk")
[Email](mailto:?body=https://www.finexmod.com/dates/&subject=Key%20dates%20in%20a%20loan%20term%20sheet%20%E2%80%93%20Part%201 "Email")

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

[Page load link](https://www.finexmod.com/dates#)

[Go to Top](https://www.finexmod.com/dates#)