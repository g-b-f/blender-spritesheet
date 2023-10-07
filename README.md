# Blender Render Exporter
Clone of render export scripts for blender for further experiments

Added a simple Blender Plugin UI to access the most functions from the render script.

The add on can be found under properties > output > direction renderer

This requires Pillow, to install go to the blender python bin directory, e.g
`C:\\Program Files\\Blender Foundation\\Blender 3.6\\3.6\\python\\bin`,
then do `./python -m pip install PIL`.

I plan on making this automatic but for the time being this should work

This is the reference direction for the canonical direction names. The logic is North character position is with the face looking in North screen position as this is the typical behaviour in Games.
![iso-directions](https://github.com/andreas-volz/blender-render-direction/assets/16402165/45533dd3-3342-4ffc-82d3-9d8367f4db7d)

This addon works perfect together with https://github.com/jasonicarter/create-isocam.
