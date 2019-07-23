import wpilib
import wpilib.drive
from ctre import WPI_TalonSRX
from wpilib.drive import DifferentialDrive

TALON_DRIVE_LF = 2
TALON_DRIVE_LR = 1
TALON_DRIVE_RF = 4
TALON_DRIVE_RR = 3
DRIVE_ENCODER_COUNTS_PER_FOOT = 535.0


class Drivetrain:
	def __init__(self):
		self.m_lDriveF = WPI_TalonSRX(TALON_DRIVE_LF)
		self.m_lDriveR = WPI_TalonSRX(TALON_DRIVE_LR)
		self.m_rDriveF = WPI_TalonSRX(TALON_DRIVE_RF)
		self.m_rDriveR = WPI_TalonSRX(TALON_DRIVE_RR)
		#self.m_rDriveF.setInverted(True)
		#self.m_rDriveR.setInverted(True)
		self.m_lSpeedGroup = wpilib.SpeedControllerGroup(self.m_lDriveF, self.m_lDriveR)
		self.m_rSpeedGroup = wpilib.SpeedControllerGroup(self.m_rDriveF, self.m_rDriveR)
		self.m_drive = DifferentialDrive(self.m_lSpeedGroup, self.m_rSpeedGroup)
		self.m_drive.setSafetyEnabled(False)


	def arcadeDrive(self, speed: float, angle: float) -> None:
		#print(f'arcade drive: {speed}, {angle}')
		self.m_drive.setSafetyEnabled(True)
		self.m_drive.arcadeDrive(speed, angle)


	'''
	encoder functions 
	'''
	def getRDistance(self) -> float:
		pass

	def getLDistance(self) -> float:
		pass

	def getRVelocity(self) -> float:
		pass

	def getLVelocity(self) -> float:
		pass

	def getYaw(self) -> float:
		pass

	def resetEncoders(self) -> None:
		pass

	def encoderWrite(self, rightDistance, leftDistance) -> None:
		pass

	def getTurningDistance(self) -> float:
		pass

	'''
	auton functions 
	'''
	def autonDrivetrain(self, rVelocity: float, lVelocity: float, rDistance: float,
					    lDistance: float) -> bool:
		pass


	def autonLimeDrive(self, speed: float, angle: float, area: float) -> bool:
		pass 

	def pidDrive(self, angle: float, distance: float) -> float:
		pass

	def autonTurning(self, distance: float) -> bool:
		pass

	def autonStraight(self, distance: float) -> bool:
		pass

	def autonPID(self, distance: float) -> bool:
		pass	

	def velocityMultiplier(self, firstV: float, secondV: float, 
						  firstEncoderSpeed: float, secondEncoderSpeed: float) -> float:
		pass


