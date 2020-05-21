#Script to send email appointment reminders. Interface should be set up as Transform Email / Transport SMTP Out.
from System import *
from MediaHighway.Common.BLL import *
from MediaHighway.Common.BLL.Patient import *
from MediaHighway.Common.BLL.Prefs import *
from MediaHighway.Common.Shared.Util import *
from System.Text import *

#outVars.Payload --The email message body
#outVars.IsHTML --Is the body html
#outVars.FromAddress --Email from address
#outVars.FromName --EMail from name
#outVars.ToAddresss --Email to adress 
#outVars.Subject --Email subject
 
EMAIL_FROM = "noreply@bakersfield.studenthealthportal.com"
EMAIL_FROM_NAME = "Student Health Center"
EMAIL_SUBJECT = "NEW Student Health and Wellness Portal"
IS_HTML = True

def BuildEMail():
	if String.IsNullOrEmpty(appointment.Patient.EmailAddress):
		errors.Add("EMail address is empty.")
		return None
	
	msg = StringBuilder(emailTemplate)
		
	msg.Replace("[PATIENT_FIRSTNAME]",appointment.Patient.FirstName);
	msg.Replace("[PATIENT_LASTNAME]", appointment.Patient.LastName);
	msg.Replace("[APPT_DATE]", appointment.StartDate.ToString("MM/dd/yy"));
	msg.Replace("[APPT_TIME]", appointment.StartDate.ToString("hh:mm tt"));
	
	apptProvider = appointment.Provider
	if apptProvider == None:
		provider = " with a provider to be determined"
	else:
		provider = " with"
		if apptProvider.FirstName != None:
			provider += " " + apptProvider.FirstName
		if apptProvider.LastName != None:
			provider += " " + apptProvider.LastName
		if apptProvider.NameSuffix != None:
			provider += ", " +  EnumDescConverter.GetEnumDescription(apptProvider.NameSuffix)	

	msg.Replace("[PROVIDER_NAME]", provider)

	outVars.ToAddresss = appointment.Patient.EmailAddress
	outVars.IsHTML = IS_HTML
	outVars.FromAddress = EMAIL_FROM
	outVars.FromName = EMAIL_FROM_NAME
	outVars.Subject = EMAIL_SUBJECT

	return msg.ToString()

def ProcessMessage():	
	msg = BuildEMail()
	if outVars.ToAddresss != None: print "EMail Address:", outVars.ToAddresss
	if testMode:
		print msg
	if errors.Count == 0:
		outVars.Payload = msg

ProcessMessage()

#Email Body
<p><font color="red">First Time Portal Clients:</font><br>
Please take a few moments and register to access your NEW BC Student Health & Wellness Portal<br>
https://bakersfield.studenthealthportal.com/Registration/Register<br>
<font color="red">University ID = BC Student ID number (ex:@00xxxxxx)<br>Email must be your College assigned email.</font>
<br>
<br>
Once access is granted, please visit My Forms to complete your Personal Health Information Updates.
<br>

