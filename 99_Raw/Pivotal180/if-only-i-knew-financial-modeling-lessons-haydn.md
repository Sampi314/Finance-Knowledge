# Things I'd wish I knew before starting in Financial Modeling

**Source:** https://pivotal180.com/if-only-i-knew-financial-modeling-lessons-haydn

---

[Skip to content](https://pivotal180.com/if-only-i-knew-financial-modeling-lessons-haydn/#fl-main-content)

If Only I Knew! – Financial Modeling Lessons from a (slightly) grey-haired Project Finance Advisor.
===================================================================================================

By Haydn Palliser | December 5, 2019

I love project finance. Maybe it’s the engineer in me, but the combination of a physical asset and a highly-structured and complex investment excites me. Add to that the importance of infrastructure and energy to our daily lives, and I am hooked.

Well, that’s part of it. Perhaps the biggest reason (or the geek in me) is that I fell in love with the financial modeling aspect. I didn’t actually touch a financial model in my first year of project finance, but once I did I have never looked back. Other than to rue what I wish I knew when I started.

Since those early days I have trained over a thousand analysts in renewable energy, infrastructure, and mining project finance. Some of those being my colleagues where I worked, and others in training programs that I have delivered globally, or in my class in renewable energy project finance modeling that I teach at Columbia University with [Daniel Gross](https://t.sidekickopen06.com/s1t/c/5/f18dQhb0S7lM8dDMPbW2n0x6l2B9nMJN7t5XWPfhMynW4X9JTq63K9pRN56dVnnK_9gW102?te=W3R5hFj4cm2zwW4mKLS-3ZWVWBW3K2-zv1JxwY5W1Lyz993H3b41W3K6c4Z49PHckW1G8GmZ1S2FdY1V3&si=8000000001685583&pi=85e3d0ec-0657-402f-baae-253bf926a3c5)
.

Having grown two relatively large financial modeling teams, I also have a view of the type of person that makes a good analyst (for you hiring managers), but that will come in my next blog. For now, I want to focus on my 5 most important lessons for the new analyst, that I try to teach.

**Lesson 1: Understand the transaction and plan before you start modeling**
---------------------------------------------------------------------------

It’s a common trait of a new analyst to jump into Excel and get started, showing their new found speed. Perhaps they just completed a financial modeling training course and want to show off their favorite shortcuts. But don’t, please don’t. Make sure you read the information memorandum, or other available information first. Who is investing and why? What are the possibly financial structures and which ones are more likely?

Plan the financial model out. Sketch out the structure and the contents. Don’t figure this out later as it may require wholesale restructuring of your model. Your boss (or client) reviewing a constantly changing model structure will not be your biggest fan.

**Lesson 2: Best practice financial modeling does actually matter**
-------------------------------------------------------------------

Best practice is mostly about making a model clear and easy to understand, with the flexibility required for the deal. So keep it simple and follow the common rules widely-recognized in the industry. And for what it is worth, of the more technical of these, the ones that had the most profound impact on me were:

*   Learning how to create scenarios and sensitivities properly (see our webinar [here](https://pivotal180.com/scenario-sensitivity-blog-post-part-1-haydn/)
    )
*   Any calculation limited to a specific timeframe or triggered by an event deserves a binary flag.
*   When you have a volume to record (or measure) over time, build a control account – see a course sample on this topic [here](https://pivotal180.com/?p=1925)
    

It goes without saying that the model needs a great summary page, so an investment decision can actually be made…

**Lesson 3: Best practice only goes so far….check your work….and use my checklist if you don’t have one**
---------------------------------------------------------------------------------------------------------

Garbage in garbage out. Check your work, after EVERY SINGLE LINE. Going back to ‘fix something tomorrow’ will cause you even more pain tomorrow. Fix it now.

These are the guidelines that I wrote down and stuck to my desk as an analyst:

*   Press F2 in every row to review the cell precedents, is the cell correctly linked
*   Check the beginning and end of the row (do the values stop and start at the right time)
*   Check the trend of the line, do the values increase / decrease over time as expected? Create a graph if needed
*   Change the inputs:
    *   For values directly from an input source:
        *   Make the input value negative, zero, and positive (if feasible) to check you still get the right answers
    *   For dates directly from an input source
        *   Make the input date the 1st day, middle day of, and the last day of the period
    *   For cash flows dependent on other cash flows (i.e. Cash available for debt service is dependent on revenue and costs etc)
        *   Consider if this ‘input’ could be negative, zero, or positive
*   Run boom/bust scenarios
*   Reconcile your results to another model, if available
*   Print the outputs and review them….yes, I am old

You will still make errors, we are human. I will never forget the worst error I ever made. Project finance models are complicated. So get your model checked!

**Lesson 4: You can run comparisons between versions of a spreadsheet!**
------------------------------------------------------------------------

This one is surprisingly not well known, particularly in the US. You can run a compare to check every formula and output change between two versions of a model. How every company doesn’t have this I don’t understand.

I use this myself for my own models, because I often forget all of the changes I may have made, and I want to know exactly how much the results changed in each step. I may be a cynic, but I want to see the comparison rather than trust my analyst who had 3 hours sleep the night before and changed a model with over 3,000 formulas….sorry.

If you want to know more about how to run comparisons, please contact [me](https://pivotal180.com/?page_id=167)
.

There are of course other add-ins that are useful, such as for tracing dependents and precedents, including [Macabacus](https://t.sidekickopen06.com/s1t/c/5/f18dQhb0S7lM8dDMPbW2n0x6l2B9nMJN7t5XWPfhMynW4X9JTq63K9pRN56dVnnK_9gW102?te=W3R5hFj26QkH9W3z8mm-3z8p75W1JxwY51Lxh-yn4fPf-t273&si=8000000001685583&pi=85e3d0ec-0657-402f-baae-253bf926a3c5)
, or BPM Traverse’s tool now under [Modano](https://www.modano.com/)
.

**Lesson 5: Ask questions, beyond what is solely within the mod**
-----------------------------------------------------------------

I have met many analysts who have modeled a number of renewable energy projects, but don’t know what a capacity factor really is (other than plugging it into the model). Or perhaps what a dispatch curve is, why capacity or availability payments make sense, or what P50 and P99 forecast really represents. Or they read the legal documents scanning only for the financial terms required for the model. You need to understand the broader picture to be a good financial modeler and certainly good within project finance

If you get a chance, visit the site of the project  context is a wonderful thing.

**Summary**
-----------

You may read all of this, and still make the same mistakes I did (I only hope not quite as many!), but we do learn best from our own mistakes.

One way we can help at Pivotal180 is to provide training that goes beyond just modeling. We provide deal training, helping you understand all of the core documents and concepts behind your renewable energy, or infrastructure project finance deal. Take a look around our courses [here](https://t.sidekickopen06.com/s1t/c/5/f18dQhb0S7lM8dDMPbW2n0x6l2B9nMJN7t5XWPfhMynW4X9JTq63K9pRN56dVnnK_9gW102?te=W3R5hFj4cm2zwW45Q4Dk4fDXYtW22TG2w43T4NQW3ZY1D943XxsQ4mMrG1&si=8000000001685583&pi=85e3d0ec-0657-402f-baae-253bf926a3c5)
 if you would like to know more.

Happy modeling!

Check out our brand new [Financial Modeling Fundamentals Course](https://pivotal180.com/courses/financial-modeling-fundamentals/)

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fif-only-i-knew-financial-modeling-lessons-haydn%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fif-only-i-knew-financial-modeling-lessons-haydn%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fif-only-i-knew-financial-modeling-lessons-haydn%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#635c010c071a5e0b17171310465022465125465125130a150c17020f525b534d000c0e4651250a054e0c0d0f1a4e0a4e080d06144e050a0d020d000a020f4e0e0c07060f0a0d044e0f0610100c0d104e0b021a070d465125)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Haydn Palliser

[https://www.linkedin.com/in/haydnpalliser/](https://www.linkedin.com/in/haydnpalliser/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/if-only-i-knew-financial-modeling-lessons-haydn/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA