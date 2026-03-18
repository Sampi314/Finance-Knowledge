# What's New at CFI: FP&A Professional Model Protection & Presentation

**Source:** https://corporatefinanceinstitute.com/resources/finpod/fp-and-a-professional-model-protection-and-presentation

---

Listen Anywhere

*   [![https://cdn.corporatefinanceinstitute.com/wp-content/themes/cfi/dist/images/apple_podcasts.svg](https://cdn.corporatefinanceinstitute.com/wp-content/themes/cfi/dist/images/apple_podcasts.svg)\
    \
    Listen On\
    \
    Apple](https://podcasts.apple.com/us/podcast/finpod/id1743813595?uo=4)
    
*   [![https://cdn.corporatefinanceinstitute.com/wp-content/themes/cfi/dist/images/spotify.svg](https://cdn.corporatefinanceinstitute.com/wp-content/themes/cfi/dist/images/spotify.svg)\
    \
    Listen On\
    \
    Spotify](https://open.spotify.com/show/11emrVlIka1BhnB9CipMX8)
    
*   [![https://cdn.corporatefinanceinstitute.com/wp-content/themes/cfi/dist/images/overcast.svg](https://cdn.corporatefinanceinstitute.com/wp-content/themes/cfi/dist/images/overcast.svg)\
    \
    Listen On\
    \
    Overcast](https://overcast.fm/itunes1743813595)
    
*   [![https://cdn.corporatefinanceinstitute.com/wp-content/themes/cfi/dist/images/pocket_casts.svg](https://cdn.corporatefinanceinstitute.com/wp-content/themes/cfi/dist/images/pocket_casts.svg)\
    \
    Listen On\
    \
    Pocket Casts](https://pca.st/54ji7zjf)
    
*   [![https://cdn.corporatefinanceinstitute.com/wp-content/themes/cfi/dist/images/amazon_music.svg](https://cdn.corporatefinanceinstitute.com/wp-content/themes/cfi/dist/images/amazon_music.svg)\
    \
    Listen On\
    \
    Amazon Music](https://music.amazon.com/podcasts/5f2bde8c-ff43-41f6-9f85-bcac5d7e779c)
    
*   [![https://cdn.corporatefinanceinstitute.com/wp-content/themes/cfi/dist/images/youtube.svg](https://cdn.corporatefinanceinstitute.com/wp-content/themes/cfi/dist/images/youtube.svg)\
    \
    Listen On\
    \
    YouTube](https://youtu.be/1JtixSxw6v0?si=0VqiVrWvmn-guudF)
    

[Go Back](https://corporatefinanceinstitute.com/resources/finpod)

What’s New at CFI | FP&A Professional Model Protection & Presentation
=====================================================================

October 28, 2024 / 00:11:59 / E53

In this episode of _What’s New at CFI on FinPod_, we discuss the latest course in the FP&A Specialization, _FP&A Professional Model Protection and Presentation_. This course is the third in a series designed to equip financial professionals with advanced modeling skills. It focuses on essential practices for protecting and presenting financial models, making them more efficient and secure for long-term use.

We discuss the importance of model protection, including the different levels of safeguarding – from entire file locks to individual cell protection. Additionally, the episode explores practical presentation techniques like row grouping, custom views, and formatting tricks that enhance model usability and professionalism. If you’re looking to improve your FP&A model-building skills, this episode is full of valuable insights to help you get there.

  
  

**Transcript**

Ryan Spendeow (00:01)  
_Hello and welcome to this episode of What’s New at CFI. My name’s Ryan Spendelow and I’m a Senior Vice President here at CFI. I’m joined today by a fellow subject matter expert, Duncan McKeen And Duncan’s been one of the driving forces behind our new FP&A specialization which was recently launched. Today we’re here to talk about one of the new courses within that specialization and it’s called FP&A Professional Model_ _protection and presentation._

_So, hi there, Duncan. How are you today?_

Duncan McKeen (00:36)  
Great, Ryan! Yourself?

Ryan Spendeow (00:37)  
_Yeah, I’m doing really, really well, thank you. And I’m so glad that you can join us today. We’ve been talking about this series of new courses in the last few What’s New at CFI podcasts. And this is actually the third course in a series of three, is that right?_

Duncan McKeen (00:54)  
_Yeah, definitely, this is the third course in a series of three, probably my favorite of the three, I have to say. And just a quick recap, like in the first course, we really focused on_

_how to build the model template up. In the second course, we’re walking through how to use the model on a month -to -month basis as new data comes in, how to have a procedure to walk through to incorporate all the new data and analyze it. And then in this course, we’re talking about how to protect this model that we’ve spent so much time building up and also how to set all of the presentation settings. So it prints properly, it presents properly to the audience._

_Really a fun, like I said, my favorite course of the series of three for sure._

Ryan Spendeow (01:40)  
_Sounds really, really practical and useful, and it’s all those little tips and tricks that an FP&A professional could leverage to make themselves more effective and more efficient in their day-to-day roll-out by the sounds of it, Duncan. So I guess my first question to you is how often do you think model protection is actually used by FP&A teams?_

Duncan McKeen (01:52)  
_Yeah, definitely._

_I think not enough would be my quick answer. Yeah. It’s, it’s when you think about it, like you’ve spent so much time designing the model, building it. You’ve probably audited it yourself. You probably had peers check it and audit it. And then it’s, it’s absolutely crazy to like just hand it over or open it up to many, many people on the team to be able to get in it and do whatever they want without protecting it. It’s, it’s crazy because you can cause so much damage to a financial model._

_if you’re not using it correctly. So I would say that probably a lot of the FP&A teams are not using protection nearly as much as they should. And it’s funny, I used to do a ton of financial modeling consulting and we build a model for a client and when we’d hand it over, it’d be in pristine condition. And then they come back, you know, about 12 months later and it was absolutely destroyed, you know, cause they’d just been like overriding formulas with hard codes and tacking on little_

_partial inputs on the end of formulas and it was just like literally ruined over the course of 12 months. So it’s important to protect._

Ryan Spendeow (03:07)  
_Unrecognizable from how you handed it over, right?_

Duncan McKeen (03:11)  
_Yeah, it kind of looks very similar, but like the when you actually hit F2 and went into some of the formulas, you’re like, no._

Ryan Spendeow (03:19)  
_What have they been doing to my model? I jotted down a couple of questions that I want to ask you about this course, and I think, in some ways, you’ve already answered this a little bit. My next question was, why do you think it’s so important to include some protection in FP&A models? But I guess you’ve already spoken to that, haven’t you?_

Duncan McKeen (03:22)  
_Yeah, exactly._

_A little bit, I guess maybe the only bit that I’ll add is that you really want to design the protection because there’s going to be people working at different levels. So you may have a really senior person that’s very experienced on your modeling team and you could provide them with all of the passwords so that they can get into any part of the model and make a modification because you’ve worked with them for a long time. They’re very experienced. They know what they’re doing. A more junior member who’s just getting started in financial modeling, you may want to protect_

_down a lot of the parts of the model that have the formulas and maybe they’re just going to start off going in and putting and changing the inputs for example and they wouldn’t have the ability to modify formulas in the model. That’s probably the most common way of protecting. It’s just literally protect formulas and allow a person to just change inputs._

Ryan Spendeow (04:27)  
_Okay, so Duncan, it seems like there’s actually various levels of protection. What are the different levels that you can actually use to protect your FP&A model?_

Duncan McKeen (04:37)  
_Mm-hmm. Yeah, you’re right. Many levels. It’s part of the thing which makes it confusing in Excel. I think maybe part of the reason, to be fair to the audience, like part of the reason that people don’t use the protection in Excel, it’s so confusing. We try to sort of cut through that confusion and simplify it in the course. But basically, you can protect the entire file. So that’s literally the moment that you go into the drive and try to open it. Without a password, you can’t even open it. Okay, so that’s the first way to protect. That would be…_

Ryan Spendeow (04:51)  
_Alright, it is._

Duncan McKeen (05:06)  
_keeping non-team members out, for example. And then what you can do is then you can protect the workbook structure. So then let’s say you’re in the file, but you want to prevent somebody from say accidentally deleting a whole worksheet out of it. Imagine that. It’s also the interesting thing about deleting an entire tab, you can’t undo it. So there’s no control Z for that one. That’s why Excel asks you the question._

Ryan Spendeow (05:31)  
_There’s no Control Z, is there?_

Duncan McKeen (05:36)  
_Are you sure that you want to delete this because it can’t be undone? So that’s protecting the structure. And then what you can do is you can, you can actually put in protection on an individual cell level, which we also do in the course. So you can, you can literally say, right, these cells that are inputs, we’re not going to lock them down, but these other cells where we’ve spent a lot of time building and checking the formulas, we’re going to lock those cells. And so you can literally get right down to the cell level with the_

Ryan Spendeow (05:38)  
_Yeah. Yeah._

Duncan McKeen (06:06)  
_protection, and we go through also some automated ways of doing that quickly as well. So yeah, it’s very, very confusing, but we hope through this course that we’ve shed some light on it and made it easier for people to understand it and use it._

Ryan Spendeow (06:23)  
_Yeah, well that sounds super useful Duncan because I’ve always found going through and putting in a level of protection into an Excel workbook really confusing, partly because it’s not something that I do all the time. So when I have to revisit it, I always have to kind of think about how do I do this? And you’re right, it is quite confusing. So this sounds really useful. The course, Model Protection and Presentation. So as you’ve alluded to earlier, this course also covers_

Duncan McKeen (06:45)  
_Yeah, totally._

Ryan Spendeow (06:52)  
_the presentation. So, what kind of presentation skills are you going through on this course?_

Duncan McKeen (06:57)  
_Yeah, great question. Well, the first thing is we talk about printing, which sounds, it might sound relatively uninteresting, but you wouldn’t believe how many people struggle with it. There’s another example of something which should be easy in Excel, but Excel makes it very difficult. So we talk about exactly the right way to print a model, how to set it up. And the key to that really is selecting each page individually so you can have control over._..

_I’m sure you’ve tried that before where you grab an entire stack of schedules and you say print and it goes and it puts dotted lines across in places where you didn’t want them. It really doesn’t work. So we select all the pages individually and then we also show all of the people in the course exactly how to use some of the really cool print features. Like you can put really nice footers across the bottom of your page so you can show your actual file name and it’s dynamic. So you change the file name, it’ll change that on the footer._

Ryan Spendeow (07:32)  
_Yeah._

Duncan McKeen (07:54)  
_You can put a nice corporate logo in there. You can put the date or the time when it was printed dynamically include number of the page you’re on, the total number of pages. So these are nice features. If you either want to print it and present it on paper, or if you want to go ahead and save it as a PDF, then all of these neat features like the footers come through on that PDF as well. So we go through that. We also go through,_

_I’m sort of calling them presentation skills, but things like, you know, row grouping, using row grouping so you can collapse all the schedules down and get things looking like a table of contents. We talk about also, we go through a feature Ryan in Excel called custom views, which a lot of people have never ever encountered or used. It’s super, super cool. It allows you, that skill is more for the model builder themselves._

_What you can do is you can say, right, here’s my view of the revenue schedule and you can program it so that wherever you are in the model, you can just hit a quick keyboard shortcut and instantly go to the revenue schedule really fast. So you can program in all your schedules, revenue schedule, cost schedule, income statement, whatever they are, hit a keyboard shortcut and navigate to those really, really quickly. So it allows you to move really fast in the model. Yeah, we go through that as well_

_and the custom views also a great feature of them, which a lot of people don’t realize about them, is you can use them to open and close row grouping. So you can say, right, I want to go to a view where everything’s collapsed. And so you just hit a keyboard shortcut, bang, everything collapses. Or you can say, I want everything open now because I’m going to do some work and it’ll open them all up. So yeah, we go through those like little kind of hidden gems that are that are that have been in Excel for a long time, but a lot of people just don’t use them or know about them._

Ryan Spendeow (09:52)  
_Gosh! Those are some brilliant tips and tricks there, Duncan, and obviously if you’re an FP&A professional and you’re able to kind of demonstrate that level of Excel proficiency, you’re going to become the office guru in Excel, aren’t you? And just I love all those tips and tricks that are just going to make your life as an FP&A analyst just more productive and effective and efficient. So I’m definitely after this podcast going to go check out that custom views, I think that sounds brilliant._

Duncan McKeen (10:05)  
_Yes, for sure._

_Yeah, it’s a cool little feature in Excel for sure. Yeah. And it keeps track of exactly where you had the zoom levels as well. It keeps track of where you had the cursor. So you can set up the schedules exactly the way you’d like to see it, like stretched out so it fits on your screen. And then you hit the keyboard shortcut. It goes right back there. Yeah, it’s really neat. It’s super cool. There’s so much in Excel and a lot of the time Microsoft doesn’t talk about it maybe as much as they should, or maybe that’s our job to talk about it._

Ryan Spendeow (10:49)  
_Yeah._

Duncan McKeen (10:51)  
_‘Cause there’s some great stuff in there._

Ryan Spendeow (10:51)  
_Maybe that’s our job. Maybe that’s yeah. I mean, I’m glad that Microsoft doesn’t talk about it so much because it just makes, makes courses more valuable for our learners, Duncan. So it’s always nice to talk to someone that gets as excited about Excel as I do. I think you get more excited about Excel than I do. But this really does sound like a brilliant course. FP&A Professional Model Protection and Presentation. As Duncan mentioned, it’s the number three course in a series of three courses for FP&A model building._

Duncan McKeen (10:59)  
_For sure._

Ryan Spendeow (11:21)  
_So Duncan, thanks ever so much for joining us on this episode of What’s New at CFI. Thank you for listening, and hopefully, we’ll see you on the next podcast. Take care everybody. Bye-bye._

Duncan McKeen (11:32)  
_Thanks so much._

[Corporate Finance Institute](https://corporatefinanceinstitute.com/)

[Back to Website](https://corporatefinanceinstitute.com/)

0 search results for ‘’

People also search for: excel power bi esg accounting balance sheet fmva real estate

Explore Our Certifications

[Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)

[Commercial Banking & Credit Analyst (CBCA)®](https://corporatefinanceinstitute.com/certifications/commercial-banking-credit-analyst-certification-cbca/)

[Capital Markets & Securities Analyst (CMSA)®](https://corporatefinanceinstitute.com/certifications/capital-markets-securities-analyst-cmsa/)

[Certified Business Intelligence & Data Analyst (BIDA)®](https://corporatefinanceinstitute.com/certifications/business-intelligence-data-analyst-bida/)

[Financial Planning & Wealth Management Professional (FPWMP)®](https://corporatefinanceinstitute.com/certifications/financial-planning-and-wealth-management-fpwm-program/)

[FinTech Industry Professional (FTIP)®](https://corporatefinanceinstitute.com/certifications/fintech-industry-professional/)

Resources

[Mastering Excel Shortcuts for PC and Mac Work Smarter in Excel with Keyboard Shortcuts If you're still reaching for the mouse every few seconds, it's time to level up. The best Excel keyboard...](https://corporatefinanceinstitute.com/resources/excel/excel-shortcuts-pc-mac/)

[Financial Modeling Guidelines CFI’s free Financial Modeling Guidelines is a thorough and complete resource covering model design, model building blocks, and common tips, tricks,...](https://corporatefinanceinstitute.com/resources/financial-modeling/free-financial-modeling-guide/)

[SQL Data Types What are SQL Data Types? The Structured Query Language (SQL) comprises several different data types that allow it to store different types of information...](https://corporatefinanceinstitute.com/resources/data-science/sql-data-types/)

[Structured Query Language (SQL) What is Structured Query Language (SQL)? Structured Query Language (known as SQL) is a programming language used to interact with a database....](https://corporatefinanceinstitute.com/resources/data-science/structured-query-language-sql/)

[See All Resources See All](https://corporatefinanceinstitute.com/resources/)

Popular Courses

 [![Excel Fundamentals - Formulas for Finance](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 58" xml:space="preserve"></svg>)BIDA Prep Course 2h 14min Excel Fundamentals - Formulas for Finance](https://corporatefinanceinstitute.com/course/excel-fundamentals-formulas-for-finance/)

 [![3-Statement Modeling](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 58" xml:space="preserve"></svg>)FMVA Required 3h 15min 3-Statement Modeling](https://corporatefinanceinstitute.com/course/3-statement-modeling/)

 [![Introduction to Business Valuation](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 58" xml:space="preserve"></svg>)FMVA Required 3h 9min Introduction to Business Valuation](https://corporatefinanceinstitute.com/course/intro-business-valuation/)

 [![Scenario & Sensitivity Analysis in Excel](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 58" xml:space="preserve"></svg>)FMVA Required 49min Scenario & Sensitivity Analysis in Excel](https://corporatefinanceinstitute.com/course/sensitivity-analysis-financial-modeling/)

 [![Excel Data Visualization and Dashboards](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 58" xml:space="preserve"></svg>)FMVA Required 1h 32min Excel Data Visualization and Dashboards](https://corporatefinanceinstitute.com/course/dashboards-and-data-visualization/)

 [![Leveraged Buyout (LBO) Modeling](data:image/svg+xml,<svg id="L4" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 58" xml:space="preserve"></svg>)4h 33min Leveraged Buyout (LBO) Modeling](https://corporatefinanceinstitute.com/course/leveraged-buyout-lbo-modeling/)

[See All Courses See All](https://corporatefinanceinstitute.com/collections/)

Recent Searches

Suggestions

[Excel Courses](https://corporatefinanceinstitute.com/topic/excel/)
 [Financial Modeling & Valuation Analyst (FMVA)®](https://corporatefinanceinstitute.com/certifications/financial-modeling-valuation-analyst-fmva-program/)