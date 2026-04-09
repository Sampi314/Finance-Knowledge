# Limitation on Disbursements in a Project finance transaction – Finexmod

**Source:** https://www.finexmod.com/limitation-on-disbursements-in-a-project-finance-transaction

---

[Skip to content](https://www.finexmod.com/limitation-on-disbursements-in-a-project-finance-transaction#content)

Limitation on Disbursements in a Project finance transaction

In this blog post, i want to talk about two limitations that might be imposed on the loan disbursement:

**1\. Minimum amount in each disbursement**

In most loan agreements you have a clause that limits the amount of each disbursement.

Example 1: This is extracted from the EBID disbursement handbook. You can see the same guideline in most disbursements guidelines.

![Minimum Disbursement Amount](https://www.finexmod.com/wp-content/uploads/2022/01/EBID-Minimum-disbursement.jpg)

Example 2: Extracted from a real loan agreement

![](https://www.finexmod.com/wp-content/uploads/2022/01/Minimum-disbursement.jpg)

**2\. Maximum number of disbursement**

You can also have lenders limiting a number of total disbursement requests during the availability period or even another limit for the number of requests per year.

Example: as you can see in the below example, the number of total requests is limited to 10.

![](https://www.finexmod.com/wp-content/uploads/2022/01/Extract-from-loan-agreement-limitation-in-disbursment02.jpg)

**Does this have financial implications?** We should go and check it out in the financial model:

**Step 1:** Make sure that construction flows and your sources and uses of funds statement are projected on a monthly basis. If not then you need to do it. I used to provide flexibility in my financial models to have construction on quarterly or semi-annually or even annually but I don’t believe we should allow this. The reason being that once you reach financial close, you’ll need to monitor expenses on a monthly basis and therefore you need to have a financial model that considers construction on a monthly basis. If you have a pre-financial close model that is on a quarterly basis then it will be a lot of work to have everything on a monthly basis. So instead, do the hard work up-front and it will be easier to convert the pre-FC model to a post-FC with actuals and projections.

**Step 2:** Introduce  new input parameters in your financing :

|     |
| --- |
| – Periodicity of debt drawdown expressed in number of months |
| Minimum debt Disbursement Amount expressed in currency |
| Maximum total number of disbursements expressed in # |

![](https://www.finexmod.com/wp-content/uploads/2022/01/snapshot-minimum-disbursment-04.jpg)

**Step 3:** Make sure you separate your total project cost into “non-financing costs” and “financing costs”. Then use the input parameter that you created in step 2 to create a periodic non-financing costs looking-forward. So for example, if the lenders say they limit the number of disbursements to maximum nine (9) drawdowns over a period of 24 months, then you better base your drawdown on non-financing costs over a quarter in each period. You can do this in multiple ways but I am using the MOD function to get the payment flag and then the combo of SUM and OFFSET function to do the sum looking forward.

![Minimum disbursement](https://www.finexmod.com/wp-content/uploads/2022/01/snapshot-minimum-disbursment-01.jpg)

Then you add up the looking forward non-financing costs to the financing costs and use this line for calculating your drawdown schedules

**Step 4:** You also want to make sure that the periodic financing costs like commitment fees and interest during construction are also calculated on a quarterly basis if you are drawing down on the debt on a quarterly basis.

![](https://www.finexmod.com/wp-content/uploads/2022/01/snapshot-minimum-disbursment-02.jpg)

**Step 5:** Create 2 checks. One to make sure that the total number of debt drawdowns are equal or less than the maximum number of drawdowns allowed under the loan agreement. Second, check that each disbursement amount is greater than the minimum disbursements limit.

![](https://www.finexmod.com/wp-content/uploads/2022/01/snapshot-minimum-disbursment-03.jpg)

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2022-01-07T15:06:20+00:00January 7th, 2022|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Flimitation-on-disbursements-in-a-project-finance-transaction%2F&t=Limitation%20on%20Disbursements%20in%20a%20Project%20finance%20transaction "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Flimitation-on-disbursements-in-a-project-finance-transaction%2F&text=Limitation%20on%20Disbursements%20in%20a%20Project%20finance%20transaction "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/limitation-on-disbursements-in-a-project-finance-transaction/&title=Limitation%20on%20Disbursements%20in%20a%20Project%20finance%20transaction "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Flimitation-on-disbursements-in-a-project-finance-transaction%2F&title=Limitation%20on%20Disbursements%20in%20a%20Project%20finance%20transaction&summary=%C2%A0%0D%0A%0D%0AIn%20this%20blog%20post%2C%20i%20want%20to%20talk%20about%20two%20limitations%20that%20might%20be%20imposed%20on%20the%20loan%20disbursement%3A%0D%0A%0D%0A1.%20Minimum%20amount%20in%20each%20disbursement%0D%0A%0D%0AIn%20most%20loan%20agreements%20you%20have%20a%20clause%20that%20limits%20the%20amount%20of%20each%20disbursement.%0D%0A%0D%0AExample%201%3A%20T "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Flimitation-on-disbursements-in-a-project-finance-transaction%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Flimitation-on-disbursements-in-a-project-finance-transaction%2F&name=Limitation%20on%20Disbursements%20in%20a%20Project%20finance%20transaction&description=%26nbsp%3B%0D%0A%0D%0AIn%20this%20blog%20post%2C%20i%20want%20to%20talk%20about%20two%20limitations%20that%20might%20be%20imposed%20on%20the%20loan%20disbursement%3A%0D%0A%0D%0A1.%20Minimum%20amount%20in%20each%20disbursement%0D%0A%0D%0AIn%20most%20loan%20agreements%20you%20have%20a%20clause%20that%20limits%20the%20amount%20of%20each%20disbursement.%0D%0A%0D%0AExample%201%3A%20This%20is%20extracted%20from%20the%20EBID%20disbursement%20handbook.%20You%20can "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Flimitation-on-disbursements-in-a-project-finance-transaction%2F&description=%26nbsp%3B%0D%0A%0D%0AIn%20this%20blog%20post%2C%20i%20want%20to%20talk%20about%20two%20limitations%20that%20might%20be%20imposed%20on%20the%20loan%20disbursement%3A%0D%0A%0D%0A1.%20Minimum%20amount%20in%20each%20disbursement%0D%0A%0D%0AIn%20most%20loan%20agreements%20you%20have%20a%20clause%20that%20limits%20the%20amount%20of%20each%20disbursement.%0D%0A%0D%0AExample%201%3A%20This%20is%20extracted%20from%20the%20EBID%20disbursement%20handbook.%20You%20can&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2022%2F01%2FMinimum-disbursement-Cover.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Flimitation-on-disbursements-in-a-project-finance-transaction%2F&title=Limitation%20on%20Disbursements%20in%20a%20Project%20finance%20transaction&description=%26nbsp%3B%0D%0A%0D%0AIn%20this%20blog%20post%2C%20i%20want%20to%20talk%20about%20two%20limitations%20that%20might%20be%20imposed%20on%20the%20loan%20disbursement%3A%0D%0A%0D%0A1.%20Minimum%20amount%20in%20each%20disbursement%0D%0A%0D%0AIn%20most%20loan%20agreements%20you%20have%20a%20clause%20that%20limits%20the%20amount%20of%20each%20disbursement.%0D%0A%0D%0AExample%201%3A%20This%20is%20extracted%20from%20the%20EBID%20disbursement%20handbook.%20You%20can "Vk")
[Email](mailto:?body=https://www.finexmod.com/limitation-on-disbursements-in-a-project-finance-transaction/&subject=Limitation%20on%20Disbursements%20in%20a%20Project%20finance%20transaction "Email")

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

[Page load link](https://www.finexmod.com/limitation-on-disbursements-in-a-project-finance-transaction#)

[Go to Top](https://www.finexmod.com/limitation-on-disbursements-in-a-project-finance-transaction#)