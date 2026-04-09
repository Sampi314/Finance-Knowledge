# Circular Relationships: Humans versus financial models – Finexmod

**Source:** https://www.finexmod.com/circular-relationships-humans-versus-financial-models

---

[Skip to content](https://www.finexmod.com/circular-relationships-humans-versus-financial-models#content)

Circular Relationships: Humans versus financial models

Last week, I was invited to a podcast about financial modeling. The episode hasn’t been released yet. I’ll share it once it’s available. What I want to discuss here is inspired by my conversation during that podcast. I had a great time during the 45-minute discussion with the host; it was relaxed, and I could be myself without many filters. Reflecting on our conversation, I realized that we touched on a topic I have a deep history and passion for—circular references.

The host asked, “Circular reference or no circular reference?” I said I advocate for the “war on circular reference,” and we laughed! However, after that, I pondered over my stance. Do I genuinely have such a strong issue with circular references that I can declare war on them? I want to highlight that my concern with circular references only pertains to intentional ones. If a circular reference is unintentional and can be resolved by adjusting a link or using algebraic methods, then having that type of circular reference is an error rather than an issue. So, when asked if I have a problem with (intentional) circular references, my answer was: “No, I cannot declare war on circular references.” My interest in understanding how to handle circular references best led me to connect with Professor Edward Bodmer, who has developed methods and tools that enable modelers to address circular references confidently.

So, is a circular reference indeed a problem? The answer that came to mind was a resounding No! The issue is not circular references themselves; it’s how we handle them in our project finance models. To delve deeper, we must first define what constitutes a circular reference is. My friend Mike Flynn, a top-notch financial modeler, gave me this definition: “A circular reference occurs when two objects (or cells in Excel) depend on each other either directly or indirectly, creating a loop of dependencies. Comparing this type of relationship to human relationships, humans are the objects that contain the interrelated dependencies.” Check out Mike’s profile here: [Mike Linkedin profile](https://www.linkedin.com/in/mike-f-9517181b1/)

This brings us to the concept of a relationship. It’s intriguing to compare how we address circular references in our financial models with how we navigate human relationships.

In human interactions, circular relationships involve interdependence and connections, whether between partners, parents, siblings, or professionals. When things are going well, there’s no problem, and everything runs smoothly. However, when issues arise, the circular nature of the relationship becomes more apparent and requires attention.

Here, I’ve identified three typical models for how we humans approach and manage relationships:

Technique 1: The “Let It Be” Approach
-------------------------------------

This involves tolerating a less-than-ideal situation within the relationship. It’s important to note that tolerance isn’t the same as acceptance. Acceptance falls into the category of Technique 3. This approach isn’t particularly sustainable, as there comes a point where one or both parties can no longer bear the strain of tolerating the situation. Most of the time, this approach doesn’t lead to positive outcomes.

Technique 2: The “Cut It Off” Approach
--------------------------------------

The name says it all. This is when you opt to end the relationship, freezing memories of the person at a particular point in time and refusing to create new memories with them. However, the existing memories and history with the person remain. Occasionally, triggered by a song or a discussion, those memories resurface, and they might be painful until you “cut off” again.

Technique 3: Creating a Parallel World
--------------------------------------

This advanced technique isn’t suitable for everyone. It involves self-work and reaching a level of self-understanding where you no longer have relationship issues. You recognize that you’re responsible for your life and cultivate beliefs that grant you access to your inner world. This approach allows you to co-create with people rather than deal with them.

![](https://www.finexmod.com/wp-content/uploads/2023/08/Circular-human-relationships.png)

Similarly, we can apply these three techniques to the realm of project finance modeling:

Technique 1: The “Let It Be” Approach – Iterative Models
--------------------------------------------------------

Working with iterative spreadsheets renders them vulnerable to errors and significantly slows down the model’s performance, making it unsustainable.

Technique 2: The “Cut It Off” Approach – Copy and Paste
-------------------------------------------------------

This is a common solution adopted in the industry to date. It provides a quick fix by breaking circularity through copying and pasting the parameter causing the issue as values. This severs the relationship between parameters and freezes it in a single scenario. If any scenario changes, the copy-and-paste action needs to be repeated. However, this approach can disrupt the use of Excel’s built-in functions like Goalseek and Datatable, necessitating additional macros to perform these tasks. It also introduces performance issues, especially in complex project finance models.

Technique 3: Professor Edward Bodmer’s Parallel Model
-----------------------------------------------------

This method, developed by Professor Edward Bodmer, is the optimal solution. It effectively resolves circularity without negatively impacting the model’s functionality. With this approach, you reprogram the equations causing circular references in VBA, then employ this function within the Excel model. This technique not only enhances model flexibility and speed but also aids in debugging. This is because you program the same calculations twice: in Excel and VBA. Often, mistakes originate from Excel formulas rather than VBA code.

If you’re intrigued by the idea of delving into the realm of parallel worlds in financial modeling, I encourage you to visit Professor Edward Bodmer’s website at [edbodmer.com](https://edbodmer.com/)
. There, you can learn more about this technique. If you are eager to dive deeper into this innovative approach, please don’t hesitate to contact Professor Bodmer or me. We’re here to guide you through the nuances and assist you in developing a more comprehensive understanding.

![](https://www.finexmod.com/wp-content/uploads/2023/08/www.finexmod.com_-1.png "www.finexmod.com")

![](https://www.finexmod.com/wp-content/uploads/2023/08/www.finexmod.com-1.png "www.finexmod.com (1)")

[finexmod](https://www.finexmod.com/author/finexmod/ "Posts by finexmod")
2023-08-21T13:04:09+00:00August 21st, 2023|

#### Share This Story, Choose Your Platform!

[Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.finexmod.com%2Fcircular-relationships-humans-versus-financial-models%2F&t=Circular%20Relationships%3A%20Humans%20versus%20financial%20models "Facebook")
[X](https://x.com/intent/post?url=https%3A%2F%2Fwww.finexmod.com%2Fcircular-relationships-humans-versus-financial-models%2F&text=Circular%20Relationships%3A%20Humans%20versus%20financial%20models "X")
[Reddit](https://reddit.com/submit?url=https://www.finexmod.com/circular-relationships-humans-versus-financial-models/&title=Circular%20Relationships%3A%20Humans%20versus%20financial%20models "Reddit")
[LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.finexmod.com%2Fcircular-relationships-humans-versus-financial-models%2F&title=Circular%20Relationships%3A%20Humans%20versus%20financial%20models&summary=Last%20week%2C%20I%20was%20invited%20to%20a%20podcast%20about%20financial%20modeling.%20The%20episode%20hasn%E2%80%99t%20been%20released%20yet.%20I%E2%80%99ll%20share%20it%20once%20it%E2%80%99s%20available.%20What%20I%20want%20to%20discuss%20here%20is%20inspired%20by%20my%20conversation%20during%20that%20podcast.%20I%20had%20a%20great%20time%20during%20the%2045-minute "LinkedIn")
[WhatsApp](https://api.whatsapp.com/send?text=https%3A%2F%2Fwww.finexmod.com%2Fcircular-relationships-humans-versus-financial-models%2F "WhatsApp")
[Tumblr](https://www.tumblr.com/share/link?url=https%3A%2F%2Fwww.finexmod.com%2Fcircular-relationships-humans-versus-financial-models%2F&name=Circular%20Relationships%3A%20Humans%20versus%20financial%20models&description=Last%20week%2C%20I%20was%20invited%20to%20a%20podcast%20about%20financial%20modeling.%20The%20episode%20hasn%E2%80%99t%20been%20released%20yet.%20I%E2%80%99ll%20share%20it%20once%20it%E2%80%99s%20available.%20What%20I%20want%20to%20discuss%20here%20is%20inspired%20by%20my%20conversation%20during%20that%20podcast.%20I%20had%20a%20great%20time%20during%20the%2045-minute%20discussion%20with%20the%20host%3B%20it%20was%20relaxed%2C%20and%20I%20could "Tumblr")
[Pinterest](https://pinterest.com/pin/create/button/?url=https%3A%2F%2Fwww.finexmod.com%2Fcircular-relationships-humans-versus-financial-models%2F&description=Last%20week%2C%20I%20was%20invited%20to%20a%20podcast%20about%20financial%20modeling.%20The%20episode%20hasn%E2%80%99t%20been%20released%20yet.%20I%E2%80%99ll%20share%20it%20once%20it%E2%80%99s%20available.%20What%20I%20want%20to%20discuss%20here%20is%20inspired%20by%20my%20conversation%20during%20that%20podcast.%20I%20had%20a%20great%20time%20during%20the%2045-minute%20discussion%20with%20the%20host%3B%20it%20was%20relaxed%2C%20and%20I%20could&media=https%3A%2F%2Fwww.finexmod.com%2Fwp-content%2Fuploads%2F2023%2F08%2FCircula-2.png "Pinterest")
[Vk](https://vk.com/share.php?url=https%3A%2F%2Fwww.finexmod.com%2Fcircular-relationships-humans-versus-financial-models%2F&title=Circular%20Relationships%3A%20Humans%20versus%20financial%20models&description=Last%20week%2C%20I%20was%20invited%20to%20a%20podcast%20about%20financial%20modeling.%20The%20episode%20hasn%E2%80%99t%20been%20released%20yet.%20I%E2%80%99ll%20share%20it%20once%20it%E2%80%99s%20available.%20What%20I%20want%20to%20discuss%20here%20is%20inspired%20by%20my%20conversation%20during%20that%20podcast.%20I%20had%20a%20great%20time%20during%20the%2045-minute%20discussion%20with%20the%20host%3B%20it%20was%20relaxed%2C%20and%20I%20could "Vk")
[Email](mailto:?body=https://www.finexmod.com/circular-relationships-humans-versus-financial-models/&subject=Circular%20Relationships%3A%20Humans%20versus%20financial%20models "Email")

Related Posts
-------------

![Using Macros in your financial models: Quick tips](https://www.finexmod.com/wp-content/uploads/2025/07/Cover-Learning-VBA-500x383@2x.png)

[](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/)

#### [Using Macros in your financial models: Quick tips](https://www.finexmod.com/using-macros-in-your-financial-models-quick-tips/ "Using Macros in your financial models: Quick tips")

July 3rd, 2025

![The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/circular-relationships-humans-versus-financial-models)

[](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/)

#### [The Art of Structuring Project Finance Models: A Personal Journey](https://www.finexmod.com/the-art-of-structuring-project-finance-models-a-personal-journey/ "The Art of Structuring Project Finance Models: A Personal Journey")

April 10th, 2025

![Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/wp-content/uploads/2024/04/Comic-Sans-Blog-Banner-500x383@2x.png)

[](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/)

#### [Do Circular References Still Have Us Stuck on Copy-Paste?](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/ "Do Circular References Still Have Us Stuck on Copy-Paste?")

April 29th, 2024 | [0 Comments](https://www.finexmod.com/do-circular-references-still-have-us-stuck-on-copy-paste-time-to-retire-the-copy-paste-habit/#respond)

[Page load link](https://www.finexmod.com/circular-relationships-humans-versus-financial-models#)

[Go to Top](https://www.finexmod.com/circular-relationships-humans-versus-financial-models#)