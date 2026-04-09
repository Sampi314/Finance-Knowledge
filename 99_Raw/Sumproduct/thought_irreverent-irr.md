# Irreverent IRR

**Source:** https://sumproduct.com/thought/irreverent-irr/

---

[Home](https://sumproduct.com/)

\> Irreverent IRR

*   May 14, 2025

Irreverent IRR
==============

Understanding some of the issues associated with the Internal Rate of Return (IRR) in Excel.

Irreverent IRR: is it irrelevant or just incalculable?
======================================================

We look at a common calculation for accountants: the Internal Rate of Return (IRR). But be warned: it may make for uncomfortable reading. By Liam Bastick, Director with SumProduct Pty Ltd.

Query
-----

My colleague has warned me that I cannot necessarily rely on the IRR results calculated in Excel. Is this true? If so, is there a way to work around the issue(s)?

Advice
------

The Internal Rate of Return (IRR) is the name given to the discount rate that makes the Net Present Value (NPV) of a range of cashflows zero. For example, if I invest $100 now and receive $121 back in two years’ time this would give me an annual IRR of 10% since:

| ($100) + PV($121) | \=  | ($100) + $121 / (1 + 10%)2 |
| --- | --- | --- |
|     | \=  | ($100) + $100 |
| i.e. **NPV** | \=  | 0   |

It is often used to calculate cost of capital hurdle rates, bond rates, discount rates implicit in leases and Compound Annual Growth Rates, amongst other tasks.

Excel has two functions that estimate IRR:

*   **IRR(values,\[guess\])** returns the periodic IRR for a set of sequential cashflows occurring on a regular periodic basis. There must be at least one positive and one negative value in the range. IRR will then cycle through an iterative technique (up to 20 times) to try and find an answer which is accurate to within 0.00001%;
*   **XIRR(values,dates,\[guess\])** returns the annual IRR (assuming a 365 day year) for a set of cashflows which may neither be sequential nor occur on a regular periodic basis. Again, there must be at least one positive and one negative value in the range. XIRR will then cycle though a similar iterative technique (this time up to 100 times) to try and find an answer which is accurate to within 0.000001%;
*   If the guess is not specified, Excel will assume that it is 10% (0.1) for both functions; and
*   Watch out with XIRR: in Excel 2003 and earlier versions it is found in the Analysis ToolPak (go to Tools -> Add Ins… or ALT + T + I). If the ToolPak has not been added in, using XIRR in a formula will give rise to the #NAME? error.

Both are fraught with problems in practice and the [attached Excel file](https://sumproduct.com/assets/thought-files/e-m/sp-internal-rates-of-return-summary-examples.xls)
 provides several documented examples. However, before we discuss some of the problems with the functions, let me compare and contrast with a simple example:

![](<Base64-Image-Removed>)

IRR vs. XIRR

In the illustration above, we consider three slightly different cashflows. The first one has the old faithful “hockey stick” projections of an outflow followed by five successive cash inflows. In our example, this would give us a periodic IRR of 1.64%. If the periods were months and we wished to convert this to annual rate then, using the compounding formula, this would be:

(1 + 1.64%)12 – 1 = 21.54%.

The second example for IRR gives the same rate – which is correct. Start dates for IRR are irrelevant: the only thing that matters is how long after the initial cashflow subsequent flows occur.

Unfortunately, the third scenario is not right and demonstrates a weakness in the IRR function. Here, the outflow still occurs in the first period, but then there is a two month delay before the inflows are received. Clearly, this will impact both the NPV and the IRR. The IRR is unaffected however – because blanks are ignored by the IRR function. To get Excel to calculate the IRR correctly here, zeroes should be entered into the two blank cells.

The XIRR examples use the same three cashflow scenarios and calculates correctly for the first and third scenarios. They demonstrate what happens when cashflows are aperiodic. For example, in the first scenario, instead of an annual IRR of 21.54% (as calculated above) we get 2.77%, reflecting the irregular payment profile.

The second scenario should be different now too, as the timing of the cashflows is different. The rate cited is 0.00%. This means that with no discounting the NPV should be zero, i.e. the numbers should add up to zero. They do not: the sum is actually $2,325.05 and there is a clue in the number formatting as to what is going on here.

Regular readers will know that I always format numbers so that values that are precisely zero are represented by a dash (“-”), whereas numbers that are approximately zero are shown as 0, or similar. Here, the actual value (in scientific notation) is **2.98 E-09** (which is 2.98 x 10-9 or 0.00000000298). Watch out for this value with XIRR: it occurs regularly and shows that Excel has been unable to calculate the value correctly, which may call for a (better) guess to be used. Microsoft claims that if the function cannot calculate a value within the tolerable limit then #NUM! is supposed to be returned, but this is often not the case:

![](<Base64-Image-Removed>)

XIRR and IRR don’t always work

IRR and XIRR can give several erroneous results. In summary, never trust 2.98 E-09.

One of the reasons this second example has gone wrong here is because XIRR requires a non-zero first value (in fact there appears to be significant anecdotal evidence to suggest it prefers a negative number).

### First Cashflow

As cited above, XIRR requires a non-zero first cashflow and that the first date in the series is the start date (further dates do not need to be in order but are supposed to occur after the start date). Consider the following example:

![](<Base64-Image-Removed>)

XIRR failure

XIRR gives a value of 2.98 E-09 here, i.e. a wrong answer (whereas IRR gives 21.43%, which is correct). XIRR should work here, but it does not. Negating all of the cashflows (which will not affect the IRR) makes no difference.

However, if the series is rearranged:

![](<Base64-Image-Removed>)

XIRR now works

XIRR now gives the right answer (when it shouldn’t). Of course, IRR will not work as cashflows need to be in the correct order. There appears to be little logic however:

![](<Base64-Image-Removed>)

Now it doesn’t work again

Changing dates around to make things work is not recommended. One tip many professional modellers employ is to use a very small negative number for the first period’s value, viz.

![](<Base64-Image-Removed>)

Using a very small number

Here, a value of -0.000001 was used. The date 2 January 2012 was chosen so that all periods are of equal length (i.e. so IRR should equal XIRR). This appears to work much of the time and hence is used by many in the modelling fraternity to overcome known XIRR issues. Unfortunately, the final example in the Excel workbook (not shown here) blows this out of the water with a scenario which delivers 2.98 E-09 once more.

### Date Recognition

Aside from understanding the importance of ordering time series, dates present another problem. Many times when we analyse data we download information from third party Management Information Systems. Often, this downloaded data provides dates in a text format. This may cause problems for XIRR, viz.

![](<Base64-Image-Removed>)

Care with dates

What’s gone wrong this time? Here, the dates have been downloaded as text strings and the XIRR function needs dates to be numerical. More often than not, this can be readily solved by applying the DATEVALUE function to these dates, although on occasion more painful (manual) approaches will have to be adopted. An example can be found in the [Excel attachment](https://sumproduct.com/assets/thought-files/e-m/sp-internal-rates-of-return-summary-examples.xls)
.

### More than One Solution

There can be more than one IRR. Every time a cashflow series changes sign (i.e. goes from positive to negative or vice versa) there is potentially another solution. Consider the following:

![](<Base64-Image-Removed>)

Multiple solutions

![](<Base64-Image-Removed>)

Here, prompted by a guess in the XIRR function (albeit of the other solution 21.43%), XIRR and IRR return the two IRRs associated with this cashflow scenario.

It is important to not only check that an IRR gives an NPV of zero but that it is also the correct one in the circumstances.

### Checking IRRs

What is a simple method for checking an IRR is correct? Consider the following example:

![](<Base64-Image-Removed>)

Checking IRR and XIRR outputs

Here, I have split the calendar year up into four equal parts (hence taking into account the time of day). XIRR and IRR should give the same answer, allowing for the fact that theoretically the XIRR solution is calculated to within 0.000001% whereas IRR is ‘only’ calculated to within 0.00001%. Unsurprisingly, testing the values using **XNPV(rate,values,dates)** shows that XIRR gives a more accurate answer.

Rubbish.

Let’s calculate the implied NPV long hand from first principles:

![](<Base64-Image-Removed>)

Checking IRR and XIRR outputs from first principles

Notice that the IRR value actually gives the more accurate answer. This is because of the little known fact that XIRR always truncates dates and assumes cashflows occur at midnight. You might think this immaterial, but I provide this example to show that XIRR is not always as accurate as many think. Take care with XNPV: it follows a similar logic to XIRR and should not be used to verify XIRR values.

### So What Would You Use Instead?

There are times when accuracy is paramount, e.g. bond issues involving large sums of money. Excel will only calculate XIRR on a maximum cycle of 100 times. GOAL SEEK, on the other hand, can calculate on a cycle of up to 32,767 iterations (this may be changed in Excel Options, ALT + T + O) with greater accuracy.

Therefore, when it is business critical, I always use GOAL SEEK to calculate IRRs. It is a very simple approach and uses the longhand checking approach described above. For example:

![](<Base64-Image-Removed>)

GOAL SEEK example

Here, an NPV calculation is constructed long hand with the discount rate an input in cell E46 (this is similar to an example in the attached Excel file).

Next, call up GOAL SEEK (ALT + T + G):

![](<Base64-Image-Removed>)

GOAL SEEK dialog box

The NPV (cell F57 here) can be set to zero by GOAL SEEK by changing the rate in cell E46. Once you have clicked ‘OK’ in the dialog box, the algorithm will cycle through to a solution where possible with the NPV displayed at the same time to confirm that the value obtained is indeed the IRR.

It may be a cumbersome method, but give me reliability over elegance any day.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/irreverent-irr/#0)
    
*   [Register](https://sumproduct.com/thought/irreverent-irr/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/irreverent-irr/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/irreverent-irr/#0)

[](https://sumproduct.com/thought/irreverent-irr/#0 "close")

top