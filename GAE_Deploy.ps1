# ########################################################################################
# GAE configuration
# ########################################################################################
$VERSION				= "20181230t012741"
$PROJECT 				= "jimmyvo2410"

# ########################################################################################
# Build configuration
# ########################################################################################
$Path_StaticProject		= "D:\Github\jimmyvo2410.github.io"
$Path_FlashProject 		= "D:\Github\jimmyvo2410.GAE"
$Path_Deploy 			= "Deploy"

$Path_BuildFolders 		= @("static", "templates")
$Path_BuildFiles 		= @("app.yaml", "appengine_config.py", "mw_email.py", "main.py", "requirements.txt")

# ########################################################################################
# Update from static project (It may not work on your local machine)
# ########################################################################################
if(Test-Path -Path $Path_StaticProject ){

	#remove folders
	cd $Path_FlashProject
	for ($i=0; $i -lt $Path_BuildFolders.length; $i++) {
		Remove-Item -Recurse -Force -path $Path_BuildFolders[$i] -ErrorAction SilentlyContinue
	}
	
	#Copy folders
	cd $Path_StaticProject
	for ($i=0; $i -lt $Path_BuildFolders.length; $i++) {
		$newFolder = $Path_FlashProject + "\" + $Path_BuildFolders[$i]
		Copy-Item -Path $Path_BuildFolders[$i] -Recurse -Destination $newFolder -Container
	}	
}

# ########################################################################################
# Clone project to deploy
# ########################################################################################
#Project Path
cd $Path_FlashProject

#Remove folder if existing
Remove-Item -Recurse -Force -path $Path_Deploy -ErrorAction SilentlyContinue

#Create folder
mkdir $Path_Deploy 

#Copy files
for ($i=0; $i -lt $Path_BuildFiles.length; $i++) {
    Copy-Item -Path $Path_BuildFiles[$i] -Recurse -Destination $Path_Deploy -Container
}

#Copy folders
for ($i=0; $i -lt $Path_BuildFolders.length; $i++) {
    $newFolder = $Path_Deploy + "\" + $Path_BuildFolders[$i]
    Copy-Item -Path $Path_BuildFolders[$i] -Recurse -Destination $newFolder -Container
}

#go to folders
cd $Path_Deploy

# ########################################################################################
# Prepare to deploy
# ########################################################################################
#setup virtual environment
# virtualenv --python python env

#install required packages
pip install -t lib -r requirements.txt

#activate python
# . env/bin/activate

#start to deploy
gcloud app deploy --project=$PROJECT --version=$VERSION --quiet


#start to deploy
gcloud app browse --project=$PROJECT

# ########################################################################################
# Start deploying
# ########################################################################################
cd $Path_FlashProject
while (Test-Path $Path_Deploy) { 
    Start-Sleep 1 
    echo "try to delete $Path_Deploy"
    Remove-Item -Recurse -Force -path $Path_Deploy -ErrorAction SilentlyContinue
}

Pause