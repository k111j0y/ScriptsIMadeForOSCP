#Hardcoded Path && keywords
# PS C:\SomeDir\Youre\In> .\poshInspectFiles_hardcoded.ps1

# Specify the directory to search
$directory = "C:\SomeDir\You\Wanna\Search\Under" 

# Specify the keywords to search for
$keywords = "keyword", "keyword2" , "keyword3"

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
