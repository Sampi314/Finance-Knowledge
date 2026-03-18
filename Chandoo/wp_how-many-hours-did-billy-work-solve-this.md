# How many hours did Billy work? [Solve this] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this

---

How many hours did Billy work? \[Solve this\]
=============================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 140 comments

  

_Here is a simple but tricky problem._

Imagine you are the HR manager of a teeny-tiny manufacturing company. As your company is small, you just have one employee in the shop floor. He is Mr. Billy.

As this is a one person production facility, Billy has the flexibility to choose his working hours. At the end of each week, Bill would email you a file that says start & end times of his work. You are supposed to look at this file, figure out how many hours he worked and pay him accordingly.

So you are looking at the recent data Billy sent.

![hours-worked-billy](https://chandoo.org/wp/wp-content/uploads/2015/06/hours-worked-billy.png)

**So how would you calculate the total hours?**

*   Note: Billy doesn’t know much about Excel.

**Go ahead and answer the question.**

What formula would you write in Hours worked column for each day?

_Assume Start times are in C4:C9 and End times are in D4:D9_

Please post your answers in comments section. Billy is waiting for his pay!!!

PS: In case you want a sample file to play with this data & work, [download it here](https://chandoo.org/wp/wp-content/uploads/2015/06/billy.xlsx)
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
| Written by Chandoo  <br>Tags: [date and time](https://chandoo.org/wp/tag/date-and-time/)<br>, [downloads](https://chandoo.org/wp/tag/downloads/)<br>, [excel formulas](https://chandoo.org/wp/tag/excel-formulas/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 140 Responses to “How many hours did Billy work? \[Solve this\]”

1.  ![](https://secure.gravatar.com/avatar/d3fe07e573358c852c1bb91cabb87ee1e3639becf8aa4b630cf006fa61b3e7e0?s=64&d=mm&r=g) GDH says:
    
    [June 5, 2015 at 8:59 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985986)
    
    \=IF(D4<C4, 1+D4-C4,D4-C4)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985986)
    
    *   ![](https://secure.gravatar.com/avatar/ecee021ef5adf04bbec6c34e4113552a03a3330f7496b500a9c80ffcd38769ea?s=64&d=mm&r=g) alexander says:
        
        [June 5, 2015 at 8:29 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986362)
        
        \=TEXT(D4-C4,"h")
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986362)
        
2.  ![](https://secure.gravatar.com/avatar/ca477f279cc7cc18fe64f39ca2c1b6b4e2134e8528ea5df44bc4e627a28e299a?s=64&d=mm&r=g) Neil A says:
    
    [June 5, 2015 at 9:00 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985987)
    
    \=IF(D4>C4,D4-C4,((D4+1)-C4))  
    Assumes he never works more than a 24 hour shift
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985987)
    
3.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [June 5, 2015 at 9:08 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985990)
    
    In cell F4 type: =MOD(D4-C4,1) and copy down.
    
    In cell F11 type =SUM(F4:F9) and custom format as: \[h\]:mm
    
    Michael (Micky) Avidan  
    “Microsoft® Answers" - Wiki author & Forums Moderator  
    “Microsoft®” MVP – Excel (2009-2015)  
    ISRAEL
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985990)
    
    *   ![](https://secure.gravatar.com/avatar/cdcce791ec727df34461720227219f2aaa9af2d00fa052ad77be7ad968af6ac6?s=64&d=mm&r=g) Ronnie says:
        
        [June 5, 2015 at 4:28 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986215)
        
        Micky,  
        I get .30 using your formula. What am I doing wrong?
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986215)
        
        *   ![](https://secure.gravatar.com/avatar/cdcce791ec727df34461720227219f2aaa9af2d00fa052ad77be7ad968af6ac6?s=64&d=mm&r=g) Ronnie says:
            
            [June 5, 2015 at 4:39 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986227)
            
            OK, if I convert this to a Time value, I get 7:15. But I don't think Hours Worked is a time value. I prefer Nick's formula with \*24 added to get the numeric value of 7.25.
            
            Thanks,  
            Ronnie
            
            [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986227)
            
            *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                
                [June 5, 2015 at 5:21 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986256)
                
                @Ronnie,  
                You are welcome to choose/use any formula you want.  
                I'm looking for some elegance beside using "cold" formulas.  
                Now, imagine a start hour: 08:07 AM. End hour: 03:50 PM.  
                Upon multiplying by 24 and formatting the cell as "Number" you'll get: 7.72 (while my suggestion shows: 07:43)  
                Please take a moment and tell me (us) what is more appropriate.  
                Michael (Micky) Avidan  
                “Microsoft® Answers” – Wiki author & Forums Moderator  
                “Microsoft®” MVP – Excel (2009-2015)  
                ISRAEL
                
                [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986256)
                
                *   ![](https://secure.gravatar.com/avatar/64e6988bfaf93bb19a5ed330ece3909c293ff28d6fbf96ccebfedd55228b3340?s=64&d=mm&r=g) [Dheeru](http://chandoo/)
                     says:
                    
                    [June 6, 2015 at 4:57 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986806)
                    
                    If the confusion is in AM and PM then we have to use formula as "=(D4-C4)+1" , which will reflect correct hours in time format. But if you want to convert it into number format then value will not be correct for reverse timing like "9:00 PM 5:00 AM". For that we have to use logic to convert into num format that would be "=RIGHT(F4,LEN(F4)-1)\*24"
                    
    *   ![](https://secure.gravatar.com/avatar/fd2486bdf1237c184c5d959ce3d4a19e203c11ebf8d820e2255f69687a7fd164?s=64&d=mm&r=g) Arun Rajappa says:
        
        [June 12, 2015 at 9:31 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-991629)
        
        I used if(starttime>0.5,(1-Starttime)+endtime,endtime-starttime)
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-991629)
        
4.  ![](https://secure.gravatar.com/avatar/d13f49ec3dd654844a8ff3fdea295ae605bfa74ea92039c60c1befc7cdae27e2?s=64&d=mm&r=g) Fredy says:
    
    [June 5, 2015 at 9:14 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985994)
    
    I used at the end the "IF" way. One single formula that you can use all over. Thanks a lot for this web! Greetings,  
    Fredy
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985994)
    
5.  ![](https://secure.gravatar.com/avatar/d13f49ec3dd654844a8ff3fdea295ae605bfa74ea92039c60c1befc7cdae27e2?s=64&d=mm&r=g) Fredy says:
    
    [June 5, 2015 at 9:16 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985996)
    
    Upps, I forgot the formula  
    \=IF(D4>C4;D4-C4;D4+2\*TIME(12;0;0)-C4)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985996)
    
    *   ![](https://secure.gravatar.com/avatar/d13f49ec3dd654844a8ff3fdea295ae605bfa74ea92039c60c1befc7cdae27e2?s=64&d=mm&r=g) Fredy says:
        
        [June 5, 2015 at 9:21 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985999)
        
        as you can see I didn't know how to add 24 hours, that's why 2xTIME(12;0;0), jajaja. Thanks to you I know now (just add "1").
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985999)
        
        *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [June 5, 2015 at 9:32 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986001)
            
            @Fredy,  
            As you can see I like "short formulas" (the shorter the better) - so, your approach can be shorten down to:
            
            \=D4-C4+(D4<C4)
            
            Michael (Micky) Avidan  
            “Microsoft® Answers” – Wiki author & Forums Moderator  
            “Microsoft®” MVP – Excel (2009-2015)  
            ISRAEL
            
            [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986001)
            
            *   ![](https://secure.gravatar.com/avatar/d13f49ec3dd654844a8ff3fdea295ae605bfa74ea92039c60c1befc7cdae27e2?s=64&d=mm&r=g) Fredy says:
                
                [June 5, 2015 at 9:39 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986005)
                
                cool!
                
                [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986005)
                
            *   ![](https://secure.gravatar.com/avatar/6b03c1ddf9231cbbf65730ea01c93dfe9e77fc61a1419db1f37c9d2c6c97de69?s=64&d=mm&r=g) [Nick Partridge](http://www.partridge.co.nz/)
                 says:
                
                [June 5, 2015 at 9:51 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986010)
                
                "and pay him accordingly."
                
                [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986010)
                
            *   ![](https://secure.gravatar.com/avatar/8169adf50843770093821032ca6dfd9939793bcb6f7f3de26a06cc470210733e?s=64&d=mm&r=g) N Shivkumar says:
                
                [June 5, 2015 at 6:00 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986290)
                
                \=(IF(C4>D4,D4+1-C4,D4-C4))\*24
                
                [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986290)
                
6.  ![](https://secure.gravatar.com/avatar/6b03c1ddf9231cbbf65730ea01c93dfe9e77fc61a1419db1f37c9d2c6c97de69?s=64&d=mm&r=g) [Nick Partridge](http://www.partridge.co.nz/)
     says:
    
    [June 5, 2015 at 9:20 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985998)
    
    Modifying Micky's
    
    In F4 =MOD(D4-C4,1)\*24 copy down
    
    \=SUM(F4:F9) and format either fractions of appropriate number of decimals. 10 1/2 hours of 10.5 hours.
    
    To run payroll I want a number of hours, not an Excel format time result - it is easier to multiply that by hourly rate.
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-985998)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [June 5, 2015 at 10:36 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986034)
        
        @Nick,  
        I don't remember we were asked to calculate any payroll.  
        BUT, if we would have then, to my(!) opinion, it is more elegant to present the day by day working hours in HOURS Format and to multiply the end TOTAL by 24 and by the hour wage.
        
        Michael (Micky) Avidan  
        “Microsoft® Answers” – Wiki author & Forums Moderator  
        “Microsoft®” MVP – Excel (2009-2015)  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986034)
        
7.  ![](https://secure.gravatar.com/avatar/64f3ca9031d8d6d04048ec2f41499646f58129752d4e1e3646103e8684042a97?s=64&d=mm&r=g) ZUR says:
    
    [June 5, 2015 at 9:36 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986002)
    
    good teaser
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986002)
    
8.  ![](https://secure.gravatar.com/avatar/1553d5ef47b0393a50c10641d37284e69f38d33c948dee33ce37a3f64bff4823?s=64&d=mm&r=g) Jo says:
    
    [June 5, 2015 at 9:38 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986003)
    
    \=(D4-C4+(C4>D4))\*24
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986003)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [June 5, 2015 at 9:45 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986006)
        
        @Jo,  
        Multiplying by 24 returns a DECIMAL Time Value which is, mainly, used when one needs to calculate wages by the hour.  
        In this case you may/should leave it out.  
        Michael (Micky) Avidan  
        “Microsoft® Answers” – Wiki author & Forums Moderator  
        “Microsoft®” MVP – Excel (2009-2015)  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986006)
        
9.  ![](https://secure.gravatar.com/avatar/35fe0824f0e26e133074efad77638ea91b80141a1bf2a7af8a18310a42c87f13?s=64&d=mm&r=g) Philip\_Go says:
    
    [June 5, 2015 at 9:39 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986004)
    
    \=TEXT(IF(D7<C7,((24-C7)+D7),C7-D7),"HH:mm")
    
    🙂 Philip
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986004)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [June 5, 2015 at 10:04 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986017)
        
        @Philip\_Go,  
        Chandoo's range starts at row 4 (not 7).  
        Michael (Micky) Avidan  
        “Microsoft® Answers” – Wiki author & Forums Moderator  
        “Microsoft®” MVP – Excel (2009-2015)  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986017)
        
10.  ![](https://secure.gravatar.com/avatar/813efb64c1527559d235fbb31f79f50580669a2dfc00582736561f97f543046b?s=64&d=mm&r=g) chandra mohan says:
    
    [June 5, 2015 at 10:23 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986025)
    
    \=abs(d7-c7) and change cell format to hh:mm
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986025)
    
    *   ![](https://secure.gravatar.com/avatar/813efb64c1527559d235fbb31f79f50580669a2dfc00582736561f97f543046b?s=64&d=mm&r=g) chandra mohan says:
        
        [June 5, 2015 at 11:14 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986057)
        
        for total hours, change cell format type to \[h\]:mm:ss, you can apply same format to diff. of time also.
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986057)
        
        *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [June 5, 2015 at 1:16 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986114)
            
            @Chandra,  
            To my opinion the total working hours from 09:00 PM (21:00) till 05:00 AM is: 08:00 and not 16:00.  
            Michael (Micky) Avidan  
            “Microsoft® Answers” – Wiki author & Forums Moderator  
            “Microsoft®” MVP – Excel (2009-2015)  
            ISRAEL
            
            [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986114)
            
11.  ![](https://secure.gravatar.com/avatar/4215fd1e081db69d1f571e197d7d25b797c175bb36de869be32ec05ac68086f7?s=64&d=mm&r=g) Darin says:
    
    [June 5, 2015 at 1:01 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986102)
    
    \=((D4+(C4>D4)\*1)-C4)\*24
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986102)
    
12.  ![](https://secure.gravatar.com/avatar/42e579732c63c08bf6feceb9d6c1f1560096545b1184b14e629b9fb1a98d08fd?s=64&d=mm&r=g) Peter W. says:
    
    [June 5, 2015 at 1:15 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986112)
    
    \=(IF(C4<D4,0,1)+D4-C4)\*24
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986112)
    
13.  ![](https://secure.gravatar.com/avatar/0941af9b2ffd9d3bdbb50f5bdd534aab0713ef367a8fcbac9fba53a5804b65c2?s=64&d=mm&r=g) Phil says:
    
    [June 5, 2015 at 1:32 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986124)
    
    \=sum each day; then =sum total of week
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986124)
    
14.  ![](https://secure.gravatar.com/avatar/1866b63295becb23ac3bc365307d3217eb492c067279deac88a942ae503b7029?s=64&d=mm&r=g) Paul says:
    
    [June 5, 2015 at 2:15 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986140)
    
    \=IF(HOUR(C2)-HOUR(B2)<0,24+(HOUR(C2)-HOUR(B2)),HOUR(C2)-HOUR(B2))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986140)
    
15.  ![](https://secure.gravatar.com/avatar/cdcce791ec727df34461720227219f2aaa9af2d00fa052ad77be7ad968af6ac6?s=64&d=mm&r=g) Ronnie says:
    
    [June 5, 2015 at 2:33 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986149)
    
    I like long, drawn-out formulas and didn't want to make the assumption that Billy would only work complete hours. So here is what I came up with. You may now start laughing.
    
    \=IF(C4<D4,(HOUR(D4)+MINUTE(D4)/60)-(HOUR(C4)+MINUTE(C4)/60),(HOUR(D4)+MINUTE(D4)/60-(HOUR(C4)+MINUTE(C4)/60)+24))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986149)
    
16.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [June 5, 2015 at 3:12 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986167)
    
    @Ronnie,  
    With all due respect (I'm not laughing - even not when I see too long formulas) BUT I just would like to point out that all previous suggested formulas (that work as expected) are capable to handle fraction of hours.  
    Michael (Micky) Avidan  
    “Microsoft® Answers” – Wiki author & Forums Moderator  
    “Microsoft®” MVP – Excel (2009-2015)  
    ISRAEL
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986167)
    
17.  ![](https://secure.gravatar.com/avatar/fc212104c087eb155840e32622e49588dc7b08cb0f4e26768d55964b0863269b?s=64&d=mm&r=g) [Ken Puls](http://www.excelguru.ca/)
     says:
    
    [June 5, 2015 at 3:30 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986177)
    
    I'd just use the following Power Query script. That way I just have to right click and refresh the output next time, and never write the formula again:
    
    let  
    Source = Excel.CurrentWorkbook(){\[Name="Table1"\]}\[Content\],  
    #"Changed Type2" = Table.TransformColumnTypes(Source,{{"Start", type datetime}, {"End", type datetime}}),  
    #"Added Custom1" = Table.AddColumn(#"Changed Type2", "End\_Adj", each if \[Start\]>\[End\] then Date.AddDays(\[End\],1) else \[End\]),  
    #"Inserted Time Subtraction" = Table.AddColumn(#"Added Custom1", "Hours Worked", each \[End\_Adj\] - \[Start\], type duration),  
    #"Removed Columns" = Table.RemoveColumns(#"Inserted Time Subtraction",{"End\_Adj"}),  
    #"Changed Type" = Table.TransformColumnTypes(#"Removed Columns",{{"Start", type time}, {"End", type time}})  
    in  
    #"Changed Type"
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986177)
    
    *   ![](https://secure.gravatar.com/avatar/efdd88b16970c70dc36076b434b7288b4d8dfbb1c255a9a2b8314b0d4327e365?s=64&d=mm&r=g) gino says:
        
        [June 5, 2015 at 5:22 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986257)
        
        Ha ha ha - Ken - that's awesome!!! Gotta love it!
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986257)
        
        *   ![](https://secure.gravatar.com/avatar/0240a64726a93bd78500346e2a1e2be7384893dea1124b11c585976fcef4ecc7?s=64&d=mm&r=g) Rebou says:
            
            [June 8, 2015 at 11:43 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988962)
            
            Oh! You clever boy, and not one to hide his light under a bushel.
            
            [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988962)
            
18.  ![](https://secure.gravatar.com/avatar/96e6e1030b42477cb319e440687142ffe5a3967bc51ba19d79db8d96bffd1c89?s=64&d=mm&r=g) ChacoKevy says:
    
    [June 5, 2015 at 4:58 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986238)
    
    I love this blog post, and am thankful to see everyone's comments. Thanks so far!
    
    I once came upon a problem similar to this. Can we have a part 2 to this post with a little more difficulty?  
    For instance, how about a formula to calculate total net hours spent on a project, but using an employee's work schedule, days off, and holidays?  
    Assume Jim's job is restoring antique cars. His regular schedule is 09:00 to 17:00 M-F. His most recent project began on Thursday, July 3rd 2013 at 14:00 and he finished on July 14th 2013 at 11:00.  
    Jim works in America, where July 4th is a Holiday, and therefore doesn't work.  
    So if Columns A,B,C,D,E are Shift start, Shift end, Project start, Project end, Holidays in the year, row 2 reads out as 09:00, 17:00, (date submitted in US English) 7/3/2013 14:00:00, 7/14/2013 11:00:00, 7/4/2013. How many hours did Jim work?
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986238)
    
19.  ![](https://secure.gravatar.com/avatar/08ce11362a0416d908f18fc0faf2be5a7161005b74d3d8ce0fdbbb9b4addf63f?s=64&d=mm&r=g) Kevin says:
    
    [June 5, 2015 at 5:12 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986248)
    
    \=IF((D5<C5),24-(C5\*24)+(D5\*24),(D5-C5)\*24)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986248)
    
20.  ![](https://secure.gravatar.com/avatar/ee44d9af9fccf383c0f8c65deed33696d7b55190712b7facfef73f341970aefe?s=64&d=mm&r=g) [Stephen Hogan](http://twitter.comdatalore_tv/)
     says:
    
    [June 5, 2015 at 5:13 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986249)
    
    \=IF(D4<C4,(TODAY()+1+D4)-(TODAY()+C4),D4-C4)\*24
    
    Handles negative hours. There is a reason why I am doing it like this - anyone hazard a guess?
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986249)
    
21.  ![](https://secure.gravatar.com/avatar/d41d3a55cf967f57c041f24102a4adb536d3bdae723419a77ff6fd85165979d3?s=64&d=mm&r=g) Rich says:
    
    [June 5, 2015 at 5:14 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986250)
    
    Not very 'clean', in cell e4 enter =12-c4+d4 (copy down).
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986250)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [June 5, 2015 at 9:27 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986388)
        
        @Rich,  
        Are you, somehow, related to Billy ?  
        He will be very happy to get paid for 1700 Hours (which is the total sum of your daily calculation).  
        Michael (Micky) Avidan  
        “Microsoft® Answers” – Wiki author & Forums Moderator  
        “Microsoft®” MVP – Excel (2009-2015)  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986388)
        
        *   ![](https://secure.gravatar.com/avatar/d41d3a55cf967f57c041f24102a4adb536d3bdae723419a77ff6fd85165979d3?s=64&d=mm&r=g) Rich says:
            
            [June 9, 2015 at 8:58 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990018)
            
            I didn't add them together to get 1700 hours - you did. I did the calculations to convert clock time into daily hours worked. From there, many of us born prior to 1985 tend to add the 6 daily numbers in our head.
            
            [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990018)
            
22.  ![](https://secure.gravatar.com/avatar/4760e6f0a4f6f6264de126f41eeb98a147b6cfd54098a554e68a0d9fa59b895a?s=64&d=mm&r=g) Vaibhav Garg says:
    
    [June 5, 2015 at 5:18 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986251)
    
    This does work well. Just a little twist to the cut and dried. (N(NOT(D4>C4))+D4-C4)\*24
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986251)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [June 5, 2015 at 9:40 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986392)
        
        @Vaibhav,  
        So then after eliminating unnecessary operands you'll end up with: =((D4<C4)+D4-C4)\*24  
        Michael (Micky) Avidan  
        “Microsoft® Answers” – Wiki author & Forums Moderator  
        “Microsoft®” MVP – Excel (2009-2015)  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986392)
        
23.  ![](https://secure.gravatar.com/avatar/f8abafbd8a429f710a4523d5223c2840f01e56191e9ebc7d1875a65a9f38ea0e?s=64&d=mm&r=g) Alf says:
    
    [June 5, 2015 at 5:18 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986252)
    
    answer is 44, I sent the MS Excel file
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986252)
    
24.  ![](https://secure.gravatar.com/avatar/efdd88b16970c70dc36076b434b7288b4d8dfbb1c255a9a2b8314b0d4327e365?s=64&d=mm&r=g) gino says:
    
    [June 5, 2015 at 5:21 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986254)
    
    44 hours...
    
    In cell E4:  
    \=(D4-C4+(D4<C4))\*24
    
    Drag down to E9 and then =SUM(E4:E9) in cell E10 to show somebody needs to pay Mr. Billy for 44 hours work. Oh, and for the record, Mr. Billy earns $459.78 per hour and has authorized me to collect his paycheck this week. LOL!!!
    
    Cheers,  
    Gino
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986254)
    
    *   ![](https://secure.gravatar.com/avatar/375619229a7a85a42c36cf46de7053cea62e70d968f0241bab0ccfc97eec2449?s=64&d=mm&r=g) Anil says:
        
        [June 8, 2015 at 10:19 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988917)
        
        I got it
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988917)
        
25.  ![](https://secure.gravatar.com/avatar/023654a8284b8b76289c96e961b54444d315dce8cc154c9f4194b1bc49cb0763?s=64&d=mm&r=g) Jack Surma says:
    
    [June 5, 2015 at 5:25 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986258)
    
    How about simply this to get the daily hours worked:
    
    \=MOD((D4-C4+1)\*24,24)
    
    It subtracts end from start and adds 1 (day) in case it is PM to AM  
    Then if multiplies it by 24 to get hours from the decimal days  
    Lastly it does a mod to "remove" the 24 hours if the values were in the same day
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986258)
    
26.  ![](https://secure.gravatar.com/avatar/6a576790ad2e8630bd5ed28309ad884a266817f6c62a2005f654d1c3d06e0097?s=64&d=mm&r=g) farshad says:
    
    [June 5, 2015 at 5:30 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986265)
    
    \=+IF(C4<D4,D4-C4,D4+24-C4)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986265)
    
27.  ![](https://secure.gravatar.com/avatar/49703b3e3b8a9258cd42b031139b062fc25d223440f8ca0b3ea20802cc6ebb17?s=64&d=mm&r=g) Nam says:
    
    [June 5, 2015 at 5:40 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986277)
    
    \=((D4-C4)+(C4>D4))\*24
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986277)
    
28.  ![](https://secure.gravatar.com/avatar/9df4c772feeaa2f3745b31e6829a57c29d308cb57406a955b7d4e516effb88d5?s=64&d=mm&r=g) Unimord says:
    
    [June 5, 2015 at 5:41 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986279)
    
    \=SUM(D4,(D4<C4)\*720,-C4) and copy down.
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986279)
    
29.  ![](https://secure.gravatar.com/avatar/3f5997f7bbd6092f3b146cc6ba069125dbef39ad48b52255058f64fca6f6f30d?s=64&d=mm&r=g) Rich says:
    
    [June 5, 2015 at 5:49 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986284)
    
    To keep transparency that we're working with time:
    
    \= IF(HOUR(D4) - HOUR(C4)>0,  
    HOUR(D4) - HOUR(C4),  
    24 + (HOUR(D4) - HOUR(C4))  
    )
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986284)
    
30.  ![](https://secure.gravatar.com/avatar/8169adf50843770093821032ca6dfd9939793bcb6f7f3de26a06cc470210733e?s=64&d=mm&r=g) N Shivkumar says:
    
    [June 5, 2015 at 6:01 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986291)
    
    \=(IF(C4>D4,D4+1-C4,D4-C4))\*24
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986291)
    
    *   ![](https://secure.gravatar.com/avatar/089b56a59ecfa1e6d731ad0718b9c932b4c8a40d3522eafd5d6b3e5685ede706?s=64&d=mm&r=g) K-Li-Ch says:
        
        [June 5, 2015 at 6:05 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986296)
        
        \=IFI(D4 >=C4;D4 - C4; D4 - C4 + 1) \* 24
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986296)
        
31.  ![](https://secure.gravatar.com/avatar/b95828d6f06eaaad7496699f41e3eca3b814d1a2f0b2be29889630a0e0be301f?s=64&d=mm&r=g) Dan says:
    
    [June 5, 2015 at 6:04 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986295)
    
    Sheet Cell Value Displayed value Formula  
    billy F4 0.291666667 7:00 =IF(C4="","",IF(D4="","",+D4-C4))  
    billy F5 0.333333333 8:00 =IF(C5="","",IF(D5="","",+D5-C5))  
    billy F6 0.291666667 7:00 =IF(C6="","",IF(D6="","",+D6-C6))  
    billy F7 0.333333333 8:00 =IF(C7="","",IF(D7="","",+D7-C7))  
    billy F8 0.25 6:00 =IF(C8="","",IF(D8="","",+D8-C8))  
    billy F9 0.333333333 8:00 =IF(C9="","",IF(D9="","",+D9-C9))  
    billy F11 1.833333333 44:00 =SUM(F4:F9)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986295)
    
32.  ![](https://secure.gravatar.com/avatar/b95828d6f06eaaad7496699f41e3eca3b814d1a2f0b2be29889630a0e0be301f?s=64&d=mm&r=g) Dan says:
    
    [June 5, 2015 at 6:05 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986297)
    
    \=IF(C4="","",IF(D4="","",+D4-C4))  
    \=IF(C5="","",IF(D5="","",+D5-C5))  
    \=IF(C6="","",IF(D6="","",+D6-C6))  
    \=IF(C7="","",IF(D7="","",+D7-C7))  
    \=IF(C8="","",IF(D8="","",+D8-C8))  
    \=IF(C9="","",IF(D9="","",+D9-C9))  
    \=SUM(F4:F9)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986297)
    
33.  ![](https://secure.gravatar.com/avatar/8169adf50843770093821032ca6dfd9939793bcb6f7f3de26a06cc470210733e?s=64&d=mm&r=g) N Shivkumar says:
    
    [June 5, 2015 at 6:06 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986299)
    
    \=(IF(C4>D4,D4+1-C4,D4-C4))\*24  
    Total 44 hours
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986299)
    
34.  ![](https://secure.gravatar.com/avatar/acea3f2ba76aef3f1d8c7d8a097b6fd4a9ab6784a73e077a91d0ebc578d6ebdb?s=64&d=mm&r=g) Truong Nguyen says:
    
    [June 5, 2015 at 6:28 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986309)
    
    \=IF(HOUR(D4)>12,HOUR(D4-C4),HOUR(24-C4)+HOUR(D4))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986309)
    
35.  ![](https://secure.gravatar.com/avatar/c6991daf4d0fea04f5358a825892ce6087ca4a39ea68531348ef4608fe265dd1?s=64&d=mm&r=g) [Don](http://pistulka.com/other)
     says:
    
    [June 5, 2015 at 6:49 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986316)
    
    \=ABS(IF((D4-C4)\*24>0,(D4-C4)\*24,((C4-(1+D4)))\*24))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986316)
    
    *   ![](https://secure.gravatar.com/avatar/93e751ca8ab5515864e8c90561757212d9bd3ec3e9d01cabc71c161146822e8c?s=64&d=mm&r=g) Johniron says:
        
        [June 5, 2015 at 8:20 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986356)
        
        \=MOD(ABS(D4-C4);1/2)  
        and  
        \=SUM(F4:F9)\*24
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986356)
        
36.  ![](https://secure.gravatar.com/avatar/dbf52b5affba8518884e43383d5ba1a0bada4aaaef3b1ac2f7b694852da09b46?s=64&d=mm&r=g) June says:
    
    [June 5, 2015 at 6:55 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986320)
    
    Total 44 hours.
    
    Format the sum cell: \[h\]:mm;@
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986320)
    
37.  ![](https://secure.gravatar.com/avatar/624760007631c3720c1c92176d8e067e5a9b091df07957753c9d88b91af0f77e?s=64&d=mm&r=g) Mark says:
    
    [June 5, 2015 at 7:06 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986322)
    
    I had this problem with the added twist of Before Lunch (in:C11/out:D11) and After Lunch (in:E11/out:F11) to calculate Regular (max 8 hours) and OT over 8 hours. Times are entered as AM / PM.
    
    Regular: =IF((((D11-C11)+(F11-E11))\*24)>8,8,((D11-C11)+(F11-E11))\*24)
    
    OT: =IF(((D11-C11)+(F11-E11))\*24>8,((D11-C11)+(F11-E11))\*24-8-L11,0)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986322)
    
38.  ![](https://secure.gravatar.com/avatar/9413bb608c954a409f90e155fa1366dcd39e268b8e1820be08477fb10ec5d47d?s=64&d=mm&r=g) Jeff says:
    
    [June 5, 2015 at 8:00 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986344)
    
    Oh, you non-HR folks; Billy does not get paid for his meal break each shift. Need to subtract one hour per worked shift greater than 6 hours, no deduction for shorter shifts as no meal break is required. 😉
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986344)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [June 6, 2015 at 7:59 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986896)
        
        @Jeff,  
        Most of the time I take people as serious even if the put a blinking smiley at the end of their post - therefore, here (in the linked picture) is my suggestion to the above mentioned situation.  
        Pls note that the Threshold & Lunch break time were entered in 2 cells in order to make it easy to change them if needed.
        
        [http://jpg.co.il/view/5572a6ea0abbd.png/](http://jpg.co.il/view/5572a6ea0abbd.png/)
        
        Michael (Micky) Avidan  
        “Microsoft® Answers” – Wiki author & Forums Moderator  
        “Microsoft®” MVP – Excel (2009-2015)  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986896)
        
        *   ![](https://secure.gravatar.com/avatar/9413bb608c954a409f90e155fa1366dcd39e268b8e1820be08477fb10ec5d47d?s=64&d=mm&r=g) Jeff says:
            
            [June 6, 2015 at 9:26 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987531)
            
            Very elegant solution. Thanks.  
            Brought a whole new level of spreadsheets top my attention!
            
            Jeff
            
            [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987531)
            
    *   ![](https://secure.gravatar.com/avatar/ca001eeabcda092dabada99dcebc945563a21c24797ad9e1c70ab25f4b3cd16a?s=64&d=mm&r=g) Eddie says:
        
        [June 8, 2015 at 8:48 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988880)
        
        Jeff, this should answer your problems (N.B. it's 1 meal break for every 6 hours worked)  
        F4: Hours worked =(D4<C4)+(D4-C4)  
        G4: # Meal Breaks =INT(F4/TIME(6,0,1)) \[The extra second is there to ensure the shift is over 6 hours and not equal to 6 hours\]  
        H4: Paid Hours =F4-TIME(G4,0,0)  
        H11: =SUM(H4:H9)
        
        gives you 39 paid hours
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988880)
        
39.  ![](https://secure.gravatar.com/avatar/3b23ba31bc239880246ac989b02bab3dfbc6a87a3333c86eedeed98db64bfb91?s=64&d=mm&r=g) [W.Carr](http://www.putjahmosthigh.com/)
     says:
    
    [June 5, 2015 at 8:01 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986345)
    
    \=IF(AND(C4\*24>12,D4\*24>12),((D4-C4)\*24),IF(C4\*24>12,24-(C4\*24)+(D4\*24),((D4-C4)\*24)))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986345)
    
40.  ![](https://secure.gravatar.com/avatar/5cbb48df5a5677c25fd2e4d93beb22b4ddd74de1d50a260bb2e182ea251ca421?s=64&d=mm&r=g) Somak says:
    
    [June 5, 2015 at 8:10 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986349)
    
    \=IFERROR(HOUR(D4-C4),24-HOUR(C4-D4))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986349)
    
41.  ![](https://secure.gravatar.com/avatar/db0d0629dac6ea1c01cdcb2d17de1b885ec1306c08e2dfc03e6283bd97a346ff?s=64&d=mm&r=g) Vikram says:
    
    [June 5, 2015 at 8:19 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986354)
    
    \=IFERROR(HOUR(D4-C4),HOUR(12-C4)+HOUR(D4-0)). Total 44 hours
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986354)
    
42.  ![](https://secure.gravatar.com/avatar/ed3550eff0acd063de1e923a57ef4b7eb4e8dc3c970f0fc6778182e3ddd27e8e?s=64&d=mm&r=g) Ron Wallace says:
    
    [June 5, 2015 at 8:30 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986363)
    
    This is the best I can find.
    
    Enter =MOD(24\*(1+D4-C4),24) in cell F4 and copy down.
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986363)
    
43.  ![](https://secure.gravatar.com/avatar/fe5381867164f5057e5c27175dcabc37708f3318b679bcccb82235e0d5710e32?s=64&d=mm&r=g) Gweed says:
    
    [June 5, 2015 at 9:16 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986381)
    
    F cells format : Numeric  
    in F cells  
    \=IF((HOUR(D4)-HOUR(C4))>0,HOUR(D4)-HOUR(C4),24+HOUR(D4)-HOUR(C4))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986381)
    
44.  ![](https://secure.gravatar.com/avatar/d2b3f77fd2ff454d31bd76dfee74518b60eb8877daf9b5e043f528fa155282db?s=64&d=mm&r=g) Brett Ellingson says:
    
    [June 5, 2015 at 9:41 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986393)
    
    I thought my answer was cool...untill I looked at a few of these answers 🙂
    
    This gives me the number of hours he worked that day  
    IF(TEXT(D4,"\[m\]")\*1>TEXT(C4,"\[m\]")\*1,TEXT(D4,"\[m\]")-TEXT(C4,"\[m\]"),1440+TEXT(D4,"\[m\]")-TEXT(C4,"\[m\]"))/60
    
    converted each time entry to minutes (TEXT function) - I don't need the TEXT function but wanted to put it in there anyway to show my process
    
    subtracted start time from finish time  
    used IF function to look for when end time was in the early AM hours  
    Multiplied by 1 to convert text back to number with IF function
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986393)
    
45.  ![](https://secure.gravatar.com/avatar/7988fcbf48485513e616a24b5bda217f2e06dd767978ddfc80f4b235f66875d9?s=64&d=mm&r=g) Chuck says:
    
    [June 5, 2015 at 10:21 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986405)
    
    \=IF(D4>C4,(D4-C4)\*24,((D4+1)-C4)\*24)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986405)
    
46.  ![](https://secure.gravatar.com/avatar/eb37b8a00841c0b290921261245d28e73679aa13efabdfccafcb43ea1303c71e?s=64&d=mm&r=g) [Eljefegeneo](http://none/)
     says:
    
    [June 5, 2015 at 11:07 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986422)
    
    I got it, but I am not sure if there is an error in my formula:
    
    \=(D4-C4) +24
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986422)
    
47.  ![](https://secure.gravatar.com/avatar/a1792ffec9cf9a100c6152c67f8bf942b182eb3e044b442d2b47f8af2f4d3521?s=64&d=mm&r=g) John D says:
    
    [June 6, 2015 at 12:16 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986489)
    
    For each day =(C2-B2)\*24  
    Sum all days.  
    total = 44 Hrs
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986489)
    
48.  ![](https://secure.gravatar.com/avatar/c98dd686e501fd0cc415cb4eb50b542f2ac6724512a79bfd83eaa79abb5a67cd?s=64&d=mm&r=g) Bala says:
    
    [June 6, 2015 at 4:59 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986808)
    
    Easy..  
    IF((D4-C4)>0,(D4-C4)\*24,(1-(C4-D4))\*24)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986808)
    
49.  ![](https://secure.gravatar.com/avatar/50246677663f3937dd6076c6aa4fedf13520658aa5dab50d1c5719bdbfd7ca9d?s=64&d=mm&r=g) Shajid Hossain says:
    
    [June 6, 2015 at 5:26 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986822)
    
    For a day =IF(B2>C2,1+C2,C2)-B2  
    For Total =SUM(E2:E7)\*24
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986822)
    
50.  ![](https://secure.gravatar.com/avatar/27f38e7362fc6f2fcf0a83d95633ea6c23bee0410db93b8e7c09f92ff5528e71?s=64&d=mm&r=g) Gaurav says:
    
    [June 6, 2015 at 6:43 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986864)
    
    \=IF(D9<C9,D9+1,D9)-C9
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986864)
    
51.  ![](https://secure.gravatar.com/avatar/167d8b65d12600316e71f2911b6c3082ce99cb028af1b4d37168faf88b03d3ff?s=64&d=mm&r=g) Amit says:
    
    [June 6, 2015 at 7:23 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986883)
    
    Used below formula to get the result
    
    \=IF(TEXT(D4,"HH:MM")>TEXT(C4,"HH:MM"),TEXT(D4,"HH:MM")-TEXT(C4,"HH:MM"),(24-TEXT(C4,"HH:MM"))+TEXT(D4,"HH:MM"))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986883)
    
52.  ![](https://secure.gravatar.com/avatar/b4873ed7f148fdcb5565d2c4088a97919284dc89a4136ec30bb01da7ce856939?s=64&d=mm&r=g) jraju says:
    
    [June 6, 2015 at 7:31 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986885)
    
    Hi, My simple formula would be  
    \=TEXT(d4-c2,"h"), provided the input entries in c and d coloum are manually formatted as 1:30 PM in the time format to get the exact hours.
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986885)
    
53.  ![](https://secure.gravatar.com/avatar/eedf7c572dcd7238723c0289c35f021a89ad0ae8b7346050245996f0b283d4ca?s=64&d=mm&r=g) Deepak Kumar says:
    
    [June 6, 2015 at 8:20 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986906)
    
    \=IF(E4<C4,TEXT(24+D4-C4,"hh:mm"),TEXT(D4-C4,"hh:mm"))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986906)
    
54.  ![](https://secure.gravatar.com/avatar/53c4770c0934bdcd7338d505803bbbd7ebfe3f60916a20a1748317f4dd9dd67b?s=64&d=mm&r=g) [Rahat Khan](http://www.banglatrek.org/)
     says:
    
    [June 6, 2015 at 9:09 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986933)
    
    \=24-(C4-$H$4)-($H$4-D4)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986933)
    
    *   ![](https://secure.gravatar.com/avatar/53c4770c0934bdcd7338d505803bbbd7ebfe3f60916a20a1748317f4dd9dd67b?s=64&d=mm&r=g) [Rahat Khan](http://www.banglatrek.org/)
         says:
        
        [June 6, 2015 at 9:14 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986936)
        
        particialy work 🙁
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986936)
        
        *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [June 6, 2015 at 3:33 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987330)
            
            @Rahat,  
            Let us assume that Billy gets $20 per hour.  
            After calculating his daily hours - will you, please, sum his 6 days working hours and multiply that sum by $20 ?  
            How much did you get ?  
            From previous posts it is easy to find out that the total hours were 44 and by multiplying them by $20, Billy should be paid $880.
            
            Michael (Micky) Avidan  
            “Microsoft® Answers” – Wiki author & Forums Moderator  
            “Microsoft®” MVP – Excel (2009-2015)  
            ISRAEL
            
            [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987330)
            
55.  ![](https://secure.gravatar.com/avatar/f1c96301746c45ea765053a74c7b3d1bc608a267194ff79e1fdcf83bed90ad33?s=64&d=mm&r=g) Saad Hanif says:
    
    [June 6, 2015 at 9:27 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986942)
    
    This formula should be applied in above condition.
    
    \=IF(D4>C4,TEXT(D4-C4,"h"),TEXT(C4-D4,"h"))
    
    Check and reply me either it is easy to understand and apply
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-986942)
    
56.  ![](https://secure.gravatar.com/avatar/78937019f70ba3301cc975115b58b9a0841546daf5253e2b7810b304370d2f37?s=64&d=mm&r=g) [Hasaan Fazal](http://www.pakaccountants.com/excel)
     says:
    
    [June 6, 2015 at 1:24 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987172)
    
    \=D4-C4+(C4>D4)  
    Problem is that time can't be negative so one way to get around it is use logical test to make it positive.
    
    Would like to hear from other excel heads here to see if this approach stands the test.
    
    Hasaan
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987172)
    
57.  ![](https://secure.gravatar.com/avatar/2df44ede72795de936be209699a5ffaa582df98320f5a2be0e00a7693abbfe7d?s=64&d=mm&r=g) [David Hager](https://dhexcel1.wordpress.com/)
     says:
    
    [June 6, 2015 at 6:07 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987418)
    
    \=MOD(D4+1-C4,1)\*24
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987418)
    
58.  ![](https://secure.gravatar.com/avatar/1d37348be87adfbd5ddfadb09c4b89747d61b12fc758089b2400bf14925b958b?s=64&d=mm&r=g) Taanya Lynn Pillsbury says:
    
    [June 6, 2015 at 6:16 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987423)
    
    \=IF(D4<C4,D4+1,D4)-C4 , this calculate the proper hours for each day worked; however, it doesn't give the correct sum at the bottom if you try to add the hours up. But, if you change the grand total hours to a custom format of \[h\]:mm:ss then the total hours is correct (44 hours).
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987423)
    
59.  ![](https://secure.gravatar.com/avatar/34ef8e6463cdcf1d540c34264f2a43391851f3f2e7802be4ec1bd11c980cf23a?s=64&d=mm&r=g) Xiq says:
    
    [June 6, 2015 at 6:36 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987440)
    
    One formula non-array solution:  
    \=SUMPRODUCT((D4:D9-C4:C9+(C4:C9>D4:D9)))\*24
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987440)
    
    *   ![](https://secure.gravatar.com/avatar/34ef8e6463cdcf1d540c34264f2a43391851f3f2e7802be4ec1bd11c980cf23a?s=64&d=mm&r=g) Xiq says:
        
        [June 6, 2015 at 6:41 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987446)
        
        Another one formula non-array solution:  
        \=SUMPRODUCT(MOD(D4:D9+1-C4:C9,1))\*24
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987446)
        
        *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [June 7, 2015 at 7:00 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987992)
            
            @Xiq,  
            What role plays the "+1" ?  
            Michael (Micky) Avidan  
            “Microsoft® Answers” – Wiki author & Forums Moderator  
            “Microsoft®” MVP – Excel (2009-2015)  
            ISRAEL
            
            [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987992)
            
60.  ![](https://secure.gravatar.com/avatar/79c30c3b5d7335767dfec78788c0aadcc7d1d0dd58241c20d90e2385c3795b6f?s=64&d=mm&r=g) IndDon says:
    
    [June 6, 2015 at 7:12 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987458)
    
    One of the ninja's helped me with the below formula, added function was ABS. You have to format the Hours worked column to 00.00 :
    
    1\. Hours worked=IF(OR($C4="",$D4=""),"",ABS(MOD($D4-$C4,1)\*24))  
    2\. Total=SUM(F4:F9)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987458)
    
61.  ![](https://secure.gravatar.com/avatar/58b001eca0431554f67348ec6c37b710b843fcee5ff2824993f6fe81ec131d4a?s=64&d=mm&r=g) Shaji says:
    
    [June 7, 2015 at 4:48 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987940)
    
    format the 'Hours Worked' column as number with 2 digits and use the following formula...
    
    \=HOUR(IF(C4>D4,(D4+24)-C4,D4-C4))+(MINUTE(IF(C4>D4,(D4+24)-C4,D4-C4))/60)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-987940)
    
62.  ![](https://secure.gravatar.com/avatar/6dca2279e95df33619e2406105bfa25af446001f64751ef0fa4a9285fd7e4855?s=64&d=mm&r=g) Ateeque Malik says:
    
    [June 7, 2015 at 8:09 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988031)
    
    \=IF((D4-C4)<0,((D4-C4)+1)\*24,(D4-C4)\*24)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988031)
    
    *   ![](https://secure.gravatar.com/avatar/6dca2279e95df33619e2406105bfa25af446001f64751ef0fa4a9285fd7e4855?s=64&d=mm&r=g) Ateeque Malik says:
        
        [June 7, 2015 at 8:12 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988033)
        
        And format the cells as General.
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988033)
        
63.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [June 7, 2015 at 3:19 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988363)
    
    @To whom it may concern !
    
    The shortest formula (for daily hours calculation) is: =D4-C4+(D4<=C4) and NOT: =D4-C4+(D4<C4).
    
    The simple reason (you may bump into it in extreme cases) is that there may be a 24:00 shift (Start: 09:30 AM, End: 09:30 AM (on the next day) and the lack of a "equal sign" will show to 00:00 hours instead of 24:00.  
    (With all due respect and as a Proper Disclosure I didn't checked/followed all suggestions - especially not the long formulas.
    
    Take care and keep on Excelling..."  
    Michael (Micky) Avidan  
    “Microsoft® Answers” – Wiki author & Forums Moderator  
    “Microsoft®” MVP – Excel (2009-2015)  
    ISRAEL
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988363)
    
    *   ![](https://secure.gravatar.com/avatar/3502aaa90ca3d1a86a284f6843e52996e8271cf2c0c04a31bfaab2cc630b5788?s=64&d=mm&r=g) Bill Szysz says:
        
        [June 11, 2015 at 10:46 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-991049)
        
        Maybe Billy goes in and goes out in the same minute?  
        We can not be sure, which case is, so MOD(End-Start,1) is as good as End-Start+(End<=Start). Only if we exclude situation when Billy goes in and goes out in the same minute we can say that was 24 hours shift. If not, we don't know it was zero hours shift or 24 hours shift. 🙂
        
        Regards 🙂
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-991049)
        
64.  ![](https://secure.gravatar.com/avatar/84ba46f1f80bd9f39b5a9ba1c8b02a84860226ab5d77c639eb6c93b1f4dac8b4?s=64&d=mm&r=g) [MF](http://wmfexcel.com/)
     says:
    
    [June 8, 2015 at 2:21 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988691)
    
    Is =MOD(End-Start,1) the simplest one to get the difference?
    
    And multiplying the result by 24 to get the result in hours.
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988691)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [June 8, 2015 at 6:53 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988840)
        
        @MF,  
        Yes it is - with an exceptional case like a 24 hours shift (09:30 AM -> 09:30 AM)  
        In such a case that formula returns 00:00 (0) instead of 24:00 (1).  
        The SHORTEST & CORRECT formula is: =End-Start+(End<=Start)  
        Michael (Micky) Avidan  
        “Microsoft® Answers” – Wiki author & Forums Moderator  
        “Microsoft®” MVP – Excel (2009-2015)  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988840)
        
        *   ![](https://secure.gravatar.com/avatar/84ba46f1f80bd9f39b5a9ba1c8b02a84860226ab5d77c639eb6c93b1f4dac8b4?s=64&d=mm&r=g) [MF](http://wmfexcel.com/welcome)
             says:
            
            [June 10, 2015 at 2:05 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990121)
            
            Hi Micky,  
            You get the point. I didn't expect a long working day of 24 hours... ;p  
            I like the use of the +(End<=Start). Very nice.  
            Cheers,
            
            [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990121)
            
65.  ![](https://secure.gravatar.com/avatar/3a10f566280282bc7bbb3094f076d638080a1a675e2d0a106d3d86ed3f464747?s=64&d=mm&r=g) Phoy says:
    
    [June 8, 2015 at 2:57 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988712)
    
    It should be  
    \=IFERROR(HOUR(D4-C4),HOUR(C4-D4)-24)
    
    Sum = SUM(F4:F9)
    
    You get total hours = 44 hours
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988712)
    
    *   ![](https://secure.gravatar.com/avatar/50af073b93aedb5b272ac3ba262a84c55ec13f60f25ff0d88bd267451b2f6f33?s=64&d=mm&r=g) aakash says:
        
        [June 8, 2015 at 6:47 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988833)
        
        \=IFERROR(HOUR(D4-C4),HOUR(24-(C4-D4)))
        
        a minor tweak!
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988833)
        
66.  ![](https://secure.gravatar.com/avatar/6f97094e3a90efdd3f5ca6a503ddde5bb4a3258ad2f95f5f58b29e2fd7a365be?s=64&d=mm&r=g) rop says:
    
    [June 8, 2015 at 3:54 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988760)
    
    HOUR(D4)-HOUR(C4)+24\*(C4>D4)
    
    Sum = SUM(F4:F9)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988760)
    
67.  ![](https://secure.gravatar.com/avatar/748b5ff4b26b20441021ea20ade031d6e958eda976172b9ce31017c91945e049?s=64&d=mm&r=g) Krishna says:
    
    [June 8, 2015 at 7:11 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988848)
    
    \=IF(C4<D4,HOUR(D4)-HOUR(C4),24-ABS((HOUR(D4)-HOUR(C4))))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988848)
    
68.  ![](https://secure.gravatar.com/avatar/5c581df71e80441e606dcebacb6bfe4fd49b462b954df628b418f0d2245907b6?s=64&d=mm&r=g) Andy Forrester says:
    
    [June 8, 2015 at 9:00 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988883)
    
    \=IF(D4>C4, (D4-C4)\*24,24 +(HOUR("12:00 AM")-HOUR(C4))+HOUR(D4))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988883)
    
69.  ![](https://secure.gravatar.com/avatar/678c5e050b067cde303543e7568c1eb72afdd0ff6e2393f22abed05e53de2629?s=64&d=mm&r=g) bVs says:
    
    [June 8, 2015 at 10:23 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988919)
    
    for the cells  
    "=IF((HOUR(D4)-HOUR(C4))>0,HOUR(D4)-HOUR(C4),HOUR(D4)-HOUR(C4)--24)"
    
    then a simple sum of all the cells for the total
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988919)
    
70.  ![](https://secure.gravatar.com/avatar/b89294bde59ad038aee283ac580472a12e4588929f4ea7061b9a4b0527053c9d?s=64&d=mm&r=g) Jacinto Morales says:
    
    [June 8, 2015 at 10:37 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988926)
    
    You need to be present if you start at night to next day.  
    \=IF(d4<c4;D4+1;D4)-C4
    
    TIME IN TIME OUT HOUR  
    11.00 PM 07.00 AM 8.00  
    10.00 AM 03.00 PM 5.00
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988926)
    
71.  ![](https://secure.gravatar.com/avatar/acf2d1d81d0b2931fec68728af361cdf36c3e2acd9a8d543453221376e97d201?s=64&d=mm&r=g) Chirayu says:
    
    [June 8, 2015 at 10:43 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988930)
    
    \=IFERROR(HOUR(D4-C4),HOUR(C4-D4)/2)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988930)
    
    *   ![](https://secure.gravatar.com/avatar/acf2d1d81d0b2931fec68728af361cdf36c3e2acd9a8d543453221376e97d201?s=64&d=mm&r=g) Chirayu says:
        
        [June 8, 2015 at 10:44 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988934)
        
        just checked, doesn't work 😛 back to drawing board
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988934)
        
        *   ![](https://secure.gravatar.com/avatar/acf2d1d81d0b2931fec68728af361cdf36c3e2acd9a8d543453221376e97d201?s=64&d=mm&r=g) Chirayu says:
            
            [June 8, 2015 at 11:03 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988944)
            
            Fixed it  
            \=IF(HOUR(D4)-HOUR(C4)<0,(24-HOUR(C4))+HOUR(D4),HOUR(D4)-HOUR(C4))
            
            [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988944)
            
72.  ![](https://secure.gravatar.com/avatar/ee44d9af9fccf383c0f8c65deed33696d7b55190712b7facfef73f341970aefe?s=64&d=mm&r=g) [Stephen Hogan](http://twitter.comdatalore_tv/)
     says:
    
    [June 8, 2015 at 11:38 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988956)
    
    I have a question... probably trivial, but if Billy worked 10am Tuesday to 6pm Wednesday, how could he start Wednesday's shift at 3pm?
    
    Wed - Thu has a similar overlap...
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988956)
    
    *   ![](https://secure.gravatar.com/avatar/ee44d9af9fccf383c0f8c65deed33696d7b55190712b7facfef73f341970aefe?s=64&d=mm&r=g) [Stephen Hogan](http://twitter.comdatalore_tv/)
         says:
        
        [June 8, 2015 at 11:41 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988959)
        
        Oh my head. Sorry sorry that doesn't make sense! Eyes got screwed up lol.
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988959)
        
        *   ![](https://secure.gravatar.com/avatar/ee44d9af9fccf383c0f8c65deed33696d7b55190712b7facfef73f341970aefe?s=64&d=mm&r=g) [Stephen Hogan](http://twitter.comdatalore_tv/)
             says:
            
            [June 8, 2015 at 11:41 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988960)
            
            Ignore please.
            
            [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988960)
            
73.  ![](https://secure.gravatar.com/avatar/80d37af3e8ed8c61a95cd583bf2f1779c4e084a2c6c4ef05533bca7fcf485334?s=64&d=mm&r=g) Peter Allen says:
    
    [June 8, 2015 at 11:46 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988966)
    
    I know I'm slow with this, but:  
    \=IF(D4<C4,D4+12,D4)-C4  
    does the trick by adding 12 hours to an all nighter.
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988966)
    
74.  ![](https://secure.gravatar.com/avatar/ee44d9af9fccf383c0f8c65deed33696d7b55190712b7facfef73f341970aefe?s=64&d=mm&r=g) [Stephen Hogan](http://twitter.comdatalore_tv/)
     says:
    
    [June 8, 2015 at 11:51 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988969)
    
    OK after making that dumb mistake... how about filling this formula down from F4:
    
    \=24\*(D4+(C4>D4)-C4)
    
    Then F11:
    
    \=SUM(F4:F9)
    
    It's neat.
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988969)
    
75.  ![](https://secure.gravatar.com/avatar/1dcafbe155712f85b1af989de8c630c605edd8f313904216bff0b197f4e8f222?s=64&d=mm&r=g) Sérgio Silva says:
    
    [June 8, 2015 at 1:18 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988997)
    
    hi.  
    in this cases, i usually use:
    
    i'm from Portugal, so  
    \=RESTO(D4-C4;1)
    
    that in english, is
    
    \=Mod(D4-C4,1)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-988997)
    
76.  ![](https://secure.gravatar.com/avatar/77767ee34f292ece24df85ab6b4a07b93f125f2296c964f93efdaa137937dfac?s=64&d=mm&r=g) Bruno says:
    
    [June 8, 2015 at 1:47 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-989007)
    
    \=IF(D4-C4)>0;D4-C4;(12-C4)+D4)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-989007)
    
77.  ![](https://secure.gravatar.com/avatar/6035ff72515bd8161bffe397a14586b93b8b87180456c588469f242a29f67247?s=64&d=mm&r=g) Ganesh says:
    
    [June 8, 2015 at 2:47 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-989033)
    
    \=IF(C2>B2,TEXT(C2-B2,"H"),24-TEXT(B2-C2,"H"))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-989033)
    
78.  ![](https://secure.gravatar.com/avatar/61d394d93f6ea2c844b1d0e5a537f72d60ba1c0701044c428560b2711bcaf353?s=64&d=mm&r=g) Carpy1985 says:
    
    [June 8, 2015 at 8:10 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-989187)
    
    I used:
    
    \=IF(HOUR(D4)-HOUR(C4)<0,(24-HOUR(C4))+HOUR(D4),HOUR(D4)-HOUR(C4))
    
    which spat the answer out in number not time format.
    
    I have never used the MOD function so thats something to learn next 🙂
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-989187)
    
79.  ![](https://secure.gravatar.com/avatar/06031a85e78e4a6d8e463ab1e0aa2df3cd75cbc9ede62e1eac718d218707940d?s=64&d=mm&r=g) Nur Fuad says:
    
    [June 9, 2015 at 3:45 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-989440)
    
    Formula in cell F4:  
    \=IF(D4>C4;D4-C4;(1-C4)+D4)
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-989440)
    
80.  ![](https://secure.gravatar.com/avatar/9041859041cd28e5aa9263fddc22e53b0075f637771e934134f1982b756bfab9?s=64&d=mm&r=g) [Kevin Lehrbass](https://www.youtube.com/user/MySpreadsheetLab)
     says:
    
    [June 9, 2015 at 3:48 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-989444)
    
    This is a fun puzzle. Thanks Chandoo!  
    I used a single cell array formula:  
    \=SUM(IF($D$4:$D$9>$C$4:$C$9,$D$4:$D$9-$C$4:$C$9,$D$4:$D$9+(1-$C$4:$C$9)))  
    (don't forget to hold down the 'Ctrl' key and the 'Shift' key while you press the 'Enter' key as this is an array formula).
    
    I just noticed that Xiq has a Sumproduct. Nice!  
    Cheers,  
    Kevin Lehrbass
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-989444)
    
81.  ![](https://secure.gravatar.com/avatar/f9b401a64ef78c8dd68143f10796d1d6fd9f94858277c743c6505388b8534a72?s=64&d=mm&r=g) JHarris says:
    
    [June 9, 2015 at 3:22 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-989774)
    
    Subtracting End Time from Start Time works fine as long as both occur on the same day. If one, for ex, starts at 11:00 pm and ends at 5:00 am, straight subtraction yields a negative number. To fix, I used an if statement: if end - start is +, then just subtract end from start, else add 24 to (end - start) to get the correct figure. In each case multiplying by 24 (\*24) transforms the answer from decimal days to hours. I did not format further as I would hours in decimal form to enable further pay calculations.
    
    \=IF(D7-C7>0,(D7-C7)\*24,24+((D7-C7)\*24))
    
    Another good one Chandoo, when is your next dashboard contest???
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-989774)
    
82.  ![](https://secure.gravatar.com/avatar/315092f93ab82d8952eaf86aa917f9d9da8da7bed7ac7eeae1380feba2841a6c?s=64&d=mm&r=g) Subbu says:
    
    [June 10, 2015 at 3:46 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990150)
    
    Hello,
    
    Its working for me..  
    \=IF(D4>C4,D4-C4,1-(C4-D4))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990150)
    
83.  ![](https://secure.gravatar.com/avatar/39509f5bb01b660244f2d78bbc41d999e263f411a1fff3935fdcf5927a5fdc6e?s=64&d=mm&r=g) Brij Arora says:
    
    [June 10, 2015 at 5:12 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990177)
    
    \=IF((D4-C4)>0,(D4-C4)\*24,((D4\*24)+24-(C4\*24)))
    
    number format  
    Hours worked total 44
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990177)
    
84.  ![](https://secure.gravatar.com/avatar/13158ae53eee5b093821c20efae8601a890b7a9122ccd445538cc7949d28e5e9?s=64&d=mm&r=g) Anant Jain says:
    
    [June 10, 2015 at 2:04 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990322)
    
    Answer is  
    \=IF(AND(HOUR(A2)>12,HOUR(B2)<12),24-(HOUR(A2)-HOUR(B2)),HOUR(B2)-HOUR(A2))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990322)
    
85.  ![](https://secure.gravatar.com/avatar/41b8f67fc82483a5243db524afe61a7b8182c0c27ad611b36a8395460a6dcd06?s=64&d=mm&r=g) jay prakash says:
    
    [June 11, 2015 at 3:46 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990919)
    
    \=IF(C4<D4,D4-C4, C4-D4), do it for all cells and then sum , will provide the hours.
    
    Only change the answer cell in format of h:mm:ss
    
    Done it and found OK
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990919)
    
86.  ![](https://secure.gravatar.com/avatar/41b8f67fc82483a5243db524afe61a7b8182c0c27ad611b36a8395460a6dcd06?s=64&d=mm&r=g) jay prakash says:
    
    [June 11, 2015 at 3:47 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990920)
    
    Total Hours is 72 Hrs..
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990920)
    
87.  ![](https://secure.gravatar.com/avatar/9041859041cd28e5aa9263fddc22e53b0075f637771e934134f1982b756bfab9?s=64&d=mm&r=g) [Kevin Lehrbass](https://youtu.be/0D98I73TJeI)
     says:
    
    [June 11, 2015 at 4:21 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990930)
    
    Hi Everyone,
    
    I created a YouTube video to explain my array solution:  
    [https://youtu.be/0D98I73TJeI](https://youtu.be/0D98I73TJeI)
    
    Cheers,  
    Kevin Lehrbass
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990930)
    
88.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [June 11, 2015 at 7:10 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990982)
    
    @Kevin,  
    While your suggested formula works - try a much shorter Array solution: =SUM(D4:D9-C4:C9+(D4:D9<=C4:C9))  
    BTW: upon presenting a single formula - all $$$ signs are useless.  
    Michael (Micky) Avidan  
    “Microsoft® Answers” – Wiki author & Forums Moderator  
    “Microsoft®” MVP – Excel (2009-2015)  
    ISRAEL
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-990982)
    
    *   ![](https://secure.gravatar.com/avatar/9041859041cd28e5aa9263fddc22e53b0075f637771e934134f1982b756bfab9?s=64&d=mm&r=g) [Kevin Lehrbass](https://www.youtube.com/user/MySpreadsheetLab)
         says:
        
        [June 13, 2015 at 7:23 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-992501)
        
        Good point. Thanks Michael.
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-992501)
        
89.  ![](https://secure.gravatar.com/avatar/e7d8fee0dfd2336eca4220b742c56e18f1f7e9f4e78a30c6dc4d145a514ade23?s=64&d=mm&r=g) Uejsi says:
    
    [June 12, 2015 at 7:26 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-991576)
    
    1\. I have used this formula to calculate each row  
    \=IF(D4>"12:00",D4-C4,12-C4+0+D4)  
    2\. i have formatted the result column hh:mm:ss  
    3\. the end i have used only sum function
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-991576)
    
    *   ![](https://secure.gravatar.com/avatar/e7d8fee0dfd2336eca4220b742c56e18f1f7e9f4e78a30c6dc4d145a514ade23?s=64&d=mm&r=g) Uejsi says:
        
        [June 12, 2015 at 7:45 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-991587)
        
        this is the exact formula for each row  
        \=NUMBERVALUE(TEXT(IF(D4>"12:00",D4-C4,12-C4+0+D4),"h"),1)  
        the result cell has normal sum function in total 44 hours
        
        thnx
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-991587)
        
90.  ![](https://secure.gravatar.com/avatar/c114899e0d37b4fa1d167d8a349266178610edbca8a5d6b2d94f63f2d3f8c482?s=64&d=mm&r=g) excel says:
    
    [June 12, 2015 at 9:48 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-991638)
    
    I hope this formula will work  
    \=HOUR(D4+24-C4)  
    and then doing the sum
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-991638)
    
91.  ![](https://secure.gravatar.com/avatar/181ddef99b5f55609d072969e18b20446107cb87d38b077c33a1c4f869f764fb?s=64&d=mm&r=g) Sri Vidya says:
    
    [June 15, 2015 at 6:10 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-993300)
    
    Simplest of all solutions -  
    \=12-C4+D4 🙂
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-993300)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [June 15, 2015 at 11:29 pm](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-993700)
        
        @Sri,  
        Most of the above participants got a total sum of 44 hours and if Billy's hour rate is $20 he will be paid $880.  
        Would you be so kind to check if your sum comes out 44 hours - and if so, to present us the detailed calculation regarding the payment ?  
        Thanks,  
        Michael (Micky) Avidan  
        “Microsoft® Answers” – Wiki author & Forums Moderator  
        “Microsoft®” MVP – Excel (2009-2015)  
        ISRAEL
        
        [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-993700)
        
92.  ![](https://secure.gravatar.com/avatar/42b3dae989688d8365b7571765e3e8f66642bfe9a1ac9d9ea56cafe39d097eb1?s=64&d=mm&r=g) Luís Pires says:
    
    [June 18, 2015 at 10:49 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-996320)
    
    \=+MOD(+D3-C3;1)\*24 and copy the formula down
    
    44 Hours too...
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-996320)
    
93.  ![](https://secure.gravatar.com/avatar/40f2ccba22a5adee0b3e95ae1ab75c77592228292bc6baffcb989411e89af70a?s=64&d=mm&r=g) Micheal Poh says:
    
    [June 19, 2015 at 6:01 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-996966)
    
    \=D4+12-C4  
    \=D5+12-C5  
    \=D6+12-C6  
    \=D7+12-C7  
    \=D8+12-C8  
    \=D9+12-C9
    
    i used the formula above and change the cells format to Custom H(Hours).  
    But i cannot get the sum of the total of Mr Willy.
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-996966)
    
94.  ![](https://secure.gravatar.com/avatar/82df41c336ab3bc3fb45c1c58c07c4904f2445282746041e9b084b78fd43422a?s=64&d=mm&r=g) Vijay Dhangar says:
    
    [June 22, 2015 at 6:37 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-998384)
    
    what if there are more than 1 person??
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-998384)
    
95.  [Provocare Excel pentru a calcula numarul de ore lucrate](http://invatamexcel.ro/2015/06/provocare-calcul-ore-lucru-chandoo/)
     says:
    
    [June 22, 2015 at 7:09 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-998390)
    
    \[…\] In actualizarea saptamanala, am dat peste o provocare Excel care la prima vedere parea foarte simpla. (How many hours did Billy work?) \[…\]
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-998390)
    
96.  ![](https://secure.gravatar.com/avatar/868a314d82b041b4061962030b1ec15ab927c67a9a6f1fb2c04c7bb73fc3c476?s=64&d=mm&r=g) Zak says:
    
    [June 30, 2015 at 2:01 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-1002055)
    
    Hi,
    
    here is mine :
    
    \=IF(D4<C4,(D4+1)-C4,D4-C4)\*24 (general format)
    
    total 44 hours
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-1002055)
    
97.  ![](https://secure.gravatar.com/avatar/894a5841d14d0373996076ea210c2543530d084c5c815af5a11c63bda41be68e?s=64&d=mm&r=g) Marydas Joseph says:
    
    [June 12, 2016 at 11:51 am](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-1211276)
    
    \=IF(HOUR(D4)<HOUR(C4),(HOUR(D4)-HOUR(C4))+25,(HOUR(D4)-HOUR(C4)+1))
    
    [Reply](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#comment-1211276)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/how-many-hours-did-billy-work-solve-this/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Changing stubborn opinions with visualizations \[case study\]](https://chandoo.org/wp/changing-opinions-with-visualizations/) | [What functions is Excel missing ?](https://chandoo.org/wp/what-functions-is-excel-missing/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)