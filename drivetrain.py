import wpilib
import wpilib.drive
from ctre import WPI_TalonSRX
from wpilib.drive import DifferentialDrive
from math import fabs
from MyPID import ProtoPID

TALON_DRIVE_LF = 2
TALON_DRIVE_LR = 1
TALON_DRIVE_RF = 4
TALON_DRIVE_RR = 3
DRIVE_ENCODER_COUNTS_PER_FOOT = 535.0


class Drivetrain:
	def __init__(self):
		self.lDriveF = WPI_TalonSRX(TALON_DRIVE_LF)
		self.lDriveR = WPI_TalonSRX(TALON_DRIVE_LR)
		self.rDriveF = WPI_TalonSRX(TALON_DRIVE_RF)
		self.rDriveR = WPI_TalonSRX(TALON_DRIVE_RR)
		#self.rDriveF.setInverted(True)
		#self.rDriveR.setInverted(True)

		self.lSpeedGroup = wpilib.SpeedControllerGroup(self.lDriveF, self.lDriveR)
		self.rSpeedGroup = wpilib.SpeedControllerGroup(self.rDriveF, self.rDriveR)
		self.drive = DifferentialDrive(self.lSpeedGroup, self.rSpeedGroup)
		self.drive.setSafetyEnabled(False)

		self.drivePID = ProtoPID(1/5.0, 0.0, 0.0, 0.0, 0.02)


	def arcadeDrive(self, speed: float, angle: float) -> None:
		#print(f'arcade drive: {speed}, {angle}')
		self.drive.setSafetyEnabled(True)
		self.drive.arcadeDrive(speed, angle)


	'''
	encoder functions 
	'''
	def resetEncoders(self) -> None:
		self.lDriveF.setSelectedSensorPosition(0)
		self.rDriveR.setSelectedSensorPosition(0)

	def getDistance(self) -> float:
		return (-self.lDriveF.getSelectedSensorPosition(0) + \
			self.rDriveR.getSelectedSensorPosition(0)) \
			/ 2 / DRIVE_ENCODER_COUNTS_PER_FOOT

	def getTurningDistance(self) -> float:
		return (fabs(-lDriveF.getSelectedSensorPosition(0)) + \
			 abs(rDriveR.getSelectedSensorPosition(0))) \
			 / 2 / DRIVE_ENCODER_COUNTS_PER_FOOT

	def getRDistance(self) -> float:
		return self.rDriveR.getSelectedSensorPosition(0) / DRIVE_ENCODER_COUNTS_PER_FOOT

	def getLDistance(self) -> float:
		return -self.lDriveF.getSelectedSensorPosition(0) / DRIVE_ENCODER_COUNTS_PER_FOOT	

	def getRVelocity(self) -> float:
		return self.rDriveR.getSelectedSensorVelocity(0)	

	def getLVelocity(self) -> float:
		return -self.lDriveR.getSelectedSensorVelocity(0)	

	def getYaw(self) -> float:
		pass

	def encoderWrite(self, rightDistance, leftDistance) -> None:
		pass


	'''
	auton functions 
	'''
	def autonDrivetrain(self, rVelocity: float, lVelocity: float, rDistance: float,
					    lDistance: float) -> bool:
		self.drive.setSafetyEnabled(False)
		if fabs(self.getRDistance()) < rDistance:
			self.rDriveF.set(-rVelocity)
			self.rDriveR.set(-rVelocity)
		elif fabs(self.getRDistance()) < rDistance:
			self.rDriveF.set(-.1)
			self.rDriveR.set(-.1)
		else:
			self.rDriveF.set(0)
			self.rDriveR.set(0)

		if fabs(self.getLDistance()) < (lDistance - .2):
			self.lDriveF.set(lVelocity)
			self.lDriveR.set(lVelocity)
		elif fabs(self.getLDistance()) < lDistance:
			self.lDriveF.set(.1)
			self.lDriveR.set(.1)
		else:
			self.lDriveF.set(0)
			self.lDriveR.set(0)

		if fabs(self.getRDistance()) >= rDistance and fabs(self.getLDistance()) >= lDistance:
			return True
		else:
			return False

	def autonLimeDrive(self, speed: float, angle: float, area: float) -> bool:
		self.drive.arcadeDrive(speed, angle)
		if area > 8:
			return True
		else:
			return False


	def autonTurning(self, distance: float) -> bool:
		angle = 0
		if distance > 0:
			angle = .5
		else:
			angle = -.5
		if self.getTurningDistance() < distance:
			self.drive.arcadeDrive(0, angle)
		else:
			self.drive.arcadeDrive(0, 0)
			return True
		return False

	def autonStraight(self, distance: float) -> bool:
		speed = 0
		if distance > 0:
			speed = .6
		else:
			speed = -.6

		if self.getDistance() < distance:
			self.drive.arcadeDrive(speed , 0)
		else:
			self.drive.arcadeDrive(0,0)
			return True
		return False

	def autonPID(self, distance: float) -> bool:
		if fabs(self.getDistance() < fabs(distance)):
			command = self.drivePID.compute(self.getDistance(), distance)
			bias = 0
			if distance > 0:
				bias = .22
			else:
				bias = -.22
			self.drive.arcadeDrive(command + bias, 0)
		else:
			self.drive.arcadeDrive(0,0)

		return True

	def velocityMultiplier(self, firstV: float, secondV: float, 
						  firstEncoderSpeed: float, secondEncoderSpeed: float) -> float:
		ratio = firstV / secondV
		vRatio = firstEncoderSpeed / secondEncoderSpeed
		if (vRatio / ratio) < 1:
			return (ratio / vRatio) * firstV
		else:
			return 1.0 * firstV

	'''teleop PID drive for testing'''
	def pidDrive(self, angle: float, distance: float) -> float:
		command = self.drivePID.compute(self.getDistance(), distance)
		bias = 0
		if distance > 0:
			bias = .22
		else:
			bias = -.22
		self.drive.arcadeDrive(command + bias, angle)

