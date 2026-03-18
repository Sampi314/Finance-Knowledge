# Spreadsheet Skills: Flagging IF

**Source:** https://sumproduct.com/thought/spreadsheet-skills-flagging-if/

---

[Home](https://sumproduct.com/)

\> Spreadsheet Skills: Flagging IF

*   May 14, 2025

Spreadsheet Skills: Flagging IF
===============================

Everything you need to know about IF flags.

Spreadsheet Skills: Flagging IF
===============================

_This month, in our series of articles providing solutions to common issues encountered by finance professionals, Liam Bastick, director (and Excel MVP) with SumProduct Pty Ltd, takes a look at **IF** – how on earth can we have written over 100 articles without looking at this key function!?_

Query
-----

I have heard that there is an alternative to using the **IF** function in Excel using “flags”. What are they?

Advice
------

So what’s the most **I**mportant **F**unction in Excel? Any takers for **IF**? The syntax for **IF** demonstrates just how useful this function is for financial modelling:

**\=IF(logical\_test,\[value\_if\_TRUE\],\[value\_if\_FALSE\])**

This function has three arguments:

*   **logical\_test**: this is the “decider”, _i.e._ a test that results in a value of either TRUE or FALSE. Strictly speaking, the **logical\_test** tests whether something is TRUE; if not, it is FALSE
*   **value\_if\_TRUE**: what to do if the **logical\_test** is TRUE. Note that you do not put square brackets around this argument! This is just the Excel syntax for saying sometimes this argument is optional. If this argument is indeed omitted, this argument will have a default value of TRUE
*   **value\_if\_FALSE**: what to do if the **logical\_test** is FALSE (strictly speaking, not TRUE). If this argument is left blank, this argument will have a default value of FALSE.

This function is actually more efficient than it may look at first glance. Whilst the **logical\_test** is always evaluated, only one of the remaining two arguments is computed, depending upon whether the **logical\_test** is TRUE or FALSE. For example:

![](<Base64-Image-Removed>)

In this example, the intention is to evaluate the quotient **Numerator / Denominator**. However, if the **Denominator** is either blank or zero, this will result in an _#DIV/0!_ error. Excel has several errors that it cannot evaluate, _e.g. #REF!, #NULL, #N/A, #Brown, #Pipe_. OK, so one or two of these I may have made up, but **_prima facie_**errors should be avoided in Excel as they detract from the key results and cause the user to doubt the overall model integrity. Worse, in some instances these errors may contribute to Excel crashing and / or corrupting. Note to self: prevent these errors from occurring.

This is where **IF** comes in. In my example above,

**\=IF(Denominator=0,,Numerator/Denominator)**

tests whether the **Denominator** is zero. If so, the value is unspecified (blank) and will consequently return a value of zero in Excel; otherwise, the quotient is calculated as intended.

This is known as creating an **error trap**. Errors are “trapped” and the ‘harmless’ value of zero is returned instead. You could put “n.a” or “This is an error” as the **value\_if\_TRUE**, but you get the picture.

It is my preference not to put a zero in for the **value\_if\_TRUE**: personally, I think a formula looks clearer this way, but inexperienced end users may not understand the formula and you should consider your audience when deciding to put what may appear to be an unnecessary zero in a formula. The aim is to keep it simple **for the end user**.

An **IF** statement is often used to make a decision in the model, _i.e._

**\=IF(Decision\_Criterion=TRUE,Do\_it,Don’t\_Do\_It)**

This automates a model and aids management in decision making and what-if analysis. **IF** is clearly a very powerful tool when used correctly. However, sometimes it is used when another function might be preferable. For example, if you find yourself writing a formula that begins

**\=IF(IF(IF(IF…**

then I humbly suggest you are using the wrong function. And I don’t mean start using **IFS** from Excel 2016! **IF** should never be used to look up data: there are plenty of functions out there to help with that problem, but we will come to that in time. However, sometimes your **‘ogical\_test** might consist of multiple criteria, _e.g._

**\=IF(condition1=TRUE,IF(condition2=TRUE,IF(condition3=TRUE,1,),),)**

Here, this formula only gives a value of 1 if all three conditions are true. This nested **IF** statement may be avoided using the logical function **AND(Condition1,Condition2,…)** which is only TRUE if and only if all dependent arguments are TRUE, _i.e._

**\=IF(AND(condition1,condition2,Condition3),1,)**

This is actually easier to read. There are two other useful logic functions sometimes used with **IF**:

*   **OR(condition1,condition2,…)** is TRUE when at least one of the arguments is TRUE
*   **NOT(condition)** gives the opposite logic value, so that if the **condition** is TRUE it will be FALSE and vice versa.

Even using these logic functions, formulae may look complex quite quickly. There is an alternative: **_flags_**. In its most common form, flags are evaluated as

**\=(condition=TRUE)\*1**

**condition=TRUE** will give rise to a value of either TRUE or FALSE; the brackets will ensure this is evaluated first; multiplying by 1 will provide an end result of zero (if FALSE, as FALSE\*1 = 0) or one (if TRUE, TRUE\*1 = 1). I know some modellers prefer TRUEs and FALSEs everywhere, but I think 1’s and 0’s are easier to read (when there are lots of them) and more importantly, easier to sum when you need to know how many issues there are, _etc_.

Flags make it easier to follow the tested conditions. Consider the following:

![](<Base64-Image-Removed>)

In this illustration, you might not yet understand what the **MOD** function does (check out [A Modicom of MOD](https://www.sumproduct.com/thought/a-modicum-of-mod)
 for more details), but hopefully, you can follow each of the flags in rows 4 to 7 without being an Excel guru. Row 9, the product, simply multiplies all of the flags together (using the **PRODUCT** function allows you to add additional conditions / rows easily). This produces an **AND** flag. If I wanted the flag to be a 1 as long as one of the above conditions is TRUE, that is easy too:

![](<Base64-Image-Removed>)

Flags frequently make models more transparent and this example provides a great learning point. Often we mistakenly believe that condensing a model into fewer cells makes it more efficient and easier follow. On the contrary, it is usually better to step out a calculation. If it can be followed on a piece of paper (without access to the formula bar), then more people will follow it. If more can follow the model logic, errors will be more easily spotted. When this occurs, a model becomes trusted and therefore is of more value in decision-making.

**_Word to the Wise_**

I’d like to finish on a word of caution. Sometimes you just can’t use flags. Let me go back to my first example in this section – but this time using the flag approach:

![](<Base64-Image-Removed>)

Here, the flag does not trap the division by zero error. This is because this formula evaluates to

**\=_#DIV/0!_ x 0**

which equals _#DIV/0!_ If you need to trap an error, you must use an **IF** function.

If you have a query for the _Spreadsheet Skills_ section, please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)
 or visit the [SumProduct website](https://www.sumproduct.com/)
.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/spreadsheet-skills-flagging-if/#0)
    
*   [Register](https://sumproduct.com/thought/spreadsheet-skills-flagging-if/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/spreadsheet-skills-flagging-if/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/spreadsheet-skills-flagging-if/#0)

[](https://sumproduct.com/thought/spreadsheet-skills-flagging-if/#0 "close")

top