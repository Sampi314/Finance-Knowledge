# NAV Model for Oil & Gas: How to Make Revenue Projections

**Source:** https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model

---

NAV Model for Oil & Gas: Revenue Projections
============================================

In this video, you’ll learn to project revenue in a NAV model out beyond the traditional 5-year period used in operating models using assumptions for long-term production decline rates and average realized prices.

 Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model/#tab-signup)
    

NAV Model for Oil &amp; Gas: Revenue Projections
------------------------------------------------

In this lesson, we’re going to dive into the mechanics of our net asset value model for XTO Energy, and you’re going to learn exactly how this spin, this twist on the traditional DCF model that you see for normal companies, differs and how it applies specifically to oil and gas and natural resource companies.

Keep in mind the basic idea here, which we went over in the previous lesson, which is that everything in a net asset value model flows from the company’s existing proved reserves. We are assuming that they’re not spending anything on CapEx in terms of finding new reserves, finding new land, acquiring companies. We are instead assuming the entire value of the company, at least 90% to 95% of it, is based on their existing proved reserves.

Then for the non-exploration and production portions, we simply value the land separately. Then for the other business segments, like chemicals, midstream, and downstream for example, we would value those separately. We do effectively a sum of the parts valuation here and look at the cash flows from their E&P segment, and then assign simple multiples to the other business segments or to the undeveloped acreage that they have to figure out the values there. Then, once again, use the same approach to get to the implied share price and the implied equity value here.

Also keep in mind that this model applies not only to oil and gas companies but also to mining, any type of natural resource company that has proved reserves and production. The only difference, of course, is that for mining companies, maybe you’re looking at ounces, maybe you’re looking at tons or metric tons or kilograms or pounds or whatever other unit you want to use. So you’re not looking at billions of cubic feet equivalent or barrels of oil. You’re just looking at different units, but the concept and the mechanics here are exactly the same for mining companies as well.

So to get started with this, we need to figure out what our proved reserves here are. I’ve already filled this information in for the end of 2009. If you want to look at it yourself, you can go to the handout that I’ve created called “Oil and Gas Supplement XTO” under this video. On the second page here, they give their proved reserves for 2009 for gas, natural gas liquids, and oil, and then natural gas equivalents. So I’ve taken these three numbers directly from here. This is always where you find the information in the 10-K or annual filing for an oil and gas company.

We have them right here. So what I’m going to say for each of these is that the beginning reserves, at the beginning of 2010, this is simply equal to the ending reserves at the end of 2009. So I’m going to go up here and take the number for gas, and then for natural gas liquids, and then for oil as well.

Now we need to figure out what the annual production each year is going to be. Now remember that previously we have gone in and created a production and operating model for XTO Energy. So we can go in and take much of the information from here.

In addition, we also need to figure out what kind of prices they’re getting for their commodities. So we need to figure out the average price per thousand cubic feet. Again, we have this in our production model, so it’s not going to be terribly complicated to pull this in.

\[03:30\]

So let’s go and get started and pull in the annual production information and then the average price per thousand cubic feet, both of which are coming directly from XTO’s production model that we’ve already created.

Let’s start with the average prices for gas here. I’m going to go back to our production model. We want to take the averaged realized sale prices after hedging here. Remember that we have a couple different things going on in our model. We have the base market prices here, the average NYMEX prices. But then there’s a differential on those, because the company’s not going to get the market price all the time. So there’s going to be a differential. Then they’re also using hedging to reduce their downside risk, which also limits the upside potential here.

So long story short, we want the average realized sales prices after hedging, because we want to take into account everything I just mentioned here. Take the gas from right there.

