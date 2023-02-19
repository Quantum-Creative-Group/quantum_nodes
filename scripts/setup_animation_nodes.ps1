param(
    [string]$animation_nodes = "./animation_nodes/",
    [string]$quantum_nodes = "./",
    [string]$site_packages
)

Write-Output "---------- SETUP ANIMATION NODES: START ---------"

Write-Output "STEP 1: replace __init__.py file"

Remove-Item $animation_nodes/__init__.py
Copy-Item $quantum_nodes/docs/_static/animation_nodes_init_replacement_file.txt -Destination $animation_nodes/__init__.py

Write-Output "STEP 2: edit preferences.py"

$file = "$animation_nodes/preferences.py"
$find = "return bpy.app.version"
$replace = "return bpy.app.version if bpy.app.version is not None else (2, 93, 0)"
(Get-Content -Path $file -Raw) -replace $find, $replace | Set-Content -Path $file -NoNewLine

Write-Output "STEP 3: remove '@persistent' decorators"

"$PSScriptRoot\..\docs\replace_matching_string_in_files.ps1 -folder ./animation_nodes/"

Write-Output "STEP 4: move animation_nodes to 'site-packages/'"

Copy-Item $animation_nodes -Destination $site_packages -Recurse

Write-Output "----------- SETUP ANIMATION NODES: END ----------"
