# .\poshInspectFiles_commandArgs.ps1 -directory "C:\Your\Directory" -keywords "keyword1", "keyword2", "keyword3"

param(
    [string]$directory,    
    [string[]]$keywords   
)

if (-not $directory) {
    Write-Host "Please provide a directory to search."
    exit
}

if (-not $keywords) {
    Write-Host "Please provide one or more keywords to search for."
    exit
}

# Get all files in the specified directory
$files = Get-ChildItem -Path $directory -File -Recurse

# Loop through each file
foreach ($file in $files) {
    # Read the file content
    $content = Get-Content $file.FullName

    # Check if the file contains any of the keywords
    foreach ($keyword in $keywords) {
        if ($content -match $keyword) {
            Write-Host "Keyword '$keyword' found in file: $($file.FullName)"
        }
    }
}
