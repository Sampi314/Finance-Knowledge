# How to Create a dynamic text box for your master error check in your financial models – Finexmod

**Source:** https://www.finexmod.com/how-to-create-a-dynamic-text-box-for-your-master-error-check-in-your-financial-models

---

[Skip to content](https://www.finexmod.com/how-to-create-a-dynamic-text-box-for-your-master-error-check-in-your-financial-models#content)

How to Create a dynamic text box for your master error check in your financial models

Every financial model should contain a series of error checks and it is recommended to include a master error check and alert indicator in the freeze pane in each worksheet within the model.

![](https://www.finexmod.com/wp-content/uploads/2020/12/1-6.jpg)

This way if there is an issue in the model, the user will be notified that something is wrong either in the model mechanic or in the assumptions.

For more on typical error checks please refer to below link:

[Building Integrity Checks in Project Finance Models (Manual & Template)](https://www.eloquens.com/tool/wmjEi0N4/finance/project-finance-models/building-integrity-checks-in-project-finance-models-manual-template/?ref=FinExMod)

and sometimes the issue is with macros and by running certain macros the issue will be resolve. So my aim here is to insert a button in the model that contains a text that says “Ok” if there’s no issue meaning all sanity checks are satisfied and say something else if some of the checks are not satisfied. For example I want to tell my users, if you see this alert, then first click in this button and if the issue persists then go and check what’s wrong in the “Checks” sheet. Let’s see how we can do this.

**Step 1:** Go to the sheet where you listed all your error checks and create a Master check.

![](https://www.finexmod.com/wp-content/uploads/2020/12/2.jpg)

**Step 2:** In any cell type in an If formula with the text that you want the user to see and actions to take in case of errors. For example, I have macros in mu model so I want to tell the user to first click on the button and if the problem remains then go to Checks.

\=IF(Master-Error-Check = 0; “OK”;”Please click on this button or if the issue persists go to Checks sheet and trace the issue”)

If you don’t have macros, you want to refer them to your “Checks” sheet to trace the error.

\=IF(Master-Error-Check = 0; “OK”;”Please go to Checks sheet and trace the issue”)

![](https://www.finexmod.com/wp-content/uploads/2020/12/3.jpg)

**Step 3:** Use conditional formatting on the cells where you have If formula. For example I want to mark the cell as a flashy red if the checks are not satisfied and if all ok, I put a green color background.

![](https://www.finexmod.com/wp-content/uploads/2020/12/4.jpg)

**Step 4:** Once you are ok with the cell format and text, you simply copy and paste is as Linked Picture.

![](https://www.finexmod.com/wp-content/uploads/2020/12/5.jpg)

**Step 5:** Because you want to import the linked image button to other sheets within your model, you need to changed the link. So just simply click on it and go to another sheet and comeback to the same sheet and make the link. When you click on the image, the link will show as “Checks!$E$32” and not just “$E$32”.

![](https://www.finexmod.com/wp-content/uploads/2020/12/6.jpg)

**Step 6:** You can insert Macro or links to the image button if necessary.

![](https://www.finexmod.com/wp-content/uploads/2020/12/7.jpg)

**Step 7:** Copy and Paste the Image button to you Summary sheet and in the freeze pane in each worksheet within the model.

![](https://www.finexmod.com/wp-content/uploads/2020/12/8.jpg)

Ok, I hope you can use this in your models and if you know a more efficient and elegant way to do the same, please let me know.

All the best,

Hedieh

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2020-12-21T12:27:55+00:00December 21st, 2020|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-create-a-dynamic-text-box-for-your-master-error-check-in-your-financial-models%2F&t=How%20to%20Create%20a%20dynamic%20text%20box%20for%20your%20master%20error%20check%20in%20your%20financial%20models "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-create-a-dynamic-text-box-for-your-master-error-check-in-your-financial-models%2F&text=How%20to%20Create%20a%20dynamic%20text%20box%20for%20your%20master%20error%20check%20in%20your%20financial%20models "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/how-to-create-a-dynamic-text-box-for-your-master-error-check-in-your-financial-models/&title=How%20to%20Create%20a%20dynamic%20text%20box%20for%20your%20master%20error%20check%20in%20your%20financial%20models "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-create-a-dynamic-text-box-for-your-master-error-check-in-your-financial-models%2F&title=How%20to%20Create%20a%20dynamic%20text%20box%20for%20your%20master%20error%20check%20in%20your%20financial%20models&summary=Every%20financial%20model%20should%20contain%20a%20series%20of%20error%20checks%20and%20it%20is%20recommended%20to%20include%20a%20master%20error%20check%20and%20alert%20indicator%20in%20the%20freeze%20pane%20in%20each%20worksheet%20within%20the%20model.%0A%0A%0A%0AThis%20way%20if%20there%20is%20an%20issue%20in%20the%20model%2C%20the "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-create-a-dynamic-text-box-for-your-master-error-check-in-your-financial-models%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-create-a-dynamic-text-box-for-your-master-error-check-in-your-financial-models%2F&name=How%20to%20Create%20a%20dynamic%20text%20box%20for%20your%20master%20error%20check%20in%20your%20financial%20models&description=Every%20financial%20model%20should%20contain%20a%20series%20of%20error%20checks%20and%20it%20is%20recommended%20to%20include%20a%20master%20error%20check%20and%20alert%20indicator%20in%20the%20freeze%20pane%20in%20each%20worksheet%20within%20the%20model.%0A%0A%0A%0AThis%20way%20if%20there%20is%20an%20issue%20in%20the%20model%2C%20the "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-create-a-dynamic-text-box-for-your-master-error-check-in-your-financial-models%2F&description=Every%20financial%20model%20should%20contain%20a%20series%20of%20error%20checks%20and%20it%20is%20recommended%20to%20include%20a%20master%20error%20check%20and%20alert%20indicator%20in%20the%20freeze%20pane%20in%20each%20worksheet%20within%20the%20model.%0A%0A%0A%0AThis%20way%20if%20there%20is%20an%20issue%20in%20the%20model%2C%20the&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2020%2F12%2F0.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fhow-to-create-a-dynamic-text-box-for-your-master-error-check-in-your-financial-models%2F&title=How%20to%20Create%20a%20dynamic%20text%20box%20for%20your%20master%20error%20check%20in%20your%20financial%20models&description=Every%20financial%20model%20should%20contain%20a%20series%20of%20error%20checks%20and%20it%20is%20recommended%20to%20include%20a%20master%20error%20check%20and%20alert%20indicator%20in%20the%20freeze%20pane%20in%20each%20worksheet%20within%20the%20model.%0A%0A%0A%0AThis%20way%20if%20there%20is%20an%20issue%20in%20the%20model%2C%20the "Vk")
[Email](mailto:?body=https://www.finexmod.com/how-to-create-a-dynamic-text-box-for-your-master-error-check-in-your-financial-models/&subject=How%20to%20Create%20a%20dynamic%20text%20box%20for%20your%20master%20error%20check%20in%20your%20financial%20models "Email")

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

[Page load link](https://www.finexmod.com/how-to-create-a-dynamic-text-box-for-your-master-error-check-in-your-financial-models#)

[Go to Top](https://www.finexmod.com/how-to-create-a-dynamic-text-box-for-your-master-error-check-in-your-financial-models#)