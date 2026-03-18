# Section Numbering

**Source:** https://sumproduct.com/thought/section-numbering/

---

[Home](https://sumproduct.com/)

\> Section Numbering

*   May 14, 2025

Section Numbering
=================

Some very simple tricks can make both you and your colleagues’ lives easier when it comes to building a “Best Practice” model.

Section Numbering
=================

Not all aspects of financial modelling revolve around knowing when to use **VLOOKUP** versus **INDIRECT** versus Power Query. Some very simple tricks can make both you and your colleagues’ lives easier when it comes to building a “Best Practice” model.

If you open almost any example model I have ever shared, you will see something like the following:

![](https://sumproduct.com/wp-content/uploads/2025/05/4bceb1ebbdeff378610b62a1f9570a99.jpg)

You may not have even noticed row 11, but it can prove to be very useful. That’s right: this time I want to look at numbering your sections – and for that matter subsections and subsubsections too (yes, I might be making these words up, but I wasn’t planning to enter the Scrabble world championships).

Similar to previous arguments with dates, I am a firm believer in auto-numbering. You should _never_ type a section / subsection / subsubsection number in: it should calculate automatically. For example, if you add in a new subsection, all subsequent numbering should update – you really don’t want to make the changes manually.

So why the big fuss about breaking your spreadsheet into sections and then numbering them? There are numerous reasons, including:

1.  It disciplines you into structuring our spreadsheets into a logical, organised manner. You start to consider both the _content_ and _purpose_ of your section, making it easier for end users to understand your calculation flow and reduce misunderstanding and consequential errors
2.  People are used to numbering. If you read a book, you expect chapter numbering and sub(sub)section referencing. Why do we get so lazy in not bothering when building spreadsheets? Often, they will consider ideas more complex than their text counterparts
3.  When building models, numbering makes it easier to communicate between the model developer and the end user, and make it easier for referencing too, creating more transparent models.

Therefore, I am going to show you here how to create numbering down to three levels. The method I will explain here will allow you to number from Section 1 to SubSubSection 999.999.999 – more than enough options for all but the most hardcore modeller. Quite frankly, if you require larger section numbers, I think you have greater problems with your model design than the number formulae!

In my example models, I usually only use Section Numbers, _e.g._ 1, 2, 3, … These have been generated automatically using the formula

**\=MAX($B$10:$B10)+1**

where the section numbering is in column **B** and the counter starts in row 11 (as in the pictured example, above). The idea for section numbering is similar. If I want to be able to generate every section number between Section 1 and SubSubSection 999.999.999, then the easiest way to do is this is to create a numbering system that will generate numbers between 1,000,000 (one million) and 999,999,999 (nine hundred and ninety-nine million, nine hundred and ninety-nine thousand, nine hundred and ninety-nine), and then “play with these numbers to generate decimal points in the right place.

I suggest headers like the following:

![](<Base64-Image-Removed>)

I try to be as lazy – sorry, I mean “efficient” – as I can be. I want to just copy the appropriate row and have the numbering present correctly and automatically. In my illustration I require five designated columns:

1.  **Section number (column B):** This column displays the correct section number
2.  **Subsection number (column C):** This column displays the correct subsection number
3.  **Subsubsection number (column D):** This column displays the correct subsubsection number
4.  **Hidden counter (column E):** This is the key column as it drives all the numbering
5.  **Heading description (column F):** This describes the content and the purpose of the section.

We need a total of six formulae:

1.  Formula to calculate next section number prior to formatting (for column **E**)
2.  Formula to calculate next subsection number prior to formatting (for column **E**)
3.  Formula to calculate next subsubsection number prior to formatting (for column **E**)
4.  Formula to format calculated section number (for column **B**)
5.  Formula to format calculated subsection number (for column **C**)
6.  Formula to format calculate subsubsection number (for column **D**).

To assist us, we will create two range names, **Million** (which equals the value 1,000,000) and **Thousand** (which equals 1,000). These can be readily created using **CTRL + F3** for example.

![](<Base64-Image-Removed>)

Let’s make a start then – and we begin in _reverse_ order…

**_SubSubSection Header_**

![](<Base64-Image-Removed>)

I will assume that you will be using a template similar to the [attached Excel file](https://sumproduct.com/assets/thought-files/2019/section-numbering/sp-section-numbering-example.xlsm)
. In this example, headers may start from row 6 onwards, therefore our anchor row has to be row 5. The formula for the hidden counter in column **E** is very simple. Assuming our header is in row 6, we would use the formula:

**\=MAX($E$5:$E5)+1**

We start with the subsubsections because the numbering is trivial. This is the formula for the hidden counter in column **D**. The number to be displayed would be generated using the calculation

**\=INT(E6/Million)&”.”&ROUND(MOD(E6/Million,1)\*Thousand,0)  
&”.”&ROUND(MOD(E6/Thousand,1)\*Thousand,0)**

which is perhaps not quite so trivial, but not as complex once you break it down! Let me explain:

*   Our numbering is going to be of the form **abc,def,ghj**, which will convert to **abc.def.ghj**, with any zeros suppressed for the algebraic representatives **a**, **b**, **d**, **e**, **g** and **h**
*   The first part, ****INT(E6/Million)****
*   takes the whole number in cell **E6** once it has been divided by **Million**, _i.e. **abc**_.For example, the number 13,071,412 would be displayed as 13
*   The next element,  
    **&”.”&  
    **simply adds a decimal point after the first calculation (_e.g._ “13.” in our illustration)
*   The second calculation,  
    **ROUND(MOD(E6/Million,1)\*Thousand,0)  
    **extracts the hundreds of thousands, tens of thousands and thousands numbers (the numerical characters **def** in **abc,def,ghj**), suppressing zeros.
    
    I have covered the **MOD** function before. **MOD(number,divisor)**, returns the remainder after the **number** (first argument) is divided by the **divisor** (second argument). The result will have the same sign as the **divisor**.
    
    For example, 9 / 4 = 2.25, or 2 remainder 1. **MOD(9,4)** is an alternative way of expressing this, and hence equals one (1) also. Note that the 1 may be obtained from the first calculation by (2.25 – 2) x 4 = 1, _i.e._ in general:  
    **MOD(n,d) = n – d\*INT(n/d)**,  
    where **INT()** is the integer function in Excel.
    
    Therefore, **MOD(x,1)** returns the fractional part of **x**, i.e. the number after the decimal point. Hence, **ROUND(MOD(E6/Million,1)\*Thousand,0)** removes any number greater than or equal to 1,000,000 (**Million**) and returns the first three numbers after the decimal point, when the number has been divided by **Million**. In our example, this formula returns 71 from the number 13,071,412
    
*   The next element is again**  
    &”.”&**  
    which simply adds a decimal point after the calculations so far (_e.g._ “13.71.” in our illustration)
*   The final calculation,**  
    ROUND(MOD(E6/Thousand,1)\*Thousand,0)**  
    works similarly to the second one returning the final three values (**ghj** in **abc,def,ghj**), again suppressing any leading zeroes.
    
    This would return 412 from our example 13,071,412, and the formula in its entirety produces  
    13.71.412.
    

So far, so good – so what’s next?

**_SubSection Header_**

![](<Base64-Image-Removed>)

Again, I will assume that you will be using a template similar to the [attached Excel file](https://sumproduct.com/assets/thought-files/2019/section-numbering/sp-section-numbering-example.xlsm)
. The headers will start from row 6 as before, with our anchor in row 5. The formula in column **E** is not quite as simple as the subsubsection’s counterpart:

**\=(ROUNDDOWN(MAX($E$5:$E5)/Thousand,0)+1)\*Thousand**

Subsection counters are the three digits in the thousands, namely the hundreds of thousands, the tens of thousands and the thousands. This function disregards any numbers smaller than 1,000 (**Thousand**). It works by dividing the number by 1,000, adding one (1) and then multiplying it by 1,000 once more. This means that the next number after 13,071,412 would be 13,072,000.

Note that I use the **ROUNDDOWN** function, rounding to zero (0) decimal places. Having used **INT** earlier, you might be wondering why I did not use **INT** here. It’s simple. One of the quirks of Excel is that **INT** will not always work as intended when dividing and re-multiplying by larger numbers. **ROUNDDOWN** is a reliable alternative.

The formula to present the subsection number (_e.g._ convert 13,072,000 to 13.72) is as follows:

**\=INT(E6/Million)&”.”&ROUND(MOD(E6/Million,1)\*Thousand,0)**

which is simpler than its subsubsection counterpart:

*   As before, our numbering is going to be of the form **abc,def,ghj**, which will convert to **abc.def.ghj**, with any zeros suppressed for the algebraic representatives **a**, **b**, **d**, **e**, **g** and **h**
*   The first part,  
    **  
    INT(E6/Million)  
    **  
    once more takes the whole number in cell **E6** once it has been divided by **Million**, _i.e. **abc**_.For example, the number 13,072,000 would be displayed as 13
*   The next element,  
    **  
    &”.”&  
    **  
    simply adds a decimal point after the first calculation (_e.g._ “13.” in our illustration)
*   The second calculation,  
    **  
    ROUND(MOD(E6/Million,1)\*Thousand,0)  
    **  
    extracts the hundreds of thousands, tens of thousands and thousands numbers (the numerical characters **def** in **abc,def,ghj**), as previously. In our example, this formula returns 72 from the number 13,072,000, and the formula in its entirety would return 13.72.

This leaves us with just the section header to go…

**_Section Header_**

![](<Base64-Image-Removed>)

We are nearly there. Yet again, the headers will start from row 6 as before, with our anchor in row 5. The formula in column **E** is similar to the one for the subsection, but using **Million** rather than **Thousand**:

**\=(ROUNDDOWN(MAX($E$5:$E5)/Million,0)+1)\*Million**

Subsection counters are the digits greater than or equal to 1,000,000. This function disregards any numbers smaller than 1,000,000 (**Million**). It works by dividing the number by 1,000,000, adding one (1) and then multiplying it by 1,000,000 once more. This means that the next number after 13,071,412 would be 14,000,000.

Again, I have to use **ROUNDDOWN** rather than **INT** as before.

The formula to present the section number is trivial:

**\=MAX($B$5:$B5)+1**

which is how the section counter calculates in my other Excel example files. The counter in column **E** is not required here but is to keep the running totals for the subsection and subsubsection counters.

**_Word to the Wise_**

This all may seem like overkill, but once you start using section numbering you will never look back, In fact, most modellers will incorporate their section numbering into their model templates and just copy the headers as they need them, knowing the auto-numbering will work as intended. Over time, they probably will have forgotten the mechanics of these formulae – but this makes the idea no less important.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/section-numbering/#0)
    
*   [Register](https://sumproduct.com/thought/section-numbering/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/section-numbering/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/section-numbering/#0)

[](https://sumproduct.com/thought/section-numbering/#0 "close")

top