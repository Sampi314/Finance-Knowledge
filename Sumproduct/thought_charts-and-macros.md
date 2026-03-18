# Charts and Macros

**Source:** https://sumproduct.com/thought/charts-and-macros/

---

[Home](https://sumproduct.com/)

\> Charts and Macros

*   March 1, 2019

Charts and Macros
=================

VBA Blogs: Charts and Macros
============================

1 March 2019

_Welcome back to this week’s VBA blog! This month, we’re going to look at the interaction between charts and macros._

You may know that as part of our business, we provide model auditing services to clients, checking spreadsheets for errors. As part of that process, we often take two versions of a file and run software over it to identify changes in inputs and formulae.

However, our software doesn’t work on charts – it only looks through the cells in a workbook. Instead, we had to check the charts manually, which can take a very long time when we’re working with multiple charts.

As with many other manual processes, that prompted us to ask – why can’t we create a macro to do it?

![](https://sumproduct.com/wp-content/uploads/2025/06/e774d10cbbb9450fc45efbe51abdf434-701.jpg)

This month, we’ll look at the thought process around creating a macro that would help us to identify a chart’s details and present the results to a user. The Chart Identifier macro would need to report on the following characteristics of a chart:

*   The sheet that the chart was located on
*   The name of the chart object
*   A list of the different data series that were being reported
*   The formulae of each data series being reported on
*   The axis formula for each item
*   Any X / Y / Z axis formulae that might apply for things like bubble charts

That’s quite a lot! This is why it takes so long to do manually, and why we will use VBA to overcome it. Over the next month, we’ll introduce the different processes that form the tool we actually use in our audits, so that you can benefit from understanding our approach and have a tool that you can use in the end. Hope you join us for the rest of this series!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/charts-and-macros/#0)
    
*   [Register](https://sumproduct.com/thought/charts-and-macros/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/charts-and-macros/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/charts-and-macros/#0)

[](https://sumproduct.com/thought/charts-and-macros/#0 "close")

top