"""ROS node that takes map and publishes it as a PNG to the web server folder"""

from __future__ import (print_function, absolute_import, division)

import os

import imageio
import numpy as np
import rospy
from pathlib2 import Path
from map_web_republisher.msg import MapStatus
from nav_msgs.msg import OccupancyGrid


def _color_converter(value):
    if value == -1:
        return 0xcd / 0xff
    return (100 - value) / 100.0


class Node(object):
    """Main node class"""

    def __init__(self):
        """Constructor"""
        self._path = rospy.get_param('~path',
                                     os.path.join(os.getenv('HOME'),
                                                  'ipw/ws/src/web/site/dist/maps/map.png'))
        # Ensure directory exists
        Path(self._path).parent.mkdir(parents=True, exist_ok=True)
        self._sub = rospy.Subscriber('map',
                                     OccupancyGrid,
                                     callback=self._callback_map,
                                     queue_size=1)
        self._pub = rospy.Publisher('web/map_updated',
                                    MapStatus,
                                    queue_size=1,
                                    latch=True)

    def _callback_map(self, msg):
        """Callback from map

        :type msg: OccupancyGrid
        """
        np_data = np.array([_color_converter(e) for e in msg.data])
        reshaped = np.flipud(np.reshape(np_data, (msg.info.height, msg.info.width)))
        imageio.imwrite(self._path, reshaped, format='png', optimize=True, quantize=4)
        rospy.loginfo("Wrote map of size %r to %s" % (reshaped.shape, self._path))
        # Publish message to tell client to download new map.
        status = MapStatus()
        status.header = msg.header
        status.info = msg.info
        self._pub.publish(status)


def main():
    """Main program entry point"""
    rospy.init_node("oru_ipw_cmd_inverter")

    ros_node = Node()

    # Spin on ROS message bus
    rospy.spin()
