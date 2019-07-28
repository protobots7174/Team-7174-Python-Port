import wpilib
from math import fabs
from ctre import WPI_TalonSRX
from MyPID import ProtoPID


ELEVATOR_TALON = 0
TOLERANCE_INCHES = 1.5


class Elevator:
	def __init__(self):
		self.lidar = wpilib.I2C(wpilib.I2C.Port.kOnboard, 0x03)
		self.liftMotor = WPI_TalonSRX(ELEVATOR_TALON)
		self.elevatorPID = ProtoPID(1/18.0, 0.0, 0.0, 0.0, .02)

	def translateElevator(self, speed: float) -> None:
		self.liftMotor.set(speed)

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
		currentHeight = self.getHeight()
		direction = 0
		if height - currentHeight >= 0:
			direction = 1
		else:
			direction = -1

		if (fabs(height - currentHeight) > TOLERANCE_INCHES and 
				fabs(height - currentHeight) > 8):
			self.liftMotor.set(1 * direction)
			return False
		elif (fabs(height - currentHeight) > TOLERANCE_INCHES and 
				fabs(height - currentHeight) > 6):
			self.liftMotor.set(.55 * direction)
			return False
		elif (fabs(height - currentHeight) > TOLERANCE_INCHES and 
				fabs(height - currentHeight) > 3):
			self.liftMotor.set(.4 * direction)
			return False
		else:
			self.liftMotor.set(.07)
			return True

	def setHeight(self, height: float) -> None:
	    currentHeight = self.getHeight()
	    direction = 0
	    if (height - currentHeight) >= 0:
	        direction = 1
	    else:
	        direction = -1

	    if (fabs(height - currentHeight) > TOLERANCE_INCHES and 
	    		fabs(height - currentHeight) > 8):
	        self.liftMotor.set(1.0 * direction)
	    elif (fabs(height - currentHeight) > TOLERANCE_INCHES and 
	    		fabs(height - currentHeight) > 6):
	        self.liftMotor.set(0.55 * direction)
	    elif (fabs(height - currentHeight) > TOLERANCE_INCHES and 
	    		fabs(height - currentHeight) > 3):
	        self.liftMotor.set(0.2 * direction)
	    elif (fabs(height - currentHeight) > TOLERANCE_INCHES):
	        self.liftMotor.set(0.2 * direction)
	    else:
	        self.liftMotor.set(0.07)

	def setHeightPID(self, height: float) -> None:
		command = self.elevatorPID.compute(self.getHeight(), height)
		lift.set(command + .07)