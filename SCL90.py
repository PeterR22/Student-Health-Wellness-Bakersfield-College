#-------------Name: Peter  Rodriguez 
#-------------Date: 03/30/2020
#-------------Information: This script counts the number of each response provided by
#-------------             patients from the SCL-90 form. The total number of Yes/No responses
#-------------             are totaled to assist mental health providers in their methodology 
#-------------             for assessing/diagnosing their clients. 

# 100% Functional
#-------------Name: Peter  Rodriguez 
#-------------Date: 05/01/2020
#-------------Information: This script counts the number of each response provided by
#-------------             patients from the SCL-90 form. The total number of Yes/No responses
#-------------             are totaled to assist mental health providers in their methodology 
#-------------             for assessing/diagnosing their clients. 

#---- Variable Name Characters Exceed Name Object in System. List below details variable name changes.
#----
#---- I did it! :)

from MediaHighway.Common.BLL.Forms import *

def Run(form,changedObject,changeType,loadStatus):
	if changedObject.Name == None : return
	if changedObject.Name.StartsWith("q"):
		Count_SCL90_Responses(form)

#@funtion Count_SCL90_Responses counts the user response choice to the 90 Question assessment.
#@Variables declared in function scope to avoid global variables 
def Count_SCL90_Responses(form):
	Number_of_Not_At_All_Response = 0 
	Number_of_A_Little_Bit_Response = 0
	Number_of_Moderately_Response = 0
	Number_of_Quite_A_Bit_Response = 0
	Number_of_Extremely_Response = 0

	#@Variables assigned point value of each response choice
	Not_At_All_Response_Value = 0 
	A_Little_Bit_Response_Value = 1
	Moderately_Response_Value = 2
	Quite_A_Bit_Response_Value = 3
	Extremely_Response_Value = 4
	
	#@variables hold accumulated points for each answer
	Points_Accumulated_Not_At_All_Response = 0   
	Points_Accumulated_A_Little_Bit_Response = 0 
	Points_Accumulated_Moderately_Response = 0
	Points_Accumulated_Quite_A_Bit_Response = 0 
	Points_Accumulated_Extremely_Response = 0
	
	#@variables names reflect name put into form interface. 
	Total_Points_Accumulated_Not_At_All_Re = 0   
	Total_Points_Accumulated_A_Little_Bit_Re = 0 
	Total_Points_Accumulated_Moderately_Re = 0
	Total_Points_Accumulated_Quite_A_Bit_Re = 0 
	Total_Points_Accumulated_Extremely_Re = 0
	
	#@Variable Total_Points holds summation of all points
	Total_Points = 0
	#@variable Total_Points_Overall reflects name put into form interface
	Total_Points_Overall = 0
	
	#The loop will count the response of each question ('q1') to ('q90')
	for i in range(1,91):
		question = form["q"+str(i)]
		if question == None or question.EditValueAsString == "" : continue
		idx = question.Selections.IndexOf(question.CurrentSelection)
		if idx == 0: Number_of_Not_At_All_Response+= 1
		if idx == 1: Number_of_A_Little_Bit_Response+= 1
		if idx == 2: Number_of_Moderately_Response+= 1
		if idx == 3: Number_of_Quite_A_Bit_Response+= 1
		if idx == 4: Number_of_Extremely_Response+= 1
			
	#@variables hold amount of points generated from multiplying amount of each choice by associated choice value
	Points_Accumulated_Not_At_All_Response = Number_of_Not_At_All_Response*Not_At_All_Response_Value  
	Points_Accumulated_A_Little_Bit_Response = Number_of_A_Little_Bit_Response*A_Little_Bit_Response_Value
	Points_Accumulated_Moderately_Response = Number_of_Moderately_Response*Moderately_Response_Value
	Points_Accumulated_Quite_A_Bit_Response = Number_of_Quite_A_Bit_Response*Quite_A_Bit_Response_Value
	Points_Accumulated_Extremely_Response = Number_of_Extremely_Response*Extremely_Response_Value
	
	#@variable Total_Points stores the total amount of points earned from each question
	Total_Points = Points_Accumulated_Extremely_Response+Points_Accumulated_Not_At_All_Response+Points_Accumulated_A_Little_Bit_Response+Points_Accumulated_Moderately_Response+Points_Accumulated_Quite_A_Bit_Response
	
	#Stores value in form object name to detail total number of each form response. 
	if form["Total_Number_of_Not_At_All_Response"]!= None: form["Total_Number_of_Not_At_All_Response"].EditValue = Number_of_Not_At_All_Response
	if form["Total_Number_of_A_Little_Bit_Response"]!= None: form["Total_Number_of_A_Little_Bit_Response"].EditValue = Number_of_A_Little_Bit_Response
	if form["Total_Number_of_Moderately_Response"]!= None: form["Total_Number_of_Moderately_Response"].EditValue = Number_of_Moderately_Response
	if form["Total_Number_of_Quite_A_Bit_Response"]!= None: form["Total_Number_of_Quite_A_Bit_Response"].EditValue = Number_of_Quite_A_Bit_Response
	if form["Total_Number_of_Extremely_Response"]!= None: form["Total_Number_of_Extremely_Response"].EditValue = Number_of_Extremely_Response	
	
	#Stores value in form object name to detail total points generated from each response. Object names edited to reflect character limit of interface text box. 
	if form["Total_Points_Accumulated_Not_At_All_Re"]!= None: form["Total_Points_Accumulated_Not_At_All_Re"].EditValue = Points_Accumulated_Not_At_All_Response
	if form["Total_Points_Accumulated_A_Little_Bit_Re"]!= None: form["Total_Points_Accumulated_A_Little_Bit_Re"].EditValue = Points_Accumulated_A_Little_Bit_Response
	if form["Total_Points_Accumulated_Moderately_Re"]!= None: form["Total_Points_Accumulated_Moderately_Re"].EditValue = Points_Accumulated_Moderately_Response
	if form["Total_Points_Accumulated_Quite_A_Bit_Re"]!= None: form["Total_Points_Accumulated_Quite_A_Bit_Re"].EditValue = Points_Accumulated_Quite_A_Bit_Response
	if form["Total_Points_Accumulated_Extremely_Re"]!= None: form["Total_Points_Accumulated_Extremely_Re"].EditValue = Points_Accumulated_Extremely_Response
	
	#Stores total points of entire assessment in form object Total_Points_Overall to detail User Total Score of Assessment.  
	if form["Total_Points_Overall"]!= None: form["Total_Points_Overall"].EditValue = Total_Points
		
if __loadStatus == LoadStatus.Loaded: Run(__form,__changedObject,__changeType,__loadStatus)
