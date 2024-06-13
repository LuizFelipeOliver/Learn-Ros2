#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
 
 
class AddTwoIntsServerNode(Node): 
    def __init__(self):
        super().__init__("node_name") 
        self.server_ =self.create_service(
            AddTwoInts, "add_two_ints", self.callback_add_two_ints)
    
    def callback_add_two_ints(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a) + "+" + str(request.b) + "=" + str(request.sum)) 
        return response    
 
def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsServerNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
