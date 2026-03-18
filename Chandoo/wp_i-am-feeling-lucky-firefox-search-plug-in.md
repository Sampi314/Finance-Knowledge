# Install \"I am feeling lucky\" Firefox Search plug-in

**Source:** https://chandoo.org/wp/i-am-feeling-lucky-firefox-search-plug-in

---

“I am feeling lucky” Firefox Search plug-in
===========================================

[hacks](https://chandoo.org/wp/category/hacks/)
 , [ideas](https://chandoo.org/wp/category/ideas/)
 , [technology](https://chandoo.org/wp/category/computer/)
 - 0 comments

  

![google-iam-feeling-lucky-search-plug-in for mozilla firefox](https://chandoo.org/wp/wp-content/uploads/2008/06/google-iam-feeling-lucky-search-plug-in.jpg "google-iam-feeling-lucky-search-plug-in")

While trying to understand [how the Mozilla firefox search plug-ins work](http://labnol.blogspot.com/2006/09/learn-to-create-firefox-search-plugin.html)
 \[ [more](http://developer.mozilla.org/en/docs/Creating_OpenSearch_plugins_for_Firefox)\
 \] I got curious and wrote a search plug-in that will take you to the first Google search result directly instead of displaying the results pages, _ie_ mimicking the “I am feeling lucky” searches. Feel free to download and install it.

**1\. First [Download the Google “I am feeling lucky” search plug-in for Firefox](https://chandoo.org/wp/wp-content/uploads/2008/06/google_feeling_lucky.xml)
**  
2\. Save the file in your Firefox _searchplugins_ folder (usually, `C:\Program Files\Mozilla Firefox\searchplugins`, if not locate your Firefox installation directory and navigate to the ‘searchplugins’ folder)  
3\. Restart Firefox, thats all, you now have a shiny little search add-in that can make you feel lucky… 🙂

**  
For the curious, here is the xml file contents:**  
(If you are viewing this post in feedreader, you may not see the above code, in that case [visit the blog](http://chandoo.org/wp)
 to see it.)

* * *

<br /> <SearchPlugin xmlns="http://www.mozilla.org/2006/browser/search/"><br /> <ShortName>Google – Are you feeling lucky</ShortName><br /> <Description>Google Search</Description><br /> <InputEncoding>UTF-8</InputEncoding><br /> <Image width="16" height="16">data:image/x-icon;base64,R0lGODlhEAAQAPfLAAATVikwdA8SnxUfgAsWpAAilholjxw4jBc7kwAlvQQ2sRMsoBUqqhMzuhY/vxw4tSgmiyM1mSUztiQ6sTE3sQ4qyxMxxRoyxiAuxR1CtBxJsBxasSJuuTFguBte0Rlf2xVc9h9W9xVjzxVr0gdj6BRh4R1o5yBcyiZbyydT1i9b2Ddb1iFY6CJg2Vpor1dzvEJu20Z0yi23QDy1REi2OUy0O1WzOVC4PU+tVUe5Sk2xQU2zRUO4UE21Ula2SmKEqWWF2HyPx2+a6X6e6Xqk1m+s78sUDs4UGdEQB9YfDdwaANEfHd0YEscjAM4mAM0qANIoD9IkGdslGswuItYgL4aP0ImP2YGZ36Opzaq2wq/S+rzX/7/e8MrS1MLO/sTb48rT8snX/83c89PZ+crq+cH1/9Dl/9Ln/93r/9fy/+Hf7P/42eDm/O7u/+T29uX2/eT2/+f4/+f5/+j/9u//8+3/9u7/9ur5/+j//+n//+v//u3//+7//e7//+////b66/T/6vX/6/f/7f/07fj/4fv/4Pj/5v/45v7/4/r+7/3/6fDw+Pfx//D/9/X/8fT/8/f/8ff/8/D///H///L8/fL///P///X7//b6/ff/+/T///b9//f///v19//w9v/09P/29v/x+f/y///z///1+v/1///2///3//j79P/58/z/8/z99/z/9v7/9P7/9vn7//v6//j9//n9//j///n///v//vv////4+v/5+//6+P/4///6/P/6/v/6///7///9+P/8+v/9+v7/+Pz////8/f/9/f79///8///9//7//////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAEAAMsALAAAAAAQABAAAAj/AEn4oIFjBw8bOnrMuJGjhowZM1T8UdYJUZ5ZcNRYWjSrVK5QU0DMmtUnzRAXEy4o6FCEy6NDTkQIq1MmRgM0eZTlCXMgQJtRSE4gmgUkwh1EiZTNUiamy6NUUExcuoJgDCdDjQg9KgVL2SNFT1hwEvKglLBWuixZ+jSrlSBdRlL04bBBkTBdpZTpIqWsFaBcTEr0QaEhl6dWlswKW6poDRUPlmAUQKWMkTJLc76QMQNGUZMWgIgkCFJnlq5WXigwkFClVZQQyuRgELAlk7JBymCZGYAF0ZEPrQixgUDAihxVdPpoAZAFUZIRfThxgvPCwAILDipk+OFG2ZIVoxApERtPfvwlvZ+kQFzPvv0MJQEBADs=</Image><br /> <Url type="application/x-suggestions+json" method="GET" template="http://suggestqueries.google.com/complete/search?output=firefox&client=firefox&qu={searchTerms}"/><br /> <Url type="text/html" method="GET" template="http://www.google.com/search"><br /> <Param name="btnI" value="I'm Feeling Lucky"/><br /> <Param name="q" value="{searchTerms}"/><br /> <Param name="ie" value="utf-8"/><br /> <Param name="oe" value="utf-8"/><br /> <Param name="aq" value="t"/><br /> <!-- Dynamic parameters --><br /> <Param name="rls" value="{moz:distributionID}:{moz:locale}:{moz:official}"/><br /> <MozParam name="client" condition="defaultEngine" trueValue="firefox-a" falseValue="firefox"/><br /> </Url><br /> <SearchForm>http://www.google.com/firefox</SearchForm><br /> </SearchPlugin><br />

* * *

I just took the google.xml file in the searchplugins folder and added the line

<Param name="btnI" value="I'm Feeling Lucky"/> beneath the URL tag. This will tell Google that the button “I am feeling lucky” has been clicked and hence the search engine would redirect you to the first page of results instead of the results page. Cool eh?

* * *

[Click here to download the Google “I am feeling lucky” search plug-in for Firefox](https://chandoo.org/wp/wp-content/uploads/2008/06/google_feeling_lucky.xml)

* * *

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
| Written by Chandoo  <br>Tags: [cool](https://chandoo.org/wp/tag/cool/)<br>, [firefox](https://chandoo.org/wp/tag/firefox/)<br>, [google](https://chandoo.org/wp/tag/google/)<br>, [hacks](https://chandoo.org/wp/tag/hacks/)<br>, [I am feeling lucky](https://chandoo.org/wp/tag/i-am-feeling-lucky/)<br>, [ideas](https://chandoo.org/wp/tag/ideas/)<br>, [plug-in](https://chandoo.org/wp/tag/plug-in/)<br>, [search](https://chandoo.org/wp/tag/search/)<br>, [technology](https://chandoo.org/wp/tag/technology/)<br>, [web](https://chandoo.org/wp/tag/web/)<br>  <br>Home: [Chandoo.org Main Page](https://chandoo.org/wp/ "Chandoo.org - Learn Excel & Charting Online")<br>  <br>? Doubt: [Ask an Excel Question](https://chandoo.org/forums/) |     |

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/i-am-feeling-lucky-firefox-search-plug-in/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ

  

|     |     |
| --- | --- |
| « [Email marketing is NOT distributing pamphlets](https://chandoo.org/wp/email-marketing-is-not-distributing-pamphlets/) | [Am I a Japanese Translator?](https://chandoo.org/wp/am-i-a-japanese-translator/)<br> » |

**Meet Chandoo**

![Chandoo - Avatar](https://cache.chandoo.org/images/profile-pic-sbw.png)At Chandoo.org, I have one goal, "to make you awesome in Excel & Power BI". I started this website in 2007 and today it has 1,000+ articles and tutorials on data analysis, visualization, reporting and automation using Excel and Power BI.  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel + Power BI Newsletter](https://dogged-author-8382.ck.page/89b5d1883f)
.

**Connect:**

[Chandoo.org](https://www.pinterest.com/xlawesome/)