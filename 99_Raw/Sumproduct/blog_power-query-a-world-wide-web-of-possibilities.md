# Power Query: a World (Wide Web) of Possibilities

**Source:** https://sumproduct.com/blog/power-query-a-world-wide-web-of-possibilities/

---

[Home](https://sumproduct.com/)

\> Power Query: a World (Wide Web) of Possibilities

*   February 21, 2017

Power Query: a World (Wide Web) of Possibilities
================================================

Power Query: a World (Wide Web) of Possibilities
================================================

22 February 2017

_Welcome to our new Power Query blog. I have already shown how to extract and transform data from CSV files, folders and Access database tables. Today, I look at a potentially huge source of data – extracting data from the web…_

Whilst Power Query will allow data to be extracted from the web, for many webpages, some knowledge of HTML is needed, and even then, a great deal of transformation is often required to get the data into a tabular form. However, if the page uses tables, then the data can be much easier to extract. Today’s blog shows how to extract data from a webpage that holds information in a table.

For my example, I will use an excellent webpage which provides a list of training events by Excel specialists – perhaps it looks familiar?

![](https://sumproduct.com/wp-content/uploads/2025/05/e5ce99d85fcad3d88a345296bfc36e6f.jpg)

**Please Note**: Since this blog was written, we have moved to a new website and links have been updated.  To view the equivalent page on the new website, please use the link [www.sumproduct.com/public-courses/](https://sumproduct.com/public-courses/)
.

I start in the ‘Get External Data’ section, by choosing to get my data ‘From the Web’. The window that pops up gives me a choice of ‘Basic’ or ‘Advanced’ options. I could have used the basic option since my full web page is fairly short, but I have chosen the advanced option to show how webpage addresses may be built.

![](https://sumproduct.com/wp-content/uploads/2025/05/90e2800383a2a3084aa228f0a2def943.jpg)

I have chosen to access [https://www.sumproduct.com/courses](https://www.sumproduct.com/courses)
; I can opt to set timeouts if I find I am having problems with a particular website, but I will choose not to set any in this example (since I know how great this website is!).

If I were accessing [www.sumproduct.com](https://www.sumproduct.com/)
 for the first time, then I would be prompted to confirm the authentication options, which default to ‘Anonymous’. It is possible to see the same authentication options from ‘Data Source Settings’ in the ‘Settings’ section as shown below:

![](<Base64-Image-Removed>)

I have chosen to use the anonymous setting, since the webpage I am viewing does not require any password or other security information. Future queries accessing the same website will use the existing authentication settings.

Once the authentication method has been defined, Power Query links to the webpage and returns the recognised content.

![](<Base64-Image-Removed>)

The navigator pane above shows that Power Query has identified a document and a table. The document highlighted clearly doesn’t show any recognisable data about courses. More work would be required in order to obtain useful information from this. The table, however, proves more fruitful, as shown below:

![](<Base64-Image-Removed>)

I have a list of courses which I can edit (if required) and load to an Excel workbook. I choose to skip the edit step, and create the following workbook

![](<Base64-Image-Removed>)

The link to the webpage can be refreshed in the same way as other data sources. A word of caution however – in this case I have used a reliable source, which I know will be well maintained, and which will not be subject to abrupt format changes without warning. Using content which I have no control over is risky and can lead to bad decisions being taken as a result of using out of date or erroneous data. Good data can however be refreshed and uploaded – and this refreshing can be automated. More on how to automate refreshes next time…

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-a-world-wide-web-of-possibilities/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-a-world-wide-web-of-possibilities/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-a-world-wide-web-of-possibilities/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-a-world-wide-web-of-possibilities/#0)

[](https://sumproduct.com/blog/power-query-a-world-wide-web-of-possibilities/#0 "close")

top