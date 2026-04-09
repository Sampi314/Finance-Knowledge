# Biomass and Biogas Analysis

**Source:** https://edbodmer.com/biomass-and-biogas-analysis

---

This page discusses biomass and biogas project finance and biomass project finance models. When structuring biomass analysis, you will generally have to take something that has not much value such as waste wood and then turn it into some kind of energy. This means you will end up making a lot of conversions and you may need some kind of equipment to turn the raw stuff into something that can be used to make energy for transportation or electricity. As many of us do not have an engineering background, I will walk through some really basic stuff on how to go to google and get conversion factors and then put those into your financial model. I will also give you some ideas about how to present your model so users can clearly see risks in the models. I start with presenting a couple of older models and then address two projects in more detail.

### General Conversions

Here is the rule. When google says 1 meter = 100 cm, you put the cm at the top and then make a conversion factor with units of cm/meter in excel. Whenever you have something in meters, you can convert to cm through multiplying by the cm/meter constant of 100. This is a very simplified example, but the same idea applies to the other conversion factors.

![](https://edbodmer.com/wp-content/uploads/2021/03/image-78.png)

It would be kind of silly, but in your model you would look and see that 1 is for the meter and 100 is for the cm. So you would put cm/meter in your model as below. If you have something in the model in meters, let’s say 500 meters, then you could see that meter x cm/meter = cm = 50,000. Just cross multiply and divide and make the effort to put in the converstions.

Unit Amount

Conversion cm/meter 100

![](https://edbodmer.com/wp-content/uploads/2021/03/image-77.png)

In the example above, put the m3 at the top and in the units column make

Unit Amount

Conversion m3/MMBTU 28.264

So, if you have prices in USD/MMBTU of 5.0 and you have the units being produced of natural gas in m3 — say 100 m3 — then you look at the unit and see that you cannot multiply m3 by the factor but you must divided it. So the value of the natural gas is 100/28.264 x 5 = 3.538. This kind of thing is very common in biomass models.

Classic Risk Analysis in Biomass
--------------------------------

Biomass projects can appear relatively safe compared to other projects. You can offset construction risk with EPC contracts (although the EPC contractor may want a big premium for locking in the price). Similarly you can get an O&M contract. Finally, you can store the biomass fuel in inventory and seem to have less resource risk than other renewable projects. You can even arrange a contract with the farmer, wood producer, palm leaf provider etc. to hedge the price. It seems that you have mitigated all of the risks and you can even make a diagram of this. In terms of the cow dung example, below the price for received depends on the supply and demand for particular types of fuel.

But the classic problem is demonstrated by what happened to biomass projects in Austria and California. The source of fuel originally had a negative price. It was waste. It even had contracts. But once the provider of the fuel such as waste wood understands that his stuff has value, the fuel provider wants a higher price. Even if there is a contract with a farmer, he or she does not care about the contract any more. With the increase in the cost of the input, the cash flow of the biomass diminishes.

### Rotting Palm Oil Leaves into Compressed Natural Gas

The picture below is of a covered lagoon. This type of lagoon can be used to store piles of crap. Eventually after you put stuff in here, biogas can be produced and it can be converted to natural gas.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-6.png)

a project that takes palm oil leaves, puts them in a pile and covers the pile so that they rot and produce gas — called biogas. This gas is then converted to compressed natural gas with a refining type machine called an upgrader.

I have made a similar file for using biomass to compute methane and then use the methane as fuel for trucks. This case is a representative case of using palm oil fruit bunches an putting them in a lagoon. The lagoon produces biogas which can be refined in an upgrader and converted to methane. Finally the methane must be dispensed to be used as replacement for diesel fuel. Both of these cases have a lot of conversions and as I am a bit slow and not an engineer, I insist on being very explicit about how the conversions are made.

![](https://edbodmer.com/wp-content/uploads/2020/08/image-46.png)

### Cow Dung into Natural Gas

In converting cow manure into Methane, you need to store the source and then allow it to biodegrade so it produces gas. Then you can move it into an upgrader that purifies the biogas into methane.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-7.png)

![](https://edbodmer.com/wp-content/uploads/2021/03/image-73.png)

![](https://edbodmer.com/wp-content/uploads/2021/04/image-8.png)

The second project is illustrated in the diagram below.

![](https://edbodmer.com/wp-content/uploads/2021/04/image-9.png)

![](https://edbodmer.com/wp-content/uploads/2021/03/image-72.png)

As with any project analysis, you can start with the analysis of the physical volumes produced and the capacity of machines to accomplish the production. The production is illustrated on the screenshot below. Note first that there are a lot of conversions.

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=13389&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=11176&rand=0.4612162321501725)