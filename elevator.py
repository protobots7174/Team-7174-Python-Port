import wpilib
from ctre import WPI_TalonSRX


ELEVATOR_TALON = 0


class Elevator:
	def __init__(self):
		self.lidar = wpilib.I2C(wpilib.I2C.Port.kOnboard, 0x03)
		self.lift_motor = WPI_TalonSRX(ELEVATOR_TALON)

	def translateElevator(self, speed: float) -> None:
		self.lift_motor.set(speed)

	#Get the current height with LiDar
	def getHeight(self) -> float:
		buffer = self.lidar.read(0x03, 1)
		#data comes in as a list of one integer 
		height = buffer[0]
		#convert cm to inches
		height = height/2.54
		#print(f'Elevator height: {height}')
		return height 

	def autonElevator(self, height: float) -> bool:
		pass

	def setHeight(self, height: float) -> None:
		pass

	def setHeightPID(self, height: float) -> None:
		pass