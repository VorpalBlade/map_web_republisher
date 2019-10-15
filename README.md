# Map web republisher

This simple [ROS](https://www.ros.org/) node subscribes to `map` and saves the
map as a png to a specified directory. It then republishes the header and
map metadata to `web/map_updated` as a `map_web_republisher/MapStatus` message.

This is inteded to be used together with
[rosbridge](https://wiki.ros.org/rosbridge_server) in order to deal with large
maps, as they are inefficiently transferred as JSON.

## Topics

* `map` (`nav_msgs/OccupancyGrid`) - Input
* `web/map_updated` (`map_web_republisher/MapStatus`) - Output

## Parameters

* `~path` (`str`) - Where to save the image.
