# Excel Functions: IF(OR) & IF(AND) for checking multiple conditions

**Source:** https://pivotal180.com/basic-functions-ifor-ifand-video

---

[Skip to content](https://pivotal180.com/basic-functions-ifor-ifand-video/#fl-main-content)

Basic Excel: IF(OR) & IF(AND) for checking multiple conditions
==============================================================

By Haydn Palliser | December 5, 2019

### Overview

This tutorial on how to use the IF(OR) & IF(AND) functions in Excel is an extract from our pre-course videos for our renewable energy and infrastructure project finance modeling course.

### Video

**How to use the IF(OR) & IF(AND) functions for checking two or more conditions in Excel**
------------------------------------------------------------------------------------------

Now that you’ve been following [**Pivotal180’s Financial Modeling Courses**](https://pivotal180.com/all-courses/)
, you probably have the IF statement down. Your boss sees you as the go to person for Excel. But now they ask you to check if the company spending was equal to the target spending this year or the previous year, not just in one year. Earlier we used the IF statement to check only one condition, that is, if A2 equaled B2. Fortunately, Excel has a built in function for checking two conditions.

### IF(OR) function in Excel

Let’s see how the IF(OR) function works for checking two or more conditions in Excel. It is constructed as equals IF, open parentheses, OR, open parentheses, condition 1, condition 2, condition N, closed parentheses. Then, value of true, value of false. And finally a closed parentheses.

So we can type **\=IF(OR(A2=B2, A3=B3),1,0)**. And we’re looking at both the conditions of A2=B2 and A3=B3. If only one of those is true, then we get a true result. For example, if A3 equals B3, this condition is true and we get a value of 1, regardless of whether the other  condition is true or false.

### IF(AND) function in Excel

Now, how can you check if the company spending was equal to the budget spending in year one, and also the same as in year two? It’s exactly the same function as with IF(OR), except we replace OR with AND. So we can type **\=IF(AND(A2=B2, A3=B3),1,0)**. And if A3 equals B3, but A2 doesn’t equal B2, then A2=B2, A3=B3 is false. So the IF statement equals 0.

As you can see, it’s pretty easy to **test multiple conditions using just two basic Excel functions**. This will become second nature to you, as these calculations will be used extensively during this financial modeling course.

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fbasic-functions-ifor-ifand-video%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fbasic-functions-ifor-ifand-video%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fbasic-functions-ifor-ifand-video%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#efd08d808b96d2879b9b9f9ccadcaecadda9cadda99f8699809b8e83ded7dfc18c8082cadda98d8e9c868cc2899a818c9b8680819cc28689809dc286898e818bc299868b8a80cadda9)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Haydn Palliser

[https://www.linkedin.com/in/haydnpalliser/](https://www.linkedin.com/in/haydnpalliser/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/basic-functions-ifor-ifand-video/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA