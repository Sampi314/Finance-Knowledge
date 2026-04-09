# Modeling Value added Tax in a Project Finance model – Finexmod

**Source:** https://www.finexmod.com/vat

---

[Skip to content](https://www.finexmod.com/vat#content)

Modeling Value added Tax in a Project Finance model

In my opinion, one of the relatively complex subject in project finance modeling is the value added tax. The complexity comes from the VAT refund or reimbursement mechanism.

In this blog post and the video, I explain in a step by step manner how you can model VAT in your project finance model.

Step 1: Get the inputs
----------------------

First you need to answer the following questions:

*   What is the VAT rate?
*   what items of investment costs are subject to VAT?
*   what items of operating costs are subject to VAT?
*   If the project charging VAT on it’s outputs?
*   If VAT is levied, how quickly does the project receive a VAT refund. How long is the delay? Is the delay during construction when the project is cash negative is different than during operation?

Once you have the answer to these questions, then you can report them as inputs in your model. Here’s an example:

![VAT refund mechanism in a Project Finance Model ](https://www.finexmod.com/wp-content/uploads/2021/06/VAT01.jpg)

Step 2: Let’s start with the construction phase
-----------------------------------------------

In a project finance structure, typically there are no revenues during construction or even if there are revenues at some point during construction, then most of the time lenders are reluctant to consider the revenues generated during construction as a source of financing. If the project is subject to VAT during construction, then the project should drawdown on debt and equity to pay the VAT. If the VAT is reimbursable, then it is important to understand how long it takes for the project to recover the taxes.

First we need to calculate the VAT applicable during construction. We will use the VAT applicable %s defined in the Inputs to calculate Expenses subject to VAT. Then get the periodic VAT by simply multiplying the VAT rate by the Expenses subject to VAT. If the project is exempted from paying VAT during construction, then you simply put the %s for VAT applicable on Capex to zero.

![VAT refund mechanism in a Project Finance Model ](https://www.finexmod.com/wp-content/uploads/2021/06/VAT02.jpg)

Now you need to take into account the time lag between paying VAT and getting a refund from VAT paid. In the below example, there’s a 3 months delay from the time the project initiate the refund process and the time when the refund is reimbursed in project’s accounts.

You can use Excel “=Offset” function to look back and calculate the amount of VAT received. Note that this requires that you have a monthly construction period.

![VAT refund mechanism in a Project Finance Model ](https://www.finexmod.com/wp-content/uploads/2021/06/VAT03.jpg)

Now that you have the amount of VAT receivable and VAT received then you can calculate how much VAT is paid and not refunded during construction. This will need to be included in the Sources and Uses of funds and funded with Debt and/or equity.

![VAT refund mechanism in a Project Finance Model ](https://www.finexmod.com/wp-content/uploads/2021/06/VAT04.jpg)

Step 3: Input VAT receivable during operation
---------------------------------------------

Now you need to deal with VAT mechanism during operation.

Same as CapEx, you need to first calculate how VAT is paid on the operating expenses and can be claimed against the VAT received on the output sold.

Once we have the VAT receivable, we just multiply it by the VAT rate to get the VAT receivable.

![VAT refund mechanism in a Project Finance Model ](https://www.finexmod.com/wp-content/uploads/2021/06/VAT05.jpg)

Now you need a corkscrew account with the following items:

*   Input VAT Receivable During Construction : You need to bring in any pending VAT refund from construction. Then how to treat the remaining VAT refund carried forward varies from project to project. You might recover all pending VAT refund pending from construction after COD or you might use it as a credit against the VAT you billed on your invoices.
*   Input VAT receivables: This is the amount of VAT paid on operating expenses.
*   Input VAT Credit Used: is the amount of taxes that can be reduced when paying taxes on output. to calculate this line, you need to first switch to step 3 and get then come back to step 2 and do the link.

![VAT refund mechanism in a Project Finance Model ](https://www.finexmod.com/wp-content/uploads/2021/06/VAT06.jpg)

Step 4: Output VAT payable
--------------------------

Output VAT is what the project charges as VAT on invoices billed to customers. First like we did for Input VAT, calculate the **%s of revenues subject to VAT** and then multiply it by the VAT rate to get the **output VAT payable**.

![VAT refund mechanism in a Project Finance Model](https://www.finexmod.com/wp-content/uploads/2021/06/VAT07.jpg)

Now you need a corkscrew account with the following items:

*   Output VAT Payable: You need to link the output VAT payable in the corkscrew
*   Input VAT Credit Used: to calculate the credit used, you need to take the minimum of what is receivable in the Input VAT account and what is payable under output VAT.
*   Output VAT Paid: if after taking into account the Input VAT credit used, any output VAT paid is calculated using the delay in output paying taxes. the output VAT payable is calculated exactly like any account payable. For example if number of days to pay VAT output is 30 days, then in each semi-annual model period, 30 days of VAT is postpone to the next period (t+1), 30 days of VAT payable in the previous model period (t-1) is payable in the current period and the net gives you the VAT payable in each model period (t).

Output VAT Paid t\= (Output VAT payable) t-1 \*(30 / 180) + (Output VAT payable)t \*(1 – 30/180)

![VAT refund mechanism in a Project Finance Model](https://www.finexmod.com/wp-content/uploads/2021/06/VAT08.jpg)

Step 5: Capture the working capital impact of VAT
-------------------------------------------------

What goes to the Cashflow statement (or cash flor waterfall) is the change in Input VAT receivable and output VAT payable or in other words it’s the working capital impact of VAT.

![VAT refund mechanism in a Project Finance Model](https://www.finexmod.com/wp-content/uploads/2021/06/VAT09.jpg)

Links to establish towards the financial statements:

the working capital impact of VAT: to be linked to the cashflow waterfall

Input VAT Receivable Closing Balance: to be linked to the current assets in the balance sheet

Output VAT Payable Closing Balance: to be linked to the current liabilities in the balance sheet

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-06-07T07:31:54+00:00June 7th, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fvat%2F&t=Modeling%20Value%20added%20Tax%20in%20a%20Project%20Finance%20model "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fvat%2F&text=Modeling%20Value%20added%20Tax%20in%20a%20Project%20Finance%20model "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/vat/&title=Modeling%20Value%20added%20Tax%20in%20a%20Project%20Finance%20model "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fvat%2F&title=Modeling%20Value%20added%20Tax%20in%20a%20Project%20Finance%20model&summary=In%20my%20opinion%2C%20one%20of%20the%20relatively%20complex%20subject%20in%20project%20finance%20modeling%20is%20the%20value%20added%20tax.%20The%20complexity%20comes%20from%20the%20VAT%20refund%20or%20reimbursement%20mechanism.%0D%0AIn%20this%20blog%20post%20and%20the%20video%2C%20I%20explain%20in%20a%20step%20by%20step%20manner%20how%20you%20can%20m "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fvat%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fvat%2F&name=Modeling%20Value%20added%20Tax%20in%20a%20Project%20Finance%20model&description=In%20my%20opinion%2C%20one%20of%20the%20relatively%20complex%20subject%20in%20project%20finance%20modeling%20is%20the%20value%20added%20tax.%20The%20complexity%20comes%20from%20the%20VAT%20refund%20or%20reimbursement%20mechanism.%0D%0AIn%20this%20blog%20post%20and%20the%20video%2C%20I%20explain%20in%20a%20step%20by%20step%20manner%20how%20you%20can%20model%20VAT%20in%20your%20project%20finance%20model.%0D%0AStep%201%3A%20Get%20the "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fvat%2F&description=In%20my%20opinion%2C%20one%20of%20the%20relatively%20complex%20subject%20in%20project%20finance%20modeling%20is%20the%20value%20added%20tax.%20The%20complexity%20comes%20from%20the%20VAT%20refund%20or%20reimbursement%20mechanism.%0D%0AIn%20this%20blog%20post%20and%20the%20video%2C%20I%20explain%20in%20a%20step%20by%20step%20manner%20how%20you%20can%20model%20VAT%20in%20your%20project%20finance%20model.%0D%0AStep%201%3A%20Get%20the&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F06%2FCover-VAT.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fvat%2F&title=Modeling%20Value%20added%20Tax%20in%20a%20Project%20Finance%20model&description=In%20my%20opinion%2C%20one%20of%20the%20relatively%20complex%20subject%20in%20project%20finance%20modeling%20is%20the%20value%20added%20tax.%20The%20complexity%20comes%20from%20the%20VAT%20refund%20or%20reimbursement%20mechanism.%0D%0AIn%20this%20blog%20post%20and%20the%20video%2C%20I%20explain%20in%20a%20step%20by%20step%20manner%20how%20you%20can%20model%20VAT%20in%20your%20project%20finance%20model.%0D%0AStep%201%3A%20Get%20the "Vk")
[Email](mailto:?body=https://www.finexmod.com/vat/&subject=Modeling%20Value%20added%20Tax%20in%20a%20Project%20Finance%20model "Email")

Related Posts
-------------

![Using Macros in your financial models: Quick tips](https://www.finexmod.com/wp-content/uploads/2025/07/Cover-Learning-VBA-500x383@2x.png)

[](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/)

#### [Using Macros in your financial models: Quick tips](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/ "Using Macros in your financial models: Quick tips")

July 3rd, 2025

![The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/vat)

[](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/)

#### [The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/ "The Art of Structuring Project Finance Models: A Personal Journey")

April 10th, 2025

![Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/wp-content/uploads/2024/04/Comic-Sans-Blog-Banner-500x383@2x.png)

[](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/)

#### [Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/ "Do Circular References Still Have Us Stuck on Copy-Paste?")

April 29th, 2024 | [0 Comments](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/#respond)

[Page load link](https://www.finexmod.com/vat#)

[Go to Top](https://www.finexmod.com/vat#)