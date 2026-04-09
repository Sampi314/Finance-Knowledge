# What Ohtani’s Contract can Teach us About Discount Rates

**Source:** https://pivotal180.com/what-ohtanis-contract-can-teach-us-about-discount-rates

---

[Skip to content](https://pivotal180.com/what-ohtanis-contract-can-teach-us-about-discount-rates/#fl-main-content)

Understanding Discount Rates Through Real-World Examples in Finance
===================================================================

By Matt Davis | January 3, 2024

**_Sho’ money, Sho’ problems_: What A major athlete’s contract can teach us about discount rates**
==================================================================================================

Before the last Major League Baseball season even ended, fans and media around the world knew that the biggest story of the offseason would be about the sport’s best player. 

Over the past three seasons, Ohtani had firmly established himself as not only the sport’s best player, but a generational talent able to do things previously thought unimaginable on the diamond. In a highly specialized sport, Ohtani was the one man who could do it all. From 2021-2023, he was one of the game’s top hitters _and_ pitchers, swatting more home runs than all but three other players while simultaneously placing among the league leaders in most major pitching statistics. Ohtani won two Most Valuable Player awards and more-or-less invented the concept of a two-way baseball player.

Given those credentials and his looming free agency, it was all but certain the 29-year-old would ink baseball’s largest contract of all time. Industry prognosticators estimated Ohtani might secure as much as half a billion dollars guaranteed from one of the sport’s richest teams. So when Ohtani announced [via Instagram](https://www.instagram.com/p/C0pR_vyvLpR/)
 that he’d signed with the Los Angeles Dodgers, long a financial behemoth, that was no surprise. The reported [$700 million contract size](https://www.espn.com/mlb/story/_/id/39076745/shohei-ohtani-join-dodgers-10-year-700m-deal)
, however, blew all expectations away. But numbers – even, or perhaps especially, very big ones – can be deceiving.

The staggering $700 million headline number came with a major caveat: the majority of Ohtani’s salary, a whopping $680 million, would be deferred beyond the 10-year term of the contract. Instead of receiving equal salaries of $70 million per year for a decade, the contract called for a base salary of just $2 million per year from 2024-2033, with an additional $68 million paid in each of the next 10 years _after_ the contract ends. No major sports contract had ever been structured with such a high proportion of deferred salaries.

Why did Ohtani and the Dodgers agree to such extreme deferments? MLB enforces soft spending limits on teams via a mechanism called the Competitive Balance Tax, or CBT for short[\[1\]](https://pivotal180.com/what-ohtanis-contract-can-teach-us-about-discount-rates/#_edn1)
. Teams whose total player payrolls exceed certain levels pay increasingly severe penalties the more they spend. While not a hard salary cap, teams have generally been unwilling to blow past the top spending tiers and suffer the most onerous penalties.

An average annual salary of $70 million for one player – nearly 30% of the CBT threshold – might have significantly hamstrung the Dodgers’ ability to spend on other players and build a well-rounded team. By deferring over 97% of Ohtani’s money, his “average salary” for CBT calculation purposes is reduced from $70 million to just over $46 million; in other words, right in line with market estimates that he’d receive around $500 million in total over the full contract.

Many writers and fans – particularly of teams other than the Dodgers – have cried foul at this arrangement, accusing the team and player of sins ranging from tax dodging to accounting fraud. But extreme (even unlimited) deferrals are explicitly allowed under MLB’s rules. Instead, Ohtani’s reduced CBT salary figure is a textbook example of two core project finance concepts: **discount rates** and the **time value of money**.

**How does discounting work?**
------------------------------

The concept of time value of money (TVM) is relatively simple: $1 today is worth more than $1 in the future. You don’t have to (and shouldn’t, for your own sanity) ask your parents what they paid for their house 30 years ago to prove that. Any money you have today can be invested, earning value (e.g. interest from a savings account) over time so that the initial amount is worth more in the future. If I give you $1 today and you deposit it in a savings account earning 5% interest, it’ll be worth $1.05 in a year. If I give you $1 in a year, it’s just worth $1. The formula linking the _present value_ (**PV**) and _future value_ (**FV**) of an amount of money, discounted at a given rate (**r**) for a certain number of periods (**n**) is:![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20136%2055'%3E%3C/svg%3E)The corollary of this idea is that payments received in the future are worth less than payments received today. In project finance, we rely on this concept to size and sculpt non-recourse project loans. The amount of money that a project can borrow on the day it starts operating is determined by the cash flows it is expected to generate over time, _discounted_ by the interest rate on the loan. For example, a project that will generate $100 of cash per year to pay debt service over 10 years ($1,000 in total) can only borrow $772 at an interest rate of 5%. The sum of the principal and interest that the project will pay on the loan over 10 years equals that $1,000 it is expected to generate. In Excel, we can use the [NPV function](https://pivotal180.com/?p=1945) (for fixed interest rates) or [debt discount factors](https://pivotal180.com/?p=1942)
 (for variable interest rates) to calculate this.

**_Exhibit A: Simple discounting and debt sizing in Excel_**

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20622%20160'%3E%3C/svg%3E)

**How Discounting Applies to Real-World Contracts**
---------------------------------------------------

It’s not just that it combines my favorite sport with my profession! Baseball players (and other athletes) often sign multi-year contracts, tying them to a particular team for periods of several years. In a way, this can be thought of as the player loaning their capital – their skills and abilities on the field – to a team. If we assume the same 5% interest rate on the player’s “performance loan,” we could demonstrate that a 10-year contract paying $10 million per year ($100 million in total _future value_) is worth $79 million in _present value_.

In practice, MLB doesn’t discount non-deferred annual salaries for CBT calculation purposes. This is because the CBT threshold rises each year, implicitly reducing the value of $1 of salaries in each year. In the case of deferred salaries, however, payments that will be made _after_ the performance period of the contract are discounted back in order to determine their present value in each relevant contract year.

**Why This Matters in Project Finance**
---------------------------------------

Because Ohtani’s contract has a 10-year term with 10 years of deferred payments, the math is relatively simple. In each of years one through 10, the “average salary” for CBT purposes is equal to the $2 million to be paid in that year, plus $68 million of deferred payments discounted back by 10 years (i.e. the year 11 payment is discounted to year 1, the year 12 payment discounted to year 2, etc.). The discount rate under MLB’s rules is currently 4.43%[\[2\]](https://pivotal180.com/what-ohtanis-contract-can-teach-us-about-discount-rates/#_edn2)
, resulting in a discounted amount in each year of $44.08 million:

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%2062'%3E%3C/svg%3E)

Adding the $44.08 million discounted deferred annual payment to the $2 million annual salary, we get our average annual CBT salary of $46.08 million.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20635%20180'%3E%3C/svg%3E)

So, Ohtani’s contract isn’t actually worth $700 million, but $460.8 million in present value, right? Not quite! That $460.8 million, or $46.08 million per year, is the contract’s value _for CBT purposes only_, with deferrals only discounted by 10 years and non-deferred salaries not discounted at all as noted earlier. To calculate the real-world present value as of the contract, we need to discount _all_ of the salaries _all the way back to today_, deferred or otherwise.

If we assume that the contract was signed this past December 31 and that Shohei gets paid in full each year on June 30[\[3\]](https://pivotal180.com/what-ohtanis-contract-can-teach-us-about-discount-rates/#_edn3)
,  then the value of his contract is reduced to “only” $374 million in present-day dollars (at the 4.43% discount rate), just 53% of the nominal $700 million quantum. The massive deferrals weigh heavily here – the same contract with no deferrals would be worth $568 million (81% of nominal) in present value. (You can use the XNPV function in Excel to do this math yourself!) That Sho is a big difference (sorry).

It’s no wonder that players – and their agents! – love to announce contracts in undiscounted terms.

**Conclusion**
--------------

Nobody will be crying for Shohei Ohtani because his contract isn’t quite worth what the headline numbers claimed. Even on a discounted basis, it represents a record for North American professional sports. Contrary to detractors’ claims, though, its structure is no sort of tax or accounting fraud, just an extreme example of the power of discounting. Some may never be convinced by that argument, but it shouldn’t surprise you that the [man who signed Ohtani](https://www.mlb.com/dodgers/team/front-office/andrew-friedman) has a background in finance himself!

Accurate, best-practice discounting logic for debt sizing and sculpting is an essential part of any project finance model. Pivotal180 offers courses that ensure your team understand these concepts and can build an error-free model to examine the borrowing power of your project. Our in-person, live streamed and online self-paced classes include:

*   [Financial Modeling and Support](https://pivotal180.com/advisory/) 
*   [Project finance financial modeling](https://pivotal180.com/?course_type=project-finance-modeling)
    
*   [Renewable energy project finance modeling](https://pivotal180.com/?course_type=renewable-energy-project-finance-modeling)
    
*   [Tax equity modeling](https://pivotal180.com/?course_type=tax-equity-course-content)
    
*   [Introduction to Battery Storage](https://pivotal180.com/?course_type=battery-storage-financial-modeling) 

Intro to Baseball Economics coming soon! _(Ed. Note: No, Matt, it is not.)_

[\[1\]](https://pivotal180.com/what-ohtanis-contract-can-teach-us-about-discount-rates/#_ednref1)
 The CBT provisions discussed in this post are not technically MLB rules, but rather a provision of the Collective Bargaining Agreement between the league and the MLB Players Association.

[\[2\]](https://pivotal180.com/what-ohtanis-contract-can-teach-us-about-discount-rates/#_ednref2)
 The deferred salary discount rate for CBT purposes is equal the annual Federal mid-term rate as of the October prior to the contract’s start. As of October 2023, the Federal mid-term rate was 4.43%.

[\[3\]](https://pivotal180.com/what-ohtanis-contract-can-teach-us-about-discount-rates/#_ednref3)
 The contract was formally announced on December 11, and players are typically paid bi-monthly during the season (April-September), but these simplifying assumptions won’t impact our math much.

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fwhat-ohtanis-contract-can-teach-us-about-discount-rates%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fwhat-ohtanis-contract-can-teach-us-about-discount-rates%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fwhat-ohtanis-contract-can-teach-us-about-discount-rates%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#506f323f34296d38242420237563117562167562162039263f24313c6168607e333f3d756216273831247d3f3824313e39237d333f3e24223133247d33313e7d24353133387d25237d31323f25247d343923333f253e247d2231243523756216)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Matt Davis

[](https://pivotal180.com/what-ohtanis-contract-can-teach-us-about-discount-rates/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/what-ohtanis-contract-can-teach-us-about-discount-rates/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA