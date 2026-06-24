<h1>WeChat Backend</h1>

<h2>1. Application Name: WeChat</h2>
<h2>2. Description</h2>
<p>
WeChat is a modern AI-powered chat application built with React and Vite, designed to deliver an intuitive and interactive user experience. The application enables users to explore predefined topics and ask questions in natural language. Leveraging advanced AI capabilities, it understands user queries and provides accurate, context-aware responses based on the selected topic, making information retrieval simple, efficient, and conversational.
</p>

<h3>Tech Stack</h3>
<ul>
    <li>FastAPI</li>
    <li>MongoDB</li>
    <li>Pinecone</li>
    <li>LangChain</li>
    <li>Gemini 2.5 Flash</li>
    <li>GoogleGenerativeAIEmbeddings</li>
    <li>Cloudinary</li>
</ul>

<h2>3. Installation & Run Steps</h2>

<h3>Create Virtual Environment</h3>
<pre>
python -m venv venv
</pre>

<h3>Activate Virtual Environment</h3>
<pre>
<b>Windows</b>
venv\Scripts\activate

<b>Linux</b>
source venv/bin/activate
</pre>

<h3>Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>Run Application</h3>
<pre>
uvicorn app.main:app --reload
</pre>

<h3>API Documentation</h3>
<pre>
http://localhost:8000/docs
</pre>

<h2>4. Application Screenshots</h2>

<h3>Landing Page</h3>
<img src="./App_screenshots/Home.png" alt="Landing Page Screenshot">

<br>

<h3>Admin page to add topics(enhancing RAG knowledge)</h3>
<img src="./App_screenshots/Admin.png" alt="Chat Interface Screenshot">
