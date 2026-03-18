# VBA Blogs: Speeding up the Pace of Running Your Macros

**Source:** https://sumproduct.com/blog/vba-blogs-speeding-up-the-pace-of-running-your-macros/

---

[Home](https://sumproduct.com/)

\> VBA Blogs: Speeding up the Pace of Running Your Macros

*   May 18, 2017

VBA Blogs: Speeding up the Pace of Running Your Macros
======================================================

VBA Blogs: Speeding up the Pace of Running Your Macros
======================================================

19 May 2017

Macros can run pretty slowly when you start working with large files. There are a couple of tricks to improve the speed that your macro runs, relating to a) calculation time, and b) screen updates.

When you run a macro, often the screen will start flickering as it jumps from step to step, and the screen frantically tries to keep up. We can enable or disable this by using the code:

Application.ScreenUpdating = False

Application.ScreenUpdating = True

This determines whether the screen will continue to update and show what the macro is doing while it is running. Turning this off (switching it to False) will improve the processing time of the macro, because less computing power is spent updating the screen, so it can be focused on completing the task at hand.

The other thing that slows macros down is waiting for the file to calculate every time you take an action. You should know that we have three calculation options: Automatic, Automatic except for Data Tables, and Manual. These are represented by the following codes:

Application.Calculation = xlAutomatic

Application.Calculation = xlSemiAutomatic

Application.Calculation = xlManual

Before you run a long set of code, you can set the calculation setting to Manual, so that the code doesn’t recalculate the model every time it takes an action. Of course, if you need it to calculate something before using it in the next step of a macro, you can perform a ‘manual’ calculation, using the code:

Application.Calculate

Just remember that if you turn off the screen updating or calculation options, make sure that you turn them back on again afterwards!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/vba-blogs-speeding-up-the-pace-of-running-your-macros/#0)
    
*   [Register](https://sumproduct.com/blog/vba-blogs-speeding-up-the-pace-of-running-your-macros/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/vba-blogs-speeding-up-the-pace-of-running-your-macros/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/vba-blogs-speeding-up-the-pace-of-running-your-macros/#0)

[](https://sumproduct.com/blog/vba-blogs-speeding-up-the-pace-of-running-your-macros/#0 "close")

top