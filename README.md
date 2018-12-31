# Portfolio Demo - GAE - Flask
## Description
This is a demonstration of deploying a website on Google Cloud Platform using multiple frameworks: Flask framework Jquery and languages: Python, HTML, CSS, JavaScript.

## Features
* Static rendering:
  * 3 Pages: Profile, Project, Contact.
  * Image preview tooltip when the mouse is hovering on an image.
  * Auto generate content from XML format.
  * Loading HTML fragment template using Jquery
* Blog

## Demonstration:
You can find a demonstration link from [here](https://portfolio-227204.appspot.com/)
* Main page: ![photo](https://github.com/jimmyvo2410/RrcNews/blob/master/doc/doc_Main.JPG)
* Edit page: ![photo](https://github.com/jimmyvo2410/RrcNews/blob/master/doc/doc_Edit.JPG)
* Login page: ![photo](https://github.com/jimmyvo2410/RrcNews/blob/master/doc/doc_Login.JPG)
* Full-post page: ![photo](https://github.com/jimmyvo2410/RrcNews/blob/master/doc/doc_Full.JPG)


## Deployment Instruction
### Prerequisites
 * Download and install the latest version of Pycharm: [Download](https://www.jetbrains.com/pycharm/) 
 * Create a new GCP project and App Engine application using the GCP Consoles
 * It is optional to download and install the Cloud SDK, or you can complete the following instruction with the GCP's Shell and editor 
 
### Deploy locally using Pycharm
 * Open Pycharm 
   * Open New Project
   * Navigate to [BlogsDemo](https://github.com/jimmyvo2410/Portfolio-GCP-Flask) folder
 * Configure Interpreter
   * In Pycharm, select File > Settings.. 
   * In Settings, on the left pannel, select Project:BlogsDemo > Project Interpreter. Navigate to [env/Scripts/python.exe](https://github.com/jimmyvo2410/Portfolio-GCP-Flask/blob/master/env/Scripts/python.exe)  

### Deploy on Google Cloud Platform
 * Open Cloud Shell
 * Create Demo folder on the Cloud Shell Editor
 * Copy the list of items to Demo folder:
    * [src/static](https://github.com/jimmyvo2410/Portfolio-GCP-Flask/tree/master/src/static)
    * [src/templates](https://github.com/jimmyvo2410/Portfolio-GCP-Flask/tree/master/src/templates)
    * [src/app.yaml](https://github.com/jimmyvo2410/Portfolio-GCP-Flask/blob/master/src/app.yaml)
    * [src/appengine_config.py](https://github.com/jimmyvo2410/Portfolio-GCP-Flask/blob/master/src/appengine_config.py)
    * [src/main.py](https://github.com/jimmyvo2410/Portfolio-GCP-Flask/blob/master/src/main.py)
    * [src/requirements.txt](https://github.com/jimmyvo2410/Portfolio-GCP-Flask/blob/master/src/requirements.txt)
 * On Cloud Shell Terminal
    * Navigate to Demo folder:
        ```
        cd Demo
        ```
    * Initialize Google App Engine
        ```
        gcloud app create 
        ```
        Select server by inputting the associated number.
    * Setup virtual environment
        ```
        virtualenv --python python env
        ```
    * Install required library
        ```
        pip install -t lib -r requirements.txt
        ```
    * Active Python
        ```
        . env/bin/activate
        ```
        ```
    * Finally, Upload files to Google Cloud Storage
        ```
        gcloud app deploy --quiet
        ```
    
# How to modify static content?
The websites is coded in the way that you can easily modify the content by:
* Edit xml files from [here](https://github.com/jimmyvo2410/Portfolio-GCP-Flask/tree/master/src/static/xml "xml folder")
* Update your photos in this [folder](https://github.com/jimmyvo2410/Portfolio-GCP-Flask/tree/master/src/static/images/thumb "photo folder") 
* Put your resume in this [folder](https://github.com/jimmyvo2410/Portfolio-GCP-Flask/tree/master/src/static/file "photo folder") 
