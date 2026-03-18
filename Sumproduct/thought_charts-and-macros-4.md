# Charts and Macros 4

**Source:** https://sumproduct.com/thought/charts-and-macros-4/

---

[Home](https://sumproduct.com/)

\> Charts and Macros 4

*   March 22, 2019

Charts and Macros 4
===================

VBA Blogs: Charts and Macros 4
==============================

22 March 2019

_Welcome back to this week’s VBA blog! This month, we have been looking at the interaction between charts and macros._

As we mentioned previously, this month we’re going to look at the thought process around creating a macro that would help us to identify a chart’s details and present the results to a user. We effectively need to go through the following steps:

*   Define the target / output file, save target details
*   Determine the series details and loop through to extract them
*   Extract out the relevant name / y-axis / x-axis / bubble size from the formula and clean up

This week, we’re covering the final step in that list.

So far, we’ve extracted out details from the charts in a workbook and dropped them into a new workbook that looks something like this:

![](https://sumproduct.com/wp-content/uploads/2025/06/e774d10cbbb9450fc45efbe51abdf434-703.jpg)

From here, we need to disentangle the formula to work out what the component parts of the data series are. Luckily, there are a few basic rules:

*   The formula always starts off with “=**SERIES**(“
*   The name of the data series will the first parameter (i.e. before the first comma)
*   It’s always followed by the Y-axis, the X-axis, any bubble size or Z-axis (where relevant)
*   It finishes off with a number indicating where in the list of series items it is.

As a result, we can use formulae to work out what each component is. So under the Name column, we can use the following formula to extract the name:

Name: =IFERROR(MID(D7,FIND(“(“,D7)+1,FIND(“,”,D7,FIND(“(“,D7)+1)-FIND(“(“,D7)-1),”n.a.”)

We can then repeat the steps for the axis items as well:

Y-axis: =IFERROR(MID(D7,FIND(“,”,D7,FIND(“(“,D7)+1)+1,FIND(“,”,D7,FIND(“,”,D7,FIND(“(“,D7)+1)+1)-FIND(“,”,D7,FIND(“(“,D7)+1)-1),”n.a.”) 

X-axis: =IFERROR(MID(D7,FIND(“,”,D7,FIND(“,”,D7,FIND(“(“,D7)+1)+1)+1,FIND(“,”,D7,FIND(“,”,D7,FIND(“,”,D7,FIND(“(“,D7)+1)+1)+1)-FIND(“,”,D7,FIND(“,”,D7,FIND(“(“,D7)+1)+1)-1),”n.a.”)

Bubble size: =IFERROR(MID(D7,FIND(“,”,D7,FIND(“,”,D7,FIND(“,”,D7,FIND(“(“,D7)+1)+1)+1)+3,LEN(D7)-FIND(“,”,D7,FIND(“,”,D7,FIND(“,”,D7,FIND(“(“,D7)+1)+1)+1)-3),”n.a.”) 

All of these formulae basically look up the location of the relevant commas and brackets in order to find the start and end points of each of the chart series details. In order to build them into the code, we need something like this:

Range(“NameStart”).Offset(1, 0).Formula = “=IFERROR(MID(D7,FIND(“”(“”,D7)+1,FIND(“”,””,D7,FIND(“”(“”,D7)+1)-FIND(“”(“”,D7)-1),””n.a.””)”

Range(“YAxisStart”).Offset(1, 0).Formula = “=IFERROR(MID(D7,FIND(“”,””,D7,FIND(“”(“”,D7)+1)+1,FIND(“”,””,D7,FIND(“”,””,D7,FIND(“”(“”,D7)+1)+1)-FIND(“”,””,D7,FIND(“”(“”,D7)+1)-1),””n.a.””)”

Range(“XAxisStart”).Offset(1, 0).Formula = “=IFERROR(MID(D7,FIND(“”,””,D7,FIND(“”,””,D7,FIND(“”(“”,D7)+1)+1)+1,FIND(“”,””,D7,FIND(“”,””,D7,FIND(“”,””,D7,FIND(“”(“”,D7)+1)+1)+1)-FIND(“”,””,D7,FIND(“”,””,D7,FIND(“”(“”,D7)+1)+1)-1),””n.a.””)”

Range(“BubbleStart”).Offset(1, 0).Formula = “=IFERROR(MID(D7,FIND(“”,””,D7,FIND(“”,””,D7,FIND(“”,””,D7,FIND(“”(“”,D7)+1)+1)+1)+3,LEN(D7)-FIND(“”,””,D7,FIND(“”,””,D7,FIND(“”,””,D7,FIND(“”(“”,D7)+1)+1)+1)-3),””n.a.””)”

Once the formulae are in place, we can copy these down, then copy and paste-special as values, so that we don’t have the formulae there the whole time – it’s much easier to follow if it’s hard-coded.

![](<Base64-Image-Removed>)

There’s another thing too – if there are no charts in the workbook, the formulae will simply break. In that instance, we might just want a simple message that lets the user know that there are no charts.

![](<Base64-Image-Removed>)

Then, all that is left is a bit of macro clean-up to tidy things up and reset screen updating and calculation statuses.

![](<Base64-Image-Removed>)

And that’s it – that’s our full macro! You can find a sample of the whole thing [here](https://sumproduct.com/assets/blog-pictures/2019/vba/charts-and-macros-4/sumproduct---vba-chart-identifier.xlsm)
 – have a play around and let us know what you think. Next week is the Final Friday Fix, so we’ll be back next month with more VBA tricks. See you then!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/charts-and-macros-4/#0)
    
*   [Register](https://sumproduct.com/thought/charts-and-macros-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/charts-and-macros-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/charts-and-macros-4/#0)

[](https://sumproduct.com/thought/charts-and-macros-4/#0 "close")

top