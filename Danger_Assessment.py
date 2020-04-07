#-------------Name: Peter Rodriguez 
#-------------Date: 05/28/2019 
#-------------Information: This script is for provider use when assessing 
#-------------             patients for the Danger Assessment. 
from MediaHighway.Common.BLL.Forms import *

def Run(form,changedObject,changeType,loadStatus):
	if changedObject.Name == None : return
	if changedObject.Name.StartsWith("W"):
		 DoCalc(form)

def DoCalc(form):
	t1 = 0
	t2 = 0
	t3 = 0
	t4 = 0
	t5 = 0
	t6 = 0
	danger_assessment_total = 0
	for i in range(1,12):
		question = form["W"+str(i)]
		if question == None or question.EditValueAsString == "" : continue
		idx = question.Selections.IndexOf(question.CurrentSelection)
		if idx == 0: t1+= 1
		if idx == 1: t1+= 0
	for i in range(1,3):
		question = form["E"+str(i)]
		if question == None or question.EditValueAsString == "" : continue
		idx = question.Selections.IndexOf(question.CurrentSelection)
		if idx == 0: t2+= 2
		if idx == 1: t2+= 0
	for i in range(1,4):
		question = form["R"+str(i)]
		if question == None or question.EditValueAsString == "" : continue
		idx = question.Selections.IndexOf(question.CurrentSelection)
		if idx == 0: t3+= 3
		if idx == 1: t3+= 0
	for i in range(1,3):
		question = form["T"+str(i)]
		if question == None or question.EditValueAsString == "" : continue
		idx = question.Selections.IndexOf(question.CurrentSelection)
		if idx == 0: t4+= 4
		if idx == 1: t4+= 0
	for i in range(1,2):
		question = form["Y"+str(i)]
		if question == None or question.EditValueAsString == "" : continue
		idx = question.Selections.IndexOf(question.CurrentSelection)
		if idx == 0: t5+= 5
		if idx == 1: t5+= 0
	for i in range(1,2):
		question = form["Z"+str(i)]
		if question == None or question.EditValueAsString == "" : continue
		idx = question.Selections.IndexOf(question.CurrentSelection)
		if idx == 0: t6-= 3
		if idx == 1: t6+= 0

	t7 = t1 + t2 + t3 + t4 + t5 + t6
	if form["t1"]!= None: form["t1"].EditValue = t1
	if form["t2"]!= None: form["t2"].EditValue = t2
	if form["t3"]!= None: form["t3"].EditValue = t3
	if form["t4"]!= None: form["t4"].EditValue = t4
	if form["t5"]!= None: form["t5"].EditValue = t5
	if form["t6"]!= None: form["t6"].EditValue = t6
	if form["t7"]!= None: form["t7"].EditValue = t7
