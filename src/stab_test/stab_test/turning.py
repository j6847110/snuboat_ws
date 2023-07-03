import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import Int32

class Pub(Node):

	def __init__(self):

		super().__init__('pub')

		qos_profile = QoSProfile(depth=10)

		self.publisher_ = self.create_publisher(Int32, 'pwm', qos_profile)
		
		timer_period = 1 # seconds

		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.di = ''
		self.count = 0
		self.thrust = 1500
		self.servo = 1500		
		self.maxangle =35*(1000/135)
	def timer_callback(self):
		msg = Int32()
		self.thrust = 1600
		if self.di =='':
			self.get_logger().info('direction input error')
		
		elif self.di =='port':
		# 1500~2500
			if self.servo < 1500+self.maxangle:
				self.servo += 10
		else :
		# 500 ~ 1500
			if self.servo > 1500-self.maxangle:
				self.servo -= 10
			
#		msg.data = self.thrust*10000+self.servo
		msg.data = self.servo
		self.publisher_.publish(msg)
		self.get_logger().info('Publishing: "%d"' % msg.data)
		# self.count += 10

def turn_pt(args=None):

	rclpy.init(args=args)

	node = Pub()
	node.di = 'port'
	try:
		rclpy.spin(node)
	except KeyboardInterrupt:
		node.get_logger().info('Keyboard Interrupt (SIGINT)')
	finally:
		node.destroy_node()
		rclpy.shutdown()
		
def turn_st(args=None):

	rclpy.init(args=args)

	node = Pub()
	node.di = 'stbd'
	try:
		rclpy.spin(node)
	except KeyboardInterrupt:
		node.get_logger().info('Keyboard Interrupt (SIGINT)')
	finally:
		node.destroy_node()
		rclpy.shutdown()		
		
		

if __name__=='__main__':
	main()
