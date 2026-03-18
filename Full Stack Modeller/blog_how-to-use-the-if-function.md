# The IF Function

**Source:** https://www.fullstackmodeller.com/blog/how-to-use-the-if-function

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20IF%20Function.png)

How to use Excel's IF Function
==============================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

May 21, 2021 10:47:00 AM

_Returns one value for a TRUE result, and another for a FALSE result_

#### What does Excel's IF function do?

The IF function is one of Excel's logical functions.

The IF function performs a logical test (that is to say - is something true or false) and then returns the value you have provided if the result is TRUE or the value you have provided if the result is FALSE.

The IF function is one of the most popular functions in Excel.

In financial modelling it is often used to model business logic based on 1, 0 flags.

#### Here's a simple example

Let's take a look at a simple example of the IF function.

We would like to check is the value in A1 is the value one. If its is 1 then we would like to return "Yes", if it isn't then we would like to return "No".

#### \=IF(A1 = 1, "Yes", "No")

![Screenshot (624)](https://www.fullstackmodeller.com/hs-fs/hubfs/Screenshot%20(624).png?width=1200&name=Screenshot%20(624).png)

#### What does that mean in plain English?

The best way to understand the IF function is to replace the first comma with the word “then” and the second comma with the word “Otherwise”:

If the value in cell A1 is equal to 1, then return “Yes”, otherwise return “No”.

#### How do I write a formula using the IF function?

#### \=IF(logical test, value if true, value if false)

Logical test – A question resulting in the answer TRUE or FALSE

Value if true – What to return if the answer to the logical test is TRUE

Value if false – What to return if the answer to the logical test is FALSE

#### What to consider when using the IF function in your financial model

*   Excel will allow you to nest up to 64 different IF functions. I strongly recommend avoiding nesting IFs wherever possible as formulae with nested IF functions can become incredibly difficult to understand, audit and maintain. 
*   Instead I recommend that you separate your formula logic onto multiple rows and use the IF function to create 1 or 0 flags.
*   [XLOOKUP](https://www.fullstackmodeller.com/blog/how-to-use-the-xlookup-function)
     or INDEX MATCH can often provide a clearer and simpler solution to challenges often solved by nested IFs.
*   The SWITCH function (2016) provides a simpler alternative to nested IFs.
*   The IFS function (2019) was developed to avoid the need for nested IFs.

Read more about the IF function on the Microsoft support page [here](https://support.microsoft.com/en-us/office/if-function-69aed7c9-4e8a-4755-a9bc-aa8bbff73be2)
.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-if-function)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-if-function)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fhow-to-use-the-if-function)
    

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