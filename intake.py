import wpilib
from math import fabs
from ctre import WPI_TalonSRX, WPI_VictorSPX

RBALL_OBTAINER_VICTOR = 6
LBALL_OBTAINER_VICTOR = 7
BALL_ANGLE_TALON = 5

class Intake:
	def __init__(self):
		self.lBallObtainer = WPI_VictorSPX(LBALL_OBTAINER_VICTOR)
		self.rBallObtainer = WPI_VictorSPX(RBALL_OBTAINER_VICTOR)
		self.ballAngle = WPI_TalonSRX(BALL_ANGLE_TALON)
		self.autonTimer = wpilib.Timer()
		self.timerStart = False

	def setSpeed(self, speed: float) -> None:
		self.lBallObtainer.set(speed)
		self.rBallObtainer.set(speed)	

	def setAngle(self, speed: float) -> None:
		self.ballAngle.set(speed)	

	def getDistance(self) -> float:
		return self.ballAngle.getSelectedSensorPosition(0) / 10000

	def getAngleVelocity(self) -> float:
		return self.ballAngle.get()	

	def resetEncoders(self) -> None:
		self.ballAngle.setSelectedSensorPosition(0.0)

	def encoderWrite(self, angleDistance: float) -> None:
		if (fabs(angleDistance - self.getDistance()) > 2 and 
				self.getDistance() < angleDistance):
			self.ballAngle.set(-.5)
		elif (fabs(angleDistance - self.getDistance()) > 2 and 
				self.getDistance() > angleDistance):
			self.ballAngle.set(.5)
		else:
			self.ballAngle.set(0)


	def autonAngle(self, angleDistance: float) -> bool:
		if (fabs(angleDistance - self.getDistance()) > 2 and 
				self.getDistance() < angleDistance):
			self.ballAngle.set(-.5)
			return False
		elif (fabs(angleDistance - self.getDistance()) > 2 and 
				self.getDistance() > angleDistance):
			self.ballAngle.set(.5)
			return False
		else:
			self.ballAngle.set(0)
			return True

	def autonInOut(self, speed: float, seconds: float) -> bool:
		if not self.timerStart:
			self.autonTimer.start()
			self.timerStart = True
		self.lBallObtainer.set(speed)
		self.rBallObtainer.set(speed)

		if autonTimer.get() > seconds:
			self.autonTimer.reset()
			self.timerStart = False
			return True
		else:
			return False


	def autonTimerPrep(self) -> None:
		self.timerStart = False

	def getEncoder2Distance(self) -> float:
		pass
