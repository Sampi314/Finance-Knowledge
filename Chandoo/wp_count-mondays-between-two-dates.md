# How many Mondays between two dates? [homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/count-mondays-between-two-dates

---

How many Mondays between two dates? \[homework\]
================================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 138 comments

  

![count-of-mondays-between-two-dates](https://chandoo.org/wp/wp-content/uploads/2015/12/count-of-mondays-between-two-dates-v2.png)Here is a quick but challenging homework problem for you.

Let’s say you have two dates – _Start_ and _End_.

And you want to find out how many Mondays are there between those two dates (including the start & end dates).

**What formula would give the answer?**

Please post your formulas / VBA functions / DAX measures in the comments section.

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
| Written by Chandoo  <br>Tags: [date and time](https://chandoo.org/wp/tag/date-and-time/)<br>, [homework](https://chandoo.org/wp/tag/homework/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [no-nl](https://chandoo.org/wp/tag/no-nl/)<br>, [weekday](https://chandoo.org/wp/tag/weekday/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 138 Responses to “How many Mondays between two dates? \[homework\]”

1.  ![](https://secure.gravatar.com/avatar/2e6abaf5ac49344b95f76181c0d2c52d1cb33bf95c3606caec5af112482bfc3d?s=64&d=mm&r=g) [MF](http://wmfexcel.com/)
     says:
    
    [December 18, 2015 at 12:16 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107795)
    
    I have a post related to this question:  
    Calculate number of a specific day between two dates | wmfexcel  
    [http://wmfexcel.com/2014/04/12/calculate-number-of-a-specific-day-between-two-dates/](http://wmfexcel.com/2014/04/12/calculate-number-of-a-specific-day-between-two-dates/)
      
    Hope you like it!  
    Merry Christmas in advance!
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107795)
    
2.  ![](https://secure.gravatar.com/avatar/04b5a93edbc655803abe74ca9048a5e604383b69481c0cb5e200048e7b6d86e4?s=64&d=mm&r=g) prashant says:
    
    [December 18, 2015 at 12:24 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107796)
    
    for Excel 2010 & above
    
    \=WORKDAY.INTL(SD,ED-SD,12)-ED
    
    SD ED are start date & end date resp.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107796)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [December 18, 2015 at 1:09 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107808)
        
        If I'm not mistake there are 8 Mondays between 01/12/2015 and  
        31/01/2016.  
        Your formula retures: 10
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107808)
        
        *   ![](https://secure.gravatar.com/avatar/a99fde22ba553e95374b55cf95b4330a73402730a0061854eac75bb90c31242d?s=64&d=mm&r=g) Chandra Mohan says:
            
            [January 6, 2016 at 6:16 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1116742)
            
            \=ED-SD-NETWORKDAYS.INTL(SD,ED,12)+1, try this formula
            
            [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1116742)
            
3.  ![](https://secure.gravatar.com/avatar/f1cbf1a4af71dffb50efc0bdee625dc93fdd8ad9159ca3d7e1dd74ac8cca75ea?s=64&d=mm&r=g) Bob Phillips says:
    
    [December 18, 2015 at 12:51 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107804)
    
    Your solution might be a tad more efficient using a numeric test rather than a string test
    
    \=SUMPRODUCT(--(WEEKDAY(ROW(INDIRECT(B1&":"&B2)))=2))
    
    It might also be worth pointing out that the dates in B1 & B2 can be any order, B1 does not have to be the earlier date.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107804)
    
    *   ![](https://secure.gravatar.com/avatar/6fc25b9e2eccf76659f8e059a87723e8e15c2dd69b460bdb3164734031f6416e?s=64&d=mm&r=g) Mark says:
        
        [December 22, 2015 at 7:45 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109239)
        
        Hi Bob,  
        Love the solution, very neat and crisp. Even though i use the functions in your solution and i still confused about the row(Indirect(B1&":"&B2)) bit.
        
        To take a simple example If B1 was 2 and B2 was 6 what would Indirect(2:6) evaluate to?
        
        Applying the row function to this then yields the actual values of the reference range (2;3;4;5;6).
        
        Would you mind explaining a little if its not too much for you?
        
        Thanks
        
        Mark
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109239)
        
        *   ![](https://secure.gravatar.com/avatar/b3b4be10492adf5b38e569234355addeda41b24d897c72178d52a371c15513f7?s=64&d=mm&r=g) NARAYAN says:
            
            [December 27, 2015 at 1:43 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1112162)
            
            Hi Mark ,
            
            Let us start from the outside and move inwards.
            
            It is clear that we need a function to sum values ; since this has to operate on an array of values , SUMPRODUCT is an obvious choice.
            
            Now we need an array of values , which will have 1 for a Monday , and 0 for all other days of the week. This we can get by using the WEEKDAY function , and checking whether it returns the value for a MONDAY. Depending on the second parameter of the WEEKDAY function , the value used for checking will change.
            
            The default value for this second parameter is 1 , and this gives the weekdays from 1 through 7 , with 1 signifying Sunday , and 7 signifying Saturday ; thus , in this set , Monday would be 2.
            
            Now , we need to pass an array of dates to the WEEKDAY function ; this will be an array of dates from StartDate through EndDate , both dates inclusive.
            
            This we can do using the ROW function.
            
            Unfortunately , the ROW function acts on values , not on cell references ; thus , given the formula :
            
            \=ROW(7:17)
            
            we get an array of values {7;8;9;10;11;12;13;14;15;16;17}.
            
            To get the same array of values using cell references , we would need to use :
            
            \=ROW(A7:A17)
            
            Any other column reference can be used in place of column A e.g.
            
            \=ROW(IX7:IX17)
            
            would return the same array of values from 7 through 17.
            
            The situation we have in our case is that the StartDate is in a cell reference B1 , and the EndDate is in another cell reference. Using these references directly , as in :
            
            \=ROW(B1:B2)
            
            would only result in an array of two values {1;2} !
            
            Thus , to use the values of StartDate and EndDate through their cell references , one way would be to use the INDIRECT function ( there are other ways too ).
            
            The complication here is that the INDIRECT function takes in parameters which are strings ; hence we cannot use :
            
            \=ROW(INDIRECT(B1:B2))
            
            To generate the string for the INDIRECT function , we use the CONCATENATE function , or its shortcut , the & symbol. Hence :
            
            \=ROW(INDIRECT(B1 & ":" & B2))
            
            This generates an array of values from the StartDate through the EndDate , both dates inclusive.
            
            [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1112162)
            
            *   ![](https://secure.gravatar.com/avatar/6fc25b9e2eccf76659f8e059a87723e8e15c2dd69b460bdb3164734031f6416e?s=64&d=mm&r=g) Mark says:
                
                [January 13, 2016 at 4:58 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1119334)
                
                Hi Narayan,
                
                I have only just seen your reply to my question.
                
                Thank you for taking the time to explain this to me.
                
                I'm much clearer on how it works now.
                
                tnx
                
                Mark
                
                [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1119334)
                
        *   ![](https://secure.gravatar.com/avatar/badcf0a91dcdcb2ca6a7421d73bb477122d6771c408e82930a883ecb5ab6ab55?s=64&d=mm&r=g) Jan Martens says:
            
            [December 29, 2015 at 10:33 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1113966)
            
            [http://www.emailoffice.com/excel/arrays-bobumlas.html](http://www.emailoffice.com/excel/arrays-bobumlas.html)
              
            Here you can learn a lot about array formulas.
            
            [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1113966)
            
            *   ![](https://secure.gravatar.com/avatar/6fc25b9e2eccf76659f8e059a87723e8e15c2dd69b460bdb3164734031f6416e?s=64&d=mm&r=g) Mark says:
                
                [January 13, 2016 at 5:00 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1119336)
                
                Thanks Jan, there are some pretty cool array examples there!
                
                [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1119336)
                
        *   ![](https://secure.gravatar.com/avatar/45045fe4a850624f1372622fc56c4b94e3271015417d7e8a0ea8699272e30774?s=64&d=mm&r=g) [Jan](https://www.excelxl.nl/)
             says:
            
            [August 16, 2022 at 6:01 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-2085827)
            
            Hé Bob,
            
            It may be a few years ago but this is the most beautiful solution I came accros till now.
            
            Cheers,  
            Jan
            
            [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-2085827)
            
4.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [December 18, 2015 at 1:04 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107807)
    
    \=SUMPRODUCT(N(WEEKDAY(ROW(INDIRECT(SD&":"&ED)))=2))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107807)
    
    *   ![](https://secure.gravatar.com/avatar/df0b44d7b75149ecb0ea0fe964e98cf037d378927602c7ff818a764e9794e463?s=64&d=mm&r=g) TheQ47 says:
        
        [December 18, 2015 at 2:28 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107825)
        
        I like that one, Micky. I never saw the "N" Formula, it's a very useful one.
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107825)
        
    *   ![](https://secure.gravatar.com/avatar/78a0e0f7d76cd3514709daa4c43cc184373d514b2cf2dcebad4b9ea75a569d7e?s=64&d=mm&r=g) Steve says:
        
        [October 6, 2020 at 1:08 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1895117)
        
        many thanks!
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1895117)
        
    *   ![](https://secure.gravatar.com/avatar/45045fe4a850624f1372622fc56c4b94e3271015417d7e8a0ea8699272e30774?s=64&d=mm&r=g) [Jan](https://www.excelxl.nl/)
         says:
        
        [August 16, 2022 at 6:02 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-2085828)
        
        Hé Mike,
        
        I like your formula too and like the formula of Bob, this is also one of the most beautiful solutions.
        
        Cheers Jan
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-2085828)
        
5.  ![](https://secure.gravatar.com/avatar/d0e20486c3ec04dab02e38c7b8d2ff533cc2041a85dbee988a5ba56344243749?s=64&d=mm&r=g) mahesh says:
    
    [December 18, 2015 at 3:12 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107839)
    
    hi prashant  
    sd:11/2/2015  
    ed:11/18/2015  
    result :2 this is wrong
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107839)
    
6.  ![](https://secure.gravatar.com/avatar/b28b5b667fa0ee8187e7c0b541e29d6324a22e40c23e6f7bfbd9321114b50436?s=64&d=mm&r=g) Bertrand says:
    
    [December 18, 2015 at 3:14 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107840)
    
    In DAX, assuming you have a Date table
    
    EVALUATE  
    ROW (  
    "Count of Mondays", COUNTROWS (  
    FILTER (  
    DateTable,  
    DateTable\[Date\] > DATEVALUE ( "2014-12-31" )  
    && DateTable\[Date\] < TODAY ()  
    && WEEKDAY ( DateTable\[Date\] ) = 2  
    )  
    )  
    )
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107840)
    
7.  ![](https://secure.gravatar.com/avatar/0b87c2a05bd7fb5348138fb6dedfbf782a1ac44367c0368cf69084ec4550dfe8?s=64&d=mm&r=g) Bill says:
    
    [December 18, 2015 at 3:19 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107846)
    
    Mine certainly isn't the shortest formula, but is more intuitive for me to understand:  
    \=QUOTIENT((End-Start),7) + OR(WEEKDAY(Start)=2,WEEKDAY(End)=2)
    
    The second term covers the case where the start or the end date is on a Monday, which is needed to cover for partial weeks.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107846)
    
    *   ![](https://secure.gravatar.com/avatar/0b87c2a05bd7fb5348138fb6dedfbf782a1ac44367c0368cf69084ec4550dfe8?s=64&d=mm&r=g) Bill says:
        
        [December 18, 2015 at 3:49 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107856)
        
        never mind - that doesn't work for periods less than 7 days
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107856)
        
8.  ![](https://secure.gravatar.com/avatar/51615fd2b86a599068efb7881d15b9fba254c4f073c81b308a164dcc40f17ea7?s=64&d=mm&r=g) Gianluca says:
    
    [December 18, 2015 at 3:31 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107851)
    
    \=INT((ED-SD-WEEKDAY(SD,3)-WEEKDAY(ED,3))/7)+1
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107851)
    
    *   ![](https://secure.gravatar.com/avatar/51615fd2b86a599068efb7881d15b9fba254c4f073c81b308a164dcc40f17ea7?s=64&d=mm&r=g) Gianluca says:
        
        [December 18, 2015 at 4:58 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107877)
        
        Not working for periods less than 7 days...  
        This should fix the problem:  
        \=INT((ED-SD+7)/7)-AND(WEEKDAY(SD,3)>0;WEEKDAY(ED,3)>0)
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107877)
        
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [December 18, 2015 at 5:03 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107880)
        
        @Gianluca,  
        January 2016 has 3 Mondays (1/1/2016-31/1/2016)  
        Your suggested formula returns: 3
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107880)
        
        *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [December 18, 2015 at 5:04 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107881)
            
            Sorry for the TIPO:  
            January 2016 has 4 Mondays (1/1/2016-31/1/2016)
            
            [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107881)
            
            *   ![](https://secure.gravatar.com/avatar/51615fd2b86a599068efb7881d15b9fba254c4f073c81b308a164dcc40f17ea7?s=64&d=mm&r=g) Gianluca says:
                
                [December 18, 2015 at 6:53 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107907)
                
                @Michael  
                the formula returns 4 for DS=1/1/2016 and SD=31/1/2016.  
                The result is correct.
                
                [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107907)
                
                *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                    
                    [December 18, 2015 at 7:06 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107914)
                    
                    @Gianluca,  
                    I was referring to your first(!) formula.  
                    (You posed a new and longer one WHILE I was typing my comments).  
                    The last one works OK - however, as there might be many sorts of formulas - I always look for shorter formulas.  
                    So far the:  
                    \=SUMPRODUCT(N(WEEKDAY(ROW(INDIRECT(B1&":"&B2)))=2))  
                    is the shortest that also works as expected.
                    
                *   ![](https://secure.gravatar.com/avatar/51615fd2b86a599068efb7881d15b9fba254c4f073c81b308a164dcc40f17ea7?s=64&d=mm&r=g) Gianluca says:
                    
                    [December 19, 2015 at 12:40 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108016)
                    
                    @Michael (reply to post below)  
                    Shorter then your shortest... (array formula)
                    
                    \={INT((ED-SD+7)/7)-AND(WEEKDAY(SD:ED,3)>0)}
                    
9.  ![](https://secure.gravatar.com/avatar/e620c9825aa79a10ce2bec572c880e2563c41df6af81459ad3edc0a33143e1be?s=64&d=mm&r=g) Harold Mude says:
    
    [December 18, 2015 at 3:53 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107858)
    
    How about this one:
    
    \=(WEEKDAY(SD,2)=1)+QUOTIENT(ED-SD,7)+(WEEKDAY(ED,2)<WEEKDAY(SD,2))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107858)
    
10.  ![](https://secure.gravatar.com/avatar/e620c9825aa79a10ce2bec572c880e2563c41df6af81459ad3edc0a33143e1be?s=64&d=mm&r=g) Harold Mude says:
    
    [December 18, 2015 at 3:56 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107859)
    
    Btw. the picture above has Sundays marked.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107859)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [December 18, 2015 at 4:02 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107861)
        
        @Harold... thanks mate. Fixed the error now.
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107861)
        
11.  ![](https://secure.gravatar.com/avatar/6719e22b4f610ee109ac36e01113ea3385de0e2f7d60f5737502fb8394912b60?s=64&d=mm&r=g) Mehmet Gunal OLCER says:
    
    [December 18, 2015 at 4:03 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107862)
    
    \=IF(WEEKDAY(FIRSTDAY,11)=1,1,0)+INT(DAYS(LASTDAY,FIRSTDAY)/7)+IF(MOD(DAYS(LASTDAY,FIRSTDAY),7)+WEEKDAY(FIRSTDAY,11)>7,1,0)
    
    Where LASTDAY is assumed to be later or equal to FIRSTADAY.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107862)
    
    *   ![](https://secure.gravatar.com/avatar/6719e22b4f610ee109ac36e01113ea3385de0e2f7d60f5737502fb8394912b60?s=64&d=mm&r=g) Mehmet Gunal OLCER says:
        
        [December 21, 2015 at 6:15 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109020)
        
        Let me give another solution.
        
        \=ABS(INT((N(DAY\_2)-2)/7)-INT((N(DAY\_1)-2)/7))
        
        where DAY\_1 and DAY\_2 are two DIFFERENT dates.
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109020)
        
        *   ![](https://secure.gravatar.com/avatar/4bbda39a219bcf8603b2844f613bf1f90452619b5ddc5b0ba2abb62201253199?s=64&d=mm&r=g) Karthik says:
            
            [June 28, 2018 at 1:08 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1555469)
            
            Worked!!
            
            [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1555469)
            
12.  ![](https://secure.gravatar.com/avatar/e1aab4a2a9c37a7e2d5b564567f30a085d643132eee1e50cd8c1d3e92be2cf68?s=64&d=mm&r=g) Josh Saavoss says:
    
    [December 18, 2015 at 4:19 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107868)
    
    Function monday\_count(date1 As Date, date2 As Date)  
    Dim i As Long: Dim count As Long  
    For i = date1 To date2  
    If Weekday(i) = 2 Then count = count + 1  
    Next i  
    monday\_count = count  
    End Function
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107868)
    
13.  ![](https://secure.gravatar.com/avatar/a49db62c450d92ee3555e3d457441297cb40b7cf6c822daaf4e847d477a303e6?s=64&d=mm&r=g) Ashish says:
    
    [December 18, 2015 at 5:56 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107894)
    
    \=SUMPRODUCT(WEEKDAY(ROW(INDIRECT(VALUE(A1)&":"&VALUE(A2))))=2)\*1)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107894)
    
14.  ![](https://secure.gravatar.com/avatar/dee68165e6e8f1255e87bc5790cfab75b5d8ee6c87bf687e622133f516c40551?s=64&d=mm&r=g) Jeff Fordon says:
    
    [December 18, 2015 at 7:03 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107912)
    
    \=IF(MOD(Start,INT(Start/7))=2,1)+INT(End/7)-INT(Start/7)-1
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107912)
    
15.  ![](https://secure.gravatar.com/avatar/dee68165e6e8f1255e87bc5790cfab75b5d8ee6c87bf687e622133f516c40551?s=64&d=mm&r=g) Jeff 1 says:
    
    [December 18, 2015 at 7:06 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107913)
    
    typo, should be
    
    \=IF(MOD(Start,INT(Start/7))=2,1)+INT(End/7)-INT(Start/7)-1
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107913)
    
16.  ![](https://secure.gravatar.com/avatar/0446f53a29ce21f4620e930e762bc2f5891b705a22e205ad098b5eb1688ed1d0?s=64&d=mm&r=g) Jon says:
    
    [December 18, 2015 at 7:28 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107920)
    
    \=MAX(ROUNDUP(((A2-A1+1)+(IF(WEEKDAY(A1)>2,WEEKDAY(A1)-9,WEEKDAY(A1)-2)))/7,0),0)
    
    Where A1 = Start Date  
    A2 = End date
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107920)
    
17.  ![](https://secure.gravatar.com/avatar/05420156d3197db4a5eee5d4d905855bcd77c673917ee410c3f15ec902f829fc?s=64&d=mm&r=g) Gopi Krishna says:
    
    [December 18, 2015 at 7:37 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107925)
    
    \=IF(AND(WEEKDAY(F15,1)=2,WEEKDAY(G15,1)=2),QUOTIENT((G15-1)-(F15+1),7)+2,IF(OR(WEEKDAY(F15,1)=2,WEEKDAY(G15,1)=2),QUOTIENT((G15-1)-(F15+1),7)+1,QUOTIENT((G15-F15),7)))
    
    Will return the number of Mondays.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107925)
    
    *   ![](https://secure.gravatar.com/avatar/05420156d3197db4a5eee5d4d905855bcd77c673917ee410c3f15ec902f829fc?s=64&d=mm&r=g) Gopi Krishna says:
        
        [December 18, 2015 at 8:29 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107942)
        
        The above formula will return incorrect number of Mondays if the start date and end date are same..
        
        The following formula will return correct number of Mondays..
        
        \=IF(AND(G15=F15,WEEKDAY(G15,1)=2),1,IF(G15>=F15,IF(AND(WEEKDAY(F15,1)=2,WEEKDAY(G15,1)=2),QUOTIENT((G15-1)-(F15+1),7)+2,IF(OR(WEEKDAY(F15,1)=2,WEEKDAY(G15,1)=2),QUOTIENT((G15-1)-(F15+1),7)+1,QUOTIENT((G15-F15),7))),"Start Date later than End Date"))
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107942)
        
18.  ![](https://secure.gravatar.com/avatar/0565c6efb7fa1eacf83ccdd9383edfb3ce01f085b7bc053463df9af6cdf34257?s=64&d=mm&r=g) Darin Scott says:
    
    [December 18, 2015 at 8:07 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107930)
    
    Here is my try at this:  
    \={SUM((E:E>=StartDate)\*(E:E<=StopDate)\*(WEEKDAY(E:E)=DayChosen)/DayChosen\*(WEEKDAY(E:E)))}
    
    Where Col E contains dates  
    StartDate & StopDates are input cells  
    DayChosen is a dropdown list Sun, Mon, Tue,... which converts to 7,1,2,... based on day chosen
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107930)
    
19.  ![](https://secure.gravatar.com/avatar/0446f53a29ce21f4620e930e762bc2f5891b705a22e205ad098b5eb1688ed1d0?s=64&d=mm&r=g) Jon says:
    
    [December 18, 2015 at 8:13 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107932)
    
    \=MAX(ROUNDUP(((A2-A1+1)+(IF(WEEKDAY(A1)>2,WEEKDAY(A1)-9,WEEKDAY(A1)-2)))/7,0),0)
    
    Where:  
    A1 = Start date  
    A2 = End Date
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107932)
    
20.  ![](https://secure.gravatar.com/avatar/4bb8870542393cb78925d77ff713c114e9f9cc467c10cc6fa85d565ebe95285c?s=64&d=mm&r=g) ramjiyahoo says:
    
    [December 18, 2015 at 8:14 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107934)
    
    Google gives easy answer thru this website
    
    [http://www.easysurf.cc/wdate2.htm](http://www.easysurf.cc/wdate2.htm)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107934)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [December 19, 2015 at 9:14 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108136)
        
        L-O-L !!!
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108136)
        
21.  ![](https://secure.gravatar.com/avatar/2d28f193bbabab174ca28c3e043e3d4582f132815f5e5f524b2e87010f41f1f4?s=64&d=mm&r=g) [Daniel Lamarche](http://www.comboprojects.com.au/)
     says:
    
    [December 18, 2015 at 8:28 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107941)
    
    Sorry for me VBA is easier to use across workbooks...
    
    Function HowManyMonday(datStart As Date, datEnd As Date)  
    ' Returns the number of Mondays between two dates.  
    Dim i As Long, j As Integer
    
    For i = datStart To datEnd
    
    j = j + Abs(Weekday(i, vbMonday) = 1)  
    Next i  
    HowManyMondays = j  
    End Function
    
    In VBA Weekday(i, vbMonday) = 1 returns TRUE which equals -1 that is why ABS is used. A minus would do the same but more obscure.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107941)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [December 18, 2015 at 8:55 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107947)
        
        @Daniel,  
        You have a slight TIPO in the Function's Name.  
        If I may suggest (especially for Maintenance & User Friendly reasons) the following UDF:  
        Function HowManyMondays(datStart As Date, datEnd As Date, D As Integer)  
        ' Returns the number of days "D" between two dates.  
        Dim i As Long, j As Integer  
        For i = datStart To datEnd  
        HowManyMondays = HowManyMondays + Abs(Weekday(i, D) = 1)  
        Next i  
        End Function
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107947)
        
        *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [December 18, 2015 at 9:11 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107953)
            
            As a better praxis the UDF's name should be changed to: HowMany\_D\_Days
            
            [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107953)
            
            *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                
                [December 18, 2015 at 9:12 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107954)
                
                Function HowMany\_D\_Days(datStart As Date, datEnd As Date, D As Integer)  
                ‘ Returns the number of days “D” between two dates.  
                Dim i As Long, j As Integer  
                For i = datStart To datEnd  
                HowMany\_D\_Days = HowMany\_D\_Days + Abs(Weekday(i, D) = 1)  
                Next i
                
                [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107954)
                
22.  ![](https://secure.gravatar.com/avatar/ffc701a3c1060e6b93a400ff058c7e34b0818044748120eed3f261a8ca8be969?s=64&d=mm&r=g) Gordon says:
    
    [December 18, 2015 at 8:32 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107943)
    
    \=IF(SD<=ED,INT(WEEKDAY(SD,12)/7)+ INT((ED-SD+WEEKDAY(SD,3))/7),"error -start date is after end date")  
    \---  
    Amazed at the variety of answers - my formula is a little bit wasteful. I am sure there is a simpler way, but I tested it and it works.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107943)
    
23.  ![](https://secure.gravatar.com/avatar/7bbd3375773d818af330ee8e3ea6b839409e5281c0b66372301352a10fff8ad6?s=64&d=mm&r=g) Jason Morin says:
    
    [December 18, 2015 at 10:14 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107976)
    
    \=SUMPRODUCT(--(MOD(ROW(INDIRECT(start&":"&end)),7)=2))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107976)
    
24.  ![](https://secure.gravatar.com/avatar/72cad38f40e66afa87d23757ebeeb95836f0e50ce83e812f0f852879f9d75f51?s=64&d=mm&r=g) K?vanç Y?ld?z says:
    
    [December 18, 2015 at 10:32 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107982)
    
    #1 =SUMPRODUCT(--(TEXT(ROW(INDIRECT(SD&":"&ED)),"DDDD")="Sunday"))  
    But this formula is English.
    
    Turkish formula use "GGGG"  
    \=TOPLA.ÇARPIM(--(METNEÇEV?R(SATIR(DOLAYLI(SD&":"&ED));"GGGG")="Pazartesi"))
    
    #2 =SD-ED+1-NETWORKDAYS.INTL(SD;ED;12)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107982)
    
    *   ![](https://secure.gravatar.com/avatar/72cad38f40e66afa87d23757ebeeb95836f0e50ce83e812f0f852879f9d75f51?s=64&d=mm&r=g) Kivanç Yildiz says:
        
        [December 18, 2015 at 10:38 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107984)
        
        correction
        
        \=SUMPRODUCT(–(TEXT(ROW(INDIRECT(SD&”:”&ED)),”DDDD”)=”Monday”))
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1107984)
        
25.  ![](https://secure.gravatar.com/avatar/37126bca5b2d642974940c98f7a8241b321d0f5c21e32fb204d414d88c874564?s=64&d=mm&r=g) Leonid says:
    
    [December 19, 2015 at 1:20 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108024)
    
    \=SUMPRODUCT(N(WEEKDAY(ROW(INDEX(A:A,StartDate,):INDEX(A:A,Enddate,)),2)=1))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108024)
    
26.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [December 19, 2015 at 9:02 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108133)
    
    @Gianluca:  
    As for your really short formula (posted December 19, 2015 at 12:40 am) Please check it against:  
    SD = 01/01/2016  
    ED = 28/09/2016  
    It should return: 39 (not 38)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108133)
    
27.  ![](https://secure.gravatar.com/avatar/e2768799d3e4d5312fe7e1eedb8c176192ad92ba9f63a93d30ebe175b82fb529?s=64&d=mm&r=g) Lewis Kirby says:
    
    [December 19, 2015 at 9:02 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108134)
    
    Here's mine:  
    \=((A2-WEEKDAY(A2,3))-(A1-WEEKDAY(A1, 3)))/7+IF(WEEKDAY(A1,3)=0,1,0)  
    Using WEEKDAY(A1,3) gives you 0 for Monday, then subtracting the two and dividing by 7: ((A2-..)-(A1-..))/7 gives the number of Mondays, but not if the first date A1 is a Monday, so we have to add 1 in that case.
    
    BTW what is the advantage of using the function QUOTIENT instead of simply dividing?
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108134)
    
28.  ![](https://secure.gravatar.com/avatar/37651747824d1dd297ce5ad3bab40f4a85976821b56edeaddf4272788a5c5984?s=64&d=mm&r=g) SAGAR MOHITE says:
    
    [December 19, 2015 at 9:21 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108139)
    
    \=ROUNDDOWN((((A2-A1+1)-CHOOSE(WEEKDAY(A1),1,0,6,5,4,3,2))/7)+1,0)
    
    START DATE - A1  
    END DATE - A2
    
    S, M, T, W, T, F, S = 1, 0, 6, 5, 4, 3, 2
    
    Which day you want to count arrenge serial no. that way i.e. Monday = 0
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108139)
    
29.  ![](https://secure.gravatar.com/avatar/5601b5edf6c47c4fc693b8b1fe35aeb5d51a743fb779a55e2ddf8140ec970bcb?s=64&d=mm&r=g) Alan says:
    
    [December 19, 2015 at 1:05 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108189)
    
    FREQUENCY(N(WEEKDAY(ROW(INDIRECT(A1&":"&B1)),2)),1)  
    if only for Mondays
    
    SUM(--(TEXT(ROW(INDIRECT(A1&":"&B1)),"DDD")="Mon"))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108189)
    
30.  ![](https://secure.gravatar.com/avatar/badcf0a91dcdcb2ca6a7421d73bb477122d6771c408e82930a883ecb5ab6ab55?s=64&d=mm&r=g) Jan Martens says:
    
    [December 19, 2015 at 1:05 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108190)
    
    Hi  
    INT(DATEDIF(SD+7-WEEKDAY(SD,3),ED,"d"))/7)+1
    
    Where Monday is the first day of the week.
    
    If SD=Monday and this Monday should be included, then ((Weekday, 3) =1)\*1 +formula
    
    Have a good day.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108190)
    
31.  ![](https://secure.gravatar.com/avatar/5601b5edf6c47c4fc693b8b1fe35aeb5d51a743fb779a55e2ddf8140ec970bcb?s=64&d=mm&r=g) Alan says:
    
    [December 19, 2015 at 2:18 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108207)
    
    This appears to work  
    SUM(N(MOD(ROW(OFFSET(A1,SD-1,,ED-SD+1)),7)=2))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108207)
    
32.  ![](https://secure.gravatar.com/avatar/382310a95f1b149441c2444266e7c8d3db8ce155c792c3be1e117a6dcbc5697b?s=64&d=mm&r=g) Mindaugas says:
    
    [December 19, 2015 at 8:08 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108276)
    
    \=TRUNC((A2-A1+1)/7;0)+IF((WEEKDAY(A2;2)-MOD(A2-A1+1;7))>0;0;1)
    
    START DATE – A1  
    END DATE – A2
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108276)
    
33.  ![](https://secure.gravatar.com/avatar/67204ad7edbdda7021a257a99efc16b46e405a4c87bc23f0e920d92970a3dd01?s=64&d=mm&r=g) mma173 says:
    
    [December 19, 2015 at 8:43 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108286)
    
    Guys,
    
    Why are you proposing complicated solutions?
    
    IMHO, the easiest way would be to get the floor of (the difference between SD, ED, and the adjustment to first Monday using Weekday) / 7.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108286)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [December 19, 2015 at 10:51 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108322)
        
        @mma173,  
        As per your verbal explanation - would you be kind enough to present the actual FORMULA(!) that returns: 66 FRIDAYs for:  
        SD = 01/01/2016  
        ED = 31/03/2017  
        Thanks.
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108322)
        
        *   ![](https://secure.gravatar.com/avatar/67204ad7edbdda7021a257a99efc16b46e405a4c87bc23f0e920d92970a3dd01?s=64&d=mm&r=g) mma173 says:
            
            [December 20, 2015 at 6:54 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108442)
            
            Without the Floor part, the formula should look something like:  
            \=((End Date-Start Date)+(7-(WEEKDAY(Start Date)-2)))/7+1
            
            I forgot to mention the (+1) required to include the first Monday.  
            You can also simplify the adjustment part.
            
            Thanks'
            
            [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108442)
            
            *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                
                [December 20, 2015 at 7:27 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108448)
                
                mma173,  
                Sorry, but if you find it difficult to present a FULL FORMULA (without "look something like") - I have nothing more to say.  
                Thanks.
                
                [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108448)
                
            *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
                
                [December 20, 2015 at 7:31 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108450)
                
                @mma173,  
                ...by the way I presume that Chandoo's basic meaning was that the requested formula should work as expected by counting all sort of weekdays (not only Mondays).
                
                [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108450)
                
                *   ![](https://secure.gravatar.com/avatar/67204ad7edbdda7021a257a99efc16b46e405a4c87bc23f0e920d92970a3dd01?s=64&d=mm&r=g) mma173 says:
                    
                    [December 20, 2015 at 7:54 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108460)
                    
                    The formula I presented is the full formula. I tried it and it works. Sorry for using the wrong English expression ????
                    
                    Moreover, it can be adjusted to count another day of the week.
                    
34.  ![](https://secure.gravatar.com/avatar/af9c36e894208706c0f4a00fd53509566b31960ed97d299710ac84286578b65e?s=64&d=mm&r=g) Danny Baetens says:
    
    [December 20, 2015 at 7:45 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108455)
    
    \=IF(WEEKDAY(enddate;2)=1; 1+ INTEGER(DAYS(enddate;startdate)/7); INTEGER(DAYS(enddate;startdate)/7))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108455)
    
35.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [December 20, 2015 at 8:11 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108463)
    
    @mma173,  
    Please examine the linked picture:  
    [http://screenpresso.com/=EAOEg](http://screenpresso.com/=EAOEg)
      
    Thanks.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108463)
    
    *   ![](https://secure.gravatar.com/avatar/67204ad7edbdda7021a257a99efc16b46e405a4c87bc23f0e920d92970a3dd01?s=64&d=mm&r=g) mma173 says:
        
        [December 20, 2015 at 9:45 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108486)
        
        Thanks' for your interest.  
        The adjustment part was incorrect. Check this now:
        
        \=(End Date - (Start Date + MOD((7-(WEEKDAY(Start Date)-Weekday(Monday),7)))/7+1
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108486)
        
        *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [December 20, 2015 at 11:09 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108505)
            
            Sorry, but I gave up.
            
            [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108505)
            
36.  ![](https://secure.gravatar.com/avatar/ef40bf426380d26563f3b3963fc048c6fbdbb7233dde0b6cc983eaeeb616b9ab?s=64&d=mm&r=g) Abhijeet says:
    
    [December 20, 2015 at 11:07 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108503)
    
    Hi
    
    This macro pull all Mondays then cout  
    Dim dStart As Date  
    Dim dEnd As Date  
    Dim rw As Integer
    
    dStart = Range("A2").Value  
    dEnd = Range("A3").Value
    
    rw = 2  
    While dStart < dEnd  
    If Weekday(dStart) = vbMonday Then  
    Cells(rw, 3).Value = dStart  
    Cells(rw, 3).NumberFormat = "m/d/yyyy"  
    rw = rw + 1  
    End If  
    dStart = dStart + 1  
    Wend
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108503)
    
37.  ![](https://secure.gravatar.com/avatar/a7890c31ea949cf6a8644baacb70dd053eb1954b713a669a799b7c09a2ecb01c?s=64&d=mm&r=g) param nayak says:
    
    [December 20, 2015 at 11:15 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108507)
    
    a mathematicl approach
    
    \=INT((A2-A1+1)/7)+IF(AND(MOD((A2-A1+1),7)+WEEKDAY(A1,2)-1<=7,WEEKDAY(A1,2)1),0,1)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108507)
    
38.  ![](https://secure.gravatar.com/avatar/7172db04de729c130c11ae51bd08f28faea7ec5cfd74ffe8368e7b96fa34ffe3?s=64&d=mm&r=g) Denys Calvin says:
    
    [December 20, 2015 at 11:23 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108508)
    
    QUOTIENT(End-Start+WEEKDAY(Start,3),7)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108508)
    
    *   ![](https://secure.gravatar.com/avatar/7172db04de729c130c11ae51bd08f28faea7ec5cfd74ffe8368e7b96fa34ffe3?s=64&d=mm&r=g) Denys Calvin says:
        
        [December 20, 2015 at 11:34 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108514)
        
        Oops! Didn't read the instructions. Small adjustment added at the end of the above to deal with "(including the start & end dates)"
        
        QUOTIENT(End-Start+WEEKDAY(Start,3),7)+IF(WEEKDAY(Start,3)=0,1,0)
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108514)
        
39.  ![](https://secure.gravatar.com/avatar/a7890c31ea949cf6a8644baacb70dd053eb1954b713a669a799b7c09a2ecb01c?s=64&d=mm&r=g) param nayak says:
    
    [December 20, 2015 at 11:26 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108511)
    
    a mathematical approach
    
    \=INT((A2-A1+1)/7)+IF(AND(MOD((A2-A1+1),7)+WEEKDAY(A1,2)-1<=7,WEEKDAY(A1,2)1),0,1)
    
    start day a1  
    end day a2
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108511)
    
40.  ![](https://secure.gravatar.com/avatar/badcf0a91dcdcb2ca6a7421d73bb477122d6771c408e82930a883ecb5ab6ab55?s=64&d=mm&r=g) Jan Martens says:
    
    [December 20, 2015 at 10:17 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108738)
    
    Finished my homework.  
    This formula can return the number of any weekday. The 'daynumber' in the formula can be hard-coded or a named range. Enter 1 for Sunday and 7 for Saturday  
    This formula works.
    
    INT((DATEDIF (SD +7+"daynumber"-WEEKDAY(SD,17)-7\*(WEEKDAY (SD, 17)<="daynumber "), ED,"d")) /7)+1
    
    Have a good day.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108738)
    
41.  ![](https://secure.gravatar.com/avatar/172075b03d65af5ae46a6c5c420d9236ae06b8dbf84f1956721ee7b698042ac6?s=64&d=mm&r=g) Swapnil Shah says:
    
    [December 21, 2015 at 3:29 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108801)
    
    \=IF(OR(MOD(SD,7)=2,MOD(ED,7)=2),ROUNDDOWN((ED-SD)/7,0)+1,ROUNDDOWN((ED-SD)/7,0))
    
    This formula is based on simple division rule , considering the 0th date in excel falls on saturday , we need to add one to our count, if any of start date or End date falls on Monday.
    
    SD : Start Date  
    ED : End Date
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108801)
    
42.  ![](https://secure.gravatar.com/avatar/91aa67d5aaf4d8d018583520df3d9108b31ee95e63d8a79d7584574ca7fe3b59?s=64&d=mm&r=g) Farzad says:
    
    [December 21, 2015 at 6:54 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108842)
    
    \=IF(TEXT(A1,"DDD")="Mon",ROUND((A2-A1)/7,0)+1,ROUND((A2-A1)/7,0))
    
    A1 is Start Date  
    A2 is End Date
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108842)
    
    *   ![](https://secure.gravatar.com/avatar/6e2eb818e9bb4ca7bad6d866b75c3271a4fb7d091780bbc2193d1be2302109ee?s=64&d=mm&r=g) Dheeran says:
        
        [December 21, 2015 at 2:59 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108953)
        
        this doesn't work so nicely if end and start day is Monday...
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108953)
        
43.  ![](https://secure.gravatar.com/avatar/4c45747776dff157a2fd51ea94647aada4c43142a20952d04f3472ed0f7bb34c?s=64&d=mm&r=g) Seema says:
    
    [December 21, 2015 at 8:30 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108867)
    
    ((ED+(7-WEEKDAY(ED,12))-(SD+(7-WEEKDAY(SD,12))))/7)+1
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108867)
    
    *   ![](https://secure.gravatar.com/avatar/05420156d3197db4a5eee5d4d905855bcd77c673917ee410c3f15ec902f829fc?s=64&d=mm&r=g) Gopi Krishna says:
        
        [December 21, 2015 at 1:44 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108938)
        
        \=IF(F15>G15,"End Date must be later than start date",IF(AND(F15=G15,WEEKDAY(F15,1)=2),1,IF(AND(WEEKDAY(F15,1)=2,WEEKDAY(G15,1)=2),QUOTIENT((G15-1)-(F15+1),7)+2,IF(OR(WEEKDAY(F15,1)=2,WEEKDAY(G15,1)=2),QUOTIENT((G15-1)-(F15+1),7)+1,QUOTIENT((G15-F15),7)))))
        
        This formula works for all situations.. even if start date is equal to end date
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108938)
        
44.  ![](https://secure.gravatar.com/avatar/fc8aa774867e881ddea409c729b41359054fe31d467f4e8a9d0b39f518573573?s=64&d=mm&r=g) Satya Murthy says:
    
    [December 21, 2015 at 12:25 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108920)
    
    \= INT( (WEEKDAY(A1-2) + A2 - A1) / 7)
    
    where the cell A1 holds the start date and A2 holds the end date.
    
    This formula works correctly for all situations. It can be tweaked for any day of the week. It is very simple and elegant.
    
    In the expression (A1-2), 2 denotes Mon. Use 1 for Sun, 3 for Tue, 4 for Wed, 5 for Thu, 6 for Fri, 7 for Sat.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108920)
    
    *   ![](https://secure.gravatar.com/avatar/badcf0a91dcdcb2ca6a7421d73bb477122d6771c408e82930a883ecb5ab6ab55?s=64&d=mm&r=g) Jan Martens says:
        
        [December 22, 2015 at 8:42 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109252)
        
        Best formula to me.
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109252)
        
45.  ![](https://secure.gravatar.com/avatar/11f9f7fa561c167d13d177918136bc7c3a6e62cbf17439b455aee1955e489b28?s=64&d=mm&r=g) Robert says:
    
    [December 21, 2015 at 12:35 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108922)
    
    What about this?
    
    \=EndDate - StartDate - NETWORKDAYS.INTL(StartDate,EndDate,12) + 1
    
    where 12 means Mondays "are weekends"
    
    Gives me 8 for example of 01/12/2015 - 31/01/2016
    
    Shouldn't this be the simplest formula to get the job done?
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108922)
    
46.  ![](https://secure.gravatar.com/avatar/6e2eb818e9bb4ca7bad6d866b75c3271a4fb7d091780bbc2193d1be2302109ee?s=64&d=mm&r=g) Dheeran says:
    
    [December 21, 2015 at 1:24 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108933)
    
    \=IF(D5E5,INT(IF(WEEKDAY(start)-\_  
    WEEKDAY(end)=0,wkdsum+1,wkdsum)),\_  
    INT(IF(WEEKDAY(start)-WEEKDAY(end)=0,wkdsum+1,wkdsum)-1))
    
    were wkdsum=IF(wkd>7,dsum/7-1,dsum/7)...  
    dsum=(DAYS(end,start)+WEEKDAY(end))...  
    wkd=E5+D5
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108933)
    
47.  ![](https://secure.gravatar.com/avatar/6e2eb818e9bb4ca7bad6d866b75c3271a4fb7d091780bbc2193d1be2302109ee?s=64&d=mm&r=g) Dheeran says:
    
    [December 21, 2015 at 1:27 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108934)
    
    made a mistake...should read IF(WEEKDAY(start)WEEKDAY(end),INT(IF(WEEKDAY(start)-\_  
    WEEKDAY(end)=0,wkdsum+1,wkdsum)),\_  
    INT(IF(WEEKDAY(start)-WEEKDAY(end)=0,wkdsum+1,wkdsum)-1))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108934)
    
48.  ![](https://secure.gravatar.com/avatar/6e2eb818e9bb4ca7bad6d866b75c3271a4fb7d091780bbc2193d1be2302109ee?s=64&d=mm&r=g) Dheeran says:
    
    [December 21, 2015 at 1:31 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108935)
    
    there needs to be a "not equal" sign where the "\*\*\*" is in the formula...IF(WEEKDAY(start)\*\*\*WEEKDAY(end),INT(IF(WEEKDAY(start)-\_
    
    no idea why char aren't uploading...
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108935)
    
49.  ![](https://secure.gravatar.com/avatar/e510f2624d8c0d5905ae747d60b2b8f3c4918e49eca5766540e33e90bc173013?s=64&d=mm&r=g) Manuel Vasquez says:
    
    [December 21, 2015 at 3:10 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108959)
    
    SD = Start Date  
    ED = End Date
    
    \=SUMPRODUCT(--(WEEKDAY(ROW(INDIRECT(SD&":"&ED)))=1))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108959)
    
50.  ![](https://secure.gravatar.com/avatar/33dda0ae5c55fd2df617c6ddd692d22f467177fed73282bf57b7517478adb672?s=64&d=mm&r=g) Ray Gaurav says:
    
    [December 21, 2015 at 4:00 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108974)
    
    \=Weeknumber (XX,2)-Weeknumbr (YY,2)  
    Were xx = cell which has end date and yy = cell which has begiate
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1108974)
    
51.  ![](https://secure.gravatar.com/avatar/e4708a1733e67db9ed0b12630b9ea8830233d7f5deac23fd32be2ee0301d5d90?s=64&d=mm&r=g) Brian says:
    
    [December 21, 2015 at 5:40 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109007)
    
    \=IF(WEEKDAY(StartDate,2)=1,1,0)+((EndDate-StartDate-WEEKDAY(EndDate,2)-(7-WEEKDAY(StartDate,2)))/7)+1
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109007)
    
52.  ![](https://secure.gravatar.com/avatar/b487f330ec96ac52da4745d9d04f3be6dbd590fde4835750467dc4df8d1a0300?s=64&d=mm&r=g) Pablo says:
    
    [December 21, 2015 at 6:34 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109030)
    
    It seems that many answers include a variation of this:
    
    \=SUMPRODUCT((WEEKDAY(ROW(INDIRECT(A1&":"&A2)))=2)\*1)
    
    where the initial date is on A1 and the final date on A2
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109030)
    
    *   ![](https://secure.gravatar.com/avatar/67204ad7edbdda7021a257a99efc16b46e405a4c87bc23f0e920d92970a3dd01?s=64&d=mm&r=g) mma173 says:
        
        [December 23, 2015 at 4:03 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109656)
        
        This formula is neat. However, I prefer the ones based on simple division and small adjustment. The reason is that Sumproduct is less efficient; much more calculations (comparsions) are being done in the background.
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109656)
        
53.  ![](https://secure.gravatar.com/avatar/5b7fba6fa1563e3a099824ec450b9ea0d1abd3546da1de5314af1c00df797fc7?s=64&d=mm&r=g) Arkadiusz says:
    
    [December 21, 2015 at 6:55 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109040)
    
    {=SUM(IF(WEEKDAY(B1+ROW(INDIRECT("1:"&DAYS(A2;B1))))=2;1;0))}
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109040)
    
    *   ![](https://secure.gravatar.com/avatar/5b7fba6fa1563e3a099824ec450b9ea0d1abd3546da1de5314af1c00df797fc7?s=64&d=mm&r=g) Arkadiusz says:
        
        [December 21, 2015 at 6:55 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109041)
        
        where b1 - start date, a2 - end date
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109041)
        
54.  ![](https://secure.gravatar.com/avatar/3634835f6131806698500bc26a0b020b97d2a7c6249d5be11db4920ba639ed2d?s=64&d=mm&r=g) Paul S. says:
    
    [December 21, 2015 at 7:08 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109046)
    
    Starting date in A1 and Ending date in A2
    
    \=IF(WEEKDAY(A1,1)=2,ROUNDUP((A2-A1)/7,0)+1,ROUNDUP((A2-A1)/7,0))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109046)
    
55.  ![](https://secure.gravatar.com/avatar/73c746d6f5c6d58206f078946409726f59d2f593fd4b5f0025d8a727cf2b0bdc?s=64&d=mm&r=g) Kcdog says:
    
    [December 21, 2015 at 7:24 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109059)
    
    \=INT((WEEKDAY($A$1-2)-$A$1+$A$2)/7)
    
    A1 is Start Date  
    A2 is End Date
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109059)
    
    *   ![](https://secure.gravatar.com/avatar/fbfaaa6f51c530681ddcac752efba8729ce3487f2b78ef555192de9c7901a05b?s=64&d=mm&r=g) SAURABH SHUKLA says:
        
        [December 22, 2015 at 7:15 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109224)
        
        not giving correct answer
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109224)
        
        *   ![](https://secure.gravatar.com/avatar/fbfaaa6f51c530681ddcac752efba8729ce3487f2b78ef555192de9c7901a05b?s=64&d=mm&r=g) SAURABH SHUKLA says:
            
            [December 22, 2015 at 7:17 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109225)
            
            sorry.... my mistake
            
            [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109225)
            
56.  ![](https://secure.gravatar.com/avatar/72e2a06f95c3b0056ec51f6d718d1006a560e9862567e6e4d6922c93ea9ba9ac?s=64&d=mm&r=g) GMF says:
    
    [December 21, 2015 at 8:03 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109070)
    
    Adapting Mike Girvin's formula to find the number of Friday 13ths between two dates, it can be simplified just to look for a weekday.
    
    \=SUMPRODUCT(--(TEXT(ROW(INDIRECT(SD&":"&ED)),"ddd")="Mon"))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109070)
    
57.  ![](https://secure.gravatar.com/avatar/9f1701e473e050dda8d09e7ad3af46c2a02d7850e7812b1a0e522f44a91738f1?s=64&d=mm&r=g) [Vishwamitra](http://www.learnexcelmacro.com/)
     says:
    
    [December 21, 2015 at 8:28 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109078)
    
    Sub HowManyMonday(startDate As Date, endDate As Date)
    
    Dim startDay As String
    
    If startDate > endDate Then Exit Sub  
    startDay = VBA.Format(startDate, "ddd")  
    countMonday = VBA.Round((VBA.DateDiff("d", startDate, endDate) / 7), 0)  
    If startDay = "Mon" Then countMonday = countMonday + 1 Else countMonday = countMonday  
    MsgBox "There are " & countMonday & " Monday(s) between " & startDate & " and " & endDate  
    End Sub
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109078)
    
58.  ![](https://secure.gravatar.com/avatar/2f4e95a68e884deb9d0a72c72c2805aa72bbf22247d7cfaf544ebb3bdcae4402?s=64&d=mm&r=g) Alex Groberman says:
    
    [December 21, 2015 at 10:35 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109109)
    
    How about:
    
    \=A2-A1+1-NETWORKDAYS.INTL(A1,A2,12)
    
    Regards,
    
    Alex
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109109)
    
59.  ![](https://secure.gravatar.com/avatar/fbfaaa6f51c530681ddcac752efba8729ce3487f2b78ef555192de9c7901a05b?s=64&d=mm&r=g) SAURABH SHUKLA says:
    
    [December 22, 2015 at 6:16 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109204)
    
    \=ROUNDUP(DATEDIF(A1,B1,"D")/7,0)+IF(AND(WEEKDAY(A1)=2,WEEKDAY(B1)=2),1,0)
    
    Here, Cell A1 = Start Date  
    and Cell B1 = End Date
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109204)
    
    *   ![](https://secure.gravatar.com/avatar/fbfaaa6f51c530681ddcac752efba8729ce3487f2b78ef555192de9c7901a05b?s=64&d=mm&r=g) SAURABH SHUKLA says:
        
        [December 22, 2015 at 7:13 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109221)
        
        \=ROUNDUP((B1-A1)/7,0)+IF(AND(WEEKDAY(A1)=2,WEEKDAY(B1)=2),1,0)
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109221)
        
60.  ![](https://secure.gravatar.com/avatar/fa429a93fedeccb828b3c7ba14138f325484616a92eaecad50bdc10c2cc1c514?s=64&d=mm&r=g) Artem says:
    
    [December 22, 2015 at 7:22 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109228)
    
    \=SUM((WEEKDAY((Start\_Date+ROW(INDIRECT("1:"&End\_Date-Start\_Date))-1),2)=1)\*1)
    
    I live in country where Sunday is last day of week, so Monday = 1.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109228)
    
    *   ![](https://secure.gravatar.com/avatar/fa429a93fedeccb828b3c7ba14138f325484616a92eaecad50bdc10c2cc1c514?s=64&d=mm&r=g) Artem says:
        
        [December 22, 2015 at 7:23 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109229)
        
        Forgot to mention, enter as array formula (Ctrl+Shift+Enter)
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109229)
        
61.  ![](https://secure.gravatar.com/avatar/c72d023366260ebef49fa7df98159f503f920992df6e18250421b1ab86019c06?s=64&d=mm&r=g) John Jairo V says:
    
    [December 22, 2015 at 1:55 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109314)
    
    Hi!
    
    What about this:  
    A1: Start Date, B1: End Date  
    \=NETWORKDAYS.INTL(A1,B1,"0111111")
    
    Blessings!
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109314)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [December 23, 2015 at 4:50 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109481)
        
        Wow... didn't know you could use binary patterns in NETWORKDAYS.INTL... very cool.. 😎
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109481)
        
        *   ![](https://secure.gravatar.com/avatar/7a013f2fa6b8808ca5dae786753bc8a2610b67c9441012ee788be1093e59b7b1?s=64&d=mm&r=g) Elias says:
            
            [December 23, 2015 at 3:41 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109650)
            
            Check Debra's post
            
            [http://blog.contextures.com/archives/2015/12/10/customize-weekends-with-excel-workday-function/](http://blog.contextures.com/archives/2015/12/10/customize-weekends-with-excel-workday-function/)
            
            Regards
            
            [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109650)
            
    *   ![](https://secure.gravatar.com/avatar/6719e22b4f610ee109ac36e01113ea3385de0e2f7d60f5737502fb8394912b60?s=64&d=mm&r=g) Mehmet Gunal OLCER says:
        
        [December 23, 2015 at 8:20 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109540)
        
        Good work needs appreciation.
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109540)
        
    *   ![](https://secure.gravatar.com/avatar/d4a39a29ba251034f960a5e17b104a974f23ec9d9afdf2dc5ae6b92b3081e062?s=64&d=mm&r=g) Chihiro says:
        
        [December 23, 2015 at 2:30 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109634)
        
        Awesome! I was trying to manipulate NETWORKDAYS.INTL as well and  
        came up with  
        \=(B1-A1)+1-NETWORKDAYS.INTL(A1,B1,12)
        
        But had no idea it took binary.
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109634)
        
62.  ![](https://secure.gravatar.com/avatar/ce8379700f6e42820c8f227bddabd8b57f1f9df55681781ca18c883ccaabc47a?s=64&d=mm&r=g) Peter says:
    
    [December 23, 2015 at 5:42 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109494)
    
    This should work:
    
    \=ROUNDUP((D8-IF(E7=5,D7+3,IF(E7=6,D7+2,IF(E7=7,E7+1,IF(E7=4,E7+4,IF(E7=3,D7+5,IF(D7=2,D7+6,D7)))))))/7,0)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109494)
    
63.  ![](https://secure.gravatar.com/avatar/ca31ef0ffb38ef61a711996a1651cd24c72a6df4f9f36394c7ab102330ea3c49?s=64&d=mm&r=g) AK says:
    
    [December 23, 2015 at 7:16 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109526)
    
    my solution (limited to dates within the same year)
    
    [https://www.dropbox.com/s/8vja3qn5yca7cs2/Between\_two\_dates.xlsx?dl=0](https://www.dropbox.com/s/8vja3qn5yca7cs2/Between_two_dates.xlsx?dl=0)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109526)
    
64.  ![](https://secure.gravatar.com/avatar/dae335798cff859a2cfb98f8b7371c1baf08b4e237841fd4db8d10481aad2b00?s=64&d=mm&r=g) Vangelis M says:
    
    [December 23, 2015 at 1:54 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109621)
    
    One more
    
    \=INT((end-start+8-WEEKDAY(end,how\_many))/7)
    
    where for  
    how\_many=11 : the number of Mondays is calculated  
    how\_many=12 : the number of Tuesdays is calculated  
    ...  
    how\_many=17 : the number of Sundays is calculated
    
    However John Jairo Vs answer is excellent!!!!
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109621)
    
65.  ![](https://secure.gravatar.com/avatar/05420156d3197db4a5eee5d4d905855bcd77c673917ee410c3f15ec902f829fc?s=64&d=mm&r=g) Gopi Krishna says:
    
    [December 23, 2015 at 2:54 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109642)
    
    \=SUMPRODUCT(IF(WEEKDAY(ROW(INDIRECT(E7&":"&F7)),1)=2,1,0))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109642)
    
    *   ![](https://secure.gravatar.com/avatar/05420156d3197db4a5eee5d4d905855bcd77c673917ee410c3f15ec902f829fc?s=64&d=mm&r=g) Gopi Krishna says:
        
        [December 23, 2015 at 3:01 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109644)
        
        CTRL+SHIFT+ENTER in the above formula
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109644)
        
66.  ![](https://secure.gravatar.com/avatar/3393e3786facefe7c484c33675b6cfa1b204945fb39624a5b645a88d5ab7b315?s=64&d=mm&r=g) Pedro says:
    
    [December 23, 2015 at 3:00 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109643)
    
    \=SUM((WEEKDAY(ROW(INDIRECT(M5&":"&M6)))=2)\*1)
    
    Press Ctrl + Shift + Enter
    
    Where M5 anda M6 are the dates
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109643)
    
67.  ![](https://secure.gravatar.com/avatar/8e3f49146d236ffe0cf6458a7db5e6dfdc610ec107796105cba89ff28f11bff5?s=64&d=mm&r=g) BL says:
    
    [December 23, 2015 at 3:25 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109648)
    
    Why not
    
    \=FLOOR( (A2-A1-WEEKDAY(A2,3)) / 7 ,1) + 1
    
    A1 = Start Date  
    A2 = End Date
    
    or ignore date order
    
    \=FLOOR( (ABS(A2-A1) - WEEKDAY( MAX(A2,A1) ,3)) /7 ,1) + 1
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109648)
    
68.  ![](https://secure.gravatar.com/avatar/1a843597de28fcbddd3bac48905ffc599eed7fc898c6e79a4af4d906a90ea81d?s=64&d=mm&r=g) [Mohd Mukeet](http://na/)
     says:
    
    [December 23, 2015 at 3:41 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109651)
    
    A1 = 1-Dec-15  
    B2 = 22-Dec-15
    
    {=SUM(IF(TEXT(A1+ROW(INDIRECT("1:"&DAY(B1))),"DDD")="Mon",1,0))}  
    Press CTRL+SHIFT+ENTER in the above formula  
    \= 3 (Monday)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109651)
    
69.  ![](https://secure.gravatar.com/avatar/75c334365ff4885a44651a26505d1dad31307eafc37667131ab9089d8594d1ff?s=64&d=mm&r=g) Haz says:
    
    [December 23, 2015 at 6:12 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109699)
    
    \=SUMPRODUCT(0+(TEXT(ROW(INDIRECT(A1&":"&A2)),"DDD")="MON"))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109699)
    
70.  ![](https://secure.gravatar.com/avatar/af327b45480d0b0df193c12b96d9f01f48f1cd020c8e8411f4383a10ec06ab6b?s=64&d=mm&r=g) Eric L. says:
    
    [December 23, 2015 at 9:53 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109763)
    
    \=IF(WEEKDAY(Start\_Date,2)>1,ROUNDDOWN(DAYS(End\_Date,Start\_Date)/7,0),ROUNDDOWN(DAYS(End\_Date,Start\_Date)/7,0)+1)
    
    Got this idea from the formula for "Reverse Coding" survey results.
    
    (Number of Choices-x)+1
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109763)
    
    *   ![](https://secure.gravatar.com/avatar/af327b45480d0b0df193c12b96d9f01f48f1cd020c8e8411f4383a10ec06ab6b?s=64&d=mm&r=g) Eric L. says:
        
        [December 23, 2015 at 9:53 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109764)
        
        \=IF(WEEKDAY(B9,2)>1,ROUNDDOWN(DAYS(B10,B9)/7,0),  
        ROUNDDOWN(DAYS(B10,B9)/7,0)+1)
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109764)
        
        *   ![](https://secure.gravatar.com/avatar/af327b45480d0b0df193c12b96d9f01f48f1cd020c8e8411f4383a10ec06ab6b?s=64&d=mm&r=g) Eric L. says:
            
            [December 23, 2015 at 9:54 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109766)
            
            One more try...
            
            \=IF(WEEKDAY(Start\_Date,2)>1,  
            ROUNDDOWN(DAYS(End\_Date,Start\_Date)/7,0),  
            ROUNDDOWN(DAYS(End\_Date,Start\_Date)/7,0)+1)
            
            [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1109766)
            
71.  ![](https://secure.gravatar.com/avatar/cb5303d3578e4ae8119b8ce9df2c9b5c932d90575de7898e0a0d95bbc6798544?s=64&d=mm&r=g) Sabeesh says:
    
    [December 25, 2015 at 8:10 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1111259)
    
    \=SUMPRODUCT(1\*(WEEKDAY(ROW(INDIRECT(A1&":"&A2)))=2))
    
    Where Celll A1contains the start date and A2 contains the end date
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1111259)
    
72.  ![](https://secure.gravatar.com/avatar/dcb080e37d17fd205adf2b60e4e7d04fe49a19578c03cc8d32c7551304937442?s=64&d=mm&r=g) Jon Valz says:
    
    [December 27, 2015 at 8:52 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1112101)
    
    I think I've got q couple solns:
    
    \=round(networksdays(start-weekday(start,3),end-weekday(end,3))/5,0)
    
    Or
    
    \=round((end-weekday(end,3)-start-weekday(start,3)))/7,0)
    
    As in, the solution should be the number of weeks between the Monday of each week.
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1112101)
    
73.  ![](https://secure.gravatar.com/avatar/badcf0a91dcdcb2ca6a7421d73bb477122d6771c408e82930a883ecb5ab6ab55?s=64&d=mm&r=g) Jan Martens says:
    
    [December 30, 2015 at 11:37 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1114361)
    
    Hi, found this on the Web. The formula was written by Laurent .
    
    \=INT((Ed-MOD(Ed- daynumber,7)-SD+7)/7)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1114361)
    
    *   ![](https://secure.gravatar.com/avatar/badcf0a91dcdcb2ca6a7421d73bb477122d6771c408e82930a883ecb5ab6ab55?s=64&d=mm&r=g) Jan Martens says:
        
        [December 30, 2015 at 11:38 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1114362)
        
        Written by Laurent Longre.
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1114362)
        
74.  ![](https://secure.gravatar.com/avatar/13158ae53eee5b093821c20efae8601a890b7a9122ccd445538cc7949d28e5e9?s=64&d=mm&r=g) [Anant Jain](http://www.klick2learnmore.com/)
     says:
    
    [January 4, 2016 at 12:51 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1116004)
    
    Answer is to calculate monday between 2 dates is:
    
    \=IF(WEEKDAY(SD,1)=2,INT((ED-SD)/7)+1,INT((ED-SD)/7))
    
    SD = Start Date  
    ED = End Date
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1116004)
    
75.  ![](https://secure.gravatar.com/avatar/acf2d1d81d0b2931fec68728af361cdf36c3e2acd9a8d543453221376e97d201?s=64&d=mm&r=g) Chirayu says:
    
    [January 4, 2016 at 5:02 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1116057)
    
    Use CTRL + SHIFT + ENTER when using formula:
    
    \=COUNT(IF(WEEKDAY(A:A)=2,A:A))
    
    Explanation  
    \- Column A has dates  
    \- Weekday formula turn dates into day number. 2 is Monday
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1116057)
    
76.  ![](https://secure.gravatar.com/avatar/af9c36e894208706c0f4a00fd53509566b31960ed97d299710ac84286578b65e?s=64&d=mm&r=g) Danny Baetens says:
    
    [January 5, 2016 at 2:52 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1116443)
    
    INT((end-start+WEEKDAY(start;12))/7)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1116443)
    
77.  ![](https://secure.gravatar.com/avatar/a99fde22ba553e95374b55cf95b4330a73402730a0061854eac75bb90c31242d?s=64&d=mm&r=g) Chandra Mohan says:
    
    [January 6, 2016 at 6:18 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1116743)
    
    \=ED-SD-NETWORKDAYS.INTL(SD,ED,12)+1, try this formula
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1116743)
    
78.  ![](https://secure.gravatar.com/avatar/7ef7b54c5d60458bbe6e6a654994b746f1178f025451e1c1456711c212a5c9c0?s=64&d=mm&r=g) MichaelCH says:
    
    [January 11, 2016 at 3:56 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1118733)
    
    \=INT((ED-SD+MOD(SD-3,7)+1)/7)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1118733)
    
79.  ![](https://secure.gravatar.com/avatar/d3f4b370241446fd1be092b2a9fa1a0800f29b2965955f3e5e30c7b32eb821d5?s=64&d=mm&r=g) Philip Stevenson says:
    
    [January 22, 2016 at 3:51 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1124744)
    
    Function CountADayBetwen(StartDAte As Date, EndDate As Date, TheDay As String)
    
    Select Case TheDay
    
    Case "Sunday"  
    Nday = 1
    
    Case "Monday"  
    Nday = 2
    
    Case "Tuesday"  
    Nday = 3
    
    Case "Wednesday"  
    Nday = 4
    
    Case "Thursday"  
    Nday = 5
    
    Case "Friday"  
    Nday = 6
    
    Case "Saturday"  
    Nday = 7
    
    End Select
    
    For i = StartDAte To EndDate
    
    If Weekday(i) = Nday Then  
    x = x + 1  
    End If
    
    Next
    
    CountADayBetwen = x
    
    End Function
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1124744)
    
80.  ![](https://secure.gravatar.com/avatar/ed9f42b96f89c87b5f2bd2a7f4022e9e58aed8044febe885935b816f32b1348e?s=64&d=mm&r=g) mukesh says:
    
    [April 13, 2016 at 3:12 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1168255)
    
    A2 = Start date; A3 = End date
    
    \=IF(WEEKDAY(A2)=WEEKDAY(A3),ROUND(((A3-A2)/7)-0.14286,0)+1,ROUND(((A3-A2)/7)-0.14286,0))
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1168255)
    
81.  ![](https://secure.gravatar.com/avatar/e81113c8c86031c705a6f7e0109e3c7a9606e15703152919e3e171d9fa98b41f?s=64&d=mm&r=g) Jogo do Texto says:
    
    [June 10, 2016 at 12:15 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1210309)
    
    Man, this article it's what I was looking for in the last couple weeks! Congratulations for this great text
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1210309)
    
82.  ![](https://secure.gravatar.com/avatar/27726364a2b289f25967853cccb24bbd2c9ba9e4a4088d0060e29896eba5ed71?s=64&d=mm&r=g) [Junaid Azhar doga](http://nil/)
     says:
    
    [December 28, 2016 at 10:01 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1380746)
    
    \=INT((WEEKDAY(A1-2)-A1+A2)/7)  
    just put starting date in cell A1 and end date in Cell B2.  
    and change the day no in formula where -2 is a day no..  
    Day no like {sun, mon, tue, wed, thu, fri, sun} {1,2,3,4,5,67}
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1380746)
    
83.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [December 28, 2016 at 2:18 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1380829)
    
    @To whom it may concern,  
    Just a short update shown by the linked picture:  
    [https://s29.postimg.org/hfxvuuz13/NONAME.png](https://s29.postimg.org/hfxvuuz13/NONAME.png)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1380829)
    
84.  ![](https://secure.gravatar.com/avatar/05420156d3197db4a5eee5d4d905855bcd77c673917ee410c3f15ec902f829fc?s=64&d=mm&r=g) GOPI kRISHNA says:
    
    [December 28, 2016 at 4:21 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1380871)
    
    H8 = SUMPRODUCT(IF(WEEKDAY(ROW(INDIRECT(E8&":"&F8)))=2,1,0))
    
    by putting starting date in E8 & ending date in F8
    
    CTRL+SHiFT+ENTER
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1380871)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [December 28, 2016 at 4:39 pm](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1380876)
        
        @GOPI?  
        It should not, necessarily, be an "Array formula and the use of IF is also unnecessary.
        
        Try: =SUMPRODUCT(N(WEEKDAY(ROW(INDIRECT(E8&":"&F8)))=2))
        
        [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1380876)
        
85.  ![](https://secure.gravatar.com/avatar/dc393ed7516826fb0ad83057a1f02e82df70223805a262a0495cdb9cd5bb82f6?s=64&d=mm&r=g) [Duc Thanh Nguyen](https://www.hocexcel.online/)
     says:
    
    [January 13, 2017 at 4:51 am](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1390402)
    
    \=INT((A2-A1+WEEKDAY(A1,16))/7)
    
    [Reply](https://chandoo.org/wp/count-mondays-between-two-dates/#comment-1390402)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/count-mondays-between-two-dates/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Color changing line chart \[tutorial\]](https://chandoo.org/wp/color-changing-line-chart/) | [Generate a snow flake pattern Excel \[holiday fun\]](https://chandoo.org/wp/excel-snow-flake/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)