# Replace matching strings with another string in the given list of files
param(
    [string]$folder = "../quantum_nodes/",
    [string]$find = "@persistent",
    [string]$replace = "#@persistent"
)

[array]$files = Get-ChildItem -Path $folder -Include *.py -Recurse -Force | select -expand fullname

function Replace-Strings-In-Files {

    param(
        [array]$files,
        [string]$find,
        [string]$replace
    )

    ForEach ($file in $files) {
        (Get-Content -Path $file -Raw) -replace $find, $replace | Set-Content -Path $file -NoNewLine
    }
}

Replace-Strings-In-Files $files $find $replace