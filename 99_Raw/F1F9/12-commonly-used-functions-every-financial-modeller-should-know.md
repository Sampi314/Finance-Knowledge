# F1F9 | 12 Commonly Used Functions Every Financial Modeller Should Know

**Source:** https://www.f1f9.com/12-commonly-used-functions-every-financial-modeller-should-know

---

[Skip to content](https://www.f1f9.com/12-commonly-used-functions-every-financial-modeller-should-know/?v=7885444af42e#content "Skip to content")

[![image 3](https://www.f1f9.com/wp-content/uploads/2025/10/image-3.png)](https://roberth930.sg-host.com/)

[](https://f1f9.cademy.io/)

### [Client Login](https://f1f9.cademy.io/)

[£0.00 0 Cart](https://www.f1f9.com/12-commonly-used-functions-every-financial-modeller-should-know/?v=7885444af42e#)

Basket

[Contact Us](https://www.f1f9.com/contact-us/)

12 commonly used functions every financial modeller should know
===============================================================

![12 functions blog 882x435](https://www.f1f9.com/wp-content/uploads/2026/01/12-functions-blog-882x435-1.jpg)

Share:

Of 450+ functions available in Excel, we commonly use no more than 12 when building financial models.
-----------------------------------------------------------------------------------------------------

That’s because, when it comes to formulas, we aim for simplicity and readability.

Complex functions with poor audit trails (I’m thinking of OFFSET, for example) are less useful when your primary objective is transparency.

Here are 12 functions that we use again and again in financial modelling in excel. We’ve shared them so that you may develop your own opinion of their usefulness.

Working repeatedly and consistently with a short list of functions that are easy for others to review and understand is an important skill for financial modellers. That’s not to say that other functions are ignored – it’s just that they are used by exception only.

SUM
---

Essential and easy to understand. Since – like INDEX – it refers to a range of cells, it can include a stretch row to allow for insertion (or removal) of data without requiring amendment to the formula. Try Alt + equals (“=”) as a shortcut to set up a SUM function.

IF
--

We use this in its simplest form and avoid IF statements within an IF statements (known as a “nested IF”).

Note: IF statements can hide circularities in a model where the circularity is triggered by the unused outcome of the IF statement.

AND
---

We use this in conjunction with IF when building flags: the IF statement runs two tests – both of which must be met if the flag is to return “1”.

![10 functions 2 882x496](https://www.f1f9.com/wp-content/uploads/2026/01/10-functions-2-882x496-1.webp)

EDATE and EOMONTH
-----------------

We use EDATE to help construct timelines where it is not essential to have dates ending at the end of a month.

Whereas EOMONTH is needed to identify end-of-month dates.

![10 functions 4 882x496](https://www.f1f9.com/wp-content/uploads/2026/01/10-functions-4-882x496-1.webp)

MIN and MAX
-----------

Particularly useful in modelling cash tests: pay back the lower of available cash or loan balance outstanding, for example.

Both are essential in working with line items that have both positive and negative numbers, noting that MAX(0, number) will return positive numbers only.

![10 functions 8 882x496](https://www.f1f9.com/wp-content/uploads/2026/01/10-functions-8-882x496-1.webp)

And MIN(0, number) will return negative numbers only.

![10 functions 9 882x496](https://www.f1f9.com/wp-content/uploads/2026/01/10-functions-9-882x496-1.webp)

INDEX
-----

Our preferred choice for simple scenario selection.

![10 functions 1 882x496](https://www.f1f9.com/wp-content/uploads/2026/01/10-functions-1-882x496-1.webp)

Use in combination with MATCH for a more complex scenario manager.

SUMIFS
------

We use it both to aggregate data (from monthly to semi-annual time buckets, for example) and to shift individual numbers to the right along a row. It is more flexible than SUMIF and – even more important – its first argument is the numbers being summed (which improves its traceability).

![10 functions 3 882x496](https://www.f1f9.com/wp-content/uploads/2026/01/10-functions-3-882x496-1.webp)

VLOOKUP
-------

We use this to find and present information on a horizontal timeline from a table organised vertically.

![10 functions 5 882x496](https://www.f1f9.com/wp-content/uploads/2026/01/10-functions-5-882x496-1.webp)

Note the importance of specifying an approximate (“TRUE”) or an exact (“FALSE”) match.

ISNA
----

More useful than ISERROR since it is more precise. It only identifies #N/A errors – and leaves other errors well alone. Use in conjunction with VLOOKUP to set out-of-table range errors to zero.

![10 functions 6 882x496](https://www.f1f9.com/wp-content/uploads/2026/01/10-functions-6-882x496-1.webp)

XIRR
----

A “least worst” complex function. It returns an average, annual rate of return based on actual cash flows using day counts. The answer is presented on an annualised basis.

Compare that with IRR which assumes equal periods between cash flows and returns an answer that is presented on a periodic basis.

![10 functions 7 882x496](https://www.f1f9.com/wp-content/uploads/2026/01/10-functions-7-882x496-1.webp)

It is easy to get excited by the new functions that Excel introduces – there is no question that they offer remarkable spreadsheeting power. But if your primary purpose is to [build financial models](https://www.f1f9.com/financial-model-build/)
 that are transparent, easy to navigate and no more complex than they need to be, then you need to be highly selective in your use of functions (and very aware of their pros and cons).

Shopping Basket