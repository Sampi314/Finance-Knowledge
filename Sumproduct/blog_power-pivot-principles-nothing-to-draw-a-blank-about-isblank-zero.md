# Power Pivot Principles: Nothing to Draw a BLANK About – ISBLANK Zero?

**Source:** https://sumproduct.com/blog/power-pivot-principles-nothing-to-draw-a-blank-about-isblank-zero/

---

[Home](https://sumproduct.com/)

\> Power Pivot Principles: Nothing to Draw a BLANK About – ISBLANK Zero?

*   December 7, 2020

Power Pivot Principles: Nothing to Draw a BLANK About – ISBLANK Zero?
=====================================================================

Power Pivot Principles: Nothing to Draw a BLANK About – ISBLANK Zero?
=====================================================================

8 December 2020

_Welcome back to the Power Pivot Principles blog. This week, we take a look at a common mistake made with zero(e)s._

I am going to continue where I left off last time. [Last week](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-problems-with-1-month-ago)
, we looked at the following dataset:

![](<Base64-Image-Removed>)

We created two measures,

**Total Sales = SUM(Sales\[Sales\])**

**Total Sales 1 Month Ago = CALCULATE(\[Total Sales\],PREVIOUSMONTH(Sales\[Month\]))**

These two calculations created the following PivotTable:

![](<Base64-Image-Removed>)

I am going to create another measure to ascertain the month on month percentage growth in **Sales**:

![](<Base64-Image-Removed>)

**Pct Sales Growth Month on Month**

**\=(\[Total Sales\]-\[Total Sales 1 Month Ago\])/\[Total Sales 1 Month Ago\]**

Please note that I am deliberately staying away from the **[DIVIDE](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-introducing-the-divide-function)
**function this week as I wish to make a point about zero(e)s, the **[BLANK](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-drawing-a-blank-on-error-traps)
** function and the **ISBLANK** function.

Upon creating this measure, I get the following result:

![](<Base64-Image-Removed>)

Oh dear. We get some _#NUM!_ errors. That’s not good. These are caused for two reasons:

1.  The Jan 2020 result returns _#NUM!_ because **Total Sales 1 Month Ago** literally – as well as figuratively – draws a blank. It’s not returning any result, so it’s not just zero that may cause a division error in DAX code.
2.  The Feb 2020 result returns _#NUM!_ for the usual mathematical reasons. **Total Sales 1 Month Ago** returns zero (0) this time – and dividing anything by zero is mathematically indeterminate, hence the _#NUM!_ error.

It’s never good having _prima facie_ errors in our outputs, but this measure may be easily remedied:

![](<Base64-Image-Removed>)

**Pct Sales Growth Month on Month**

**\=****IF(\[Total Sales 1 Month Ago\]=0,0,****  
(\[Total Sales\]-\[Total Sales 1 Month Ago\])/\[Total Sales 1 Month Ago\]****)**

Having wrapped the measure in an **IF** statement, I get the following result:

![](<Base64-Image-Removed>)

This still isn’t really correct, as we haven’t achieved zero growth for the first two months – we have just created two calculations that cannot be computed. The **BLANK** function may be a better option:

![](<Base64-Image-Removed>)

**Pct Sales Growth Month on Month**

**\=IF(\[Total Sales 1 Month Ago\]=0,****BLANK()****,  
(\[Total Sales\]-\[Total Sales 1 Month Ago\])/\[Total Sales 1 Month Ago\])**

This looks better:

![](<Base64-Image-Removed>)

In fact, if we remove the fields **Total Sales** and **Total Sales 1 Month Ago** from the PivotTable, there is something else to note:

![](<Base64-Image-Removed>)

Do you see how the first two months disappear? This is because when all displayed measures return **BLANK()**, relevant headings will be suppressed automatically. This can prove quite a useful trick in financial reporting.

However, if you do want them to show, there is an option. If you right-click inside the PivotTable,

![](<Base64-Image-Removed>)

select ‘PivotTable Options…’ and then

![](<Base64-Image-Removed>)

go to the Display tab and check ‘Show items with no data on rows’ and / or ‘Show items with no data on columns’ as appropriate.

You can also consider **ISBLANK**, which pretty much does the same thing it does in Excel.

![](<Base64-Image-Removed>)

**Pct Sales Growth Month on Month**

**\=IF(****ISBLANK(****\[Total Sales 1 Month Ago\]****)****,BLANK(),  
(\[Total Sales\]-\[Total Sales 1 Month Ago\])/\[Total Sales 1 Month Ago\])**

This returns a different result:

![](<Base64-Image-Removed>)

**ISBLANK** can distinguish between zero(e)s and blanks. That’s not what we want here as this brings our _#NUM!_ error back for Feb 2020. The previous formula is more appropriate, since we did have zero sales _entered_ in Jan 2020. However, sometimes you want to distinguish between a value of zero and a blank value; **ISBLANK** is perfect for that.

That’s it for this week!

Stay tuned for our next post on Power Pivot in the [Blog](https://sumproduct.com/blog)
 section. In the meantime, please remember we have training in Power Pivot which you can find out more about [here](https://sumproduct.com/courses/)
. If you wish to catch up on past articles in the meantime, you can find all of our Past Power Pivot blogs [here](https://www.sumproduct.com/thought/power-pivot-principles-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-pivot-principles-nothing-to-draw-a-blank-about-isblank-zero/#0)
    
*   [Register](https://sumproduct.com/blog/power-pivot-principles-nothing-to-draw-a-blank-about-isblank-zero/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-pivot-principles-nothing-to-draw-a-blank-about-isblank-zero/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-pivot-principles-nothing-to-draw-a-blank-about-isblank-zero/#0)

[](https://sumproduct.com/blog/power-pivot-principles-nothing-to-draw-a-blank-about-isblank-zero/#0 "close")

top