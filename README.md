# ADM Group 26
## Homework 5 - Visit the Wikipedia hyperlinks graph!

### Group Members:
 * Jason Tsardanidis
 * Mattias Basso
 * Massimiliano Riposati

In this assignment we perform an analysis of the Wikipedia Hyperlink graph. In particular, given extra information about the categories to which an article belongs to, we are curious to rank the articles according to some criteria. 

<div style="text-align:center"><img src ="https://cryptobriefing.com/wp-content/uploads/2018/04/Wikipedia-and-Request-Network-enable-donors-to-donate-in-cryptocurrency.jpg" /></div>

## Dataset

1.  For the task we use this reduced Dataset [Wikicat hyperlink graph](https://drive.google.com/file/d/1ghPJ4g6XMCUDFQ2JPqAVveLyytG8gBfL/view?usp=sharing).  
2.  From [this](https://snap.stanford.edu/data/wiki-topcats.html) page we download:
	-  `wiki-topcats-categories.txt.gz`
	-  `wiki-topcats-page-names.txt.gz`


## Research questions

<div style="text-align:center"><img src ="http://www.societygov.org/wp-content/uploads/2017/07/network-1911678_1920-copia.jpg" /></div>

**[RQ1]** Build the graph <img src="https://latex.codecogs.com/gif.latex?G=(V,&space;E)" title="G=(V, E)" />, where *V* is the set of articles and *E* the hyperlinks among them, and provide its basic information:
 
- If it is direct or not                             
- The number of nodes                                
- The number of edges                                
- The average node degree.			     
- Is the graph dense?                                


**[RQ2]** Given a category <img src="https://latex.codecogs.com/gif.latex?C_0&space;=&space;\{article_1,&space;article_2,&space;\dots&space;\}" title="C_0 = \{article_1, article_2, \dots \}" /> as input we want to rank all of the nodes in *V* according to the following criteria:

## Content
This repository contains:

  <ul>
  	<li type="circle">The main <code>Homework_05.ipynb</code> code</li>
  	<li type="circle">The <code>functions_hw5.py</code> function file that we need in the main code.</li>
  </ul>
  
## Links
For completeness, here are the <b>nbviewer</b> link of the main code:
 
 <ul>
 	<li type="circle">http://nbviewer.jupyter.org/github/maxriposati/ADM-HW5/blob/master/Homework_05.ipynb</li>
 </ul>



