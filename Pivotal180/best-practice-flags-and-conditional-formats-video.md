# Best Practice: Flags and Conditional Formats in Financial Models

**Source:** https://pivotal180.com/best-practice-flags-and-conditional-formats-video

---

[Skip to content](https://pivotal180.com/best-practice-flags-and-conditional-formats-video/#fl-main-content)

Best Practice: Flags and Conditional Formats in Financial Models
================================================================

By Haydn Palliser | December 6, 2019

### Overview

This lesson on Flags and Conditional Formats is an extract from our pre-course videos for our [**Renewable Energy and Infrastructure Project Finance Modeling**](https://pivotal180.com/course-type/renewable-energy-project-finance-modeling/)
 course.

### Video

**Video Transcript** 

**Haydn:** Three things fundamentally changed and improved my financial modeling skills. They’re the absolute must-knows for any analyst, and I have to share them. The first one was sensitivities and scenarios, which we cover throughout the course. The second is control accounts, something new to record volumes of items over time, and we will cover that shortly. The third, and the topic of this lesson, is something called **binary flags**.

Good try, Dan, but not that type of flag. In this lesson, we’re going to learn what flags are, their use within a financial model, and how to create them. These flags are one of the most important items to learn as a financial modeler. You’ll get to do these many, many times throughout the course.

When to use Flags & Conditional Formats
---------------------------------------

Let’s start by recognizing there are many situations in financial modeling that are binary in nature. This is when something occurs only during a limited set of circumstances, i.e. if something happens, or within a specific duration of time. And in the context of that, it’s useful to remember that multiplying by zero will always yield a zero result.

Flags & Conditional Formats Example
-----------------------------------

Let’s say I have a set of revenues for five years of $100 and expenses of $60. So my EBITDA is 100 minus 60 equals 40. But even though I show five years of cash-flows, these cash-flows are only meant to last for three years. So I need to build a single formula that is consistent across the whole row. But I need to make the values in year four and five zero.

Broadly speaking in plain English, or at least plain kiwi English, if we are past year three, our values must be zero. IF being the clue. We can use an if statement.

But rather than apply an if statement separately to both the revenue and the expense line, I’m gonna do something just a little bit different. I can say, if the year is greater than three, give me a zero result, otherwise a one. I’m creating a result that’s binary. It doesn’t matter what the year is, it’s result can only be a one or a zero. Returning a one result in years one to three, and a zero result in years four and five.

I’ve added this if statement calculation directly above the revenue line in green. And given multiplying by zero results in zero, if I multiply the revenue and expense line by this if formula, this set of ones and zeros, the financial projection would be cut off after year three and my values in year four and five are equal to zero.

### What is a Binary Flag in Excel?

So what have I done? I’ve effectively replaced an if statement in both the revenue line and the expense line with a single binary if statement, and then multiplied that if statement line by revenue and expenses. This reduces the number of if statements in my model, replacing them instead with a simple multiplication. The formulas are therefore easier to review and, as such, there’s arguably less risk in my model. This one zero if statement is called a **binary flag**.

And before we go a step further, let’s recognize the different types of binary results that can live within a financial model.

### Types of binary results in Excel

Within a project life cycle, we can either be in construction or operations. Or we may have both historic and future cash-flows in our model, and they don’t occur at the same stage. They are binary. Either you’re in a future period, or you’re not. You could be in a period before or after our loan is repaid, compared to the period within which you’re actually repaying your loan. Finally, perhaps we are in compliance of our loan covenants or we’re not. We’re either breaching it or not.

### The power of visual representations

Knowing that flag simplified formula is certainly helpful, but the real power of flags is in its visual representation. By replacing the green bar from earlier, we can format a flag to show more clearly when the project or business was operating. With this formatting and row label saying Operating Period, the model tells me a story that I need to know, being cash-flows should stop past year three.

Can you see how a binary flag with a one or a zero result can really help the user understand a model? I can’t live without these now. They show me all of the items in a model that occur in a specific time-frame or that occurred due to a specific event.

**Dan:** Hey, I really liked what you did there, but how did you make that beautiful formatting? I’ve total fear of missing out. I want to learn how to do that too.

**Haydn:** Great question, Dan. How do I create this formatting? First of all, the format needs to change based on the results of my if statement. It should be green with a white-colored one or a light grey with a dash if the value is zero. We could use conditional formatting in Excel to create this. We’ll create many flags during this course so let me demonstrate just this one.

How to create Flags & Conditional Formats
-----------------------------------------

Welcome into Excel. Here we’re going to create our flags and the beautiful format you saw a short while ago using the same example.

Our inputs are clearly separated from our calculations, and our flag is shown on row 11. The calculation is the same, just saying that if the current year is greater than three years, then make the value zero, otherwise one. The revenue and the expenses simply take the input value times the flag, so we can see in year four and five the values become zero.

So how do I create this format across row 11? First, I highlight them, and what we’ve done is we’ve created a style called Flags. I navigate across to [**Cell Styles**](https://pivotal180.com/best-practice-styles-in-financial-modeling-video/)
 and select Flag. What this does is it adds a gray shading to the cells, and it’s changed the color of the font to gray. And it’s also make the zeroes to dash, which we here at Pivotal180 like because it makes it clear and easy to see for the user. This hasn’t, though, created the automatic formatting of green, where you would require. So I highlight this whole row and again I go back up to Home, into Condition Formatting, and New Rule.

We’ll learn some of other formatting rules later. For now, we’re going to select “Format only cells that contain”. And what we want to do is format the cells that are equal to one. We want to make the cells that equal to one green. So now I’ve selected cell value is equal to one, I select what format I want to see if the value is one.

### Using cell styles for Flags & Conditional Formats

I’m going to start by making the font white. So, the Font menu, I select white. I’m going to add a border by selecting Outline and I’m going to add a Fill itself. Our standard color for flags is not a standard color of Excel, so we select More Colors, Custom. I’m going to type in what’s called the RGB into the section. So 78, 172 and 150. And now you can see the green color down here. I can press OK. I select OK, I’ve done all the formatting I want to see when the value is one, and I’m going to press OK.

You now see my cells had popped out as green, and you can now probably see why we made the ones white. It makes it clear to the user that there’s a value of one in those cells. Again, what is great about this is I can clearly see when my project is in operations and directly beneath it I see all of my calculations related to that timing. You can’t get any clearer than that.

Benefits of Flags & Conditional Formats
---------------------------------------

The main benefit of flags is that they show you what to expect. They also make you aware of something. For example, “Have I breached the covenant?”, or, “Is my loans still outstanding?” The visual representation is really powerful.

Flags may also simplify your formula, as you can multiply many things by a single flag instead of writing an if statement on many lines.

And it really boils down to one thing. At Pivotal180, we’ve a single rule we like to use. When you have something that is only meant to happen over a specified time-frame, create a flag before you do any other calculations. Just seeing when something occurs is a really helpful starting point before you tackle the problem.

Now you have an overview of flags. You are ready to see the full benefits throughout the rest of the course.

#### Share This Resource

[](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fpivotal180.com%2Fbest-practice-flags-and-conditional-formats-video%2F)

[](https://twitter.com/share?url=https%3A%2F%2Fpivotal180.com%2Fbest-practice-flags-and-conditional-formats-video%2F)

[](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Fpivotal180.com%2Fbest-practice-flags-and-conditional-formats-video%2F)

[](https://pivotal180.com/cdn-cgi/l/email-protection#310e535e55480c59454541421402701403771403774158475e45505d0009011f525e5c140377535442451c41435052455852541c575d5056421c505f551c525e5f555845585e5f505d1c575e435c5045421c475855545e140377)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)

### Haydn Palliser

[https://www.linkedin.com/in/haydnpalliser/](https://www.linkedin.com/in/haydnpalliser/)

Complexity simplified.
----------------------

Advisory, financial modeling, and training courses within climate change, sustainable finance, renewable energy, and infrastructure.  
We don’t just teach you how to build models. We teach you how to do deals.

[VIEW ALL OF OUR COURSES](https://pivotal180.com/all-courses/)

[ENQUIRE ABOUT OUR SERVICES](https://pivotal180.com/contact-us/#form)

[Scroll To Top](https://pivotal180.com/best-practice-flags-and-conditional-formats-video/#)

### Download Free Brochure

Fill out the form to download your brochure now.

"\*" indicates required fields

First Name\*

Last Name\*

Email\*

CAPTCHA