# How to Embed Youtube Video in Excel Worksheet

**Source:** https://trumpexcel.com/embed-youtube-video-in-excel

---

[Skip to content](https://trumpexcel.com/embed-youtube-video-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/embed-youtube-video-in-excel/#below-title)

**Watch Video – How to Embed Youtube Video in Excel**

Embedding a Youtube video in Excel could be helpful if you want the user to go through some instructions in the video before using the spreadsheet/model/dashboard. I sometimes use it during excel training session with live examples.

In this blog post, I will show you how you can embed youtube video in Excel.

#### **Step 1 – Modify Youtube URL**

1.  Get the youtube video URL. I am using the URL of a popular video from my [Youtube channel.  \
    ![Embed Youtube Video in Excel - Original URL](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20477%2041'%3E%3C/svg%3E)](https://www.youtube.com/c/trumpexcel)
    
2.  Modify the youtube link by making the following changes
    *   Remove **watch?**
    *   Replace = after v with a forward slash (v= becomes v/)  
        ![Embed Youtube Video in Excel - Link Modify](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20425%20100'%3E%3C/svg%3E)
    *   Add **&vq=hd720** at the end of the URL to play it in HD mode. Make sure that the video has the HD mode available in youtube (if not, do not add &vq=hd720).
    *   The resulting URL looks like this  
        ![Embed Youtube Video in Excel - Link FINAL](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20447%2043'%3E%3C/svg%3E)
3.  We will use this URL in Step 2 to embed this video in Excel

#### **Step 2 – Embed Youtube Video in Excel**

1.  Go to Developer Tab. If you do not have a developer tab in ribbon, [click here to learn on how to enable it](https://trumpexcel.com/excel-developer-tab/)
    .
2.  In developer tab, go to Insert –> More Controls.  
    ![Embed Youtube Video in Excel - More Controls](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20256%20222'%3E%3C/svg%3E)
3.  In More Controls dialogue box, select Shockwave Flash Object and click OK  
    ![Embed Youtube Video in Excel - Shockwave Flash File](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20254%20205'%3E%3C/svg%3E)
4.  Click anywhere on the sheet and it will insert the Shockwave Flash Object
5.  Right click on the Shockwave Flash Object and Click on Properties
6.  In the Shockwave Flash Object Properties dialogue box, make the following changes
    *   _AllowFullScreen:_ True (This enables you to play the video in full-screen mode)
    *   _Movie:_ https://www.youtube.com/v/Gm5m-y49rI0&vq=hd720 (it is the modified URL created in Step 1)  
        ![Embed Youtube Video in Excel - Properties](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20452%20347'%3E%3C/svg%3E)
7.  Close the properties window. Go to Developer and click on Design Mode. This will get you out of Design Mode and you would see youtube video load in the flash object space. Click on play to watch the video.

_**Caution:** Do not save in compatibility mode. It may not work when you re-open it. Save it in XSLX or XLSM format_

_**Try it yourself.. Download the file  
[![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%2050'%3E%3C/svg%3E)](https://trumpexcel.com/wp-content/uploads/2014/07/EmbedYoutubeVideoinExcel.xls)
**_

**You May Also Like the following Excel Tutorials:**

*   [How to Insert and Use a Checkbox in Excel](https://trumpexcel.com/insert-checkbox-in-excel/)
    .
*   [How to Insert a Watermark in Excel](https://trumpexcel.com/insert-watermark-in-excel/)
    .
*   [How to Insert Picture Into Excel Cell](https://trumpexcel.com/insert-picture-into-excel-cell/)
    .

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

8 thoughts on “How to Embed Youtube Video in Excel Worksheet”
-------------------------------------------------------------

1.  When I try to insert the Shockwave Flash Object, Excel gives me an error message that says — Cannot Insert Object
    
    [Reply](https://trumpexcel.com/embed-youtube-video-in-excel/#comment-10448)
    
2.  Hi colleague, i have a problem with the embedded video. I do all steps but get the next: Flash-embedded videos are no longer supported, but you can still watch this video on Youtube
    
    [Reply](https://trumpexcel.com/embed-youtube-video-in-excel/#comment-10213)
    
3.  I can’t find shockwave Flash Object in my Excel 2013…any suggestion?
    
    [Reply](https://trumpexcel.com/embed-youtube-video-in-excel/#comment-1649)
    
    *   Hi Asif. It should be an inbuilt feature in the More Controls option. It should be there by default. If you can’t find it may be it is a version issue or installation issue. You can try on some other system or try and re-install again.
        
        [Reply](https://trumpexcel.com/embed-youtube-video-in-excel/#comment-1651)
        
4.  I have published 5 videos with the same exact technique and much more about that 1 and a half year ago ! Look in my channel for videos n 6 n 7 n 8 and videos n 21 and n 22 –> [https://www.youtube.com/watch?v=QWeKIJ\_9-L8&list=PLTHRcVBVe5jgtHbDCn2dsDXcT05X8vpOe&index=6](https://www.youtube.com/watch?v=QWeKIJ_9-L8&list=PLTHRcVBVe5jgtHbDCn2dsDXcT05X8vpOe&index=6)
    
    [Reply](https://trumpexcel.com/embed-youtube-video-in-excel/#comment-1508)
    
    *   🙂 Thanks . . .
        
        [Reply](https://trumpexcel.com/embed-youtube-video-in-excel/#comment-14776)
        
5.  Great tip 🙂  
    Thx for sharing.
    
    [Reply](https://trumpexcel.com/embed-youtube-video-in-excel/#comment-1444)
    
    *   thanks
        
        [Reply](https://trumpexcel.com/embed-youtube-video-in-excel/#comment-14141)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/embed-youtube-video-in-excel/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK