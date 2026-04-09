# LAMBDA Formulaic Recursion: It’s All About ME!

**Source:** https://sumproduct.com/news/lambda-formulaic-recursion-its-all-about-me/

---

[Home](https://sumproduct.com/)

\> LAMBDA Formulaic Recursion: It’s All About ME!

*   January 5, 2021

LAMBDA Formulaic Recursion: It’s All About ME!
==============================================

LAMBDA, now released into the Office 365 Beta world.

LAMBDA Formulaic Recursion: It’s All About ME!
==============================================

5 January 2021

As I mentioned previously, **[LET](https://www.sumproduct.com/news/article/let-off-the-leash)
** was recently made Generally Available, followed by its sister function, **LAMBDA**, now released into the Office 365 Beta world. This function “completes” Excel and provides you with the ability to create your own reusable formulae.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-32.jpg)

In Office 365 Beta, **LAMBDA** allows you to define a custom function in Excel’s very own formula language. Moreover, one prescribed function may call another. If the function calls itself, that’s an example of recursion, which is a way of a function calling itself, called recursion, which is a way… _\[get on with it – Ed.\]_

As a reminder, there are three key pieces of **\=LAMBDA** to understand:

1.  **LAMBDA** function components
2.  Naming a lambda
3.  Calling a lambda function.

**_1\. LAMBDA function components_**

Let’s take a simple example. Consider the following formula:

**\=LAMBDA(x, x+1)**

where we have **x** as the argument, which you may pass in when calling the **LAMBDA**, and **x+1** is the logic / operation to be performed. For example, if you were to call this lambda function and define **x** as equal to five (5), then Excel would calculate

5 + 1 = 6

Except it wouldn’t. If you tried this you would get _#CALC!_ Oops. That’s because it’s not _quite_ as simple as that. You need to name your **LAMBDA**.

**_2\. Naming a lambda_**

To give your **LAMBDA** a name so it can be re-used, you have to use the Name Manager (**CTRL + F3** / go to the Ribbon and then go to **Formulas -> Name Manager**):

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-24.jpg)

Once you open the Name Manager you will see the following dialog:

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-20.jpg)

You then click on ‘New’ and fill out the related fields, _viz._

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-15.jpg)

It’s no harder than clicking ‘OK’ at this point.

**_3\. Calling LAMBDA_**

Now that you have done this, your first new lambda function may be called in just the same way as every other Excel function is cited, _e.g._

**\=MYLAMBDA(5)**

which would equal six (6) and not _#CALC!_ as before.

You DON’T have to do it this way though if you don’t want to. You may call a lambda without naming it. If we hadn’t named this marvellous calculation, and simply authored it in the grid as we had first attempted, we could call it by simply typing:

**\=LAMBDA(x, x+1)(5)**

![](<Base64-Image-Removed>)

This trick won’t always work though – and our topic for today is on precisely this issue caused by recursion…

**_LAMBDA’s Aversion to Recursion_**

To be clear, **LAMBDA** has no aversion; in fact, it enables it. But it makes for a great sub-heading. The “aversion” is that when you use recursion in a **LAMBDA**,

**LAMBDA(**_appropriate syntax_**)(**_variable or reference_**)**

may not give the expected result. Instead, it will most likely generate an error, making you think you have written your expression incorrectly. Let me illustrate with a simple example. Consider the following:

![](<Base64-Image-Removed>)

In cell **G12**, I have typed the number nine (9), which generates the list of numbers one (1) through nine (9) from cell **G18** downwards, using the **SEQUENCE** function, _viz._

**\=SEQUENCE(G12)**

For those who recognise this is a dynamic array function and that you require Office 365 at this juncture, you are quite right – but I need Office 365 **_Beta_** version for the **LAMBDA** functions, so it’s OK. I apologise if you don’t have Office 365, but again, you might wish to reconsider which version of Excel and Office you are running, in that instance.

Cell **G16** simply sums this list:

**\=SUM(G18#)**

Therefore, inputting the numbers one (1) through (9) in cell **G12** would generate the results

1, 3, 6, 10, 15, 21, 28, 36, 45, …

In cell **G16**. These numbers are known as the **triangle numbers**

![](<Base64-Image-Removed>)

in mathematics, for very obvious reasons.

I want to show you how you can generate this sequence using a **LAMBDA**. Now, yes, I know the formula above works and you can even use the algebraic solution

**\=G12\*(G12+1)/2**

too, but the point is here, I want to show you how to create a recursive **LAMBDA** function that is simple to follow.

On the Ribbon, go to the Formulas tab and click on ‘Name Manager’ _(as above)_ (**CTRL + F3**) and click on the ‘New…’ button.

![](<Base64-Image-Removed>)

I have named my lambda function **Triangle**, and the reference (‘Refers to:’) is given by

**\=LAMBDA(x, IF(x<2, 1, x + Triangle(x-1)))**

Here, the lambda function takes a parameter **x** and defines it as one (1) if it is less than two (2), else it takes the value **x** and adds the lambda value for **x-1** – hence the recursion. This lambda function has been named **Triangle** (in the ‘Name:’ box) and is referred to in the formula too.

Therefore, for **x** equals nine (9):

**Triangle(9)** = 9 + **Triangle(8)**

\= 9 + 8 + **Triangle (7)**

\= 9 + 8 + 7 + **Triangle (6)**

\= 9 + 8 + 7 + 6 + **Triangle(5)**

\= 9 + 8 + 7 + 6 + 5 + **Triangle(4)**

\= 9 + 8 + 7 + 6 + 5 + 4 + **Triangle(3)**

\= 9 + 8 + 7 + 6 + 5 + 4 + 3 + **Triangle(2)**

\= 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + **Triangle(1)**

\= 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1

\= 45

Drawn out long hand, the recursion is clear.

This presupposes that **x** is an integer, and I have ensured this by incorporating data validation (**Data -> Data Validation** or **ALT + D + L**) into my input cell (keep it simple!):

![](<Base64-Image-Removed>)

Now that the lambda function **Triangle** has been defined, the formula in Excel is easy:

![](<Base64-Image-Removed>)

I have purposely created a simple recursive formula to demonstrate how such a calculation might work. In reality, recursive formulae are likely to be much more sophisticated and / or complex.

Let’s assume that wasn’t the case though, and you wanted to check whether your formula was working. Not everyone (anyone?) can type a formula and have it work first time, every time. Many of us would want to try the formula in a cell first:

![](<Base64-Image-Removed>)

Oh dear. That didn’t work. Of course it doesn’t. As explained above, it needs the parameter (**x**) to be defined:

![](<Base64-Image-Removed>)

Rats. This is the problem I alluded to earlier. My definition of the function refers to itself (_i.e._ recursion is exhibited). The name has not yet been defined.

Now _watch out_ here. Note the function here is **Triangle1**, not **Triangle**. There is a very important distinction. If I use **Triangle**, a similar formula _will_ work:

![](<Base64-Image-Removed>)

This is very easy to explain. I have already defined **Triangle** in the Name Manager! This is why I am using **Triangle1** to avoid this classic _gotcha_.

OK, let’s define **Triangle1** then. That will mean wrapping the expression in a **LET** function. This allows you to stop writing the same expressions time and time again in a formula, or, as Microsoft puts it, it’s “…names on a formula level”.

![](<Base64-Image-Removed>)

This has not worked either, even though **Triangle1** has supposedly been cited by **LET**. The problem is, **Triangle1** has not been defined when we are creating the lambda. This where our trick comes in – which also explains the title for this article: it’s all about **_ME_**. Let’s add a parameter (**ME**) to **Triangle1**, and replace the recursive call to **Triangle1** with **ME** (ensuring you pass in **ME** as the first parameter):

![](<Base64-Image-Removed>)

Believe it or not, we are getting somewhere now. Even though _#NAME?_ has been replaced with _#VALUE!_, the formula has evolved. Assuming you have background error checking enabled (**File -> Options -> Formulas -> Enable background error checking**), you can click on the error to see the issue:

![](<Base64-Image-Removed>)

We have an incorrect number of parameters. We have added a parameter to **Triangle1** (namely, **ME**), so the final argument of **LET** (**Triangle1($G$12)**) should also have two parameters. We do this by getting **Triangle1** to refer to itself, _viz._

![](<Base64-Image-Removed>)

It works! We have checked / debugged our **LAMBDA** in Excel. We started by calling **Triangle1(Triangle1,$G$12)**, and when we evaluate that lambda, we end up calling **Triangle1(Triangle1,$G$12-1)**_, etc_.

This technique has employed the **ME** parameter: by passing **Triangle1** as a parameter to itself, it can then use that parameter to call itself.

Once you’ve got your head around this, proved for yourself Einstein’s Theory of General Relativity and demonstrated Schwarzschild’s solution to Einstein’s field equations using tensor analysis, you have probably got your lambda working properly! Now, simply remove all references to **ME**. Exclude **ME** as the first parameter and replace the **ME(** calls with the defined name you want to use (here, **Triangle1)**. Therefore, in this instance,

**\=LET(Triangle1, LAMBDA(ME, x, IF(x<2, 1, x + ME(ME, x – 1))), Triangle1(Triangle1, $G$12))**

becomes:

**\=LAMBDA(x, IF(x<2, 1, x + Triangle1(x – 1)))**

_  
i.e_. we have proved our expression is correct. We can now add this to the Name Manager.

**_Taking it Further: Pascal’s Triangle_**

Sorry to bring back childhood recollections of mathematics, but triangle (or triangular) numbers feature in Pascal’s Triangle:

![](<Base64-Image-Removed>)

Starting with a 1 in what is conventionally known as the “zeroth” row (!), each subsequent row’s value is calculated as the sum of the cell directly above it and the cell to the left of the cell above the cell you are in. Notice the triangle numbers occur in both the third column and the third diagonal from the top.

This is an almost “ultimate” recursion, as you can trace any number on any row back through its constituent elements higher up the Triangle. Note that this beast is useful in mathematics as this array displays the binomial coefficients of **(x + 1)n**. For example:

*   **(x + 1)0 = 1** – which is the coefficient on the zeroth (**0**th) row
*   **(x + 1)1 = x + 1 = 1x + 1** – the coefficients **1** and **1** are on row **1** of Pascal’s Triangle
*   **(x + 1)2 = x2 + 2x + 1 = 1x2 +2x + 1** – the coefficients **1**, **2** and **1** are on row **2** of Pascal’s Triangle
*   **(x + 1)3 = x3 + 3x2 + 3x + 1 = 1x3 + 3x2 + 3x + 1** – the coefficients **1**, **3**, **3** and **1** are on row **3** of Pascal’s Triangle, _etc._

Now, yes, I know, Excel has a function that calculates these coefficients – and hence any element of Pascal’s Triangle. If you are often **COMBIN** the Excel functions to see how many subsets you can make, then **COMBIN** is for you. This function returns the number of combinations for a given number of items (_i.e._ the number of distinct subsets of items where order is unimportant). You should use **COMBIN** to determine the total possible number of groups for a given number of items.

The **COMBIN** function employs the following syntax to operate:

**COMBIN(number, number\_chosen)**

The **COMBIN** function has the following arguments:

*   **number:** this is required and represents the number of items
*   **number\_chosen:** this is also required. This denotes the number of items in each combination.

However, in the context of Pascal’s Triangle, it may be seen to be

**COMBIN(row\_number, column\_number)**

where both **row\_number** and **column\_number** start at zero, rather than one for the reasons demonstrated above.

The technique for calculating this using a recursive lambda function is very similar to the **Triangle** example _(above)_. You can define **Pascal** in the Name Manager (**CTRL + F3**) as

**\=LAMBDA(row\_num, col\_num, IF(OR(row\_num < 0, col\_num < 0), 0, IF(row\_num = 0, IF(col\_num = 0, 1, 0), Pascal(row\_num – 1, col\_num – 1) + Pascal(row\_num – 1, col\_num))))**

This may be checked in a cell using the **ME** technique _(as above)_:

**\=LET(Pascal1, LAMBDA(ME, row\_num, col\_num, IF(OR(row\_num < 0, col\_num < 0), 0, IF(row\_num = 0, IF(col\_num = 0, 1, 0), ME(ME, row\_num – 1, col\_num – 1) + ME(ME, row\_num -1, col\_num)))), Pascal1(Pascal1, $I$12, $I$13))**

I don’t plan to go through this here, but you may review in the [attached Excel file](https://sumproduct.com/assets/blog-pictures/2020/news/lambda-formulaic-recursion/sp-lambda-recursion-examples.xlsx)
.

![](<Base64-Image-Removed>)

This **Pascal** lambda function is a more complex example of recursion that highlights an important design consideration. On my reasonably powerful computer, when I tried to select an element from row 30 of Pascal’s Triangle, Excel took _c._55 seconds to calculate, due to all the interim recursive calculations.

Be careful. Lambda calculations in Excel are very fast, but if you adopt an excessive recursive approach as I have done here, any powerful PC will be slowed down to a “crawling speed”. The problem here is that the calculation speed in this instance is proportional to , where **_n_** is the row number.

A better lambda might be **Pascal\_Row**, where the time taken is proportional to **_n2_**:

**\=LAMBDA(a, b, LET(Pascal\_Row,**

   **LAMBDA(ME, x,**

      **IF(x=0, 1, IF(x=1, {1, 1},**

          **LET(seq, SEQUENCE(, x + 1), previous\_row, ME(ME, x – 1), shifted, IF(seq=1, 0, INDEX(previous\_row, 1, seq – 1)),**

               **IFERROR(previous\_row + shifted, 1)**

**)))), INDEX(Pascal\_Row(Pascal\_Row, a), 1, b + 1)))**

This is achieved by calculating on a row, rather than an element, basis.

But even this may be improved upon. Consider **Pascal\_Fast**:

**\=LAMBDA(n, k,**

    **IF(k \* 2 > n, Pascal\_Fast(n, n – k),**

    **IF(k = 0, 1,**

    **LET(gcd\_cutoff, 2 ^ 53 / n,**

           **previous, Pascal\_Fast(n, k – 1) \* (n + 1 – k) / k,**

           **IF(n <= gcd\_cutoff, previous,**

               **LET(gcd, GCD(previous, k),**

                      **remainder, k / gcd,**

                      **previous / gcd \* ((n + 1 – k) / remainder)))**

**))))**

This is very quick compared to both of the previous alternatives, as the time here is proportional to just **_n_**, the row number. The problem as you may have noticed here, is that as you maximise the iterative approach, the transparency of the calculation – for the average user – tends to become more and more opaque. PhDs in Computer Science are available upon request.

As a compromise, perhaps

**\=LAMBDA(n, k, IF(k=0, 1,  Pascal\_Almost\_As\_Fast(n, k – 1) \* (n + 1 – k) / k))**

{**Pascal\_Almost\_As\_Fast**) might work best, which takes approximately twice as long as the above monster (_i.e._ “almost” instantly).

**_Care with IFS and SWITCH_**

Given how calculations may “blow out” quickly when creating iterative functions, it’s best to avoid another classic _gotcha_. Let me illustrate with one of the best-known iterative sequences, the Fibonacci sequence:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, …

This sequence is calculated as **Fn = Fn-1 + Fn-2**.

You might choose to define a lambda function using **IFS** as follows:

**\=LAMBDA(x, IFS(x=1, 1, x = 2, 1, TRUE, Fibonacci(x – 1) + Fibonacci(x – 2)))**

If you are starting to follow lambdas, you should see this appears to make sense (the final argument of **IFS**, given the criterion is simply TRUE, resorts in advising what to do when **x** is neither equal to one (1) nor two (2)). There is a problem though. This function will run forever, since each parameter in this **IFS** statement must be evaluated before **IFS** gets evaluated. Therefore, when evaluating **Fibonacci(1)**, it will try to evaluate **Fibonacci(0) + Fibonacci(-1)**, and so on. Not good!

Therefore, you should use **IF** instead:

**\=LAMBDA(x, IF(x = 1, 1,IF(x = 2, 1, Fibonacci(x – 1) + Fibonacci(x – 2))))**

as **IF** does not evaluate a parameter it does not return.

Be advised, **SWITCH** exhibits a similar such property, and you should choose to use **CHOOSE** instead.

![](<Base64-Image-Removed>)

Just to highlight the point earlier about optimisation, the **Fibonacci** lambda function may be improved upon too – again, at the risk of mathematical / formulaic comprehension:

**\=LAMBDA(n, LET(Fibonacci\_Faster, LAMBDA(ME, x, F\_1, F, current, IF(x <= 2, 1, IF(x = current, F,**

 **ME(ME, x, F, F\_1 + F, current + 1)**

**))),**

**Fibonacci\_Faster(Fibonacci\_Faster, n, 1, 1, 2)))**

Now you have something to study the next time you are stranded on a desert island.

**_Word to the Wise_**

Playing with new functions is highly addictive and can lead you to using them when they are **not** needed. No matter how optimised recursive calculations are, I strongly advise that if you don’t need them, don’t use them. Formulaic alternatives, such as **COMBIN** for Pascal’s Triangle are instant and simple, to the naked eye.

Furthermore, do note that the current operand stack limit in Excel is 1,024. This should be borne in mind together with calculation times, as the current recursion limit is set as 1,024 divided by (number of lambda parameters + 1).

Finally, some common problems faced in financial modelling are **not** recursive in nature, so try not to confuse the issue unnecessarily. For example, the most common financial modelling illustration is the [calculation of interest on an average cash balance](https://www.sumproduct.com/thought/interest-received)
. This is actually an instance of solving two simultaneous equations. Applying recursive logic would be inappropriate.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/lambda-formulaic-recursion-its-all-about-me/#0)
    
*   [Register](https://sumproduct.com/news/lambda-formulaic-recursion-its-all-about-me/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/lambda-formulaic-recursion-its-all-about-me/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/lambda-formulaic-recursion-its-all-about-me/#0)

[](https://sumproduct.com/news/lambda-formulaic-recursion-its-all-about-me/#0 "close")

top