We have to be careful. We cannot just copy this down. What I’m going to do instead is take this, copy the formula, and then replace the J with a K. Then with an L, and then M, and then N. So we have this for these five years. We’re going to press ‘Ctrl + \[‘ to trace this. We see it’s corresponding to 2014 here, just as we wanted. Of course, the reason we couldn’t copy it down is because these prices are horizontally listed, whereas the prices in our NAV model are vertical.\
\
So we have these prices for these five years, and now to get the production numbers, what we want to do here is take the MIN between our beginning reserves and then the annual production. This prevents situations where the annual production goes above the beginning reserves and ensures that, no matter what happens, we can never produce more than we have in the ground.\
\
This is not a particularly likely scenario, but just in case someone comes along and decides to enter 15 trillion cubic feet of natural gas, for example, for the production, having this MIN function in place prevents anything weird from happening in our model here.\
\
So we’re going to take the MIN between the beginning reserves, and then going back to our production model, we’re going to take the natural gas production here for 2010. Take this, copy this one down, and we need to adjust this formula a little bit. We need to say K15 here instead, and then L15, M15, and then N15. Again, just to change the data from being displayed horizontally to vertically here.\
\
Now for how the reserves change, this is very straightforward. It is simply going to be our beginning reserves minus our annual production, and that is actually going to be the same all the way down here in this model to 2030. So we have that.\
\
Now we need to look at the production and the average prices beyond this five-year period. For the prices, the standard thing to do in net asset value models is just to assume the year five price and extend it all the way down. So we’re going to take the year five price, 2014 here, and take this all the way down. Then for the production, the standard way to do this in net asset value models is to take the year five or year ten or whatever your final projection year is, and then to assume a decline rate on that production.\
\
\[07:16\]\
\
Remember that with natural resources, oil, gas, mining, anything like that, the production follows a curve where it starts out low, it reaches a peak, and then eventually it dwindles and goes to zero over time. So we’re assuming in this case that the peak production occurs in 2014. Now, that may not be the case. It may actually be that it occurs earlier or later. We don’t really know, but that’s going to be our assumption.\
\
If we wanted to, we could create a two stage model where it peaks later on and then declines at some point in the future rather than in 2014. So that is a possibility, but here I’m going to keep it simple and use a relatively simple percentage estimate.\
\
So I’m going to say that the long-term decline rates for natural gas, NGLs, and oil are all negative 5%. So they go down by 5% each year after year five in our model. The formula for this, we’re going to take the MIN between our beginning reserves, at the beginning of the year, and then the annual production here times one plus the decline rates.\
\
Remember that these are already negative, so we want to use a plus sign here so that this becomes 95%. You see this going down now. I’m going to also anchor the K8 cell with ‘F4’ so it doesn’t shift around. Now we can copy this one down as well.\
\
So we see here that the production goes to zero in year 12 or 13. If you remember, going back to the public comps, we saw that the reserve life ratios for these companies were in the 10 to 15 year range. XTO specifically was around 14, 14.2, but we are also counting their oil and NGL reserves there. So this doesn’t really tell the whole story. We need to look at this in more detail and go through the calculations for natural gas liquids and oil as well. But at least the valuation here and the reserve life ratios for these other companies are telling us that our net asset value is not wildly off here.\
\
Let’s go back to the NAV model. One other thing I want to do quickly is just color code this properly, so the 2010 to 2014 ones will be in green here for the font color, because these are links from other worksheets. We’re changing that.\
\
One lingering question you may have based on this is: What happens when we change around our resource price scenario here? Remember that the price case we’re using here is the NAV one. We have a couple different choices on our inputs page: Base, Downside, Upside, DCF, and NAV. We’re using NAV here.\
\
Now, you might be wondering, what happens if we change the gas price to say $8 or $9? Will it still be properly reflected here? Because we are directly linking to the production worksheet. The answer is yes. To illustrate it, let’s say I change the price to $8. We see this is updated and is now $7.82 because of that pre-hedging price differential and then the effect of derivatives and hedging on the prices here. So the short answer is that yes, it’s going to be reflected, because in our production model we are directly pulling from this resource price information right here and on our inputs page. This works properly and flows through our model.\
\
\[10:38\]\
\
I’m going to change this back to $7 for now. So that is what the natural gas here looks like in terms of the prices, the production, and how the reserves change and ultimately run out over time.\
\
What I’m going to do now is go through the same process for natural gas liquids and oil. It’s not very interesting to show you, because you know the basic idea now that we’ve been through it for natural gas. So what I’m going to do instead is just skip ahead in this video, fill in the information for natural gas liquids and oil, and then we’ll look at the total revenue calculation here at the end and draw some conclusions based on that, and then set up the next video on calculating expenses in this model.\
\
\[Skip ahead in video\]\
\
Okay. So now I’ve gone in and completed the NAV model here for natural gas liquids and for oil. There’s really not too much different here. It’s really just that the units are slightly different, barrels of oil or thousands of barrels of oil versus billions of cubic feet of natural gas. So the units are different, but we’re still linking to the prices in the model. We’re still using the MIN function to determine whether we should use the annual production or simply the beginning reserves number. Then afterward we’re also still assuming decline rates. Remember that the decline rates for both of these are still negative 5%. So we are still using basically the same methodology to project out these productions and these reserve numbers after the end of the five-year period from 2010 to 2014.\
\
Remember that in terms of the prices, oil and natural gas liquids actually start at the same market price here of $75 a barrel. The difference is that the realization for natural gas liquids is much lower than it is for oil. Also with natural gas liquids, they have limited hedging going on. With oil they have a lot more hedging. So that’s what explains the massive difference here between the realized prices for NGLs and for oil. That’s typical. Usually the realization for NGLs is much, much lower than it is for oil. The realization does depend on the commodity itself, the region, and other factors, but just as a general guideline, for NGLs the realization is going to be much lower than it is for oil in most cases.\
\
Now for the total revenue, this is fairly straightforward. We are simply going to take our natural gas over here and take our annual production in billions of cubic feet, and then multiply by our average price per thousand cubic feet right here. Remember that by doing this, we’re effectively already converting this into millions, because 1 billion times 1/1,000 is really 1 billion divided by 1,000. A billion divided by a thousand is one million. So these units are already in millions.\
\
For oil and natural gas liquids, we’re going to take the production for both of those, multiply it by the average prices. So we have that. Then total revenue, we’re just going to sum these two up. Let’s copy this all the way down. So this gives us our revenue here.\
\
\[13:58\]\
\
We can see that this lasts around 12 years, just looking at the row and the notes in Excel here, 2010 to 2021. So our reserve life is not quite what we calculated before in the public comps and elsewhere in this model. That’s okay though. That’s actually quite typical, because again, it depends on your production assumptions here, and in this case, production is actually going up from 2010 to 2014, which explains why our RP ratio, or reserve life ratio, was higher on our public comps and in our operating model than it is in our net asset value model here.\
\
One other interesting thing to do here is to look at our total revenue number and compare it to what’s in XTO’s filings. So let’s do that and go back to our oil and gas supplement here, and go to their mini-NAV analysis at the bottom, second to last page here, the standardized measure of discounted future net cash flows relating to proved reserves.\
\
For 2009, at the end of the year, they have $57 billion or $58 billion. Notice the declining trend here from 2007 to 2009. That, of course, is because commodity prices, and especially gas prices, were declining over this period.\
\
Let’s look at this. This is basically their total revenue number. Let’s just compare it to ours. Sum these up with SUM equals. We get about twice their number. We have around $112 billion here. If we had to guess at what explains this difference in our model versus theirs, most likely it would be simply different price assumptions. Maybe they’re assuming much lower prices than we have. Based on the numbers, it seems like their prices are about half of what we have here. So that’s a possibility.\
\
It could also be a difference in production, but that doesn’t really make any sense, because we were both starting from the same proved reserves here. So it’s not really going to be a difference in production that explains it. For differences like this in a NAV model, it’s really going to come back to the difference in prices and price assumptions over the next 20 or 30 years here.\
\
So that’s how we set up the revenue side of our net asset value model. Coming up next in the next video in the series, we’re going to look at the expense side, production and development expenses, and then cash flows and after tax cash flows to figure out what the actual value of all this production is after expenses and after taxes. Then after that we’re going to look at some of their other assets, chemicals, midstream, downstream, and then undeveloped acreage, and then finally get to our share price and look at some sensitivities at the end.\
\
[For more tutorials on Oil Gas Modeling click here.](https://breakingintowallstreet.com/oil-gas-modeling/)\
\
[Premium Course Signup](https://breakingintowallstreet.com/oil-gas-modeling/)\
\
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)\
\
About Brian DeChesare\
---------------------\
\
Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)\
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)\
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.\
\
Files And Resources\
-------------------\
\
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) XTO Oil & Gas Supplement (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/72-XTO-O&G-Supplement.pdf)\
    \
\
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) NAV Revenue - Before (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/72-08-NAV-Part-1-Revenue-Before.xls)\
    \
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) NAV Revenue - After (XL)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/72-08-NAV-Part-1-Revenue-After.xls)\
    \
\
Premium Courses\
---------------\
\
Combined shape 37 Created with Sketch.\
\
Based on the content of this tutorial, our recommended Premium Course Upgrade is...\
\
[Oil & Gas Modeling](https://breakingintowallstreet.com/oil-gas-modeling/)\
\
Master financial modeling and valuation for the Upstream, Midstream, Downstream, and Oilfield Services verticals via U.S., European, and Asian case studies.\
\
[Learn More](https://breakingintowallstreet.com/oil-gas-modeling/)\
\
### Other BIWS Courses Include:\
\
Polygon 1 Created with Sketch.\
\
[BIWS Platinum](https://breakingintowallstreet.com/platinum/)\
: The most comprehensive package on the market today for investment banking, private equity, hedge funds, and other finance roles. Includes ALL the courses on the site at a huge discount, plus updates and new additions over time. [Learn More![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2019%2020'%3E%3C/svg%3E)](https://breakingintowallstreet.com/platinum/)\
\
Share\
\
[X](https://x.com/intent/tweet?text=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[LinkedIn](https://www.linkedin.com/shareArticle?title=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F&mini=true)\
[Email](mailto:?subject=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
\
#### Master Oil & Gas Modeling\
\
Learn financial modeling and valuation for the Upstream, Midstream, and Downstream verticals via U.S. and European case studies.\
\
[LEARN MORE](https://breakingintowallstreet.com/oil-gas-modeling/)\
\
[](https://x.com/intent/tweet?text=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[](https://www.linkedin.com/shareArticle?title=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F&mini=true)\
[](mailto:?subject=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model/)\
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F&title=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections)\
[](https://api.whatsapp.com/send?text=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
\
Share to...\
\
[Bluesky](https://bsky.app/intent/compose?text=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F&text=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections)\
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model/)\
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model/)\
[Copy](https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model/#)\
[Email](mailto:?subject=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F&title=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections)\
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model/)\
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model/)\
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F&t=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections)\
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F&text=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections)\
[LinkedIn](https://www.linkedin.com/shareArticle?title=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F&mini=true)\
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F&title=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections)\
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model/)\
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model/)\
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/12223148/87.jpg&description=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections)\
[Print](https://breakingintowallstreet.com/kb/oil-gas-modeling/nav-model/#)\
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F&title=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections)\
[SMS](sms:?&body=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F&text=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections)\
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[X](https://x.com/intent/tweet?text=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[WhatsApp](https://api.whatsapp.com/send?text=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F)\
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Foil-gas-modeling%2Fnav-model%2F&title=NAV%20Model%20for%20Oil%20%26amp%3B%20Gas%3A%20Revenue%20Projections&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/12223148/87.jpg&yumtype=button)\
\
This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  \
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)\
.I Understand