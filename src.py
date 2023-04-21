import tkinter as tk

# Define the global variables
votesID = [0,1,2,3,4,5]
Can1Voters = 0
Can2Voters = 0

# Create a new window
window = tk.Tk()
window.title("Online Eliction System")
window.geometry("400x400")
tk.Label(window, text="Election System")



# Add labels and entry fields for candidate names and election ID
tk.Label(window, text="Election System", font=("Helvetica", 24, "bold"), fg="white", bg="#2c3e50").grid(row=0)
tk.Label(window, text="").grid(row=1)
tk.Label(window, text="First candidate name:").grid(row=2)
tk.Label(window, text="").grid(row=3)
tk.Label(window, text="Second candidate name:").grid(row=4)
tk.Label(window, text="").grid(row=5)
tk.Label(window, text="Election ID:").grid(row=6)
tk.Label(window, text="").grid(row=7)
tk.Label(window, text="Select a candidate:").grid(row=8)
tk.Label(window, text="").grid(row=9)

candidate1_entry = tk.Entry(window)
candidate2_entry = tk.Entry(window)
voter_entry = tk.Entry(window)
vote_entry = tk.Entry(window)

candidate1_entry.grid(row=2, column=1)
candidate2_entry.grid(row=4, column=1)
voter_entry.grid(row=6, column=1)
vote_entry.grid(row=8, column=1 )

# Add labels for the candidates
tk.Label(window, text="1:").grid(row=10, column=0, sticky=tk.E)
tk.Label(window, text=candidate1_entry.get()).grid(row=4, column=1, sticky=tk.W)
tk.Label(window, text="2:").grid(row=11, column=0, sticky=tk.E)
tk.Label(window, text=candidate2_entry.get()).grid(row=5, column=1, sticky=tk.W)

# Add buttons for submitting the vote and displaying the results
def submit_vote():
    global votesID, Can1Voters, Can2Voters  # Declare the global variables
    voter_id = int(voter_entry.get())
    if voter_id in votesID:
        votesID.remove(voter_id)
        vote = int(vote_entry.get())
        if vote == 1:
            Can1Voters += 1
        elif vote == 2:
            Can2Voters += 1
        vote_entry.delete(0, tk.END)
        voter_entry.delete(0, tk.END)
    else:
        print("You are not a voter here or you already voted")

submit_button = tk.Button(window, text="Submit Vote", command=submit_vote)
submit_button.grid(row=18, column=0)

def display_results():
    if(Can1Voters > Can2Voters):
        result = (Can1Voters /5) * 100
        tk.Label(window, text="First candidate has won with"+str(result)+"%" ).grid(row=20, column=0, sticky=tk.E)
        # tk.Label(window, text=str(result)+"%").grid(row=20, column=1, sticky=tk.E)
    elif(Can2Voters > Can1Voters):
        result = (Can2Voters /5) * 100
        tk.Label(window, text= "Second candidate has won with"+str(result)+"%" ).grid(row=20, column=0, sticky=tk.E)
        # tk.Label(window, text=str(result)+"%").grid(row=20, column=1, sticky=tk.E)
    else:
        print("The election is tied")

results_button = tk.Button(window, text="Display Results", command=display_results)
results_button.grid(row=18, column=1)

# Start the GUI event loop
window.mainloop()


