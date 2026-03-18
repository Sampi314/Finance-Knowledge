# Date Functions and Timelines in Financial Modeling -Video

**Source:** https://pivotal180.com/date-functions-and-timelines-video

---

[Skip to content](https://pivotal180.com/date-functions-and-timelines-video/#fl-main-content)

Date Functions and Timelines
============================

By Haydn Palliser | December 5, 2019

Overview
--------

This is an extract from our pre-course videos for our renewable energy and infrastructure project finance modeling course.

Video
-----

**Video Transcript** 
---------------------

**Haydn:** When setting up a financial model, one of the first things you have to do is consider the duration of it. Is the model going for 1 year or 5 years, 30 years or in some cases, 99 years in the future? Is the model periodicity going to be monthly or quarterly semi-annual, or annual? By periodicity, I mean the duration each column of the model will represent. Different models require different periodicity and before you start modeling you have to decide on this and then build the timing resolution of the model. What do I mean by this? Let’s look at an example with a quarterly periodicity for six periods or 1.5 years. This is really typical of what you would need to see with the start of the period on row one on a separate line from the end of the period on road two. Each column represents its own quarter, the first period starting on the 1st of January, 2021 and ending on the 31st of March, 2021. The second quarter starts one day after the first quarter on the 1st of April, 2021 and ends on the 30th of June, 2021 there is of course one single formula per row starting in column C being copied across.

**Haydn:** This is the layout we require and in this lesson we will learn how dates in Excel work, how to calculate a model timeline and how to add other useful counters to your model such as how many years the project has been operating for.

**Haydn:** But before we build the required calculations, let’s understand what dates in Excel actually represent. So starting in A1, we have the 1st of January, 1900. In B1, the date is the 2nd of January, 1900. They are formatted as day, day, month, month, month, year, year, just to avoid confusion between the U S and international date formats. To set this format, we go to cell format which you can access by right clicking on a cell and pricing pressing format. So why the 1st of January, 1900?

**Haydn**: I’m pretty sure none of you were born by this date. Except maybe you Dan. I’m pretty sure you were born by then. He didn’t like that one at all.

**Haydn:** Anyway, dates are actually integers, just formatted to look like a date, with Excel also recognizing that this format is broken down into days and months in a year. And the 1st of January, 1900 represents the first date in Excel, for PCs at least, or it has a value of 1. So in this example, row 2 equals row 1, but it’s formatted as an integer, so the second or January, 1900 equals 2, the 3rd of January, 1900 equals 3, and so on and so forth. And given the integers we can also add or subtract dates from each other or add integers to them. The 1st of January plus 1 just equals 2. The 2nd of January minus the 1st of January of the same year equals 1. So that’s great to know, but it still doesn’t tell me how to get a date three months after another to create my quarterly time frame. I can’t just add 90 days at the start of every quarter because every quarter has a different length.

**Haydn:** Luckily, Excel has a function for us called EOMONTH. The EOMONTH formula works =EOMONTH, open parenthesis, start date, comma, number of months after the start date, closed parenthesis, where a positive number of months we’ll achieve dates after the start day and a negative number of months will calculate a date before the start date. Using some examples, let’s say we have EOMONTH 1st of January, 2021, comma, 0. That equals the 31st January, 2021. EOMONTH takes you to the end of the current month. The start date had instead been say the 14th of January, the result would still have been the same: the end of the current month. With EOMONTH 1 Jan, 2021, comma, 1, we get the 28th of February, 2021 that’s the end of the month one month after the current month. If we had EOMONTH 1 Jan, 2021, comma, 2, that equals the 31st of March, 2021, the end of the month two months after the current month. So for the end of a quarter we want to use EOMONTH, start date, comma, 2, it’s a little counter intuitive as we want to go ahead three months, not two. But the reason is that 0 takes you to the end of the current month. So we really want to go ahead 3 months minus 1 equals 2. Sorry, that’s just how it works. I didn’t design it.

**Haydn:** We don’t want to use a hard-coded 2, so we replace that with a name range of months per quarter, which equals three minus one equals two. So back to our quarterly timeline. Our calculations are as follows. For the end of the first quarter C2 equals EOMONTH open parentheses C1 comma months per quarter minus 1, which equals the 31st of March, 2021. As we can add dates, the start of the next quarter is just D1 equals C2 plus 1 equals the 1st of April, 2021. Period 2 starts the beginning of the day following the end of period 1. And of course both rows are now copied across to the end of the required time period. You may now be asking, well how long should a model timeline be? Good question. And the answer is it depends on the generation of the project or the investment, but it’s wise to always leave a little bit of spare room in case things don’t go quite to plan. As some guidance, if you have a five year plan project, perhaps take them all out to say seven years. Sometimes we need to calculate a date a number of months after another.

**Haydn:** Actually, Dan, you love Valentine’s day and this section includes the 14th of February. So why don’t you take over from here?

**Dan:** I am a romantic and I do love Valentine’s day, which is why I bought you this wonderful bottle of French wine.

**Dan:** Sometimes we need to calculate a date which is a certain number of months after another. For example, the project may draw down debt on the 14th of February, 2021 and repayments are to be every three months thereafter, meaning that the first repayment is the 14th of May, 2021. Excel has a function to help us out with that and that function is EDATE. The way we would call EDATE is simply equals EDATE open parentheses, specify a start date comma and specify a number of months closed parentheses. The formula is broadly the same as EOMONTH, however, the number of months that we input calculates a future date, which is a certain number of months into the future that’s on the same day of the month as the start date. So if for example, what we’re calling is EDATE 14 February, 2021 comma 3 closed parentheses, that will take us to the 14th of May, 2021.

**Haydn**: In addition to our date timeline at the top of the model, there are a number of other common date type calculations than a model may need. Such as in which calendar year is the current period or which quarter are we in? Are we in quarter one two, three or six from the start of the model? Or maybe which model year we’re in: year one, year two or year three from the start of the model. For calendar year, Excel comes to the rescue and we can use the year function. It’s just year open parentheses period, end date, close parentheses. So in C4 we get 2021.

**Haydn:** The model quarter, it’s also quite easy. We start with a value of 1 in the first column and we just add 1 every period. So D5 equals C5 plus 1.

**Haydn:** Model year is a little bit trickier and we want to see one for four periods throughout 2021 and then two for four periods throughout 2022. This is a little challenging but when converting between time periods, think about either dividing or multiplying numbers. For example, if we are in quarter eight what year is this? It’s year two of course, but how did we get there? We divided eight being the eighth quarter by four being the number of quarters in a year. For challenges, this works great for the eighth quarter or the fourth quarter as their factors of four so when dividing by four we get a whole number. But what about quarter three? Three divided by four equals 0.75 or the fifth quarter: five divided by four equals 1.25. Maybe you can see a solution. We can use the ROUNDUP function to round up the nearest whole number. Rounding up quarter three’s value of 0.75 to one and the fifth quarter value of 1.25 to two. The equation for ROUNDUP is simply ROUNDUP open parentheses, number comma number of digits, close parenthesis. So in the third quarter as an example, the equation equals round up open parentheses, three divided by four. That’s that 0.75 comma zero that rounds up to one the correct answer. Of course, though we don’t use hard code, so we replaced this with ROUNDUP open parentheses model quarter divided by quarters per year, comma zero.

**Haydn:** Quite challenging, but it’s okay. We will do this together in class, just come prepared to model.

Enroll in a Pivotal180 course! We offer a range of training programs for modelers of different backgrounds and experience levels:

[Renewable Energy Project Finance Modeling](https://pivotal180.com/course-type/renewable-energy-project-finance-modeling/)

[Project Finance Modeling](https://pivotal180.com/course-type/project-finance-modeling/)

[Introduction to Project Finance Modeling](https://pivotal180.com/course-type/introduction-project-finance-modeling/)

[Financial Modeling Fundamentals](https://pivotal180.com/course-type/financial-modeling-fundamentals/) 

[Tax Equity & Hybrid Financial Modeling](https://pivotal180.com/course-type/tax-equity-hybrid-financial-modeling/)

Have questions? Reach out anytime at [\[email protected\]](https://pivotal180.com/cdn-cgi/l/email-protection) 

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fdate-functions-and-timelines-video%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fdate-functions-and-timelines-video%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fdate-functions-and-timelines-video%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#95aaf7faf1eca8fde1e1e5e6b0a6d4b0a7d3b0a7d3e5fce3fae1f4f9a4ada5bbf6faf8b0a7d3f1f4e1f0b8f3e0fbf6e1fcfafbe6b8f4fbf1b8e1fcf8f0f9fcfbf0e6b8e3fcf1f0fab0a7d3)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Haydn Palliser

[https://www.linkedin.com/in/haydnpalliser/](https://www.linkedin.com/in/haydnpalliser/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/date-functions-and-timelines-video/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA