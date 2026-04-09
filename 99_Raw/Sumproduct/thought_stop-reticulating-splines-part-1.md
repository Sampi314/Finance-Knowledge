# Stop Reticulating Splines! – Part 1

**Source:** https://sumproduct.com/thought/stop-reticulating-splines-part-1/

---

[Home](https://sumproduct.com/)

\> Stop Reticulating Splines! – Part 1

*   July 6, 2018

Stop Reticulating Splines! – Part 1
===================================

VBA Blogs: Stop Reticulating Splines! – Part 1
==============================================

6 July 2018

Sometimes a Macro is still INCREDIBLY slow to run and you’re still not sure why. Obviously, it is “[Reticulating Splines](https://www.urbandictionary.com/define.php?term=reticulating+splines)
”! But if the code is extensive, does a lot of number crunching and movement how do we speed it up?

Well there are a few ways that you can do this! Over the next few weeks we’ll look at a few tips on how you can do that.

**_No Calculations!_**

You might be “Calculating Llama Expectoration Trajectories” which require a lot of numbers being copied back and forth over the spreadsheet. Each time a new value is entered in a spreadsheet, Excel recalculates all the cells that refer to it. Same thing happens in VBA. Excel’s calculation engine is still running in the background and every time VBA writes to the Workbook. It is highly recommended that you turn OFF automatic calculations before running the steps in the Macro.

You could just turn it off in the Formula tab of the Ribbon but that’s a manual action. We could easily automate this using the command:

Application.Calculation = xlCalculationManual

This will turn off automatic calculations! If you do need to Excel to recalculate Cell values for a later step in the program you can just simply add the line:

Calculate

Top tip: This can be limited to even a specific Range or Worksheet as Calculate is also an object Method (e.g. Range(“A1”).Calculate).

But remember, you’ll need to turn it back on at the end!

For automatic calculation simply use:

Application.Calculation = xlCalclulationAutomatic

Or if you prefer the mode Automatic (except for Data Tables) use:

Application.Calculation = xlCalculationSemiautomatic

However, given that we do not know where our macro may end up or what the end users preferred settings are, the best practice way would be to store the Calculation property of the Application and revert it at the end.

**Sub** StopReticulatingSplines()

**Dim** CalcMode **As Integer**

    CalcMode = Application.Calculation

    Application.Calculation = xlCalculationManual   

**Call** DoStuff

    Application.Calculation = CalcMode

**End Sub**

Next week we’ll go over some more optimisation tricks so you can stop reticulating splines!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/stop-reticulating-splines-part-1/#0)
    
*   [Register](https://sumproduct.com/thought/stop-reticulating-splines-part-1/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/stop-reticulating-splines-part-1/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/stop-reticulating-splines-part-1/#0)

[](https://sumproduct.com/thought/stop-reticulating-splines-part-1/#0 "close")

top