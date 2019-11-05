# NLP Hands-on Workshop Series - Session 2

**Creating a custom language model to optimize NLP results**

Tuesday, November 5 | 10:45 - 12:15 | Holly & Butternut

<p>&nbsp;</p>


### Section A
\[Do this section in IBM Watson Knowledge Studio]

Open the Knowledge Studio web GUI, then create an <b>entities and relations</b> workspace:

<ol>
<li>Click <b>create an entities and relations workspace</b></li>
<li>Assign the workspace a name and finish</li>
</ol>

#### &rarr; A.1 Define entities
Define the types of word we care about (_entities_) and supply some examples of those words (_dictionaries_).

<ol>
<!-- step -->
<li><p>On the <b>Entity Types</b> page, add the following entity types:</p>
<ul>
<li>action</li>
<li>docs</li>
<li>obj</li>
<li>persona</li>
<li>tech</li>
</ul>
<p>Do not edit the Roles or Subtypes.</p>
</li>
<!-- Step -->
<li><p>On the <b>Dictionaries</b> page:</p>
<ol>
<li>Download each of these dictionaries to your local computer, then upload them to Watson Knowledge Studio:
<ul>
<li><a href="https://github.com/spackows/CASCON-2019_NLP-workshops/blob/master/custom-language-model/dictionaries/action.csv"><code>actions.csv</code></a></li>
<li><a href="https://github.com/spackows/CASCON-2019_NLP-workshops/blob/master/custom-language-model/dictionaries/docs.csv"><code>docs.csv</code></a></li>
<li><a href="https://github.com/spackows/CASCON-2019_NLP-workshops/blob/master/custom-language-model/dictionaries/obj.csv"><code>obj.csv</code></a></li>
<li><a href="https://github.com/spackows/CASCON-2019_NLP-workshops/blob/master/custom-language-model/dictionaries/persona.csv"><code>persona.csv</code></a></li>
<li><a href="https://github.com/spackows/CASCON-2019_NLP-workshops/blob/master/custom-language-model/dictionaries/tech.csv"><code>tech.csv</code></a></li>
</ul></li>
<li>For each dictionary, select the dictionary and associate the dictionary with the entity type of the same name</li>
</ol>
<p><b>Note:</b> You have to upload the dictionaries one at a time by selecting <b>Upload Dictionary</b> from the menu.</p>
</li>
</ol>

#### &rarr; A.2 Provide sample customer messages
On the <b>Documents</b> page:
<ol>
<li><p>Download this document set to your local computer: <a href="https://github.com/spackows/CASCON-2019_NLP-workshops/blob/master/custom-language-model/document-set/customer-messages-documents.zip">customer-messages-documents.zip</a></p>
<p><b>Note:</b> Uncompress the .zip file into individual .txt files on your local computer</p></li>
<li>In Watson Knowledge Studio, click <b>Import Document Set</b> and then upload the 18 .txt files you downloaded in the prerequisites</li>
<li>Rename the document set "Document set 1"</li>
</ol>

<b>Note:</b> Do not upload the .zip file itself.  Upload the 18 .txt files in one upload action as a set.

#### &rarr; A.3 Process files & train model
<ol>
<!-- Step -->
<li><p>On the <b>Pre-annotation</b> page (under the <b>Machine Learning Model</b> menu  item):</p>
<ol>
<li>Click <b>Apply This Pre-annotator</b></li>
<li>When prompted, select "Document set 1" and then click <b>Run</b></li>
</ol>
</li>
<!-- Step -->
<li><p>On the <b>Performance</b> page:</p>
<ol>
<!-- <li>Click <b>Train and evaluate</b></li> -->
<li>Select all documents, and then click <b>Train and evaluate</b></li>
</ol>
</li>
</ol>

#### &rarr; A.4 Deploy model
<p>On the <b>Versions</b> page:</p>
<ol>
<li>Click <b>Create version</b></li>
<li>Deploy the snapshot version you just created to your IBM Watson Natural Language Understanding service instance
<p><b>Note</b>: If you cannot find your NLU service instance in <b>Spaces</b> try looking in <b>Resource groups</b>.</p></li>
</ol>

