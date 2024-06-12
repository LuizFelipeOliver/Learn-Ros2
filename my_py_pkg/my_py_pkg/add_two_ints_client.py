#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial

from example_interfaces.srv import AddTwoInts

class AddTwoIntsNode(Node): 
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.call_add_two_ints_server(6, 7)
    
    def call_add_two_int_server(self, a, b):
        client = self.create_client(AddTwoInts, "add_two_ints")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Add Two Ints...")
        
        request = AddTwoInts.Request()
        request.a = a
        request.b = b
        
        future = client.call_async(request)
        future.add_done_callback(partial(self.call_add_two_int_ints, a=a, b=b))
        
    def call_add_two_int_ints(self, future, a ,b):
        try:
            response = future.result()
            self.get_logger().info(str(a) + " + " + 
                                   str(b) + " = " + str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed %r" %(e,))
        
def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsNode() 
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()
