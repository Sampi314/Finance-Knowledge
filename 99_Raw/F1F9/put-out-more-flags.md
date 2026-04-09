# How to use flags in financial models | Downloadable example | F1F9 Blog

**Source:** https://www.f1f9.com/put-out-more-flags

---

[Skip to content](https://www.f1f9.com/put-out-more-flags/?v=7885444af42e#content "Skip to content")

[![image 3](https://www.f1f9.com/wp-content/uploads/2025/10/image-3.png)](https://roberth930.sg-host.com/)

[](https://f1f9.cademy.io/)

### [Client Login](https://f1f9.cademy.io/)

[£0.00 0 Cart](https://www.f1f9.com/put-out-more-flags/?v=7885444af42e#)

Basket

[Contact Us](https://www.f1f9.com/contact-us/)

Put out more flags
==================

Share:

The financial modelling community is in broad agreement that you answer the question “when?” with a flag. But how do you model them?
------------------------------------------------------------------------------------------------------------------------------------

![flags example blog 1536x863](https://www.f1f9.com/wp-content/uploads/2026/01/Flags-example_blog-1536x863-1.jpg)
-----------------------------------------------------------------------------------------------------------------

Every forecast model we build in F1F9 has a Time sheet: a worksheet dedicated to important dates e.g. when the model starts, when the model ends, when the project starts, when the project ends, when the project moves from one phase to another. The Time sheet is a foundation sheet: bringing together core information that answers the question “when do things happen?”. 

Financial models that rely on a timeline but with no dedicated Time sheet will be difficult to review.

So what is a flag? Also known as a mask, a flag is a data series corresponding to a timeline that contains in each cell either a “1” or a “0”. Multiply your underlying data (answering the question “how much?”) with a flag and the result will either be: 

*   the data (being the underlying data x 1); or 
*   zero (being the underlying data x 0) 

So what? It means that the financial modellling can distinguish between relevant data (that multiplied by “1”) and irrelevant data (that multiplied by “0”). Useful if your core data runs beyond the period of the financial model. Or if you wish to flex the period of the financial model: change the end date and all your flags update accordingly.

**Boilerplate flags**

What’s more, when it comes to modelling flags, you will find that there are only five core structures that you need to know. Once you master all five, you can model flags. 

Use the calculation block approach that is core to modelling with the FAST Standard and save yourself time by simply copying and pasting them when you need to build them again. Identify the type of flag you need and change the ingredients. There is rarely – if ever – a need to change the formula itself. 

I think of them as boilerplate flags. Here are the five:

1.  Single date flag: the data series contains a single “1” corresponding with a specific date on the timeline. All other cells contain zeroes. Used to identify when in the model a single event occurs e.g. financial close date flag.
2.  Up to and including a single date flag: the data series contains consecutive “1”s that end once a single date is reached. All other cells contain zero. Used to identify periods running up to and including a single event e.g. pre-construction period end flag.
3.  After a single date flag: the data series contains consecutive “1”s that start only once a single date is reached. All prior cells contain zero. Used to identify periods starting after a single event e.g. post-operations period flag.
4.  Between 2 dates flag: the data series contains consecutive “1”s that start only once a single date is reached and end after another single date is reached. All other cells contain zero. Used to identify periods occurring in between 2 dates e.g. operations period flag.
5.  Non-consecutive date flags: the data series contains non-consecutive “1”s. Containing the most complex formula of any flag, this device is used to identify multiple events spaced an even period apart from each other. Unlike the “between 2 dates flag”, the period between each date is greater than each period in the model timeline e.g. term loan principal repayment flag (where, for example, semi-annual payments are made in a model whose timeline is monthly).

[Download our boilerplate flags](https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Ff.hubspotusercontent00.net%2Fhubfs%2F233102%2FF1F9-flags-example%252001a.xlsx%3FhsCtaTracking%3Db6b6aa4b-bd5f-470d-967c-f58397597962%257C8ab61bdc-a0a7-4af1-ad0e-c64e371cc42c&wdOrigin=BROWSELINK)

Shopping Basket