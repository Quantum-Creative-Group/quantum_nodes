#!/bin/bash

SITE_PACKAGES=$1
ANIMATION_NODES=$2
QUANTUM_NODES=$3

echo "---------- SETUP ANIMATION NODES: START ---------"

echo "STEP 1: replace __init__.py file"

rm $ANIMATION_NODES/__init__.py
cp $QUANTUM_NODES/docs/_static/animation_nodes_init_replacement_file.txt $ANIMATION_NODES/__init__.py

echo "STEP 2: edit preferences.py"

find $ANIMATION_NODES/ -type f -name "*.py" -exec sed -i 's/return bpy.app.version/return bpy.app.version if bpy.app.version is not None else (2, 93, 0)/g' {} +

echo "STEP 3: remove '@persistent' decorators"

find $ANIMATION_NODES/ -type f -name "*.py" -exec sed -i 's/@persistent/#@persistent/g' {} +

echo "STEP 4: move animation_nodes to 'site-packages/'"

sudo cp -r $ANIMATION_NODES $SITE_PACKAGES

echo "----------- SETUP ANIMATION NODES: END ----------"
