# Lookup most frequent item [Homework] » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/lookup-most-frequent-item

---

Lookup most frequent item \[Homework\]
======================================

[Excel Challenges](https://chandoo.org/wp/category/excel-challenges/)
 - 26 comments

  

Here is an interesting problem to keep your brain cells fight boredom on this Friday & weekend.

Let’s say you have some data like this.

![most-frequent-lookup](https://chandoo.org/wp/wp-content/uploads/2017/02/most-frequent-lookup.png)

And you want to know, for a given customer name (in cell G4),

*   What is the most frequent quantity?
*   What is the most often purchased item?

How would you write formulas to get these answers?

Assume that all the data is in a table, conveniently named _data._ So you can access customer names by using structured name – data\[Customer\] etc.

\[Related: [Introduction to Excel Structured Referencing](http://chandoo.org/wp/2013/06/26/introduction-to-structural-references/)\
\]

If there are ties, you may pick any one value.

**[Click here to download sample file with raw data](https://chandoo.org/wp/wp-content/uploads/2017/02/frequent-lookup.xlsx)
.**

Go ahead and post your answers in the comments.

**Want more?** Check out our [Excel Homework problems](http://chandoo.org/wp/tag/homework)
 page and get cracking.

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
| Written by Chandoo  <br>Tags: [homework](https://chandoo.org/wp/tag/homework/)<br>, [Learn Excel](https://chandoo.org/wp/tag/excel/)<br>, [Microsoft Excel Formulas](https://chandoo.org/wp/tag/formulas/)<br>, [mode()](https://chandoo.org/wp/tag/mode/)<br>, [Mode.mult()](https://chandoo.org/wp/tag/mode-mult/)<br>, [vlookup](https://chandoo.org/wp/tag/vlookup/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 26 Responses to “Lookup most frequent item \[Homework\]”

1.  ![](https://secure.gravatar.com/avatar/67204ad7edbdda7021a257a99efc16b46e405a4c87bc23f0e920d92970a3dd01?s=64&d=mm&r=g) mma173 says:
    
    [February 17, 2017 at 11:34 am](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408594)
    
    For most frequent quantity:  
    {=INDEX(data\[Qty\],SMALL(IF(COUNTIF(data\[Qty\],data\[Qty\])=MAX(COUNTIF(data\[Qty\],data\[Qty\])), ROW(data\[Qty\]),""),1))}
    
    For most often purchased item:  
    {=INDEX(data\[Item\],SMALL(IF(COUNTIF(data\[Item\],data\[Item\])=MAX(COUNTIF(data\[Item\],data\[Item\])), ROW(data\[Item\]),""),1))}
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408594)
    
    *   ![](https://secure.gravatar.com/avatar/7e2c3fcec9d414805132ebf584d135c5b85b556b2d937ef4e2231391b306f702?s=64&d=mm&r=g) Edgars says:
        
        [February 18, 2017 at 12:58 am](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1409136)
        
        Doesn't work, always returns the 4th value from the range data\[Qty\].
        
        [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1409136)
        
2.  ![](https://secure.gravatar.com/avatar/9eadf8977d7df519580087eb567197597e71839c260df749e8b67f7f9c3ebec1?s=64&d=mm&r=g) Hugo says:
    
    [February 17, 2017 at 12:55 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408628)
    
    first sort the table (high to low)  
    then with a simple index/match  
    (first occurrence of that name is the most frequent item for that name)
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408628)
    
3.  ![](https://secure.gravatar.com/avatar/7e4971c3152778fde7ddedad4cb22034f624d5d198c7de681ed43fe2a1d3044f?s=64&d=mm&r=g) Desk Lamp says:
    
    [February 17, 2017 at 12:56 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408629)
    
    {=MODE(IF(data\[Customer\]=$G4,data\[Qty\]))}
    
    {=INDEX(data\[Item\],MATCH(TRUE,COUNTIFS(data\[Item\],IF(data\[Customer\]=$G4,data\[Item\]),data\[Customer\],$G4)=MAX(COUNTIFS(data\[Item\],IF(data\[Customer\]=$G4,data\[Item\]),data\[Customer\],$G4)),0))}
    
    I think the second formula could be simplified but I'll leave it at that for now.
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408629)
    
    *   ![](https://secure.gravatar.com/avatar/7e4971c3152778fde7ddedad4cb22034f624d5d198c7de681ed43fe2a1d3044f?s=64&d=mm&r=g) Desk Lamp says:
        
        [February 17, 2017 at 12:59 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408632)
        
        Ok, slightly simpler:
        
        {=INDEX(data\[Item\],MATCH(TRUE,COUNTIFS(data\[Item\],data\[Item\],data\[Customer\],$G4)=MAX(COUNTIFS(data\[Item\],data\[Item\],data\[Customer\],$G4)),0))}
        
        [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408632)
        
        *   ![](https://secure.gravatar.com/avatar/460be5157a8ff55b9ffdf755dce4658a7d42130b5bda58c43f07368eb6088d00?s=64&d=mm&r=g) Daniel H says:
            
            [February 18, 2017 at 8:52 am](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1409344)
            
            {=MODE(IF(G4=data\[Customer\],data\[Qty\]))}
            
            Same as yours. It’s curious why Excel doesn’t treat “FALSE” as zero
            
            {=INDEX(data\[Item\],MODE(IF(G4=data\[Customer\],MATCH(data\[Item\],data\[Item\],0))))}
            
            It just works, don’t ask me why 😉
            
            [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1409344)
            
            *   ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
                
                [February 23, 2017 at 2:39 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1412673)
                
                Daniel, that's a crazy cool and elegant solution!
                
                My initial thought was to use FREQUENCY on the concatenation of Customer and Item because the COUNTIFS solutions would be very slow if the array were much larger. Then a MATCH on the MAX (or AGGREGATE) of that FREQUENCY would have determined the corresponding position. And that approach works, as shown below. It's long, but it's also always going to be fast.
                
                You on the other hand recognized that the position of an Item relative to its Customer doesn't matter as long as every possible Item is represented by a unique position (number) and ignored unless it corresponds with the correct Customer. And your solution capitalizes on that perfectly. I also appreciate how your formula avoids repeating any of its pieces, something I particularly dislike and avoid whenever I can.
                
                {=INDEX(data\[Item\],MATCH(AGGREGATE(14,6,IF(data\[Customer\]=G4,FREQUENCY(MATCH(data\[Customer\]&"#"&data\[Item\],data\[Customer\]&"#"&data\[Item\],0),MATCH(data\[Customer\]&"#"&data\[Item\],data\[Customer\]&"#"&data\[Item\],0))),1),IF(data\[Customer\]=G4,FREQUENCY(MATCH(data\[Customer\]&"#"&data\[Item\],data\[Customer\]&"#"&data\[Item\],0),MATCH(data\[Customer\]&"#"&data\[Item\],data\[Customer\]&"#"&data\[Item\],0))),0))}
                
                [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1412673)
                
4.  ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
    
    [February 17, 2017 at 4:41 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408812)
    
    In cell H4: {=MAX((data3\[Customer\]=G4)\*data3\[Qty\])}  
    In cell I4: {=INDEX(data3\[Item\],MATCH(G4&H4,data3\[Customer\]&data3\[Qty\],))}  
    and copy down...  
    \*\*\*Both Array Formulas  
    \--------------------------------  
    Michael (Micky) Avidan
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408812)
    
    *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
        
        [February 17, 2017 at 4:44 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408816)
        
        DATA3 should read DATA.  
        It became DATA3 because I copied the sheet in oredr to work on a copy.  
        \----------------------------  
        Michael (Micky) Avidan
        
        [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408816)
        
        *   ![](https://secure.gravatar.com/avatar/0ccdd738687a5c82db64cc3abdff8709be7d8df11ba9076cefc2be38d6742992?s=64&d=mm&r=g) Michael (Micky) Avidan says:
            
            [February 17, 2017 at 4:48 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408820)
            
            Sorry..., I misssed the MODE part.  
            Ignore my posts.  
            \----------------------------  
            Michael (Micky) Avidan
            
            [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408820)
            
5.  ![](https://secure.gravatar.com/avatar/8ceae07ad389f92037be72df1988137e1d17a29339ab2d5c34385d27a027ad2f?s=64&d=mm&r=g) Ola says:
    
    [February 17, 2017 at 5:41 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408853)
    
    Make a PivotTable (sort) --> enables drilldown
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1408853)
    
6.  ![](https://secure.gravatar.com/avatar/cb5303d3578e4ae8119b8ce9df2c9b5c932d90575de7898e0a0d95bbc6798544?s=64&d=mm&r=g) Sabeesh says:
    
    [February 18, 2017 at 7:53 am](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1409337)
    
    Qty: =MODE(IF(data\[Customer\]=G4,data\[Qty\]))
    
    Item:=INDEX(data\[Item\],MATCH(MAX(COUNTIFS(data\[Customer\],G4,data\[Item\],data\[Item\])),COUNTIFS(data\[Customer\],G4,data\[Item\],data\[Item\]),0))
    
    Both are array formulas
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1409337)
    
    *   ![](https://secure.gravatar.com/avatar/22eb483a2e0cfe6363342a7dcd1a471bf947d5dfe2b9440e3b883479f2c4366e?s=64&d=mm&r=g) Rojo Loco says:
        
        [March 3, 2017 at 2:08 am](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1416571)
        
        In copy and past of the solution I get results, but not the correct results. For example, I got by your mode index formula:  
        Willie Larson 5 Bags
        
        when i should have gotten:
        
        Willie Larson Beef 10
        
        [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1416571)
        
7.  ![](https://secure.gravatar.com/avatar/cb5303d3578e4ae8119b8ce9df2c9b5c932d90575de7898e0a0d95bbc6798544?s=64&d=mm&r=g) Sabeesh says:
    
    [February 18, 2017 at 7:54 am](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1409339)
    
    \=INDEX(data\[Item\],MATCH(MAX(COUNTIFS(data\[Customer\],G4,data\[Item \],data\[Item\])),COUNTIFS(data\[Customer\],G4,data\[Item\],data\[Item\]),0))
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1409339)
    
    *   ![](https://secure.gravatar.com/avatar/e081343b9839bbb623dd2df55fcad843baf3cbbeb93d5b2b9ad35c973a23a7c6?s=64&d=mm&r=g) ZORRO2005 says:
        
        [February 25, 2017 at 5:49 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1413445)
        
        Very good solution!
        
        [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1413445)
        
8.  ![](https://secure.gravatar.com/avatar/e82549bcfec803280f481a30fa5334372a58d36965cbf05a84c067f1e4e8ce72?s=64&d=mm&r=g) ak says:
    
    [February 24, 2017 at 4:10 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1413064)
    
    Hello,
    
    Sorry for posting here but I couldn't find a place to post questions here. Is there an area where I can post questions.
    
    How can I delete every other row quickly in excel, because I ran a report and it skips a row for each entry.
    
    Thanks so much and apologize if this is not allowed.
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1413064)
    
9.  ![](https://secure.gravatar.com/avatar/e081343b9839bbb623dd2df55fcad843baf3cbbeb93d5b2b9ad35c973a23a7c6?s=64&d=mm&r=g) ZORRO2005 says:
    
    [February 25, 2017 at 4:00 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1413409)
    
    {=INDEX(data\[Item\],MODE(IF(data\[Customer\]=G4,MATCH(data\[Item\],data\[Item\],))))}
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1413409)
    
    *   ![](https://secure.gravatar.com/avatar/76a72a792fa4817a022ed202df3ad7eaeeae769ec5a5fa84ba0f3beda37fa8b0?s=64&d=mm&r=g) Andy says:
        
        [March 2, 2017 at 12:43 am](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1415732)
        
        Great stuff. I am getting most of this, but I do not understand how the array data\[Item\] in the Match lookup\_value works. How does this make sense?
        
        MATCH(data\[Item\],data\[Item\],)
        
        [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1415732)
        
        *   ![](https://secure.gravatar.com/avatar/e081343b9839bbb623dd2df55fcad843baf3cbbeb93d5b2b9ad35c973a23a7c6?s=64&d=mm&r=g) ZORRO2005 says:
            
            [March 4, 2017 at 9:50 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1417104)
            
            Andy, it will be clear if put the formula below to column E  
            \=IF(data\[Customer\]=$G$4,MATCH(data\[Item\],data\[Item\],))
            
            [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1417104)
            
        *   ![](https://secure.gravatar.com/avatar/8513d4f6a0ec1dde153f5c52c45ec43192b8188e1b63af960a589cd05c48cdf2?s=64&d=mm&r=g) Arpita says:
            
            [April 4, 2017 at 9:34 am](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1431007)
            
            Hi Andy,
            
            Hope this isn't too late.
            
            The MATCH function works by assigning a number (which is the item's first array position) to each unique item in Array 1.
            
            For example, let's say Array 1 is {Bags, Butter, Bags, Butter, Bread, Burgers, Bags}, which has 4 unique items
            
            Next, we'll take Array 2 {Bags, Butter, Bread, Bread, Burgers, Bread} to match against Array 1. Each item in Array 2 is matched against the whole of Array 1 and the MATCH function determines the first instance of a "match" and outputs the corresponding position from Array 1
            
            If we had to compare this to MATCH(data\[Item\],data\[Item\],0), the formula would be MATCH(Array 2, Array 1, 0)
            
            The answer to this formula would be {1;2;5;5;6;5). The mode of this array is 5, which is the unique code mapped to the item Bread.
            
            Hope this helps!
            
            [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1431007)
            
10.  ![](https://secure.gravatar.com/avatar/22eb483a2e0cfe6363342a7dcd1a471bf947d5dfe2b9440e3b883479f2c4366e?s=64&d=mm&r=g) Rojo Loco says:
    
    [February 26, 2017 at 7:43 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1413845)
    
    Create a pivot table off the data. Put customer and items on rows, put count of item on values. Sort highest to lowest on count of item. Go to design view of pivot table and change report lay out to tabular and repeat values, turn off grand totals and subtotals. Each customer by each item now has a value sorted highest to lowest. Index match the customer name to the item and count.
    
    This allows for changes to the pivot table to flow to the output, such as minimum value, average value (if your data allowed for it).
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1413845)
    
11.  ![](https://secure.gravatar.com/avatar/22eb483a2e0cfe6363342a7dcd1a471bf947d5dfe2b9440e3b883479f2c4366e?s=64&d=mm&r=g) Rojo Loco says:
    
    [March 3, 2017 at 1:50 am](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1416560)
    
    In looking for a more elegant and "break proof" option, here is what I have:
    
    from the raw data file you have 2 choices, top item per customer, or ranking item per customer, both have their advantages.
    
    Here is the top item per customer formula:  
    \=IF(COUNTIFS($B$4:$B$270,B4,$D$4:$D$270,">"&D4)+1>1,"",COUNTIFS($B$4:$B$270,B4,$D$4:$D$270,">"&D4)+1)  
    if you paste this into cell E4 and copy down it should work
    
    Here is the rank item per customer formula:  
    \`  
    if you paste this into cell F4 and copy down after the E4 formula above it should work
    
    Then you can filter by column E for 1 and get the top items (note some customers have tied for 1st place).
    
    Also, by column F you can see additional customer info quickly.
    
    (I call the new formula columns Top Item Per Customer for Column E and Customer Item Rank for Column F).
    
    Now you can sort by your preferred column (customer, item, quantity) and the table is always correct. (Sort by preferred item 1st and then next item, such as, customer them top item, or item, then top customer). Item A to Z, then Customer Item Rank Smallest to Largest gives you per item largest customer; Customer Item smallest to largest, then customer a to z gives you the largest items per customer etc.
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1416560)
    
12.  ![](https://secure.gravatar.com/avatar/22eb483a2e0cfe6363342a7dcd1a471bf947d5dfe2b9440e3b883479f2c4366e?s=64&d=mm&r=g) Rojo Loco says:
    
    [March 3, 2017 at 1:55 am](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1416565)
    
    In looking for a more elegant and "break proof" option, here is what I have:
    
    from the raw data file you have 2 choices, top item per customer, or ranking item per customer, both have their advantages.
    
    Here is the top item per customer formula:  
    \=IF(COUNTIFS($B$4:$B$270,B4,$D$4:$D$270,">"&D4)+1>1,"",COUNTIFS($B$4:$B$270,B4,$D$4:$D$270,">"&D4)+1)  
    if you paste this into cell E4 and copy down it should work
    
    Here is the rank item per customer formula:  
    \=COUNTIFS($B$4:$B$270,B4,$D$4:$D$270,">"&D4)+1
    
    if you paste this into cell F4 and copy down after the E4 formula above it should work
    
    Then you can filter by column E for 1 and get the top items (note some customers have tied for 1st place).
    
    Also, by column F you can see additional customer info quickly.
    
    (I call the new formula columns Top Item Per Customer for Column E and Customer Item Rank for Column F).
    
    Now you can sort by your preferred column (customer, item, quantity) and the table is always correct. (Sort by preferred item 1st and then next item, such as, customer them top item, or item, then top customer). Item A to Z, then Customer Item Rank Smallest to Largest gives you per item largest customer; Customer Item smallest to largest, then customer a to z gives you the largest items per customer etc.
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1416565)
    
13.  ![](https://secure.gravatar.com/avatar/e081343b9839bbb623dd2df55fcad843baf3cbbeb93d5b2b9ad35c973a23a7c6?s=64&d=mm&r=g) ZORRO2005 says:
    
    [March 4, 2017 at 10:44 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1417116)
    
    For cases when some customers will not have repeats  
    {=MODE(IF(data\[Customer\]=G4,data\[Qty\]\*{1,1}))}  
    {=INDEX(data\[Item\],MODE(IF(G4=data\[Customer\],MATCH(data\[Item\],data\[Item\],)\*{1,1})))}
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1417116)
    
14.  ![](https://secure.gravatar.com/avatar/c7bf82d187a9c828305b376bd981da674bac090d5e9119b14a20e61f11e139b3?s=64&d=mm&r=g) Noori says:
    
    [March 13, 2020 at 8:57 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1759519)
    
    Hi Chandoo,
    
    Is there a simple formula for these two questions. I am getting confused with the comments.
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-1759519)
    
15.  ![](https://secure.gravatar.com/avatar/aee5f5b568c6f3d309e4d5d53b9a98535fd42577d69f12c7476579f35d62842a?s=64&d=mm&r=g) David N says:
    
    [August 11, 2025 at 11:22 pm](https://chandoo.org/wp/lookup-most-frequent-item/#comment-2436299)
    
    I know this is an old thread, but I was revisiting some old example/challenge files from an Excel 365 perspective and noticed that the solutions we all came up with before didn't allow for ties -- more than one Item with the same frequency for the same Customer. So using Excel's newer functions, I came up with these two alternatives where K4# represents =SORT(UNIQUE(data\[Customer\]))...
    
    \=LET(  
    itemnum,XMATCH(data\[Item\],data\[Item\]),  
    MAP(K4#,LAMBDA(rec,LET(  
    frq,MODE.MULT(FILTER(itemnum,data\[Customer\]=rec)),  
    ARRAYTOTEXT(SORT(UNIQUE(FILTER(data\[Item\],(data\[Customer\]=rec)\*ISNUMBER(XMATCH(itemnum,frq))))))  
    )))  
    )
    
    \=MAP(K4#,LAMBDA(rec,LET(  
    grp,GROUPBY(data\[Item\],data\[Qty\],COUNT,,0,-2,data\[Customer\]=rec),  
    ARRAYTOTEXT(SORT(FILTER(CHOOSECOLS(grp,1),CHOOSECOLS(grp,2)=INDEX(grp,1,2))))  
    )))
    
    Both formulas will, for example, show that Brian Ross ordered Bacon and Baking powder just as often as Brussel Sprouts (that is after the spelling is corrected from power to powder in the file) instead of only finding Brussel Sprouts as the first Item that Brian ordered twice.
    
    [Reply](https://chandoo.org/wp/lookup-most-frequent-item/#comment-2436299)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/lookup-most-frequent-item/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Use CTRL to make copies of worksheets quickly](https://chandoo.org/wp/copy-worksheet-shortcut/) | [Kill NULLs – a Simple macro to save time when importing data from SQL Server](https://chandoo.org/wp/kill-nulls-a-simple-macro-to-save-time-when-importing-data-from-sql-server/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)