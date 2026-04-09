# Power BI Blog: Suggested Synonyms from Copilot

**Source:** https://sumproduct.com/blog/power-bi-blog-suggested-synonyms-from-copilot/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Suggested Synonyms from Copilot

*   February 14, 2024

Power BI Blog: Suggested Synonyms from Copilot
==============================================

Power BI Blog: Suggested Synonyms from Copilot
==============================================

15 February 2024

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at Copilot sticking its oar in and suggesting synonyms._

The Q&A visual allows you to ask questions about your data and get answers in the form of visual. It provides any report viewer with an intuitive means to explore their data without requiring deeper knowledge of the model or report authoring. I know; I have relied upon it for years!

![](<Base64-Image-Removed>)

Presently, the Q&A visual doesn’t rely upon generative AI to function. The Q&A engine processes your natural language input all inside Power BI algorithmically using a variety of linguistic principles, associating words and phrases you use with data in your model. This makes it good at answering precise questions about your data, but it may not be able to associate everything you input with data in the model.

To help authors ensure that the Q&A visual provides consistent and accurate answers based upon the unique language their report consumers actually use, Microsoft has introduced Q&A setup tools with an emphasis on providing Q&A with synonyms for column and table names in the model. This way, authors may explicitly define different ways people might refer to their data, and users will always receive the correct answers when they ask similar questions in the future.

![](<Base64-Image-Removed>)

Power BI recognises two types of synonyms: **approved synonyms** and **suggestions**:

*   **Approved synonyms** either come directly from the names of fields themselves or are explicitly added by the author. When you use an approved synonym in your Q&A input, it will be treated just as though you used the name of the field and the association will be presented with high confidence, signified by a solid blue underline

*   **Suggested terms** are words Power BI thinks are likely to refer to their corresponding name. They come from a variety of sources – synonyms from the Office thesaurus show up by default, but you can also connect to your organisation’s collection of approved terms and add those to your suggestions as well. Suggestions will still be used by Q&A, but with lower priority than approved synonyms, and the lower confidence will be signalled in the results with a dotted orange underline. In the Q&A setup menu, suggestions may be added to the approved synonyms list or removed entirely.

![](<Base64-Image-Removed>)

Managing synonyms is therefore an important part of improving the quality of the Q&A experience. However, coming up with synonyms for every data entity in your model can be mentally laborious and physically time-consuming. Copilot for Power BI streamlines this process by generating some for you.

If you have Copilot enabled, there are a few ways for you to get suggestions from Copilot. However, before you being you will have to enable the feature in Power BI Desktop in **File -> Options -> Preview features -> Improve Q&A with Copilot**.

Then, you might be prompted to add synonyms with Copilot via a banner that shows up the first time you make a Q&A visual or open the Q&A setup menu:

![](<Base64-Image-Removed>)

You’ll also be able to get Copilot suggested synonyms via the Q&A setup menu. You can turn on Copilot as a source in the suggestion settings menu in the Synonyms tab, then click ‘apply to get synonyms’. Alternatively, if Copilot is already enabled as a source, you can click the Refresh button next to the suggestion settings dropdown.

![](<Base64-Image-Removed>)

After you have entered / received these suggestions, you might be prompted to review them. You’ll find the new synonyms in the Suggestions column in the synonyms page of the Q&A setup menu:

![](<Base64-Image-Removed>)

Copilot-suggested synonyms will function just like any other suggested synonyms. This means that they may be used by Q&A as a fallback when trying to determine what data fields a natural language input may refer to. You should carefully review them in the Suggestions column of the Q&A visual, remove the synonyms which are inaccurate and approve the ones which best fit the data.

Please keep in mind that as Microsoft scales out Copilot, you might run into throttling, which may cause Copilot to return incomplete results if you send too many requests in a short period of time. If that happens, you should wait a while and try again. Copilot may also not return results for terms for which it cannot generate synonyms or when its results are deemed inappropriate by Microsoft’s content filter. That fxxxing sxxxs.

In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses/)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-suggested-synonyms-from-copilot/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-suggested-synonyms-from-copilot/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-suggested-synonyms-from-copilot/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-suggested-synonyms-from-copilot/#0)

[](https://sumproduct.com/blog/power-bi-blog-suggested-synonyms-from-copilot/#0 "close")

top