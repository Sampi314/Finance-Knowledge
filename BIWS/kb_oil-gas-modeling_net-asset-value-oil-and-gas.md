# Net Asset Value Oil and Gas: How to Calculate NAV per Share

**Source:** https://breakingintowallstreet.com/kb/oil-gas-modeling/net-asset-value-oil-and-gas

---

Net Asset Value Oil and Gas: How to Calculate NAV per Share
===========================================================

This tutorial will show you how to finish off the model by calculating NAV per Share for Ultra Petroleum under a wide range of different scenarios – and you’ll see how to set up sensitivity tables for the most important variables, and draw some early conclusions based on those numbers.

 Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/oil-gas-modeling/net-asset-value-oil-and-gas/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/oil-gas-modeling/net-asset-value-oil-and-gas/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/oil-gas-modeling/net-asset-value-oil-and-gas/#tab-signup)
    

**Table of Contents:**

*   **0:47:** Lesson Overview and Why NAV per Share is Important
*   **2:52:** Finding the Share Count, Options, and RSUs
*   **6:42:** Calculating the Diluted Share Count
*   **8:19:** Calculating NAV per Share and Premium / (Discount) to Current Price
*   **14:01:** Picking the Proper Assumptions to Sensitize
*   **17:47:** Picking Ranges for the Assumptions and Running the Tables
*   **20:56:** Overall Conclusions from the Sensitivity Tables
*   **29:44:** Recap & Summary

Net Asset Value Oil and Gas: How to Calculate NAV per Share
-----------------------------------------------------------

Calculating NAV and Making an Investment Recommendation: Calculating Net Asset Value (NAV) per Share

Hello, and welcome to our tenth lesson in this final module of this case study on Ultra Petroleum. This time around, we’re going to be getting to, really, the point of this case study, and our investment recommendation, and everything else we’ve been through, which is getting to the Net Asset Value per share of this company implied by our analysis.

So in the previous lessons, we had done a lot of preliminary work. We had created these roll-up tabs, these tabs that summarized the discounted cash flow from different parts of the company’s business, and so on and so forth. And, of course, we looked at all the different regions of the company. Proved Developed Reserves, Pennsylvania, Wyoming, and then the newly acquired wells and reserves in Utah. We looked at all of those. And we mostly finished our table here with the Net Asset Value by reserve type and region. And what we need to do now is actually finish this calculation and look at it on a per share basis, rather than just leaving it as a lump sum Net Asset Value.

\[01:00\]

And the reason why we need to do that is because if we do not factor in the amount of shares the company has, we might be giving them too much credit. Because, for example, if they acquire a region or a company, as they did with the Utah acreage here, and they pay for it with stock, well, that’s not going to show up as cash or debt that we subtract from Net Asset Value, but it is going to increase their share count. So we do have to factor that in. If we don’t, it’s as if they’re getting something for nothing, which we want to avoid.

And also, just in general, as a company increases its share count over time, as it issues more stock to fund its operations, well, we need to reflect that somewhere. There has to be a real cost to doing it. And if we don’t look at Net Asset Value on a per share basis, we’re not truly reflecting that cost. So that’s the motivation for doing this.

And, of course, the other reason that we’re doing all this is to create these sensitivity tables over here, which will all be based on Net Asset Value per share. We’re going to be looking at these and then comparing it to the company’s own stock price. And that’s the other major reason why we need to do this. That we’re comparing the implied Net Asset Value per share to the company’s current share price, and we’re going to see, okay, is the Net Asset Value per share greater than or less than the share price? Is it about equal to the share price? How does it differ depending on what scenario we’re in? And so on and so forth.

\[02:00\]

So what we’re going to do here is first we’re going to pull all the information on shares and options from the 10-K and the 10-Q of the company and use those to calculate the diluted shares. Then we’re going to look at Net Asset Value per share, and look at a few different sensitivities up here at different gas prices over the long term. And then we will determine the best variables to analyze in our sensitivity tables over here on the right. So it’s really a three-step process.

