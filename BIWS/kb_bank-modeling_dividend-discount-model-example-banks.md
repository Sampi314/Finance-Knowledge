# Dividend Discount Model Example for Banks - Shawbrook

**Source:** https://breakingintowallstreet.com/kb/bank-modeling/dividend-discount-model-example-banks

---

Dividend Discount Model Example for Banks – Shawbrook Case Study (32:37)
========================================================================

You will learn how to project Phases 2 and 3 of the dividend discount model for Shawbrook in this lesson, as well as the methodology for items like Risk-Weighted Assets and Goodwill & Other Intangibles; you’ll also understand the most important formula in the model, used to determine the dividends a bank can issue.

  Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/bank-modeling/dividend-discount-model-example-banks/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/bank-modeling/dividend-discount-model-example-banks/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/bank-modeling/dividend-discount-model-example-banks/#tab-signup)
    

Dividend Discount Model Example for Banks - Shawbrook Case Study

**Table of Contents:**

*   **1:28:** Part 1: Forecasting Total Asset Growth and ROTCE
*   **8:23:** Asset Growth and ROTCE in the Other Cases
*   **12:55:** Part 2: Projecting RWA, Goodwill & Other Intangibles, and Other Items
*   **18:53:** Part 3: Net Income and Dividends
*   **28:00:** Part 4: Review the Model in Different Scenarios
*   **30:44:** Recap and Summary

