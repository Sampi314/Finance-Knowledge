# Basic Functions - LOOKUP in financial modeling

**Source:** https://pivotal180.com/basic-functions-lookup-video

---

[Skip to content](https://pivotal180.com/basic-functions-lookup-video/#fl-main-content)

LOOKUP
======

By Haydn Palliser | December 5, 2019

Overview
--------

This is an extract from our pre-course videos for our renewable energy and infrastructure project finance modeling course.

Video
-----

**Video Transcript** 
---------------------

**Haydn:** The LOOKUP function covered in this lesson is most often used to find something within a specific time frame such as how many eggs were sold in a given year.

The LOOKUP function is constructed as: =LOOKUP(lookup\_value, lookup\_vector, result\_vector). In our example here, we wish to find the number of eggs shown in row 2 in year 4, that’s the input in A5, and we want to show the output in cell B5.

So here we are going to type =LOOKUP, ( look up value of a A5, that’s the year, comma, within the lookup vector, that’s the year in B1 to E1, comma, and the result factor in B2 to E2. The LOOKUP function is going to find the lookup value in year 4 in the lookup vector, which is in E1, and gives the corresponding result in the vector in row 2, which is 510 in cell E2. If I change the lookup value in A5 to 0 though, I get an N/A result. If I change the LOOKUP value to 7, which is beyond the lookup vector, we get 510.

Why?

Well, if I have a LOOKUP value less than the first value in the lookout vector, I get an N/A, I can’t do it.

But if the LOOKUP value is higher than the last value in the lookup vector, it returns the last value.

Finally, the lookup vector must be in ascending or descending order, either numerically or alphabetically.

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fbasic-functions-lookup-video%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fbasic-functions-lookup-video%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fbasic-functions-lookup-video%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#91aef3fef5e8acf9e5e5e1e2b4a2d0b4a3d7b4a3d7e1f8e7fee5f0fda0a9a1bff2fefcb4a3d7f3f0e2f8f2bcf7e4fff2e5f8feffe2bcfdfefefae4e1bce7f8f5f4feb4a3d7)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Haydn Palliser

[https://www.linkedin.com/in/haydnpalliser/](https://www.linkedin.com/in/haydnpalliser/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/basic-functions-lookup-video/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA