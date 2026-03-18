# Monday Morning Mulling: March 2020 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-march-2020-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: March 2020 Challenge

*   March 29, 2020

Monday Morning Mulling: March 2020 Challenge
============================================

Monday Morning Mulling: March 2020 Challenge
============================================

30 March 2020

_On the final Friday of each month, we set an Excel problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-246-1.jpg)

Welcome to this month’s Monday Morning Mulling. I imagine a **_fraction_** of you worked out [last Friday’s challenges](https://sumproduct.com/blog/final-friday-fix-march-2020-challenge/)
…

**_The Challenge_**

As mentioned previously, in a recent financial model build, we needed to work out how much of a certain product was sold, which reduced each period, based on two multiplicative factors. Over the life of the project, the proportion that needed to be considered was:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-243-1.jpg)

In Excel, I just needed to sum this _as efficiently as possible­_ – returning the total as a fraction in its simplest form.

Therefore, the challenge was to create an Excel spreadsheet that can calculate the result and be sufficiently flexible to allow for alternative, similar sequences of varying length. I stipulated you should not use dynamic arrays, VBA or megaformulae. How did you do?

**_Suggested Solution_**

Often under time pressure, we resort to becoming hapless automatons that simply crunch numbers without thought. Yes, I could just add the numbers up constructing an Excel summation. However, the spreadsheet would return a decimal such as

0.166333666333666…

which provides little insight. Furthermore, I actually wanted the number expressed as a fraction.

It’s trivial to note that the numbers in the denominator were consecutive pairs in the sequence

2, 5, 8, 11, …, 998, 1001

_i.e._ the pairs were always a gap of three (3) apart (_e.g._ 5 – 2 = 3, 8 – 5 = 3, 1,001 – 998 = 3).

However, did you spot that

![](<Base64-Image-Removed>)

and, more generally,

![](<Base64-Image-Removed>)

This is where readers who are parents may note their children might have helped! The trouble is many of us learned fraction subtraction a lifetime ago and either (a) have long since forgotten it and / or (b) never understood it in the first place!

After this, the problem becomes straightforward:

![](<Base64-Image-Removed>)

The [attached Excel file](https://sumproduct.com/assets/blog-pictures/2020/fff-mmm/mar/mmm/sp-adding-fractions-in-a-series.xlsm)
 shows how this could be constructed automatically.

At this point some of you will state that they could have done this simply by formatting cells and choosing ‘Fraction’ for the result:

![](<Base64-Image-Removed>)

But that will not always work – like here. If you did this with this month’s challenge you would have obtained 83/499 and not 333/2,002. These two fractions are **not** equivalent. Therefore, if you did this you would have calculated the wrong answer.

Even if you have done what I have done so far, there is still one more step. The fraction has to be in its simplest form, _i.e._ where the numerator and the denominator share no common divisor grater than one (1). This may be achieved using Excel’s [GCD](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-gcd-function)
 function.

In mathematics, the greatest common divisor (GCD), also known as the greatest common denominator or the highest common factor, of two or more non-zero integers, is the largest positive integer that divides the numbers without a remainder.

The Excel function **GCD** returns the greatest common divisor of two or more integers. The greatest common divisor is the largest integer that divides both **number1** and **number2** without a remainder. It has the following syntax:

**GCD(number1, \[number2\], …)**

For example, the GCD of 333 and 2,002 is 1, so this is the simplest fraction. However, if we extend our sequence to

![](<Base64-Image-Removed>)

Then the result is

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

This is because **GCG(400,2404)** equals four (4), so both the numerator and denominator may be quartered.

Again, the [attached Excel file](https://sumproduct.com/assets/blog-pictures/2020/fff-mmm/mar/mmm/sp-adding-fractions-in-a-series.xlsm)
 shows how this may be achieved – and how you can use it for other similar problems.

**_Word to the Wise_**

Whether you took a similar approach, chose a more convoluted route or simply didn’t bother, do note that sometimes financial modelling is about thinking more _simply_. It’s not always about who knows IFRS, the latest fancy functions in Excel or VBA, sometimes it’s simply a case of spotting there’s a wood in those trees.

_The Final Friday Fix will return on Friday 24April with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-march-2020-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-march-2020-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-march-2020-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-march-2020-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-march-2020-challenge/#0 "close")

top