# The Check’s in the Post

**Source:** https://sumproduct.com/thought/the-checks-in-the-post/

---

[Home](https://sumproduct.com/)

\> The Check’s in the Post

*   May 14, 2025

The Check’s in the Post
=======================

We Heard you like checks so we put a check in your checks.

The Check’s in the Post
=======================

_To address some of the common issues encountered by finance professionals, we consider the importance of creating checks in your models._ _By Liam Bastick, director (and Excel MVP) with SumProduct Pty Ltd._

### Query

Adding checks to a model would seem to be prudent in order to identify inherent mistakes in the model. But when should I put them in? And how many is a good number?

### Advice

Regular readers will note that I laud the inclusion of incorporating the praises of incorporating as many checks as possible into a model. I use the generic “check” descriptor to cover three types of check:

1.  **Error checks** – the model contains flawed logic or _prima facie_ errors, _e.g._ Balance Sheet does not balance, cash in cashflow statement does not reconcile with the balance sheet, or the model contains #DIV/0! errors _etc;_
2.  **Sensitivity checks** – the model’s outputs are being derived from inputs that are not deemed to be part of the base case. This can prevent erroneous decisions being made using the “Best Case”; _and_
3.  **Alert checks** – everything else! These flag points of interest to users and / or developers modelling issues that may need to be reviewed: e.g. revenues are negative, debt covenants have been breached, _etc_.

Many modellers add checks as an afterthought. Basically, it is too late to create them then. While building a model, a developer knows what situation might break a formula. _That is when you should create the check_. When the issue is foremost in your mind, create the check there and then. It is not about creating only so many; if you need it, build it.

Let me give you an example. I am going to create the world’s simplest Balance Sheet:

### Balance Sheet Illustration

![](<Base64-Image-Removed>)

You may be an accountant with 20 years of experience or you may know very little on financial reporting. In either case, one thing everybody knows: _Balance Sheets have to balance._

So let me put a check in to ensure it balances:

### Balance Sheet Illustration (Continued)

![](<Base64-Image-Removed>)

The formula **\=C6=C10** is pretty straightforward, but I don’t recommend it. Any financial model we build will have many time periods and we will need a check for each period. Further, that’s just one check out of many. How do you feel about reading through all of your error checks and making sure they all equal TRUE?

It is true you could use a **SUMIF** formula to count all of the TRUE responses, but surely there is an easier way? Of course there is; let me walk you through it. First thing is to put the formula in brackets and multiply the bracketed expression by 1:

### Balance Sheet Illustration (Continued)

![](<Base64-Image-Removed>)

The requirement for brackets is due to the order of operations in a calculation, i.e. calculations in brackets are performed before raising numbers to powers (computing exponentials), before division, and so on.

The problem with this formula is that this will count all the times the Balance Sheet balances. Is it really that informative knowing that your Balance Sheet balances in 17,212 instances? Would it be preferable to learn that you have two errors? Of course it would. This is known as **reporting by exception**. To revise the formula:

### Balance Sheet Illustration (Continued)

![](<Base64-Image-Removed>)

The “**<>**” symbol means “is not equal to” so **\=(C6<>C10)\*1** flags (_i.e._ displays a ‘1’) when Net Assets does not equal Total Equity. That sounds good, but this is not quite sufficient either. In additions and other calculations within Excel, sometimes Excel produces minor rounding errors simply due to the way the software has been programmed. This error may occur at the eighth or ninth decimal place and is not caused by the modeller’s formula _per se_, more it is an anomaly in the coding of Excel itself. To circumvent this, I use the **ROUND** function:

ROUND(Number,Number\_of\_digits)

This rounds **Number** to **Number\_of\_digits** decimal places, _e.g._**ROUND(2.928,2)** equals 2.93.

### Balance Sheet Illustration (Continued)

![](<Base64-Image-Removed>)

In this illustration, **\=(ROUND(C6-C10,5)<>0)\*1** alerts when **C6** (Net Assets) does not equal **C10** (Total Equity) to five decimal places.

So far so good. But what if someone deletes a key reference?

### Balance Sheet Illustration (Continued)

![](<Base64-Image-Removed>)

In example, the reference in cell **C5** no longer exists giving rise to an _#REF!_ error. Unfortunately, this does happen in models. Even if you protect a worksheet (**ALT + T + P + P**), the end user may still delete the sheet! (Protecting the workbook – **ALT + T + P + W** – will prevent this, but the workbook can still be deleted.)

Therefore, if someone does manage to accidentally delete a key reference, we would want our error check to alert us accordingly. The problem is, in our example above, while our check may alert us, _#REF!_ is not necessarily the ideal way to display this. I would prefer to be alerted using our 1 / 0 system already utilised:

### Balance Sheet Illustration (Continued)

![](<Base64-Image-Removed>)

Now the checks are becoming more sophisticated. In cell **C12**_(above)_, I have added a check and modified the existing one. The first check, **\=IF(ISERROR(C6-C10),1,)**, provides the value 1 if Net Assets less Total Equity may not be evaluated. This is not the same as the formula

\=IFERROR(C6-C10,1)

Whilst this formula will provide a value of 1 if the subtraction cannot be evaluated, the alternative is not necessarily zero. This formula is not intended to be my balance check, merely a check to ensure that my balance check will work. If I were to use **IFERROR** rather than **IF(IFERROR)** the values could be _anything_. I just want values of zero and one only.

Consider the following variant of the formula in cell **C13**:

\=IF(C12<>0,0,(ROUND(C6-C10,5)<>0)\*1)

This checks to ensure that the error check in cell **C12** (the “prima facie check”) has not been triggered before checking whether Net Assets equals Total Equity. We don’t have to stop there:

### Balance Sheet Illustration (Continued)

![](<Base64-Image-Removed>)

With this third check, it may be getting see why order of checks is so important.

\=IF(AND(C12=0,C13=0),(C6<0\*1,)

checks to see if Net Assets are negative, but only if there are no _prima facie_ errors in the output and the Balance Sheet balances. In fact, this last check is a different type of check. The first two are error checks, _i.e._ these highlight issues that **must** be resolved before the model may be relied upon. Materiality is not relevant. Until these issues are fixed, the model is not calculating correctly.

The insolvency check, on the other hand, is an example of an alert check. The model is calculating correctly and there appear to be no _prima facie_ errors. However, if actuality coincides with the forecast, your business will become insolvent with more owing than owed.

This whole idea may be extrapolated further:

### Balance Sheet Illustration (Continued)

![](<Base64-Image-Removed>)

In this illustration I have demonstrated how checks may be incorporated across periods of time. The checks in cells **E13:I15** are similar to those described above already, but the checks in column **C** are new. These are aggregator checks, summarising issues across their respective rows. The formula used in cell **C13**,

\=MIN(SUM(E13:I13),1)

adds up the total in each row and takes the minimum of that summation and one. This retains the structure of the checks: zero means no issues, whereas one signifies an issue to be investigated further.  
Adding conditional formatting, number formatting and wingdings font whilst removing gridlines arguably makes for a more aesthetic look:

### Balance Sheet Illustration (Continued)

![](<Base64-Image-Removed>)

It will be a preference call, whether to include checks on a row by row basis or rather on an overall section basis (just be consistent), but these checks may then be summaries on an overall Error Check worksheet _viz_.

### Checks Worksheet

![](<Base64-Image-Removed>)

The first column of checks are merely links from checks built throughout the model and may be hyperlinked back to their respective sources. A Yes / No dropdown list separates the two columns of checks, with a “No” making the check OK in all situations. This is fine during model development as construction can generate interim model errors (_e.g._ Balance Sheet does not balance), but all error checks should be switched on prior to a model being used operationally.

Finally, the summary check at the foot of the image is the overall check for the model. It is this one which is linked to the overall check at the top of each worksheet.

### Word to the Wise

Always build checks as you go along and always fix issues as they arise rather than leave them to the end. Modellers love checks as they readily identify simple errors as they are made and end users adore them as they make the model appear more trustworthy.

Interested in reading more articles? You can find plenty more on our [thought page](https://www.sumproduct.com/thought)
, otherwise please feel free to drop Liam a line at [liam.bastick@sumproduct.com](mailto:liam.bastick@sumproduct.com)
.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/the-checks-in-the-post/#0)
    
*   [Register](https://sumproduct.com/thought/the-checks-in-the-post/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/the-checks-in-the-post/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/the-checks-in-the-post/#0)

[](https://sumproduct.com/thought/the-checks-in-the-post/#0 "close")

top