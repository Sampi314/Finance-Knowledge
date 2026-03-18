# Openbox | A matter of perspective - Gridlines

**Source:** https://www.gridlines.com/blog/openbox-a-matter-of-perspective

---

[Skip to content](https://www.gridlines.com/blog/openbox-a-matter-of-perspective#content)

Openbox | A matter of perspective
=================================

*   October 12, 2022

When we started building Openbox, we thought we were building a tool to create spreadsheet models. But as anyone who has started a business will tell you, customers and the market have a way of surprising you with what they really want! And one thing they want is help understanding what their model is doing. Or even better, what someone else’s model is doing. I’ve discussed that in a [previous blog](https://www.gridlines.com/blog/ofwat-builds-its-official-price-control-model-using-openbox/)
 too.

Why can’t they just look at the spreadsheet to work out what it’s doing? Spreadsheets are great for examining the local detail of a model – what’s happening in one cell and the cells near it that you can see on one screen. But very soon, you are scrolling up hundreds of rows and flipping between sheets just to go from a calculation to (say) the inputs it depends on.

And here’s the thing: whenever you show someone a model, and the output of a model, they always ask a question like _“Why did that IRR change from 12% to 11%”? Or “What exactly is included in operating costs?”_.

Those questions should be easier to answer than they are. Yes, you can use the little blue tracer arrows, and step back through the model using Ctrl+\[. But you quickly get lost because you can only see one step at a time, and you need to remember how you got there.\
\
Our approach is to show what our friend Hjalmar from [grid.is](http://www.grid.is/)\
 called the “dependency graph” in his [“building a spreadsheet engine from scratch”](https://medium.grid.is/we-built-a-spreadsheet-engine-from-scratch-heres-what-we-learned-e4800ab9edf1)\
 article.\
\
**Use a map to avoid getting lost**\
\
In simple terms, a dependency graph is a map of the model. It has a box for each calculation item in the model and arrows between the boxes. An arrow to one box from another one shows that the first box/ calculation depends on the second box/ calculation. In Excel jargon, the arrows show precedents and dependents.\
\
![Openbox flags](https://www.gridlines.com/wp-content/uploads/2024/05/Pic-1.png "Openbox | A matter of perspective 1")\
\
With this map, you can keep track of where you have come from, and see big chunks of the model all at once.\
\
The problem is, as Hjalmar pointed out, that a dependency graph can _“…get very complicated very fast…”_. Financial models are complex – that’s part of what we get paid to deal with, as financial modeling professionals. But if you show the whole model as a graph (and we’ve tried, believe me), it is overwhelming and unreadable.\
\
**Step by step**\
\
So what did we do? First of all, we challenged the assumption that you need to show the whole model. Our experience is that people like the idea of seeing the whole model on a single screen, but for any serious model, it is too much information to take in. They instinctively pick one part to focus on first.\
\
Our solution is to show the graph one step at a time. Start with a single calculation and its immediate precedents and dependents. Let the user add layers, one at a time, not adding more until they’re happy they’ve understood what’s there already. Let them hide parts that are not interesting, or that they are no longer interested in.\
\
It’s a bit like when you use Google Maps to plan a journey. It doesn’t show you the whole world, with a tiny line representing your best route. It zooms in on the route – the part you care about – and you can then choose to zoom out if you want to.\
\
![Openbox screenshot](<Base64-Image-Removed>)\
\
If you do this, then in most cases, you’ll find that there really aren’t that many steps from input to result. You go from looking at a model with thousands of calculations to focusing on just a handful.\
\
**Laying it out**\
\
But even a model that is displayed step by step can be hard to read unless you are very careful about how you lay it out. People like to have things flow in one direction from inputs to outputs. For me, it’s left to right. And they don’t like to have lots of arrows that cross one another.\
\
There also turns out to be a concept that we might call “level”. This is basically how many steps it takes to go from a particular item to the outputs. We’ve found that it is much easier to read the model if everything at the same level is shown in a column on the screen. For example, outputs should be shown on a column on the right of the screen, and then everything that is an immediate precedent of the outputs should be shown one column to the left.\
\
Of course, it is not quite as simple as that!\
\
Suppose for example you have a fixed assets calculation in your model, and a depreciation calculation. Fixed assets depend on depreciation, so depreciation should be to the left of fixed assets. But depreciation also depends on fixed assets, so depreciation should be to the right…\
\
Or maybe a calculation is two steps away from an output, if you follow one path, and three steps away if you follow another path. Where should it go then?\
\
There’s no perfect solution, so the layout approach we use tries to strike a balance. We have been very strict about the ‘left to right’ rule. And we try to avoid arrows crossing one another. Sometimes, there’s no right answer to which ‘layer’ a calculation should be in.\
\
If you’d like to judge how successful we’ve been, you can try it out in the [latest version of Openbox here](http://www.openboxmodels.com/download-openbox)\
.\
\
**Moving it around**\
\
The next challenge is that the instant you add or remove boxes/ calculations from the graph, you change what a good layout is. Where should the new boxes go? How should the new arrows be drawn so they don’t cross existing ones? Which existing boxes should be moved to make space for the new one? Do we need to revisit any decisions about which ‘level’ each item should be at?\
\
Basically, you need to redraw at least some of the graph. And if you’re not careful, that can take a long time. We needed to ensure that each box is as quick to draw as possible and that we don’t try to redraw things that don’t need to be redrawn.\
\
One trick here is ‘caching’ – we work out what a calculation should be linked to, and then store that rather than working it out again. Unless we have to – if for example its formula or the formula of its dependents change. Excel does much the same. If you change an input in Excel, it recalculates the rest of the model, but only those parts that depend on the changed input.\
\
**Show me the numbers**\
\
Finally, a dependency graph can be a little…well… abstract. Yes, you know the three drivers of revenue. But which one matters most for the scenario you are looking at?\
\
One of the great things about spreadsheets is that they let you see the numbers, which gives you a real sense of whether the model is doing what it should be and what’s important.\
\
So show the numbers on the graph, right? Not so fast. Just like when we discussed showing part of the map and not the whole, the best approach is to show the user as little as possible but to be ready to show them more detail if they want.\
\
And that’s the approach we’ve taken here. The graph doesn’t show the numbers, but Openbox will display a spreadsheet beside it that does, and that moves around as you move around the graph. You can also draw an instant chart beside any item, by clicking F11.\
\
![Openbox dashboard](<Base64-Image-Removed>)\
\
In effect, you have a totally customisable dashboard, which lets you drill down into any calculation as far as you like.\
\
**What’s next**\
\
The new Super Focus mode was created to help people find their way around financial models. But we have big plans for making it even better. Ways to improve navigation by only showing the most relevant items, and greying out the others. Ways to have it display the changes between two scenarios, so you can see visually exactly why that change in an input affected the result. And many more.\
\
If you’d like to be involved in deciding what these next steps should be, [please get in touch](https://www.gridlines.com/contact-us/)\
!\
\
Share:\
\
*   [](https://uk.linkedin.com/company/gridlines-com)\
    \
\
More Posts\
\
[![Man in a meeting looking towards another team member](https://www.gridlines.com/wp-content/uploads/Fixed-pos-300x169.png)](https://www.gridlines.com/blog/financial-model-audit-secrets-of-pricing-2/)\
\
[Financial Model Audit – Secrets of Pricing](https://www.gridlines.com/blog/financial-model-audit-secrets-of-pricing-2/)\
\
At Gridlines, we are all about transparency. This starts with how we build our models, which we strive to make\
\
[![A person working on a laptop examining budget spreadsheets and graphs](https://www.gridlines.com/wp-content/uploads/2024/05/A-person-working-on-a-laptop-examining-budget-spreadsheets-and-graphs-300x169.png)](https://www.gridlines.com/blog/financial-modelling-examples/)\
\
[Financial Modelling Examples: An Overview of Key Model Types](https://www.gridlines.com/blog/financial-modelling-examples/)\
\
Across industries and scenarios, we use different financial modelling examples to analyse specific aspects of financial data and transactions. It\
\
[![Spring budget 2024](https://www.gridlines.com/wp-content/uploads/Spring-budget-2024-300x169.jpg)](https://www.gridlines.com/blog/uk-spring-budget-2024/)\
\
[What does the UK 2024 Spring Budget mean for tax?](https://www.gridlines.com/blog/uk-spring-budget-2024/)\
\
The UK Chancellor, Jeremy Hunt, delivered his Spring Budget on the 6th of March 2024. Although the Chancellor’s focus was on cutting\
\
[![Man working on an electronic visual display](https://www.gridlines.com/wp-content/uploads/business-analysis-lifecycle-300x169.jpg)](https://www.gridlines.com/blog/why-its-difficult-to-implement-a-standard-approach-across-a-modelling-team/)\
\
[Why implementing a financial modelling standard is hard](https://www.gridlines.com/blog/why-its-difficult-to-implement-a-standard-approach-across-a-modelling-team/)\
\
Standards in Modelling Standards in modelling have been discussed at length for many years. For this blog, we’re not interested\
\
[PreviousThe UK Mini-budget](https://www.gridlines.com/blog/the-uk-mini-budget/)\
\
[NextAn Update on the UK Mini-budget](https://www.gridlines.com/blog/an-update-on-the-uk-mini-budget/)\
\
Tell us about your project\
--------------------------\
\
[![Akram Mostafa](<Base64-Image-Removed>)](mailto:akram.mostafa@gridlines.com)\
\
Akram Mostafa\
-------------\
\
Associate Director\
\
akram.mostafa@gridlines.com\
\
[![](<Base64-Image-Removed>)](mailto:morag.loader@gridlines.com)\
\
Morag Loader\
------------\
\
Director of Accounting & Tax\
\
morag.loader@gridlines.com