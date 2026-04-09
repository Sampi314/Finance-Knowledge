# Using Macros in your financial models: Quick tips – Finexmod

**Source:** https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips

---

[Skip to content](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips#content)

Using Macros in your financial models: Quick tips

Last week, I ran a survey asking my students for feedback on our financial modelling sessions. One of the questions was about what additional Excel skills they’d like to improve. Most of them said they want to learn how to build macros.

I thought about what I could advise them. My first idea was to suggest a series of online courses and videos on how to build macros from A to Z. But then I told myself, these are busy individuals, and they don’t really have the time to enjoy learning a new language. And to be honest, if I were to recommend a new language, I’d say Mandarin, not VBA.

So here’s my recommendation:

If you have the time and the passion, then yes, go and learn VBA properly. Take a structured course that does a deep dive, step by step. Once you learn it, you’ll be able to get creative and build from scratch.

If you’re a financial modeller like me and you consider yourself more of a macro user than a VBA developer, then the first step is to understand where you actually need to apply macros and automation in your models.

Here are some of the typical use cases for macros in project finance models:

**1\. Resolving circular references**
-------------------------------------

If you have a circular reference that isn’t an error but a natural result of the model logic, you need to resolve the iterative calculation unless it’s a quick one-off calculation that you’ll throw away and never send to anyone.

The conventional method is to use a simple copy and paste macro with a loop. It’s only two lines of code, but the issue is that the number of these macros grows as your model gets more complex.

Typical circular reference examples include:

• Financing fees in the Sources and Uses  
• Interest and corporate income tax in the P&L  
• DSRA funding (depending of position in cashflow waterfall)  
• Cash sweep mechanisms  
• Capitalized interest during construction  
• Carried interest or performance fees tied to cash flows

[![Copy and Paste Macro in Project finance models](https://www.finexmod.com/wp-content/uploads/2025/07/Copy-and-Paste.png)](https://www.finexmod.com/wp-content/uploads/2025/07/Copy-and-Paste.png)

The more advanced and effective method is to get rid of the copy and paste button and apply the User Defined Function (Parallel model technique) developed by Professor Edward Bodmer.

> [Parallel Model in Project Finance and Becoming a Top Modeller Instead of a Copy and Paster](https://edbodmer.com/project-finance/edbodmer-wikispaces-com-circularreferencesincorporatefinanceandprojectfinance/)

2\. Setting the tariff
----------------------

In a tariff setting model, you may want a macro that automates the goal-seeking process for you. Especially if you’re already using copy and paste macros, you’ll want to include goal seek in the automation. A typical example is during PPA negotiations, where you’re setting a tariff based on a target equity IRR. That can easily be automated with a goal seek macro.

[![](https://www.finexmod.com/wp-content/uploads/2025/07/GoalSeek.png)](https://www.finexmod.com/wp-content/uploads/2025/07/GoalSeek.png)

For more advanced dynamic Goal Seek Macro check Professor Edward Bodmer’s technique:

> [Dynamic Goal Seek](https://edbodmer.com/dynamic-goal-seek/)

3\. Sensitivity and scenario analysis analysis
----------------------------------------------

If your model already uses macros for copy and paste or goal seek, then you need an additional macro that loops through your sensitivity cases while running the others.

[![](https://www.finexmod.com/wp-content/uploads/2025/07/Sens.png)](https://www.finexmod.com/wp-content/uploads/2025/07/Sens.png)

[![](https://www.finexmod.com/wp-content/uploads/2025/07/Sens-code.png)](https://www.finexmod.com/wp-content/uploads/2025/07/Sens-code.png)

4\. Automatic formatting of your spreadsheets
---------------------------------------------

There are already a lot of Excel add-ins available to help with formatting and auditing your models. The one I personally use is the Generic Macro by Professor Edward Bodmer. It’s free to download, and with just a couple of clicks, you can apply consistent formatting, add table of content, find hard-coded inputs, access several build-in user defined functions, useful shortcuts like copy to the right and much more.

What I really like about the Generic Macro tool is that you also have access to the code. That means you can go in, see how it works, and even change or customize it to fit your own workflow.

> [Generic Macros File (Colouring and Copy to Right)](https://edbodmer.com/excel-utilities-and-backpack/generic-macros-file/)

For everything else, you can use any AI. You’ll see that very quickly you’ll be able to read and understand macros. You’ll get to a point where you can spot the errors AI makes and ask it to fix them. And eventually, you’ll just use the AI-generated draft and make the changes yourself.

And that’s really all you need to be able to say on your CV that you know VBA for financial modeling.

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2025-07-03T12:46:30+00:00July 3rd, 2025|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fusing-macros-in-your-financial-models-quick-tips%2F&t=Using%20Macros%20in%20your%20financial%20models%3A%20Quick%20tips "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fusing-macros-in-your-financial-models-quick-tips%2F&text=Using%20Macros%20in%20your%20financial%20models%3A%20Quick%20tips "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/&title=Using%20Macros%20in%20your%20financial%20models%3A%20Quick%20tips "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fusing-macros-in-your-financial-models-quick-tips%2F&title=Using%20Macros%20in%20your%20financial%20models%3A%20Quick%20tips&summary=Last%20week%2C%20I%20ran%20a%20survey%20asking%20my%20students%20for%20feedback%20on%20our%20financial%20modelling%20sessions.%20One%20of%20the%20questions%20was%20about%20what%20additional%20Excel%20skills%20they%E2%80%99d%20like%20to%20improve.%20Most%20of%20them%20said%20they%20want%20to%20learn%20how%20to%20build%20macros.%0D%0A%0D%0AI%20thought%20about%20 "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fusing-macros-in-your-financial-models-quick-tips%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fusing-macros-in-your-financial-models-quick-tips%2F&name=Using%20Macros%20in%20your%20financial%20models%3A%20Quick%20tips&description=Last%20week%2C%20I%20ran%20a%20survey%20asking%20my%20students%20for%20feedback%20on%20our%20financial%20modelling%20sessions.%20One%20of%20the%20questions%20was%20about%20what%20additional%20Excel%20skills%20they%E2%80%99d%20like%20to%20improve.%20Most%20of%20them%20said%20they%20want%20to%20learn%20how%20to%20build%20macros.%0D%0A%0D%0AI%20thought%20about%20what%20I%20could%20advise%20them.%20My%20first%20idea%20was%20to%20suggest "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fusing-macros-in-your-financial-models-quick-tips%2F&description=Last%20week%2C%20I%20ran%20a%20survey%20asking%20my%20students%20for%20feedback%20on%20our%20financial%20modelling%20sessions.%20One%20of%20the%20questions%20was%20about%20what%20additional%20Excel%20skills%20they%E2%80%99d%20like%20to%20improve.%20Most%20of%20them%20said%20they%20want%20to%20learn%20how%20to%20build%20macros.%0D%0A%0D%0AI%20thought%20about%20what%20I%20could%20advise%20them.%20My%20first%20idea%20was%20to%20suggest&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2025%2F07%2FCover-Learning-VBA.png "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fusing-macros-in-your-financial-models-quick-tips%2F&title=Using%20Macros%20in%20your%20financial%20models%3A%20Quick%20tips&description=Last%20week%2C%20I%20ran%20a%20survey%20asking%20my%20students%20for%20feedback%20on%20our%20financial%20modelling%20sessions.%20One%20of%20the%20questions%20was%20about%20what%20additional%20Excel%20skills%20they%E2%80%99d%20like%20to%20improve.%20Most%20of%20them%20said%20they%20want%20to%20learn%20how%20to%20build%20macros.%0D%0A%0D%0AI%20thought%20about%20what%20I%20could%20advise%20them.%20My%20first%20idea%20was%20to%20suggest "Vk")
[Email](mailto:?body=https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/&subject=Using%20Macros%20in%20your%20financial%20models%3A%20Quick%20tips "Email")

Related Posts
-------------

![The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips)

[](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/)

#### [The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/ "The Art of Structuring Project Finance Models: A Personal Journey")

April 10th, 2025

![Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/wp-content/uploads/2024/04/Comic-Sans-Blog-Banner-500x383@2x.png)

[](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/)

#### [Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/ "Do Circular References Still Have Us Stuck on Copy-Paste?")

April 29th, 2024 | [0 Comments](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/#respond)

![When do we decide whether to adopt or rebuild a project finance model, and who makes that decision?](https://www.finexmod.com/wp-content/uploads/2024/02/Green-Minimalist-Blog-Post-Linkedin-Article-Cover-500x383@2x.png)

[](https://www.finexmod.com/when-do-we-decide-whether-to-adopt-or-rebuild-a-project-finance-model-and-who-makes-that-decision/)

#### [When do we decide whether to adopt or rebuild a project finance model, and who makes that decision?](https://www.finexmod.com/when-do-we-decide-whether-to-adopt-or-rebuild-a-project-finance-model-and-who-makes-that-decision/ "When do we decide whether to adopt or rebuild a project finance model, and who makes that decision?")

February 2nd, 2024 | [0 Comments](https://www.finexmod.com/when-do-we-decide-whether-to-adopt-or-rebuild-a-project-finance-model-and-who-makes-that-decision/#respond)

[Page load link](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips#)

[Go to Top](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips#)