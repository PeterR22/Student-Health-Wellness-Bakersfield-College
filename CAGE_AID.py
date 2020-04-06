#-------------Name: Peter  Rodriguez 
#-------------Date: 03/30/2020
#-------------Information: This script counts the number of each response provided by
#-------------             patients from the CAGE-AID form. The total number of Yes/No responses
#-------------             are totaled to assist mental health providers in their methodology 
#-------------             for assessing/diagnosing their clients. 

def Run(form,changedObject,changeType,loadStatus):
	if changedObject.Name == None : return
	if changedObject.Name.StartsWith("q"):
		Count_Responses(form)

def Count_Responses(form):
	Number_of_Yes_Response = 0 
	Number_of_No_Response = 0
	for i in range(1,5):
		question = form["q"+str(i)]
		if question == None or question.EditValueAsString == "" : continue
		idx = question.Selections.IndexOf(question.CurrentSelection)
		if idx == 0: Number_of_Yes_Response+= 1
		if idx == 1: Number_of_No_Response+= 1

	if form["Total_Yes_Response"]!= None: form["Total_Yes_Response"].EditValue = Number_of_Yes_Response
	if form["Total_No_Response"]!= None: form["Total_No_Response"].EditValue = Number_of_No_Response

if __loadStatus == LoadStatus.Loaded: Run(__form,__changedObject,__changeType,__loadStatus)
