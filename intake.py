import wpilib
from ctre import WPI_TalonSRX, WPI_VictorSPX

RBALL_OBTAINER_VICTOR = 6
LBALL_OBTAINER_VICTOR = 7
BALL_ANGLE_TALON = 5

class Intake:
	def __init__(self):
		self.lBallObtainer = WPI_VictorSPX(LBALL_OBTAINER_VICTOR)
		self.rBallObtainer = WPI_VictorSPX(RBALL_OBTAINER_VICTOR)
		self.ballAngle = WPI_TalonSRX(BALL_ANGLE_TALON)

	def setSpeed(self, speed: float) -> None:
		self.lBallObtainer.set(speed)
		self.rBallObtainer.set(speed)	

	def setAngle(self, speed: float) -> None:
		self.ballAngle.set(speed)	

	def getDistance(self) -> float:
		pass

	def getAngleVelocity(self) -> float:
		return self.ballAngle.get()	

	def resetEncoders(self) -> None:
		pass

	def encoderWrite(self, angleDistance: float) -> None:
		pass

	def getEncoder2Distance(self) -> float:
		pass

	def autonAngle(self, angleDistance: float) -> bool:
		pass

	def autonInOut(self, speed: float, seconds: float) -> bool:
		pass

	def autonTimerPrep(self) -> None:
		pass