And I have a lot of written notes here on how to decide which variables you should look at in sensitivity tables. We’re not going to go through all of those. You can read it yourself after this, or before this, or whatever. But I have them there for your reference, because you may come into a case where you’re doing this type of analysis, you may not know exactly which variables to pick. So I wanted to include this here as sort of a guide for which types of assumptions and variables you should put into these tables at the end.

\[03:00\]

So let’s get started with step one here, which is really getting the share count. And then we’re going to look at the diluted securities as well, and then ultimately calculate our diluted shares at the bottom. Which in this case, as we’ll see, does not really make much of a difference, but we like to be complete and correct as much as possible.

So in terms of the share count, you generally want to get this from the most recent filing. So if that’s the 10-K or the annual report because the fiscal year just ended, great. If it’s an interim report or a 10-Q, because a quarter or a half year period just ended, great. Just take it from there.

So in this case, I’ve already filled in the data. If you want to see where this is coming from, go to the company’s 10-Q, which is linked to below this video, and you’ll see the number of common shares without par value. 152,977,633. So that’s where this number’s coming from. Just taken straight from the 10-Q.

And in this case, they don’t actually have restricted stock units or other types of diluted securities here, so they don’t have any type of restricted stock or anything else that is the same as common shares, but just restricted in when you can buy and sell it. So they don’t have anything like that. So it’s going to be zero.

\[04:00\]

And then for these others. So the options and warrants and other securities like that. Oftentimes, they will have something about this in the 10-Q, but not enough to be really useful. So, for example, if I search for exercise price here, well, we get here, they give us an idea of how many total options outstanding they have. So we could go and try to use that information.

But the problem is that as we keep searching for this, they only give us a very high-level overview. Take a look at this. They give us the ending balance as of September 30th, but look at this range they give us. They give us a range of $16.97 to $98.87. Which is completely useless, because as you probably already guessed, our implied share prices are going to be all much lower than the $98.87. They may be higher or lower than the $16.97. But we need to get a much more precise range and much more precise numbers than what they’ve disclosed in the 10-Q.

So based on that, the next best place to look is in the company’s annual report, or 10-K filing for US-based companies. Because this is where they’ll give you a full breakdown of all the information.

\[05:00\]

Now, you could go and search through this and look up exercise price, as I just did. But I’ve actually already separated it all into a different extract. So a different PDF. And the title of it is just ‘79 10 UPL Options RSUs’. If you go to “Share Based Compensation” here, this is where they have a lot of the information on these items.

So let’s go down and take a look at this. And they give us the overall option count over here. They give us the same range. And then what we’re really looking for is right over here. They give us the range of exercise prices, the number of outstanding options, and then, most importantly, they actually give us the weighted average exercise price, which is exactly the information that we’re after here.

And as you can see, only the first tranche here actually has any type of aggregate intrinsic value, because all the rest are out of the money. They’re way above the company’s share price. They’re going to be way above our implied share prices in this analysis. So really, it’s only the first one here that actually makes a difference.

And you can keep reading. They have some other information down here. But this is really all that’s relevant. They have this long-term incentive plan as well, but really, the options and everything from there are already counted in these counts above, so we don’t need to do much of anything there.

\[06:00\]

And just to confirm this for yourself, if you take a look at the 10-K, let’s go down and go to “Financial Statements and Supplementary Data.” I want to draw your attention to something. Just a quick way to check our work in this analysis. Take a look at this. The weighted average common shares, basic and diluted. These are exactly the same numbers, so clearly there’s almost no dilution, or very low dilution, in this case. Which confirms that we’re doing this the right way, and confirms that later on, when we get our result from this output, from this analysis, if we get numbers that are way off, we’ve done something wrong. If, on the other hand, our numbers are almost the same, then we probably match up to what the company actually has in its filings when they did the calculations themselves.

We’re actually done with steps one and two now. And for step three, for making this calculation. So I have the formula that we’re going to use right here. Now, if you’re already in this course, I’m assuming you know what the treasury stock method is, so I’m not going to explain that. If you don’t know this, go back and look at our fundamentals course where we go into that, and look at how to calculate that and what the concept is behind it.

\[07:00\]

