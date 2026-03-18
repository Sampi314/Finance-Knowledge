# Power BI Blog: Editing Linguistic Relationships in Q&A Setup

**Source:** https://sumproduct.com/blog/power-bi-blog-editing-linguistic-relationships-in-qa-setup/

---

[Home](https://sumproduct.com/)

\> Power BI Blog: Editing Linguistic Relationships in Q&A Setup

*   October 4, 2023

Power BI Blog: Editing Linguistic Relationships in Q&A Setup
============================================================

Power BI Blog: Editing Linguistic Relationships in Q&A Setup
============================================================

5 October 2023

_Welcome back to this week’s edition of the Power BI blog series. This week, we look at how to edit linguistic relationships. Who needs a marriage counsellor..?_

The Q&A visual is an effective way to help users further understand their data by asking questions and receiving answers in the form of visuals. It offers users a way to explore their data in ways not covered by the rest of the report without requiring deeper knowledge of their data model or report authoring.

![](<Base64-Image-Removed>)

However, while the Q&A engine is good at answering precise questions about data, it may not be able to associate every word or phrase a user inputs with data in the model. For example, answering “what are our best consoles this year?” may require connecting the term “consoles” to the name “products” in the model, and understanding that the term best corresponds to the highest sales values. These terms are contextual. However, users could mean something completely different by asking for “console” and “best” in other industries, organisations or even datasets.

To help authors ensure that the Q&A visual provides consistent and accurate answers based upon the unique language their report consumers actually use, Microsoft introduced Q&A setup tools with an emphasis on providing Q&A with synonyms for column and table names in the model. This way, authors can explicitly define console as referring to products and users will always receive the correct answers when they ask similar questions in the future.

However, synonyms (nouns) are only half of the picture. The other half of the terms (adjectives, verbs, prepositions, adverbs) can’t be defined with such straightforward mappings because they must be understood as a part of a phrase: they qualify other terms or relate other terms together. The word “best” in the above previous example is one; asking “who sold the most books” requires us to know that stores sell books, connecting stores to books.

There are many types of these linguistic relationships, so Microsoft has built a new tab entirely to help you create and manage linguistic relationships for your data. You can get into the Q&A setup menu using the gear icon on the Q&A visual or the Q&A setup option in the Modeling tab of the Ribbon, then selecting the new Relationships tab.

![](<Base64-Image-Removed>)

There, you’ll be able to define a variety of relationships, including verb, adjective, noun, preposition, and more. You should choose a type which fits the term you’re trying to define (_e.g._ “best” is an adjective), then follow the prompts to define what it means in the context of your data.

Microsoft states that their investment into Q&A does not stop with this. Natural language capabilities are increasingly driven by large language models. Therefore, there is value in the precision, consistency, and customisability of the Q&A engine. Further, defining synonyms and relationships can be a lengthy process just asking to be streamlined with the power of AI-generated suggestions. Watch this space.

That’s it for this week. In the meantime, please remember we offer training in Power BI which you can find out more about [here](https://www.sumproduct.com/courses)
. If you wish to catch up on past articles, you can find all of our past Power BI blogs [here](https://www.sumproduct.com/thought/power-bi-tips-blog-series)
.

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-bi-blog-editing-linguistic-relationships-in-qa-setup/#0)
    
*   [Register](https://sumproduct.com/blog/power-bi-blog-editing-linguistic-relationships-in-qa-setup/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-bi-blog-editing-linguistic-relationships-in-qa-setup/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-bi-blog-editing-linguistic-relationships-in-qa-setup/#0)

[](https://sumproduct.com/blog/power-bi-blog-editing-linguistic-relationships-in-qa-setup/#0 "close")

top