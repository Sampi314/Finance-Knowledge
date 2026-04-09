# An introduction to the Internal Rate of Return IRR

**Source:** https://pivotal180.com/internal-rate-of-return-irr

---

[Skip to content](https://pivotal180.com/internal-rate-of-return-irr/#fl-main-content)

Internal Rate of Return – IRR
=============================

By Haydn Palliser | May 19, 2021

**Internal Rate of Return (IRR)**
=================================

Overview
--------

This is an extract from our pre-course videos for our [renewable energy](https://pivotal180.com/course-type/renewable-energy-project-finance-modeling/)
 and  [project finance modeling course.](https://pivotal180.com/course-type/project-finance-modeling/)

Video
-----

**Video Transcript** 
---------------------

**Dan:** In the prior lesson we learned that an investment is worthwhile as long as the net present value is zero, or greater than zero. So when considering any potential investment, it can be useful to know what’s the discount rate that an investor would need in order to be happy with the investment, and the internal rate of return, or IRR, is simply that number. In essence, the IRR of an investment is the discount rate at which the net present value of all future cash flows is zero. And this is a really important concept, so let me say it again. The IRR is the discount rate at which the net present value of all future cash flows is zero.

**Haydn:** In the demo file from the prior lesson, if I could buy that investment for 5,000 and my discount rate is 10%, I would enjoy a net present value of $224. The NPV is a lot higher than zero, so the IRR on that investment must be higher than 10%. So to find it, I suppose that I could just keep typing numbers into the discount rate cell, increasing it by small increments, until the NPV is zero, but that seems widely inefficient.

**Dan:** No, please don’t do that. There is a much better way. Excel has a built-in function called IRR, and the configuration is incredibly simple. The formula is just equals IRR, and then open parenthesis, and then Excel expects you to select the range of cash flows to analyze. And here, the IRR function is way easier than NPV, because you don’t need to do anything special in time period zero. Unlike NPV, the IRR function is expecting that your first cash flows will be in time period zero, so you can simply select the full range of cash flows, starting in time zero, and then close your parenthesis, and press enter. So let’s do this so we can finally answer Hayden’s question. We will go into cell F21, and type equals IRR, and open our parenthesis, and then we will select the range from F8 to K8, close the parenthesis and hit enter, and what do we discover?

**Haydn:** If I can buy this investment for 5,000, I will achieve an IRR of 11.6%. So I was right, it would definitely be better than a 10% return.

**Dan**: Way better than 10%, and what would happen if you were to pay 5,224 for the investment?

**Haydn:** My NPV will go to zero.

**Dan:** Yes, of course, but we already knew this. What will happen to your IRR?

**Haydn**: If my NPV is now zero, then I guess my IRR will be 10%.

**Dan:** Exactly, let’s try that out. I’m going to go into cell F8, and change the investment price to 5,224. And look at that, the NPV is zero, an the IRR is 10%.

**Haydn:** Amazing!

**Dan:** Yeah, amazing. And if instead you could buy the investment for only 5,000, but your discount rate was 11.6%, what would be the net present value?

**Haydn:** Would it be zero?

**Dan:** Yes, why?

**Haydn:**  Because 11.6% is the IRR, and the IRR is the discount rate, which gives me an NPV of zero.

**Dan**: Yes. And we can change the numbers in the model to prove that that’s the case, and if the discount rate is higher than 11.6%, what’s going to happen to the net present value?

**Haydn**: Does it go negative?

**Dan**: Yes, it does. Let’s change the discount rate to 15% and you can see what happens. To reinforce the concepts that we just covered, we’d encourage you to take some time playing with the Excel demo. Modify the input values as you like, and see what happens. Eventually, these quantitative relationships will become second-nature to you. If you wanna understand what Excel is doing behind the scenes, just take a look at the formula below, right here.

Excel is just churning through a set of steps to examine all of the future cash flows, and then discount them to the present at a specified discount rate, and then take the sum, just like we did in that lesson on present value. And Excel is just going to keep changing that discount rate until it ultimately finds the discount rate that gives and NPV of zero. And that’s the IRR. Now, we will be using the IRR function a lot in this course because it’s incredibly handy for an investor. Basically, it allows anyone to examine an investment without precisely specifying a discount rate. You may not know the right discount rate to use, or maybe you don’t want to share your discount rate with other people in the market, but it doesn’t matter. You can simply look at the IRR of an investment and say, “That seems good enough for me.” Or, “No way, I need a higher return “for this kind of investment.” Basically, you just need a feel for the general vicinity of your discount rate. You don’t need to declare a precise number down to one or two decimal places.

Now when we talk about the IRR throughout this course, we’ll be talking about a few different forms and so we just wanna give you a quick preview. We will refer to an unlevered IRR, or an ungeared IRR, which is the IRR of a project on a stand-alone basis if we didn’t borrow money. But we can still calculate an unlevered IRR even if the project does borrow money, and this is helpful ’cause it really demonstrates how strong the project is itself, separate and apart from how much the returns are levered up, or geared up, because we borrowed money.

**Haydn**: We will also refer to a levered IRR, sometimes called a geared IRR, which specifies a returns to the equity investor. And sometimes, this is just called an equity IRR and the levered part is implied because we know that debt must be paid before there are any financial returns to equity. We can also look at an IRR before we calculate the impact of taxes due, and this is called a pre-tax IRR. Or we can look at the IRR after taxes are paid. This is called an after-tax IRR. And precision in language is very, very important if you want to make sure that people understand what you’re talking about. To avoid confusion, we would discourage you from presenting an IRR value without specifying whether it is levered, or unlevered, or pre or post-tax.

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Finternal-rate-of-return-irr%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Finternal-rate-of-return-irr%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Finternal-rate-of-return-irr%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#a897cac7ccd195c0dcdcd8db8d9be98d9aee8d9aeed8c1dec7dcc9c499909886cbc7c58d9aeec1c6dccddac6c9c485dac9dccd85c7ce85dacddcdddac685c1dada8d9aee)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Haydn Palliser

[https://www.linkedin.com/in/haydnpalliser/](https://www.linkedin.com/in/haydnpalliser/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/internal-rate-of-return-irr/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA