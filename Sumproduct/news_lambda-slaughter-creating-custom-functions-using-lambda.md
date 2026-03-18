# LAMBDA Slaughter: Creating Custom Functions Using LAMBDA

**Source:** https://sumproduct.com/news/lambda-slaughter-creating-custom-functions-using-lambda/

---

[Home](https://sumproduct.com/)

\> LAMBDA Slaughter: Creating Custom Functions Using LAMBDA

*   December 4, 2020

LAMBDA Slaughter: Creating Custom Functions Using LAMBDA
========================================================

LAMBDA Slaughter: Creating Custom Functions Using LAMBDA
========================================================

4 December 2020

For those in Office 365 Beta, there is a fantastic announcement for Excel out today. After **[LET](https://www.sumproduct.com/news/article/let-off-the-leash)
** was made Generally Available just a couple of weeks ago, its sister function, **LAMBDA**, has been released into the wild. The power of this latest addition to the Excel family of functions cannot be overstated. This is going to REVOLUTIONISE how you build formulae in Excel. Model auditors are already scurrying for the hills!

This function “completes” Excel (more on that below), as a key programming feature – missing forever in the world’s favourite spreadsheet software – is now made available as well as the ability to create your own reusable formulae.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-33.jpg)

Confusingly, **LAMBDA** has _nothing whatsoever_ to do with previous Greek-named functions such as [**BETA**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-beta-dot-dist-function)
 and **[GAMMA](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-gamma-function)
**. The name dates back to Alonzo Church, a mathematician and logician who made major contributions to mathematical logic and the foundations of theoretical computer science. He coined the term as part of **lambda calculus**, in which all functions were deemed “anonymous”, _i.e._ one that is not bound to an identifier. If this means nothing to you and you are now possessing a glazed expression, welcome to my world.

Simply put, **LAMBDA** allows you to define your own custom functions using Excel’s formula language. It’s User Defined Functions without a PhD in VBA or JavaScript. In Office 365 Beta, **LAMBDA** allows you to define a custom function in Excel’s very own formula language. Moreover, one function can call another (including itself!!), so there is no limit to the power you can deploy with a single function call. And as Microsoft states, “…for folks with a computer science background, you’re probably already familiar with the concept of lambdas, and the introduction of LAMBDA makes the Excel formula language Turing Complete…”. You can now sleep at night.

With **LAMBDA**, you can take any formula you’ve built in Excel and wrap it up in a **LAMBDA** function and give it a name (like “**LiamIsAGenius**”). Then, anywhere in your Excel workbook, you can refer to **LiamIsAGenius**, re-using that custom function throughout your sheet.

So here’s the rub. If you create a **LAMBDA** called **CUSTOM1** for example, you can call **CUSTOM1** within the definition of **CUSTOM1**. This is known as **recursion** and this is what “completes” Excel. This is something that before was only possible in Excel through script (like VBA / JavaScript). This is what makes lambda functions so powerful _(see below)._

**_Reusable Custom Functions_**

One of the more challenging parts of working with formulas in Excel is that you often get fairly complex formulas that are re-used numerous times through the sheet (often by just copy/pasting). This can make it hard for others to read and understand what’s going on, put you more at risk of errors, and make it hard to find and fix the errors. With **LAMBDA**, you have re-use and composability. Create libraries for any pieces of logic you plan to use multiple times. It offers convenience and reduces the risk of errors.

So how does it work?

The syntax of **LAMBDA** is perhaps not the most informative:

![](<Base64-Image-Removed>)

That’s, er, great. Perhaps a run-through might be best.

There are three key pieces of **\=LAMBDA** to understand:

1.  **LAMBDA** function components
2.  Naming a lambda
3.  Calling a lambda function.

**_LAMBDA function components_**

Let’s take a simple example. Consider the following formula:

**\=LAMBDA(x, x+1)**

This is a very exciting formula, where we have **x** as the argument (oh no it isn’t, oh yes it is – see, I told you it was an argument), which you may pass in when calling the **LAMBDA**, and **x+1** is the logic / operation to be performed.

For example, if you were to call this lambda function and define **x** as equal to five (5), then Excel would calculate

5 + 1 = 6

Except it wouldn’t. If you tried this you would get _#CALC!_ Oops. That’s because it’s not _quite_ as simple as that. You need to name your little **LAMBDA**.

**_Naming a lambda_**

To give your **LAMBDA** a name so it can be re-used, you have to use the Name Manager (**CTRL + F3** / go to the Ribbon and then go to **Formulas -> Name Manager**):

![](<Base64-Image-Removed>)

Once you open the Name Manager you will see the following dialog:

![](<Base64-Image-Removed>)

You then click on ‘New’ and fill out the related fields, _viz._

![](<Base64-Image-Removed>)

To be clear:

*   **Name:** the Name of your function (this is where you name it!)
*   **Comment:** a description and associated ToolTip, which will be shown when calling your function
*   **Refers to:** your lambda function definition (this is where you put your formula – **_NOT_** in the Excel worksheet!).

Once completed, you may press ‘OK’ to store your lambda and you should see the definition returned in the resultant window.

![](<Base64-Image-Removed>)

**_Calling LAMBDA_**

Now that you have done this, your first new lambda function may be called in just the same way as every other Excel function is cited, _e.g._

**\=MYLAMBDA(5)**

which would equal six (6) and not _#CALC!_ as before.

You DON’T have to do it this way though if you don’t want to. You may call a lambda without naming it. If we hadn’t named this marvellous calculation, and simply authored it in the grid as we had first attempted, we could call it by simply typing:

**\=LAMBDA(x, x+1)(5)**

The sky’s the limit. You are not restricted to just numbers and text. You can also use:

*   **[\>Dynamic arrays](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
    :** rather than passing a single value into a function, you can pass an array of values, and functions can also return arrays of values
*   **[Data Types](https://www.sumproduct.com/news/article/auto-detecting-data-types)
    :** the value stored in a cell is no longer just a string or a number. A single cell can contain a rich Data Type, with a large set of properties, as discussed previously.

Functions can take data types and arrays as arguments, and they can also return results as data types and arrays. The same is true with the lambdas you build.

To show you just how useful these functions are, I want to finish with recursion. To show you just how useful these functions are, I want to finish with recursion. To show you just how useful these functions are, I want to finish with recursion. To show you just how useful these functions are, I want to finish with recursion… _(ad lib to fade)_

**_Recursion_**

One of the big missing pieces in Excel formulae has been the ability to loop or create a function that calls itself. This is something modellers have wanted for years with common calculations such as calculating optimum debt whilst taking account of interest and other similar iterative computations. Where you can, it is often better to solve formulaically (_e.g._ [calculating interest using simultaneous equations](https://www.sumproduct.com/thought/interest-received)
), but sometimes you find yourself in a situation screaming for a lambda function.

Here is an example that Microsoft came up with to demonstrate the idea.

Imagine you have a set of text strings and want to specify which characters should be removed from

![](<Base64-Image-Removed>)

Because the set of characters you’re specifying are not static, there really isn’t any good way of doing this. If you knew it was always a fixed set of characters, you could calculate using nested logic, but that would be pretty complex and error prone to author.

With **LAMBDA**, you could create a function called **REPLACECHARS** that references itself allowing you to iterate over the list of characters to be removed, where **REPACECHARS** has been defined as

**\=LAMBDA(textString, illegalChars,**

     **IF(illegalChars=””, textstring,**

       **REPLACECHARS(**

       **SUBSTITUTE(textString, LEFT(illegalChars, 1), “”),**

       **RIGHT(illegalChars, LEN(illegalChars)-1)**

**)))**

Notice that in the definition of **REPLACECHARS**, there is a reference to **REPLACECHARS**! The **IF** statement says if there are no more illegal characters, return the input **textString**, and otherwise remove each occurrence of the leftmost character in **illegalChars**. Recursion kicks in with the request to call **REPLACECHARS** again with the updated string, and the rest of **illegalChars**. This means it will keep calling itself until it has parsed over every character to be removed, giving the desired result.

![](<Base64-Image-Removed>)

**_Word to the Wise_**

The best thing is just to get going with this powerful addition to the Excel vocabulary. The **LAMBDA** function is available to members of the Insiders Beta program running Windows and Mac builds of Excel 365. It might just be a time to upgrade if you don’t already have it!

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/lambda-slaughter-creating-custom-functions-using-lambda/#0)
    
*   [Register](https://sumproduct.com/news/lambda-slaughter-creating-custom-functions-using-lambda/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/lambda-slaughter-creating-custom-functions-using-lambda/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/lambda-slaughter-creating-custom-functions-using-lambda/#0)

[](https://sumproduct.com/news/lambda-slaughter-creating-custom-functions-using-lambda/#0 "close")

top