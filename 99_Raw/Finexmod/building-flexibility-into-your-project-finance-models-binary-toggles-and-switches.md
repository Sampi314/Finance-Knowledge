# Building flexibility into your project Finance models: Binary Toggles and switches – Finexmod

**Source:** https://www.finexmod.com/building-flexibility-into-your-project-finance-models-binary-toggles-and-switches

---

[Skip to content](https://www.finexmod.com/building-flexibility-into-your-project-finance-models-binary-toggles-and-switches#content)

Building flexibility into your project Finance models: Binary Toggles and switches

One of the main pillars of a standard financial model is flexibility, and one of the main characteristics of a great financial modeler is flexibility.

Let’s have a look at the meaning of flexibility in the dictionary. Flexibility means ‘capable of being flexed” or “characterized by a ready capability to adapt to new, different, or changing requirements.”

So financial model should be capable of adapting to different changes and requirements.

And another aspect of a good model is user-friendliness.

With the help of toggles and switches, you can allow your users to flex some of the base case assumptions easily with a click.

![](https://www.finexmod.com/wp-content/uploads/2022/09/Flex-and-UserF-image.jpg)

In this post, I will look at cases with binary options.

**Step 1:** Formulate the options that you think should be tested in the model.

Before submitting the model to your team or client, you want to consider things that need to be flexed at every project stage.

Here are a couple of examples:

*   Is interest during construction paid or capitalized?
*   Is interest subject to withholding tax?
*   Is tariff escalated?

I will use the example of tariff escalation here.

Let’s say we are negotiating the purchase agreement and we want to test the impact of having a flat tariff or an escalated tariff.

**Step 2: Define the input** 

You must modify your inputs and include the switch in your input sheet.

In my tariff example, I want to define a time-based escalation rate and include the option to keep the tariff fixed so the escalation rate will be o.

Then I create a switch with 1 applying escalation and o for no escalation.

![](https://www.finexmod.com/wp-content/uploads/2022/09/Step-2-define-in-Inputs.jpg)

**Step 3:** Insert a checkbox using the developer tab.

If you don’t have the developer tab in your excel ribbon you can activate it by going to:

On the File tab, go to _Options > Customize Ribbon_. Under _Customize the Ribbon_ and under _Main Tabs_, select the _Developer_ check box

You can also change the text and formulate it to know what the switch represents.

**Step 4:** Link your input to the option button

Now you just need to right-click on the checkbox and establish the link. One thing to keep in mind is that you will most probably import this button to other sheets, so the cell address should contain the worksheet name. For this, you need to do what professor Bodmer calls the criss-cross or I call it zig zag. You need to click on the cell link under format control and then go to another sheet and come back to the sheet where you have the button and then click on the input cell.

**Step 5:** You then have to apply the switch in your calculation so that the switch can be activated.

Now you need to establish the link in your calculation. In my example, I have already calculated a tariff escalation index in my Revenue sheet, I just tweak the formula so that if this switch is set to false, the tariff is kept flat and if the switch is set to true then the tariff will be escalated.

**Step 6:** If you need to run any macro while changing the switch, then you can simply insert the macro that you want to run on the button.

**Step 7:** Import the button in your summary sheet or Dashboard.

You need to do this every time that you are preparing for a meeting so that you customize your summary/dashboard for the subject that will be discussed during that particular meeting.

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2022-09-20T08:32:48+00:00September 20th, 2022|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fbuilding-flexibility-into-your-project-finance-models-binary-toggles-and-switches%2F&t=Building%20flexibility%20into%20your%20project%20Finance%20models%3A%20Binary%20Toggles%20and%20switches "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fbuilding-flexibility-into-your-project-finance-models-binary-toggles-and-switches%2F&text=Building%20flexibility%20into%20your%20project%20Finance%20models%3A%20Binary%20Toggles%20and%20switches "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/building-flexibility-into-your-project-finance-models-binary-toggles-and-switches/&title=Building%20flexibility%20into%20your%20project%20Finance%20models%3A%20Binary%20Toggles%20and%20switches "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fbuilding-flexibility-into-your-project-finance-models-binary-toggles-and-switches%2F&title=Building%20flexibility%20into%20your%20project%20Finance%20models%3A%20Binary%20Toggles%20and%20switches&summary=One%20of%20the%20main%20pillars%20of%20a%20standard%20financial%20model%20is%20flexibility%2C%20and%20one%20of%20the%20main%20characteristics%20of%20a%20great%20financial%20modeler%20is%20flexibility.%0D%0A%0D%0ALet%27s%20have%20a%20look%20at%20the%20meaning%20of%20flexibility%20in%20the%20dictionary.%20Flexibility%20means%20%27capable%20of%20being "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fbuilding-flexibility-into-your-project-finance-models-binary-toggles-and-switches%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fbuilding-flexibility-into-your-project-finance-models-binary-toggles-and-switches%2F&name=Building%20flexibility%20into%20your%20project%20Finance%20models%3A%20Binary%20Toggles%20and%20switches&description=One%20of%20the%20main%20pillars%20of%20a%20standard%20financial%20model%20is%20flexibility%2C%20and%20one%20of%20the%20main%20characteristics%20of%20a%20great%20financial%20modeler%20is%20flexibility.%0D%0A%0D%0ALet%26%2339%3Bs%20have%20a%20look%20at%20the%20meaning%20of%20flexibility%20in%20the%20dictionary.%20Flexibility%20means%20%26%2339%3Bcapable%20of%20being%20flexed%26quot%3B%20or%20%26quot%3Bcharacterized%20by%20a%20ready%20capability%20to%20adapt%20to%20new%2C%20different%2C%20or%20changing "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fbuilding-flexibility-into-your-project-finance-models-binary-toggles-and-switches%2F&description=One%20of%20the%20main%20pillars%20of%20a%20standard%20financial%20model%20is%20flexibility%2C%20and%20one%20of%20the%20main%20characteristics%20of%20a%20great%20financial%20modeler%20is%20flexibility.%0D%0A%0D%0ALet%26%2339%3Bs%20have%20a%20look%20at%20the%20meaning%20of%20flexibility%20in%20the%20dictionary.%20Flexibility%20means%20%26%2339%3Bcapable%20of%20being%20flexed%26quot%3B%20or%20%26quot%3Bcharacterized%20by%20a%20ready%20capability%20to%20adapt%20to%20new%2C%20different%2C%20or%20changing&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2022%2F09%2FCover-Toggle-switches-Binary.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fbuilding-flexibility-into-your-project-finance-models-binary-toggles-and-switches%2F&title=Building%20flexibility%20into%20your%20project%20Finance%20models%3A%20Binary%20Toggles%20and%20switches&description=One%20of%20the%20main%20pillars%20of%20a%20standard%20financial%20model%20is%20flexibility%2C%20and%20one%20of%20the%20main%20characteristics%20of%20a%20great%20financial%20modeler%20is%20flexibility.%0D%0A%0D%0ALet%26%2339%3Bs%20have%20a%20look%20at%20the%20meaning%20of%20flexibility%20in%20the%20dictionary.%20Flexibility%20means%20%26%2339%3Bcapable%20of%20being%20flexed%26quot%3B%20or%20%26quot%3Bcharacterized%20by%20a%20ready%20capability%20to%20adapt%20to%20new%2C%20different%2C%20or%20changing "Vk")
[Email](mailto:?body=https://www.finexmod.com/building-flexibility-into-your-project-finance-models-binary-toggles-and-switches/&subject=Building%20flexibility%20into%20your%20project%20Finance%20models%3A%20Binary%20Toggles%20and%20switches "Email")

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

[Page load link](https://www.finexmod.com/building-flexibility-into-your-project-finance-models-binary-toggles-and-switches#)

[Go to Top](https://www.finexmod.com/building-flexibility-into-your-project-finance-models-binary-toggles-and-switches#)