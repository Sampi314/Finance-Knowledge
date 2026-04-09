# Real Estate Development Modeling: Equity, Debt Draws & Repayment

**Source:** https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-development-modeling

---

Real Estate Development Modeling Tutorial: Equity, Debt Draws, and Optional Repayment
=====================================================================================

In this lesson, you’ll learn how to allocate the funds required between equity and debt tranches, and how you can ensure that the proper amounts are drawn each month. You will also learn how to project optional debt repayments.

 Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-development-modeling/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-development-modeling/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-development-modeling/#tab-signup)
    

#### Equity, Debt Draws and Optional Repayment Transcript

In this lesson we’re going to go into our equity and debt draws for this construction project, and you’ll learn how to estimate how much an equity and debt, we’re drawing on each month. And then if we happen to have any extra cash flow available, how much of that we can actually use to repay some of this debt early, which of course is going to help us, the developer or the equity investor in the project, because it’s going to allow us to reduce our interest expense and our capitalized interest on that debt.

As with much of the rest of this model, if you’ve already been through the LBO models elsewhere in this course, these formulas will seem very familiar to you. Because conceptually, the way we set them up, is actually very similar to what you do in an LBO model, when you’re determining the optional debt repayments. So at least this part here at the bottom, for optional debt repayments, is going to be similar to what you’ve seen, before if you’ve been through those models.

