# ChatGPT Final Fiday Fix Explanation

**Source:** https://sumproduct.com/blog/chatgpt-final-fiday-fix-explanation/

---

[Home](https://sumproduct.com/)

\> ChatGPT Final Fiday Fix Explanation

*   January 31, 2024

ChatGPT Final Fiday Fix Explanation
===================================

ChatGPT Final Fiday Fix Explanation
===================================

1 February 2024

On the final Friday of each month, we release a blog series called the “Final Friday Fix” where we set an Excel / Power Pivot / Power Query / Power BI problem for users to solve over the weekend. This month, we decided to experiment by creating the Final Friday Fix and its corresponding Monday Morning Mulling using the new ‘GPTs’ feature in ChatGPT. Here is how we did it and how we also reflect on how well it went.

**_What are GPTs?_**

Generative Pre-trained Transformers (GPTs) are custom AI chatbots that are built to perform specific tasks. Essentially, they are a type of artificial intelligence (AI) language model.

It is important to note for anyone wishing to follow along, GPTs may only be used with the premium ChatGPT service, **GPT+**. One of the major issues with ChatGPT is that it traditionally struggles to deal with specialised tasks as it is built for general knowledge. GPTs allow you to implement specific instructions with a custom knowledge base and even actions such as calling external Application Programming Interfaces (APIs) (an API is a bridge that allows ChatGPT to interact with other software, but more on this later).

Additionally, it allows the image generation, web browsing and code interpreter features to run alongside and interact with these instructions for additional versatility. Most importantly for us, GPTs are community made and are simple to create even for someone with no prior coding experience.

**_Creating a GPT_**

Now, we will run you through how we created the GPT. It starts by opening up ChatGPT and going to the ‘**Explore GPTs**‘ tab.

![](<Base64-Image-Removed>)

From here, clicking ‘Create” in the top right corner will bring us to the GPT Editor.

![](<Base64-Image-Removed>)

This is where you create GPTs. The ‘Create’ tab allows you to interact with ChatGPT as you build, with ChatGPT helping build the GPT with your specifications. The ‘Preview’ pane on the right allows you to test the GPT as you make changes. As we wanted more control, we selected the ‘Configure’ tab instead. This tab contains various options allowing us to edit the GPT directly.

![](<Base64-Image-Removed>)

Here, we started by filling in some details. We named it ‘FFF Generator’ and gave it the description “Creates Final Friday Fixes and Monday Morning Mullings”. The instructions are the most important part of the GPT, as they provide the guide for how it will function. We used the following instructions:

**You job is to create blogs for our website. We have two styles of blog: Final Friday Fix and Monday Morning Mulling. The FFF poses an excel challenge for readers on the last Friday of every month. The MMM provides the answer. You job is to generate new Friday Fixes and Monday Mullings based on previous examples in your knowledge base. The problem should only involve one question.**

It first describes its basic task, then explains a little context behind what the blogs are. Finally, we added a clarifier that we only want one \[1\] question per blog to keep it a bit simpler as it was initially producing convoluted, multistage questions. Despite the typos, the GPT is able to decipher these instructions (it’s very accommodating of our fat fingers!). Next is the ‘Conversation starters’ box which provides prompt suggestions for the user of the GPT. Conversation starters are important when designing a GPT for other people as it gives the user an idea of the capabilities of the GPT. We used conversation starters like:

*   **“Generate a Final Friday Fix for me”**
*   **“Generate a sample data set for the following Excel problem using code interpreter”.**

![](<Base64-Image-Removed>)

The next step is to bring the brains into the GPT. We have a folder full of FFFs and MMMs from previous months and we uploaded these to the GPT to function as its “knowledge base”. You may upload all sorts of information to the knowledge base to customise the GPT such as instructions, sample text and even Excel spreadsheets. Depending upon your instructions it will either base its responses on the content or interact with the content to generate results (such as using code interpreter to interact with the data). We may upload the files by clicking the ‘Upload files’ button and selecting the files we wish to use.

![](<Base64-Image-Removed>)

Once those were uploaded there were a few more things we needed to adjust. Under ‘Capabilities’ there are three \[3\] check boxes for ‘Web Browsing’, ‘DALL.E Image Generation’ and ‘Code Interpreter’, which allow the GPT to use those tools. Since GPTs are meant to perform a specific task you may not want the GPT to have access to all of them. In this case, we needed the Code Interpreter to be available so it could generate Excel Spreadsheets, but the other two were not needed.

The ‘Actions’ button takes us to the window below, allowing the user to code custom Actions that allow the GPT to access and interact with external APIs. APIs allow ChatGPT to interact with other software whether they are interacting with external databases or using other software tools. You can even get assistance in building actions through the ‘ActionsGPT’. Actions are incredibly powerful, although we didn’t require them for this GPT.

![](<Base64-Image-Removed>)

The final step is to put in a profile picture for the GPT. While we could upload our own image, we can very easily use the ChatGPT image generator by going back over into the ‘Create’ tab and asking it to create one.

![](<Base64-Image-Removed>)

Once the GPT was set up we could test it in the Preview tab. Let’s try one of the conversation starters from earlier:

**Generate a Final Friday Fix for me**

![](<Base64-Image-Removed>)

If the GPT is working how we want it, then we just click the ‘Save’ button in the top right corner and publish it. The GPT can be published just for yourself or for anyone with a link or to the public.

Now that the GPT is set up, we may utilise it by returning to the Explore GPTs page and go into ‘My GPTs’. One of the great things about ChatGPT is that we may ask it for an idea as many times as we want and it will produce a new idea every time. Since we wanted this for the end of January, we asked it to

**Generate a summer themed Final Friday Fix.**

We ran this quite a few times and it produced a variety of responses running into two key issues. The first was that many of the problems that it produced were too simple, such as the one below:

![](<Base64-Image-Removed>)

The second issue was that when it did produce more complicated questions it ran into another problem. Along with creating the Final Friday Fix, we used the GPT to create the solution and establish a Monday Morning Mulling. When the GPT created more complicated examples it did struggle to produce good answers or just came up with the inefficient, brute force answers we pride ourselves on avoiding here at SumProduct. Eventually, it produced an answer that we thought, whilst a little simple, was reasonable enough to work.

![](<Base64-Image-Removed>)

From here, we asked it to generate an Excel file of sample data to use for the problem, which is why the Excel file wasn’t in our usual style. Did you notice? It was able to generate what a spreadsheet of sample data for us, but there were limitations.

Since it is using Python to interact with the spreadsheet it cannot interact with non-sheet features such as Conditional Formatting and Data Validation. It is also poor at building formulae and should be mainly used to populate a sheet with numbers. Once the sheet was created, we were able to adjust it to better suit the question by including more data along with at least one oversubscribed class for the problem.

An interesting note here: While we were building this example we couldn’t remember the word oversubscribed. A very cool trait of ChatGPT is that it can understand made up words based on context and content so we used the word oversigned instead to represent to the fact that the sign-up sheet would have too many names signed up. Isn’t it cool that ChatGPT was able to understand this completely made-up word and generate what we asked from it.

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Next, we let ChatGPT create a Monday Morning Mulling to pair with the Final Friday Fix. We needed to make sure the solution worked and it did take one iteration to get a correct solution (always check!).

![](<Base64-Image-Removed>)

Once we had this, the final step was to go through and check that everything was formatted how we wanted it. While the GPT performed well at creating the article there were some issues. For example, we have a specific way of opening and closing the articles and while it did something similar, we adjusted it to what we use. Additionally, ChatGPT does not appear to work well with dates. Due to being based in the United States, the GPT set the date as August as that is summertime in the northern hemisphere. We also made minor grammatical adjustments along with adding a few pictures.

So how useful is this actually as a tool and how good was the output it provided? Many of you would have noticed that the problem wasn’t as interesting as usual and that’s due to the GPTs problem solving limitations. Additionally, the solution that it came up with doesn’t exactly fit into the criteria it layed out itself. Notably it required more than 1 formula to do it. However, all things considered it does a remarkable job at mimicking the style of the Final Friday Fixes. This makes sense, as ChatGPT is a Large Language Model. It’s built for producing Language, not for solving coding problems (though it is reasonable at that).

For this article, we let ChatGPT do most of the work but realistically, these tools are at their best when used with human input, working off each other. That could be with the SumProduct team coming up with problems and solutions and having it write out the article based upon that idea or getting it to help brainstorm complex problems for us to find the solutions to, or even just having it edit work articles we’ve already written. Considering the small amount of input we had in creating the article, we believe it remains impressive what it was able to produce.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/chatgpt-final-fiday-fix-explanation/#0)
    
*   [Register](https://sumproduct.com/blog/chatgpt-final-fiday-fix-explanation/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/chatgpt-final-fiday-fix-explanation/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/chatgpt-final-fiday-fix-explanation/#0)

[](https://sumproduct.com/blog/chatgpt-final-fiday-fix-explanation/#0 "close")

top