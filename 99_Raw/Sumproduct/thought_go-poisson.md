# Go Poisson

**Source:** https://sumproduct.com/thought/go-poisson/

---

[Home](https://sumproduct.com/)

\> Go Poisson

*   May 14, 2025

Go Poisson
==========

This article looks at calculating the inverse of a Poisson distribution for scenario modelling in a a simple, pragmatic approach for non-academics.

Go Poisson
==========

_**Cecile Nguyen** likes fishing for answers. This article looks at calculating the inverse of a Poisson distribution for scenario modelling but with the caveat this is a simple, pragmatic approach for non-academics._

Continuing on from [Simulation Stimulation](https://www.sumproduct.com/thought/simulation-stimulation)
, let us look at another way to model scenarios.

Let us look at modelling independent events that occur at a known and constant rate. Let us say I go fishing. Over long observation, I notice that I net four fish a day. The fishes are presumed independent from each other, _i.e._ a fish deciding to be caught has no bearing on the decision of another to bite.

Let’s look at the limiting factors in modelling this:

*   Sometimes catching a fish might not happen, but I would never receive -2 fish on any given day
*   Neither would I get portions of fish – it is all or nothing
*   A large number of fish might get caught, but with small likelihood – I could theoretically amass 5,000 fish in a day though it is highly unlikely
*   The events cannot occur simultaneously, there is only one fish on the line
*   The expected average number is known over a certain time period.

Now why is the binomial situation inappropriate in this case? The binomial distribution counts the number of occurrences in a set amount of trials whereas in this case there may be infinite events.

Let’s use _**?**_ to denote the mean number of events. Returning to the _**n , p**_ of the Binomial distribution, this would more closely model an infinite amount of trials _i.e. **n ? ?**_ and the probability is decreasing _**p ? 0**_ in such a way that **n p ? ?** .This is known as a **Poisson distribution** and the mathematical proof can be viewed [here](https://medium.com/@andrew.chamberlain/deriving-the-poisson-distribution-from-the-binomial-distribution-840cc1668239)
.

Thus, the likelihood of **_x_** events happening to a Poisson distribution can be calculated according to the formula:

![](https://sumproduct.com/wp-content/uploads/2025/05/55f6841c08245b5626e751e4df3b6935.jpg)

where:

*   **?** = mean
*   _**x**_ = number of events modeeling subject to _**x**_ _= 0, 1, 2, …_

Excel has two functions that can calculate it:

*   **POISSON(x, mean, cumulative).** When the last argument (**cumulative**) is set to TRUE, **POISSON** returns the cumulative probability that the observed value of a Poisson random variable with specified mean will be less than or equal to **_x_**. If **cumulative** is set to FALSE (or 0, interpreted as FALSE), **POISSON** returns the calculated probability as per the formula above
*   **POISSON.DIST(x, mean, cumulative).** As above, but note that since Excel 2007, Microsoft has updated many of its statistical functions. This more accurate function supersedes the **POISSON** function which remains for backward compatibility – for the time being at least. If you are new to both of these functions, I would suggest using this variant as Microsoft has advised it may not support the former function in future versions of Excel.

The attached [Excel file](https://sumproduct.com/assets/thought-files/go-poisson/sp-go-poisson.xlsm)
 provides an example of the Excel function can be used in practice:

![](https://sumproduct.com/wp-content/uploads/2025/05/286da9db9c08d733ca11382ddeb7fdaf.jpg)

### Simulations Analysis in Excel

Similar to [Simulation Stimulation](https://www.sumproduct.com/thought/simulation-stimulation)
, we’d like to use the simulations method to model the number of fish caught in a day. However, unlike **NORM.INV**, Excel does not provide a Poisson Inverse function which means that we had to write our own.

Let’s look at the logic of the Poisson function and create our own User-Defined Function in VBA (which we have called **PoissonInverse**):

*   Check that the probability we want to check is within the bounds and return 0 if the probability is 0
*   Because of the relationship between Binomial and the Poisson distribution for sufficiently high number of trials, _**n p ? ?**_, we can use the Binomial inverse to estimate **_x_**. We can generate the “number of trials” by using _**n = ? / p**_ . Thus, we can use the following function

**BINOM.INV(number of trials, mean / number of trials, probability)**

*   With our estimate for _x_, using **POISSON.DIST** to retrieve the cumulative value at and then loop forward or backwards accordingly to determine that this is the correct value that the minimum cumulative value is greater than the probability supplied.

The workbook has the macro inside but the macro code in text format is attached [here](https://sumproduct.com/assets/thought-files/go-poisson/sp-go-poisson-macro.txt)
 for the security concious.

We can get Excel to pick a random number between 0 and 1 using the function. There is no situation a value of 1 is permissible but luckily the **RAND()** only calculates on the \[0,1) interval, _i.e._ the number must be greater than or equal to zero but strictly less than one. For a given mean, this will generate a particular outcome appropriate to the probability distribution specified, which can then be used in the model as in the following illustration:\
\
![](<Base64-Image-Removed>)\
\
We want to model how many fish we catch over a 1,000 day period with an average of four fish per day. As per the above points, we believe this to be Poisson distributed. Using the **RAND()** function to generate probabilities, using our newly created **PoissonInverse** function we can model how many fish are caught in a given day and then chart the frequency.\
\
![](<Base64-Image-Removed>)\
\
With that, we can see that our average is calculating very close to average the model is supplied and the frequency looks quite pretty:\
\
![](<Base64-Image-Removed>)\
\
[More Thoughts](https://www.sumproduct.com/thought)\
\
*   [Log in](https://sumproduct.com/thought/go-poisson/#0)\
    \
*   [Register](https://sumproduct.com/thought/go-poisson/#0)\
    \
\
Remember me \
\
Sign in\
\
      \
\
[Forgot your password?](https://sumproduct.com/thought/go-poisson/#0)\
\
Create account\
\
      \
\
Lost your password? Please enter your email address. You will receive mail with link to set new password.\
\
  \
\
Reset password\
\
[Back to login](https://sumproduct.com/thought/go-poisson/#0)\
\
[](https://sumproduct.com/thought/go-poisson/#0 "close")\
\
top