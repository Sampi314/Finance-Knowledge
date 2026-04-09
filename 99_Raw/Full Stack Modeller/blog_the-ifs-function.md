# The IFS Function

**Source:** https://www.fullstackmodeller.com/blog/the-ifs-function

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20IFS%20Function.png)

How to use Excel's IFS Function
===============================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Sep 22, 2022 5:01:55 PM

_Returns one value for a TRUE result, and another for a FALSE result for multiple conditions  
_

What does Excel's IFS function do?
----------------------------------

The IFS function is one of Excel's logical functions.

The IFS function performs a series of logical tests (that is to say - is something true or false) and then returns the value you have provided if the result is TRUE or the value you have provided if the result is FALSE.

The IFS function is an upgrade of the IF function, one of the most popular functions in Excel, as it allows financial modellers to test multiple arguments without needing a complicated nested IF formula.

In financial modelling, it is often used to model business logic based on 1, 0 flags.

### Here's a simple example

Let's take a look at a simple example of the IFS function.

We have the following business logic:

*   If the value is >=100 then return high
*   If the value is >=50 then return medium
*   If the value is >=10 then return low
*   If the value is <10 then return extra low

  

Using a nested IF statement this would be structured as follows:

\=IF(A1>=100,"high",IF(A1>=50,"medium",IF(A1>=10,"low","extra low")))

Using the IFS function instead of the IF function this becomes:

\=IFS(A1>=100,"high",A1>=50,"medium",A1>=10,"low",A1<10,"extra low")

![IFS function](https://www.fullstackmodeller.com/hs-fs/hubfs/IFS%20function.gif?width=2250&name=IFS%20function.gif)

#### What does that mean in plain English?

The best way to understand the IFS function is to replace the first comma in the pair with the word “then” and the second comma in the pair with the word “Otherwise”:

If the value in cell A1 is greater than or equal to 100, then return “High”, otherwise if it is greater than or equal to 50, then return “medium”, otherwise if it is greater than or equal to 10, then return “low” otherwise if it is less than 10, then return “ extra low”.

  

#### How do I write a formula using the IFS function?

#### **\=IFS(logical test1, value if true1, logical test2, value if true2, logical test3, value if true3….)**

The logical tests are in pairs: The test and the value if the result is "true":

Logical test1 – A question resulting in the answer TRUE or FALSE

Value if true1 – What to return if the answer to the logical test is TRUE

Logical test2 – A question resulting in the answer TRUE or FALSE

Value if true2 – What to return if the answer to the logical test is TRUE

#### What to consider when using the IFS function in your financial model

*   The IFS function allows you to test up to 127 different conditions, but I highly recommend against going much above 4 or 5 as the tests need to be entered in the correct order and can become very difficult to review.
*   The IFS function was introduced in 2016, so be aware of compatibility issues for users of previous Excel versions.
*   XLOOKUP, VLOOKUP or INDEX MATCH can often provide a clearer and simpler solution to challenges often solved by multiple IF arguments.

Read more about the IFS function on the Microsoft support page [here](https://support.microsoft.com/en-us/office/ifs-function-36329a26-37b2-467c-972b-4a39bd951d45)
.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fthe-ifs-function)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fthe-ifs-function)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fthe-ifs-function)
    

![Award_Winning](https://www.fullstackmodeller.com/hubfs/badge.jpg)

Become a Modelling Pro
----------------------

Join us and we'll unlock your full potential.

Our award-winning training programme, and exclusive global community, will guide you on your way to Excel, Financial Modelling, data visualisation & analytics mastery.

[Join as an Individual](https://www.fullstackmodeller.com/full-stack-membership)
 [Register Your Team](https://www.fullstackmodeller.com/team-training)

Latest Blogs
------------

*   [New Year, New You?](https://www.fullstackmodeller.com/blog/full-stack-modeller-new-year-new-you)
    
*   [New Import Functions](https://www.fullstackmodeller.com/blog/excel-importtext-importcsv)
    
*   [Best Practice Confessions & Terminology Overload](https://www.fullstackmodeller.com/blog/unpivot-episode-40-full-stack-modeller)
    
*   [Excel Meetup Groups](https://www.fullstackmodeller.com/blog/excel-meetup-groups)
    
*   [New Features and Common Data Problems](https://www.fullstackmodeller.com/blog/unpviot-episode-39)
    
*   [More AI Hype and Traps to avoid when modelling](https://www.fullstackmodeller.com/blog/unpviot-episode-38)
    
*   [The Excel World Championship Song](https://www.fullstackmodeller.com/blog/excel-world-championship-song)
    
*   [The Advanced Financial Modeler Certificate from FMI](https://www.fullstackmodeller.com/blog/advanced-financial-modeler)
    
*   [The history of Microsoft Excel](https://www.fullstackmodeller.com/blog/history-of-excel)
    
*   [My main learning from the FMI AFM exam](https://www.fullstackmodeller.com/blog/financial-modeling-institute-fmi-afm-learnings)
    

#### Subscribe to our monthly modelling newsletter