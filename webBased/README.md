# A web-based  dataset editor

<ol>
  <li>Correct Spelling of word</li>
  <li>Correct some tag that the model tagged wrong.</li>
  <li>You'll have an option to save it in the server or download the file.</li>
</ol>

## How it works:
#### Uploading
<ol>
  <li>Upload a .txt of .csv file.</li>
  <li>Server will save the filename in the database and file in server directory.</li>
  <li>It will then read the file line-by-line.</li>
  <li>Each line read, it will go through a UDF tokenizer and send the tokenized text to the model created and effectively tagged all the words.</li>
  <li>It will then create an html element to be rendered in the frontend.</li>
</ol>

#### Saving
<ol>
  <li>Retrieve all the element where the new word and tag are.</li>
  <li>Store all the word-tag in a JSON format.</li>
  <li>Send the JSON data to the server.</li>
  <li>Itterate over the data and overwrite the file with the new data.</li>
</ol>

#### Downloading
<ol>
  <li>Retrieve all the element where the new word and tag are.</li>
  <li>Store all the word-tag in a string format.</li>
  <li>Create a new blob object containing all the data and as a csv.</li>
  <li>Download Data.</li>
</ol>
