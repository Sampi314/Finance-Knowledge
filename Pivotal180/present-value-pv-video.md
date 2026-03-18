# Present Value PV concept of present value

**Source:** https://pivotal180.com/present-value-pv-video

---

[Skip to content](https://pivotal180.com/present-value-pv-video/#fl-main-content)

Present Value Math (PV)
=======================

By Daniel Gross | December 5, 2019

Overview
--------

This is an extract from our pre-course videos for our renewable energy and infrastructure project finance modeling course.

Video
-----

**Video Transcript** 

**Dan:** Let’s consider the concept of present value.

**Dan:** The idea is this: payments that are received in the future are worth less to us than payments that are received today. If you think about that, I would rather have the money now and do something with it than get it a year from now. Or alternatively, if I have some money now and I choose not to spend it, I can invest it and then I would expect that the investment would grow over time. Essentially, the concept is that future payments need to be discounted back to the present in order to determine a point of indifference or equivalent. When investors make investment decisions, what they’re really doing is taking the expected future cash distributions and discounting them back to the present. So basically they want to figure out how much money they’re willing to pay today for an investment that will provide them with some cash in the future. I’ll use an example to help translate this into numbers. Let’s take an investor and we’ll call him Haydn. Hi Haydn.

**Dan:** Haydn has the lucky opportunity to receive a payment of $107 exactly one year from now, that 107 is called a future value or FV and let’s assume that Haydn’s discount rate is 7%. So how could he calculate what that future dated $107 it’s worth to him in today’s terms or more precisely, how could he calculate the present value or the PV of that opportunity? Well, an investor like Haydn would simply take the future value, which is 107 and divide it by 1+the discount rate, which is often abbreviated as R. In this case, 1+R is simply 1.07 thus that $107 in the future would be worth $100 today in the present. Haydn, how much would you be willing to pay for an investment that will deliver $107 to you one year into the future?

**Haydn:** Um, $100 is this a trick question or is it really that simple?

**Dan:** No it’s really that simple, but we can make it a little bit more complicated by asking how much you would be willing to pay for an investment that’s expected to deliver $107 two years into the future. How would you think about that one, Haydn?

**Haydn:** Well I know is that $107 received one year into the future is worth only $100 to me today. So I suppose I just have to discount that $100 at the 7% discount rate for a second year?

**Dan:** Exactly! So let’s take that $100 which is a one year future dated cashflow and then divided by 1.07 which you will recall is 1+the discount rate or 1+R and that equals $93.46. So Haydn, would you be willing to invest $93.46 today for an investment that delivers $107 two years into the future?

**Haydn**: I mean, sure, but I would have made that decision a lot more quickly just by simplifying the calculation. Can’t I just take the future value of 107 and divide it by 1+R raised to the power of 2, because I’m just counting for two years?

**Dan:** Yes, you can! And if you had to wait five years before receiving that future value, you could just discount it by 1.07 raised to the power

**Haydn**: … 5!

**Dan:** The classic formula for discounting is that the present value is equal to the future value divided by 1+R raised to the power N, where N is the number of years into the future.

**Haydn**: Okay, Dan, this is all well and good if we’re only looking at a single cash inflow sometime in the future, but the types of investments that we’ll be talking about in this course have much more complicated cashflows. We’ll be talking about 20 or 30 or even 40 years of operations paying dividends out over many years long into the future and we need to figure out a present value of all of that stuff in order to consider whether it’s worthwhile to invest in the project.

**Dan:** Yes, we do, but chill out. It’s actually not that hard. The concept is still the same. Basically every individual distribution that will be paid to the investor needs to be discounted back to the present in order to figure out a net present value of the investment. The challenge is that each of those individual cash distributions needs to be discounted by a factor which corresponds to a number of years into the future when the cashflow is going to come to us and that’s the demo file we’re about to go through together in Excel. When you open the file, you’re going to see something that looks like this. It’s a worksheet divided up into an input section which is labeled in gray, a calculation section which is labeled in blue and an output section which is labeled in red, and this organizational structure is really a best practice which you should always aim to do when setting up a model.

**Dan:** You can obviously pick your own colors, but be sure to clearly separate and label inputs and calculations and outputs. In the input section. You can see that the worksheet specifies an annual discount rate of 10% and the worksheet provides a counter indicating the year in which the cashflow occurs. So we start with your zero, which means the present and we extend out five years into the future. The goal of the exercise is to take each of those future values; 1,000 in year one, 1,300 in year two, 1,500 in year three, etc., and we’re going to discount them all back to the present. Now before you get started, take special note of how we express the cashflow in year zero. Do you see how it’s written as a negative number as -5,000 this is because the 5,000 is a cash outflow from the perspective of an investor. Haydn needs to forgo $5,000 today in order to make an investment which is expected to pay him that schedule of future cashflows over the next five years.

**Haydn:** This is another best practice which we will use consistently throughout the course. Positive numbers indicate cash being received by an investor. So positive numbers should be used for things like dividend distributions received by an investor or cash proceeds received from exiting or selling an asset. And negative numbers should be used for expenses paid or investments that require the use of cash.

**Dan:** And with that, let’s open up the model and get to work. In the calculation section, we need to do some work on row number 12. We’re asked to calculate the discount factor for each of the five years. And that discount factor is just the denominator from the discounting equation that we just discussed. For a future value received five years into the future, that discount factor would be 1+R raised to the power 5, and for future values received one year into the future, it would be 1+R raised to the power 1. So when we want to write an equation that is 1+R raised to the power N, what we really want to do is take 1.10 and raise it to the power of the year that’s indicated on row 7. So what equation should I enter into Cell F12? Well simply, =D6, which is the 10% discount rate raised to the power of F7, which is the year. Now to make sure that everything looks okay, I can click into cell F12 and press the function key F2, and what the function key does is it shows me that Excel is taking 1+ the value indicated in the blue box, which is our 10% discount rate, and it’s raising it to the power of the number in the red box, which is the year.

**Dan:** Now it may seem a little odd that the discount factor is 1.0 in year 0 but what that means is we don’t have to discount the $5,000 cashflow at all because year 0 is the present. It’s a convenient fact that when you raise any number to the power 0, you got 1. Now once I’ve got that formula, I want to copy it across the row and towards the right, but I have a problem: if I copy it using the shortcut ctrl+C and then paste it into column G using the shortcut ctrl+V, you’ll see that my formula is no longer incorporating the 10% discount rate. Excel is attempting to pull the number from one column to the right of the discount rate, and I can see this by clicking into the cell and pressing F2. Excel has taken 1+ the value in the blue box, which is not our 10% discount rate, and it’s raising that to the power of what’s in the red box, which is 1.

**Dan:** So, how can we fix this problem? We fix it by anchoring the formula. I need to indicate that when I copy to the right, I always want to be using cell D6 for the discount rate. So, I can go back to my original formula and highlight the cell reference to D6 and insert a dollar sign before the D so that I have what’s known as an absolute cell reference for the column. Now a best practice shortcut would be to select the reference to D6 in my formula bar and then press F4 if I’m on a PC (so function key four), or if I’m on a Mac command+T, and that will cycle through all of the various anchoring options like I’m doing now. Now, once we’ve anchored our formula, we can now copy it to the right using ctrl+ C to copy and then selecting all of the destination cells and using ctrl+V to paste. And here you can see that we’ll be discounting the cash dated one year into the future by a factor of 1.1 whereas cash five years into the future is discounted much more steeply at 1.61. But let me erase that whole line and show you a shortcut. If I simply select a range by starting with the cell containing the formula that I wish to copy and ending at the end of the row, I can simply type ctrl+R and that formula will be copied to the right and this shortcut is the same in PC and Mac (ctrl+R). Now, no worries if you want to stick to copy and paste those work just fine, but copy right will save you an extra step. Now moving onto row 13 of the calculation section. Here, we’re going to divide each of the future values up in row 8 by the year specific discount factors that we calculated. So in cell F13 we will divide the future value in cell F8 by the discount factor that’s in cell F12. So I will go back into cell F13 and press the F2 key again, so we can see that the red box and the blue box point to the correct places. And now we can copy this formula across the row and there’s no need for any kind of anchoring because we want all of our cell references to be relative. As we copy that formula to the right, we want to be using values from each subsequent column to the right.

**Dan:** And now that we’ve calculated the present value of each of the future value cashflows, we have enough information to determine the net present value of this entire investment. So we’ll want to place this value right here in the output section of our model because this is a key number that the investor really cares about. We’ll take the sum of all of the present values from the anticipated future cash distributions and we’ll add them together. But we also need to include that initial cash outflow, which was our upfront investment. We call it net present value to indicate that the value to the investor is net of the cost of making the investment. So what should we enter into cell F17? Well, that formula is simply =sum of the range F13 to K13.

**Dan:** And this tells us that after factoring in the 10% discount rate and the $5,000 investment cost, the investment provides an additional $224 in value to us. Now let’s step back and think about what this really means. If our discount rate is 10%, we have achieved more financial returns than we actually need. Our net present value analysis told us that this investment would repay the full $5,000 upfront investment plus a 10% annualized return plus $224 but all we needed was the 10% return. We didn’t actually need that extra 224. Actually, we should have been happy with a net present value of zero.

**Haydn**: Wait, what? Did you just say you’d be happy with a net present value of 0? That does not sound right Dan.

**Dan:** Yeah, I know it sounds completely crazy, but it’s true. If you have an appropriate discount rate to match the risk of the investment, than any investment that has a net present value of zero, or slightly greater than zero, totally hits your hurdle rate. That 10% return is already factored into our math. So Haydn, I have a skill testing question for you. What’s the maximum that you would be willing to pay for the investment in that demo file? Is it $5,000?

**Haydn:** Well, I would certainly be willing to buy it for $5,000 if someone would actually sell it to me for that price, but I guess it would be worth 5,000 + 224 because if I also invested that extra 224 in year zero, then my NPV would be 0. and I would still receive my 10% return. Exactly 10% and I guess that’s all I need.

**Dan:** Yes, exactly. So let’s test it out. If we increase the purchase price of the investment in cell F8 to 5,000 + 224, you’ll see that the net present value is indeed 0, so that’s the most that you should pay.

**Haydn**: Cool! I can see how cell F17 is 0 so my net present value will be 0 if I pay 5,224. But let’s change that purchase price back to where it was because you told me, Dan, that I could buy the investment in the market for only $5,000 and if I can buy the 5,000 then I’m guessing my actual financial return will be higher than 10% which would be awesome. The big question I have for you though is exactly what would our return be?

**Dan:** Well, that’s an excellent question, Haydn, but you’re jumping ahead. What you’re asking about is the internal rate of return of this investment, which is commonly called the IRR. So just stick with me and I promise we’ll get there. But first I need to walk us through a more efficient approach to calculating net present value in Excel. And that will come in the next lesson.

Enroll in a Pivotal180 course! We offer a range of training programs for modelers of different backgrounds and experience levels:

[Renewable Energy Project Finance Modeling](https://pivotal180.com/course-type/renewable-energy-project-finance-modeling/)

[Project Finance Modeling](https://pivotal180.com/course-type/project-finance-modeling/)

[Introduction to Project Finance Modeling](https://pivotal180.com/course-type/introduction-project-finance-modeling/)

[Financial Modeling Fundamentals](https://pivotal180.com/course-type/financial-modeling-fundamentals/) 

[Tax Equity & Hybrid Financial Modeling](https://pivotal180.com/course-type/tax-equity-hybrid-financial-modeling/)

Have questions? Reach out anytime at [\[email protected\]](https://pivotal180.com/cdn-cgi/l/email-protection) 

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fpresent-value-pv-video%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fpresent-value-pv-video%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fpresent-value-pv-video%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#cdf2afa2a9b4f0a5b9b9bdbee8fe8ce8ff8be8ff8bbda4bba2b9aca1fcf5fde3aea2a0e8ff8bbdbfa8bea8a3b9e0bbaca1b8a8e0bdbbe0bba4a9a8a2e8ff8b)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Daniel Gross

[https://www.linkedin.com/in/daniel-gross-081237b/](https://www.linkedin.com/in/daniel-gross-081237b/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/present-value-pv-video/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA