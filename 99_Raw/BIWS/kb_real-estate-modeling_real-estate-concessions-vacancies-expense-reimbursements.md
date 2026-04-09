# Real Estate Concessions, Vacancies & Expense Reimbursements (Video)

**Source:** https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-concessions-vacancies-expense-reimbursements

---

Real Estate Concessions, Vacancies, and Expense Reimbursements (27:48)
======================================================================

In this lesson, you’ll project the remaining key line items for Tenant #1, including the Absorption & Turnover Vacancy, Concessions & Free Rent, Tenant Improvements, Leasing Commissions, Expense Reimbursements, and General Vacancy, and you’ll learn how to check for downtime and free-rent periods on a monthly basis.

  Your browser does not support HTML video.

*   [Tutorial Summary](https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-concessions-vacancies-expense-reimbursements/#tab-synopsis)
    
*   [Files & Resources](https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-concessions-vacancies-expense-reimbursements/#tab-downloads)
    
*   [Premium Course](https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-concessions-vacancies-expense-reimbursements/#tab-signup)
    

**Table of Contents:**

*   **1:10:** Absorption & Turnover Vacancy and Concessions & Free Rent
*   **8:50:** Tenant Improvements
*   **12:35:** Leasing Commissions
*   **17:11:** Expense Reimbursements
*   **23:18:** General Vacancy
*   **24:43:** Recap and Summary

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

Transcript: Real Estate Concessions, Vacancies, and Expense Reimbursements (Excerpt from 4-Hour Office/Retail Acquisition and Renovation Case Study)
----------------------------------------------------------------------------------------------------------------------------------------------------

Welcome to our next lesson in this Real Estate Acquisition and Renovation Case Study for this Office Complex. We are going to look at the next set of line items for tenant number one in this lesson. And again, our strategy, as always, is to get these formulas figured out for tenant number one. And then once we do that, it’ll be fairly easy and straightforward to copy and paste them around for the other tenants here.

So, last time around we looked at the base rental income at market rates, the in-place rental incomes at escalated rates, and then the loss to lease line item, and we set up all the calculations that are necessarily to calculate those. Now, we’re going to move into the absorption and turnover vacancy, the concessions and free rent, the tenant improvements, the leasing commissions, the expense reimbursements, and the general vacancy line item, again, all sticking to what we have here for tenant number one. So, we’ll divide this lesson into five parts and go through, roughly speaking, each one of those in one part.

\[00:55\]

We’ll start off with the absorption and turnover vacancy and concessions and free rent then we’ll go into the tenant improvements in part two, then the leasing commissions in part three, the expense reimbursements and some of the expenses on the pro-forma in part four, and then the general vacancy in part five.

Let’s go to part one first and look at the absorption and turnover vacancy. So, as you can see here, this is a pretty easy formula because it’s only going to be active during the downtime period in between the initial lease expiration and the new tenant’s lease starting.

Now, if we did not have a very important constraint here, which is that we can assume at most one lease expiration for each tenant in the holding period, then this would be a lot more difficult, we’d have to come up with probability trees and we’d have to consider the possibility of many lease expirations, but since we are assuming that there is at most one lease expiration, it is quite simple to model this one.

So, let’s go up and enter this formula; we’ll enter an IF(AND and we want to get our month, as always, and we want to compare this to our lease expiration date right there. I’ll anchor the E part.

\[02:02\]

And then we’ll look at our month again, and we also want it to be less than or equal to our new lease start date right there – and this corresponds directly to the downtime period in between the lease expiration date and the start of the next lease.

And if that’s true, then we’re going to take the in-place rental income for the new tenant and just reverse that by putting a negative sign in front, and then I’ll say 0 if that is not true. So, we have the absorption and turnover vacancy; there isn’t really much to that. Let’s move to the concessions and free rent, which are a little bit more difficult.

So, for this one we really have three cases to think through: the case when the lease first starts, the renewal case when the lease expires and the existing tenant renews, and then the non-renewal case when the lease expires and it takes us some amount of time to find a new tenant, and that’s what each part of the formula here corresponds to.

\[02:56\]

I’m moving through this pretty quickly because it’s almost exactly the same as what we did in the office development case study. It’s just that the line items and the numbers are a little bit different, but the basic logic is almost the same.

So, to do this one, let’s enter an IF(AND function and, once again, we’ll get our month number and we want to check and make sure that this is past our lease start date right here, and then we want to check and do an EOMONTH function, look at our lease start date, and then move forward the number of rent-free months in this initial lease.

Now, you might be looking at this and thinking that it’s a bit pointless because the lease start date is somewhere in 2015, but our pro-forma here, our monthly rent roll schedule, only starts in January 2018. But remember, later on we will have some tenants whose leases start in 2019 or 2020 or 2021 or some other period that is shown in our monthly schedule right here.

\[03:55\]

So, to make this flexible, we are handling this case anyway. Even though, for this specific tenant, this particular case is not going to come up because 6 months past the lease start date have already passed as of the start of our monthly schedule here. In any case, if we’re in that rent-free period for the initial lease year, then we will simply reverse the in-place rental income for the initial tenant, and then I’ll say 0 otherwise. So, that’s the first part in the formula.

And then the next part of the formula, once again, we’ll enter an IF(AND function and we’ll look at our month right here, and for this one we need to look at lease expiration date. We’ll anchor the E part of that and then we’ll also look at our month once again and then we’ll do and EOMONTH function and we will look at our lease expiration date and move forward the number of free months that we grant the tenant upon lease renewal. That is defined over in our annual tab, as always. So, for the renewal, free-rent months – we’ll get it from right there. It’s 2 in this Base case.

\[04:59\]

So, if we’re in that period then we need to go up and we need to reverse the renewal tenant’s in-place rental income right there, and I’ll say 0 otherwise. And I can just delete the “Monthly!” part there. We don’t truly need it, and it makes it a little bit easier to read in this case. So, we have that.

And then the final case here is just the non-renewal case, so once again, I will go up and enter an IF(AND function. We’ll look at our current month and check to make sure that we are past our new lease start date right here. I’ll anchor the E part. We also want to go up and look at our month and make sure that we’re in that free-rent period for the new tenants, so say less than or equal to EOMONTH and then our new lease start date, anchor the E part and then go over and take our free months of rent for the new tenant over here, and then let’s go up and reverse the new tenant’s in-place rental income right there, and I’ll say 0 otherwise. So, we have that.

\[06:01\]

With that in place, we can copy this across, and let’s just verify quickly that this works before moving on to the next part of this process. So, for the absorption and turnover vacancy, let’s start with that line item. This should only activate when the lease actually expires. So, the lease expires in October 2020 and sure enough, we see one, two, three, four, five, six months for that and we do have 6 months of downtime. We can also see that this exactly matches the new tenant’s in-place rental income, which is in this case equal to the market rent times the non-renewal probability, so that seems to make sense. We don’t have anything else going all the way to the end.

And then for the concessions and free rent, we don’t have anything for the initial lease here because it began before January 2018. But if we look at what is going on here, for the renewal case, we should have 2 months of free rent and for the new case, we should have 3 months of free rent.

\[06:59\]

So, let’s look at these numbers. For the renewal case, we reverse exactly the initial tenant renewal in-place rental income for these 2 months. And then moving over to the new lease start date, we do the same thing right here. We take the new tenant’s base rental income or in-place rental income, rather, and reverse that for those 3 months. So, it appears that this is working correctly from our quick check.

If you want to do some further stress testing, you could look at the lease start date and we could say something like, let’s say this only starts in 2018 instead of 2015 and let’s make sure it actually works for the initial case now.

So, we have our baseline rental income here. We don’t have our general vacancy filled in yet, but that’s okay. Let’s just move over and see that this actually works as intended. So, concessions and free rent, in this case we have 6 months of free rent and it begins in November of 2018.

\[07:55\]

One, two, three, four, five, six, so we have six months total right there and you could see that we are reversing exactly the in-place rental income for this initial tenant, the $56,706 and then, moving across, we can see it keeps going and going and this should expire somewhere in 2023, which it appears to do here – and you can see we have absorption and turnover vacancy and also the concessions and free rent.

The concessions and free rent, of course, is for the renewal case right here, we reverse that. And then the absorption and turnover vacancy is for the new case where we essentially take the market rental income, we multiply it by the non-renewal probability, and then we reverse that for a certain period of time for the absorption and turnover vacancy. So, that appears to be working. That’s just something quick I wanted to show you; another way you can check your work as you’re going through this.

In any case, we’re done with part one now, the absorption and turnover vacancy and the concessions and free rent. Let’s now move to part two and talk about the tenant improvements and enter these formulas.

\[08:58\]

Now, the basic concept here is very, very similar. It’s also very, very similar for the leasing commissions. We have three cases in all of these: the initial lease, the renewal lease, and then the non-renewal case. For the tenant improvements, let’s go up and start entering these formulas. So, once again, we need to enter an IF statement and look at our current month and then for the initial case, we need to look at our lease start date right here, anchor the E part and go one past it.

So, if we’re one month past the lease start date which, again, really means if the lease starts on October 31st, the real start date is November of that year. Then we will take the new tenant improvements per rentable square foot, which we have defined as a named cell on the annual tab, and then we’ll go up and we will take our rentable square feet right here and I’ll anchor the E part so that does not shift around.

\[09:56\]

We’ll take that and then we’ll multiply it by the expense inflation multiplier right here because as times passes, these TIs, just as with the other expenses, should get more expensive simply because of inflation. So, that’s the first part of our formula. And then the second part is very, very similar. So, I am actually just going to copy this formula and paste it and just change a few things.

So, first off, the E24 here we need to change to E30, the renewal lease start date, because that’s the condition we’re checking here. The new TIs we need to change to renewal TIs instead. The E23 is the same because that is simply the rentable square feet that this tenant has. And then the F15, the expense inflation multiplier, is also the same. The one addition we need to make is we need to multiply by the renewal probability because these TIs were only incurred in the case that the existing tenant actually renews its lease. So, we have that.

And then for the last case here, once again, I’m going to copy and paste this formula and just tweak it a little bit.

\[10:59\]

So, for this one, we need to change the E30 to E35 because that is the new lease start date right here. I will change the Renewal TIs to the New TIs because this is a new tenant now from our perspective. The E23 can stay the same, the F15 can stay the same, and then the last part here is, I just need to make this (1 – the renewal probability) instead. So, we have that.

Let’s do a quick copy and paste around so we can check our work with this. So, we don’t have anything for the initial period, as expected. When the lease expires, we get some amount right here. We don’t have a really quick and easy way to check this, but we could take the renewal TIs and just do a bit of a manual check here by multiplying it by the rentable square feet and then multiplying it by the expense inflation multiplier and then multiplying it by the renewal probability, and it comes out with the same thing, so that’s a good sign.

\[12:01\]

And then let’s go over, and we have something in the non-renewal case as well. So, let’s take our non-renewal TIs, as I call them, and multiply it by our square feet and then we’ll multiply it by the expense inflation multiplier and then we’ll multiply it by (1 – this renewal probability), and it comes out with the same thing. So, that’s just a quick way we can check our work here. And we don’t have anything else until the end because those are the only relevant time periods for this one in the model. So, that’s pretty much it for the tenant improvements, part two.

Let’s go to part three now and look at the leasing commissions here. Once again, it’s exactly the same setup. It’s a little bit more complicated because, remember, the leasing commissions are based on the percentage times the total value of the lease. So, you have to take the initial lease rate and then you have to factor in the 2% or 3% or 4% annual escalation per year.

\[12:57\]

And the easiest way to do that in Excel is to use the FV function for “future value.” That will grow a number at a specified rate over a certain number of years and then sum up the values over those years. So, let’s go up and start entering these. Let’s enter an IF function, and then we need to check and see if we’re in the appropriate month for the initial lease start date. And if we are, then we are going to take the new leasing commission percentage, 6% right here, and then we can use the FV function for future value.

So, for the rate we need to go up and take our annual rental escalation right here. I will anchor this part so it does not shift around or anchor the E part of it, rather. Then we need to take our term right here, so the E25 part, that’s the number of periods, “nper”.

\[13:56\]

And then for the actual amount that we want to be escalating here, we want to take our escalated rent paid by initial tenant right here in the very first month that we have and then multiply it by the square feet, the rentable square feet that this tenant occupies, and I’ll anchor the E part of that. Once again, we can delete the monthly parts here because we don’t truly need them for this formula to work, and I think it’s easier to read without them in it and I’ll say 0 otherwise.

And I messed up something there. I forgot the comma in the middle of that function, so we have that. So, that’s the initial case. We can do something very, very similar for the others. So, for the renewal case, let’s just take this formula and I’ll copy and paste it. Let’s just tweak a few things here. The E24 will become E30 because that’s the renewal lease start date. The new leasing commission percentage will be changed to the renewal leasing commission percentage instead. And then the E27 right here will be changed to E33, the annual rental escalation for the renewal lease.

\[15:00\]

And then E25, the initial lease term that we’ll change to E31 instead. And then row 41 here should actually be row 42, so I’m going to change it to F42 for the escalating rent paid by the initial tenant in the renewal case. The E23 part can stay the same. And then the last thing we need to do is multiply this by the renewal probability because this only happens in the case where the tenant renews. So, we have that.

And then let’s enter the last case here. I’m going to copy and paste this formula. We’ll change the E30 here to E35 instead. And then for the renewal leasing commission percentage, I’ll change it to the new leasing commission percentage. The E33 I will change to E38 right there. And then the E31 I will change to E36 because we want the new lease term for this case.

\[16:03\]

The F42 I will change to F43. And then the E23, the rentable square feet, will stay the same. And then the last change is to make this (1 – the renewable probability) instead. So, we have that. Let’s copy and paste this around and just verify very quickly that it appears to be working. So, we have leasing commissions paid out in November of 2020 and then we should get them in May of 2021 and we do.

Now, it’s a bit difficult to actually check all the numbers here because the whole point of using the Future Value function is so that we don’t have to do this manually. But let’s just copy and paste the relevant part of the function outside of it and see if we get to the correct number here, so, $69,131, and we do. And then for the other one, we get to the same number there as well.

\[17:01\]

If you want to do more checking yourself, you could try to manually calculate this instead of using the future value function. I don’t really think it’s worth it. It seems to be working based on our quick inspection. That’s it for part three, the leasing commissions.

Let’s go to part four now, the expense reimbursements. Now, we need these because, remember, some of the tenants here have triple net leases. In fact, most of them have triple net leases. Some also have percentage rent. One tenant has a full service lease or will have a full service lease. And then one tenant has a double net lease with percentage rent. The point is that for any tenants with triple net or double net leases, they are going to have to reimburse some amount of expenses here, and so we need to figure out what that is and what the appropriate numbers here are.

Now, before we can do this, of course, we need to actually get the real expenses. So, we need to go down to our pro-forma and enter all the expenses right here, or at least the reimbursable expenses. Property management fees are never going to be reimbursable, so we’re not going to worry about them. Common area maintenance, though, will be.

\[18:01\]

So, let’s go and get our common area maintenance assumption, which should be right down here and then we multiply it by the total rentable square feet in the property. We’ll divide it by the months in the year, 12, to get this on a monthly basis. And then we also need to multiply this by the expense inflation multiplier to factor in how this will increase over time. So, we have that.

Now, for the insurance and utilities, it’s pretty much the same thing except we just have to change the main assumption here that we’re using. So, let’s get it for the insurance, I entered insurance here but it actually should be utilities for this one. So, common area utilities, let’s copy it down again, and then enter this for the insurance instead.

\[19:00\]

Now, the only one here that’s really different is the property taxes because these are based, typically, on a percent of the property’s value. So, for this one I’m going to take our acquisition price right here. We will multiply it by the property taxes as a percent of that, which we have as another assumption down here, the 2.55%. We’ll divide it by the months in the year to get this on a monthly basis, and then we’ll multiply it by that same expense inflation multiplier, the F15; I’ll anchor the 15 part. So, we have this.

Let’s go and copy this across now. And so we have that. And just taking a quick glance at this, we can see that these expenses are generally increasing over time, which is what we want to see, and they’re staying in about the same range on a monthly basis. So, with that set up, we can now actually enter our formula for the expense reimbursements here. So, I’m scrolling up to get to tenant number one.

\[19:59\]

The basic idea here is pretty simple, which is that as long as the initial lease has begun and we’re not in a downtime period in between one tenant’s lease expiring and us having to find a new tenant, we will get full expense reimbursements for everything applicable. If the lease has not yet begun, we will not get any expense reimbursements. And if we’re in that downtime period, we will get partial expense reimbursements. So, if there’s a 70% renewal probability, we should get 70% of the potential expense reimbursements for that period.

So, to implement this in Excel I’ll put a negative sign in front because we want to flip the sign of those expenses from negative to positive here. And then we’ll look at our month right up here and then I’ll say if this is greater than our lease start date then we’ll go down and we’ll the sum up everything here. We’ll anchor the row parts of those so those do not shift around.

\[21:01\]

And then we’ll go up, and we need to get the share that this tenant actually owes. So, we need to get their rentable square feet occupied and divide it by the total in the property to figure out the percentage, or, actually, we could just take the 25% right here. It doesn’t really matter. Come to think of it, the 25% is probably easier but I’ll just leave this as is for now.

So, we’re checking so far if the lease has actually begun, and then the second check is to make sure that we’re not in one of those downtime periods. So, once again, let’s look at our month and if we are past the lease expiration date right here and we are in or before the new lease start date, then we want to multiply this whole term by the renewal probability because we’re only going to have expense reimbursements here in full if the tenant renews.

\[21:56\]

So, we’re going to multiply by that 70% or 60% or 50% or whatever it is; otherwise we will multiply it by 1. That’s the cleanest, simplest way to do it here. So, if we’re not in that period, we will just get the normal full expense reimbursements and then I’ll say 0 if the lease has not yet begun. And I forgot to enter an AND right here for this function, so let’s just fix that quickly. So, we have that. Let’s copy this around to make sure this is actually working.

So, for the most part in most of these periods, we should be reversing the tenant’s share of all these expenses on the pro-forma. But we should see a dip as soon as the lease expiration occurs and, sure enough, we do. If we just do the rough math here, it comes out to around a 60% drop, and sure enough, our renewal probability in this Base case is 60%, so that makes sense intuitively, just doing the quick math here.

\[23:00\]

Now this lasts for one, two, three, four, five, six months. We have 6 months of downtime, so it makes sense. And then right after that, it resumes back to its normal level. We could do some more extensive checks for this, but you’ll see more about how this works once we copy and paste this formula around for the other tenants. That’s it for part four, the expense reimbursements.

Let’s go to part five now and look at the general vacancy. This is really, really easy, probably the easiest thing here because there isn’t much to it. Put simply, if the initial lease has not yet begun, then we have to reverse the full market rental income and record it as a negative for this item. So, all we do here is look at the month that we’re in, and if it is less than or equal to the lease start date right here, then we will take our market rent per square foot per year, we’ll multiply it by the tenant’s rentable square feet occupied, we’ll divide it by the months in the year, and we’ll say 0 otherwise. So, this should be 0 everywhere for this particular tenant.

\[23:59\]

If we want to check and make sure that this is actually working, we could try changing this to a start date of 2018 instead, and let’s see what happens here. And in this case, we completely offset the market rental income with the general vacancy line item. So, we have that. And then we can see that once this initial lease starts now in 2018, we get tenant improvements and leasing commissions. We don’t have any expense reimbursements for that, but we do get expense reimbursements after that. And then if you go all the way across, everything stays as is. We don’t get any more general vacancy, and then when it comes up for renewal and we get the lease expiration in 2023, then we get the TIs and the LCs, the absorption and turnover vacancy, the free rent, and those other items.

So, that’s just a quick and simple way that you could check your work here. With that, we are now done with the formulas for tenant number one. Now, I’m not going to copy and paste them around at this stage because I want to finish one more thing, which is, namely, figuring out the percentage rent. We’ll look at that in the next lesson. Once we have that figured out, then we can go in and copy and paste around all the formulas for all the other tenants.

\[25:02\]

But since we’re at the end of this lesson, let’s do a recap and summary. So, in part one, we started with absorption and turnover vacancy and the concessions and free rent. This is pretty simple and straightforward. If we’re in a downtime period, then we reverse the new tenant’s in-place rental income, which should be the same as the market rental income for that downtime period. And that’s all there is to the absorption and turnover vacancy.

For the concessions and free rent, tenant improvements, and leasing commissions, we always have three cases: the initial case, the renewal case, and the non-renewal case. And in each case, we simply do a date check and then we bring in the appropriate numbers. So, for the concessions and free rent, if the lease has just begun, then we look at the initial lease rent-free months right here, and if we’re in that period, then we reverse the in-place rental income for the initial tenant. If we’re in the renewal phase, then we reverse that in-place rental income. And if we’re in the new tenant phase, then we reverse that in-place rental income.

\[26:01\]

For the tenant improvements, it’s very similar except here we have to multiply it by the renewal probability or the non-renewal probability. We also have to factor in renewal versus new TIs and then also the expense inflation multiplier up here and the rentable square feet occupied by this tenant.

And then for the leasing commissions, it’s also very, very similar except we now use the FV, the future value function, to calculate the total value of the escalated rent over five years or six years or four years or whatever it is. We multiply it by the percentages. We probability weight this by multiplying by the renewal probability or (1 – the renewal probability), and then we have that.

For the expense reimbursements, we had to go down to the pro-forma first and actually fill in some of the expenses here, the ones that are reimbursable by tenants, potentially, which are pretty simple and straightforward. These are mostly on a per-rentable-square-foot basis. The real estate and property taxes are not. Those are based on a percent of the property’s value or the acquisition price.

\[27:00\]

Once we had those, we went back and essentially we bring in these expense reimbursements. If the lease has actually begun and then if we’re in that downtime period, we reduce these and we multiply them by the renewal probability to represent the fact that if there’s a non-renewal, we are not going to get expense reimbursements in that period.

And then finally, for the general vacancy, if we’re before the lease start date, then we reverse the market rent per square foot per year. I could have also done it more simply by just linking to the baseline rental income at the market rate right there. It doesn’t really matter what you do, but that’s the basic idea for this one.

So, that’s it for this lesson. Coming up next, as I said, we’ll look at the percentage rent and a few different ways you can calculate that, and then we’ll get into the business of copying and pasting these formulas around to set up our monthly pro-forma for this property.

[See BIWS Real Estate Modeling Course](https://breakingintowallstreet.com/real-estate-modeling/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20190%20190'%3E%3C/svg%3E)

About Brian DeChesare
---------------------

Brian DeChesare is the Founder of [Mergers & Inquisitions](https://mergersandinquisitions.com/)
 and [Breaking Into Wall Street](https://breakingintowallstreet.com/)
. In his spare time, he enjoys lifting weights, running, traveling, obsessively watching TV shows, and defeating Sauron.

Files And Resources
-------------------

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Lesson Transcript](https://samples-breakingintowallstreet-com.s3.amazonaws.com/RE-05-03-Vacancies-Concessions-LCs.pdf)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) 4-Hour Office/Retail Acquisition and Renovation Case Study (PDF)](https://samples-breakingintowallstreet-com.s3.amazonaws.com/RE-05-Office-Acquisition-Renovation-Case-Study.pdf)
    

*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Concessions, Vacancies, TIs, LCs, and Expense Reimbursements - Before](https://samples-breakingintowallstreet-com.s3.amazonaws.com/RE-05-03-Vacancies-Concessions-LCs-Before.xlsx)
    
*    [![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2020%2020'%3E%3C/svg%3E) Concessions, Vacancies, TIs, LCs, and Expense Reimbursements - After](https://samples-breakingintowallstreet-com.s3.amazonaws.com/RE-05-03-Vacancies-Concessions-LCs-After.xlsx)
    

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

[X](https://x.com/intent/tweet?text=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F&mini=true)
[Email](mailto:?subject=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)

#### Master Real Estate Modeling

Master financial modeling for real estate development and private equity with 11 global case studies based on property acquisitions, developments, and renovations.

[LEARN MORE](https://breakingintowallstreet.com/real-estate-modeling/)

[](https://x.com/intent/tweet?text=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[](https://www.linkedin.com/shareArticle?title=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F&mini=true)
[](mailto:?subject=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-concessions-vacancies-expense-reimbursements/)
[](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F&title=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29)
[](https://api.whatsapp.com/send?text=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)

Share to...

[Bluesky](https://bsky.app/intent/compose?text=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[Buffer](https://buffer.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F&text=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29)
[ChatGPT](https://chat.openai.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-concessions-vacancies-expense-reimbursements/)
[Claude](https://claude.ai/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-concessions-vacancies-expense-reimbursements/)
[Copy](https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-concessions-vacancies-expense-reimbursements/#)
[Email](mailto:?subject=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29&body=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[Flipboard](https://share.flipboard.com/bookmarklet/popout?v=2&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F&title=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29)
[Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-concessions-vacancies-expense-reimbursements/)
[Grok](https://grok.com/?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-concessions-vacancies-expense-reimbursements/)
[Hacker News](https://news.ycombinator.com/submitlink?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F&t=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29)
[Line](https://lineit.line.me/share/ui?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F&text=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29)
[LinkedIn](https://www.linkedin.com/shareArticle?title=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F&mini=true)
[Mastodon](https://mastodon.social/share?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F&title=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29)
[Messenger](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[Mistral AI](https://chat.mistral.ai/chat?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-concessions-vacancies-expense-reimbursements/)
[Mix](https://mix.com/add?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[Nextdoor](https://nextdoor.com/sharekit/?source={website}&body=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[Perplexity](https://www.perplexity.ai/search/new?q=Summarize%20the%20content%20of%20this%20URL:%20https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-concessions-vacancies-expense-reimbursements/)
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F&media=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/04224940/Real-estate-concessions-1.jpg&description=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29)
[Print](https://breakingintowallstreet.com/kb/real-estate-modeling/real-estate-concessions-vacancies-expense-reimbursements/#)
[Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F&title=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29)
[SMS](sms:?&body=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29%20https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[Telegram](https://telegram.me/share/url?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F&text=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29)
[Threads](https://www.threads.net/intent/post?text=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[Tumblr](https://www.tumblr.com/widgets/share/tool?canonicalUrl=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[X](https://x.com/intent/tweet?text=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29&url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[VK](https://vk.com/share.php?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[WhatsApp](https://api.whatsapp.com/send?text=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29+https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[Xing](https://www.xing.com/spi/shares/new?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F)
[Yummly](https://www.yummly.com/urb/verify?url=https%3A%2F%2Fbreakingintowallstreet.com%2Fkb%2Freal-estate-modeling%2Freal-estate-concessions-vacancies-expense-reimbursements%2F&title=Real%20Estate%20Concessions%2C%20Vacancies%2C%20and%20Expense%20Reimbursements%20%2827%3A48%29&image=https://biwsuploads-assest.s3.amazonaws.com/biws/wp-content/uploads/2019/04/04224940/Real-estate-concessions-1.jpg&yumtype=button)

This website and our partners set cookies on your computer to improve our site and the ads you see. To learn more about  
what data we collect and your privacy options, see our [privacy policy](https://breakingintowallstreet.com/privacy-policy/)
.I Understand