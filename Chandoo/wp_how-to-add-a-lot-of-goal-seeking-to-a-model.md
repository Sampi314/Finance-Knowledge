# How to add a lot of Goal Seeking to an Excel model

**Source:** https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model

---

How to add a lot of Goal Seeking to a model
===========================================

[Huis](https://chandoo.org/wp/category/huis/)
 , [Posts by Hui](https://chandoo.org/wp/category/huis-posts/)
 , [simulation](https://chandoo.org/wp/category/simulation/)
 - 11 comments

  

Recently in the [Chandoo.org Forums](http://forum.chandoo.org/threads/how-to-create-sensitivity-data-table-based-off-input-created-from-goal-seek-value.34905/)
, **MR06** asked the question, “_I am trying to create a sensitivity table that tells me what amount of equity I need to include in a deal in order to get a fixed IRR as the year 3 sales price changes._”

MR06 was using Goal Seek to change the equity input so that the IRR achieved 25% value. But he wanted to do that for a number of Year 3 price changes in the model.

He could obviously change the Year 3 value manually, then run a Goal Seek and write down the Solution and repeat for the range of Year 3 prices changes.

Or he could have setup a macro to do the same and tabulate the results.

Eventually I provided a solution which uses a Data Table and some formulas to determine these values

This post will examine the technique used to solve the problem for MR06

The Problem
-----------

This is MR06’s model. It is a simple financial model of an investment in some units over a 6 1/2 year period.

[![SR01](https://chandoo.org/wp/wp-content/uploads/2017/07/SR01.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR01.png)

The problem is that MR06 wants to know what Equity value **B10** is required to achieve an Internal Rate of Return (IRR) of 25% subject to varying the Year 3 Price, cell **G6**.

Goal Seek
---------

This problem can be solved using Goal Seek  
Goto the **Data, What-If-Analysis, Goal Seek** Tab

[![SR02](https://chandoo.org/wp/wp-content/uploads/2017/07/SR02.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR02.png)

Set the dialogs in the Goal Seek to the values shown above and press Ok

[![SR03](https://chandoo.org/wp/wp-content/uploads/2017/07/SR03.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR03.png)

Excel sets the value in cell B12 to the value of $441,910 and shows an IRR of 25.1%. This small discrepancy will be discussed later.

MR06 can now manually repeat that changing the values of G6 between each iteration. Except that MR06 has many many models and wants to do that for variations in the Year 3 Price from $8 to $15.

Data Tables
-----------

An alternative method to solve this is to use a Data Table to feed in the starting values for both the Year 3 Price **G6**, as well as a list of Values for the Equity Contribution **B12.**

The Data Table will then retrieve a list of the IRR’s for the various combinations.

Then we can then setup a formula to calculate the Equity contribution required to achieve the target IRR value of 25%

You can follow along with a copy of the worked example: [Download Example File Here](https://chandoo.org/wp/wp-content/uploads/2017/07/MR06-Example.xlsx)

### Firstly setup a Data Table

Setup a list of required Prices for Year 3 in a Row D15:K15 and a list of possible Equities in a Column C16:C25

[![SR04](https://chandoo.org/wp/wp-content/uploads/2017/07/SR04.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR04.png)

I have colored the cells to simplify which cells are linked to which parts of the Data Table.

In the Top Left cell C15 link that to the Target IRR cell using \=B12

[![SR05](https://chandoo.org/wp/wp-content/uploads/2017/07/SR05.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR05.png)

Now select the whole area **C15:K25** and goto the **Data, What-If-Analysis, Data Table** Tab

Complete the Data Table dialog  
Row Input cell:  $G$6  
Row Input cell:  $B$10

[![SR06](https://chandoo.org/wp/wp-content/uploads/2017/07/SR06.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR06.png)

Press **Ok**

Excel will now fill in the Data Table area with the IRR’s from the combination of Each Row (Equity) and Column (Year 3 Price)

[![SR07](https://chandoo.org/wp/wp-content/uploads/2017/07/SR07.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR07.png)

At this point we now have a table of IRR’s from the combination of Each Row (Equity) and Column (Year 3 Price), but we can see that we don’t have an actual solution, only approximate solutions for each Year 3 Price.

Our goal was to find the Equity value which returned a 25% IRR

We can use the Excel **Forecast()** function to interpolate the exact answers based on the data in the Data Table

Forecast allows us to forecast a Y value based on an X value from a Table of Known X and Y values  
You can read the excel help about forecast

[![SR08](https://chandoo.org/wp/wp-content/uploads/2017/07/SR08.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR08.png)

We can see from the help that Forecast uses the syntax:  
\=FORECAST(x, known\_y’s, known\_x’s)  
In our example we are seeking a known value of the IRR of 25%  
We have a List of Known X’s which is the IRR’s in the Data Table and the list of known Y’s is the corresponding list of Equities in Column C

To test this in cell **D27** type the following: =FORECAST(25%,$C16:$C25,D16:D25) and press **Enter**  
Excel will return **$444,481.25**

**[![SR09](https://chandoo.org/wp/wp-content/uploads/2017/07/SR09.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR09.png)
**

This is the equity required to return 25% IRR based on a Year 3 Price of $8.00

You can copy Cell D27 across and you will now have a Table of all the equities required for all Year 3 Prices.

[![SR10a](https://chandoo.org/wp/wp-content/uploads/2017/07/SR10a.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR10a.png)

A neater solution is to also allow the IRR to be set as a variable. This way it can be changed and the new equities automatically shown for each Year 3 Price change  
In Cell **D29** type 25%  
Then setup a Row of Year 3 Prices in cell **D31** type: \=D15  
Copy D31 across to K1  
Then in **D32** type: \=FORECAST($D$29,$C16:$C25,D16:D25)  
Copy it across to K32

You now have a table of Year 3 Prices and the required Equities to achieve a 25% IRR

[![SR10](https://chandoo.org/wp/wp-content/uploads/2017/07/SR10.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR10.png)

You can simply change the Required IRR in Cell **D29** eg 20%  
And you will have a Table of the required Equities to achieve a 20% IRR

[![SR11](https://chandoo.org/wp/wp-content/uploads/2017/07/SR11.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR11.png)

The good thing about having this as a separate table is that it can easily be graphed  
Select the Table and got the **Insert, Chart** Tab  
Select an appropriate chart type

[![SR12](https://chandoo.org/wp/wp-content/uploads/2017/07/SR12.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR12.png)

### One warning

In this example the model appears to be very linear, this means there is a direct or straight line relationship between the Equity and the IRR for a given Year 3 Price

If we choose a value of equity of say 30% we can see that we need an equity of $725,020 for a Year 3 Price of 8.00

[![SR13](https://chandoo.org/wp/wp-content/uploads/2017/07/SR13.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR13.png)

It is important to note that the value of $725,020 is outside the range of the Equity values we set in Column C

In this case we should check that this is still a valid Forecast

To do this reset the Equity values in Column C to that shown below, ensuring that the equity values extend both below and above the expected equity value we saw of $725,020

[![SR14](https://chandoo.org/wp/wp-content/uploads/2017/07/SR14.png)](https://chandoo.org/wp/wp-content/uploads/2017/07/SR14.png)

We can now see that the Equity value required is $649,577.

### Warning:

Those who are observant will notice that the Equity value of 649,577 should have an IRR of slightly less than 29.61%, not 30%

This is because although the model appears linear, it is in fact not exactly linear.

The model’s non-linearity occurs for a number of reasons but primarily is that XIRR is not an exact function. It is an Iterative Function and to quote from Microsoft Help “_Excel uses an iterative technique for calculating XIRR. Using a changing rate (starting with guess), XIRR cycles through the calculation until the result is accurate within 0.000001 percent._”

For all intention purposes it is close enough to linear that we don’t notice the differences.

If it was perfectly linear the extrapolation to 30% which was outside the original Equity range would have given us the same result of $649,577 not the $725,020 that it returned. Non-linearity is magnified once the extrapolation used in the Forecast Function is outside the range of the known Y values and we need to always check for this.

This non-linearity causes small discrepancies in the Excel functions like IRR and Forecast, of which we are using both.

Forecast uses a least squares approximation to best estimate a line of best fit, but it is just that, an approximation.

If you are wondering how close the model is to being linear, it is 99.77% fit to being linear

This is calculated using the r value or Pearson() function  
D50: \=PEARSON(C16:C25,D16:D25)  
\=0.997747518  
That is the closer the value is to 1 the more linear it is.

### Excel 2016+

In Excel versions 2016+ Microsoft has added a new set of functions including: FORECAST.LINEAR()

Forecast.Linear and the other new Statistical Functions “_use advanced machine learning algorithms, such as Exponential Triple Smoothing (ETS)_”

You can read all about them here: [Advanced Forecast Functions in Excel 2016+](https://support.office.com/en-us/article/Forecasting-functions-reference-897a2fe9-6595-4680-a0b0-93e0308d5f6e?ui=en-US&rs=en-US&ad=US#_forecast.linear)

It is recommended that they are used in model from using Excel 2016 onwards.

Closing
-------

I hope you have enjoyed this discussion on the use of Data Tables and the Forecast() Function to replicate multiple Goal Seek commands.

For more information on Data Tables I refer you to my post: [Data Tables & Monte Carlo Simulations in Excel – A Comprehensive Guide](http://chandoo.org/wp/2010/05/06/data-tables-monte-carlo-simulations-in-excel-a-comprehensive-guide/)

Many thanx to MR02 for permission to use his model for this post.

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
| Written by Hui...  <br>Tags: [Forecast](https://chandoo.org/wp/tag/forecast/)<br>, [Pearson()](https://chandoo.org/wp/tag/pearson/)<br>, [xirr()](https://chandoo.org/wp/tag/xirr/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 11 Responses to “How to add a lot of Goal Seeking to a model”

1.  ![](https://secure.gravatar.com/avatar/dc9b9238fe8eb9e31ee6f50f6633b000b8d7b2a96f8dd1e9b57bcb8a9dfa0f01?s=64&d=mm&r=g) Rocky\_Rocks says:
    
    [July 4, 2017 at 5:49 pm](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1476233)
    
    Thanks for this, though the data table with goal seeked values could be achieved easily through a simple macro using loops without having the problem of linearity.
    
    [Reply](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1476233)
    
2.  ![](https://secure.gravatar.com/avatar/04b5a93edbc655803abe74ca9048a5e604383b69481c0cb5e200048e7b6d86e4?s=64&d=mm&r=g) prashant says:
    
    [July 5, 2017 at 5:41 am](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1476419)
    
    Informative & helpful
    
    [Reply](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1476419)
    
3.  ![](https://secure.gravatar.com/avatar/2aea458c9376b6c645cdf0d2bac30ec4360fb4c91b12afe96f9149be2dc4c3ff?s=64&d=mm&r=g) Chrojas says:
    
    [July 5, 2017 at 6:53 pm](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1476572)
    
    This was such a good setup of a problem with a terrible solution.
    
    Several key points:  
    1\. The math is such that an IRR calculation is done iteratively. That's why you're allowed to submit a guess. The format of the IRR function is: IRR(values, \[guess\]) . I'm not aware of any other functions which take a guess, except...  
    2\. XIRR - should always and everywhere be used. Never, ever, ever use the IRR function. It's a receipe for disaster. Your spreadsheet shows this but the point should be explicit.  
    3\. If you're calculating an IRR or an XIRR, it's because you're making an investment decision. And more likely than not, if you're a spreadsheeter and you're calculating an IRR or XIRR, you're calculating a return on somebody else's money. So do yourself a favor and take the time to do it properly. Actually calculate it. Don't take shortcurts.
    
    What this means is USE THE XIRR FUNCTION.
    
    4\. Don't assume that things are linear. They might not be. Don't calculate a few points and then use FORECAST to fill in the rest. That's a sure fire way to get yourself fired or lose money. If an analyst handed me a spreadsheet that used FORECAST in it for an IRR I would tell them to take the time to redo the analysis properly, or find a new job.
    
    5\. The right way to calculate a bunch of IRRs is to automate things with a macro. A simple goal seek has three variables. You can simplify it down to two by always backsolving to zero with one line of VBA and a couple of range names.
    
    Range("target").GoalSeek Goal:=0, ChangingCell:=Range("change")
    
    Wrapping this into a loop to fill out a sensitivity table is not too hard, and it would be worthy of a followup post.
    
    [Reply](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1476572)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [July 6, 2017 at 6:21 am](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1476688)
        
        @Chrojas  
        Thank you for your feedback
        
        The post was written as an example of using Data Tables and Forecast to perform multiple Goal Seek functions within a model.
        
        Nowhere in the post do I say use either IRR() or XIRR().  
        Each can be used to give an Internal Rate of Return within the limitations of the function and the suiability & limitations of your model.
        
        The model specifically identifies that it uses XIRR and uses XIRR in the calculations.
        
        The errors are not introduced by the Forecast function but come from the errors in the XIRR function.
        
        Using XIRR with a poor guess can give widely differing and yet all correct answers for nonlinear problems.  
        Refer how XIRR can return 3 results: [https://freefincal.com/irr-xirr-excel-limitations-calculate-returns/](https://freefincal.com/irr-xirr-excel-limitations-calculate-returns/)
        
        The use of Goal-Seek is also an approximation tool and does return the correct answer, as highlighted in the post it returns 25.1%IRR, Third image above, so using that in a loop in a macro won't fix that issue. In fact there is a better case for writing a follow up warning post on the use of Goal Seek with XIRR as the two iterative functions together probably shouldn't be practised.
        
        Using approximation tools such as Forecast() is an acceptable method of finding IRR's: [http://www.corality.com/tutorials/calculate-irr-excel](http://www.corality.com/tutorials/calculate-irr-excel)
        
        [Reply](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1476688)
        
    *   ![](https://secure.gravatar.com/avatar/33eed53a4b49a2f8df0d9527c539d76ed4b04376f78ed336afccf183d5eef8ce?s=64&d=mm&r=g) MR06 says:
        
        [July 11, 2017 at 9:58 pm](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1478776)
        
        Hi Chrojas,
        
        With regards to my specific issue, which requires 2 steps (1: set the year 3 price, 2: goal seek the equity to achieve 25% IRR), how would you set up that macro? The end goal is to create rows 31 and 32 in Hui's example, but in a quick, repeatable way such that I can copy/paste with minimal adjustments to solve this question for hundreds of different investments.
        
        The real models used are significantly more complex than this, although they do have simple inputs for price and equity.
        
        Thanks!
        
        MR06
        
        [Reply](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1478776)
        
    *   ![](https://secure.gravatar.com/avatar/4f5ad54bd7fd474d475b95926b122fa490251cc3bc2f60396c893de366ca6797?s=64&d=mm&r=g) Stan Bown says:
        
        [July 24, 2017 at 4:04 pm](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1484315)
        
        Have you got a macro solution you can share?
        
        [Reply](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1484315)
        
4.  ![](https://secure.gravatar.com/avatar/bdc9f435d3b9dddbd07882ddca5a6cf2e574c23ffb89efc2bcc39593512a883b?s=64&d=mm&r=g) [John MacDougall](http://www.howtoexcel.org/)
     says:
    
    [July 7, 2017 at 12:04 pm](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1477276)
    
    Just a note about why the IRR calculation involves an iteration rather than an exact solution. IRR essentially is finding the roots of a polynomial equation. There are closed form algebraic solutions when the highest power in the polynomial is 4 or less but no closed form solutions exist when the highest power is 5 or more.
    
    You probably remember the closed form solution for a polynomial of power 2:
    
    (-b+-root(b^2-4ac))/2a
    
    The solution for 3 and 4 get pretty ugly and there are no general solutions for 5 and over (although there are solutions for special cases).
    
    [Reply](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1477276)
    
5.  ![](https://secure.gravatar.com/avatar/66cee84e516f6f525bfa83191783a890df87a573a28e0fe4ce24d39b7416e29f?s=64&d=mm&r=g) Bob says:
    
    [July 10, 2017 at 4:03 pm](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1478293)
    
    Many thanks Hui!
    
    Despite Chrojas' moaning I found this very useful
    
    [Reply](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1478293)
    
6.  ![](https://secure.gravatar.com/avatar/4d92002b77cac0d3903323e51265d2d46c4315096d30b6b803b7adb76295df3b?s=64&d=mm&r=g) Hassan says:
    
    [July 11, 2017 at 10:56 am](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1478536)
    
    This article is very helping and well written. I am learning alot from this website.
    
    [Reply](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1478536)
    
7.  ![](https://secure.gravatar.com/avatar/4f5ad54bd7fd474d475b95926b122fa490251cc3bc2f60396c893de366ca6797?s=64&d=mm&r=g) Stan Bown says:
    
    [July 24, 2017 at 3:54 pm](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1484312)
    
    Very useful, all round. Thanks to question, answer and commentators.
    
    [Reply](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1484312)
    
8.  ![](https://secure.gravatar.com/avatar/efc35befeb4717e5954ae41000dcd7caffc50c78c9a440aa6c9507b0b5fad2af?s=64&d=mm&r=g) Khirai says:
    
    [August 24, 2020 at 9:49 pm](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1861950)
    
    Can anyone help me regarding goal seek vba for a data range of which onlylternative rows only to be done. Like in some case only the even row or the odd row number only. Thanks in advance.
    
    [Reply](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#comment-1861950)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/how-to-add-a-lot-of-goal-seeking-to-a-model/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Rounding time to nearest minute or quarter hour etc. \[formulas\]](https://chandoo.org/wp/rounding-time-in-excel/) | [Joyplot in Excel](https://chandoo.org/wp/joyplot-in-excel/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)