<img src="images/dictionaries-03.png" alt="Creating a custom model" width="60%"/>
  
<p>&nbsp;</p>


### Section B
\[Do this section in IBM Watson Studio]

Create a project in Watson Studio from the sample project.

<ol>
<!-- step -->
<li>
<p>Download this sample project to your local computer:<br/>
<a href="https://github.com/spackows/CASCON-2019_NLP-workshops/raw/master/sample-projects/CASCON-2019-NLP-Workshop-2-Tuesday.zip">CASCON-2019-NLP-Workshop-2-Tuesday.zip</a></p>
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

**Demo video**<br/>
[Create project from sample](https://youtu.be/UWGZPVKFk1o)

<p>&nbsp;</p>


### Section C
Analyze customer questions and comments a notebook.

<ol>
<!-- step -->
<li>
<p>On the <b>Assets</b> page of your project, open the notebook named "3-Custom-language-model" in edit mode by clicking the pencil ( <img src="images/pencil.png" /> ) beside the notebook</p>
</li>
<ol>
<!-- step -->
<li>
<p>Add the NLU service apikey:</p>
<ol>
<li>From the <b>Services</b> menu in Watson Studio, right-click "Watson Services" and then open the link in a new browser tab</li>
<li>In the new Watson services tab, from the <b>Action</b> menu beside the Natural Language Understanding instance, select "Manage in IBM Cloud"</li>
<li>In the service details page that opens, click <b>Service credentials</b>, then expand credentials to view them, and then copy the apikey</li>
</ol>
</li>
<!-- step -->
<li>
<p>Specify the custom model ID:</p>
<ol>
<li>On the <b>Versions</b> page in your Knowledge Studio workspace, expand the <b>Deployed Models</b> list</li>
<li>Copy the <b>Model ID</b></li>
</ol>
</li>
<!-- step -->
<li>
<p>Run the <code>code</code> cells in the notebook <b>in order, starting at the top</b>.</p>
<ol>
<li>Import sample customer messages</li>
<li>Analyze sample customer messages: default model & custom model</li>
</ol>
</li>
</ol>

<img src="images/notebook.png" alt="Notebook" width="90%"/>

<p>&nbsp;</p>


### Section D
Normalize results.

<ol>
<!-- step -->
<li>
<p>On the <b>Assets</b> page of your project, open the notebook named "4-Normalize-custom-model-results" in edit mode by clicking the pencil ( <img src="images/pencil.png" /> ) beside the notebook</p>
</li>
<!-- step -->
<li>
<p>Run the <code>code</code> cells in the notebook <b>in order, starting at the top.</p>
</li>
</ol>

<img src="images/normalized.png" alt="Normalizing results" width="60%"/>

<p>&nbsp;</p>


### Section E
Visualize normalized results.

<ol>
<!-- step -->
<li>
<p>On the <b>Assets</b> page of your project, open the notebook named "5-Visualize-custom-model-results" in edit mode by clicking the pencil ( <img src="images/pencil.png" /> ) beside the notebook</p>
</li>
<!-- step -->
<li>
<p>Run the <code>code</code> cells in the notebook <b>in order, starting at the top.</p>
</li>
</ol>

<img src="images/actions-compare.png" alt="Visualize normalized results" width="60%"/>

<p>&nbsp;</p>


### Bonus: Section F [Optional]
Cluster messages using extracted entities.

<ol>
<!-- step -->
<li>
<p>On the <b>Assets</b> page of your project, open the notebook named "5-Visualize-custom-model-results" in edit mode by clicking the pencil ( <img src="images/pencil.png" /> ) beside the notebook</p>
</li>
<!-- step -->
<li>
<p>Run the <code>code</code> cells in the notebook <b>in order, starting at the top.</p>
</li>
</ol>

<img src="images/cluster.png" alt="Visualize normalized results" width="300px"/>

<p>&nbsp;</p>

