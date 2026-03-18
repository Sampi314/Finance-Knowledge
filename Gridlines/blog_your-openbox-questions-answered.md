# Your Openbox questions answered - Gridlines

**Source:** https://www.gridlines.com/blog/your-openbox-questions-answered

---

[Skip to content](https://www.gridlines.com/blog/your-openbox-questions-answered#content)

Your Openbox questions answered
===============================

*   May 20, 2020

Well, that was quite a week!

Watching Kenny doing the Openbox demo on Wednesday ranks among the most stressful things I’ve ever done. I’m sure it was pretty high pressure for him too! But we were fully prepared, well practised, and it all worked on the day.

Thank you to everyone who attended, or watched the webinar via YouTube.

There were lots of good questions asked during the webinar and we felt they deserved some detailed answers.

This blog is my attempt to deal with the main question themes that came through.  

If you didn’t get to see the live demo, please do watch it below.

![swatch 3](https://www.gridlines.com/wp-content/uploads/2024/05/swatch-3.jpeg "Your Openbox questions answered 1")

So, to the questions. They fell into three main categories: standards, model size & complexity, and components. There were also a couple more, which didn’t fit neatly into any category. They are as follows:

**Standards**
-------------

### **Does Openbox adhere to the** **FAST standard?**

The model Kenny produced was designed to the FAST standard. We think that’s a great standard, and it’s the one we use in-house. It’s not the only one though and our intention is that Openbox should be able to produce models to any well-codified standard.

### **Is the ICAEW Financial Modelling Code an alternative?**

Someone mentioned the ICAEW financial modelling standard, and we’re also fans of that one. Ultimately, we see Openbox as being able to produce models to any standard. It can already produce non-FAST models – you just untick the box that says “Produce model to FAST”. Once you do that, you get models that don’t follow FAST,  but one that is still compliant with the ICAEW standard – calculations only referring to cells above or to the left, and so on. It does the same job (and the same calculations) but just laid out differently.

**Model size/ complexity**
--------------------------

### **Does Openbox run fully in memory/ Are there memory limitations when building ‘large’ models?**

A few people asked if there are limitations on the size of models that Openbox can produce, either because of memory or for some other reason. We did an experiment once to test this out, to see how large a model Openbox could produce on my standard desktop. The largest we got to was nearly 500MB. It took nearly an hour to appear, but it did open (slowly!). Not suggesting that anyone does that for a real project, but it does show that Openbox can comfortably handle models in the 10-50MB range that we often find ourselves in.

### **How would Openbox fare for more complicated projects/ industries and in terms of providing scenario analyses?**

Well, we’ve spent the last few months trying to add as many of those as possible. We can do some fairly complex things, such as having multiple timelines in the model and detecting and fixing circular references. Input scenarios are added out of the box and adding things like Monte Carlo analysis (coming soon!) to switch between single point and distributions as inputs. In the end, even if Openbox can’t (yet) do something, you always have the option to produce most of the model in Openbox and implement the last 5% in Excel the regular way.

**Components/ templates**
-------------------------

### **Presumably, the initial models come with Openbox?** **How do you add a module for reuse or edit the modules that come with Openbox?**

We’ve focused on Openbox for project finance in the first instance and we’re developing components for that sector. We see part of the value proposition of Openbox as the continual development and release of reusable components, and yes it is easy to edit the supplied components. We foresee a “marketplace” of components that other people can license to Openbox users.  

### **Does Openbox have the ability to import from excel – for example, the income statement data?**

Yes. You can either design it in Openbox itself (just type the formulas you want), or you can read in some formulas from Excel and create a component from those. So if you already have a model that does some useful standard calculations for your industry, you can quickly read them in and store them in Openbox.

### **Can we customize the templates to specific situations/ transactions (LBO, Private placement, 3 statement modelling)?**

Yes. Our approach here is one of openness and trusting modellers. Every project is different and often you need to just tweak that standard approach you always use. The flexibility of Excel is one of the best things about it and we want to continue that within Openbox.

### **You have used the project finance model template in your working example – have you built templates for various types of business, or would it generally be a bespoke template when requested?**

We have to be careful with the word template. When we talk about templates we mean a model skeleton with some financial statements, a few basic standard calculations, and lots of placeholders. Components are little groups of calculations that do a specific job – e.g. calculate debt and interest for senior debt. We are looking to build a range of components for different sectors.  

### **What sectors have library pre-built templates?**

Currently, we are developing templates for the Project Finance sector. We expect to expand this in due course. If you work in an industry where you feel that a template would help to improve your user experience, then please do get in contact with us and join the beta tester programme.

**Any other questions**
-----------------------

### **How do you apply conversions?** **For example, production may be in tonnage but the price of production for revenue is in lb, oz etc. Do you have a conversion box for inputs in Openbox or do you use the CONVERT formula in Excel?**

Openbox will support the CONVERT function, so you can include that in your models. It also, as part of the checks it does on all models, makes sure that your units are consistent. So if, for example, you try to add something in US$ to something in EUR, without applying an exchange rate, it will warn you.

### **How important is creating a flexible dashboard in driving insights for a financial model?**

Effective data visualisation is very important. Slick, easy, powerful dashboards are on our development roadmap. We’re thinking about how to make the design process easy enough that you can produce them quickly, but also powerful enough to produce good-looking dashboards straight out of the box. This might make it to version 1.0 (depending on how other things go!) but even if it’s not there, it will be included soon.

Well that feels like quite a lot to write for a blog, so if you got this far, well done. I hope it has answered the questions you have, and given you an idea of our approach and where we are. If there are things which I haven’t covered and that you would like to hear more about, do please get in touch! Applications for the first round of the beta testing are now closed.

Share:

*   [](https://uk.linkedin.com/company/gridlines-com)
    

More Posts

[![Mobile phone with a live chat display, showing conversations between a human and chat bot](https://www.gridlines.com/wp-content/uploads/chatbot-news-300x169.jpg)](https://www.gridlines.com/blog/how-google-taught-bard-to-doubt-itself/)

[How Google taught Bard to doubt itself](https://www.gridlines.com/blog/how-google-taught-bard-to-doubt-itself/)

“Knowledge is the antidote to fear” – Ralph Waldo Emerson Welcome to the new look Miscellany. If you have modelling-related

[![A person working on a laptop examining budget spreadsheets and graphs](https://www.gridlines.com/wp-content/uploads/2024/05/A-person-working-on-a-laptop-examining-budget-spreadsheets-and-graphs-300x169.png)](https://www.gridlines.com/blog/financial-modelling-examples/)

[Financial Modelling Examples: An Overview of Key Model Types](https://www.gridlines.com/blog/financial-modelling-examples/)

Across industries and scenarios, we use different financial modelling examples to analyse specific aspects of financial data and transactions. It

[![Spring budget 2024](https://www.gridlines.com/wp-content/uploads/Spring-budget-2024-300x169.jpg)](https://www.gridlines.com/blog/uk-spring-budget-2024/)

[What does the UK 2024 Spring Budget mean for tax?](https://www.gridlines.com/blog/uk-spring-budget-2024/)

The UK Chancellor, Jeremy Hunt, delivered his Spring Budget on the 6th of March 2024. Although the Chancellor’s focus was on cutting

[![financial audit modelling](https://www.gridlines.com/wp-content/uploads/financial-audit-modelling-300x169.jpg)](https://www.gridlines.com/blog/cut-the-cost-of-your-financial-model-audit-expert-tips-you-need-to-know/)

[Cut the cost of your financial model audit: expert tips you need to know](https://www.gridlines.com/blog/cut-the-cost-of-your-financial-model-audit-expert-tips-you-need-to-know/)

A financial model audit is often a formal due diligence requirement of investors in major infrastructure transactions. It is an

[PreviousOpenbox closed beta](https://www.gridlines.com/blog/openbox-closed-beta/)

[NextOpenbox dev diary – Private Beta week 1](https://www.gridlines.com/blog/openbox-dev-diary-week-1/)

Tell us about your project
--------------------------

[![Akram Mostafa](<Base64-Image-Removed>)](mailto:akram.mostafa@gridlines.com)

Akram Mostafa
-------------

Associate Director

akram.mostafa@gridlines.com

[![](<Base64-Image-Removed>)](mailto:morag.loader@gridlines.com)

Morag Loader
------------

Director of Accounting & Tax

morag.loader@gridlines.com