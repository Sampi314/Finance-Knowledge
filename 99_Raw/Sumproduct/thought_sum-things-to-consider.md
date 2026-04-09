# SUM Things to Consider

**Source:** https://sumproduct.com/thought/sum-things-to-consider/

---

[Home](https://sumproduct.com/)

\> SUM Things to Consider

*   May 14, 2025

SUM Things to Consider
======================

Looking at SUM in ways you may not have considered previously.

SUM Things to Consider
======================

_Liam Bastick, director (and Excel MVP) with SumProduct Pty Ltd, highlights some of the common issues and scenarios in financial modelling / Excel spreadsheeting. This article looks at a SUM in ways you may not have considered previously._

Ever heard of **SUM**? I cannot believe it, but it’s taken me this long to cast a beady eye over one of the most commonly-used functions in Excel. No, I’m not taking it easy in this article – **SUM** has some issues you might not be aware of…

**SUM** adds things up. It may include cells, numbers or ranges. In the context of financial modelling, summations are usually of numbers either directly above or to the left of the cell in question:

![](https://sumproduct.com/wp-content/uploads/2025/05/dd4e6ffac626c72483c80403fe69e17a.jpg)

There is a great keyboard shortcut available on most computers. If you select the cell to the right or directly below the values to be aggregated and then use the shortcut **ALT + =** you will see that the range is summed automatically. If you find this doesn’t work for you, make sure you keep the **ALT** button held down on your keyboard.

I use this all of the time in modelling. It’s a fast shortcut, it ensures you don’t miss cells within the range, it requires the range to be contiguous and you can’t leave blank cells. This shortcut actually forces you to build in a manner that will reduce the number of errors you might make. This reinforces one of my on-going crusades:

**A lazy modeller is to be encouraged (it encourages efficiency); lazy modelling isn’t**.

Using **ALT + =** only works if there aren’t blank cells between values. Believe it or not, I think that’s a _good_ thing. Let me explain. Imagine I had created an output which contained blank rows, such as the following Indirect Cash Flow Statement:

![](https://sumproduct.com/wp-content/uploads/2025/05/cf2eaa13a2f4c64f42b06a22f6d9e459.jpg)

Do you see only the highlighted cells in column **J** have been included in the summation formula in cell **J56**?

**\=SUM(J44,J46:J48,J50:J51,J53:J54)**

_  
i.e._ cells **J45**, **J49**, **J52** and **J55** have all been specifically excluded. This is how it should be. If instead I had used the summation formula:

**\=SUM(J44:J55)**

these cells would have been included. Don’t see the problem? The issue is often end users will add percentages or other analysis into blank cells on output sheets. No matter how small these numbers, they will lead to Balance Sheet o other reconciliation errors. If they are not numbers, they can lead to _#VALUE!_ errors or sums being incorrect _(see below)_ instead. In short, try not to aggregate blank cells.

That’s not the only issue with **SUM** though. Consider the following example:

![](<Base64-Image-Removed>)

In this example, I have totalled the values in cells **E3:E7** in two distinct ways: the first uses the aforementioned **SUM** function with **ALT + =**, the other has added each cell individually using the ‘+’ operator. Are you thinking you’d be mad to use the alternative (second) approach – especially if there were many more rows?

Well, take another look:

![](https://sumproduct.com/wp-content/uploads/2025/05/985c3a2a10dfd6ec84fa9c755ccc4790.jpg)

In this example, cell **E5** has been modified. It has been stored as text, even though it looks like the number 3. **SUM** treats this as having zero value whereas the more convoluted addition carries on regardless. Simplest may not always be bestest.

In an example like the one above, this may be easy to spot, but would you stake your life that the sum:

![](<Base64-Image-Removed>)

is correct?

There is a simple way to check using the **COUNT** function. **COUNT** counts the number of **numbers** in a range, so we can use it to spot numbers that aren’t numbers:

![](<Base64-Image-Removed>)

Here, the formula in column **I** highlights when a number is not a number. Note how it reports by exception: if the cell in question contains a number then **COUNT(Cell\_Reference)** equals 1 and **\=1-COUNT(Cell\_Reference)** equals zero. Only non-numbers will be highlighted – it’s better to know I have two errors rather than 14,367 values working correctly.

If you don’t think this applies to you, have you ever worked with PivotTables? This article isn’t about PivotTables, but as an aside, for those of you who have ever worked with this Excel feature, have you ever been frustrated when the following has happened?

![](<Base64-Image-Removed>)

You want your aggregation of values to default to **SUM** but instead they display as **COUNT**. This could be highlighting that some of your data is non-numerical and / or blank. Just a thought.

If you have a query for the _Thought_ section, please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)
 or visit the [SumProduct website](https://www.sumproduct.com/)
.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/sum-things-to-consider/#0)
    
*   [Register](https://sumproduct.com/thought/sum-things-to-consider/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/sum-things-to-consider/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/sum-things-to-consider/#0)

[](https://sumproduct.com/thought/sum-things-to-consider/#0 "close")

top