The idea here is that if we have circular references enabled, then we want to use the NAV per share right here in cell H100. We want to be using this in our calculations. If, on the other hand, we have circular calculations disabled, then we want to use the company’s current share price of $18.83 instead.

So that is the idea. And based on that, we are using one of those to make all these calculations for the diluted share count from the treasury stock method here. So that is the only thing that may be a little bit different from what you’ve seen before. I’m going to copy this formula, and… let’s go in here.

And for now, I actually have circular references disabled. So this is set to “no.” And you could go in and enable this if you want. It’s really not going to make a huge difference. If I set this to “yes,” let’s see what happens. So it’s not going to make a huge difference for now. And also, we can’t really finish this analysis or see what the difference is until we actually fill in these values, anyway.

\[08:00\]

So let’s keep going down, and just copy this formula all the way down. We can see there’s no dilution from any of these, which is exactly the result we would expect. And then to calculate the dilution from options and other, let’s just link to this number right here, and then sum up everything at the bottom. So we have that. So we have our diluted share count. And we’re actually done with step number three now.

Now, step number four, calculating Net Asset Value per share, the current share price premium or discount to Net Asset Value per share, and the sensitivities at different long-term gas prices. So this is the next major step. To do this, we’re going to link to our diluted shares outstanding from below. So we have that. And I actually linked that incorrectly. Let me try that again. It’s still wrong. Okay. So we have 153 right there. And for the Net Asset Value per share, we can just take our Net Asset Value, divide by the share count.

\[09:00\]

We could put and error checking formula around this as well, but it’s almost pointless, because if we get an error this analysis is all meaningless. So if we get an error, really it means that we need to go back and fix something. So I’m not even going to bother with doing any error checking here.

Now, for the current share price, we’re going to go and take the company’s current share price from right here. And then, to calculate the current share price premium or discounted Net Asset Value, let’s take this number and then divide by this one and subtract one. And I’ll put a plus sign in front, just to clarify that. So here, we can see that the Net Asset Value per share is slightly higher than the current share price, but not so much higher, at least for these base case assumptions, to make us say, “Okay, well, clearly this company’s undervalued by a huge amount.” Looks like maybe it’s undervalued by a few percentage points, if we assume that gas prices in the long-term are going to go back up to around $4.50 per thousand cubic feet. So keep in mind that everything in this base case scenario is dependent on that assumption.

Now, the other thing that we want to do is, in addition to the sensitivity tables that are more comprehensive below, we also like to look at a sort of mini sensitivity table over here.

\[10:00\]

And the reason we like to do that is because sometimes managing directors, partners at firms, other people at your firm, even if they’re lower level than that, they don’t want to see the full output. They don’t want to go through your entire model. They just want a quick summary. They want to be able to say, “Okay, how much value does each type of reserve, does each region contribute at different long-term gas prices?” And we’re really just creating a quick summary like that over here.

So for the range, I’m going to say $3.50, $4.50, and $5.50. So $3.50 is if it drops a little bit from between $3.70 and $4.00 right now. $4.50 is if it goes up to what we think it’s going to go up to. $5.50 is if it goes even beyond that, and goes closer to the more recent highs in gas prices over the past five to 10 years or so.

So to set up this table, what we can do is actually just highlight everything. And I’m going to show you a trick that you may not have known about before. You can just highlight this whole area, even though it doesn’t look like it’s actually a real sensitivity table.

\[11:00\]

And what you can do is just go to ‘Alt + D + T’ in Excel. And for the row input cell, you can actually just go up to the LT gas price right here. And you can input that. And you can press ‘F9’ to refresh the table.

And so after you press ‘F9’, you can see how everything here updates. And of course, as we’d expect, gas prices are higher. We get a whole lot more value from these different types of reserves, especially from the probable reserves down here, which is pretty interesting. It looks like we get a lot more value overall at higher gas prices here than we do from, say, the proved developed non-producing reserves, the proved developed producing reserves, and so on and so forth.

