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
- The number of nodes
- The number of edges 
- The average node degree. Is the graph dense?

**[RQ2]** Given a category <img src="https://latex.codecogs.com/gif.latex?C_0&space;=&space;\{article_1,&space;article_2,&space;\dots&space;\}" title="C_0 = \{article_1, article_2, \dots \}" /> as input we want to rank all of the nodes in *V* according to the following criteria:
	
* Obtain a *block-ranking*, where the blocks are represented by the categories. In particular, we want:


<img src="https://latex.codecogs.com/gif.latex?block_{RANKING}&space;=\begin{bmatrix}&space;C_0&space;\\&space;C_1&space;\\&space;\dots&space;\\&space;C_c\\&space;\end{bmatrix}" title="block_{RANKING} =\begin{bmatrix} C_0 \\ C_1 \\ \dots \\ C_c\\ \end{bmatrix}" />
	
Each category <img src="https://latex.codecogs.com/gif.latex?C_i"/> corresponds to a list of nodes. 

The first category of the rank, <img src="https://latex.codecogs.com/gif.latex?C_0" title="C_0" />, always corresponds to the input category. The order of the remaining categories is given by:

<img src="https://latex.codecogs.com/gif.latex?$$distance(C_0,&space;C_i)&space;=&space;median(ShortestPath(C_0,&space;C_i))$$" title="distance(C_0, C_i) = median(ShortestPath(C_0, C_i))" />

The lower is the distance from <img src="https://latex.codecogs.com/gif.latex?C_0" title="C_0" />, the higher is the <img src="https://latex.codecogs.com/gif.latex?C_i" title="C_i" /> position in the rank. <img src="https://latex.codecogs.com/gif.latex?ShortestPath(C_0,&space;C_i)" title="ShortestPath(C_0, C_i)" /> is the set of all the possible shortest paths between the nodes of <img src="https://latex.codecogs.com/gif.latex?C_0" title="C_0" />  and <img src="https://latex.codecogs.com/gif.latex?C_i" title="C_i" />. Moreover, the length of a path is given by the sum of the weights of the edges it is composed by.


* Once you obtain the <img src="https://latex.codecogs.com/gif.latex?block_{RANKING}" title="block_{RANKING}" /> vector, you want to sort the nodes in each category. The way you should sort them is explained by this example:

	*	Suppose the categories order, given from the previous point, is <img src="https://latex.codecogs.com/gif.latex?C_0,&space;C_1,&space;C_2" title="C_0, C_1, C_2" />


__[STEP1]__ Compute subgraph induced by <img src="https://latex.codecogs.com/gif.latex?C_0" title="C_0" />. For each node compute the sum of the weigths of the in-edges.

 <img src="https://latex.codecogs.com/gif.latex?score_{article_i}&space;=&space;\sum_{i&space;\in&space;in-edges}&space;w_i" title="score_{article_i} = \sum_{j \in in-edges(article_i)} w_j" />

__[STEP2]__ Extend the graph to the nodes that belong to <img src="https://latex.codecogs.com/gif.latex?C_1" title="C_1" />. Thus, for each article in <img src="https://latex.codecogs.com/gif.latex?C_1" title="C_1" /> compute the score as before. __Note__ that the in-edges coming from the previous category, <img src="https://latex.codecogs.com/gif.latex?C_0" title="C_0" />, have as weights the score of the node that sends the edge.


__[STEP3]__ Repeat Step2 up to the last category of the ranking. In the last step of the example you clearly see the weight update of the edge coming from node *E*.


# Submitting the homework

Homework 5 is due on [23rd December 2018 - 23:59:59](http://aris.me/index.php/data-mining-ds-2018). 

The content of the repository is up to you. The mandatory files are:

* `README.md`:
* `Homework_5.ipynb`:

create [here](http://nbviewer.jupyter.org/) just copying and paste the url of your notebook on GitHub.

It __must not__ contain:

* The datasets you used (thus you should clearly state in the readme what dataset you used, if any not in the homework description).
