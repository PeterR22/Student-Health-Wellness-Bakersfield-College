#-------------Name: Peter  Rodriguez 
#-------------Date: 03/30/2020
#-------------Information: This script counts the number of each response provided by
#-------------             patients from the SCL-90 form. The total number of Yes/No responses
#-------------             are totaled to assist mental health providers in their methodology 
#-------------             for assessing/diagnosing their clients. 

def Run(form,changedObject,changeType,loadStatus):
	if changedObject.Name == None : return
	if changedObject.Name.StartsWith("q"):
		Count_SCL90_Responses(form)

def Count_SCL90_Responses(form):
  Number_of_Not_At_All_Response = 0 
	Number_of_A_Little_Bit_Response = 0
  Number_of_Moderately_Response = 0
  Number_of_Quite_A_Bit_Response = 0
  Number_of_Extremely_Response = 0
  
  Not_At_All_Response_Value = 0 
  A_Little_Bit_Response_Value = 1
  Moderately_Response_Value = 2
  Quite_A_Bit_Response_Value = 3
  Extremely_Response_Value = 4
	
	Points_Accumulated_Not_At_All_Response = 0   
	Points_Accumulated_A_Little_Bit_Response = 0 
  Points_Accumulated_Moderately_Response = 0
  Points_Accumulated_Quite_A_Bit_Response = 0 
  Points_Accumulated_Extremely_Response = 0
	
	Total_Points_Accumulated_Not_At_All_Response = 0   
	Total_Points_Accumulated_A_Little_Bit_Response = 0 
  Total_Points_Accumulated_Moderately_Response = 0
  Total_Points_Accumulated_Quite_A_Bit_Response = 0 
  Total_Points_Accumulated_Extremely_Response = 0
	
	Total_Points = 0
	Total_Points_Overall = 0
	
  
	for i in range(1,91):
		question = form["q"+str(i)]
		if question == None or question.EditValueAsString == "" : continue
		idx = question.Selections.IndexOf(question.CurrentSelection)
		if idx == 0: Number_of_Not_At_All_Response+= 1
		if idx == 1: Number_of_A_Little_Bit_Response+= 1
    if idx == 2: Number_of_Moderately_Response+= 1
    if idx == 3: Number_of_Quite_A_Bit_Response+= 1
    if idx == 4: Number_of_Extremely_Response+= 1
	
	Points_Accumulated_Not_At_All_Response = Number_of_Not_At_All_Response*Not_At_All_Response_Value  
	Points_Accumulated_A_Little_Bit_Response = Number_of_A_Little_Bit_Response*A_Little_Bit_Response_Value
  Points_Accumulated_Moderately_Response = Number_of_Moderately_Response*Moderately_Response_Value
  Points_Accumulated_Quite_A_Bit_Response = Number_of_Quite_A_Bit_Response*Quite_A_Bit_Response_Value
  Points_Accumulated_Extremely_Response = Number_of_Extremely_Response*Extremely_Response_Value
	
	Total_Points = Points_Accumulated_Not_At_All_Response+Points_Accumulated_A_Little_Bit_Response+Points_Accumulated_Moderately_Response+Points_Accumulated_Quite_A_Bit_Response+Points_Accumulated_Extremely_Response
	
	if form["Total_Number_of_Not_At_All_Response"]!= None: form["Total_Number_of_Not_At_All_Response"].EditValue = Number_of_Not_At_All_Response
	if form["Total_Number_of_A_Little_Bit_Response"]!= None: form["Total_Number_of_A_Little_Bit_Response"].EditValue = Number_of_A_Little_Bit_Response
	if form["Total_Number_of_Moderately_Response"]!= None: form["Total_Number_of_Moderately_Response"].EditValue = Number_of_Moderately_Response
	if form["Total_Number_of_Quite_A_Bit_Response"]!= None: form["Total_Number_of_Quite_A_Bit_Response"].EditValue = Number_of_Quite_A_Bit_Response
	if form["Total_Number_of_Extremely_Response"]!= None: form["Total_Number_of_Extremely_Response"].EditValue = Number_of_Extremely_Response	
	
	if form["Total_Points_Accumulated_Not_At_All_Response"]!= None: form["Total_Points_Accumulated_Not_At_All_Response"].EditValue = Points_Accumulated_Not_At_All_Response
	if form["Total_Points_Accumulated_A_Little_Bit_Response"]!= None: form["Total_Points_Accumulated_A_Little_Bit_Response"].EditValue = Points_Accumulated_A_Little_Bit_Response
	if form["Total_Points_Accumulated_Moderately_Response"]!= None: form["Total_Points_Accumulated_Moderately_Response"].EditValue = Points_Accumulated_Moderately_Response
	if form["Total_Points_Accumulated_Quite_A_Bit_Response"]!= None: form["Total_Points_Accumulated_Quite_A_Bit_Response"].EditValue = Points_Accumulated_Quite_A_Bit_Response
	if form["Total_Points_Accumulated_Extremely_Response"]!= None: form["Total_Points_Accumulated_Extremely_Response"].EditValue = Points_Accumulated_Extremely_Response
	
	if form["Total_Points_Overall"]!= None: form["Total_Points_Overall"].EditValue = Total_Points
		
if __loadStatus == LoadStatus.Loaded: Run(__form,__changedObject,__changeType,__loadStatus)
