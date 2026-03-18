# Avoiding Macros: Solve for X

**Source:** https://sumproduct.com/thought/avoiding-macros-solve-for-x/

---

[Home](https://sumproduct.com/)

\> Avoiding Macros: Solve for X

*   May 14, 2025

Avoiding Macros: Solve for X
============================

How to avoid using macros by using basic math instead.

Avoiding Macros: Solve for X
============================

_As a professional modeller for more years than he’d care to admit Liam Bastick highlights some of the ways to avoid the need to use macros in financial modelling / Excel spreadsheeting. This article highlights how accountants can get rid of a common macro using some basic algebra…_

### The endless loop

Throughout every Excel user’s life, there will come a time when we hear the dulcet error tones of Excel and see a dialog box pop up on the screen with a vague message:

![](https://sumproduct.com/wp-content/uploads/2025/05/30691818b35cc22c68b04e96a3f191ae.jpg)

Excel even kindly defines circular references for us. It seems so innocuous, until we realise that none of our calculations work anymore, or that it provides the wrong solution, or it has not solved it, or it has crashed / corrupted Excel – or any combination of the above.

If this logic is intentional, people will often work around this issue by creating a macro that will copy and paste the calculation in question until it loops around to the correct answer (assuming that there is a correct answer!). One of my favourite past times as a model auditor is to keep pressing ill thought-out macro buttons supposedly purporting to solve these circularities and watch them calculate astronomical – and utterly erroneous – solutions…

This is not the way.

### A Not-So-Taxing Case Study

Let’s take a look at a question that our firm has been asked to solve recently. A company wants to pay all of its profits to another party as a management fee. Suppose it makes $100 in profit, pays $20 in tax, leaving it with $80 to distribute.

If the company pays $80 in management fees, assuming that the fees have been set up to be tax deductible, then the company will actually receive an extra $16 in tax deductions. Suddenly, there’s a bit more that the company will need to pay out.

If you think about how you might lay this out in Excel, you might have the following lines:

**(1) Management fee = Income – Tax**

**(2) Profit = Income – Management fee**

**(3) Tax = (Profit + Adjustments) x 20%**

Can you see the circular reference here? You need your management fee to calculate your tax, but you need your tax to work out the fee.

The macro approach would want you to create two tax lines: one that calculates the tax; the other that contains a hard-coded pasted tax amount, which can then feed into the fee calculation. Because the tax amount is hard-coded, the calculation is ‘broken’ at that point, and it is no longer circular.

The problem with the macro approach is actually the same as having a circular reference directly in your spreadsheet. Calculations stop working properly, except this time, you don’t get an error message to warn you about it. Instead, you have to keep running the macro every time you want to see what the answer is.

### How To Avoid: Basic Maths(!?)

Or should that be, how to avoid basic maths? Now, that’s a Pulitzer prize in the making…

If you show this problem to a maths student, they might recognise the problem as something else: a set of simultaneous equations. Rather than continuously clicking the macro button to get your answer, you can solve the equation and let Excel calculate it continuously instead.

Let me break it down:

**(2) -> (3) = (4): Tax = (Income – Management Fee + Adjustments) x 20%**

**(4) -> (1): Management fee = Income – (Income – Management Fee + Adjustments) x 20%**

Rearranging this equation around a bit:

**Management Fee – Management Fee x 20% = Income – Income x 20% – Adjustments x 20%**

**Management Fee x 80% = Income x 80% – Adjustments x 20%**

**Management Fee = Income – Adjustments x 25%**

In hindsight, if we ignore the adjustments, it might have seemed a bit obvious..! Of course, with a more complicated example, the adjustments to the tax line make it a little less intuitive.

If we substitute the 20% tax rate with a variable tax rate, the formula might look like this:

**Management Fee = Income – Adjustments x Tax Rate / (1 – Tax Rate)**

So with a relatively simple calculation, we can avoid the need to have a circular reference or a macro in place, allowing the rest of our spreadsheet to continue working without the need to constantly click the ‘Run’ button.

### Word to the Wise

I often joke in training that “those who can, model – those who can’t, write a macro”. I say this with tongue firmly placed in cheek – no death threats please!!

It is not always possible to solve a circular reference in this way. Some formulae revert to polynomial calculations and those of order 5 and higher cannot be solved in an algebraic manner, for example. As the calculation logic gets more complicated, the set of equations that you need to solve becomes more difficult, especially as numbers need to be carried across time periods. To decide which to use at that point, at the end of the day, the goal is always to minimise complexity and reduce the risk of making mistakes.

To see how this example works in practice, please refer to the associated [Excel file](https://sumproduct.com/assets/thought-files/avoiding-macros-solve-for-x/sp-avoiding-macros-example.xls)
.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/avoiding-macros-solve-for-x/#0)
    
*   [Register](https://sumproduct.com/thought/avoiding-macros-solve-for-x/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/avoiding-macros-solve-for-x/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/avoiding-macros-solve-for-x/#0)

[](https://sumproduct.com/thought/avoiding-macros-solve-for-x/#0 "close")

top