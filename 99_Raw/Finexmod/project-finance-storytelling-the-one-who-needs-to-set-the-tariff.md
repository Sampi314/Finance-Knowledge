# Project Finance Storytelling: The one who sets the price – Finexmod

**Source:** https://www.finexmod.com/project-finance-storytelling-the-one-who-needs-to-set-the-tariff

---

[Skip to content](https://www.finexmod.com/project-finance-storytelling-the-one-who-needs-to-set-the-tariff#content)

Project Finance Storytelling: The one who sets the price

In this episode of project finance storytelling, I tell you the story of Joseph, a financial modeler working for a private equity fund investing in wind power projects. through this story, I will tell you how to:

*   change the model structure to have tariff as an output by defining a target equity IRR.
*   create a simple goal seek macro to make the process dynamic

Joseph just got back from vacation. He’s been away for almost a month. Although he had a lot of fun during his holiday, but now he’s glad to be back. He loves his job. He works as a financial modeler for a private equity fund investing in wind power projects.

While he is having morning coffee, he goes through his email and sees an urgent email from Joshua.

![](https://www.finexmod.com/wp-content/uploads/2021/09/email-1-from-Joshua.jpg)

The first thought that comes to Joseph’s mind is: what is he talking about? What is this project?

he took another sip on his coffee and remembers:” Ok, I remember now! but we fixed the tariff a long time ago and I completely removed the tariff setting mechanism from that model!”

So he analyzes his options.

Option 1: I take the old model with the tariff setting mechanism and update it

Option 2: I can built-in the tariff setting mechanism into the new model

He remembers all the different changes he made to that model and it will be much harder and time consuming to make all those changes to the old model than rebuilding the tariff setting mechanism into the new model, so his decision is made. He goes with option 2.

He takes a deep breath and another sip on his coffee, He pulls up his down-tempo playlist and starts to work on the model.

Step 1: on top of the summary sheet he creates a new section and labels it as “Tariff Setting mechanism”. His aim is to set the tariff based on a target equity IRR. So target equity IRR is an input and tariff will be an output of the model.

He creates a hard-coded input for Target equity IRR and copies the calculated equity IRR from the “return and ratios” sheet. He needs another hard-coded value which is the tariff which will be determined using the “Goal Seek” function under Excel. So, he creates that but color-codes it differently  so that the user knows that this is an output of the macro and not an input.

Step 2: He plugs-in a number for tariff for now and makes the link to the model. Because he already had an input for tariff in his “Inputs” sheet. He will just replace that input or make a link so that the model uses the output from the macro as tariff.

Step 3: Now he needs to record a goal seek macro. but before he does that he will do another adjustment. He normally doesn’t like to do a goal seek on IRR. IRR can be quite unpredictable, so just to be on the same side, he will use the NPV function using the target IRR as a discount rate and creates a goal seek that sets the NPV to zero by changing Tariff. This way, it will be exactly the same as if he was setting the calculated equity IRR equal to target equity IRR.

He will then press record on Developer tab to record the macro and then does the goal seek:

1.  On the **Data** tab, in the **Data Tools** group, he clicks on **What-If Analysis**, and then clicks **Goal Seek**.
    
2.  In the **Set cell** box, he enters the reference for the cell that contains the NPV.
    
3.  In the **To value** box, he types zero
4.  In the **By changing cell** box, he enter the reference for the cell the tariff.
    

He stops recording the macro. He just needs to do a minor change in the code.

1.  He will create name ranges for the cells containing “NPV” and “Tariff” and give them a name and then goes back to the code and replace the cell references with the name ranges he defined for these cells.

> Sub Goalseektariff()
> ' Goalseektariff Macro
> Range("Equity\_NPV").GoalSeek Goal:=0, ChangingCell:=Range("Tariff")
> End Sub

1.  He has a copy and paste macro that he wants to run while the goal seek is running, he will just call that macro within the code.

> Sub Goalseektariff()
> ' Goalseektariff Macro
> Range("Equity\_NPV").GoalSeek Goal:=0, ChangingCell:=Range("Tariff")
> Call UsesCopyPaste
> End Sub

Now he can copy the code to different buttons and switches and the macro will not be limited to this worksheet only.

He does a different rounds of test by changing different parameters and see if the model works properly:

Test 1: he increases EPC and expects tariff to go up —> OK

Test 2: He decreases Opex and expects tariff to go down —> OK

Test 3: He changes the debt terms and check if the tariff changes accordingly —> OK

Now, he feels comfortable and excited to go for tomorrow’s meeting.

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2021-09-26T08:01:34+00:00September 26th, 2021|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-needs-to-set-the-tariff%2F&t=Project%20Finance%20Storytelling%3A%20The%20one%20who%20sets%20the%20price "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-needs-to-set-the-tariff%2F&text=Project%20Finance%20Storytelling%3A%20The%20one%20who%20sets%20the%20price "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/project-finance-storytelling-the-one-who-needs-to-set-the-tariff/&title=Project%20Finance%20Storytelling%3A%20The%20one%20who%20sets%20the%20price "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-needs-to-set-the-tariff%2F&title=Project%20Finance%20Storytelling%3A%20The%20one%20who%20sets%20the%20price&summary=In%20this%20episode%20of%20project%20finance%20storytelling%2C%20I%20tell%20you%20the%20story%20of%20Joseph%2C%20a%20financial%20modeler%20working%20for%20a%20private%20equity%20fund%20investing%20in%20wind%20power%20projects.%20through%20this%20story%2C%20I%20will%20tell%20you%20how%20to%3A%0D%0A%0D%0A%20%09change%20the%20model%20structure%20to%20have%20tar "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-needs-to-set-the-tariff%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-needs-to-set-the-tariff%2F&name=Project%20Finance%20Storytelling%3A%20The%20one%20who%20sets%20the%20price&description=In%20this%20episode%20of%20project%20finance%20storytelling%2C%20I%20tell%20you%20the%20story%20of%20Joseph%2C%20a%20financial%20modeler%20working%20for%20a%20private%20equity%20fund%20investing%20in%20wind%20power%20projects.%20through%20this%20story%2C%20I%20will%20tell%20you%20how%20to%3A%0D%0A%0D%0A%20%09change%20the%20model%20structure%20to%20have%20tariff%20as%20an%20output%20by%20defining%20a%20target "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-needs-to-set-the-tariff%2F&description=In%20this%20episode%20of%20project%20finance%20storytelling%2C%20I%20tell%20you%20the%20story%20of%20Joseph%2C%20a%20financial%20modeler%20working%20for%20a%20private%20equity%20fund%20investing%20in%20wind%20power%20projects.%20through%20this%20story%2C%20I%20will%20tell%20you%20how%20to%3A%0D%0A%0D%0A%20%09change%20the%20model%20structure%20to%20have%20tariff%20as%20an%20output%20by%20defining%20a%20target&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2021%2F09%2FCover-project-finance-storytelling-episode-2.jpg "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fproject-finance-storytelling-the-one-who-needs-to-set-the-tariff%2F&title=Project%20Finance%20Storytelling%3A%20The%20one%20who%20sets%20the%20price&description=In%20this%20episode%20of%20project%20finance%20storytelling%2C%20I%20tell%20you%20the%20story%20of%20Joseph%2C%20a%20financial%20modeler%20working%20for%20a%20private%20equity%20fund%20investing%20in%20wind%20power%20projects.%20through%20this%20story%2C%20I%20will%20tell%20you%20how%20to%3A%0D%0A%0D%0A%20%09change%20the%20model%20structure%20to%20have%20tariff%20as%20an%20output%20by%20defining%20a%20target "Vk")
[Email](mailto:?body=https://www.finexmod.com/project-finance-storytelling-the-one-who-needs-to-set-the-tariff/&subject=Project%20Finance%20Storytelling%3A%20The%20one%20who%20sets%20the%20price "Email")

Related Posts
-------------

![Unlocking the 3D Dimension of Financial Modeling: A Consultant’s Journey](https://www.finexmod.com/wp-content/uploads/2023/09/Unlocking-the-3D-Dimension-of-Financial-Modeling-A-Consultants-Journey-500x383@2x.png)

[](https://www.finexmod.com/unlocking-the-3d-dimension-of-financial-modeling-a-consultants-journey/)

#### [Unlocking the 3D Dimension of Financial Modeling: A Consultant’s Journey](https://www.finexmod.com/unlocking-the-3d-dimension-of-financial-modeling-a-consultants-journey/ "Unlocking the 3D Dimension of Financial Modeling: A Consultant’s Journey")

September 27th, 2023 | [0 Comments](https://www.finexmod.com/unlocking-the-3d-dimension-of-financial-modeling-a-consultants-journey/#respond)

![Project Finance Storytelling: The one who is balancing the balance sheet](https://www.finexmod.com/wp-content/uploads/2021/09/cover-500x383@2x.jpg)

[](https://www.finexmod.com/project-finance-storytelling-the-one-who-is-balancing-the-balance-sheet/)

#### [Project Finance Storytelling: The one who is balancing the balance sheet](https://www.finexmod.com/project-finance-storytelling-the-one-who-is-balancing-the-balance-sheet/ "Project Finance Storytelling: The one who is balancing the balance sheet")

September 21st, 2021 | [0 Comments](https://www.finexmod.com/project-finance-storytelling-the-one-who-is-balancing-the-balance-sheet/#respond)

[Page load link](https://www.finexmod.com/project-finance-storytelling-the-one-who-needs-to-set-the-tariff#)

[Go to Top](https://www.finexmod.com/project-finance-storytelling-the-one-who-needs-to-set-the-tariff#)