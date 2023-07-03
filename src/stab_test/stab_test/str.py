import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import Int32

class Pub(Node):

	def __init__(self):

		super().__init__('pub')

		qos_profile = QoSProfile(depth=10)

		self.publisher_ = self.create_publisher(Int32, 'pwm', qos_profile)
		
		timer_period = 0.1 # seconds

		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.count = 0
		self.thrust = 1500
		self.servo = 1500	
		
	def timer_callback(self):
		msg = Int32()
		
		if self.count >10:
			self.thrust=1500
			#msg.data=self.thrust*10000+self.servo
			msg.data=self.servo
		else:
			self.thrust=1600
			#msg.data = self.thrust*10000+self.servo
			msg.data = self.servo
		self.publisher_.publish(msg)
		self.get_logger().info('Publishing: "%d"' % msg.data)
		self.count += 10

def main(args=None):

	rclpy.init(args=args)

	node = Pub()

	try:
		rclpy.spin(node)
	except KeyboardInterrupt:
		node.get_logger().info('Keyboard Interrupt (SIGINT)')
	finally:
		node.destroy_node()
		rclpy.shutdown()
		
if __name__=='__main__':
	main()
