# ADM Group 26
## Homework 5 - Visit the Wikipedia hyperlinks graph!

### Group Members:
 * Jason Tsardanidis
 * Mattias Basso
 * Massimiliano Riposati

In this assignment we perform an analysis of the Wikipedia Hyperlink graph. In particular, given extra information about the categories to which an article belongs to, we are curious to rank the articles according to some criteria. 

<div style="text-align:center"><img src ="https://cryptobriefing.com/wp-content/uploads/2018/04/Wikipedia-and-Request-Network-enable-donors-to-donate-in-cryptocurrency.jpg" /></div>

**categories that has a number of articles greater than 3500.**

## General notes

You will notice that one article might belong to a single category or multiple ones. In the case it belongs to more than one:

* If the article belongs to the input category (we will talk about this in RQ2) it belongs to that one.
* Otherwise, the category of the article will correspond, among the categories it belongs to, to the closest to the input category.


## Research questions

<div style="text-align:center"><img src ="http://allywebs.com/images/social_networking.png" /></div>

**[RQ1]** Build the graph <img src="https://latex.codecogs.com/gif.latex?G=(V,&space;E)" title="G=(V, E)" />, where *V* is the set of articles and *E* the hyperlinks among them, and provide its basic information:
 
- If it is direct or not                             
> G is directed Graph:  True
- The number of nodes                                
>number of nodes:  461193
- The number of edges                                
> number of edges:  2645247
- The average node degree.                           
> Average in-node/predecessors degree:  5.7357
> Average out-node/successors degree:  5.7357
						     
- Is the graph dense?                                
> The graph density is:  1.2436602635647606e-05
> NOT very dense


**[RQ2]** Given a category <img src="https://latex.codecogs.com/gif.latex?C_0&space;=&space;\{article_1,&space;article_2,&space;\dots&space;\}" title="C_0 = \{article_1, article_2, \dots \}" /> as input we want to rank all of the nodes in *V* according to the following criteria:
	
## Links
For completeness, here are the <b>nbviewer</b> links of the main code and the map:
 
 <ul>
  <li type="circle">http://nbviewer.jupyter.org/github/maxriposati/ADM-HW5/blob/master/Homework_05.ipynb</li>
 </ul>