If you’re wondering why the value here stays the same for proved developed non-producing regardless of the gas price, the reason is that we only produce from here in year two, and we assume fixed gas price there. So our year two output is not impacted at all by these gas prices. And that’s why for this one, it stays the same. So that’s not actually an error. If you dig in and you look at what we’re doing, you’ll see why this is the case. And it’s very small anyway, so we almost don’t even care about this.

\[12:00\]

Now, for the others, as we go down, we can see that in all cases, the NPV of G&A stays the same. Cash taxes, of course, this increases a lot as our gas prices go up, as you’d expect. And then you can see that our net debt and preferred, this always stays the same. The price we pay for the acquisition stays the same, regardless of what gas prices do in the future. And then value of undeveloped acreage similarly stays the same. So it looks like, just doing a quick spot check for this table, that our calculations here are correct.

And then I’m going to actually leave circular calculations off, because it makes such a small difference in this case. If you wanted to leave them on… let’s go in and take a look at this. So if I set this to “yes” instead, let’s see what would actually change here. And, of course, we can see that it barely even registered a change. The diluted share count is almost the same. And so it’s a much longer calculation for Excel to make without much of a benefit, which is really the main reason why I’m actually leaving it off here completely.

Now, you might also be wondering, “So what does this tell us about the company’s valuation?” Well, looking at this, I would probably say that it’s telling us the company is about fairly valued right now. Or maybe not fairly valued exactly, but appropriately valued right now.

\[13:00\]

Because looks like in the base case, where we assume gas prices do increase back to about $4.50 or so, as a lot of people expect, they’re undervalued by maybe 2%, 3%, but it’s not a case where a hedge fund or an asset management firm could invest in this and then get a 20% or 30% gain in a year. It doesn’t look like it’s really that type of scenario. And it looks like there’s actually quite a lot of risk if gas prices fall even a little bit below their current levels. If they fall below that in the long-term, it’s around a 65% to 70% difference versus the current share price.

And then in the upside case, where they go up a lot, it’s only about a 31%, 30%, 32% upside there. So what this is telling us is that in all likelihood, this company is probably overvalued slightly right now, or maybe valued about right. Which means that overall, we’re probably going to lean towards against investing it, or maybe making a short recommendation. Although we’ll get to the exact logic and what we think through when we get to that part of the case study, coming up after this.

\[14:00\]

So we have that done. We’re done with step four. Now, the next part here, step number five. We have to think about what variables to analyze in our sensitivity tables. And in a sense, I’ve already answered this question, because I already have the variables right here. But I want to explain a little bit more about why we’re picking these variables first, before we get into the calculations.

So when you decide to do this, I think you need to look at three things. First off, what variables are easy to sensitize in a single cell, which assumptions make the biggest impact overall on the model, and then which values could actually impact our investment thesis or recommendation.

So if you go up to the top, let’s take a look at a couple of the things here. And by the way, normally with oil and gas you always want to have gas prices or oil prices, depending on whether it’s a gas-dominant or oil- dominant company. You always want to have those in one row or column of the table.

Now, for the other variables. So clearly expenses are always going to make an impact. They’re going to be pretty easy to sensitize, because they’re all basically in one cell here. So these are pretty easy to sensitize.

\[15:00\]

The estimated ultimate recovery per well is also going to make a really big difference. We saw that when we looked at some of our production decline curves earlier. The IP rate, also going to make a pretty big difference. The D&C costs will also make a difference, because CapEx is a huge component of this company’s value, and when we subtract CapEx, we get numbers that are completely different from what we had before we subtracted CapEx.

Now, the percent gas, NGLs, and oil. This is both impossible for the company to control, and also it’s not really going to make that much of a difference within a specific range. Yes, if we have more oil overall, it would probably help us. But it’s just not something we can actually control, and it’s not something that’s really going to affect our investment thesis because of that lack of control by the company.

Now, similarly, variables like working interest and royalty rate, it doesn’t really make sense to sensitize these, because, again, lack of control. The contracts have already been locked in. The company can’t really do much of anything about them. And even if you do change these around, something like the working interest is not going to make a huge difference, because you just scale down the ownership proportionally.

\[16:00\]

