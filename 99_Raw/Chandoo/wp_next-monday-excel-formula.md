# When is the next Monday? [Homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/next-monday-excel-formula

---

When is the next Monday? \[Homework\]
=====================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 31 comments

  

![Calculate next Monday in Excel](https://chandoo.org/wp/wp-content/uploads/2018/08/next-monday-formula-excel.png)  
Psst. Hey you, yeah, you there… have time for a quick date? A date with Excel that is.

If so, take up this homework problem and post your answers in comments.

Assuming you have an input date in cell A1,

*   What is the formula for finding next Monday?
*   What is the formula for finding first Monday of next month?

Note: If _i__nput date_ is a Monday, you need to calculate the **next** one.

Post your answers in comments

Need a clue? Check out [Excel Date & Time concepts](https://chandoo.org/wp/date-time-tips-ms-excel/)
.

**Want additional challenge?**

Try to solve the problem using either Power Pivot or Power Query. In both cases, assume your input is called \[input date\] or #”input date”

Go ahead and post your answers. Your date is waiting…

Craving for more?  [Other Excel homework problems for you](https://chandoo.org/wp/tag/homework/)
.

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
| Written by Chandoo  <br>Tags: [date and time](https://chandoo.org/wp/tag/date-and-time/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 31 Responses to “When is the next Monday? \[Homework\]”

1.  ![](https://secure.gravatar.com/avatar/209e7451ce1024aeaa3d6bd9bdd83dd16a2da89940e8e35067d9f9e488e47577?s=64&d=mm&r=g) [roberto mensa](https://sites.google.com/site/e90e50charts/)
     says:
    
    [August 31, 2018 at 10:22 am](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571810)
    
    next Monday:  
    \=A1+7-MOD(A1-2,7)  
    first Monday of next month:  
    \=DATE(YEAR(A1),MONTH(A1)+1,0)+7-MOD(DATE(YEAR(A1),MONTH(A1)+1,-2),7)
    
    ciao  
    r
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571810)
    
    *   ![](https://secure.gravatar.com/avatar/773c67d37cbeb61567dc190074df93d35664f54df39f2801ef06725c832fd3a5?s=64&d=mm&r=g) Pavel says:
        
        [August 31, 2018 at 12:08 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571833)
        
        I don’t like using function MOD in date calculation, I prefer WEEKDAY but philosophy is same.  
        Nest Monday:  
        \=A1+7- WEEKDAY(A1-2,3)  
        first Monday of next month:  
        \=DATE(YEAR(A1),MONTH(A1)+1,0)+7-WEEKDAY(DATE(YEAR(A1),MONTH(A1)+1,0),12)
        
        [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571833)
        
2.  ![](https://secure.gravatar.com/avatar/4154eb7d3c696bae9f5ee99c27224915b55c61da74c33384290e1273b8394ed4?s=64&d=mm&r=g) Jozef Melichar says:
    
    [August 31, 2018 at 11:05 am](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571821)
    
    \=A1+(8-WEEKDAY(A1;2))
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571821)
    
3.  ![](https://secure.gravatar.com/avatar/df0b44d7b75149ecb0ea0fe964e98cf037d378927602c7ff818a764e9794e463?s=64&d=mm&r=g) TheQ47 says:
    
    [August 31, 2018 at 1:20 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571847)
    
    For next Monday:  
    \=IF(A1+2-WEEKDAY(A1)+(1-(2>=WEEKDAY(A1)))\*7=A1,A1+7,A1+2-WEEKDAY(A1)+(1-(2>=WEEKDAY(A1)))\*7)
    
    and for First Monday of Next Month:  
    \=DATE(YEAR(A1),MONTH(A1)+1,3)-WEEKDAY(DATE(YEAR(A1),MONTH(A1)+1,1))+(1-(2>=WEEKDAY(DATE(YEAR(A1),MONTH(A1)+1,1))))\*7
    
    Those formulas above mine are easier and shorter, though. Goes to show how when you get stuck into working on a formula, you can sometimes work too hard and get too complicated.
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571847)
    
4.  ![](https://secure.gravatar.com/avatar/d4a39a29ba251034f960a5e17b104a974f23ec9d9afdf2dc5ae6b92b3081e062?s=64&d=mm&r=g) Chihiro says:
    
    [August 31, 2018 at 2:01 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571854)
    
    I do this in several ways when using PowerQuery/PowerPivot
    
    1 Using SQL/Native query  
    TSQL - Replace getdate() with relevant column  
    Next Monday  
    Select dateadd(week, datediff(week, 0, getdate()), 7)
    
    First Monday Next Month  
    SELECT dateadd(week,datediff(week,0,dateadd(day, 6 - datepart(day, dateadd(month, 1, getdate())), dateadd(month, 1, getdate()))), 0)
    
    2 Using M  
    Next Monday  
    \=Date.AddWeeks(Date.StartOfWeek(\[Input date\],1), 1)
    
    First Monday Next Month  
    \=Date.AddWeeks(Date.StartOfWeek(Date.AddMonths(#date(Date.Year(\[Input date\]),Date.Month(\[Input date\]),1),1)-#duration(1,0,0,0),1),1)
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571854)
    
5.  ![](https://secure.gravatar.com/avatar/d4a39a29ba251034f960a5e17b104a974f23ec9d9afdf2dc5ae6b92b3081e062?s=64&d=mm&r=g) Chihiro says:
    
    [August 31, 2018 at 2:11 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571857)
    
    Oh, and in DAX, I never use it. As I almost always have date dimension table in the model. But it would be pretty much same as Excel version.
    
    Ex: Next Monday  
    \=\[Input date\]+(8-WEEKDAY(\[Input date\],2))
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571857)
    
6.  ![](https://secure.gravatar.com/avatar/3d59f57da241ec5207f04f5df6ca5eb519a6bc98a18650c89e3c07dbbef68b64?s=64&d=mm&r=g) Brian says:
    
    [August 31, 2018 at 6:57 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571904)
    
    Next Monday:
    
    \=CHOOSE(WEEKDAY(A1),A1+1,A1+7,A1+6,A1+5,A1+4,A1+3,A1+2)
    
    Next Month 1st Monday:
    
    \=CHOOSE(WEEKDAY(DATEVALUE(MONTH(A1)+1&"/1/"&YEAR(A1))),DATEVALUE(MONTH(A1)+1&"/1/"&YEAR(A1))+1,DATEVALUE(MONTH(A1)+1&"/1/"&YEAR(A1)),DATEVALUE(MONTH(A1)+1&"/1/"&YEAR(A1))+6,DATEVALUE(MONTH(A1)+1&"/1/"&YEAR(A1))+5,DATEVALUE(MONTH(A1)+1&"/1/"&YEAR(A1))+4,DATEVALUE(MONTH(A1)+1&"/1/"&YEAR(A1))+3,DATEVALUE(MONTH(A1)+1&"/1/"&YEAR(A1))+2)
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571904)
    
7.  ![](https://secure.gravatar.com/avatar/aa9b2beaccef8d5f84bbce40aae5a85473176fd40da7a8c4068db650e2d841b1?s=64&d=mm&r=g) Chander Joshi says:
    
    [August 31, 2018 at 7:16 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571911)
    
    If reference date is in Cell A1
    
    Next Week's Monday =A1+9-WEEKDAY(A1)
    
    Next Month's Monday =EOMONTH(A1,1)+9-WEEKDAY(EOMONTH(A1,1))
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571911)
    
8.  ![](https://secure.gravatar.com/avatar/74a43f5a2491b706609180d3059d0b4269b25d859801497ec0d248fe75f37ac4?s=64&d=mm&r=g) Haz says:
    
    [August 31, 2018 at 8:13 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571924)
    
    Next Monday:  
    \=A1+7-WEEKDAY(A1,3)
    
    First Monday of next month:  
    \=EOMONTH(A1,0)+7-WEEKDAY(EOMONTH(A1,0),3)
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571924)
    
9.  ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
    
    [August 31, 2018 at 8:42 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571930)
    
    Next Monday: =WORKDAY.INTL(A1,1,"0111111")
    
    First Monday of next month: =WORKDAY.INTL(EOMONTH(A1,0),1,"0111111")
    
    The 0111111 string tells WORKDAY.INTL to treat every day except Monday as a weekend -- i.e. not a workday -- so that it can find the date that is 1 workday after the date in A1. And EOMONTH does it's normal job of returning the last day of the A1 month to use as the starting point in searching for the next Monday (first Monday of the following month).
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571930)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [August 31, 2018 at 9:35 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571940)
        
        Genius ....
        
        [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571940)
        
    *   ![](https://secure.gravatar.com/avatar/84ba46f1f80bd9f39b5a9ba1c8b02a84860226ab5d77c639eb6c93b1f4dac8b4?s=64&d=mm&r=g) [MF](http://wmfexcel.com/)
         says:
        
        [September 1, 2018 at 8:06 am](https://chandoo.org/wp/next-monday-excel-formula/#comment-1572040)
        
        Nice use of WORKDAY.INTL for solving this problem!
        
        I believe many users are not aware of the existence and usage of it, and its brother - NETWORKDAY.INTL which I have a blogpost about it:  
        [https://wmfexcel.com/2016/02/06/calculate-number-of-day-in-a-given-period/](https://wmfexcel.com/2016/02/06/calculate-number-of-day-in-a-given-period/)
        
        Remind that these functions are for Excel 2010 or later versions though.
        
        [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1572040)
        
10.  ![](https://secure.gravatar.com/avatar/e7b2ae5fa073846c5bde28e4a5a853f99a7815346671c6420e6690e5804eadd1?s=64&d=mm&r=g) Roderick O says:
    
    [September 1, 2018 at 12:53 am](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571967)
    
    Next Monday  
    \=A1+7-WEEKDAY(A1,12)
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571967)
    
11.  ![](https://secure.gravatar.com/avatar/7925142fcc14b1ac77ad6fdb6159e92136f4b9641fb2877a1a80a9116de1345c?s=64&d=mm&r=g) Mandeep says:
    
    [September 1, 2018 at 1:51 am](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571974)
    
    for next monday  
    \=A1+ CHOOSE(WEEKDAY(A1, 2), 7,6,5,4,3,2,1)
    
    for 1st Monday next month  
    \=DATE(YEAR(A1),MONTH(A1)+1,1+1\*7)-WEEKDAY(DATE(YEAR(A1),MONTH(A1)+1,8-2))
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571974)
    
12.  ![](https://secure.gravatar.com/avatar/b3bc1ac59881f0ec6844932e136e419fc2f9172f557878c7472b5aafdc7bc073?s=64&d=mm&r=g) Chris says:
    
    [September 1, 2018 at 3:31 am](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571991)
    
    \=IF(WEEKDAY(A2)=1,A2+1,A2+9-WEEKDAY(A2))
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571991)
    
13.  ![](https://secure.gravatar.com/avatar/62aaebe784659bb6ef9ba0fae856f4b2d1d7007257653ecf00513309e1851407?s=64&d=mm&r=g) Amit Jalan says:
    
    [September 1, 2018 at 3:43 am](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571994)
    
    For Next Monday:  
    \=IF(WEEKDAY(A1)=1,A1+1,A1+9-WEEKDAY(A1))
    
    For First Monday of next Month  
    \=IF(WEEKDAY(EOMONTH(A1,0))=1,EOMONTH(A1,0)+1,EOMONTH(A1,0)+9-WEEKDAY(EOMONTH(A1,0)))
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1571994)
    
14.  ![](https://secure.gravatar.com/avatar/b78a9d9d3099642b3fc80d27343da0b4cc2a0a452f9a260f56cdcd72cb0ab553?s=64&d=mm&r=g) ankur murarka says:
    
    [September 1, 2018 at 7:33 am](https://chandoo.org/wp/next-monday-excel-formula/#comment-1572031)
    
    current cell containing date + 9 - weekdays( currrent cell containing date)
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1572031)
    
15.  ![](https://secure.gravatar.com/avatar/7c8afb3834d2a2ec3fef30e397f74a645d44816c9d2ef938945ab6b96336a18e?s=64&d=mm&r=g) Brian says:
    
    [September 1, 2018 at 2:56 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1572128)
    
    I supply a date from the week in cell A2, such as 9/2/18. It could in fact be any date from this week.
    
    In cell B2, I enter: =a2-weekday(a2)+2. This will calculate the date for Monday of the week in question.
    
    If you need additional Mondays, use the result in cell B2 and add 7.
    
    I use this method to generate a two-week record keeping calendar. Works like a charm.
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1572128)
    
16.  ![](https://secure.gravatar.com/avatar/1ca16f2abe1fea72877bdf7f93a5c601e356fcfabc3f06e432ddf5a6d48af294?s=64&d=mm&r=g) Rob says:
    
    [September 1, 2018 at 9:08 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1572193)
    
    I seem to have gone a little more complicated than some but this is my effort.
    
    Next Monday  
    \=IF(WEEKDAY(A1,1)=1,A1+1,A1+(9-WEEKDAY(A1,1)))
    
    For first Monday  
    \=IF(WEEKDAY(EOMONTH(A1,0),1)=1,EOMONTH(A1,0)+1,A1+(9-WEEKDAY(EOMONTH(A1,0),1)))
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1572193)
    
17.  ![](https://secure.gravatar.com/avatar/460be5157a8ff55b9ffdf755dce4658a7d42130b5bda58c43f07368eb6088d00?s=64&d=mm&r=g) Daniel N says:
    
    [September 3, 2018 at 9:12 am](https://chandoo.org/wp/next-monday-excel-formula/#comment-1572559)
    
    First Monday of next month:
    
    {=DATE(YEAR(A1),MONTH(A1)+1,SUM({1;2;3;4;5;6;7}\*(WEEKDAY(DATE(YEAR(A1),MONTH(A1)+1,{1;2;3;4;5;6;7}),2)=1)))}
    
    Horrible... no doubt, but it works 😉
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1572559)
    
18.  ![](https://secure.gravatar.com/avatar/a233e91ab328f13086b5a311ffa9d10010ddcf92af4efa8a9eacaaf53db407b6?s=64&d=mm&r=g) miaousse says:
    
    [September 3, 2018 at 3:19 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1572614)
    
    for first monday  
    \=A1+CHOOSE(Weekday(A1);1;7;6;5;4;3;2)  
    for frst monday the month after  
    \=EOMONTH(A1;0)+1+CHOOSE(WEEKDAY(EOMONTH(A1;0)+1);1;0;6;5;4;3;2)
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1572614)
    
19.  ![](https://secure.gravatar.com/avatar/bf089e8bf66610b4a1777ca9b7e638d08ed1c42b4e326cd5f247b1e1f0be68c9?s=64&d=mm&r=g) sezer says:
    
    [September 17, 2018 at 1:27 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1575982)
    
    \=IF(WEEKDAY(EOMONTH(A1;0)+1;2)=1;EOMONTH(A1;0)+1;EOMONTH(A1;0)+1+8-WEEKDAY(EOMONTH(A1;0)+1;2))
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1575982)
    
20.  ![](https://secure.gravatar.com/avatar/16fd50a15922676dcb3511a397c87c2c2fd8e11176d8aa058a3e847bdf7dab2f?s=64&d=mm&r=g) Robert H. Gascon says:
    
    [September 18, 2018 at 5:23 am](https://chandoo.org/wp/next-monday-excel-formula/#comment-1576102)
    
    Next Monday: =A1+7-WEEKDAY(A1+7-2)  
    The 7 means Next while the 2 means Monday. So, this formula means Next Week - Weekday of Adjusted Next Week.
    
    First Monday of Next Month: =EOMONTH(A1,0)+1+7-WEEKDAY(EOMONTH(A1,0)+1-2)  
    The foregoing formula uses the same logic as the first. So, this formula means One Week after the First Day of Next Month - Weekday of the Adjusted First Day of Next Month.
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1576102)
    
    *   ![](https://secure.gravatar.com/avatar/c7db5b0f3d9a0799a97109f1f51c0416751e3421c7ea6f963e0072ccf811bccd?s=64&d=mm&r=g) Peter Bartholomew says:
        
        [September 21, 2018 at 9:31 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1576733)
        
        Robert  
        One of the shorted formulas but why the +7 in the WEEKDAY parameter?  
        I tried your formula with my use of Names
        
        \= Input\_Date + 7 - WEEKDAY(Input\_Date - wd)  
        and  
        \= first + 7 - WEEKDAY(first - wd)
        
        [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1576733)
        
21.  ![](https://secure.gravatar.com/avatar/c7db5b0f3d9a0799a97109f1f51c0416751e3421c7ea6f963e0072ccf811bccd?s=64&d=mm&r=g) Peter B says:
    
    [September 21, 2018 at 9:18 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1576732)
    
    \= CEILING( Input\_Date - wd, 7 ) + wd  
    (where wd=2 gives Mondays)
    
    Similarly  
    \= CEILING( first-wd, 7 ) + wd  
    where 'first' is a named formula  
    \= EOMONTH( +Input\_Date, 0) + 1
    
    Note: The + is needed in front of the date parameter to ensure the formula still works if Input\_Data became an array.
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1576732)
    
22.  ![](https://secure.gravatar.com/avatar/e49883fd0c018329c6eb9bdbbe0126f121dd89419c9f692ca70045cd5a9f6b10?s=64&d=mm&r=g) Quadri Adebayo says:
    
    [October 9, 2018 at 10:23 am](https://chandoo.org/wp/next-monday-excel-formula/#comment-1579959)
    
    \=DATE(YEAR(J11),MONTH(J11),WEEKDAY(DATE(YEAR(J11),MONTH(J11),DAY(J11)),1)+6)
    
    \=EOMONTH(J11,0)+1
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1579959)
    
23.  ![](https://secure.gravatar.com/avatar/8337f15d2dffbce0931a72e25dd82fc9e492b733e8a11f761f02ddab7e97c960?s=64&d=mm&r=g) Meagan says:
    
    [November 19, 2018 at 4:58 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1592631)
    
    Late to the party, but...
    
    Next Monday:  
    \=InputDate+CHOOSE(WEEKDAY(InputDate,2),7,6,5,4,3,2,1)
    
    First Monday Next Month:  
    \=EOMONTH(InputDate,0)+CHOOSE(WEEKDAY(EOMONTH(InputDate,0),2),7,6,5,4,3,2,1)
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1592631)
    
24.  ![](https://secure.gravatar.com/avatar/123f3d2c34fd63c3e7871187937f8edabf94ec991ca702bfef1c094471ff5186?s=64&d=mm&r=g) Eduardo says:
    
    [May 16, 2019 at 7:41 am](https://chandoo.org/wp/next-monday-excel-formula/#comment-1647611)
    
    I created a list with the months and their number... (January-1, February-2, and put at the number the name of the month, the next was...
    
    F3= "The month"  
    \=VLOOKUP(IF(INDIREC(F3,0)+1>12,INDIRECTO(F3,0)-11,INDIRECTO(F3,0)+1),$J$2:$K$13,2,0)
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1647611)
    
    *   ![](https://secure.gravatar.com/avatar/123f3d2c34fd63c3e7871187937f8edabf94ec991ca702bfef1c094471ff5186?s=64&d=mm&r=g) Eduardo says:
        
        [May 16, 2019 at 8:17 am](https://chandoo.org/wp/next-monday-excel-formula/#comment-1647614)
        
        sorry I had a little mistake...
        
        For the next Monday in the next month:  
        F8=The first date
        
        \=SI(MONTH(DATE(YEAR(F8),MONTH(F8),DAY(F8)+28))=MONTH(F8),DATE(YEAR(F8),MONTH(F8),DAY(F8)+35),DATE(YEAR(F8),MONTH(F8),DAY(F8)+28))
        
        [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1647614)
        
25.  ![](https://secure.gravatar.com/avatar/028603cbef419d81fa9417afa4d8bbc9fc1bb9f0ef4de5d0ef4cb5349b6e6031?s=64&d=mm&r=g) SG Kenny says:
    
    [November 15, 2019 at 2:45 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1713285)
    
    Next Monday: =B3-WEEKDAY(B3,2)+8
    
    First Monday of next month: =EOMONTH(B3,0)+1+MOD(SUM(7-WEEKDAY(EOMONTH(B3,0)+1,3)),7)
    
    [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1713285)
    
    *   ![](https://secure.gravatar.com/avatar/028603cbef419d81fa9417afa4d8bbc9fc1bb9f0ef4de5d0ef4cb5349b6e6031?s=64&d=mm&r=g) SG Kenny says:
        
        [November 15, 2019 at 2:47 pm](https://chandoo.org/wp/next-monday-excel-formula/#comment-1713286)
        
        Sorry, B3 should say A1 (it was just the way my sheet was set up to work this out!)
        
        [Reply](https://chandoo.org/wp/next-monday-excel-formula/#comment-1713286)
        

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/next-monday-excel-formula/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Performing Maths in Microsoft Word (In an Excel Blog)](https://chandoo.org/wp/performing-maths-in-microsoft-word-in-an-excel-blog/) | [5 tips: Power Query for Accountants (and finance people) – Free Masterclass](https://chandoo.org/wp/power-query-tips-for-accountants/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)