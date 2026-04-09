# The SWITCH Function

**Source:** https://www.fullstackmodeller.com/blog/the-switch-function

---

[Back to Blog](https://www.fullstackmodeller.com/blog)

![Blog post image](https://www.fullstackmodeller.com/hubfs/How%20to%20use%20Excels%20SWITCH%20Function.png)

How to use Excel's SWITCH Function
==================================

Published [by Myles Arnott](https://www.fullstackmodeller.com/blog/author/myles-arnott)

Sep 27, 2022 11:17:53 AM

_Compares values against a given expression and returns the corresponding result value_

What does Excel's SWITCH function do?
-------------------------------------

The SWITCH function is one of Excel's logical functions.

The SWITCH function evaluates an expression against a given value and returns the corresponding result value that you have provided.

The SWITCH function is an alternative to the [IF](https://www.fullstackmodeller.com/blog/how-to-use-the-if-function)
 and [IFS](https://www.fullstackmodeller.com/blog/the-ifs-function)
 functions.

An important difference between these functions is that SWITCH can only perform exact matching (ie "is equal to") it cannot perform greater than or lower than checks.

### Here's a simple example

Let's take a look at a simple example of the SWITCH function.

We have the following business logic:

*   If the value is =100 then return high
*   If the value is =50 then return medium
*   If the value is =10 then return low
*   If the value is =5 then return extra low
*   If the value is not one of the above then return "not found"

![SWITCH](https://www.fullstackmodeller.com/hs-fs/hubfs/SWITCH.gif?width=2268&name=SWITCH.gif)

Using a nested IF statement this would be structured as follows:

\=IF(A1=100,"high",IF(A1=50,"medium",IF(A1=10,"low",IF(A1=5,"extra low","not found"))))

Using the IFS function this becomes:

\=IFS(A1=100,"high",A1=50,"medium",A1=10,"low",A1=5,"extra low",TRUE,"not found")

Using the SWITCH function this becomes:

\=SWITCH(A1,100,"high",50,"medium",10,"low",5,"extra low","not found")

Notice the difference between how the three functions are structured.

#### What does that mean in plain English?

If the value in cell A1 is equal to 100, then return “High”, otherwise if it is equal to 50, then return “medium”, otherwise if it is equal to 10, then return “low” otherwise if it is equal to 5, then return “ extra low” otherwise return "not found".

  

#### How do I write a formula using the SWITCH function?

#### **\=SWITCH(Expression, Value 1, Result 1, \[Value 2\], \[Result 2\]...)  
**

The logical tests are in pairs: The value and corresponding result:

Expression - This is the value to match against

Value 1 – The first value to check against

Result 1 – What to return if the expression matches value 1

\[Value 2\] – The second value to check agains

\[Result 2\] – What to return if the expression matches value 2

...etc...

\[Default\] - Optional value to return if the expression does not match any of the given values

#### What to consider when using the SWITCH function in your financial model

*   The SWITCH function allows you to test up to 126 pairs of conditions.
*   The SWITCH function was introduced in 2019, so be aware of compatibility issues for users of previous Excel versions.
*   [XLOOKUP](https://www.fullstackmodeller.com/blog/how-to-use-the-xlookup-function)
    , VLOOKUP or [INDEX](https://www.fullstackmodeller.com/blog/how-to-use-the-index-function)
     MATCH can often provide a clearer and simpler solution than the SWITCH function.

Read more about the SWITCH function on the Microsoft support page [here](https://support.microsoft.com/en-us/office/switch-function-47ab33c0-28ce-4530-8a45-d532ec4aa25e)
.

*    [![facebook](https://www.fullstackmodeller.com/hubfs/facebook.svg) Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fthe-switch-function)
    
*    [![twitter](https://www.fullstackmodeller.com/hubfs/twitter.svg) Share on Twitter](https://twitter.com/intent/tweet?text=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fthe-switch-function)
    
*    [![linkedin](https://www.fullstackmodeller.com/hubfs/linkedin.svg) Share on Linkedin](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.fullstackmodeller.com%2Fblog%2Fthe-switch-function)
    

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