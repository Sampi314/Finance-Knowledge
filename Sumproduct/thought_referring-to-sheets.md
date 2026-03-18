# Referring to Sheets

**Source:** https://sumproduct.com/thought/referring-to-sheets/

---

[Home](https://sumproduct.com/)

\> Referring to Sheets

*   May 10, 2019

Referring to Sheets
===================

VBA Blogs: Referring to Sheets
==============================

10 May 2019

_Welcome back to the VBA blog! Last week, we looked at how referencing sheets can be fraught with peril in the event that sheet names change, and we showed how you can use the VBA sheet name to avoid that issue._

This week, we’re going to look at working with sheets from left to right.

The VBA code “Sheets” essentially refers to the entire collection of sheets in the workbook. Instead of referring to Sheets(“Sheet1”), which will look for a sheet that is labelled “Sheet1”, we can try using Sheets(1) instead.

Sheets(1) will essentially refer to the first sheet in the workbook. So, code like the following will result in VBA activating the first sheet in the model:

![](https://sumproduct.com/wp-content/uploads/2025/06/e774d10cbbb9450fc45efbe51abdf434-708.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/f32e5a15e2cf9c3e4d2d058458ce054d-815.jpg)

Likewise, I can use any of the other Sheets properties here as well:

![](https://sumproduct.com/wp-content/uploads/2025/06/f1140ff857fc3b6f5f97a6a24f4a6fc7-729.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/06/72aa864d2854c6fefb1083fba0ab5792-677.jpg)

In this way, if you know that your data is always going to be in the 1st sheet, or the Nth sheet, you can code that logic into your VBA.

Come back next week for more VBA tips!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/referring-to-sheets/#0)
    
*   [Register](https://sumproduct.com/thought/referring-to-sheets/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/referring-to-sheets/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/referring-to-sheets/#0)

[](https://sumproduct.com/thought/referring-to-sheets/#0 "close")

top