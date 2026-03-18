# Power Query: Linking Up

**Source:** https://sumproduct.com/blog/power-query-linking-up/

---

[Home](https://sumproduct.com/)

\> Power Query: Linking Up

*   December 25, 2018

Power Query: Linking Up
=======================

Power Query: Linking Up
=======================

26 December 2018

_Welcome to our Power Query blog. This week, I look at how to view links in a webpage._

Unlike my usual Power Query blog, I am going to look at something that is impossible in Power Query (at the moment). Well, it is and it isn’t. Today’s Power Query lives in the Power BI application, and some **M** functions are available from Power BI, but not yet supported when running Power Query from the ‘Get & Transform’ section of the ‘Data’ tab. If I need to work with webpages, then running Power Query from [Power BI](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
 is very tempting.

To access queries from Power BI, I use the ‘Edit Queries’ option:

![](<Base64-Image-Removed>)

Once in the Power Query Editor, I can choose to create a query from ‘New Source’ in the ‘New Query’ section on the ‘Home’ tab. I will create a new Blank Query:

![](<Base64-Image-Removed>)

In my query, I am going to use two **M** functions that are not available to me when I run Power Query from Excel. The first is:

**Web.BrowserContents(url as text, optional options as nullable record) as text**

This returns the HTML for the specified `**url**`, as viewed by a web browser. An optional record parameter, `**options**`, may be provided to specify additional properties.

The second is:

**Html.Table(html as any, columnNameSelectorPairs as list, optional options as nullable record) as table**

This returns a table containing the results of running the specified **columnNameSelectorPairs** against the provided `**html**`. An optional record parameter, `**options**`, may be provided to specify additional properties.

I am going to combine these functions. To show what each one does, I will use **Web.BrowserContents()** first.

![](<Base64-Image-Removed>)

By using

**\= Web.BrowserContents(“https://www.sumproduct.com/”)**

I can see the contents of the famous website, [sumproduct.com](https://www.sumproduct.com/)
. Next, I need a step that will extract any links from this text:

![](<Base64-Image-Removed>)

This has been achieved using **M** code

**\= Html.Table(Source, {{“Link”, “a\[href^=””http””\]”, each \[Attributes\]\[href\]}})**

I don’t claim to have an encyclopaedic knowledge of the CSS selectors needed for this functionality – but a list of CSS selectors can be retrieved with a quick search online. This particular code searches all the **<a>** elements (as shown on the **WebBrowserContents()** example screen), where the **href** attribute begins ‘**http**‘ (and so calls a link).

I made this brief foray into Power BI territory because these functions are useful tools, which I hope to see in Excel’s Power Query / Get & Transform very soon (please?).

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-linking-up/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-linking-up/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-linking-up/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-linking-up/#0)

[](https://sumproduct.com/blog/power-query-linking-up/#0 "close")

top