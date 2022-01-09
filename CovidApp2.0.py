import requests
import tkinter as tk
from tkinter import font

HEIGHT = 500
WIDTH = 600


def getStats(country,state):

	url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

	querystring = {"country":country}

	headers = {
	    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
	    'x-rapidapi-key': "489c6765f9msh34f1b5798d17b78p17966djsnb47152e47e8c"
	    }

	response = requests.request("GET", url, headers=headers, params=querystring)

	output = response.json()

	status = output['statusCode']

	data = output['data']['covid19Stats']

	dead = 0
	confirmed = 0
	recovered = 0

	for x in data:
		if x['province'] == state:
			dead = dead + x['deaths']
			confirmed = confirmed + x['confirmed']
			if type(x['recovered']) is int:
				recovered = recovered + x['recovered']
				

	answer = 'Deaths = %s \nConfirmed = %s' % (str(dead),str(confirmed))

	label['text'] = answer

	# print('Deaths: ' + str(dead))
	# print('Confirmed: ' + str(confirmed))
	#print('Recovered: ' + str(recovered))




root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# background_image = tk.PhotoImage(file='landscape.png')
# background_image = tk.Label(root, image=background_image)
# background_image.place(x=0, y=0, relwidth=1, relheight=1)
  
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75,relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relx=0.35, relwidth=0.65, relheight=1)

frame_2 = tk.Frame(root, bg='#80c1ff', bd=5)
frame_2.place(relx=0.5, rely=0.25, relwidth=0.75,relheight=0.1, anchor='n')

entry_2 = tk.Entry(frame_2, font=40)
entry_2.place(relx=0.35, relwidth=0.65, relheight=1)


button = tk.Button(root, text = "Search", font=('Courier',12), command=lambda: getStats(entry.get(),entry_2.get()))
button.place(relx=0.5,rely=0.38,relwidth=0.3,relheight=0.1, anchor='n')

lower_frame = tk.Frame(root,bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.4, anchor='n')

label = tk.Label(lower_frame, font=('Courier',18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)


message = tk.Message(frame,text="Country:", font=5)
message.place(relwidth=0.3, relheight=1)

message = tk.Message(frame_2,text="State:", font=5)
message.place(relwidth=0.3, relheight=1)

root.mainloop()


