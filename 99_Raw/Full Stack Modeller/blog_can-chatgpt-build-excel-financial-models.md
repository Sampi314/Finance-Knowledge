# Can ChatGPT build Excel financial models

**Source:** https://www.fullstackmodeller.com/blog/can-chatgpt-build-excel-financial-models

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/1.png)

Can ChatGPT build Excel financial models?
=========================================

Published [by Freddy Teyssieux](https://www.fullstackmodeller.com/blog/author/freddy-teyssieux)

May 21, 2024 4:51:54 PM

To give more context, here is what I have been able to do in MS Excel with ChatGPT 3, 3.5, 4, 4o so far.  

1\. ChatGPT is right now unable to build an entire Excel Financial Model
------------------------------------------------------------------------

### 1\. A. ChatGPT struggles to perform the simplest tasks in MS Excel

To give more context, here is what I have been able to do in MS Excel with ChatGPT 3, 3.5, 4, 4o so far.

*   ChatGPT 3: As a beta-tester, I was able to perform mathematical operations, asking ChatGPT to pretend to be in a matrix 9x9 as a small snapshot of an MS Excel window. ChatGPT could not work with MS Excel initially, so we had to work around it.
*   ChatGPT 3.5: This version introduced the ability to plug in Excel files and provided Excel support to build and analyze formulas, extract insights (potentially generating text or charts in Python), generate dummy data, assist with VBA coding, generate user manuals, and helping with Power Query...
*   ChatGPT 4: Same as ChatGPT 3.5 with better results and the ability to develop GPT tools with contextual knowledge, extended memory …
*   ChatGPT 4.o: I only managed to produce direct formulas (4.o) for reference in the last version.

Here is a link to a video that attempts to replicate basic Excel financial projections using chatGPT 3.5 to give you a brief overview of challenges that you can come across :

[https://www.youtube.com/watch?v=7TdxNZ-2diQ&ab\_channel=BankRun](https://www.youtube.com/watch?v=7TdxNZ-2diQ&ab_channel=BankRun)

It is pretty hard to assess how fast ChatGPT will be able to be fully operational in MS Excel. Right now, ChatGPT is an additional layer (”a conversational layer”) between humans and a programming language that performs tasks in MS Excel (Python, VBA, Office Script …, etc.) to potentially give additional adaptability to the workflow.

ChatGPT error rate is still particularly high  :

*   on sequential actions (”dominos effect”): one minor effect leading to a series of errors;
*   on actions that require contextual knowledge of the model (ex, correctly plugging debt in the rest of the financial statements);
*   the vast amount of lines for the same operation (in the video, the principal repayment was not calculated past a certain period);
*   on second-order logic (ChatGPT will not build a module having in mind potential adjustment to integrate this new module);
*   thorough explanations to perform a task for humans but not for ChatGPT (the more I know ChatGPT, the more I appreciate my human colleagues…).

**1\. B. Building financial models is not always straightforward and cannot always be replicated easily through ChatGPT.**
--------------------------------------------------------------------------------------------------------------------------

As we all know, we do not just produce an Excel file when we build financial models. It is not a small task, as building financial models from scratch can take from a few hours (for the most vanilla ones with a great cup of coffee) to several weeks (depending on the complexity and the client's requirements). Building financial models is usually an iterative process involving back-and-forth with the clients and the rest of the stakeholders to arrive at the end product, a financial model.

Sometimes, we even need to break/adjust modules to accommodate new project directions, making it a non-linear/unintuitive process.

**1\. C. The entire process cannot be built using a single prompt but potentially hundreds.**
---------------------------------------------------------------------------------------------

The construction of a financial model cannot be achieved by a single prompt but rather necessitates using numerous prompts for different tasks, such as creating modules, adjusting parameters, saving files, and tracking changes. A single prompt cannot encompass the modelling process, requiring numerous, sometimes conflicting instructions. Here is an example using Python for Tokenomics Model to give you an illustrative example: [Example Model Framework with Tokenomics Model that leverages Python language](https://mirror.xyz/0xFD1b6961B8CDAcaE0bb35b0f1e78b46b900735af/V1ybyg0t8eNz8ADq5GiBQrhP3i_rRKOCtp_mkjH8j68)

The framework is not only purely ChatGPT but also with coding (ChatGPT interacts between humans and machines to provide the coding instructions to the machine). ChatGPT / AI is a hybrid solution that we couple with coding/automation to make it more user-friendly for humans. 

**1.D. Additional considerations in using ChatGPT in building financial models**
--------------------------------------------------------------------------------

It may be difficult to predict all the risks that may occur, but there would likely be at least four major risks :

*   Interface: How can the user and the AI interface with each other?
*   Black box risk: how can we measure if the AIs perform exactly as we intend them to do?
*   Data Privacy / Responsibility: How can we secure the integrity of the confidential data provided by our clients? Who should bear the legal responsibility in case of bad models, AI or modeller?
*   Memory / Accuracy: Anyone who talks with ChatGPT knows that AI has a short-term memory. Right now, AI tends to forget the data you provide and hallucinate on some occasions (they will probably be better in the future, considering how far we were compared to the first version of ChatGPT).

**2\. Where does that leave us with ChatGPT?**
----------------------------------------------

2.A.ChatGPT and Financial Modellers
-----------------------------------

ChatGPT will likely be leveraged in some capacity to build financial models if it has an advantage over financial modellers. ChatGPT can work faster than humans when provided with specific instructions and can be automated. In the future, they might also have the capacity or "experience" provided by thousands of models created. Most now view ChatGPT as a cheap, fast assistant that performs specific tasks decently enough to be used probably 10 to 20% of the time, depending on your use cases and under solid scrutiny.

The coding framework (5G, OfficeScript) may create an additional use case to leverage ChatGPT for us financial modellers.

2.B. ChatGPT and Financial Modeller User
----------------------------------------

The user may update the parameter values in a model while conversing with ChatGPT, potentially improving the user experience without risking breaking the model. Using GPT models, for example, you can even restrict the capacity for the user to access a portion of the model.

An example could be that you do not want the bank to access your master file, but the analyst can ask directly to perform a sensitivity analysis and print out the results.

Another example could be recording a meeting to update specific values; a ChatGPT model will interact with the model to update parameters.

**Final words**

The constant evolution of ChatGPT may increase its potential use in our workflow to build financial modelling. The modeler and User will then decide whether we can use it in some capacity.

VBA was created in 1993, and there is still potential backlash to its use in financial models (some of the reasons are legitimate). 

I am happy to have learned it and made an informed decision about when to use it. I think the same should be true for ChatGPT.

![Picture of Freddy Teyssieux](https://www.fullstackmodeller.com/hubfs/Freddy%20Teyssieux.jpeg)

### Published by Freddy Teyssieux

#### Community Members Of Full Stack Modeller | DeFi

This article was written and published by one of our Full Stack Modeller community members, FREDDY TEYSSIEUX. Freddy has over eight years of experience in finance, with a focus on project finance, renewable energy, and decentralized finance (DeFi). He is passionate about finding innovative solutions for financing sustainable and impactful projects, and leveraging the power of blockchain and smart contracts to create new opportunities for investors and entrepreneurs. I co-founded Finteam Consult, a boutique advisory firm that helps clients secure financing for their projects, ranging from infrastructure to tokenized real-world assets (RWAs). At Finteam Consult, he advises more than 30 projects for a combined financing amount of USD 1.3bn, covering various sectors and regions. He also co-authored a white paper on solving for secondary RWA liquidity, proposing a novel approach that combines proven methods from both DeFi and traditional finance. He uses his analytical skills, corporate finance knowledge, and market insights to deliver tailored and effective solutions for his clients, and to contribute to the development of the DeFi ecosystem.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fcan-chatgpt-build-excel-financial-models)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fcan-chatgpt-build-excel-financial-models)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fcan-chatgpt-build-excel-financial-models)
    

![Award_Winning](https://www.fullstackmodeller.com/hubfs/badge.jpg)

Become a Modelling Pro
----------------------

Join us and we'll unlock your full potential.

Our award-winning training programme, and exclusive global community, will guide you on your way to Excel, Financial Modelling, data visualisation & analytics mastery.

[Join as an Individual](https://www.fullstackmodeller.com/full-stack-membership)
 [Register Your Team](https://www.fullstackmodeller.com/team-training)

Latest Blogs
------------

*   [New Year, New You?](https://www.fullstackmodeller.com/blog/full-stack-modeller-new-year-new-you)
    
*   [New Import Functions](https://www.fullstackmodeller.com/blog/excel-importtext-importcsv)
    
*   [Best Practice Confessions & Terminology Overload](https://www.fullstackmodeller.com/blog/unpivot-episode-40-full-stack-modeller)
    
*   [Excel Meetup Groups](https://www.fullstackmodeller.com/blog/excel-meetup-groups)
    
*   [New Features and Common Data Problems](https://www.fullstackmodeller.com/blog/unpviot-episode-39)
    
*   [More AI Hype and Traps to avoid when modelling](https://www.fullstackmodeller.com/blog/unpviot-episode-38)
    
*   [The Excel World Championship Song](https://www.fullstackmodeller.com/blog/excel-world-championship-song)
    
*   [The Advanced Financial Modeler Certificate from FMI](https://www.fullstackmodeller.com/blog/advanced-financial-modeler)
    
*   [The history of Microsoft Excel](https://www.fullstackmodeller.com/blog/history-of-excel)
    
*   [My main learning from the FMI AFM exam](https://www.fullstackmodeller.com/blog/financial-modeling-institute-fmi-afm-learnings)
    

#### Subscribe to our monthly modelling newsletter