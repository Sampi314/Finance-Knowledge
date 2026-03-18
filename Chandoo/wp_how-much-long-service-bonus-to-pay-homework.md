# How much long service bonus to pay? [Homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework

---

How much long service bonus to pay? \[Homework\]
================================================

[Formula Challenges](https://chandoo.org/wp/category/formula-challenges/)
 - 22 comments

  

‘Tis Friday and it is too hot in my home office to stand and type a longish post. So, let’s keep this skirtish (short and pretty).

**How would you calculate long service bonus?**

Let’s say you are HR manager at BigLargeInc. and you are looking at Julia’s service details. You have her employment start date, current date, her leave without pay details, as shown below.

![](https://chandoo.org/wp/wp-content/uploads/2017/12/long-service-bonus-how-to.png)

You need to _**calculate how many days of continuous service Julia has**_ (ie total service – duration on leave without pay). How would you write the formula?

Assume cell references as shown in the picture above.

Please post your answers in comments.

**Bonus question?** Think Julia’s troubles are nothing? Then come up with formulas to tell how many years and months of long service Julia had. Assume each year has 365.25 days and 12 months in it.

Answers for the example above:

For the above data, you should get below answers

*   Continuous service days: 4,870
*   Continuous service in years and months: 13 years and 4 months

**Go ahead and post your formulas in comments**. Julia is waiting for her bonus.

![Chandoo](https://chandoo.org/wp/wp-content/uploads/2018/05/chandoo-profile-pic.png)

**Hello Awesome...**

My name is Chandoo. Thanks for dropping by. My mission is to make you awesome in Excel & your work. I live in Wellington, New Zealand. When I am not F9ing my formulas, I cycle, cook or play lego with my kids. Know more [about me](https://chandoo.org/wp/about/)
.

I hope you enjoyed this article. Visit [Excel for Beginner](https://chandoo.org/wp/excel-basics/)
 or [Advanced Excel](https://chandoo.org/wp/advanced-excel-skills/)
 pages to learn more or join my [online video class to master Excel](https://chandoo.org/wp/excel-school-program/)
.

Thank you and see you around.

### Related articles:

|     |     |
| --- | --- |
| Written by Chandoo  <br>Tags: [date and time](https://chandoo.org/wp/tag/date-and-time/)<br>, [Excel for HR](https://chandoo.org/wp/tag/excel-for-hr/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [HR](https://chandoo.org/wp/tag/hr/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 22 Responses to “How much long service bonus to pay? \[Homework\]”

1.  ![](https://secure.gravatar.com/avatar/5449b53bd0f2052ebca5e7eed4275fda68f9dad9744205792f21a817b1e73d28?s=64&d=mm&r=g) FirstTimePoster says:
    
    [December 8, 2017 at 3:02 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526765)
    
    Days:  
    \=(C4-C3)-(C8-C7)
    
    Years and Months  
    \=INT(((C4-C3)-(C8-C7))/365.25) & " Years " & ((MOD(((C4-C3)-(C8-C7)),365.25)/365.25)\*12) & " Months"
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526765)
    
    *   ![](https://secure.gravatar.com/avatar/07f5b1a0f2b5f3e6f43629c526f6959da5f33e22f51997fe272b87bad73d421f?s=64&d=mm&r=g) Khurram Shahzad says:
        
        [January 25, 2018 at 8:01 am](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1533391)
        
        Continuous Service Days-I:  
        \=DATEDIF(D4,D5,"D")-DATEDIF(D10,D11,"D")
        
        Continuous Service Days-II:  
        \=DATEDIF(D4,D5,"Y")& " years "&DATEDIF(D4,D5,"YM")-DATEDIF(D10,D11,"YM")&" months"
        
        [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1533391)
        
2.  ![](https://secure.gravatar.com/avatar/cc7e0246051303bdfc29dc4d2aaedeb3cd6eb4b40681204eef72311fa83a5be3?s=64&d=mm&r=g) Toichat says:
    
    [December 8, 2017 at 4:54 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526772)
    
    In C10, Days = "=DATEDIF(C2,C3,"d")-DATEDIF(C6,C7,"d")"  
    In C11, Years = "=TRUNC(C10/365.25)"  
    In C12, Months = "=TRUNC(MOD(C10,365.25)/(365.25/12))"
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526772)
    
    *   ![](https://secure.gravatar.com/avatar/cc7e0246051303bdfc29dc4d2aaedeb3cd6eb4b40681204eef72311fa83a5be3?s=64&d=mm&r=g) Toichat says:
        
        [December 8, 2017 at 4:56 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526773)
        
        Just noticed that I set my sheet up slightly differently to the post. C10 should read "=DATEDIF(C3,C4,"d")-DATEDIF(C7,C8,"d")"
        
        [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526773)
        
3.  ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [December 8, 2017 at 5:02 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526774)
    
    @FirstTimePoster,  
    To my opinion - the Months calculation part can be shorten to:  
    \=(MOD(((C4-C3)-(C8-C7))/365.25,1)\*12)  
    Micky
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526774)
    
    *   ![](https://secure.gravatar.com/avatar/ea7798229ab47b87a09f4f80ae5061a229bb4b685a686ffafe7b3912485edc32?s=64&d=mm&r=g) FrankT says:
        
        [December 9, 2017 at 6:40 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526890)
        
        FirstTimePoster: 13 years and 4 months  
        Michael: 13 years and 4.00000000000001 months
        
        [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526890)
        
4.  ![](https://secure.gravatar.com/avatar/df3ee467ec673d1ed4c4b5240699825be1e6999c11b96933317b4e32efdba3f3?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [December 8, 2017 at 6:59 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526779)
    
    and with some arithmetic manipulation:  
    \=MOD((C4-C3-C8+C7)/365.25,1)\*12  
    Micky
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526779)
    
5.  ![](https://secure.gravatar.com/avatar/b58f660d8fbf6dba9c536b1fda39c88cf9aa3dd0c8e84ba298f0dea21cae2414?s=64&d=mm&r=g) Prem Singh says:
    
    [December 9, 2017 at 4:32 am](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526830)
    
    I think this function works well.  
    \=DATEDIF(B1,B2,"d")-DATEDIF(B4,B5,"d")
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526830)
    
6.  ![](https://secure.gravatar.com/avatar/ce7106cfd406deda8e930395f2500f4f475abf9d52cd3e0b31cc8d7a998ec803?s=64&d=mm&r=g) GraH says:
    
    [December 9, 2017 at 2:40 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526876)
    
    \=DATEDIF(C2,C3,"d")-DATEDIF(C7,C8,"d")  
    or =C7-C2+C3-C8  
    or =ROWS(INDIRECT(C2&":"&C3,TRUE))-ROWS(INDIRECT(C7&":"&C8,TRUE))  
    \=DATEDIF(C2,C3,"y")-DATEDIF(C7,C8,"y")& " years and "&DATEDIF(C2,C3,"ym")-DATEDIF(C7,C8,"ym")&" months"  
    or  
    \=INT(YEARFRAC(C2,C3,1)-YEARFRAC(C7,C8,1))&" Years and "&ROUND(MOD(YEARFRAC(C2,C3,1)-YEARFRAC(C7,C8,1),1)\*12,0)&" Months"
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526876)
    
7.  ![](https://secure.gravatar.com/avatar/ea7798229ab47b87a09f4f80ae5061a229bb4b685a686ffafe7b3912485edc32?s=64&d=mm&r=g) FrankT says:
    
    [December 9, 2017 at 6:25 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526889)
    
    B12=C4-C3-(C8-C7)  
    B13=DATEDIF(1,B12,"Y") & " years and " & DATEDIF(1,B12,"YM") & " months"
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526889)
    
8.  ![](https://secure.gravatar.com/avatar/8bdc85fdf6686c06062cba11232f1b38b4e26bc99d1f911f4cfda558a0e515d8?s=64&d=mm&r=g) Jules says:
    
    [December 9, 2017 at 8:03 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526895)
    
    To acquire the service days in B12 I used \[ =DAYS(C4,C3)-DAYS(C8,C7) \]
    
    Then to convert the answer in B12 into years, months and days I used -  
    \[ =DATEDIF(0,B12,"y")&" years "&DATEDIF(0,B12,"ym")&" months "&DATEDIF(0,B12,"md")&" days" \]
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526895)
    
9.  ![](https://secure.gravatar.com/avatar/62aaebe784659bb6ef9ba0fae856f4b2d1d7007257653ecf00513309e1851407?s=64&d=mm&r=g) Amit Jalan says:
    
    [December 10, 2017 at 7:39 am](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526931)
    
    Continuous Service Days  
    \=((C4-C3)-(C8-C7))
    
    Continous Service Year & Month  
    \=DATEDIF(C3,C4,"Y")-DATEDIF(C7,C8,"Y")&" Years "&TEXT(MOD(((C4-C3)-(C8-C7))/365.25,1)\*12,"#")&" Months"
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526931)
    
10.  ![](https://secure.gravatar.com/avatar/86016301c6bcd142167389d1a9930a6c24e63e68d0361d321851c22e3c0fcee1?s=64&d=mm&r=g) anil says:
    
    [December 10, 2017 at 2:10 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526975)
    
    pl rephrase the question-as "total service – duration on leave without pay" should not be called continuos service-as I understand she worked continuosly for 1157 days and ,after unpaid leave, for 3713 days-pl clarify what is required
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1526975)
    
11.  ![](https://secure.gravatar.com/avatar/379e46dbd3095aae6ba1c5cdcaa798775f9f75068ea9b5535cb7e551eef9f274?s=64&d=mm&r=g) John O says:
    
    [December 11, 2017 at 6:49 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1527149)
    
    Continuous Days: =(C4-C3)-(C8-C7)
    
    I agree with Anil above..."continuous days" means something different than the definition given. That, and I distrust most HR departments. 🙂
    
    In Years and Months: This will be a break from the DATEDIF function I see above. Nothing wrong with DATEDIF, I just did things differently:  
    \=QUOTIENT(B12,365.25)&" years and "&QUOTIENT(MOD(B12,365.25),365.25/12)&" months"
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1527149)
    
12.  ![](https://secure.gravatar.com/avatar/ca9ea90a49dd1c83ffff2d59b732a924e96021df7c5611d77a7cd7c080b75065?s=64&d=mm&r=g) Ola says:
    
    [December 12, 2017 at 2:59 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1527299)
    
    Days: =C7-C3+C4-C8 (result in cell G8)  
    Years and months: =ROUNDDOWN(G8/365,25;0)&" years and "&ROUND((G8/365,25-G9)\*12;0)&" months"  
    Result: 13 years and 4 months
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1527299)
    
13.  ![](https://secure.gravatar.com/avatar/58c24a17970395d1d1164b4d1407b8896d5948183740d626a4cc213b6a3b9678?s=64&d=mm&r=g) Nitin Verma says:
    
    [December 12, 2017 at 3:29 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1527304)
    
    Simple pattern for plus and minus and datedif for year and month
    
    \=A4-A3-(A8-A7) =>4870
    
    \=DATEDIF(1,(A4-A3-(A8-A7)),"Y")&" Years "&DATEDIF(1,(A4-A3-(A8-A7)),"YM")&" Months" =>13 Years 4 Months
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1527304)
    
14.  ![](https://secure.gravatar.com/avatar/2f2a95577dbf41182e822b6000d74e31c80f7f9d64492599869e8ad1a56cb3f9?s=64&d=mm&r=g) [Sahil](http://indexrotator.com/)
     says:
    
    [December 14, 2017 at 1:26 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1527579)
    
    Thanks, I will bookmark it and try it when I get back 😉
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1527579)
    
15.  ![](https://secure.gravatar.com/avatar/c7db5b0f3d9a0799a97109f1f51c0416751e3421c7ea6f963e0072ccf811bccd?s=64&d=mm&r=g) Peter B says:
    
    [December 20, 2017 at 2:18 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1528729)
    
    I would first calculate the Julias's days of service (ServiceDays) as  
    \= (CurrentDate - EmploymentStart + 1) - (LeaveEnd - LeaveStart + 1)  
    Complete years service would be  
    \= FLOOR( ServiceDays, DaysPerYear ) / DaysPerYear  
    with a balance of days (AdditionalDays)  
    \= MOD( ServiceDays, DaysPerYear )  
    To avoid clutter that could be a Named formula.  
    The additional days equate to completed months  
    \= FLOOR( AdditionalDays, DaysPerMonth ) / DaysPerMonth  
    where DaysPerMonth is given by  
    \= DaysPerYear / MonthsPerYear
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1528729)
    
16.  ![](https://secure.gravatar.com/avatar/a96812162ecaadcfd666346bace7214aac1bfd61457d2a56e38510a4a005560d?s=64&d=mm&r=g) Rishi Kumar says:
    
    [December 27, 2017 at 2:14 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1529756)
    
    \=DAYS(C4,C3)-DAYS(C8,C7)&" Days"
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1529756)
    
17.  ![](https://secure.gravatar.com/avatar/b8314d1e55bd62900c3c35ca28440ce0fd1c6d13ce1ff142a2dfc3d675c40b58?s=64&d=mm&r=g) Jay Krishnam says:
    
    [January 1, 2018 at 2:20 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1530360)
    
    Both (Continuous service days) & (Continuous service in years and months) can be found out by using a single formula DATEDIF
    
    \=DATEDIF("1-1-04","8-12-17","d")-DATEDIF("3-3-07","9-10-07","d") will give 4,870
    
    \=DATEDIF("1-1-04","8-12-17","y")-DATEDIF("3-3-07","9-10-07","y") will give 13
    
    \=DATEDIF("1-1-04","8-12-17","ym")-DATEDIF("3-3-07","9-10-07","ym") will give 4
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1530360)
    
18.  ![](https://secure.gravatar.com/avatar/459d5bb75159124ec2248baef47839b136d7be478e5ac4cb4ebff6bd796d3bb3?s=64&d=mm&r=g) Ajay Jaiswal says:
    
    [January 17, 2018 at 1:52 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1532360)
    
    \=DATEDIF(B1,B2,"y")-DATEDIF(D2,D3,"y")&"years,"&DATEDIF(B1,B2,"Ym")-DATEDIF(D2,D3,"Ym")&"Months"
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1532360)
    
19.  ![](https://secure.gravatar.com/avatar/459d5bb75159124ec2248baef47839b136d7be478e5ac4cb4ebff6bd796d3bb3?s=64&d=mm&r=g) Ajay Jaiswal says:
    
    [January 17, 2018 at 1:54 pm](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1532362)
    
    for days: =DATEDIF(B1,B2,"d")-DATEDIF(D2,D3,"d")
    
    [Reply](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#comment-1532362)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/how-much-long-service-bonus-to-pay-homework/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [5 conditional formatting top tips – Excel basics](https://chandoo.org/wp/conditional-formatting-top-tips/) | [Merry Christmas and Happy New Year 2018 \[Holiday Card\]](https://chandoo.org/wp/holiday-card/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)