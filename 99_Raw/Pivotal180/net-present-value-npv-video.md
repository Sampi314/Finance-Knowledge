# Net Present Value NPV most widely used term in finance

**Source:** https://pivotal180.com/net-present-value-npv-video

---

[Skip to content](https://pivotal180.com/net-present-value-npv-video/#fl-main-content)

Net Present Value (NPV )
========================

By Daniel Gross | December 5, 2019

Overview
--------

This is an extract from our pre-course videos for our renewable energy and infrastructure project finance modeling course.

Video
-----

**Video Transcript** 
---------------------

**Dan:** In the demo file, you’ll recall that we calculated discount factors year by year and then we discounted all of the future cash flows to the present one at a time and then we added all of those present values together using the SUM function and that’s how we produce the NPV. And that approach totally works but it’s inefficient and not surprisingly, Excel has a built in function that will eliminate a lot of steps and make it much easier to calculate a net present value and not surprisingly, that function is called NPV for net present value.

**Dan:** Let me first explain how the function works and then we’ll walk through an example and the demo file. To enter the function into Excel, you just type equals NPV and then open parentheses and inside the parentheses Excel first asks you to specify the applicable discount rate and this is followed by a comma and then Excel asks you to indicate all of the cash flows that you want to discount and then you close the function.

**Dan:** Now you’ll recall that we don’t need to discount a cashflow that occurs in year zero. By definition, this is already a present value because times zero is today, but Excel is expecting that the first cash flow will be one year into the future. So if you want the NPV calculation to be net of that initial investment at time zero, you need to take that into consideration outside of the NPV function. So in our demo we will need to subtract that $5,000 from the value that we get when we apply the NPV function to the cash flows from year one through your five. So let’s jump back into that demo file. In cell F19 I will insert a formula: equals NPV open parentheses and then I will select the discount rate, which is in cell D6. And then I type a comma and then I select all of the future cash flows starting in year one.

**Haydn:** And it’s really important to remember that the NPV function is not equipped to handle anything from time zero. You need to deal with that separately.

**Dan:** Yes. So I will select all of the future values and then close out the parentheses. And if I hit enter, I see the value of 5,224 which is the present value of all of the future cash flows.

**Haydn:** That’s also the maximum amount that I was prepared to pay for the investment.

**Dan:** Yes, and if you want to subtract the $5,000 investment costs in order to see the net present value, net of the upfront investment, you go back to cell F19 and you add plus F13 which will subtract the initial investment of 5,000, and now the NPV is exactly the same as we calculated using the method in the prior lesson, which broke down that calculation into so many separate pieces. Excel’s NPV function is just so much simpler and going forward in the course we’ll be using the NPV function a lot. So what’s the key insight here? I think there are really two. The first is that a discount rate is equivalent to a hurdle rate or a cost of capital for an investor.

**Dan:** Something to keep in mind is that every investor is going to have their own discount rate and every investor should applied different discount rates for different kinds of investments. High risk investments should be discounted at a higher value and lower risk investment should be discounted at a lower discount rate. Essentially, investors apply a concept known as a risk adjusted cost of capital or a risk adjusted discount rate. And Haydn, what’s the second point?

**Haydn:** Well, an investment is worthwhile if the net present value of that investment is greater than zero, even though that sounds completely counterintuitive, if you think about it, it makes perfect sense. We take the present value of all of the future cash flows and we discount them at the appropriate risk adjusted discount rate. This amount is equal to the cost of our initial investment. Then we’ve hit our 10% requirement, and that’s all we need. But Dan, I still want to know the answer to my earlier question. What is my financial return if I buy the investment for 5,000 and take home at additional 224. I know it’s greater than 10% but how much more?

**Dan:** Well, you’re in luck, Haydn, because that’s exactly where we’re going in the next lesson.

Enroll in a Pivotal180 course! We offer a range of training programs for modelers of different backgrounds and experience levels:

[Renewable Energy Project Finance Modeling](https://pivotal180.com/course-type/renewable-energy-project-finance-modeling/)

[Project Finance Modeling](https://pivotal180.com/course-type/project-finance-modeling/)

[Introduction to Project Finance Modeling](https://pivotal180.com/course-type/introduction-project-finance-modeling/)

[Financial Modeling Fundamentals](https://pivotal180.com/course-type/financial-modeling-fundamentals/) 

[Tax Equity & Hybrid Financial Modeling](https://pivotal180.com/course-type/tax-equity-hybrid-financial-modeling/)

Have questions? Reach out anytime at [\[email protected\]](https://pivotal180.com/cdn-cgi/l/email-protection) 

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fnet-present-value-npv-video%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fnet-present-value-npv-video%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fnet-present-value-npv-video%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#b986dbd6ddc084d1cdcdc9ca9c8af89c8bff9c8bffc9d0cfd6cdd8d588818997dad6d49c8bffd7dccd94c9cbdccadcd7cd94cfd8d5ccdc94d7c9cf94cfd0dddcd69c8bff)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Daniel Gross

[https://www.linkedin.com/in/daniel-gross-081237b/](https://www.linkedin.com/in/daniel-gross-081237b/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/net-present-value-npv-video/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA