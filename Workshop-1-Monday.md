# NLP Hands-on Workshop Series Session 1

**Extracting meaning from text using a notebook in Watson Studio**

## Section A
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

<img src="images/demo-app.png" alt="NLU demo app" width="60%"/>

<p>&nbsp;</p>


### Section B
Create a project in Watson Studio from the sample project.

<ol>
<!-- step -->
<li>
<p>Download this sample project to your local computer:<br/>
<a href="https://github.com/spackows/CASCON-2019_NLP-workshops/raw/master/sample-projects/CASCON-2019-NLP-Workshop-1-Monday.zip">CASCON-2019-NLP-Workshop-1-Monday.zip</a></p>
</li>
<!-- step -->
<li>
<p>In Watson Studio, create a new project "from a sample or file":</p>
<ol>
<li>Upload the sample project .zip file</li>
<li>Give the project a name</li>
<li>If you don't already have Cloud Object Storage set up, follow the prompts to create an instance of Cloud Object Storage for the project</li>
<li>Click <b>Create</b></li>
</ol>
</li>
</ol>

<img src="images/proj.png" alt="Creating a project from a file" width="60%"/>

Demo video:<br/>
[Create project from sample](https://youtu.be/UWGZPVKFk1o)

<p>&nbsp;</p>


### Section C

Analyze customer questions and comments in the first notebook.

<ol>
<!-- step -->
<li>
<p>On the <b>Assets</b> page of your project, open the notebook named "1-Explore-NLU" in edit mode by clicking the pencil ( <img src="images/pencil.png" /> ) beside the notebook</p>
</li>
<!-- step -->
<li>
<p>In the notebook, add the NLU service apikey:</p>
<ol>
<li>From the <b>Services</b> menu in Watson Studio, right-click "Watson Services" and then open the link in a new browser tab</li>
<li>In the new Watson services tab, from the <b>Action</b> menu beside the Natural Language Understanding instance, select "Manage in IBM Cloud"</li>
<li>In the service details page that opens, click <b>Service credentials</b>, then expand credentials to view them, and then copy the apikey</li>
</ol>
</li>
<!-- step -->
<li>
<p>Run the <code>code</code> cells in the notebook <b>in order, starting at the top</b>.</p>
<ol>
<li>Explore text analytics features with a sample test message</li>
<li>Import sample customer messages</li>
<li>Analyze sample customer messages - keywords and semantic roles</li>
</ol>
</li>
</ol>

<img src="images/notebook.png" alt="Notebook" width="90%"/>

<p>&nbsp;</p>


### Section D
Visualize analysis results in the second notebook.

<ol>
<!-- step -->
<li>
<p>On the <b>Assets</b> page of your project, open the notebook named "2-Visualize-NLU-results" in edit mode by clicking the pencil ( <img src="images/pencil.png" /> ) beside the notebook</p>
</li>
<!-- step -->
<li>
<p>Run the <code>code</code> cells in the notebook <b>in order, starting at the top.</p>
<ol>
<li>Create word clouds</li>
<li>Create bar charts</li>
</ol>
</li>
</ol>

<img src="images/keywords-word-cloud.png" alt="Visualize NLU analysis" width="60%"/>

<p>&nbsp;</p>

