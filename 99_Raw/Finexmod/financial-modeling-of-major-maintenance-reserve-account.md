# Financial Modeling of Major Maintenance Reserve Account – Finexmod

**Source:** https://www.finexmod.com/financial-modeling-of-major-maintenance-reserve-account

---

[Skip to content](https://www.finexmod.com/financial-modeling-of-major-maintenance-reserve-account#content)

Financial Modeling of Major Maintenance Reserve Account

What is Major Maintenance cost? 
--------------------------------

**Maintenance costs** in general are unlike operating costs are more irregular and not necessary occurring on periodic basis. However it depends on the type of maintenance.

**Soft maintenance** cost are required on regular basis and will be included as part of the operating cost budget.

**Major maintenance** typically include replacement of parts or major repair and maintenance.

What is a Major Maintenance reserve account?
--------------------------------------------

Typically major maintenance has a long cycle, meaning it is required every 5, 10 or 15 years. There is a risk that the project will not have enough cash to cover these cost when they are due to be paid. That is when a Major Maintenance Reserve Account (MMRA) is required. This is also a requirement by lenders and the MMRA will be maintained by lenders to make sure that the reserve account accumulates enough cash to fund the major maintenance expenses.

So in short:

*   MMRA reduces risk of cash shortfall to fund major maintenances expenses
*   It is a requirement from lenders 

Questions you need to ask about MMRA?
-------------------------------------

*   How much to budget for major maintenance?

You should know how much money is needed and when is needed so that you can plan on how to build up cash in the reserve account.

I would recommend that you include the maintenance budget as time series input. This way you have more flexibility to change the schedule when required. However if you are sure that the cost will happens every X year, then you can also include the 3 input items to capture the maintenance schedule.

Major Maintenance Cost for example benchmarked at 5% of EPC

Frequency of Major Maintenance for example every 5 years post commercial operation date

*   Is the major maintenance account pre-funded? if yes by how much?

For long cycle major maintenance, it doesn’t make sense to pre-fund the MMRA when the cost is due in 10 years time. Instead you can assume that MMRA will be funded from cash flow from operation. However, still include the option in the model even if at the time you build the model the pre-funding of MMRA is not required. Things will change and another investment officer might be joining the lenders team and completely change the structure so keep it flexible.

*   When should the project start funding the MMRA?

If the MMRA is funded from cash, then you need the information on when to start to place funds in the MMRA. To give you an example, in a solar PV projects when you need to replace the inverter or batteries costing $10m every 10 years, then the payments can be annualized by placing $1m every year in the MMRA and release it at year 10 to pay for the new Equipment.

*   What is the position of the MMRA in the cash flow waterfall? 

There is no one answer on where to place the funding and release from MMRA. It depends on the negotiations with lenders.

Typically lenders require the MMRA to be positioned after and subordinated to debt service and also to funding of debt service reserve account.

let’s Model the MMRA
--------------------

### Inputs

If you have the answer to the above questions, you should be able to built the MMRA into your base case model.

Here are the typical inputs extracted from a real project finance model:

![Major Maintenance reserve Account](https://www.finexmod.com/wp-content/uploads/2021/08/MMRA-Input-Image-01.jpg)

![Major Maintenance Reserve Account](https://www.finexmod.com/wp-content/uploads/2021/08/MMRA-Input-Image-02.jpg)

### Funding of MMRA 

In the above snapshot from the input sheet we see that there’s half a million dollar to be spent on major maintenance 5 years after the start of the operation of this project. 

If you assume that the reserve account should be funded 5 years ahead of time then this means that we need to put aside USD100k every year so that we have USD500k by the end of year 5. However you need to make it flexible so that if later you want to change the assumption and say assume that you don’t need to start putting money aside from year 1 but you start to fund the MMRA 3 years prior to schedule maintenance, then this can be done with swiftly by changing one input in the model.

![Major Maintenance Reserve Account](https://www.finexmod.com/wp-content/uploads/2021/08/MMRA-model-snapshot.jpg)

In Excel you can use the combination of sum and offset function to dynamically sum values through a given number of months indicated in your input sheet.

![Major Maintenance Reserve Account](https://www.finexmod.com/wp-content/uploads/2021/08/MMRA-model-snapshot02.jpg)

### Net Cash flow available for MMRA

You should have net cash flow available for MMRA in your cash flow waterfall.

![cash flow waterfall and Major Maintenance Reserve account](https://www.finexmod.com/wp-content/uploads/2021/08/Cash-flow-waterfall-MMRA.jpg)

### Release from MMRA

You should allow release from MMRA:

*   when maintenance is due and cost is payable
*   at the end of the life of the project or if just a requirement from lenders, at the lend of life of loans

### Links to Financial Statements 

Here are the links that you need to establish from MMRA to financial statement:

Funding and release from MMRA –> Linked to Cash flow waterfall statement

MMRA ending balance  –> Linked to Balance sheet under assets

Watch the video 👇🏽

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-09-02T08:21:18+00:00September 1st, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-modeling-of-major-maintenance-reserve-account%2F&t=Financial%20Modeling%20of%20Major%20Maintenance%20Reserve%20Account "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-modeling-of-major-maintenance-reserve-account%2F&text=Financial%20Modeling%20of%20Major%20Maintenance%20Reserve%20Account "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/financial-modeling-of-major-maintenance-reserve-account/&title=Financial%20Modeling%20of%20Major%20Maintenance%20Reserve%20Account "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-modeling-of-major-maintenance-reserve-account%2F&title=Financial%20Modeling%20of%20Major%20Maintenance%20Reserve%20Account&summary=What%20is%20Major%20Maintenance%20cost%3F%C2%A0%0D%0AMaintenance%20costs%20in%20general%20are%20unlike%20operating%20costs%20are%20more%20irregular%20and%20not%20necessary%20occurring%20on%20periodic%20basis.%20However%20it%20depends%20on%20the%20type%20of%20maintenance.%0D%0ASoft%20maintenance%20cost%20are%20required%20on%20regular%20basis%20 "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-modeling-of-major-maintenance-reserve-account%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-modeling-of-major-maintenance-reserve-account%2F&name=Financial%20Modeling%20of%20Major%20Maintenance%20Reserve%20Account&description=What%20is%20Major%20Maintenance%20cost%3F%C2%A0%0D%0AMaintenance%20costs%20in%20general%20are%20unlike%20operating%20costs%20are%20more%20irregular%20and%20not%20necessary%20occurring%20on%20periodic%20basis.%20However%20it%20depends%20on%20the%20type%20of%20maintenance.%0D%0ASoft%20maintenance%20cost%20are%20required%20on%20regular%20basis%20and%20will%20be%20included%20as%20part%20of%20the%20operating%20cost%20budget. "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-modeling-of-major-maintenance-reserve-account%2F&description=What%20is%20Major%20Maintenance%20cost%3F%C2%A0%0D%0AMaintenance%20costs%20in%20general%20are%20unlike%20operating%20costs%20are%20more%20irregular%20and%20not%20necessary%20occurring%20on%20periodic%20basis.%20However%20it%20depends%20on%20the%20type%20of%20maintenance.%0D%0ASoft%20maintenance%20cost%20are%20required%20on%20regular%20basis%20and%20will%20be%20included%20as%20part%20of%20the%20operating%20cost%20budget.&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F09%2FMMRA-Cover.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Ffinancial-modeling-of-major-maintenance-reserve-account%2F&title=Financial%20Modeling%20of%20Major%20Maintenance%20Reserve%20Account&description=What%20is%20Major%20Maintenance%20cost%3F%C2%A0%0D%0AMaintenance%20costs%20in%20general%20are%20unlike%20operating%20costs%20are%20more%20irregular%20and%20not%20necessary%20occurring%20on%20periodic%20basis.%20However%20it%20depends%20on%20the%20type%20of%20maintenance.%0D%0ASoft%20maintenance%20cost%20are%20required%20on%20regular%20basis%20and%20will%20be%20included%20as%20part%20of%20the%20operating%20cost%20budget. "Vk")
[Email](mailto:?body=https://www.finexmod.com/financial-modeling-of-major-maintenance-reserve-account/&subject=Financial%20Modeling%20of%20Major%20Maintenance%20Reserve%20Account "Email")

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

[Page load link](https://www.finexmod.com/financial-modeling-of-major-maintenance-reserve-account#)

[Go to Top](https://www.finexmod.com/financial-modeling-of-major-maintenance-reserve-account#)