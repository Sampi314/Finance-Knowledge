# Final Friday Fix: September 2018 Challenge

**Source:** https://sumproduct.com/blog/final-friday-fix-september-2018-challenge/

---

[Home](https://sumproduct.com/)

\> Final Friday Fix: September 2018 Challenge

*   September 27, 2018

Final Friday Fix: September 2018 Challenge
==========================================

Final Friday Fix: September 2018 Challenge
==========================================

28 September 2018

_Welcome to this month’s Final Friday Fix! This month we’re going to delve into the world of project finance, and in particular, look at the issue of construction funding – in particular, the problem of what to do when there is an upfront cost based on some total financed amount._

In a construction project, funds are typically drawn from a bank when the costs demand it. Interest is usually capitalised, effectively drawing down further funds each month. At the end of the construction period, just prior to repayments starting, the final debt amount is calculated, and this is used as the maximum value of the facility – the headline number used in a loan agreement as the maximum amount to be borrowed.

Typically, these facilities will have a few different sorts of costs – interest is the most obvious one, but often there will be some sort of upfront or establishment fee – the cost payable to the bank for signing the loan off in the first place. This is usually a percentage of the maximum amount to be borrowed. Naturally, this establishment fee is capitalised and included into the borrowing amount as well. For the sake of simplicity, we usually model this as occurring in the first period of a forecast.

Here’s where the problem lies: by capitalising the establishment fee, you effectively increase the amount due to be borrowed, which leads to an increase in the fee. If you just model it out on face value, you end up with a circular reference. As a result, people will generally either a) use an arbitrarily higher total debt input and include a check to warn if it needs to be increased, or b) use a macro to solve for the target debt value required for the establishment fee to calculate correctly.

![](<Base64-Image-Removed>)

We’ve provided an example of the problem [here](https://sumproduct.com/assets/blog-pictures/2018/challenges/09-sept/sumproduct-september-2018-final-friday-fix.xlsm)
. Note that you’ll need to keep iterative calculations on to see what the final number for this problem is. The challenge we have set this week: can you solve this exactly in a way that will update dynamically without a circular reference and without a macro? To be clear, the formula needs to:

*   solve for the correct upfront / establishment fee when you change the inputs (capital expenditure, upfront fee %, or interest rate on debt)
*   not require a macro to be run or updated
*   work when iterative calculations are switched off

In reality, the construction funding is a bit more complicated than our example provides for, but that should only make it easier to work out what the solution is. Think it’s easy? Let us know if you have a good solution, or check out the answer on Monday next week!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/final-friday-fix-september-2018-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/final-friday-fix-september-2018-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/final-friday-fix-september-2018-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/final-friday-fix-september-2018-challenge/#0)

[](https://sumproduct.com/blog/final-friday-fix-september-2018-challenge/#0 "close")

top