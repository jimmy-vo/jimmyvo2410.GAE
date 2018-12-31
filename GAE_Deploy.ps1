
#configuration
$VERSION="20181230t012741"
$loc_project = "D:\Github\Portfolio-GCP-Flask"
$loc_tmp = "Deploy"
$loc_src_folders = @("static", "templates")
$loc_src_files = @("app.yaml", "appengine_config.py", "main.py", "requirements.txt")

#Project Path
cd $loc_project

#Remove folder if existing
Remove-Item -Recurse -Force -path $loc_tmp -ErrorAction SilentlyContinue

#Create folder
mkdir $loc_tmp 

#Copy files
for ($i=0; $i -lt $loc_src_files.length; $i++) {
    Copy-Item -Path $loc_src_files[$i] -Recurse -Destination $loc_tmp -Container
}

#Copy folders
for ($i=0; $i -lt $loc_src_folders.length; $i++) {
    $newFolder = $loc_tmp + "\" + $loc_src_folders[$i]
    Copy-Item -Path $loc_src_folders[$i] -Recurse -Destination $newFolder -Container
}

#go to folders
cd $loc_tmp

#setup virtual environment
# virtualenv --python python env

#install required packages
pip install -t lib -r requirements.txt

#activate python
# . env/bin/activate

#start to deploy
gcloud app deploy --stop-previous-version --project=jimmyvo2410 --version=$VERSION --quiet

#delete folder
cd $loc_project
Remove-Item -Recurse -Force -path $loc_tmp -ErrorAction SilentlyContinue

#start to deploy
gcloud app browse --project=jimmyvo2410





