# Calculate CAGR (Compounded Annual Growth Rate) using Excel [Formulas] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/calculate-cagr-using-excel

---

Calculate CAGR (Compounded Annual Growth Rate) using Excel \[Formulas\]
=======================================================================

[Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
 - 34 comments

  

**Here is a story we all are familiar with,**

Jack learns about compound interest in school. He quickly forgets about it while learning other complicated things like trignometry, partial differentiation, correct spelling of trigonometry etc. Jack graduates and ends up with a job he loves / hates. Years pass and one day out of boredom jack looks thru mail and stumbles on a credit card bill. As Jack has nothing else to do, he opens it. _He looks at something and wonders why his credit card number has only 7 digits!_

Then he realizes that it is the amount he owes to credit card company!!!

Jack scratches his head vigorously and wonders how the tiny bits of money he spends on gas, toothpaste and occasional pizza can add up to $19,234.55 ?

Then he realizes the true power and meaning of compound interest!

**The moral of the story:** Never open a credit card bill.

_Of course the real moral is, **understand the power of compound interest and use it to your advantage.**_

_But we are not here to talk about unhealthy money habits._

_**We are here to talk about awesome benefits of Excel.**_

So moving on, lets talk about how we can use Excel to calculate **Compounded Annual Growth Rate (CAGR for short).**

### What is CAGR? What does it signify?

Let us say you are the CEO of ACME Inc. You have been selling various widgets since 2009. In your latest annual report you want to tell your shareholder at what rate you have been growing ACME Inc. sales. The figure are,

*   2009 – $150 Mn
*   2010 – $125 Mn
*   2011 – $160 Mn
*   2012 – $174 Mn
*   2013 – $195 Mn
*   2014 – $210 Mn

Now, if you see the growth rates, they are all over the place. Right from -16.67% to 28%. **But you want to report a single annual growth rate.**

This is where CAGR (Compounded Annual Growth Rate) comes handy.

Imagine that the sales of ACME Inc. _**grew at constant rate every year from $150 Mn in 2009 to reach the $210 Mn in 2014**_. This is what CAGR represents.

As you can see, **CAGR removes all the volatility in the numbers to tell at what uniform rate the numbers grew** (or declined) every year.

### Arithmetic behind CAGR

While we can never explain the arithmetic behind how credit card companies calculate interest, penalties, fees, interest on penalties and miscellaneous charges, we can easily understand the logic of CAGR.

You see CAGR uses the all important compound interest math at the heart.

**Lets throw a few variables in to this article now:**

Lets say the starting value is P (in our case P= $150 Mn in 2009)

End value is A (A = $210 Mn in 2014)

and N represents the number of years it took P to become A. In our case N is 5 years.

R denotes the rate of growth (CAGR).

The basic equation is

![Compound Interest Equation for calculating CAGR using Excel](https://img.chandoo.org/f/equation-for-compound-interest.png)

**A = P \*(1+R/100)^N**

And we need to find R.

So lets do some simple Arithmetic. Lets expand,

![Expanding Compound Interest equation to find R](https://img.chandoo.org/f/expanding-compound-interest-equation.png)

not that kind of expansion, you silly!

We need to do this:

![Finding Compounded Annual Growth Rate (CAGR) using Excel](https://img.chandoo.org/f/calculating-R-CAGR-using-arithmetic-equation.png)

The final equation for R is **\=(A/P)^(1/N) – 1**

Calculating CAGR in Excel
-------------------------

Now that we have finished a crash course in arithmetic behind compound interest, we can calculate CAGR in Excel. There are 3 ways to do this.

1.  Using raw arithmetic as shown in above equation.
2.  Using RATE formula
3.  Using IRR formula

### Using arithmetic equation for calculating CAGR

![Calculating CAGR (Compounded Annual Growth Rate) using Excel arithmetic](https://img.chandoo.org/f/calculating-cagr-using-arithmetic.png)This is simple. Assuming,

*   P is the initial value
*   A is the last value
*   N is the number of years

in a blank cell, write

\=(A/P)^(1/N) – 1

And you get the Compounded Annual Growth Rate as output. (Just need to format the cell as %).

### Using RATE() formula

![Calculating CAGR using RATE() formula in Excel](https://img.chandoo.org/f/calculating-cagr-using-RATE-function.png)RATE() is a financial formula (function) in Excel that can tell us what would be the interest rate for an annuity. Sounds complicated? See this example:

Lets say, as the CEO of ACME Inc. you took a loan of $30Mn to expand your company. You agreed to pay $5 Mn per year for next 10 years to pay off the loan. So what is the effective rate of interest?

**\=RATE(10, 5, -30) tells us that the rate of interest is 10.558%**

We can use RATE() formula with below parameters to calculate CAGR,

\=RATE(N,,-P,A)

Explanation:

In our situation, we want to know at what uniform rate the sales grew from $150 Mn in 2009 to $210 Mn in 2014.

This is same as taking a loan of $150 Mn in 2009 and paying off $0 per year for 5 years and paying one lump-sum payment of $210 Mn in 2014.

So we use =RATE(N,,-P,A) to indicate that we are paying $0 per year (hence omission of 2nd parameter) and paying one lump-sum amount at the end.

### Using IRR() formula

While the above 2 formulas do not require any changes in the original data, this one requires that we re-shape the data.

See this picture:

![Calculating CAGR using IRR() function in Excel](https://img.chandoo.org/f/calculating-cagr-using-IRR-function.png)

So original data in B3:B8 is re-shaped in D3:D8,

Now, use =IRR(D3:D8) to get the rate of growth (CAGR).

Related: [Using IRR() function over a dynamic range with OFFSET](http://chandoo.org/wp/2011/10/04/offset-function-to-calculate-irr-for-dynamic-range/)
.

### Other scenarios where CAGR is helpful

*   You purchased some shares at $100.00 per share on 1st of February 2007. You sold them off at $270.13 per share on 3rd of April 2014. What is your annual rate of return?
*   Your website traffic was 15,000 page views per month in Jan 2012. In March 2014 it is 75,000 per month. What is the monthly growth rate?
*   You had 10 paying clients when you started business 5 years ago. Today you have 300. What is the annual growth rate?

### So what method do you use to calculate CAGR?

I have always relied on the brute arithmetic calculation of (A/P)^(1/N) -1. I guess derive strange pleasure writing equations in Excel cells.

_**What about you?**_ Do you compute CAGR? Where do you use it? And what method do you use to calculate it? **Please share your tips & thoughts in comments.**

### Feeling love towards money & modeling it in Excel?

While it may take us forever to earn few millions or pay off that student loan, _we can model all of that in Excel in a few hours!_ Here are a bunch of articles to help you get started with just that.

*   [Financial modeling using Excel (6 part tutorial)](http://chandoo.org/wp/2010/07/21/financial-modeling-introduction/)
    
*   [Mortgage calculator using formulas & form controls](http://chandoo.org/wp/2010/01/20/mortgage-payment-calculator/)
    
*   [When can you retire, find out using goal seek](http://chandoo.org/wp/2009/07/29/excel-goal-seek-tutorial/)
    
*   [Growing a money mustache using Excel](http://chandoo.org/wp/2012/08/22/growing-a-money-mustache-using-excel/)
    

![Chandoo](https://chandoo.org/wp/wp-content/uploads/2018/05/chandoo-profile-pic.png)

**Hello Awesome...**

My name is Chandoo. Thanks for dropping by. My mission is to make you awesome in Excel & your work. I live in Wellington, New Zealand. When I am not F9ing my formulas, I cycle, cook or play lego with my kids. Know more [about me](https://chandoo.org/wp/about/)
.

I hope you enjoyed this article. Visit [Excel for Beginner](https://chandoo.org/wp/excel-basics/)
 or [Advanced Excel](https://chandoo.org/wp/advanced-excel-skills/)
 pages to learn more or join my [online video class to master Excel](https://chandoo.org/wp/excel-school-program/)
.

Thank you and see you around.

### Related articles:

|     |     |
| --- | --- |
| Written by Chandoo  <br>Tags: [CAGR](https://chandoo.org/wp/tag/cagr/)<br>, [financial formulas](https://chandoo.org/wp/tag/financial-formulas/)<br>, [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)<br>, [IRR](https://chandoo.org/wp/tag/irr/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [rate()](https://chandoo.org/wp/tag/rate/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 34 Responses to “Calculate CAGR (Compounded Annual Growth Rate) using Excel \[Formulas\]”

1.  ![](https://secure.gravatar.com/avatar/92dfc87c771a87a2cda90c7d601ed984549f2bdd1f7a756a9c0ee187dadce400?s=64&d=mm&r=g) Excel says:
    
    [April 29, 2014 at 12:05 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-500101)
    
    I use the power formula to calculate the CAGR.  
    power(A/P,1/5)-1
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-500101)
    
2.  ![](https://secure.gravatar.com/avatar/a5e95347c3ad4df7e3cd5fde19c76d215b41a65ba159584073604dbc449da063?s=64&d=mm&r=g) [Mike Alexander](http://www.datapigtechnologies.com/)
     says:
    
    [April 29, 2014 at 2:22 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-500318)
    
    Very well written Chandoo. Great explanation.
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-500318)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [April 30, 2014 at 4:23 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-501830)
        
        Thank you Mike. Your compliment means a lot 🙂
        
        [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-501830)
        
3.  ![](https://secure.gravatar.com/avatar/c99c48eab87e12c73dd4891b280faa9b0f2077f87ffee64794a925352a746734?s=64&d=mm&r=g) Bob says:
    
    [April 29, 2014 at 6:08 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-500727)
    
    Back in the dark ages I was taught that CAGR (or AAGR - Average Annual Growth Rate) was the exponential growth rate of the line that best fit all the data. i.e., that you had to consider the data from all of the data points. The 6.96% CAGR you calculate ignores the performace in intervening years, notably the large sales drop in 2010. Therefore I would use LOGEST(B3:B8)\*-1 and say that a more representative estimate of the average compound growth of ACME's sales over the period from 2010 to 2014 was 9.26% - more attractive than 6.96%. If ACME's sales were: 150,220,230,240,180,210 your calculations would still yield 6.96% while LOGEST would calculate the average growth to be 3.26%.
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-500727)
    
4.  ![](https://secure.gravatar.com/avatar/4255b05ff39edad0c0da6783f96d60dde0da0fde2def1e0264877152e0dc1c76?s=64&d=mm&r=g) Brian says:
    
    [April 29, 2014 at 7:20 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-500879)
    
    Using IRR to calculate the rate of growth of sales is not strictly speaking a correct application of the IRR concept IMHO. The IRR function is intended to measure the return on an amount invested. In your example the final sales figure would represent the amount realised at the end of the investment term rather than the level of sales ( or any other variable) at a particular time. But interesting application nevertheless.
    
    Also an interesting post about LOGEST function Bob. How does it handle negative values ? As you know the IRR doesn't handle negatives very well, sometimes producing two or more solutions to the same problem.
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-500879)
    
5.  ![](https://secure.gravatar.com/avatar/bdaafe0a89ba7a9193a291a8d6d8f142dc924f24d8521166cd7de045833c9823?s=64&d=mm&r=g) sswilcox says:
    
    [April 29, 2014 at 7:51 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-500939)
    
    I always use the full mathematical formula and have never considered the notion of using an Excel formula as an alternative. Of course, I then always verify the CAGR by plugging it back in and making sure I end up at the correct number. So much for shortcuts.
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-500939)
    
6.  ![](https://secure.gravatar.com/avatar/c99c48eab87e12c73dd4891b280faa9b0f2077f87ffee64794a925352a746734?s=64&d=mm&r=g) Bob says:
    
    [April 29, 2014 at 8:23 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-501002)
    
    LOGEST doesn't handle negatives well at all. If ACME had negative sales that would probably be a signal to avoid them. However, if looking at profits and some periods were negative we would have the formula return "NMF" - No Meaningful Figure - instead of the #NUM! error and then use cumulative profits/cumulative sales to compare competitor profitability (or couple Sales Growth with absolute improvement in % Return on Sales over the period being analyzed.) Three key measures: Grow sales faster than your world (i.e. gain market share); grow your income faster than your sales (i.e. improve ROS/become more efficient); and grow cash faster than your income (effectively manage your assets).
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-501002)
    
7.  ![](https://secure.gravatar.com/avatar/b4873ed7f148fdcb5565d2c4088a97919284dc89a4136ec30bb01da7ce856939?s=64&d=mm&r=g) jraju says:
    
    [April 30, 2014 at 6:19 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-502036)
    
    Hi,  
    Cagr could be used only for those parameters, where you are having a kind of closing stock. Opening stock etc. But in calculating the growth rate of Gross State Domestic Product and such a kind of parameters, then this formula could not be used. Only mere arithmetic average could be used. Because, the Value added to the particular years are only taken in to account for GSDP. Any comments, chandoo, Am I correct
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-502036)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [May 3, 2014 at 4:11 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-509340)
        
        Hi Jraju.. I think CAGR works even in such cases too.
        
        When someone says Country X's GDP grew by 8% on average in the last 5 years, I would imagine the GDP grew from 100 to 136 in 5 years, not 132.
        
        When you explain 100 to 136, 8% would be the CAGR.
        
        [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-509340)
        
8.  ![](https://secure.gravatar.com/avatar/b4873ed7f148fdcb5565d2c4088a97919284dc89a4136ec30bb01da7ce856939?s=64&d=mm&r=g) jraju says:
    
    [May 3, 2014 at 2:04 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-509144)
    
    Hi,  
    Chandoo, could i expect your views on my point above about using arithmetic average for gsdp
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-509144)
    
9.  ![](https://secure.gravatar.com/avatar/b4873ed7f148fdcb5565d2c4088a97919284dc89a4136ec30bb01da7ce856939?s=64&d=mm&r=g) jraju says:
    
    [May 3, 2014 at 7:34 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-509708)
    
    Hi, chandoo,
    
    Please review the use of cagr in gsdp . The gross value added from each sector for the year only has been taken in to the calculation of GSDP. There is no opening stock or closing stock to brought forward in such case. So, only arithmetic mean, that is the growth rate of each year divided by the no of years is the possible way, as far as i know. Expecting your clarification
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-509708)
    
10.  ![](https://secure.gravatar.com/avatar/1cdbacd1cfdaa17d9caf0a5e40b6faeca3c91d73c8540a725dd95780ce1c08f6?s=64&d=mm&r=g) Luis says:
    
    [May 8, 2014 at 7:10 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-525785)
    
    I use =RRI(nper,pv,fv)  
    It is very simple
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-525785)
    
11.  ![](https://secure.gravatar.com/avatar/1e2bf19d134d1252f425784fbed648b6dcad1a4d3396e28b8bed463bc33bd9e2?s=64&d=mm&r=g) Rupa says:
    
    [May 22, 2014 at 2:52 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-539490)
    
    Nice explanation.
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-539490)
    
12.  ![](https://secure.gravatar.com/avatar/0d2e6fe79f833cf4cf431a3a09050a7b71b5b93acaf10ee984218731aa36eed3?s=64&d=mm&r=g) tony says:
    
    [July 15, 2014 at 6:19 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-573452)
    
    Very beautiful, but can further explain how to calculate a compound monthly growth rate (CMGR).  
    Thank you
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-573452)
    
13.  ![](https://secure.gravatar.com/avatar/b4873ed7f148fdcb5565d2c4088a97919284dc89a4136ec30bb01da7ce856939?s=64&d=mm&r=g) jraju says:
    
    [July 16, 2014 at 4:00 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-573673)
    
    Hi, Chandoo  
    Expecting your clarification on using cagr in gsdp
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-573673)
    
14.  ![](https://secure.gravatar.com/avatar/918460b3a81c416a0aa25403dc2bd94e8055518c143cb0b206855f8d5d63c84d?s=64&d=mm&r=g) [Joy](http://none/)
     says:
    
    [September 24, 2014 at 7:37 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-782656)
    
    Hi Chandoo,  
    How to calculate if I hv yearly growth rates and not absolute figures.
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-782656)
    
    *   ![](https://secure.gravatar.com/avatar/c99c48eab87e12c73dd4891b280faa9b0f2077f87ffee64794a925352a746734?s=64&d=mm&r=g) Bob says:
        
        [September 24, 2014 at 2:25 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-783959)
        
        If you have no absolute values you can set the first year to 1 and construct an an annual index \[prior period index \* (1+ Annual Growth Rate)\] for each year. The Compound Growth Rate of this calculated index, calculated using the Logest function as I suggested in above comments, will be the same as if you had all the actual values. I assume the other calculation methods would work as well. As noted in above discussion, if an actual value (not the % change) is negative, calculating a meaningful CGR is problematical.
        
        [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-783959)
        
        *   ![](https://secure.gravatar.com/avatar/918460b3a81c416a0aa25403dc2bd94e8055518c143cb0b206855f8d5d63c84d?s=64&d=mm&r=g) [Joy](http://none/)
             says:
            
            [September 29, 2014 at 8:20 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-795016)
            
            Many thanks Bob its really working...
            
            [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-795016)
            
15.  ![](https://secure.gravatar.com/avatar/5bea226ff12dfa6fc4ebf82e7a27c3cf023421c3a78327d3b8481ad78b80416f?s=64&d=mm&r=g) Umesh says:
    
    [October 8, 2014 at 12:06 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-802712)
    
    Sometimes you might feel that CAGR is not an effective way of calculating the growth. For ex. in calculating the CAGR %, what is important is the Value during the base year & Value during the final year of calculation, all other values are non-significant. So irrespective of what growth rates are achieved (even 0 or negative) during the intermediary years, CAGR is calculated based on the final year results & first year results only.
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-802712)
    
16.  ![](https://secure.gravatar.com/avatar/c99c48eab87e12c73dd4891b280faa9b0f2077f87ffee64794a925352a746734?s=64&d=mm&r=g) Bob says:
    
    [October 8, 2014 at 1:54 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-802802)
    
    I beg to differ with Umesh. I beleive that all the points in a trend are relevant. Would you rather have a business with periodic revenues of 10, 15, 20, 25, 30 or a stock with periodic revenues 10, 5, 20, 10, 5, 30? Some may like the roller coaster but others get sick. Ignoring intermediate points is quick and easy but ignores both cummulative revenues and very important volatility.
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-802802)
    
    *   ![](https://secure.gravatar.com/avatar/c4b491bb390e7d0a8d069ec0939a60d37ae99d41176a69d10ba51059d08c8d42?s=64&d=mm&r=g) Mike says:
        
        [January 12, 2015 at 1:25 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-892379)
        
        Bob - I was very happy to find your comments here. I've been warning folks for years about the pitfalls of the CAGR in terms of expressing historical trends, and it's nice to happen upon the same arguments by an independent source.
        
        I've just started a blog about analyzing industries and markets, and I cover the topic here: [http://theindustryanalyst.info/2014/12/30/the-cagr-handle-with-care/comment-page-1/#comment-2](http://theindustryanalyst.info/2014/12/30/the-cagr-handle-with-care/comment-page-1/#comment-2)
        
        Perhaps you'd be so kind as to review my post. (I hope to elaborate on LOGEST in a later post.)
        
        Many thanks.
        
        [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-892379)
        
        *   ![](https://secure.gravatar.com/avatar/c4b491bb390e7d0a8d069ec0939a60d37ae99d41176a69d10ba51059d08c8d42?s=64&d=mm&r=g) Mike says:
            
            [January 12, 2015 at 1:27 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-892382)
            
            Bob - this is a better link: [http://theindustryanalyst.info/2014/12/30/the-cagr-handle-with-care/](http://theindustryanalyst.info/2014/12/30/the-cagr-handle-with-care/)
            
            [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-892382)
            
            *   ![](https://secure.gravatar.com/avatar/c99c48eab87e12c73dd4891b280faa9b0f2077f87ffee64794a925352a746734?s=64&d=mm&r=g) Bob says:
                
                [January 13, 2015 at 3:06 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-893254)
                
                Mike - Nice clear article on CAGR versus AAGR. In many instances calculating a point to point CAGR can be very misleading.
                
                [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-893254)
                
17.  ![](https://secure.gravatar.com/avatar/1a211beba4417b92fa96fd0f5c7a5de326cf315289c585e636efe34e383845df?s=64&d=mm&r=g) Elizabeth Crum says:
    
    [November 11, 2014 at 11:04 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-845982)
    
    Hi there - I am using the RATE funtion to calculate CAGR, using your example above. The "starting" point (2009) is annual sales for a product. The number is not negative, how do I keep the number positive in the spreadsheet, yet use the RATE function? I tried putting in a negative sign in the formula and it didn't work.... I had to change the first sales figure to a negative number. Thank you!
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-845982)
    
    *   ![](https://secure.gravatar.com/avatar/c99c48eab87e12c73dd4891b280faa9b0f2077f87ffee64794a925352a746734?s=64&d=mm&r=g) Bob says:
        
        [November 12, 2014 at 2:36 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-846906)
        
        The negative sign has to be in front of the pv argument. So if your starting point value is in cell A2 then the formula should be RATE(number of periods , , -A2 ,ending value. If your values are in A2:A5, e.g., 10,15,20,25. Then the formula would be:  
        \=RATE(3,,-A2,A5) which would return 35.72%.  
        I continue to think that using RATE is not the best way to calcualte CAGR - see my comments above.
        
        [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-846906)
        
18.  ![](https://secure.gravatar.com/avatar/e5a1a3f087742bab099b4a10383345e5289cb88358ab998f60e17811a2b47a13?s=64&d=mm&r=g) Sreedhar says:
    
    [February 11, 2015 at 12:22 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-911128)
    
    Thanks. Here is a questions.  
    Would this brute arithmetic calculation of (A/P)^(1/N) -1 and RATE() formula work even when the value of N is LESS than ONE year - few months or days? In other words, would it work in the example below.
    
    I purchased some shares at $100.00 per share on 7-JAN-2015. I sold them off at $120.00 per share on 3rd of 4-FEB-2015. What is the Annualized return I received?
    
    Thanks in advance.
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-911128)
    
19.  ![](https://secure.gravatar.com/avatar/197de4f8b39392dbe6a4abe8f8e7698f719407c0b6228fc1ec0c6352cf27f567?s=64&d=mm&r=g) Prashant says:
    
    [February 14, 2015 at 6:37 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-913125)
    
    Very Nice explanation ..do liked it.  
    I was confused on one of the explanation given in other website but chandu is very nice to explain
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-913125)
    
20.  ![](https://secure.gravatar.com/avatar/0af9ed3d6f6db2b150ee1089c30f496a3e7e268c41042efd51c92110667eae2a?s=64&d=mm&r=g) [Rama](http://www.stockcalculation.com/)
     says:
    
    [June 11, 2015 at 1:27 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-991084)
    
    You can easily calculate CAGR value using this web calculator.
    
    [http://www.stockcalculation.com/2015/06/compound-growth-rate-calculator.html](http://www.stockcalculation.com/2015/06/compound-growth-rate-calculator.html)
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-991084)
    
21.  ![](https://secure.gravatar.com/avatar/ed58a04f5211a108bdd9cc47238ae456f02feeae09efe1c39bc1f5a40171b29d?s=64&d=mm&r=g) vijay says:
    
    [September 7, 2015 at 2:53 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-1039579)
    
    Calculated LOGEST on the below 2 different sets of data (difference being value for the 3rd year is 10 vs 800), however result is exactly same....hence this seems to be limitation of LOGEST.
    
    120 120  
    150 150  
    10 800  
    200 200  
    240 240  
    18% 18%
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-1039579)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [September 8, 2015 at 12:47 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-1040298)
        
        @Vijay
        
        Logest can be used as a function or as an array function  
        Using it as a function returns the Slope of a line of best fit or m value  
        In this case the 2 slopes are the same at 0.18 or 18%  
        One line has a larger Y Intercept than the other due to the 800 value
        
        If instead you use Logest as an array function  
        Select a 2 Column x 5 row area  
        Enter =LOGEST(C2:C6,A2:A6,TRUE,TRUE) Ctrl+Shift+Enter  
        Then repeat for the other data set
        
        Use the Excel help to lookup the Linest function where the array of results is discussed
        
        You can also read about these parameters here:  
        [http://chandoo.org/wp/2011/01/26/trendlines-and-forecasting-in-excel-part-2/](http://chandoo.org/wp/2011/01/26/trendlines-and-forecasting-in-excel-part-2/)
        
        [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-1040298)
        
22.  ![](https://secure.gravatar.com/avatar/95540291a3ac55d70e03513b43df5a4ca76ef827b15321520021809dc59da416?s=64&d=mm&r=g) [Thomas Ling](http://txsling.com/)
     says:
    
    [January 19, 2016 at 3:07 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-1122808)
    
    The RATE formula is calculated by iteration and does not always converge on the correct CAGR value when the inputs take unusually large or very small values. For example, in Excel 2007, RATE returns a #NUM error when asked to calculate the CAGR over 10 periods with P = 10 and A >707 (the correct CAGR is >53.08%). Conversely, RATE returns a CAGR of -99.999... % when asked to calculate the CAGR over 10 periods with P = 10 and A = 0 (the correct CAGR is -100%). So, the simple arithmetic and POWER approaches are more robust.
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-1122808)
    
23.  ![](https://secure.gravatar.com/avatar/15020565f7063e658087e67901e0e91e380070709b04f9dd7abba39236d5d090?s=64&d=mm&r=g) Allen J says:
    
    [January 21, 2016 at 7:50 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-1123561)
    
    I have a question.... how do you calculate the rate of how fast sales have to go to keep the same market share
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-1123561)
    
24.  ![](https://secure.gravatar.com/avatar/09a147a72ebae365c1d3d541afd178c0bbb16380c3cb07bebf0eb5d8807f8432?s=64&d=mm&r=g) [Duncan Williamson](http://excelmaster.co/)
     says:
    
    [September 13, 2016 at 11:02 am](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-1284570)
    
    I support Luis suggestion of using =RRI () since it was made for this!
    
    Secondly, some comments here reflect the situation in which we are dealing with exponential growth or logarithmic growth or some other non linear growth function. In such cases we need to use a CAGR calculation to reflect that.
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-1284570)
    
25.  ![](https://secure.gravatar.com/avatar/ac1c25fb59917537a1109f556b8278d032495994e8aa6fff6ab22121df4f822c?s=64&d=mm&r=g) Aaron Raub says:
    
    [November 10, 2016 at 11:46 pm](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-1336434)
    
    I was wondering what the procedure would be to handle negative numbers in calculating CAGR.
    
    [Reply](https://chandoo.org/wp/calculate-cagr-using-excel/#comment-1336434)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/calculate-cagr-using-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [How to become an MVP in Excel \[case study\]](https://chandoo.org/wp/how-to-become-an-mvp-in-excel-case-study/) | [CP007: aweSUM() – Overview of SUM functions in Excel](https://chandoo.org/wp/cp007-awesum-overview-of-sum-functions-in-excel/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)