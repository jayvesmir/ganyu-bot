Write-Output "Creating Virtual Environment"
python -m venv venv
Write-Output "Activating Virtual Environment"
venv/scripts/activate.ps1
Write-Output "Installing required libraries"
python -m pip install -r requirements.txt
Clear-Host