![Bank Modeling](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20128%20128'%3E%3C/svg%3E)

### Master Bank and Financial Institution Valuation and Financial Modeling

*   #### Master financial institution modeling and valuation
    
    Build operating models, perform valuations, and analyze M&A deals with 4 global case studies
    
*   #### Dominate interviews and excel on the job
    
    Create professional deliverables like stock pitches, equity research reports, and IB pitch books
    
*   #### Explore private equity and growth equity scenarios
    
    Study buyouts and minority-stake deals in the financial services sector
    

[Full Details](https://breakingintowallstreet.com/bank-modeling/)
 [Short Outline](https://biws-support.s3.us-east-1.amazonaws.com/Course-Outlines/Bank-Modeling-Course-Outline.pdf)

Transcript: Bank & Financial Institution Modeling – Dividend Discount Model for Banks
-------------------------------------------------------------------------------------

Welcome to the second lesson on the dividend discount model in our valuation module for Shawbrook. In this module, we’re going to pick up from where we left off previously where we had linked in the existing three-statement model to this dividend discount model. Now we’re going to extend it over the next 10 years.

Remember, we are showing projections over 15 years here, but in our three-statement model we only had projections over five years. So we need to extend it over the next 10 years after that so it goes out 15 years total into the future.

We have three phases here. Phase 1 was what we covered in the three-statement projection model where dividends begin to be issued and they grow rapidly. In Phase 2, they’re going to slow down. In Phase 3, they’re going to stabilize at a set payout ratio and not be changing quite that much after that.  
We’re going to divide this lesson into four parts.

\[00:58\]

We’ll start by forecasting total asset growth and return on tangible common equity as the key drivers. In Part 2, we’ll forecast risk-weighted assets, goodwill & other intangibles and other items that contribute to this model. In Part 3, we’ll look at net income and dividends and see how we can forecast those. In Part 4, we’ll look at the model and the output in different scenarios and see how different it is in our different cases. As always, we’ll do a recap and summary after that.

To get started, with total asset growth and return on tangible common equity, these are both methods of simplifying the model. Since we only have projections for five years, we need to get the bank’s net income and dividends beyond that. We don’t really want to go back into our operating model and our loan portfolio projections and then try to extend these out for another 15 years or 10 years or whatever the case is. It would be better if we could just take what we have so far and make simplifying assumptions and extend it into the future and still reflect an upside case, a base case and a downside case, but not go into quite as much detail as we had previously.

\[02:06\]

With asset growth, this is generally going to slow down over time. For a healthy bank, it will still be growing its loans and assets at a faster clip than the overall GDP growth rate. It’s still going to be growing faster than the overall UK GDP growth rate, but it’s going to be lower than its current level, and that’s what we have to look for over time.

Let’s actually take a look at that first and see what we have here. Now we’re in our base case. I have it listed in the Op-Model tab. Total asset growth here is slowing down quite a bit from around 21% or 20% down to around 12% in Year 5 of our projection period. So it’s slowing down by quite a bit.

\[02:58\]

Logically, we want this to go to a lower level, but again, still be higher than the overall UK GDP growth rate which might be around 2% or 3% over the next 10 or 15 years, if you remember from our lessons on the loan portfolio projections and how we came up with those numbers.

So to go up here, let’s actually go in and start filling in some of what we can. In the base case, we know it’s around 12% right now. We want it to fall to a lower number. I’m going to start it at 11% and then go to 10%, 9%, 8.5%, 8%, 7.5% and 7.5%. In the final three years and for the period beyond that, we’re going to set this to 7% and just say that into perpetuity, we’re going to assume that the assets grow at 7% forever.

Obviously, this doesn’t really hold up because it will probably come down to a level lower than that.

\[04:00\]

You’ll eventually get to the point where the bank is growing at just barely more than the GDP growth rate, but that’s what we’re going to set for now because we only have 10 or 15 years in our model. We’re not going out 100 years in this model.

We also need to set up a formula to actually select the case that we want. I’m going to use an INDEX and MATCH function here. We’re going to index this array, and for the row number, we need to use a MATCH function. We’re going to use the scenario that we’re in and then we’re going to look it up in this array right here. Then for the matched up, I’m going to say 0 because we want an exact match. For the column number, we can say 1 because we only have one column in our area.

To test this out, if we change it to 8% in the upside case and 6% in the downside case and then we change around our scenario, we can see that this changes.

\[05:02\]

So it appears that that is working correctly.

Let’s copy this formula over. Let’s also change some of what we have here. We’re going to make this J9 thru J11 and we will anchor this. K9 thru K11 doesn’t need to be anchored because this should shift over as we copy over the formula. For the last three years, we want to link to our final selected number.

For return on tangible common equity, the idea is the same but there is one difference here, which is that we have to think about the cost of equity at the end. We know that cost of equity starts at 12% and then declines gradually to 11% by the end to reflect the fact that the company does become bigger and less risky over time as it gets more diversified and turns into more of a mid-sized bank.

\[06:02\]

In some models, you’ll see that [return on equity](https://breakingintowallstreet.com/kb/financial-statement-analysis/return-on-equity-roe/)
 or return on tangible common equity or whatever you’re using eventually converges on cost of equity under the logic that in the long-term, a company’s returns will come back down to what investors are expecting the company to return.

In this case, though, we’re going to keep the numbers slightly above it. The difference is going to be very slight in the downside case but it will be more substantial in the base and upside cases because, yes, Shawbrook is becoming bigger and more of an established bank over this time period, but it’s still far younger than the truly big banks out there like HSBC and Barclays and so on, so we don’t quite think it’s fair to make return on tangible common equity equal cost of equity exactly by the end of this period just because of the bank we’re dealing with.

If we were doing a model for UBS or Bank of America or JP Morgan or some other bank like that, then you might be better off changing that around and actually making the returns-based metric equal the cost of equity at the end.

\[07:07\]

But we’re not going to follow that approach here.

For this one, the return on tangible common equity in the base case starts out at around 17% or 18%. It’s declined from around 25% or 23% when we first began these projections. So it’s declining, but it is still rather high, certainly higher than what you’d see for the large, established banks.

Let’s continue that trend and make it 16%, 15%, 14.5%, 14%, 13.5%, 13% and 12.5%. For the final year of return on tangible common equity, we’re going to set it to 12%. We can use the same formulas here, INDEX and MATCH. We can copy this across and we can change this one to link to the 12% instead.

\[08:00\]

Technically, we should also copy down this formula, the J9 to J11, although it really doesn’t matter at all because it’s the exact same set of scenarios here. Nevertheless, let’s do that anyway.

I’m going to delete these other numbers for the upside case and downside cases because now we have to go in and look at those and see how these numbers change in the upside and downside cases and how our returns and total asset growth numbers are going to change as a result.

Let’s start with the upside case and go over here and take a look at how this changes. In the upside case, our total asset growth is a fair amount higher.  
It ends up being around 15%. It’s declining from around 30% to 35% down to around 15% by the end. Return on tangible common equity declines from around 24% or 25% to more like 20% or 21%.

\[09:02\]

So we’re still a fair amount above the base case, but when all is said and done, we are still showing declining metrics simply because the bank is getting bigger over time.

For the total asset growth, I’m going to start it at 14% and make it decline to 13%, 12%, 11%, 10%, 9% and 8.5%. So we end up at almost the same level. We’re still a little bit above the base case, but not by that much.

For return on tangible common equity, we’ll start it at 18%, down from the 20% or so number we have now, and then go to 17%, 16.5%, 16%, 15.5%, 15% and 14.5%. For the final year number for both of these, I’m going to say 8% for the asset growth and then 14% for return on tangible common equity.  
So that’s the upside case.

\[09:58\]

Let’s go over and look at the downside case now and see what’s happening here. In this case, our asset growth isn’t really that much different. We do start off at a much lower number because we have a recession projected in the first two years. But then past that, we end up at around 13%, which isn’t really that much different from the other cases. The main difference is that we have a decline in those first two years because of the downturn that we forecasted.

If you look at return on tangible common equity, again, it’s lower, but it’s not dramatically lower. It ends up at around 15% versus 18% in the base case and around 20% in the upside case. So we are a good bit lower here and we want to reflect that in our numbers.

Let’s start with the asset growth first. Remember, this ended up at 13% in our projection so far. I’m going to start it at 12.5%, then 11.5%, 10.5%, 9.5%, 8.5%, 7.5% and 6.5%.

\[11:05\]

The final year number will be 6%. For return on tangible common equity, we’ll start it at 14%. So it’s below the 14.5% or so number we have right now. Then 13.5%, 13%, 12.5%, 12%, 11.5% and 11.5%. Our final year number will be 11%.

In this case, the final year number is exactly equal to the cost of equity, but that’s okay. In the downside case, it’s fine to assume that the bank returns nothing above and beyond what investors are expecting in the long-term, and that’s actually a reasonable assumption. It’s just that in the other cases, we want to be a little bit more optimistic than that.

With those in place, I’m going to change it back to the base case now. The other thing we can do is since we have these, we can link to them within our model and we can also forecast numbers like the total asset growth rate.

\[12:00\]

For this one, for total assets, we can link to our growth rate right up here. For the return on tangible common equity, we can link up here to this one and copy this across. For total assets, we can also just take our old number and multiply by the growth rate down here to get our new number and then copy this across as well.

Technically, it will be a little bit better if we set this up differently and just made this 1+K12, which is the growth rate at the top, and then we kept using the same formula all the way across that we had before, just to keep it consistent. But in any case, now we have our total assets set up and we also have our return on tangible common equity down here.

So that takes us to the end of Step 1 of this process.

\[13:00\]

Let’s move into Step 2 and look at some of these other items, risk-weighted assets, goodwill & other intangibles, and various other items like stock issuances, for example.

With stock issuances, we’re going to set this to zero because the company has no need to keep issuing stock indefinitely as time goes by. Yes, they can issue more dividends if they issue more stock, but they’re also going to get more shares outstanding. All else being equal, if a company has enough capital on hand to issue dividends and keep growing them, it’s not going to want to issue stock because that just dilutes existing shareholders. It also reduces their earnings per share, which is an important metric for public companies.

For these others, for risk-weighted assets as a percent of total assets, this is clearly increasing over time. The interesting thing is that even if you look at this in different cases, so if we change it to the upside case, for example, it doesn’t really change by that much. It still goes up to around 70%, 71%.

\[13:58\]

Even in the downside case, it still ends up at around the same number. This is because of the way we set up the model where we didn’t really vary risk-weighted assets as a percent of interest-earning assets.

For this one, we can just assume that it keeps increasing up to a certain level. I’m going to say that that level is about 80%. So for the first part of this in Phase 2, we’re going to have it increase to 80%, and then in the stabilizing phase, Phase 3 – Stabilization, we’re going to keep it at 80% going all the way across.

For goodwill & other intangible assets, this one we can see is declining as a percent of total assets. The amount of goodwill & other intangibles of course is increasing, but as a percent of the total assets, which is one simple way to project it here, it’s clearly declining over time.

For this one, you can look at it in different cases and you’ll see that it doesn’t really differ by that much.

\[15:01\]

There’s a bit more of a difference here, but it still ends up at just over 1% in most of these cases. In the downside case, it is actually a fair amount higher, so we might have to think about that in a bit more detail. You could also use a growth rate to project this if you wanted to do that. But it’s a fairly minor item, so I’m not going to worry about it too much.

Instead, I’m just going to start this out at 1.1%, making it go to 1.07%, 1.05%, 1.03% and then 1%. In the stabilizing phase, we’re just going to keep it the same at 1% going all the way across.

At this stage, we can also project our actual risk-weighted assets, and we probably should do that. Let’s take our total assets and multiply by this percentage. For the growth rate, we can use the same exact concept here and just change the row number slightly.

\[16:02\]

So we have our risk-weighted assets down there. Then our growth rate, we can also copy across. We can see that by the end, it slows down to that 7% rate that we had at the top.

For goodwill & other intangibles, let’s just take our percentage down here and multiply by the total assets. We can copy this across.

In terms of other numbers and percentages, the targeted common equity Tier 1 ratio we’re just going to keep the same and we will copy this across. There’s no real reason to change this because if the company has been targeting 13% historically and we assume that in our projection period, there’s no real reason to think they’re going to change it in the future. So we’re just going to hold this one the same.

\[17:00\]

Other than that, we also want to think about the common shareholders’ equity and common equity Tier 1. We want to project something for these because when get into net income and dividends in the next step, if these are blank for right now, we are going to have a very difficult time projecting those and getting the formulas right. So we want to at least fill in something for these, even though they’re not going to be correct. They’re not going to be the final formulas, or at least not the final numbers here.

So for beginning common stockholders’ equity, we can just link to the ending number. For ending common stockholders’ equity, we can just sum up everything above and then copy this across.

\[17:57\]

For common equity Tier 1, we can just sum up ending common shareholders’ equity and then the goodwill & other intangible deduction. We don’t need to look at tangible common equity here because it’s the same as common equity Tier 1 for this bank. That’s not always true in real life, so you may actually have to calculate tangible common equity for some banks. But here, it’s a fairly simple new bank and so they’re effectively the same number.

So now we at least have something there, even though obviously it’s staying the same each year because we don’t have anything for net income or dividends and we assume no stock issuances.

At this point, we could also take a look at our actual common equity Tier 1 ratio. We can take common equity Tier 1 and divide by the risk-weighted assets and copy this across. This just lets us compare our actual number to our targeted number. Right now, we run into some serious trouble because we don’t have net income and dividends, but of course this will be fixed in the next step.

Let’s actually do that now and move into the next step of this process.

\[19:00\]

Part 3 is all about net income and dividends. We’re going to start with net income and then go into the dividends. You can project net income in a couple of different ways in the dividend discount model. You can use [return on assets](https://breakingintowallstreet.com/kb/financial-statement-analysis/return-on-assets-roa/)
, return on equity or return on tangible common equity. We’re going to keep using return on tangible common equity because that’s what we’ve used so far and focused on in this valuation.

As I said before, since this company is simple, tangible common equity equals common equity Tier 1 and so we can just link this calculation directly to the company’s common equity Tier 1 levels.

There is a problem here because this will end up creating a circular reference, so we have to check for this. The reason it creates a circular reference is because if you think about it, with these returns-based metrics like return on tangible common equity, you’re supposed to average the tangible common equity from one year to the next, multiply by this percentage and that will get you the net income to common in the year you’re in.

\[19:57\]

The problem, though, is that if we do that, when we project net income to common here, it’s going to flow into the common equity Tier 1 in this year and so our net income this year will depend on our ending common equity Tier 1, but then our ending common equity Tier 1 will also depend on our net income and so we get a circular reference.

The way around this is to simply check for this. Remember that on the Op-Model tab, we had that option to enable or disable circular references. We can continue with that here. We can say that IF(Circ\_Ref, so if it’s enabled, then we can take the average between last year’s common equity Tier 1 and then this year’s common equity Tier 1. Otherwise, to avoid the circular reference, we can just use the beginning balance. In the beginning, of course, we can multiply by the return on tangible common equity in this year. Now that we have that, let’s actually copy this formula and then the growth rate formula across.

\[21:00\]

We can link our net income to common in this buildup for ending common shareholders’ equity to what we calculated above. Now since we have circular references enabled, all the numbers are going to change because we’re using averages to calculate this.  
These numbers are way too high right now. They’re going to come down once we factor in dividends because dividends are going to reduce common shareholders’ equity and common equity Tier 1.

So that’s what you do for net income. Then for dividends, you have to start by setting a targeted payout ratio. Remember that we ended the five-year projection period with this ratio of 40%, so the company is working up to that, or has worked up to that, really. Then going forward, we have to assume something.

If you recall from some of the comparable public companies, if you look at a more established one like Secure Trust Bank, for example, they actually had a payout ratio of almost 50%, 49.2% in the last 12 months.

\[22:00\]

Many of the others had not yet started issuing dividends, so they’re not appropriate comparisons. If you look at some of the other companies that we looked at in the regression analysis, remember that for some like Provident Financial, they actually had a 75% payout ratio. So clearly, there’s some room here to increase the payout ratio. The question is by how much?

If you keep looking through the materials, you’ll see that many of these other more established banks like Close Brothers have a payout ratio somewhere between 40% and 50%. So on the basis of all these numbers we’ve examined, we would say that it’s fair to say that the payout ratio goes up to around 50% and then stays there as dividends stabilize. So I’ll say 42.5% and then 45%, 47.5%, 50%, 50%, and then we can just hold this constant going all the way across.

For the formula for dividends, I have it written out over here because it gets a little bit complicated to explain.

\[23:02\]

It looks a little bit complicated at first glance. It’s a MIN formula. What we’re really doing in this is comparing the payout ratio times net income to common, which is what we’d ideally like to pay out. We’re comparing that to what we can actually pay out, which is determined by the amount of regulatory capital we actually need, so the risk-weighted assets times that targeted common equity Tier 1 ratio, and then we have to subtract or add all the components that go into it.

So we subtract goodwill & other intangibles because those get subtracted from common equity Tier 1, stock issuances add to it, net income adds to it, and the beginning common stockholders’ equity in this year will also add to it. So we have to factor in all the individual components and this tells us exactly the maximum that we can actually pay out.

In many years, this won’t be an issue because it will just be the payout ratio times net income to common. But as we keep going, we’ll see that this does become more of a constraint, especially because the company stops issuing stock at a certain point.

\[24:00\]

Let’s go in now and actually just enter this formula. You can see it right here, net income to common times this payout ratio. That is the very first part of this formula. That’s the first point of comparison. Then right after that, we have our second point of comparison. So we take our risk-weighted assets in cell K62 and then we multiply by the common equity Tier 1 ratio that’s being targeted in cell K57. Then we have to factor in goodwill & other intangibles, stock issuances, net income to common, and also our beginning balance. All of those are going to play into it and affect it. Essentially, we’re seeing if everything proceeds as-is with these assumptions, how much is left for us to be able to meet the minimum common equity Tier 1 that we’re targeting?

\[25:00\]

So, moment of truth. Let’s enter that and see what happens. Nothing dramatic so far. We can copy across our growth rate formula and then the actual payout ratio formula.

The last step of this process is to finally link to our common dividends. We’re going to use a negative sign for that, and then we can copy this across. We can see now that after doing that, the constraints come into play. Look at this. We’re targeting in some of these periods a 50% payout ratio, but we’re only getting to around a 40% payout ratio because of the way the company is growing and its capital structure and its regulatory capital on hand.

\[25:57\]

We also see that the targeted and actual common equity Tier 1 levels converge on each other over time. Really, by the end of Phase 2 is when they’re the same number. Then in Phase 3 onward, they’re always the same number.

So this is how you want your dividend discount model to be set up. We can copy across some of these other parts like dividends for the full year. Then toward the bottom, if you want to finish up this process, you can go down here and calculate the present value of dividends.

Remember, for this one, you want the dividends for the remaining period in year. This is only an issue in the first year because of the stub period, but to be technically correct, that’s the one you should be taking.

We already calculated the discount factors or the cumulative discount factor in our last lesson, so for this one, we’re just going to take dividends for remaining period in year and divide by that cumulative discount factor.

\[26:57\]

Then we get to our present value of dividends at the bottom of this page. We can see that the present value of each one goes up for a while. It stays in about the same range, but then it starts falling over time because the payout ratio falls and also the discount factor just becomes a much bigger number over the course of 10 years.

We are now mostly done with this set up. We have all of our dividends projected. We’ve been through the key parts of the model. The point I would really emphasize is that this formula for dividends is the key one here. Out of everything we’ve been through, this is the most important part because this is what makes a dividend discount model for a commercial bank or an insurance firm or anything else that has regulatory capital fundamentally different from a dividend discount model for a utilities company or for a retail company or something like that. With those, you don’t have this limitation. You don’t have to do this check. You might constrain it in some way if you want or if you have to, but you don’t constrain it against the common equity Tier 1 because it doesn’t apply to those types of firms.

\[28:00\]

With that done, let’s move into Part 4 and look at the model and the output in different cases. Let’s just zoom out a bit. Up here, I’m going to list the sum of the present value of our dividends at the bottom. So it’s 290.5 in the base case. If we go over and change this to the upside case, this changes it to about 296.5.

So it goes up, but it’s a fairly small increase. If you look at the reasons why, the issue again is that the company is constrained somewhat by its regulatory capital. We want to be able to issue 50% of net income in the form of dividends, but we only get up to around 37%, 38% or 39% by the end.

In the downside case, it is more like 246.3.

\[29:02\]

So there’s quite a bit of a bigger difference there. Here we actually get to this 50% level, but that’s because our net income is much lower to begin with. We don’t really know how much that means. Interestingly, in the downside case, the actual and targeted common equity Tier 1 only really begin to converge toward the very end of this period.

So those are some interesting differences to look at. We get that convergence much earlier on in the upside case. Almost right away, they start to converge and become the same number, whereas the base case takes a little bit longer to get there.

So those are just a few interesting differences to point out as we go through this. You could go and nitpick and change around other various points in the model, but we’d say it’s reasonably good right now in terms of robustness and reflecting these different scenarios.

Really, the main downside that we can see so far is that, as I say right here, the base and upside cases are quite close.

\[30:01\]

There is more of a difference in the downside case if you look at the cumulative present value of dividends. This doesn’t mean that our model is wrong, but it just means that it’s going to be a bit more dependent on the terminal value than we like. We’d ideally like to have quite a big difference in dividends in the projection period so that even if the implied value of the bank is quite different, at least a good chunk of it is coming from the dividends as opposed to the terminal value.

In this case, though, it seems like most of the difference is going to come from that terminal value because the return on tangible common equity across all the cases is so different at the end and that in turn means that the terminal value is also going to be quite a bit different, and so the present value of it will also be different.

Let’s do a recap and summary now since we’re at the end of this lesson. We started here by forecasting total asset growth and return on tangible common equity as key drivers. We looked at how these change across different scenarios and how we still want them to generally end up at around the same spot over time.

\[31:02\]

You don’t have to use those. You could use return on assets or return on equity or something else, but we chose to use those here to keep it consistent with the rest of our valuation.

Then we projected these other items like the risk-weighted assets and goodwill & other intangibles, and mostly just continued trends and then had them end up at about the same place in the stabilized period.

Then we projected net income and dividends based on one of our returns-based metrics, the payout ratio and the company’s regulatory capital. That’s where we got into this formula for full-year dividends and you saw how that worked and how the regulatory capital constrains the amount of dividends a bank can issue.

Finally, in Part 4, we just compared the model in different scenarios and saw how it doesn’t look terrible, but it is a little bit concerning how the base and upside cases are so similar, which means that we may have to put some more time and thought into our terminal value calculation here because it’s going to explain so much of the difference in implied value across the different scenarios.

\[32:09\]

With all that done, in the final lesson of the dividend discount model coming up next, we are going to move into that last step looking at terminal value, calculating the bank’s implied equity value and implied share price, the premium or discount to its current share price, and we’ll also have to tie up some other loose ends such as what to do with the stock issuances and how to set up sensitivity tables and draw some conclusions from the model based on all that.

[Sign Up To BIWS Bank Modeling](https://breakingintowallstreet.com/bank-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Lesson Transcript](https://samples-breakingintowallstreet-com.s3.amazonaws.com/Banks-03-12-DDM-Part-2-Phases-2-3.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Shawbrook - Operating Model and Valuation Case Study (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/Banks-02-SHAW-Valuation-Case-Study.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Shawbrook - Completed Valuation (Excel)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/Banks-03-SHAW-Valuation.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Channel Checks Document (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/Banks-02-SHAW-Channel-Checks.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Dividend Discount Model, Part 2 - Before (Excel)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/Banks-03-12-DDM-Part-2-Phases-2-3-Before.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Dividend Discount Model, Part 2 - After (Excel)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/Banks-03-12-DDM-Part-2-Phases-2-3-After.xlsx)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Bank Modeling](https://breakingintowallstreet.com/bank-modeling/)

Master bank accounting, valuation, M&A, and buyouts with 4 global case studies based on Shawbrook, KeyCorp / First Niagara, ANZ, and the Philippine Bank of Communications.

[Learn More](https://breakingintowallstreet.com/bank-modeling/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[Bank Modeling + Excel & VBA + Core Financial Modeling](https://members.breakingintowallstreet.com/offers/CfRbkrvF)
: Learn the fundamentals of Excel, accounting, 3-statement modeling, valuation, and M&A and LBO modeling from the ground up, along with commercial banks and insurance firms and how everything differs for them. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://members.breakingintowallstreet.com/offers/CfRbkrvF)

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F&mini=true)
[Email](mailto:?subject=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)

#### Master Bank & Insurance Modeling

BIWS Bank & Financial Institution Modeling Course prepares you for FIG interviews and the job itself with tutorials on bank accounting, valuation, M&A, and buyout modeling.

[LEARN MORE](https://breakingintowallstreet.com/bank-modeling/)

[](https://x.com/intent/tweet?text=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[](https://www.linkedin.com/shareArticle?title=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F&mini=true)
[](mailto:?subject=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/dividend-discount-model-example-banks/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F&title=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29)
[](https://api.whatsapp.com/send?text=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F&text=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/dividend-discount-model-example-banks/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/dividend-discount-model-example-banks/)
[Copy](https://breakingintowallstreet.com/kb/bank-modeling/dividend-discount-model-example-banks/#)
[Email](mailto:?subject=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F&title=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/dividend-discount-model-example-banks/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/dividend-discount-model-example-banks/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F&t=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F&text=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F&title=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/dividend-discount-model-example-banks/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/bank-modeling/dividend-discount-model-example-banks/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/04221719/Dividend-Discount.jpg&description=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29)
[Print](https://breakingintowallstreet.com/kb/bank-modeling/dividend-discount-model-example-banks/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F&title=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29)
[SMS](sms:?&body=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F&text=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[X](https://x.com/intent/tweet?text=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Fbank-modeling%2Fdividend-discount-model-example-banks%2F&title=Dividend%20Discount%20Model%20Example%20for%20Banks%20-%20Shawbrook%20Case%20Study%20%2832%3A37%29&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/04221719/Dividend-Discount.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand