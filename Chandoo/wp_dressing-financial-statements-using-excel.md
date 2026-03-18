# Dressing Financial Statements - What Motivated Mr. Bean to Defraud Latte? » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/dressing-financial-statements-using-excel

---

Dressing Financial Statements – What Motivated Mr. Bean to Defraud Latte?
=========================================================================

[Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
 - 2 comments

  

_This is a guest article by **Paramdeep**, a financial modeling expert & teacher._

Did you know What Happened at Last Coffee Day?
----------------------------------------------

Mr. Bean “dressed up” the financial statements and was caught in the fraud. But he was the CEO of Latte! So why did he commit fraud in his own company??

Any Guess?

Take a cappuccino and I will give you a hint – How was Mr. Bean’s Bonus to be decided?

Now?

Hmm…, His Bonus was dependent on the Share Price and he had all the motivation in the world to increase it.

But How come Fraud?

There is nothing bad in motivating people to perform and as CEO of Latte, Mr. Bean had to make Shareholders happy and he is simply working towards his goal. But then what can possibly be wrong in that?

Still… clueless 🙁

If you give wrong information to the target audience and mislead them to believe that you are performing better than you actually are, is a fraud.

But the financial statements (Income statements, Balance sheet and Cash Flow statements) are pure numbers, how can one possibly “window dress” them?

Yes, they are numbers – But surprisingly “interpreted” (jargon: Recognized) numbers. And people can interpret them to project better than actual numbers!Which is a fraud.

Implementation of Incentives – Stock Options
--------------------------------------------

Typically top executive’s income is linked to the performance using stock options. Stock Option – as the name implies gives the executive an option to buy the shares of the company at some price X (Called as an Exercise price), typically at a pre-agreed discount to the market price. As the share price increases, they can sell these shares in the market and their take-home amount increases accordingly.

The good part about the options is that it is an Option. If the share price is below the exercise price, you need not exercise it and hence avoid the loss that you would have to bear because of non-performance.

In a nut-shell, it has all the upside and no downside. The employees are incentivized to perform in such a way that it boosts the company’s stock price.

The Pricing Mechanism P/E Ratio
-------------------------------

Analysts say that the prices of shares are dependent upon the performance, which is captured in the Profit (PAT) of the company. This is again captured in a ratio called the PE (Price to Earnings Ratio). Latte has been trading at a PE of 10. Based on estimates, the earnings are projected to be:

[![image](https://chandoo.org/wp/wp-content/uploads/2012/12/image_thumb.png "image")](https://chandoo.org/wp/wp-content/uploads/2012/12/image.png)

Based on this the share Price (Price = EPS x PE) is projected to be:

[![image](https://chandoo.org/wp/wp-content/uploads/2012/12/image_thumb1.png "image")](https://chandoo.org/wp/wp-content/uploads/2012/12/image1.png)

What would Mr. Bean Take Home?
------------------------------

Mr. Bean has a fixed take-home salary of USD 1 Mn. Latte has also granted 50,000 stock options to him at an exercise price of USD 40. So, if the prices stay at 40, Mr. Bean’s payoff from the stocks would remain zero. The good part is that even if they are below 40, the payoff is still zero.

The bad part about this is that if Mr. Bean thinks that the price is going to be below 40 (even slightly), he has all the incentives in the world to make it look like its above 40, so that he can gain from the stocks. His fixed is any ways fixed at USD 1 Mn.

Modeling Options Payoff in Excel
--------------------------------

Excel can do interesting stuff. You can use either the “if or the Max” functions Excel to get the options payoffs.

[![image](https://chandoo.org/wp/wp-content/uploads/2012/12/image_thumb2.png "image")](https://chandoo.org/wp/wp-content/uploads/2012/12/image2.png)

Payoff from options= Share price – Exercise price of stock option

Mr. Bean would execute an option only when Share price> Exercise Price of stock option.

Using Max Function for Options Modeling
---------------------------------------

To accommodate this feature of an Option in excel, we can use Max function.

_Max Function Syntax_: `Max(Number1, Number2...NumberN)`

\[[More on MAX Formula](http://chandoo.org/excel-formulas/max.shtml)\
\]

Options Payoff= Max (((Share Price- Exercise Price of Option)\* Number of Stock Options/10^6), 0)

This implies that, options payoff can never be negative.

Using If Function for Options Modeling
--------------------------------------

We can reach to same results using If Statement.

_If Statement Syntax_: `If(Logical Test, Value if True, Value if False)`

\[[More on IF Formula](http://chandoo.org/excel-formulas/if.shtml)\
\]

Options Payoff = If (Share Price>Exercise Price of Stock Option), ((Share Price- Exercise Price of Option)\* Number of Stock Options/10^6), 0)

How’s this Fraud Possible?
--------------------------

An obvious question in this case, would be – If this fraud is that simple? And if it is that easy to fudge, then why is everybody not doing it.

The answer is – It is definitely not easy (and simple), but it is possible. And people do play games to fudge the financial statements and hence increase their take-home amount. What can possibly be used (Some advanced accounting jugglery)

*   Capitalizing costs
*   Revenue Inflation
*   Manipulation of Depreciation Provisions
*   Manipulating lease agreements, etc.

Stay tuned and we would delve deeper into one of these.

Way forward
-----------

This series gives you a flavor of some basics concepts on finance that are very important for professionals engaged in non-finance activities as well. To learn more about various financial concepts & how to do financial analysis using Excel, consider joining our **Finance for non-finance people** course.

[Click here to know more about Finance for Non-finance People course](http://chandoo.org/wp/resources/finance-for-non-finance-people/ "Finance for Non Finance People")
.

Templates to download
---------------------

I have created a template for you, where the subheadings are given and you have to link the model to get the cash numbers! You can download the same [from here](https://chandoo.org/wp/wp-content/uploads/2012/12/Options-Payoff-to-Mr.Bean-Unfilled.xlsx)
**.** You can go through the case and fill in the yellow boxes. I also recommend that you try to create this structure on your own (so that you get a hang of what information is to be recorded).

Also you can download this filled template and check, if the information you recorded, [matches mine or not](https://chandoo.org/wp/wp-content/uploads/2012/12/Options-Payoff-to-Mr.Bean-Filled.xlsx)
! 🙂

For any queries regarding the cash impact or financial modeling, feel free to put the comments in the blog or write an email to [paramdeep@edupristine.com](mailto:paramdeep@edupristine.com)

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
| Written by paramdeep@gmail.com  <br>Tags: [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [finance](https://chandoo.org/wp/tag/finance/)<br>, [financial ratios](https://chandoo.org/wp/tag/financial-ratios/)<br>, [guest posts](https://chandoo.org/wp/tag/guest-posts/)<br>, [if() excel formula](https://chandoo.org/wp/tag/if-excel-formula/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [max()](https://chandoo.org/wp/tag/max/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 2 Responses to “Dressing Financial Statements – What Motivated Mr. Bean to Defraud Latte?”

1.  ![](https://secure.gravatar.com/avatar/024dde822e78b6bff17a52658a9029aaec6af087294dd5801f9af24d228b97dc?s=64&d=mm&r=g) Andrew says:
    
    [December 11, 2012 at 4:25 pm](https://chandoo.org/wp/dressing-financial-statements-using-excel/#comment-341860)
    
    Reminds me of my college days. Anyone in business should learn this knowledge even if as a reminder.  
       
     
    
    [Reply](https://chandoo.org/wp/dressing-financial-statements-using-excel/#comment-341860)
    
2.  ![](https://secure.gravatar.com/avatar/64f3ca9031d8d6d04048ec2f41499646f58129752d4e1e3646103e8684042a97?s=64&d=mm&r=g) zur says:
    
    [December 12, 2012 at 7:50 am](https://chandoo.org/wp/dressing-financial-statements-using-excel/#comment-342754)
    
    SOMETIME THESE OLD TRICKS REFRESHES
    
    [Reply](https://chandoo.org/wp/dressing-financial-statements-using-excel/#comment-342754)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/dressing-financial-statements-using-excel/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [How the tax burden has changed over the years – Excellent chart by NYTimes & Redoing it in Excel](https://chandoo.org/wp/tax-burden-chart-excel/) | [Highlight best week & month in a trend chart \[tutorials\]](https://chandoo.org/wp/highlight-best-week-month-in-charts/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)