Royalty rate would make more of a difference, because now you’re losing revenue and production each time. But even with that, we don’t have them in the two major regions, so it’s going to make a much smaller difference overall.

And then going down, you can see how we’ve set this up with our toggles for sensitivities. And I did this on purpose, because I wanted us to be able to, when we got to the end, actually change these around. Which is exactly what we’re going to go into right now.

The other thing to keep in mind here is that in terms of these variables, the estimated ultimate recovery. This one, as I say here, there’s a lot of uncertainty around this, because we saw going through this entire case study that there’s a lot of different numbers thrown out by the company. They have different numbers depending on how you calculate it, depending on which source you’re using.

When we backed into the numbers ourselves in the data tab, remember what happened here. We got results that really didn’t make sense, because we got to a place where the implied proved undeveloped, probable, and possible reserves actually exceeded the 3P net reserves, which makes no sense, at least for Wyoming and Pennsylvania.

\[17:00\]

So we got some results here that were very curious. And so there’s a lot of doubt around the estimated ultimate recovery numbers and what the company’s claiming versus the specific average. So this one’s going to impact our investment thesis a lot.

And then, similarly, the costs on the cost side. That’s also going to make a pretty big impact, because this company’s whole claim to fame is that they’re the low-cost producer. And the question we have to ask as investors is, “Does that actually matter?” Let’s say they reduce the cost by 20% or 15%. Would that actually result in a higher or lower share price? Well, a higher share price, obviously. But would that actually increase the share price by 15% or 20%, or would it simply not make that much of a difference in this model and this analysis? So those are the types of questions you want to ask yourself when you decide on the variables to sensitize here.

So that’s just a brief explanation of what we’re going to go through. And I’m actually going to mark this one off as completed right now.

And then for step number six here. So, moving on. So we have to decide on a reasonable range, and then actually run the sensitivity tables in step number seven.

\[18:00\]

Now, for the reasonable range, I think it’s generally good to have a 20% to 30% differential around your base case assumptions. So you can see here that for all of these, we pretty much are going up by around 20% to 30% in either direction. So we’re going up by around 20% to 30% above, and then 20% to 30% below.

So obviously for expenses, the lower the better. We would expect higher share prices on this side, lower share prices on this side. And then for the others, so for the D&C costs, same idea there. And then IP rate and the estimated ultimate recovery. With these, if we have negative values, that’s a negative, because we get less from the well. We get less in production from the well over time. So we’d expect lower share prices in this region, and then higher share prices as we move over here.

So these are the ranges that we’ve assumed. What I’m going to do now is just go in and set up this table. So let’s link to our share price calculation over here. And we’re going to link to it in the base case. So each 100. And what I can actually do now is just copy this down for all of these tables, as well. So we have that.

\[19:00\]

And then what I’m going to do is just go through and set up all these tables, and then hit the refresh button to refresh all of them and to get these updated.

Now, keep in mind here that when you go through this… ‘Alt + D + T’ for the data table. We always have the long-term gas prices on the left, so that’s always going to be our column input cell. So for the row input cell, we’re going to go up to our toggles up here and enter that. And then for the column input cell, we’re going to go up and go to our long-term gas price, as always. So we have that.

This table is not going to refresh right now, because in Excel, I’ve set it up so that we have to press ‘F9’ or ‘CTRL + S’ to actually save and refresh everything.

Now, for this next one over here. Let me zoom out a little bit so you can see this better. So this next one here, we’re going to take the IP rate differential, and let’s get that from our toggles once again.

And then for the column input cell, same idea. K14. So we have that. And then let’s go down here. The D&C costs. Once again, same idea. We have our toggle up from above, and we can just set this up, as always.

\[20:00\]

So D&C costs. And then column input cell, K14, because we always want the gas prices displayed there. And I don’t know how this underline got there, but we’ll delete that.

And then for the LOE per thousand cubic feet equivalent. Actually, in this case, it might almost be more interesting and better to look at something like production taxes or the other operation expenses, because those are actually bigger on a per thousand foot equivalent basis. But we already have this set up as is, so let’s just take a look at it and see what happens here.

