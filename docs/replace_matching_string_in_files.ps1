# Replace matching strings with another string in the given list of files
param(
    [string]$folder = "../quantum_nodes/",
    [string]$find = "@persistent",
    [string]$replace = "#@persistent"
)

[array]$files = Get-ChildItem -Path $folder -Include *.py -Recurse -Force | select -expand fullname

function Find-And-Replace-Strings {

    param(
        [array]$files,
        [string]$find,
        [string]$replace
    )

    ForEach ($file in $files) {
        (Get-Content -Path $file -Raw) -replace $find, $replace | Set-Content -Path $file -NoNewLine
    }
}

Find-And-Replace-Strings $files $find $replace