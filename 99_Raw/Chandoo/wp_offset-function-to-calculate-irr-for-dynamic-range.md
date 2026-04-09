# Offset() function to Calculate IRR for Dynamic Range » Chandoo.org - Learn Excel, Power BI & Charting Online

**Source:** https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range

---

Offset() function to Calculate IRR for Dynamic Range
====================================================

[Financial Modeling](https://chandoo.org/wp/category/financial-modeling/)
 - 37 comments

  

**Offset() function to Calculate IRR for Dynamic Range**

When you start the project can you be sure, for how long will you operate it? A VC gives you funds to buy a commercial project. You are to operate the project for some time and then sell it off! Can you tell me today, when you will sell?

Real world is dynamic and business situations keep changing! Your excel is not that dynamic, when you use the IRR function and tell it to calculate the IRR, you show fixed cash flows! These cash flows are dynamic.

Not to worry! We have Offset function to our rescue!

**What is the Offset() function**

In my opinion it is one of the most versatile (And dangerous) functions to use. On the face of it, it is a simple function – As the name suggests, it just offsets your reference.

Offset( range, rows, columns, height, width )

[![image](https://chandoo.org/wp/wp-content/uploads/2011/09/image_thumb.png "image")](https://chandoo.org/wp/wp-content/uploads/2011/09/image.png)

![clip_image002](https://chandoo.org/wp/wp-content/uploads/2011/09/clip_image002.jpg "clip_image002")

**_So in the illustrated example, it starts from the C8 cell, moves 0 rows and 0 columns and then gives an array of size 5 x 5 to the sum function!_**

The difference – Now Offset is NOT returning a value. It is returning references to arrays!

**So what can you do with this function?**

Ah… you can do a lot! It can change diapers of your kids as well :-). Right now we will see, how it can introduce unparalleled flexibility in your models.

So the VC we were speaking about – gives you USD 1000. You propose to operate the commercial complex for 4 years and post that sell it off for USD 1200.

But then you are not certain if the economic & business conditions would be such that you need to operate it for 4 or 5 or even 6 years. You want a flexibility in the model to “Dynamically Update” itself.

[![offset](https://chandoo.org/wp/wp-content/uploads/2011/09/offset_thumb.gif "offset")](https://chandoo.org/wp/wp-content/uploads/2011/09/offset.gif)

**How do we implement this?**

The first step is to find the last cash flow in the assumption. I do that simply by counting the number of cash flows. It indicates the number of years that you run the business.

[![clip_image006](https://chandoo.org/wp/wp-content/uploads/2011/09/clip_image006_thumb.jpg "clip_image006")](https://chandoo.org/wp/wp-content/uploads/2011/09/clip_image006.jpg)

Once I have the number of cash flows with my, I dynamically return the size of the cash flow range using the offset function and input that to IRR function.

[![clip_image008](https://chandoo.org/wp/wp-content/uploads/2011/09/clip_image008_thumb.jpg "clip_image008")](https://chandoo.org/wp/wp-content/uploads/2011/09/clip_image008.jpg)

Since the offset returns reference to the array of cash flows, I can give that as an argument to the IRR function and it gets me the IRR of the project!

If a new cash flow is entered, the count function would calculate it, pass it to the offset function, which would return the new range to IRR. Phew!!

**Few more places, where you can use Offset function**

Anywhere you want references to be returned, Offset function does come handy. Similarly I have found offset to be a very useful function if you are looking at creating scenarios, especially in Merger Modeling, Growth Assumptions, Economic Assumptions, etc. With the click of the mouse, it can completely update your model!

**Beware**

In my modeling experience I have found the following three functions to be quite versatile with the ability to surprise you with their power!

· Offset

· Indirect

· Index

They can return references. This is not usually what you expect Excel to do. So when you are not expecting they can return references to unknown ranges and surprise you. They can make understanding of model (for the reader of your model) fairly difficult and auditing your model difficult. So use them with care!

**Do you use these functions?**

These functions can make your financial model quite flexible. Do you use such functions in your models? Share your views and experience on making your model more flexible!

**Templates to download**

I have created a template for you, where the subheadings are given and you have to link the model to get the cash numbers! You can [download the same from here](https://chandoo.org/wp/wp-content/uploads/2011/09/Par-Dynamic-IRR.xlsx)
**.** You can go through the case and fill in the yellow boxes. I also recommend that you try to create this structure on your own (so that you get a hang of what information is to be recorded).

Also you can download this filled template and check, if the information you recorded, [matches mine or not](https://chandoo.org/wp/wp-content/uploads/2011/09/Ins-Dynamic-IRR.xlsx)
!

### Join our Financial Modeling Classes

We are glad to inform that our new financial modeling & project finance modeling online class is ready for your consideration. **[Please click here to learn more about the program & sign-up.](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp)
** _Chandoo.org has partnered with Pristine to launch a Financial Modeling Course. [**For details click here**](http://chandoo.org/wp/financial-modeling/ "Financial Modeling Online Training Program - Chandoo.org")
._ [![Financial Modeling using Excel - Online Classes by Chandoo.org & Pristine](https://cache2.chandoo.org/content/fm/financial-modeling-class-msg-1.png)](http://chandoo.org/wp/financial-modeling/?utm_source=chandoo.org&utm_medium=fmp "Financial Modeling using Excel - Online Classes by Chandoo.org & Pristine")
 For any queries regarding the cash impact or financial modeling, feel free to put the comments in the blog or write an email to [paramdeep@edupristine.com](mailto:paramdeep@edupristine.com)

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
| Written by paramdeep@gmail.com  <br>Tags: [excel 2007](https://chandoo.org/wp/tag/excel-2007/)<br>, [Financial Modeling](https://chandoo.org/wp/tag/financial-modeling/)<br>, [Financial Modeling School](https://chandoo.org/wp/tag/financial-modeling-school/)<br>, [OFFSET()](https://chandoo.org/wp/tag/offset/)<br>, [tips](https://chandoo.org/wp/tag/tips/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### 37 Responses to “Offset() function to Calculate IRR for Dynamic Range”

1.  ![](https://secure.gravatar.com/avatar/bc64a3325a83a9e301d755d35327fdc6eb8bb39edb5a23e5f22af056ab0a452b?s=64&d=mm&r=g) Lianna says:
    
    [October 4, 2011 at 3:44 pm](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209249)
    
    Awesome stuff. Offset / Index are great for moving averages too. Not sure what I'd do with Indirect.
    
    One thing is certain - you will spend half the time saved explaining to folks what your formula does.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209249)
    
2.  ![](https://secure.gravatar.com/avatar/51ae33943eba48f67d13146af3c083a3fa3eea8f64c939273bf3e0d5ebb30a05?s=64&d=mm&r=g) [Prakash Singh Gusain (PSG)](http://prakashgusain.blogspot.com/)
     says:
    
    [October 4, 2011 at 7:03 pm](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209252)
    
    I use them at work for creating Dashboards. I love them all 🙂
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209252)
    
3.  ![](https://secure.gravatar.com/avatar/d75b2dded123620d1ff6dfa9b7a458edb6eaa3f87950e3daa6570cc253e0163b?s=64&d=mm&r=g) John H says:
    
    [October 5, 2011 at 12:06 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209255)
    
    This post is a beauty and another example of why I love this site!
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209255)
    
4.  ![](https://secure.gravatar.com/avatar/586aa5f4d031191b4717c72c526863bf332fcf0059d9abac1d4a6153e4e9c4fe?s=64&d=mm&r=g) Andrew says:
    
    [October 5, 2011 at 12:06 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209256)
    
    Indirect() is good for cascading data validation - based on the value in another cell.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209256)
    
5.  ![](https://secure.gravatar.com/avatar/7426eab78443c4e9359b02fd169b251fc5f528a999de075c6b79803498682152?s=64&d=mm&r=g) Mike86 says:
    
    [October 5, 2011 at 2:36 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209258)
    
    You could make it really dangerous and use:
    
    IRR=offset(E3,0,0,1,counta(3:3)-1)
    
    Dynamic update just waiting for someone to put a text string into another row 3 cell.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209258)
    
6.  ![](https://secure.gravatar.com/avatar/7adcd34ffe6350b11faed34c5a6eff04cec015e552b0611a9aeb409b04f7a8a0?s=64&d=mm&r=g) K Mac says:
    
    [October 5, 2011 at 4:47 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209261)
    
    Definitely pretty useful stuff especially with rolling periods but as  
    Lianna & Mike86 allude to can be pretty dangerous in the hands of babes and most likely a feature that requires some explanation where a workbook is distributed.
    
    The reality is that for many users a combination of more than one function in any one formula frightens the hell out of them and they never bother to read even the introductory paragraph in Help (what's that?) to give them a clue as to the nature of the formula
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209261)
    
7.  ![](https://secure.gravatar.com/avatar/ba756660793bf222714be273cae197cfbc137c30414089edfcbd620771c95218?s=64&d=mm&r=g) Imran says:
    
    [October 5, 2011 at 6:41 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209265)
    
    Hi Chandoo,  
    I recently started using your site and I am pretty impressed.  
    This is the 1st time I am commenting.  
    Just to know, why not we have the dynamic range of cashflows in a excel table, so that we can refer it in the IRR calculation so that it auto adjusts?  
    I hope I am not fooling myself 🙂  
    Thanks.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209265)
    
8.  ![](https://secure.gravatar.com/avatar/ebfcd2219316d63259822e474d1c613329685f5fb81d9125e27812c4f015c8ed?s=64&d=mm&r=g) paramdeep@gmail.com says:
    
    [October 5, 2011 at 7:25 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209266)
    
    @Lianna, @PSG, @John: Thanks  
    @Andrew: Thanks. This is a great usage. Have you used it in financial models?  
    @Mike: Yes. If the full row is selected, it would be still more dangerous! 😉  
    @Mac: I am assuming that this function is not for "babes" 🙂
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209266)
    
9.  ![](https://secure.gravatar.com/avatar/ecc8d7f4f4dec73ef8b6d699628a9042ed5422d282f52be5789b5f12d9b3c0e7?s=64&d=mm&r=g) DQKennard says:
    
    [October 6, 2011 at 1:42 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209292)
    
    I've used Indirect to construct lookup references (e.g. in Index functions). In the article example, FY column headers could be used to construct references to the correct datasheet or table for that fiscal year, to be used in Index, Match, etc.
    
    I use Index all the time, usually with Match to determine row, and/or column. Match for column in a table header row is much more dynamic, since it avoids the hard coded column number, and can be much more explainable and extensible -- e.g. this is row "Exempt" so I'm looking for column "Exempt" and entering another row is much easier.
    
    Sometimes, my row Match function has things like Match(criteria1&criteria2,array1&array2,0) requiring the index and whatever else it's embedded in to be an array formula.
    
    These could, of course, be all mashed together in one big unholy nested function: Indirects to determine where to look, Counts to determine how big the arrays are, Offsets to return the arrays, Match to access the arrays, Index to determine which array member to use, wrapped in If to handle errors and such, and the whole thing's an array formula. I wouldn't leave that out and visible where someone might see it. 🙂
    
    I've used Offset less. I've used it to compare rows above and below for duplicate checking in sorted data, or to conditionally format duplicates, or to change color based on changes in section/group.
    
    Since I've always used offset to, well, \*offset\*, I've never thought about using the height and width to return dynamic arrays. I can use that. Thanks.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209292)
    
10.  ![](https://secure.gravatar.com/avatar/d8dca7d1b7d98efad4f71339cb0b6a5df442fb687a1ccfef586c335a548c85cf?s=64&d=mm&r=g) [Mawdo81](http://www.mypetbubble.com/)
     says:
    
    [October 6, 2011 at 7:34 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209295)
    
    Hi,  
    Offset is Key for any sort of data validation list.  
    Keep 1 sheet for your options and arrange these in lists. I always use shOptions as codename for this sheet, allowing me reuse code mudules easily.
    
    Use offset to name ranges and then use the data validation list as =namedrange
    
    Hide & protect shOptions.
    
    This give you a very quick and easy way to add additional items to the data validation (new product for example). Or you can build a userform and allow users to add to these lists without fear of them breaking your workbook.
    
    Hope that helps,
    
    M
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209295)
    
11.  ![](https://secure.gravatar.com/avatar/f62a5ddddfaff83c54d7892682f96bb41bedc3eb81cc3b47761e4e8d4b0f6a11?s=64&d=mm&r=g) Alex says:
    
    [October 6, 2011 at 1:11 pm](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209330)
    
    My problem with Offset function that it keeps recalculating the spreadsheet. As it has become very large with over 5000 rows, this takes a long time even if nothing has changed and I open my spreadsheet. Any solutions for this
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209330)
    
12.  ![](https://secure.gravatar.com/avatar/266f3f67d3fd200718e02f1863b65ca1fde0088504bb58a771150aacc0c58873?s=64&d=mm&r=g) Mark says:
    
    [October 6, 2011 at 4:20 pm](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209348)
    
    Alex, use INDEX to create your dynamic ranges in a psuedo-volatile way (see examples @ excelhero). Hope this helps.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209348)
    
13.  ![](https://secure.gravatar.com/avatar/ebfcd2219316d63259822e474d1c613329685f5fb81d9125e27812c4f015c8ed?s=64&d=mm&r=g) paramdeep@gmail.com says:
    
    [October 7, 2011 at 8:59 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209377)
    
    @Imran: Thanks. If you link this IRR to a data table, it should still work. But how do you input the new cash flows in the cells (dynamically)?  
    @DQKennard: 🙂 As chandoo would say, you would definitely need a laaarge cup of caffe latte to understand that function! 😉  
    @Alex: As Mark has pointed out, Index can be use there. Else, I guess you can remove the auto calculate in Excel (File --> Excel Options --> Formulas) and make it manual.  
    @Mark: Thanks.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209377)
    
14.  ![](https://secure.gravatar.com/avatar/d8dca7d1b7d98efad4f71339cb0b6a5df442fb687a1ccfef586c335a548c85cf?s=64&d=mm&r=g) [Mawdo81](http://www.mypetbubble.com/)
     says:
    
    [October 7, 2011 at 9:09 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209378)
    
    @paramdeep:  
    Please don't turn of auto calculate! It has to be one of the worst feature in Excel! I understand why some might need to very occassionally turn it off but it should be avoidable through good workbook design.
    
    There is never enough visual clues to when it is off & if users don't know that it is off it can cause all sorts of errors becuase the result cells aren't always the result that should be given based on the inputs.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209378)
    
15.  ![](https://secure.gravatar.com/avatar/ebfcd2219316d63259822e474d1c613329685f5fb81d9125e27812c4f015c8ed?s=64&d=mm&r=g) paramdeep@gmail.com says:
    
    [October 10, 2011 at 7:18 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209407)
    
    @Mawdo: I agree it is not a good idea to turn off auto calculate. But if your sheet has become slow because of this, you can turn it off, and then remember to turn it on, once the model is built! 🙂
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209407)
    
16.  ![](https://secure.gravatar.com/avatar/d8dca7d1b7d98efad4f71339cb0b6a5df442fb687a1ccfef586c335a548c85cf?s=64&d=mm&r=g) [Mawdo81](http://www.mypetbubble.com/)
     says:
    
    [October 11, 2011 at 7:45 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209428)
    
    @paramdeep:  
    I think we'll have to agree to dis-agree on this one. 😉
    
    I stand by my comment that it should be avoidable through good workbook design.
    
    Keep up the goodwork on the rest though, I'm fairly new to the site but its quickly moving up my "go-to" list.  
    M
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209428)
    
17.  ![](https://secure.gravatar.com/avatar/adf684a131f430f8b4b8f57d80283cfcab9c8dd16a1899b738abdbded43aa1ad?s=64&d=mm&r=g) marninei says:
    
    [October 15, 2011 at 8:51 pm](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209758)
    
    Hi all,
    
    New to this site, very impressive.
    
    I am a financial consultant\\modelist, and where I work people used to write dynamic offsets as: OFFSET(ref,row,column):OFFSET(ref,row,column). This of course made formulas extremely long, but when I started working there I didn't know about the height\\width options.  
    As time went by I learned to use height\\width and got people around me to shrink their formulas by using them.  
    generally I'm not a big fan of offsets because their so hard to audit, BUT, the funniest thing happened last week. I was auditing a model (I use Explode Add-In, by xl-logic.com) and usually the addin doesn't help much with offsets because it only helps you jump to the references but you don't see the actual result. ANYWAY, I found out that when you use the OFFSET:OFFSET way of writing, explode jumps you to the offset's result, i.e. the range refered to.
    
    Now I find myself thinking what do I prefer, shorter, more readable lines or easier use of audit tools....
    
    Any thoughts?
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209758)
    
18.  ![](https://secure.gravatar.com/avatar/d8dca7d1b7d98efad4f71339cb0b6a5df442fb687a1ccfef586c335a548c85cf?s=64&d=mm&r=g) [Mawdo81](http://www.mypetbubble.com/)
     says:
    
    [October 17, 2011 at 11:14 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209925)
    
    @marninei - Can you edit Explode? Or Can you get the functionality added in, Offest is widely used & I used to be a massive advocate so it would make sense for Explode to be able to cope with that. As far as I would have thought, it is a change from coping with Offset retruning a cell to coping with it returning a range.
    
    @ Mark et all - Excel Hero's dynamic range using Index is very powerful & I've become a convert. Offset is powerful but volatile. I was happy with that due to the frequency of the ranges I tended to use it for. (Named formula to be exact, so not needing as many re-calcs as it might otherwise). However in trying to access some of these ranges the other day, from external workbooks, I realised the limitation of Offset - the workbook needs to be open to return what ever it would have returned. The index solution doesn't, leaving you with names you can access freely with data as current as when the source was last saved.
    
    M
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-209925)
    
19.  ![](https://secure.gravatar.com/avatar/adf684a131f430f8b4b8f57d80283cfcab9c8dd16a1899b738abdbded43aa1ad?s=64&d=mm&r=g) marninei says:
    
    [October 18, 2011 at 8:54 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-210039)
    
    @Mawdo81 - Sadly, explode is locked. btw, if any of you haven't experienced its power I advise you all to try it. It's an amazing auditing tool.  
    About offset, I think there are situtions for using every formula, but as you know sometime people "fall in love" with a single formula and use it for practically everything, even when there are much more useful, simple, elegant tools to use. Dynamic IRR is one of the best things to use offsets for, since sometimes the cashflow's first periods are zero, resulting in the IRR returning either zero or an error.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-210039)
    
20.  ![](https://secure.gravatar.com/avatar/e04d231c585ed95e422c0515087a8bd0062696167f3caf88446a001f333d39e5?s=64&d=mm&r=g) Model\_Citizn says:
    
    [January 16, 2012 at 12:29 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-219404)
    
    Thanks, useful tool...how would one do this dynamic change for XIRR which relies on dates as an input..doesnt quiet work as easily.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-219404)
    
    *   ![](https://secure.gravatar.com/avatar/ebfcd2219316d63259822e474d1c613329685f5fb81d9125e27812c4f015c8ed?s=64&d=mm&r=g) [paramdeep@gmail.com](http://www.edupristine.com/)
         says:
        
        [April 14, 2012 at 7:35 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-222415)
        
        @Model\_Citizn: I am sorry for the delayed reply. I seem to have missed the comments on the thread! But just like we find the dynamic range of cash flow using offset, you can find the dates using offset. It is just extending the same logic on two rows instead of one!
        
        [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-222415)
        
21.  [Reporting Scenarios using Offset | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2012/02/14/reporting-scenarios-using-offset/)
     says:
    
    [February 14, 2012 at 8:34 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-220204)
    
    \[...\] few months back, I had written about the offset function and how it can be used to create flexible models. I had discussed at that point of time, why offset function is one of the most versatile functions \[...\]
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-220204)
    
22.  ![](https://secure.gravatar.com/avatar/041df521133ab47458eb54c8f3844b10888290b50396d3986d4a214b64008df9?s=64&d=mm&r=g) Himanshu Arora says:
    
    [April 13, 2012 at 9:15 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-222310)
    
    Thank You..I understood how to use and apply "Offset" function from this article
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-222310)
    
    *   ![](https://secure.gravatar.com/avatar/ebfcd2219316d63259822e474d1c613329685f5fb81d9125e27812c4f015c8ed?s=64&d=mm&r=g) [paramdeep@gmail.com](http://www.edupristine.com/)
         says:
        
        [April 14, 2012 at 7:33 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-222414)
        
        @Himanshu: Thanks
        
        [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-222414)
        
23.  ![](https://secure.gravatar.com/avatar/a29d71d1b6d71509542ce4acf78722c0f8a7e24b100ffb9fca4ddbde4a39e91d?s=64&d=mm&r=g) Ed says:
    
    [January 23, 2014 at 2:51 pm](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-466762)
    
    HEy Chandoo - any advice on how to calculate IRR when the cashflow values are not in an array? I have a situation where all the cashflow values are in a column array except for the final one that is in the correct row but in a different column.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-466762)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [January 24, 2014 at 2:08 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-466837)
        
        @Ed
        
        I'd setup a range and transfer all values, using formulas, into a single location so that it can be simply used
        
        [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-466837)
        
24.  ![](https://secure.gravatar.com/avatar/f3e009e12345faac330c79c25fdf7288272f588055c62627f153f0ad2a2655a2?s=64&d=mm&r=g) Nara says:
    
    [February 28, 2014 at 10:28 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-471966)
    
    I have downloaded Flexible IRR Model and followed all the steps. And then I simply put IRR formula to (E3:S3 ) range and whatever I do, I get the same results by using both options.
    
    The only exception is when I don't put any number in-between two but then if I put zero, I get the common result which was different from IRR results from two different options.
    
    So what's the point of OFFSET function in this calculation?
    
    Thanks
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-471966)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [February 28, 2014 at 1:49 pm](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-471993)
        
        @Nara
        
        Chandoo's formula =IRR(Offset(E3,0,0,1,E5))  
        Allows the user to change the value in E5 ie the number of years and the formula adjusts itself
        
        Using Offset in an IRR or other function that requires a range allows you to make it dynamic or variable based on a cell's value eg: E5
        
        That is as the data is added to the range changes automatically
        
        So Chandoo could also use  
        \=IRR(Offset(E5,0,0,1,Counta(E5:Z5)))  
        and the formula would adjust itself as you added extra years to the project
        
        [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-471993)
        
        *   ![](https://secure.gravatar.com/avatar/f3e009e12345faac330c79c25fdf7288272f588055c62627f153f0ad2a2655a2?s=64&d=mm&r=g) Nara says:
            
            [March 1, 2014 at 7:32 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-472110)
            
            @Hui
            
            But if you add IRR function in the same spreadsheet and tIn IRR function select the whole line indicating cashflow amounts, you will get the same results. I have tested by adding cashflows in following years. As I said the only difference came in the case of living blank cell in-between.
            
            [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-472110)
            
25.  [Calculate CAGR (Compunded Annual Growth Rate) using Excel \[Formulas\] | Chandoo.org - Learn Microsoft Excel Online](http://chandoo.org/wp/2014/04/29/calculate-cagr-using-excel/)
     says:
    
    [April 29, 2014 at 8:11 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-499590)
    
    \[…\] Related: Using IRR() function over a dynamic range with OFFSET. \[…\]
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-499590)
    
26.  ![](https://secure.gravatar.com/avatar/df19dfb5f2d7e39c503985d1ee7c6d0336cbd88229b1d983e247a7e0f93dfcc1?s=64&d=mm&r=g) Dianne Souder says:
    
    [May 6, 2014 at 11:21 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-518609)
    
    Is the CAGR applicable to the growth rate of spend as well?
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-518609)
    
27.  ![](https://secure.gravatar.com/avatar/c6ca2630c80ea6b661a37c10cf6295b04be2205392ebe8a78e8287639266c116?s=64&d=mm&r=g) Bryan says:
    
    [October 4, 2016 at 9:13 pm](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-1303756)
    
    Does anyone know if you can skip cells with values in XIRR functions? There is one line of data i want to skip for the XIRR calc without having to delete anything or copy the data anywhere else.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-1303756)
    
    *   ![](https://secure.gravatar.com/avatar/857be1660dc31ec491b32a9e8b9d4f678ac70575ae3466658e6e6ccd5e860e4f?s=64&d=mm&r=g) [Hui...](http://chandoo.org/wp/about-hui/)
         says:
        
        [October 5, 2016 at 1:34 am](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-1304002)
        
        @Bryan
        
        No and Yes
        
        If you use a straight range, No  
        But you maybe able to use a formula to extract the Cashflows & Dates for use in the XIRR Function
        
        For transparency you are better to extract the data to a separate range and then do the Xirr calcs on that range
        
        If you want specific help can you please ask the question in the Chandoo.org Forums [http://forum.chandoo.org/](http://forum.chandoo.org/)
          
        and please attach a sample file
        
        [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-1304002)
        
28.  ![](https://secure.gravatar.com/avatar/69bcf8bb5ace1bfb11f682eabc18f7fe1ca503bbc8685fdeb5865c90c97c84a1?s=64&d=mm&r=g) Roger says:
    
    [June 10, 2017 at 8:09 pm](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-1459226)
    
    Absolutely beautiful! Thank you for the elegant solution and the clear explanation of this function's purpose and usage.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-1459226)
    
29.  ![](https://secure.gravatar.com/avatar/8f37210f534140b1ecefab12741c322f0a20c926b1d7c9a9e55a32c098793583?s=64&d=mm&r=g) Tom says:
    
    [December 15, 2021 at 4:07 pm](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-2053487)
    
    I am trying to create a dynamic range based on the number of months eclipsed to an IRR function. I would like to get your input on how to do that.
    
    Example:
    
    \[Cell A1\] Beg Balance = -20000  
    \[Cell A2\] Monthly Contribution = -200  
    \[Cell A3\] End Balance = 25000
    
    \[Cell A4\] IRR % after 5 months of contributions =IRR((A1,A2,A2,A2,A2,A2,A3),0.01)
    
    I am wanting to avoid adding another A2 after each new month.
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-2053487)
    
30.  ![](https://secure.gravatar.com/avatar/fcad759e633ecb9101be2109a353b663da8350ef61edcdfdfaa7574022feeb71?s=64&d=mm&r=g) David says:
    
    [November 2, 2023 at 9:06 pm](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-2150779)
    
    Hi All,
    
    Any idea on how to use offset to calculate IRR dynamically between two date ranges. For example, I want to calculate IRR between two dates of my choosing. e.g. between Jan and Apr or between 2023 and 2027. The formula and IRR calculation needs to be set up to be dynamic though so that I can switch dates at my discretion.
    
    Thanks  
    David
    
    [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-2150779)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 6, 2023 at 8:01 pm](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-2151762)
        
        If you are using Excel 365, you can use FILTER to first filter down the data to the relevant dates and the send that to IRR.  
        Something like this:  
        \=IRR(FILTER(values, (datecolumn>=start\_date)\*(datecolumn<=end\_date)))
        
        [Reply](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#comment-2151762)
        

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/offset-function-to-calculate-irr-for-dynamic-range/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [A Challenge from Hui](https://chandoo.org/wp/a-challenge-from-hui/) | [Filter values where Fruit=Banana OR Sales>70. In Other Words, How to use Advanced Filters?](https://chandoo.org/wp/how-to-use-advanced-filters/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)