![Real Estate Modeling](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Learn Property Modeling from A to Z with the **BIWS Real Estate Modeling Course**

*   #### Evaluate property developments and acquisitions
    
    You’ll assess the risks and rewards and make investment recommendations
    
*   #### Master financial modeling
    
    You’ll build office, retail, hotel, industrial, multifamily, and pre-sold condo models
    
*   #### Complete 11 case studies
    
    Build 6 shorter “crash course” models and 5 detailed “on the job” ones
    

[Full Details](https://breakingintowallstreet.com/real-estate-modeling/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Real-Estate-Modeling-Course-Outline.pdf)

\[01:00\]

Now to get started with the equity and debt draws remember how this works. Ideally, we’d like to use our own funds first the developer equity here, to fund everything that we can. Now we only have approximately $1.8 million of developer equity, so past a certain point, we’re going to have to start drawing on investor equity, and then mezzanine, then the senior notes after that.

So, that is the order of drawing here. The order of repayment is going to be different. We’re going to start with Term Loan A, then B, then mezzanine. That, once again is because the mezzanine debt holders are taking the most risk, so they are going to have the highest potential reward.

If you think about this accounting-wise, they are going to get a higher return if we end up paying more interest on mezzanine. And so as a result, we’re going to have to repay other forms of debt first, before we get to the mezzanine. That’s going to allow the mezzanine investors here to get a higher return, because their debt will be outstanding for a longer time period. So for the equity and debt draws here, basically we are going to draw on the equity or the debt in one of two ways.

\[02:00\]

First off we can look at the funds required, for the development and operation of this business, of this property really, and then we can subtract however much, we’ve drawn on so far. So for example, if we’re at the mezzanine line item, we can look at our funds required, and then we can subtract what we’ve drawn on for our developer equity and investor equity, whatever is left, is what we have to draw on for our mezzanine, right here.

Now there is a problem with that, which is what if we exceed our maximum draw right here? So the other factor we have to look at is how much we have drawn on so far, and what our maximum draw is. We have to look at those, and compare them to how much we actually require, and then what we’ve drawn on so far, in other types of equity or other types of debt.

So that’s the basic idea behind the formulas here. It looks a little bit intimidating when you first see it, but it is actually not that difficult to understand. So what we’re going to do here is take the minimum between the funds required, which I’m going to anchor, at least the row part of that cell (i.e. row 104 which lists the total funds required), and then we’re going to subtract however much we’ve repaid, so far.

\[03:00\]

Now in this case it is simply zero, because developer equity is the first one. But just to make sure this formula is correct I’m going to select this area of F105 to F106. And I’m going to anchor the row 105 part of F105 cell, right there. So that’s the first thing we need to consider.

Again, this is basically the funds that we require minus however much we’ve drawn on through other tranches or other types of equity, so far. Then the other thing we need to look at is our maximum draw, over here, so the D107. We’re going to anchor the column part of that, the D, and then we’re going to subtract the sum of E107 to E107.

We are doing it this way, because once again, we need to subtract however much we’ve drawn on, so far. So let’s hope we get into a scenario where we have $1 million of funds required, and so far we have drawn on $700,000, out of a max draw of $1.8 million of total developer equity (i.e. developer equity max draw amount), here.

\[04:00\]

Well, in that case, what’s going to happen here is that our maximum draw remaining, would only be $900,000 there. So here, it would default to this part of the formula, the D107 minus the sum so far, because that would be equal to $900,000. And then this part would be equal to the $1.0 million in funds required, minus however much we have drawn on elsewhere, which is zero for now, because this is the first item that we’re considering, the developer equity.

So, that’s really how it works. The first part is just the funds required, minus what we’ve drawn on so far elsewhere, and then the second part the maximum, minus however much we’ve drawn from there. We can never exceed our max draw, so that’s why we need to add this check in place. Just close the parenthesis, for now. So we have that formula.

Now if you’re wondering about one additional point here which is, “Wait a minute. What happens if our funds required, minus the repayment, so far is negative? Or what happens if the D107 minus the sum so far, what if this is negative? Aren’t we then going to be drawing on a negative number? Does that even make any sense?”

\[05:00\]

The answer is that, unlike a traditional LBO model, it’s not really going to happen here, because of the way we’ve set this up. What we’re going to do in this model is work backwards, and then go back to our sources and uses, and make sure that we always have enough to draw on, to actually repay these amounts.

So the short answer is that the funds required minus the amount repaid so far, this is never going to be negative, because it’s not like an LBO where we might have a revolver, and mandatory debt repayments, and those mandatory debt repayments might exceed our cash flow available, to repay debt, turning our number negative, so it’s not like an LBO model.

So this part is not going to turn negative, it’s only either going to be positive or zero. And then the second part also cannot really turn negative here. So we could include a MAX formula around our existing formula, and then a zero function around this. But I’m actually going to leave it out here, because it’s not necessary in this case. In the LBO model the MAX formula is wrapped around the MIN function as a safety precation, but in this real estate development model that is unnecessary.

And before I copy this formula across, one thing I want to fix here is this E107 to E107 sum, I’m going to anchor the column part of that, so it doesn’t shift around, that’s really important. So now, let’s copy this around.

\[06:00\]

And now we can see that we have this circular reference calculate, here at the bottom. You can see that we are gradually drawing on this debt and equity over time, and gradually shifting from one to the other. You can also see that our interest expense here is now positive, and is generally increasing over time, until it reaches around $440,000, each month here at the end.

You can also see that now our equity and debt balances are changing correctly right here. And basically, what’s happening is that we go up to the maximum draw, on each one of these. Then when we reach that maximum draw then we are done, and we get to our maximum debt and equity amount, of around $80.5 million or $80.6 million, right here.

Now just to show you with the capitalized interest, I will once again set up a frame here, so you can see some of this a little bit better. So with the capitalized interest here, let’s see what’s going on now you can see that it is being capitalized in the construction phase of the project, for the mezzanine, for senior notes B, and for senior notes A.

\[07:00\]

And then once we hit the end of construction, that’s when we stop capitalizing the interest, it goes to zero right here. Of course, this is not really accurate. What really happens is that we will shift over the interest, and it’ll start going into the operating deficit, instead. Right now the operating deficit is not linked correctly, because up above on our income statement we have not linked our interest expense to our net income, so we’ll need to come back and do that after this lesson.

But that’s effectively what’ll happen here. After the end of the construction period, interest won’t be capitalized per say, but it will be added to our operating deficit and the operating deficit, in turn, will add to our debt and equity balances and our maximum draws.

Now in terms of the draws themselves, let’s just take a look at what’s going on here. So developer equity we’re drawing it for the first three months, mostly to pay for the land actually, if you think about the numbers here.

Then we’re drawing on investor equity, up to the maximum amount. Then when we can no longer afford investor equity, that’s when we switch to mezzanine. We draw on that. You can see it’s mostly being used to finance the hard cost of construction here.

\[08:00\]

Then we go to senior notes; then we go to the next tranche of senior notes. We don’t really use these quite as much, because by the time we get to these we’re almost at the end of construction. So then there we sort of switch over and we start paying a much lower amount, because our funds required are simply not as high in this case.

And we can see we have a problem here, because in the final year of this our total capital drawn. Let me just go in, and make that calculation right now. Copy this all the way across. So we have a problem here, because at first our capital drawn, and our funds required all match each other in these early years, all the way really up through, the end of the construction on the project.

As you go across here, you’ll see that these two rows will always match each other. Then here at the end, is when we get into a problem. Because now our funds no longer match each other, so our funds required exceed our total capital drawn. The reason this happens and the reason why we get this problem in the model, is because of our capitalized interest and also our origination costs and taxes, and our operating deficit, right here.

\[09:00\]

Back on our sources and uses schedule, we have not added to these to our total uses, yet. As a result, our total sources here are off and we need to increase the amount of mezzanine, senior notes B, senior notes A, and equity that we are drawing on, or could potentially draw on right here. So that is the issue, the fact that these are not yet linked in, correctly.

What can we do to actually fix this, so we can get the correct numbers? Well, the easiest thing to do here to actually fix this is to go back to our sources and uses schedule, and what we can do is add in a check here and say that; IF we have a circularity breaker enabled; we’re going to say zero to do a hard reset.

We could also check for circularity itself and if that is set to no, then we could also do a hard reset. I’m just going to do it this way, so if we have a breaker it’s set to zero to avoid a circular reference, here. Otherwise we’re going to sum up everything on our statements, for the capitalized interest, right here.

\[10:00\]

We have that. Then the same thing for origination costs and taxes, same thing for operating deficit, so for origination costs and taxes, IF the circularity breaker is enabled we’re going to say zero. Otherwise, we’re going to sum up all these origination costs and taxes, for each different tranche of debt.

Then for operating deficit, same idea, so IF circularity breaker we’re going to set it to zero, otherwise we’re going to take the operating deficit, right here. This total uses of funds now comes out to $90 million, about $90.3 million here. Let’s go over to our statements. Let’s see if these actually match up now. They should, but let’s just double check our numbers. Here now our funds required, if you go across.

\[11:00\]

The funds required and the total capital drawn will now match each other in each year, until we get to the end of the project here, so that’s how we know we’ve set this up correctly. And again, this entire model is inherently circular. The concept of only enabling circularity or having a circularity breaker, in real life the model has to be circular, because this is just how real estate development works.

You have to fund it based on your projected operating deficit and your projected capital needs for the project, so it’s inherently circular. So you can’t really make it noncircular, as you could with an LBO model just by taking the beginning balance of debt, and using that for the interest. So, it’s a bit of an artificial construction.

It’s really here just in case we run into errors in our model, and we need to reset everything and then change it back, to get rid of those #REF! errors, or divide by zero errors. But again in real life it’s not like an LBO model, where you could conceivably make it noncircular by changing around a few things. We have all that in place now. The last thing I want to do here is look at the optional debt repayments, and the cash flow available to repay debt. So for the cash flow available to repay debt, this one’s pretty simple.

\[12:00\]

Since our capital drawn here has to equal our funds required in each year, because of the way we’ve set it up, we are not going to be able to get any additional cash flow, from here. Really the only source of cash flow to repay debt here, is going to be from if we do not have an operating deficit, if this is actually a positive number.

So we’re going to go up, and I’m going to undo the frame here. We are going to go up a bit, to our cash flow statement. I’m going to say IF the net income here is; or really if the cash flow from operations is positive; if it’s above zero we’re going to take this number, otherwise we’re going to say zero for this.

So that’s really the only source of cash flow, we have available here. Let’s go across, and see what these numbers look like. So here we see going across, finally it turns positive. But remember this is not really accurate, because we still haven’t linked together our interest expense to the income statement yet. So this will change, right now these are positive, but this is going to change.

\[13:00\]

I’m just going to leave them in here for now, because I want to show you how to also calculate the optional debt repayments down here, but this will change over time as we go in, and properly link together our statements. Now for the optional debt repayment, once again I’m going to set up a frame here, so you can see this a little bit better.  
So optional debt repayment, similar principle to the equity and debt draws, and similar to what you’ve seen in standard LBO models before. So, what I’m going to say here is first we have a MIN function, I’m going to take the E91 for senior notes A, because remember the repayment order is the opposite of the draw order.

So we have E91, our beginning senior notes A balance plus the draw, so that’s going to increase how much in senior notes A we have, so that’s one possibility. So if it’s possible we might be able to repay our entire senior notes A balance, if we have enough cash flow available.

\[14:00\]

But then the other possibility is that our cash flow available to repay debt minus whatever we have repaid so far; for this one I’m just going to anchor the 116 part of the first F116; so then the other possibility is that our senior notes A exceed this number, so our cash flow minus whatever we’ve repaid so far is less than senior notes A. In which case, all we can do is repay what we have left with our cash flow.

The first case here handles the scenario where, say we have $10 million of cash flow available, but then only $1.0 million of senior notes A plus a $1.0 million draw; $2.0 million; which means that we can easily repay that $2.0 million with our cash flow available minus our debt repayments. So that’s the first scenario, we have enough to repay the entire balance. The second scenario is we do not have enough to repay the entire balance, but we do have something, so we can repay part of our senior notes A, right here.

\[15:00\]

Now sometimes with real estate development, prepayment is not allowed on this type of debt, it really depends. Usually, for senior secured debt you can repay it early. For mezzanine debt it varies, and sometimes you cannot. I’m really just including this here, so you can learn from this example, and learn how it works.

But keep in mind, in real life the terms of the debt may vary, and you may not always be able to actually repay this type of debt, early. Do we need a MAX function around this, to check if we possibly have a negative number, here? The answer is no, not really because here senior notes A this is never going to be negative, because it’s the ending debt balance, you can’t have a negative debt balance.

And then the draw here is never going to be negative either, it’s only going to be positive or zero, so this part can never be negative. And then the second part here, this can’t really be negative, either, because the cash flow available we’ve done a check here, and we’re only listing zero or positive numbers. And then the repayments so far, it’s not possible for those to exceed cash flow available for debt repayment, so we do not need a MAX function, around this one either.

\[16:00\]

Which is in contrast to what you sometimes see in LBO models, again just a difference in style and a difference in how we’re actually projecting this compared to standard companies. But in short we do not need a MAX function; we don’t need to check whether or not either of these could be negative. So, we’ll copy this one down, and sum up everything there. Let’s just check these numbers.

Okay, so senior notes A, let’s look at that first, so senior notes A, right there. What I should have done is probably set this up, a little bit differently, not a huge deal. Basically what I need to do is here; so E92 should really be E90 plus E110, because we’re going in the opposite direction for these.

The F114 minus the repayments so far is fine. Then this next one, so the E93, this should really be E89 plus the F109. So we have all those in place. Just a quick check there it’s a common mistake to mess this up, because the order of repayment is different from the order of the draws.

\[17:00\]

Now let’s copy this one across, as well. So here we see that we are repaying senior notes A here, because we have so much cash flow available to repay debt. Of course again this will change, because our interest expense is going to be massive. We have not yet taken that into account, but this is basically how it works, you can see it right here.

In this case the senior notes A balance is far bigger than our cash flow available, so we are using only the cash flow available, to repay senior notes. If we had, say a very small balance here, much smaller than our cash flow available, then we’d just repay that entire balance, in one month here. So, let’s also go up, and check that our debt balances here are changing correctly. Let’s also look at our interest formulas, so senior notes B, mezzanine. One thing we need to fix here is that in the beginning I set this up slightly differently, so we need to change around some of the formulas. For mezzanine that is correct, except for the optional debt repayments. That should actually be F119, instead.

\[18:00\]

And then for senior notes B that first part is okay, so that’s fine. But then senior notes A we’ve flipped the order around, so I’m just changing that right now to F117. Okay so now, let’s look at this, and see if this is correct.

So let’s go to when we start having these optional debt repayments for senior notes A, here we’re drawing on $133,000 of senior notes A. But then we’re also repaying a certain amount, which is unusual. But if you think about it, it is actually a plausible scenario, because what’s happening here is that we’re using these funds to pay for our cash flow from investing.

But then operating-wise, our operating cash flow is actually positive, so we’re using our operating cash flow to repay this, but then we’re using the funds here, to pay for our investing cash flow. So here it is going up slightly, because we are still drawing on more than we are repaying. The next year it is going down slightly, because here we’re repaying more than we’re drawing on.

\[19:00\]

So that’s how we know that this is working correctly, now. And again the reason this happened is just because here in this lesson, specifically, I changed around the order, originally I had it mezzanine, to senior notes B, to senior notes A, in the first few lessons here. But I changed it around, because I wanted to reflect the correct optional repayment order, instead.

So that’s how you go through and estimate the optional repayments on debt in a model like this. Again, it’s not terribly common to see this. It’s sort of an optional feature, because to be honest, most of the time in real estate development, you’re not in a position to even do this.

So it really is sort of an optional feature. I just wanted to add it in, to show you how it would contrast with what you see in a standard LBO model, for most companies out there.

Conceptually not terribly difficult, some of the formulas do look a little bit intimidating, but if you think through what each part actually means, it’s actually not that complicated. The key thing to be careful of is that you’re referring to the right cells, here. Remember that we made a mistake in the beginning, because I had changed around the order, so I was actually referring to the wrong cells at first, so be very careful of that.

\[20:00\]

But other than that, it’s really not that complicated, you just have to make sure that your entire model is flowing correctly, and is linked to the correct things. So now that we have this in place, what we’re going to do next is now link together the financial statements.

Make sure that our interest expense, from our debt and equity schedule is properly linked, on our income statement. Make sure that our cash flow from financing here is also properly linked. Then at the end of course we should make sure that our net change in cash is zero. That is what is going to tell us that our model is actually working in the end.

[For more tutorials on Real Estate Modeling click here.](https://breakingintowallstreet.com/real-estate-modeling/)

[See BIWS Real Estate Modeling Course](https://breakingintowallstreet.com/real-estate-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Real Estate Development Key Terms - Quick Reference Guide](https://samples-breakingintowallstreet-com.s3.amazonaws.com/80-BIWS-RE-Development-Key-Terms.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Real Estate Development - Quick Reference Guide](https://samples-breakingintowallstreet-com.s3.amazonaws.com/80-BIWS-RE-Development.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Debt Schedules, Part 3 - After](https://samples-breakingintowallstreet-com.s3.amazonaws.com/81-10-Debt-Schedules-Part-3-Draws-Repayments-After.xls)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Debt Schedules, Part 3 - Before](https://samples-breakingintowallstreet-com.s3.amazonaws.com/81-10-Debt-Schedules-Part-3-Draws-Repayments-Before.xls)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Real Estate Modeling](https://breakingintowallstreet.com/real-estate-modeling/)

Master financial modeling for real estate developments and acquisitions with 6 short case studies and 5 in-depth ones based on real properties from around the world.

[Learn More](https://breakingintowallstreet.com/real-estate-modeling/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[Real Estate Modeling + Excel & VBA + Core Financial Modeling](https://members.breakingintowallstreet.com/offers/F33HSJpg/)
: Learn the fundamentals of Excel, accounting, 3-statement modeling, valuation, and M&A and LBO modeling from the ground up, along with real estate developments and acquisitions. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://members.breakingintowallstreet.com/offers/F33HSJpg/)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F&mini=true)
[Email](mailto:?subject=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)

#### Master Real Estate Modeling

Master financial modeling for real estate development and private equity with 11 global case studies based on property acquisitions, developments, and renovations.

[LEARN MORE](https://breakingintowallstreet.com/real-estate-modeling/)

[](https://x.com/intent/tweet?text=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[](https://www.linkedin.com/shareArticle?title=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F&mini=true)
[](mailto:?subject=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-development-modeling/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F&title=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment)
[](https://api.whatsapp.com/send?text=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F&text=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-development-modeling/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-development-modeling/)
[Copy](https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-development-modeling/#)
[Email](mailto:?subject=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F&title=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-development-modeling/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-development-modeling/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F&t=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F&text=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F&title=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-development-modeling/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-development-modeling/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/04223116/Real-estate-development.jpg&description=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment)
[Print](https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-development-modeling/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F&title=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment)
[SMS](sms:?&body=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F&text=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[X](https://x.com/intent/tweet?text=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-development-modeling%2F&title=Real%20Estate%20Development%20Modeling%20Tutorial%3A%20Equity%2C%20Debt%20Draws%2C%20and%20Optional%20Repayment&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/04223116/Real-estate-development.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand