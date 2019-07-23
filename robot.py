#!/usr/bin/python3
import wpilib
import wpilib.drive
from drivetrain import Drivetrain
from elevator import Elevator
from intake import Intake

JOYSTICK_PORT = 0
JOYSTICK2_PORT = 1
ELEVATOR_SPEED = 0.75
SLOW_SPEED = .5

class Robot(wpilib.TimedRobot):
	def robotInit(self):
		self.slowMode = True 
		self.drivetrain = Drivetrain()	
		self.elevator = Elevator()
		self.driver = wpilib.XboxController(JOYSTICK_PORT)	
		self.intake = Intake()

	def robotPeriodic(self):
		pass

	def autonomousInit(self):
		print('auton init')	

	def autonomousPeriodic(self):
		print('auton periodic')
		
	def teleopInit(self):
		print('teleop init')


		
	def teleopPeriodic(self):
		#Variables to hold motor values
		driveSpeed, driveAngle = 0, 0 
		elevatorSpeed = .07 #constant to maintain height
		intakeSpeed = 0
		intakeAngle = 0

		if self.driver.getAButtonPressed():
			print('a')	
		elif self.driver.getBButtonPressed():
			print('b')
		elif self.driver.getBackButtonPressed():
			self.slowMode = not self.slowMode
			if self.slowMode:
				print('Slow Mode Enabled')
			else:
				print('Slow Mode Disabled')
			#print('back')
		elif self.driver.getStartButtonPressed():
			print('start')
		elif self.driver.getStickButtonPressed(0):
			print('left stick button')
		elif self.driver.getStickButtonPressed(1):
			print('right stick button')

		'''intake'''
		if self.driver.getBumper(0):
			intakeSpeed = -0.5
			#print('left bumper')
		elif self.driver.getBumper(1):
			intakeSpeed = .8
			#print('right bumper')
		if self.driver.getXButton():
			intakeAngle = -0.7
			#print('x')
		elif self.driver.getYButton():
			intakeAngle = 0.7
			#print('y')

		'''elevator'''
		#left trigger
		if self.driver.getTriggerAxis(0) > .05:
			elevatorSpeed = -self.driver.getTriggerAxis(0)*0.7 #move slower while lowering elevator
			#print(f'left trigger: {self.driver.getTriggerAxis(0)}')

		#right trigger
		elif self.driver.getTriggerAxis(1) > .05:
			elevatorSpeed = self.driver.getTriggerAxis(1)
			#print(f'right trigger: {abs(self.driver.getTriggerAxis(1))}')

		'''drivetrain'''
		#left and right stick
		#up is negative, down is positive
		#-------------------------------------
		#left stick x axis
		if self.driver.getX(0) < -.05 or self.driver.getX(0) > .05:
			#print(f'left x: {self.driver.getX(0)}')
			pass

		#right stick x axis
		if self.driver.getX(1) < -.05 or self.driver.getX(1) > .05:
			driveAngle = self.driver.getX(1)
			#print(f'right x: {self.driver.getX(1)}')

		#left stick y axis
		if self.driver.getY(0) < -.05 or self.driver.getY(0) > .05:
			#negative because of the inverted signal
			driveSpeed = -self.driver.getY(0)
			#print(f'left y: {-self.driver.getY(0)}')

		#right stick y axis is mapped to right trigger for some reason
		#right stick y axis
		if self.driver.getY(1) < -.05 or self.driver.getY(1) > .05:
			#negative because of the inverted signal
			#print(f'right y: {-self.driver.getY(1)}')
			pass

		if self.slowMode:
			driveAngle = driveAngle * SLOW_SPEED
			driveSpeed = driveSpeed * SLOW_SPEED
			elevatorSpeed = elevatorSpeed * SLOW_SPEED
			if elevatorSpeed < .07 and elevatorSpeed >= 0:
				elevatorSpeed = .07
			intakeSpeed = intakeSpeed * SLOW_SPEED
			intakeAngle = intakeAngle * SLOW_SPEED

		#h = self.elevator.getHeight()
		#print(h)

		#apply values to motors
		self.drivetrain.arcadeDrive(driveSpeed, driveAngle)
		self.elevator.translateElevator(elevatorSpeed)
		self.intake.setSpeed(intakeSpeed)
		self.intake.setAngle(intakeAngle)


if __name__ == '__main__':
	wpilib.run(Robot)