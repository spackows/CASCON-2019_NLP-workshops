
# Instructions: CASCON 2019 NLP workshop - replay 2020

## Part 1
A great way to learn about the basic concepts and terms related to IBM Watson Natural Language Understanding is to explore the demo app: [https://natural-language-understanding-demo.ng.bluemix.net](https://natural-language-understanding-demo.ng.bluemix.net)

In the demo app, you can explore:
- **Sentiment** - positive/negative
- **Emotion** - joy, anger, disgust, sadness, fear
- **Keywords** - list important words
- **Entities** - "type" of keywords - eg. Location, Quantity, Sport
- **Categories** - hierarchical taxonomy - eg. arts & entertainment &rarr; books &rarr; poetry
- **Concepts** - phrases that indicate what the text is about
- **Syntax** - part of speech - eg. verb, adjective
- **Semantic roles** - subject, action, object

See: [Text analytics features](https://cloud.ibm.com/apidocs/natural-language-understanding#text-analytics-features)

<img src="../images/demo-app.png" alt="NLU demo app" width="60%"/>

<p>&nbsp;</p>


### Part 2
Create a project in Watson Studio from the sample project.

<ol>
<!-- step -->
<li>
<p>Download this sample project to your local computer:<br/>
<a href="./CASCON-replay-project.zip">CASCON-replay-project.zip</a></p>
</li>
<!-- step -->
<li>
<p>In Watson Studio, create an empty project:</p>
<ol>
<li>Give the project a name</li>
<li>If you don't already have Cloud Object Storage set up, follow the prompts to create an instance of Cloud Object Storage for the project</li>
<li>Click <b>Create</b></li>
</ol>
</li>
<!-- step -->
<li>
<p>Add the sample notebook to your project:</p>
<ol>
<li>On the <i>Assets</i> page in your Watson Studio project, click <b>Add to project</b></li>
<li>Select <b>Notebook</b></li>
<li>Select <b>From URL</b></li>
<li>Name the notebook (eg. "Analyzing customer messages")</li>
<li>Paste this URL in the <b>Notebook URL</b> text box: <a href="https://raw.githubusercontent.com/spackows/CASCON-2019_NLP-workshops/master/2020-replay/CASCON-replay-nb.ipynb">Notebook URL</a><br/><i><b>Note:</b> Right-click and select "Copy Link Location"</i> ^^</li>
<li>Click <b>Create Notebook</b></li>
</ol>
</li>
</ol>

<img src="../images/proj.png" alt="Creating a project from a file" width="60%"/>

<p>&nbsp;</p>


### Part 3

Analyze customer questions and comments in the notebook.

<ol>
<!-- step -->
<li>
<p>On the <b>Assets</b> page of your project, open the notebook in edit mode by clicking the pencil ( <img src="../images/pencil.png" /> ) beside the notebook</p>
</li>
<!-- step -->
<li>
<p>Run the <code>code</code> cells in the notebook <b>in order, starting at the top</b>.</p>
</li>
</ol>

<img src="../images/replay-notebook-image.png" alt="Notebook" width="90%"/>

<p>&nbsp;</p>