So row input cell. For this one, remember, we don’t need a toggle, because we have quasi universal assumptions. The LOE is different in Utah, but for the other two main regions it’s the same. So we’re just going to link to this and ignore differences or possible differences in Utah. And then column input cell, K14. We have that.

So now let’s hit the ‘F9’ button or ‘CTRL + S’ to refresh this, and see what happens.

\[21:00\]

Okay, so moment of truth. Let’s go through this and take a look at these values, and see if we can draw some initial conclusions. I should also go over and, in the interest of completeness, check off step number six and number seven. Because we’re really on step number eight now, which is reviewing our overall impressions from this output.

So let’s take a look at these tables. If we look at the estimated ultimate recovery differentials versus the long-term gas prices. So let’s first take a look at this portion of the table. So the overall conclusion here is that if you look at this, when the estimated ultimate recovery in all these regions drops by around 5%, it corresponds to almost $2 in per share value. Which is huge. Think about it. This company has a share price of around $18 to $20 right now, and if the estimated ultimate recovery is off by even 5%, the share price… the implied share price drops from anywhere from $1.50 to $2.00. So it’s highly sensitive to this assumption.

\[22:00\]

And what’s interesting is that even in the upside case over here, take a look at these numbers. 5% to 25% differentials. Well, if we go and take a look at these, we see that really, the only way that we can get up to above around $30 per share. So a pretty substantial increase. Around a 50% increase over current values. Is if we assume that not only long-term gas prices, not only will they be higher than what we’ve assumed, but also that our estimated ultimate recovery, our differential, is about 10% to 25% higher than what we’ve assumed.

Now, is that likely to happen? Based on our analysis so far, we think no. We think it’s actually overstated right now based on some of the figures the company’s given. So we think perhaps something more in this region is the most likely outcome. Which, really, to us as investors looking at it, this indicates that, if anything, the company is about valued appropriately right now, and is possibly even overvalued.

Because if you look at this, if gas prices fall, there’s a lot of risk. If our estimated ultimate recovery is off by more than 10%, more than 5%, 10%, 15%, there’s also quite a lot of risk here.

\[23:00\]

And, of course, if gas prices collapse, there’s also a ton of risk. But that’s pretty much true of most oil and gas companies, so that’s not necessarily a valid way to think about our investment thesis on this company.

Now, moving down. The IP rate differentials. Also interesting to look at this. There’s less uncertainty around this. So let’s just focus on a more narrow range here. So around 5% to negative 5% off of our differentials. And again, the thing that really stands out here is that if gas prices go above what they’re at right now, or what we’re assuming for the long-term. Up to more the $4.75 to $5.50 range. There is some potential upside here, but they’d have to go up by quite a bit to actually see something like a $10 per share gain in the company’s stock price. Whereas if they fall by a bit, well, we’re looking at around $3 per share less, $3 per share less, or $4 per share less. Something like that.

So we don’t have quite as much of a strong impression from this particular table. But again, what it’s really telling us is that it seems like, with this company, there is probably more to be lost than to be gained.

\[24:00\]

Because forget about gas prices even going back above the $4.50 level. $4.50 is above where they’re at right now as of the time we’re doing this case study. So let’s say that they stay at their current levels of around $4.00 to $3.70. Well, take a look at this. The implied share price in this region is actually substantially lower than what it’s at right now.

So just taking a look at that and thinking about it that way, you can see that overall, our impression is that this company is probably a little bit overvalued looking at the output from these tables.

And then D&C costs. So this is interesting. And what I want to draw your attention to is let’s say that we stick with our $4.50 per share assumption here. $4.50 per thousand cubic feet assumption for the gas prices. Well, even if the D&C costs decreased by 25%, the share price doesn’t actually go up by that much. The implied share price doesn’t actually increase by that much. It goes up by… it looks like around $5 per share. So here… and that actually does correspond to about a 25% increase over $19 to $20 currently.

\[25:00\]

But it doesn’t make as much of an impact as the other variables. It doesn’t make as much of an impact as you might expect.

