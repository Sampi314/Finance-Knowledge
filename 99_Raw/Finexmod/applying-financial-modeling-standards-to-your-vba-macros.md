# Applying financial modeling standards to your VBA Macros – Finexmod

**Source:** https://www.finexmod.com/applying-financial-modeling-standards-to-your-vba-macros

---

[Skip to content](https://www.finexmod.com/applying-financial-modeling-standards-to-your-vba-macros#content)

Applying financial modeling standards to your VBA Macros

Everything I share with you on my blog is inspired by my own experiences, either exciting or frustrating. This one comes from a frustration I experienced recently reviewing a financial model.

Nowadays, most people working on financial models are familiar or have heard of the financial modeling best practices. To me the most important ones are:

*   Make your models Flexible so that it can accommodate future changes (This is the F in “FAST” standards.
*   Keep your financial model Simple (The S in “SMART” standards)
*   Develop financial models that are Transparent ( The “T” in FAST standards)

Fortunately and due to the great work of people like _Kenny Whitelaw_–_Jones_ from gridlines and _Rickard Wärnelid_ from Mazars (previously Corality) and their teams, nowadays I receive more and more models that are well designed and structured. Having to work with a standard model saves me a lot of time and allows me to focus more on the inputs and helping the deal team to come up with better structures and policies and negotiate better deals instead of wasting weeks of work trying to simplify and beautify a badly structured model and sometimes rebuilding a model from scratch.

However, I sometimes see that the basic rules of financial modeling that I mentioned above are not applied to the macros included in the models. It has been my experience that model auditors are not as sensitive to the nonconformity of codes with the best practices.

In this post I want to mention the things that bothered me while reviewing and using other people’s macros and I came up with the below rules for myself. 

### **For the sake of transparency, do not hard code inputs within the VBA code**

Look at the below example extracted from a real project finance model. It’s a goal seek macro to set the tariff based on a target equity IRR. As you can see the modeler has hard-coded the target equity IRR within the code.

![Applying financial modeling standards in your VBA codes](https://www.finexmod.com/wp-content/uploads/2021/11/hardcoding-within-macro.jpg)

Why would you do that? 70% of people I know around me, even professionals who are users of Excel don’t even have the developer tab in their Excel ribbon. How do you expect them to change the target IRR? and the worst thing is that in that specific model, the goal seek macro was included in a copy and paste macro so the average user who doesn’t open the VBA editor doesn’t even know that there’s a goal seek that is keeping the equity IRR fixed. This is a real example of not being transparent with your users.

Instead, they could have included the target equity IRR in the Input sheet and indicate that the tariff is an output of the model and equity IRR is an input. The example below from my models shows how i apply the same in my models:

![](https://www.finexmod.com/wp-content/uploads/2021/11/Correct-Goalseek-ExcelVBA2.jpg)

So don’t hard code within the code and include the inputs you need for your code in your worksheet; in the Input section and create a range name and use it in your macro.

### **Color code outputs of you macro differently so that they can be recognized from Inputs**

Most of the time, the output of the macro will be a hard-coded figure. For example, when you are using a goal seek macro to set your price, the price will be hard-coded and fixed by the macro and the user might not understand if that hard-coded input can be changed or not. As the developer of the model, you should color code the outputs of your macro differently. In the below example, I have color coded cells that are the outcomes of a macro in blue background and in my guide sheet I mention that cells with the blue background are not inputs but are results of running a macro.

![](https://www.finexmod.com/wp-content/uploads/2021/11/ColorcodeMacro.jpg)

### **If you are using someone else’s macro, mention the reference**

I consider myself as a user of VBA macros and not a developer. Most codes are already written and people are generous and share them for free online. So when I need to automate a task, I google it and copy and paste the code in my VBA editor within my model, make necessary changes if needed or most of the time, I use the code as is. So like any other digital products, codes are also the property of someone and the least we can do is to mention where we got the code from and acknowledge the work of the person who developed the macro. When citing within the code, the citation information could be placed as a comment above the code, as shows below:

![](https://www.finexmod.com/wp-content/uploads/2021/11/cite-reference.jpg)

### **Explain to the user what each macro in your model is doing** 

If you really want to be transparent when it comes to your macros, then I would suggest to apply the below 3 techniques:

1.  Put texts in your macro to provide information about the code. This is mainly for users who want to go and check your macro and even if they are not familiar with VBA, they should be able to understand the code easily so provide comments for each block in your code.

![](https://www.finexmod.com/wp-content/uploads/2021/11/comment-text-VBA.jpg)

2\. Include a worksheet within your model and list all macros included in your financial model and their functions.

![](https://www.finexmod.com/wp-content/uploads/2021/11/guide-sheet-macro.jpg)

3\. I would go as far as including a message box within your macro that pops out when the user presses the button and explains what the macro will do and if the user is ok with the function, they can press ok and run it.

![](https://www.finexmod.com/wp-content/uploads/2021/11/message-box.jpg)

**Avoid long running Macros** 

I don’t know if it ever happened to you but I have come across models that I was really scared to press the “Run Macro” button! because it was taking so long for the macro to run. So I would say just make sure to limit the number of iteration when you are trying to break a loop with a macro or doing goal seek so that if it goes to a loop, then it breaks after a limited number or after a specific time. 

![](https://www.finexmod.com/wp-content/uploads/2021/11/long-running-macro2.jpg)

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-11-29T09:41:51+00:00November 28th, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fapplying-financial-modeling-standards-to-your-vba-macros%2F&t=Applying%20financial%20modeling%20standards%20to%20your%20VBA%20Macros "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fapplying-financial-modeling-standards-to-your-vba-macros%2F&text=Applying%20financial%20modeling%20standards%20to%20your%20VBA%20Macros "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/applying-financial-modeling-standards-to-your-vba-macros/&title=Applying%20financial%20modeling%20standards%20to%20your%20VBA%20Macros "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fapplying-financial-modeling-standards-to-your-vba-macros%2F&title=Applying%20financial%20modeling%20standards%20to%20your%20VBA%20Macros&summary=Everything%20I%20share%20with%20you%20on%20my%20blog%20is%20inspired%20by%20my%20own%20experiences%2C%20either%20exciting%20or%20frustrating.%20This%20one%20comes%20from%20a%20frustration%20I%20experienced%20recently%20reviewing%20a%20financial%20model.%0D%0A%0D%0ANowadays%2C%20most%20people%20working%20on%20financial%20models%20are%20familia "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fapplying-financial-modeling-standards-to-your-vba-macros%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fapplying-financial-modeling-standards-to-your-vba-macros%2F&name=Applying%20financial%20modeling%20standards%20to%20your%20VBA%20Macros&description=Everything%20I%20share%20with%20you%20on%20my%20blog%20is%20inspired%20by%20my%20own%20experiences%2C%20either%20exciting%20or%20frustrating.%20This%20one%20comes%20from%20a%20frustration%20I%20experienced%20recently%20reviewing%20a%20financial%20model.%0D%0A%0D%0ANowadays%2C%20most%20people%20working%20on%20financial%20models%20are%20familiar%20or%20have%20heard%20of%20the%20financial%20modeling%20best%20practices.%20To%20me%20the "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fapplying-financial-modeling-standards-to-your-vba-macros%2F&description=Everything%20I%20share%20with%20you%20on%20my%20blog%20is%20inspired%20by%20my%20own%20experiences%2C%20either%20exciting%20or%20frustrating.%20This%20one%20comes%20from%20a%20frustration%20I%20experienced%20recently%20reviewing%20a%20financial%20model.%0D%0A%0D%0ANowadays%2C%20most%20people%20working%20on%20financial%20models%20are%20familiar%20or%20have%20heard%20of%20the%20financial%20modeling%20best%20practices.%20To%20me%20the&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F11%2FVBA-standards-in-Fms.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fapplying-financial-modeling-standards-to-your-vba-macros%2F&title=Applying%20financial%20modeling%20standards%20to%20your%20VBA%20Macros&description=Everything%20I%20share%20with%20you%20on%20my%20blog%20is%20inspired%20by%20my%20own%20experiences%2C%20either%20exciting%20or%20frustrating.%20This%20one%20comes%20from%20a%20frustration%20I%20experienced%20recently%20reviewing%20a%20financial%20model.%0D%0A%0D%0ANowadays%2C%20most%20people%20working%20on%20financial%20models%20are%20familiar%20or%20have%20heard%20of%20the%20financial%20modeling%20best%20practices.%20To%20me%20the "Vk")
[Email](mailto:?body=https://www.finexmod.com/applying-financial-modeling-standards-to-your-vba-macros/&subject=Applying%20financial%20modeling%20standards%20to%20your%20VBA%20Macros "Email")

Related Posts
-------------

![Using Macros in your financial models: Quick tips](https://www.finexmod.com/wp-content/uploads/2025/07/Cover-Learning-VBA-500x383@2x.png)

[](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/)

#### [Using Macros in your financial models: Quick tips](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/ "Using Macros in your financial models: Quick tips")

July 3rd, 2025

![The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/applying-financial-modeling-standards-to-your-vba-macros)

[](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/)

#### [The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/ "The Art of Structuring Project Finance Models: A Personal Journey")

April 10th, 2025

![Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/wp-content/uploads/2024/04/Comic-Sans-Blog-Banner-500x383@2x.png)

[](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/)

#### [Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/ "Do Circular References Still Have Us Stuck on Copy-Paste?")

April 29th, 2024 | [0 Comments](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/#respond)

[Page load link](https://www.finexmod.com/applying-financial-modeling-standards-to-your-vba-macros#)

[Go to Top](https://www.finexmod.com/applying-financial-modeling-standards-to-your-vba-macros#)