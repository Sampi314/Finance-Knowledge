# Key Dates in a Loan Term Sheet – Part 2 – Finexmod

**Source:** https://www.finexmod.com/dates2

---

[Skip to content](https://www.finexmod.com/dates2#content)

Key Dates in a Loan Term Sheet – Part 2

In the previous blog post, I opened up the topic of key dates in a typical project finance loan term sheet. This is part 2 of the same discussion and I will take you through the below terms:

*   Availability Period
*   Calculation Date
*   Payment Date
*   First Repayment Date
*   Final Maturity Date

### ![the Commercial Operations Date As the name says, it’s the date on which the commercial operation of the project occurs. If the project is under a concession or has signed any sort of purchase agreement then the definition might refer to the contract between the purchaser and the project. Example from a real loan contract:](https://www.finexmod.com/wp-content/uploads/2021/04/dates2-1.jpg)

### Availability Period

Definition and Notes:

*   Also called “Validity Period” or “Commitment Period”
*   It’s a period during which a borrower may draw down a loan.
*   Typically it starts from signing date or sometimes from Effective Date ([check my previous blog post](https://www.finexmod.com/dates/)
    ) and end once the project has been completed and becomes fully operational.

Extract from a real Term sheet:

![Key dates in a typical project finance loan term sheet and its application in a project finance model ](https://www.finexmod.com/wp-content/uploads/2021/04/dates21.jpg)

How to use it in the financial model?

I don’t see how to use this information any any of the calculation in the model. Drawdown on facilities are typically modeled throughout the construction phase and typically availability period covers the whole construction phase. I have not come across any availability period shorter than the duration of construction. If you think otherwise or have examples to share, please let me know in the comments.

You can still include it in your inputs but make sure you put a note saying “For information Only” so that auditors and users know that you are aware that the cell containing the availability period is not linked and is idle but it’s intentional.

Payment Date
------------

Definition and Notes:

*   Typically the frequency of debt service is defined under the definition of Payment Date
*   The Payment Dates are defined in a dedicated Schedule under the loan agreements together with the repayment profile (repayment Schedule).
*   Sometimes Payment Date is defined as “Payment Date of Interest” and payment of Principal is defined under “Repayment Date”

Extract from a real Term sheet:

![Key dates in a typical project finance loan term sheet and its application in a project finance model](https://www.finexmod.com/wp-content/uploads/2021/04/dates23.jpg)

How to use it in the financial model?

one of the most critical decision to make when it comes to the financial model structure is the model periodicity. Meaning the number of months to include in each model period. I discuss this in more detail in my blog post on [how to build flexible timeline in your project finance models](https://www.finexmod.com/timeline/)
.

One of the important criteria in determining the periodicity in your financial models should be the frequency of debt service. This is because the debt metrics like historical and projected DSCR and LLCRs are calculated on periodic basis.

I have seen cases where for example the model was built on monthly basis but debt payments and ratios were calculated using a flag enabling for example quarterly payment of debt. This really complicates the model but on the other hand it provide great flexibility. You can allow quarterly repayment for one debt tranche and semi-annual for another.

Regarding the payment dates and payment schedule, the financial model should have flexibility to accommodate a fixed repayment profile. Once the loan is signed, the repayment profile and the repayment dates are fixed and need to be hard-coded in the financial model. During the appraisal stage and before signature, you can build in flexibility in the debt repayment schedule and use mortgage or equal style but once the loan agreement is signed, the payment profile should be hard-coded.

![Project finance loan agreement and the repayment profile and schedule ](https://www.finexmod.com/wp-content/uploads/2021/04/dates27.jpg)

Calculation Date
----------------

Definition and Notes:

*   As the name say, calculation date is the date where the ratios are calculated (DSCRs (Projected & Historic), the LLCR and the Debt to Equity Ratio
*   Typically Calculation Date coincide with each Payment Date.

Extract from a real Term sheet:

![Key dates in a typical project finance loan term sheet and its application in a project finance model ](https://www.finexmod.com/wp-content/uploads/2021/04/dates22.jpg)

How to use it in the financial model?

Calculation dates typically coincide with the payment dates so there’s no need to consider calculation dates separately in the model unless otherwise.

### **First Repayment Date**

Definition and Notes:

*   The first repayment instalment must be repaid on the First Repayment Date
*   It’s usually defined as the minimum of a specific date and the date falling x-month post commercial operation date

Extract from a real Term sheet:

![Key dates in a typical project finance loan term sheet and its application in a project finance model](https://www.finexmod.com/wp-content/uploads/2021/04/dates24.jpg)

How to use it in the financial model?

In the debt terms for each tranche of debt in the financial model, the first repayment date or First Principal repayment date should be included as one of the key dates and should be used in the model for creating payment flags and counters.

In the snapshot below, the first principal repayment date is calculated based on the grace period ( 30 months post signing date) and is basically defined as 6months post commercial operation date.

If you are working on a project and the term sheet is already signed and the first payment date is fixed in the contract then you need to hard-code it in your financial model.

![First Repayment Date or First Principal Repayment Date in a Loan agreement](https://www.finexmod.com/wp-content/uploads/2021/04/dates26.jpg)

### Final Maturity Date

Definition and Notes

*   it’s the last payment date
*   Refers to the date on which the loan must be fully reimbursed.

Extract from a real Term sheet:

![Key dates in a typical project finance loan term sheet and its application in a project finance model](https://www.finexmod.com/wp-content/uploads/2021/04/dates25.jpg)

How to use it in the financial model?

Same as First Repayment Date, the Final Maturity Date should be reflected as an input in the financial model and be used for calculating calculation flags and counters for each debt tranche included in the financial model.

In the below snapshot the last payment date is calculated using 15 years maturity starting from signature date. If the loan agreement is signed and the date is fixed in the contract, then this date should be hard-coded in the model.

![the final maturity date or maturity date is an important date in a project finance loan agreement](https://www.finexmod.com/wp-content/uploads/2021/04/dates28.jpg)

I am sure there are other definitions related to time that I didn’t cover here. If you think of anything, please let me know in the comments.

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-04-30T06:19:18+00:00April 28th, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fdates2%2F&t=Key%20Dates%20in%20a%20Loan%20Term%20Sheet%20%E2%80%93%20Part%202 "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fdates2%2F&text=Key%20Dates%20in%20a%20Loan%20Term%20Sheet%20%E2%80%93%20Part%202 "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/dates2/&title=Key%20Dates%20in%20a%20Loan%20Term%20Sheet%20%E2%80%93%20Part%202 "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fdates2%2F&title=Key%20Dates%20in%20a%20Loan%20Term%20Sheet%20%E2%80%93%20Part%202&summary=In%20the%20previous%20blog%20post%2C%20I%20opened%20up%20the%20topic%20of%20key%20dates%20in%20a%20typical%20project%20finance%20loan%20term%20sheet.%20This%20is%20part%202%20of%20the%20same%20discussion%20and%20I%20will%20take%20you%20through%20the%20below%20terms%3A%0D%0A%0D%0A%20%09Availability%20Period%0D%0A%20%09Calculation%20Date%0D%0A%20%09Payment%20Date%0D%0A%20%09F "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fdates2%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fdates2%2F&name=Key%20Dates%20in%20a%20Loan%20Term%20Sheet%20%E2%80%93%20Part%202&description=In%20the%20previous%20blog%20post%2C%20I%20opened%20up%20the%20topic%20of%20key%20dates%20in%20a%20typical%20project%20finance%20loan%20term%20sheet.%20This%20is%20part%202%20of%20the%20same%20discussion%20and%20I%20will%20take%20you%20through%20the%20below%20terms%3A%0D%0A%0D%0A%20%09Availability%20Period%0D%0A%20%09Calculation%20Date%0D%0A%20%09Payment%20Date%0D%0A%20%09First%20Repayment%20Date%0D%0A%20%09Final%20Maturity%20Date "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fdates2%2F&description=In%20the%20previous%20blog%20post%2C%20I%20opened%20up%20the%20topic%20of%20key%20dates%20in%20a%20typical%20project%20finance%20loan%20term%20sheet.%20This%20is%20part%202%20of%20the%20same%20discussion%20and%20I%20will%20take%20you%20through%20the%20below%20terms%3A%0D%0A%0D%0A%20%09Availability%20Period%0D%0A%20%09Calculation%20Date%0D%0A%20%09Payment%20Date%0D%0A%20%09First%20Repayment%20Date%0D%0A%20%09Final%20Maturity%20Date&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F04%2Fcover-Dates2.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fdates2%2F&title=Key%20Dates%20in%20a%20Loan%20Term%20Sheet%20%E2%80%93%20Part%202&description=In%20the%20previous%20blog%20post%2C%20I%20opened%20up%20the%20topic%20of%20key%20dates%20in%20a%20typical%20project%20finance%20loan%20term%20sheet.%20This%20is%20part%202%20of%20the%20same%20discussion%20and%20I%20will%20take%20you%20through%20the%20below%20terms%3A%0D%0A%0D%0A%20%09Availability%20Period%0D%0A%20%09Calculation%20Date%0D%0A%20%09Payment%20Date%0D%0A%20%09First%20Repayment%20Date%0D%0A%20%09Final%20Maturity%20Date "Vk")
[Email](mailto:?body=https://www.finexmod.com/dates2/&subject=Key%20Dates%20in%20a%20Loan%20Term%20Sheet%20%E2%80%93%20Part%202 "Email")

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

[Page load link](https://www.finexmod.com/dates2#)

[Go to Top](https://www.finexmod.com/dates2#)