So perhaps our main takeaway from this is that even if the company is really this low-cost producer, they’re really spending very little compared to other companies, overall these factors make less of a difference than what the average ultimate recovery for new wells in many of the other regions actually is, and how that impacts the share price. So that’s one of the takeaways from this.

And even if the D&C costs goes up, on the flip side, that also makes a difference. But it looks like it’s about symmetric to the difference that it makes on this side of the table, as well.

So bottom line is even if gas prices fall here, it’s not really going to be enough to offset a drop in the company’s D&C costs per well. Because look at this. Even if they fall by 15% to 25% in terms of CapEx cost, really, here, well, if gas prices also fall, we’re pretty much going to lose money on this. Because if they fall below $4 in the long-term, and go down to maybe something like $3, they’re all still substantially below what the company’s currently valued at. So that’s one of the takeaways from this table.

\[26:00\]

And then this table on LOE per thousand cubic feet. The differentials there versus the baseline assumptions for Pennsylvania and Wyoming. So this one, really the conclusion is that this is almost irrelevant. Take a look at how little the share price actually changes when we have a negative 20% differential all the way up to over a 30% differential here.

So the main takeaway from this one is that even if they get these costs down, similar conclusion. If gas prices actually go up to the $4.50 level that we project, or even maybe a little bit below that, potentially we’re about where the share price is right now. But if gas prices fall, lower expenses here are not going to save the company.

And that’s almost always the case with oil and gas companies, but here it’s especially the case, because you could run into a lot of scenarios where you run the tables, and it seems like the company is actually valued at a completely inappropriate level, or a level that’s off by a lot more than this one is.

\[27:00\]

But in this case, really what it’s telling us is that it’s about right, right now, and if gas prices fall, there’s a lot of downside risk, and the company’s going to be subject to that risk even if they get their expenses down, even if they get their overall CapEx spending down.

One final thing I want to draw your attention to that’s interesting to look at here is the reserve credits. Now, we had pretty conservative assumptions here. We had 50% for probable, 10% for possible. In a lot of models, you’ll see something more aggressive than that. You’ll see more like 50% for possible, maybe 75% for probable. What would happen if we changed it?

So let’s say we did change it to 75% and 50% instead. And I’m going to rerun all these tables once we have that in place, to show you what happens here. So take a look at this. Even with those reserve credits here, if the estimated ultimate recovery is still even a bit lower than what we think it is, and even if gas prices in the long-term are around $4.25 to $4.50, well, even with that, the company is still about appropriately valued right now.

\[28:00\]

And, of course, if gas prices fall by a substantial amount, and we still have those reserve credits that I just assumed 75% and 50%, sure, the picture looks a little bit better than when we had 50% and 10%. But it still doesn’t make as much of a difference as you might think.

And the main reason for that is that in the long-term, a lot of those probable and possible wells are drilled so far out into the future that they just don’t make as much of a difference as you might expect. And really, I would argue that’s the correct way to run a model like this. You never want to assume probable and possible drilling right away. That’s always going to be something that’s farther out into the future.

And if you go down, you can see that we draw similar conclusions from the rest of this. Yes, in some cases, for example, for the D&C costs, if we assume much more favorable reserve credits, the numbers here do look a lot better. Perhaps there’s something to be gained. But overall, we don’t think those reserve credits of 75% and 50% are really justified. And, of course, if you change them back down to, say, 50% and 50%, or 50% and 10%, the numbers once again start to look a whole lot worse here.

\[29:00\]

So just something interesting to look at in the context of the estimated ultimate recovery. We’re going to set these back to 50% and 10% for now. But that’s pretty much what I wanted to cover here.

So as I say here, overall impression is that the company seems about valued appropriately right now, which means that we’re not really going to have a long… we’re not going to really have a strong long or short recommendation one way or the other. We’re going to very heavily hedge our recommendation. And if anything, it seems like they’re probably overvalued based on these tables. We don’t have this hugely strong conviction either way, but we’re probably leaning more toward the company being overvalued based on this.

So we may recommend shorting them. But even if we do that, we’re going to very heavily hedge our recommendation. Because it seems like it’s not really a strong short candidate based on this. It seems like maybe it’s a scenario where we could get maybe a 10%, 20% gain, something in that range, from shorting this company.

