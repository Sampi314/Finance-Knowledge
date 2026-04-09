# How many employees are on leave during Easter holidays [Homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework

---

How many employees are on leave during Easter holidays \[Homework\]
===================================================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 37 comments

  

_Easter is around the corner_. After what seemed like weeks of lousy weather, finally the sun shone today. I capitalized on the day by skipping work, walking kids to school, taking Jo out for some shopping, enjoying a leisurely walk / cycling with Nishanth in the park and _almost_ forgetting about the blog. But it is dark now and before tucking the kids in, let me post a short but interesting home work problem.

**Let’s say you are HR manager at Egg Co. and you are looking at the vacation plans of your team.**

Easter is your busiest time and it would be a bummer if a majority of your staff are on leave during the Easter season (14th of April to 28th of April, 2017). So you want to know how many people are on leave. This is how your data (table name: _**lvs**_) looks:

![easter-leaves-problem](https://chandoo.org/wp/wp-content/uploads/2017/04/easter-leaves-problem.png)

[**Click here to download the sample file**](https://chandoo.org/wp/wp-content/uploads/2017/04/employee-leaves.xlsx)
.

You want to answer below three questions:

1.  How many employees are on leave during Easter holidays (14th of April to 28th of April)?
2.  How many employees are on approved vacation during Easter holidays?
3.  How many employees in “Team ninja” are on approved leave during Easter holidays? Assume team employee numbers are in named range _**ninja**_

For first question, assume that any employees whose leave is _pending_ will be approved.

Also, assume that Easter season start & end dates are in cells P4 & P5 respectively.

You can use formulas, pivot tables, power pivot measures, VBA or pixie dust to solve the problem. If using pivot table approach, just explain how you would solve in words. For other methods, please post your solution in the comments.

_**Go ahead and post your questions.**_ 

**Want some hints..?**

What is an Easter themed homework without some clues? So here we go

*   [Between formula in Excel](http://chandoo.org/wp/2010/06/24/between-formula-excel/)
    
*   [Check if your two ranges of dates overlap](http://chandoo.org/wp/2010/06/01/date-overlap-formulas/)
    
*   [Range lookup in Excel](http://chandoo.org/wp/2010/06/30/range-lookup-excel/)
    
*   [Count unique values subject to conditions](http://chandoo.org/wp/2012/07/26/formula-forensics-025/)
    

All the best. The weekend forecast is blue skies and light winds. Finally, we will be checking out walking trials in [Trelissick park](http://www.trelissickpark.org.nz/)
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
| Written by Chandoo  <br>Tags: [between formula](https://chandoo.org/wp/tag/between-formula/)<br>, [challenge](https://chandoo.org/wp/tag/challenge/)<br>, [date and time](https://chandoo.org/wp/tag/date-and-time/)<br>, [excel formulas](https://chandoo.org/wp/tag/excel-formulas/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [logical operators in excel](https://chandoo.org/wp/tag/logical-operators-in-excel/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 37 Responses to “How many employees are on leave during Easter holidays \[Homework\]”

1.  ![](https://secure.gravatar.com/avatar/028d37308327c214a626cd36939a66ce94ee7410dde285bd46f6a22b08102ce6?s=64&d=mm&r=g) [Abhay](http://datalyze.in/)
     says:
    
    [April 7, 2017 at 8:07 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433463)
    
    This is very similar to consecutive leave problem I had. I have posted a video solution here:
    
    [https://www.youtube.com/watch?v=BKa8Bbdhq7I](https://www.youtube.com/watch?v=BKa8Bbdhq7I)
    
    Further, I have also launched a Power Query course here:  
    [https://www.udemy.com/power-query-training-for-excel-2010-2013-2016-powerbi/?ccManual=&couponCode=pqyt80](https://www.udemy.com/power-query-training-for-excel-2010-2013-2016-powerbi/?ccManual=&couponCode=pqyt80)
    
    Have a look and please suggest.
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433463)
    
    *   ![](https://secure.gravatar.com/avatar/d6a3bcdb33cfcd117d3a38f821a279999431e52db067f05a0f7e93c9e499fd24?s=64&d=mm&r=g) Martin says:
        
        [October 26, 2018 at 9:53 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1583882)
        
        Hi Chandoo! I'm resolved Using Pivot Tables and filtering by Dates filtes. I Got:
        
        Q1 = 272 | Q2 = 115 | Q3 = 5
        
        I did 3 pivot tables, the first one Leave Start and Leave end in Rows,  
        Status in columns and Status in values, after that, I only used for Leave Start: Date Filters, Is after and specified is after: 4/13/17 for Leave End, Date filters, is Before 4/29/17 and Booom! the second and third pivot table I only used some filters trick and ready..!
        
        I think than my results are corrects!  
        Regars! From Tijuana Mexico.
        
        [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1583882)
        
2.  ![](https://secure.gravatar.com/avatar/04b5a93edbc655803abe74ca9048a5e604383b69481c0cb5e200048e7b6d86e4?s=64&d=mm&r=g) prashant says:
    
    [April 7, 2017 at 8:27 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433473)
    
    1\. 340=COUNTIFS(lvs\[Leave Start\],">="&$P$3,lvs\[Leave End\],"="&$P$3,lvs\[Leave End\],"="&$P$3,lvs\[Leave End\],"<="&$P$4,lvs\[Status\],"Approved",lvs\[Emp Number\],ninja)
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433473)
    
3.  ![](https://secure.gravatar.com/avatar/98fbd49fb20645dd63ebf7f4dbe170740c4df8a2c16ce15774c807b437088dc2?s=64&d=mm&r=g) Amol says:
    
    [April 7, 2017 at 10:03 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433528)
    
    \=COUNTIFS(lvs\[Leave Start\],">=42839",lvs\[Leave End\],"<=42853")
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433528)
    
4.  ![](https://secure.gravatar.com/avatar/73ae4d4b4c74cb80e037083a485b16d5e543b2602fb033199fd56d77f1276c23?s=64&d=mm&r=g) Suryakant says:
    
    [April 7, 2017 at 10:04 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433530)
    
    1\. Formula for answer to 1 question - COUNTIFS(lvs\[Leave Start\],">=14-04-17",lvs\[Leave End\],"<=28-04-17")+COUNTIFS(lvs\[Leave Start\],"=14-04-17",lvs\[Leave End\],"=14-04-17",lvs\[Leave Start\],"28-04-17")+COUNTIFS(lvs\[Leave Start\],"=28-04-17") = 417
    
    2\. Formula for answer to 2 question -COUNTIFS(lvs\[Leave Start\],">=14-04-17",lvs\[Leave End\],"<=28-04-17",lvs\[Status\],"Approved")+COUNTIFS(lvs\[Leave Start\],"=14-04-17",lvs\[Leave End\],"=14-04-17",lvs\[Leave Start\],"28-04-17",lvs\[Status\],"Approved")+COUNTIFS(lvs\[Leave Start\],"=28-04-17",lvs\[Status\],"Approved") = 293
    
    3.Formula for answer to 3 question - COUNTIFS(lvs\[Leave Start\],">=14-04-17",lvs\[Leave End\],"<=28-04-17",lvs\[Status\],"Approved",lvs\[Emp Number\],ninja)+COUNTIFS(lvs\[Leave Start\],"=14-04-17",lvs\[Leave End\],"=14-04-17",lvs\[Leave Start\],"28-04-17",lvs\[Status\],"Approved",lvs\[Emp Number\],ninja)+COUNTIFS(lvs\[Leave Start\],"=28-04-17",lvs\[Status\],"Approved",lvs\[Emp Number\],ninja) = 2
    
    For every answer there are 4 scenario's:  
    A. Leave START before 14-Apr-17 but ends Between 14-04-17 to 28-04-17.  
    B. Leave START after 14-Apr-17 but ends before 28-04-17.  
    C. Leave START between 14-Apr-17 to 28-04-17 but ends after 14-04-17 to 28-04-17.  
    D. Leave START before 14-Apr-17 but ends after 28-04-17.
    
    Hence, we get above answers..
    
    Hope this is correct thinking..
    
    Suryakant
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433530)
    
    *   ![](https://secure.gravatar.com/avatar/7e4971c3152778fde7ddedad4cb22034f624d5d198c7de681ed43fe2a1d3044f?s=64&d=mm&r=g) Desk Lamp says:
        
        [April 11, 2017 at 10:30 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435725)
        
        Everyone seems to have a different answer!
        
        Let me walk through question 1, using just the autofilter to count numbers:
        
        1\. There are 1044 people with "Approved" Holiday  
        2\. Of which 59 have their holiday starting after 28-04-2017. We exclude all these  
        3\. A further 692 have their holiday ending before 14-04-2017. We exclude all these  
        4\. 1044 - 59 - 692 = 293
        
        5\. Now repeat this process for "Pending" holidays:  
        6\. 151 - 10 - 96 = 45
        
        7\. Add the results for approved and pending gives = 338
        
        It's not pretty but the following formula returns that answer:  
        \=COUNTIFS(lvs\[Status\],"Approved")-  
        COUNTIFS(lvs\[Status\],"Approved",lvs\[Leave End\],""&$P$5)+  
        COUNTIFS(lvs\[Status\],"Pending")-  
        COUNTIFS(lvs\[Status\],"Pending",lvs\[Leave End\],""&$P$5)
        
        [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435725)
        
        *   ![](https://secure.gravatar.com/avatar/7e4971c3152778fde7ddedad4cb22034f624d5d198c7de681ed43fe2a1d3044f?s=64&d=mm&r=g) Desk Lamp says:
            
            [April 11, 2017 at 11:06 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435739)
            
            Ergh, the comments software seems to have chopped out big chunks of my formula! It doesn't seem to like working with less then and greater than symbols.
            
            [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435739)
            
        *   ![](https://secure.gravatar.com/avatar/dcf61b986f27b2a856fba15e6fd276ea47aecc9917932dc03029645125af7f7a?s=64&d=mm&r=g) sunrise06 says:
            
            [April 11, 2017 at 11:26 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435995)
            
            Yes, but there are duplicate Emp Numbers, you have to account for that.
            
            [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435995)
            
5.  ![](https://secure.gravatar.com/avatar/98fbd49fb20645dd63ebf7f4dbe170740c4df8a2c16ce15774c807b437088dc2?s=64&d=mm&r=g) Amol says:
    
    [April 7, 2017 at 11:22 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433546)
    
    For 1st = =COUNTIFS(lvs\[Leave Start\],">=42839",lvs\[Leave End\],"=42839",lvs\[Leave End\],"=42839",lvs\[Leave End\],"<=42853",lvs\[Status\],"Approved",lvs\[Emp Number\],ninja)) = 5
    
    Dear chandoo,  
    Kindly specify if you want the count of leave is starting from 14/04/2017 and ending on or before 28/04/2017.
    
    There is an ambiguity in that question.
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433546)
    
6.  ![](https://secure.gravatar.com/avatar/98fbd49fb20645dd63ebf7f4dbe170740c4df8a2c16ce15774c807b437088dc2?s=64&d=mm&r=g) Amol says:
    
    [April 7, 2017 at 11:24 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433547)
    
    For 1st = =COUNTIFS(lvs\[Leave Start\],">=42839",lvs\[Leave End\],"=42839",lvs\[Leave End\],"=42839",lvs\[Leave End\],"<=42853",lvs\[Status\],"Approved",lvs\[Emp Number\],ninja))  
    5
    
    Dear chandoo,  
    Kindly specify if you want the count of leave is starting from 14/04/2017 and ending on or before 28/04/2017.
    
    There is an ambiguity in that question.
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433547)
    
7.  ![](https://secure.gravatar.com/avatar/c9541a3df1830a072f3a957af85e7855b33ad6da4e843e5672118ac8f79bbdfc?s=64&d=mm&r=g) Josh says:
    
    [April 7, 2017 at 2:05 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433582)
    
    Q1 - 408  
    Q2 - 286  
    Q3 - 5
    
    My method:  
    Add two helper columns.  
    Helper 1 "Is Leave During Easter" : =OR(AND(\[@\[Leave Start\]\]>=$Q$4,\[@\[Leave Start\]\]=$Q$4,\[@\[Leave End\]\]<=$Q$5))
    
    Helper 2 "Is Employee on Team Ninja?" : =ISNUMBER(MATCH(\[@\[Emp Number\]\],ninja,0))
    
    Then Insert a Pivot Table, adding the Data to Data Model. Adding to Data Model allows you to get a distinct count instead of a regular count (the questions ask "How many Employees", not "How many leave requests").
    
    Once in a pivot table, you can add filters to isolate leave requests during the holidays, with a distinct count by employee id. Then you can add the filter for Status=Approved. Finally, you can get a distinct count for those on team ninja.
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433582)
    
    *   ![](https://secure.gravatar.com/avatar/c9541a3df1830a072f3a957af85e7855b33ad6da4e843e5672118ac8f79bbdfc?s=64&d=mm&r=g) Josh says:
        
        [April 7, 2017 at 2:07 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433583)
        
        Actually, I take back my response for Q2. I failed to notice that the leave Type must be vacation. The correct answer is 139.
        
        [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1433583)
        
8.  ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
    
    [April 7, 2017 at 11:14 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1434020)
    
    As Josh noticed, the biggest challenge is to avoid counting duplicates, but I'll have to disagree slightly with the results of his formula/pivot work.
    
    Assumptions:  
    1\. Being "on leave" for Q1 means Status is not Cancelled or Declined  
    2\. Unless explicitly stated (e.g. vacation), "leave" means any Leave Type  
    3\. Start and end dates are inclusive (i.e. any leave that ends on April 14 or starts on April 28 is counted as an overlap)
    
    Q1 = 331  
    \=SUMPRODUCT(SIGN(FREQUENCY(lvs\[Emp Number\]\*($P$4<=lvs\[Leave End\])\*(lvs\[Leave Start\]<=$P$5)\*ISNUMBER(MATCH(lvs\[Status\],{"Approved","Pending"},0)),lvs\[Emp Number\])))-1
    
    Q2 = 139  
    \=SUMPRODUCT(SIGN(FREQUENCY(lvs\[Emp Number\]\*($P$4<=lvs\[Leave End\])\*(lvs\[Leave Start\]<=$P$5)\*(lvs\[Status\]="Approved")\*(lvs\[Leave Type\]="Vacation"),lvs\[Emp Number\])))-1
    
    Q3 = 4  
    \=SUMPRODUCT(SIGN(FREQUENCY(lvs\[Emp Number\]\*($P$4<=lvs\[Leave End\])\*(lvs\[Leave Start\]<=$P$5)\*(lvs\[Status\]="Approved")\*ISNUMBER(MATCH(lvs\[Emp Number\],ninja,0)),lvs\[Emp Number\])))-1
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1434020)
    
9.  ![](https://secure.gravatar.com/avatar/36b7c25d166a350fed0d61418f075a8f64c4688662beb9056267fff8550f3bfc?s=64&d=mm&r=g) Sujeet Jaiswal says:
    
    [April 10, 2017 at 9:53 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435135)
    
    1)340  
    2)242  
    3)18
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435135)
    
    *   ![](https://secure.gravatar.com/avatar/36b7c25d166a350fed0d61418f075a8f64c4688662beb9056267fff8550f3bfc?s=64&d=mm&r=g) Sujeet Jaiswal says:
        
        [April 10, 2017 at 9:58 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435138)
        
        3)5 is right answer
        
        [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435138)
        
10.  ![](https://secure.gravatar.com/avatar/36b7c25d166a350fed0d61418f075a8f64c4688662beb9056267fff8550f3bfc?s=64&d=mm&r=g) Sujeet Jaiswal says:
    
    [April 10, 2017 at 10:02 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435139)
    
    I neither used any formula nor pivot table. Solved using Advanced Filter
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435139)
    
11.  ![](https://secure.gravatar.com/avatar/76aa4c980b680608fd155abf355c2b152e5787d94315c6e930579f97a6eac12d?s=64&d=mm&r=g) Nils says:
    
    [April 10, 2017 at 10:58 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435149)
    
    I can't see why the table would look like that from the beginning.
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435149)
    
12.  ![](https://secure.gravatar.com/avatar/42b3dae989688d8365b7571765e3e8f66642bfe9a1ac9d9ea56cafe39d097eb1?s=64&d=mm&r=g) Luís Pires says:
    
    [April 10, 2017 at 2:26 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435173)
    
    Q1) 227  
    Q2) 199  
    Q3) 5
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435173)
    
    *   ![](https://secure.gravatar.com/avatar/42b3dae989688d8365b7571765e3e8f66642bfe9a1ac9d9ea56cafe39d097eb1?s=64&d=mm&r=g) Luís Pires says:
        
        [April 10, 2017 at 2:45 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435178)
        
        Sorry!
        
        New Numbers:  
        Q1) 267  
        Q2) 237  
        Q3) 4
        
        [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435178)
        
13.  ![](https://secure.gravatar.com/avatar/5af2cf5ea39d6b77269224dbdbd7796a932368c799654ea3b1de959d5f0dae15?s=64&d=mm&r=g) Robert says:
    
    [April 11, 2017 at 9:49 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435711)
    
    q1) 338  
    \=SUM(COUNTIFS(lvs\[Leave Start\],"=" &$P$4,lvs\[Status\],{"Approved","Pending"}))+SUM(COUNTIFS(lvs\[Leave Start\],">"&$P$4,lvs\[Leave Start\],"=" &$P$4,lvs\[Leave Start\], "<="&$P$5,lvs\[Leave Type\],"Vacation",lvs\[Status\],"Approved")
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435711)
    
14.  ![](https://secure.gravatar.com/avatar/bfa5735e4168487cf99d14c74eb8759b5393ebdb1092305bd411b05c0bc97a6c?s=64&d=mm&r=g) Ankur, IncomeBoy says:
    
    [April 11, 2017 at 10:51 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435730)
    
    Hi Chandoo, To be honest, i am not really good in Excel, however, this article has given me some insight on how to use it efficiently. You will be glad to know now even I have taught a little bit to my friend. Hope to get a more post from you in the future.  
    Thank you
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435730)
    
15.  ![](https://secure.gravatar.com/avatar/aade450ee4034589d08bca25fdb38fd1dd7b95910f1d52b395c912226f4fe2ca?s=64&d=mm&r=g) jomili says:
    
    [April 11, 2017 at 2:57 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435901)
    
    Wow, there's a lot of different numbers being proposed. Here's the way I looked at it:  
    I made a helper column to take out anything "Declined" or "Cancelled", then to determine if any part of the leave fell within the Easter Holiday Season range. Formula used for this part is:  
    '=IF(AND(\[@Status\]"Declined",\[@Status\]"Cancelled"),MAX(0,MIN($P$5,\[@\[Leave End\]\])-MAX($P$4,\[@\[Leave Start\]\])+1),0)  
    Result is the number of days of leave that fall in the Easter Holiday Season (on leave DURING, not on leave for the ENTIRE Period).  
    Then, for Q1, I simply counted the values in my helper column that were greater than 0:  
    '=COUNTIF(lvs\[helper1\],">0")  
    Result = 338
    
    For Q2 the question is ambiguous, since the assumption is that Pending will be approved, so the answer would be the same as Q1. However, taking it at face value, taking out the Pending and only counting the Approved, my formula is:  
    '=COUNTIFS(lvs\[Status\],"Approved",lvs\[helper1\],">0")  
    Result is 293
    
    Haven't tackled Q3 yet.
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435901)
    
    *   ![](https://secure.gravatar.com/avatar/aade450ee4034589d08bca25fdb38fd1dd7b95910f1d52b395c912226f4fe2ca?s=64&d=mm&r=g) jomili says:
        
        [April 11, 2017 at 3:00 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435902)
        
        Website hosed my Helper formula. Between \[@Status\] and "Cancelled" there should be GreaterThanLessThan symbols.
        
        [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435902)
        
        *   ![](https://secure.gravatar.com/avatar/aade450ee4034589d08bca25fdb38fd1dd7b95910f1d52b395c912226f4fe2ca?s=64&d=mm&r=g) jomili says:
            
            [April 11, 2017 at 5:03 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435941)
            
            Sometimes I amaze myself by what I miss. For Q2, I missed "Vacation". Updated formula (NOT using a Helper Column) is:  
            '=COUNTIFS(lvs\[Leave Start\],"="&P4,lvs\[Status\],"Approved",lvs\[Leave Type\],"Vacation")  
            Result is: 141
            
            Updated formula for Q1 (NOT using Helper) is:  
            '=COUNTIFS(lvs\[Leave Start\],"="&P4,lvs\[Status\],"Pending")+COUNTIFS(lvs\[Leave Start\],"="&P4,lvs\[Status\],"Approved")  
            Result is still: 338
            
            For Q3, the answer without duplicates is 5, but I've yet to come up with a formula solution to arrive at that.
            
            [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435941)
            
            *   ![](https://secure.gravatar.com/avatar/aade450ee4034589d08bca25fdb38fd1dd7b95910f1d52b395c912226f4fe2ca?s=64&d=mm&r=g) jomili says:
                
                [April 11, 2017 at 5:05 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435942)
                
                Grrr.... all the "=" signs in my last post or either Less Than or Equal, or Greater Than or Equal.
                
                [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435942)
                
                *   ![](https://secure.gravatar.com/avatar/aade450ee4034589d08bca25fdb38fd1dd7b95910f1d52b395c912226f4fe2ca?s=64&d=mm&r=g) jomili says:
                    
                    [April 11, 2017 at 5:10 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1435944)
                    
                    I'm tired of my formulas being hosed. LT = Less Than, GT = Greater Than:  
                    '=COUNTIFS(lvs\[Leave Start\],"LT="&P5,lvs\[Leave End\],"GT="&P4,lvs\[Status\],"Approved",lvs\[Leave Type\],"Vacation")
                    
                    '=COUNTIFS(lvs\[Leave Start\],"LT="&P5,lvs\[Leave End\],"GT="&P4,lvs\[Status\],"Pending")+COUNTIFS(lvs\[Leave Start\],"LT="&P5,lvs\[Leave End\],"GT="&P4,lvs\[Status\],"Approved")
                    
16.  ![](https://secure.gravatar.com/avatar/5af2cf5ea39d6b77269224dbdbd7796a932368c799654ea3b1de959d5f0dae15?s=64&d=mm&r=g) Robert says:
    
    [April 12, 2017 at 8:51 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1436087)
    
    For Q2: 141
    
    \=COUNTIFS(lvs\[Leave Start\], ">=" &$P$4,lvs\[Leave Start\], "<="&$P$5,lvs\[Leave Type\],"Vacation",lvs\[Status\],"Approved")+COUNTIFS(lvs\[Leave Start\],"="&$P$4,lvs\[Leave Type\],"Vacation",lvs\[Status\],"Approved")
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1436087)
    
17.  ![](https://secure.gravatar.com/avatar/ad2a6176483f24fd8fb543314cdc253ac72507f8ad41c8bae1d18ca8a85ee5ca?s=64&d=mm&r=g) Pavan Sistla says:
    
    [April 13, 2017 at 2:18 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1437077)
    
    1Q. How many employees are on leave during Easter holidays (14th of April to 28th of April)?  
    Ans: =COUNTIFS(lvs\[\[#All\],\[Status\]\],"Declined",lvs\[\[#All\],\[Status\]\],"Cancelled",lvs\[\[#All\],\[Leave Start\]\],">="&P4,lvs\[\[#All\],\[Leave Start\]\],"<="&P5)
    
    2Q. How many employees are on approved vacation during Easter holidays?  
    Ans: =COUNTIFS(lvs\[\[#All\],\[Leave Type\]\],"Vacation",lvs\[\[#All\],\[Status\]\],"Declined",lvs\[\[#All\],\[Status\]\],"Cancelled",lvs\[\[#All\],\[Status\]\],"pENDING",lvs\[\[#All\],\[Leave Start\]\],">="&P4,lvs\[\[#All\],\[Leave Start\]\],""&P4,lvs\[\[#All\],\[Leave Start\]\],"<="&P5)
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1437077)
    
18.  ![](https://secure.gravatar.com/avatar/ae034148a1cafb014095f61641916832108652449842f3c21380cd9d77fac0ac?s=64&d=mm&r=g) Mamdouh Elfors says:
    
    [April 16, 2017 at 7:53 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1437834)
    
    1 - Formula : COUNTIFS(lvs\[Leave Start\];">="&P4;lvs\[Leave Start\];"="&P4;lvs\[Leave Start\];"="&P4;lvs\[Leave Start\];"="&MIN(ninja);lvs\[Emp Number\];"<="&MAX(ninja);lvs\[Status\];"Approved") answer : 6
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1437834)
    
    *   ![](https://secure.gravatar.com/avatar/aade450ee4034589d08bca25fdb38fd1dd7b95910f1d52b395c912226f4fe2ca?s=64&d=mm&r=g) Jomili says:
        
        [April 17, 2017 at 1:38 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1438089)
        
        Madouh,  
        I can see you got the right answer, but I can't get your formula to work correctly. I converted the semicolons to commas, and the formula calculates, but the result is zero. Did something get left out, or mistyped, in the formula you posted?
        
        [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1438089)
        
19.  ![](https://secure.gravatar.com/avatar/ad2a6176483f24fd8fb543314cdc253ac72507f8ad41c8bae1d18ca8a85ee5ca?s=64&d=mm&r=g) Pavan Sistla says:
    
    [April 16, 2017 at 9:52 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1437862)
    
    Here is the modified and correct result:  
    1) How many employees are on leave during Easter holidays (14th of April to 28th of April)?  
    Ans: Logic used - Counted all the employees are whose leave status is either Approved or Pending and deducted : a) the count of emp whose leave start and end dates are before holiday start (14th Apr) b) the count of emp whose leave start and end dates are after holiday end (28th Apr). This gives 338 which is resultant of 1195-788-69 based on the above logic and the formula is:  
    \=SUM(COUNTIFS(lvs\[\[#All\],\[Status\]\],{"Approved","Pending"}))-SUM(COUNTIFS(lvs\[\[#All\],\[Status\]\],{"Approved","Pending"},lvs\[\[#All\],\[Leave Start\]\],"<"&P4,lvs\[\[#All\],\[Leave End\]\],""&P5,lvs\[\[#All\],\[Leave End\]\],">"&P5)).
    
    2) How many employees are on approved vacation during Easter holidays?  
    Ans: Applying the same logic as explained above we have to count all the employees whose leave status is approved and leave type is vacation and then deduct: "Refer answer section of 1st question".  
    This gives 141 which is resultant of 490-318-31 and the formula is:  
    \=COUNTIFS(lvs\[\[#All\],\[Status\]\],"Approved",lvs\[\[#All\],\[Leave Type\]\],"Vacation")-COUNTIFS(lvs\[\[#All\],\[Status\]\],"Approved",lvs\[\[#All\],\[Leave Type\]\],"Vacation",lvs\[\[#All\],\[Leave Start\]\],"<"&P4,lvs\[\[#All\],\[Leave End\]\],""&P5,lvs\[\[#All\],\[Leave End\]\],">"&P5).
    
    3) How many employees in "Team ninja" are on approved leave during Easter holidays?  
    Ans: Applying the same logic as explained in the above 2 questions, below is the formula.  
    \=SUM(COUNTIFS(lvs\[\[#All\],\[Emp Number\]\],"="&ninja,lvs\[\[#All\],\[Status\]\],"Approved"))-SUM(COUNTIFS(lvs\[\[#All\],\[Emp Number\]\],"="&ninja,lvs\[\[#All\],\[Status\]\],"Approved",lvs\[\[#All\],\[Leave Start\]\],"<"&P4,lvs\[\[#All\],\[Leave End\]\],""&P5,lvs\[\[#All\],\[Leave End\]\],">"&P5))
    
    Though the formula appears lengthy, this is conventional way which matches with the count when cross checked using filter criteria.  
    I would be happy to look easier and tricky way of writing formula from others and especially Chandoo 🙂
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1437862)
    
20.  ![](https://secure.gravatar.com/avatar/998864bea9a37544d4b8334724025ba25f3f6f3ea981a8daded0c3dc2995700f?s=64&d=mm&r=g) Abbas says:
    
    [April 18, 2017 at 11:12 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1438294)
    
    Q1:
    
    FORMULA  
    \=SUM(COUNTIF(Status,{"Approved","Pending"}))  
    \-SUM(COUNTIFS(Status,{"Approved","Pending"},L\_End,""&E\_End))
    
    ANSWER  
    338
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1438294)
    
    *   ![](https://secure.gravatar.com/avatar/998864bea9a37544d4b8334724025ba25f3f6f3ea981a8daded0c3dc2995700f?s=64&d=mm&r=g) Abbas says:
        
        [April 18, 2017 at 11:13 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1438295)
        
        \=SUM(COUNTIF(Status,{"Approved","Pending"}))-SUM(COUNTIFS(Status,{"Approved","Pending"},L\_End,""&E\_End))
        
        [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1438295)
        
21.  ![](https://secure.gravatar.com/avatar/7f7a93adf7e1f2e13508e2eb13408e122885f9011aefca94ae888b2134c61af0?s=64&d=mm&r=g) Brijesh says:
    
    [May 22, 2017 at 7:05 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1452527)
    
    1\. 267  
    2\. 237  
    3\. 4
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1452527)
    
22.  ![](https://secure.gravatar.com/avatar/e3ac7290af128e00cd62b2d0248e4c605cae4a7c6d4e434803496bbd868e6359?s=64&d=mm&r=g) PARTHIV says:
    
    [May 22, 2017 at 9:45 am](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1452566)
    
    267  
    127  
    2
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1452566)
    
23.  ![](https://secure.gravatar.com/avatar/eac56e2ca437f3d28649a89ccf904f910be6a397719e05bae50d9dc95859c02a?s=64&d=mm&r=g) Cristopher says:
    
    [June 9, 2017 at 1:58 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1458220)
    
    Q1: 338  
    Approved or pending  
    Leave starts on or before 28 apr  
    Leave ends on or after 14 apr
    
    \=SUMPRODUCT((lvs\[Leave Start\]=$P$4)\*ISNUMBER(MATCH(lvs\[Status\];{"approved";"pending"};0)))
    
    Q2: 141  
    Approved & type is vacation
    
    \=SUMPRODUCT((lvs\[Leave Start\]=$P$4)\*(lvs\[Status\]="approved")\*(lvs\[Leave Type\]="vacation"))
    
    Q3: 6  
    assuming type of leave doesn't matter
    
    \=SUMPRODUCT((lvs\[Leave Start\]=$P$4)\*(lvs\[Status\]="approved")\*ISNUMBER(MATCH(lvs\[Emp Number\];ninja;0)))
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-1458220)
    
24.  ![](https://secure.gravatar.com/avatar/c92be49672553bf5f22270ce7958e377f91ba25178e01638a07c4e088cff7e0e?s=64&d=mm&r=g) Ricardo says:
    
    [January 2, 2024 at 6:14 pm](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-2161665)
    
    Sorry for the mistakes!!  
    First I have created a table column named Ninja? with this formula:  
    \=SI(ESERROR(BUSCARV(\[@\[Emp Number\]\];ninja;1;FALSO));"N";"S")  
    This tells me whether the employee belongs to Ninja Team.  
    I've only used the sumproduct function filtering all the columns based on the example request.  
    Finally, my results are:  
    Q1: 272  
    \=SUMAPRODUCTO((lvs\[Leave Start\]>=$P$4)\*(lvs\[Leave End\]=$P$4)\*(lvs\[Leave End\]=$P$4)\*(lvs\[Leave End\]<=$P$5)\*(lvs\[Ninja?\]="S")\*(lvs\[Leave Type\]="Vacation")\*((lvs\[Status\]="Approved")+(lvs\[Status\]="Pending")))
    
    [Reply](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#comment-2161665)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/how-many-employees-are-on-leave-during-easter-holidays-homework/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Hide columns one one tab same way as they were in another place \[quick tip\]](https://chandoo.org/wp/hide-columns-quickly-excel/) | [There are 5 hidden cells in this workbook – Find them all \[Excel Easter Eggs\]](https://chandoo.org/wp/easter-eggs-2017/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)