So those are the conclusions to draw based on what we’ve done here.

So just to recap what we did in this lesson. We started out by filling in the share count and the diluted shares, calculating the diluted shares outstanding based on the treasury stock method, allowing for circular references. Then we calculated the Net Asset Value per share and the premium or discount based on the current share price.

\[30:00\]

Then we looked at the proper variables to use in sensitivity tables here based on which ones would have the biggest impact and which ones are easiest to sensitize. We came to some conclusions on that. And overall, it seems like the company is either valued appropriately or somewhat overvalued right now, based on our work in these tables.

So coming up next, we’re going to go through our investment recommendation and thesis. And I’m not going to present the actual thesis right away. Instead, I’m going to draw your attention to how to think about this, and how to use the numbers to come up with an argument for or against the company. And then in the lesson after that, then we’ll go through the actual thesis. But first, I want to spend some time on that, and go through some key points when thinking about catalysts, when thinking about risk factors, when thinking about how to mitigate your risk when longing or shorting a company like this. And we’re going to go through all that, and then use that to inform our own investment recommendation, and go through that as the final lesson in this module.

[For more tutorials on Oil Gas Modeling click here.](https://breakingintowallstreet.com/oil-gas-modeling/)

[Premium Course Signup](https://breakingintowallstreet.com/oil-gas-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) UPL - Annual Report (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/79-10-UPL-2012-10K-2013.02.20.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) UPL - 10-Q from Quarter Prior to Deal Announcement (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/79-10-UPL-2013-Q3-10Q-2013.11.01.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) UPL - Options and RSU Information from 10-K (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/79-10-UPL-Options-RSUs.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) NAV per Share - Before (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/79-10-NAV-per-Share-Before.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) NAV per Share - After (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/79-10-NAV-per-Share-After.xlsx)
    

Premium Courses
---------------

Combined shape 37 Created with Sketch.

Based on the content of this tutorial, our recommended Premium Course Upgrade is...

[Oil & Gas Modeling](https://breakingintowallstreet.com/oil-gas-modeling/)

Master financial modeling and valuation for the Upstream, Midstream, Downstream, and Oilfield Services verticals via U.S., European, and Asian case studies.

[Learn More](https://breakingintowallstreet.com/oil-gas-modeling/)

### Other BIWS Courses Include:

Polygon 1 Created with Sketch.

[BIWS Platinum](https://breakingintowallstreet.com/platinum/)
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)

Share

[X](https://x.com/intent/tweet?text=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F&mini=true)
[Email](mailto:?subject=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)

#### Master Oil & Gas Modeling

Learn financial modeling and valuation for the Upstream, Midstream, and Downstream verticals via U.S. and European case studies.

[LEARN MORE](https://breakingintowallstreet.com/oil-gas-modeling/)

[](https://x.com/intent/tweet?text=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[](https://www.linkedin.com/shareArticle?title=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F&mini=true)
[](mailto:?subject=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/net-asset-value-oil-and-gas/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F&title=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share)
[](https://api.whatsapp.com/send?text=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F&text=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/net-asset-value-oil-and-gas/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/net-asset-value-oil-and-gas/)
[Copy](https://breakingintowallstreet.com/kb/oil-gas-modeling/net-asset-value-oil-and-gas/#)
[Email](mailto:?subject=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F&title=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/net-asset-value-oil-and-gas/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/net-asset-value-oil-and-gas/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F&t=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F&text=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F&title=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/net-asset-value-oil-and-gas/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/net-asset-value-oil-and-gas/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/12223209/88.jpg&description=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share)
[Print](https://breakingintowallstreet.com/kb/oil-gas-modeling/net-asset-value-oil-and-gas/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F&title=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share)
[SMS](sms:?&body=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F&text=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[X](https://x.com/intent/tweet?text=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnet-asset-value-oil-and-gas%2F&title=Net%20Asset%20Value%20Oil%20and%20Gas%3A%20How%20to%20Calculate%20NAV%20per%20Share&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/12223209/88.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand