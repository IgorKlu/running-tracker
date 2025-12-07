import json

runs = []


def add_run(): #asking about data, distance, time, tempo, dictionary, adding to 'runs'
    date = input("Input the date: ")
    distance = float(input("Input distance: "))
    time_min = float(input("input time (in minutes): "))
    pace = time_min / distance
    traindict = {
        "date" : date,
        "distance" : distance,
        "time_min" : time_min,
        "pace" : pace
    }
    runs.append(traindict)
    print("Run added succesfully.\n")

def show_runs(): # Checking if the list isn't empty then showing runs 
    if len(runs) == 0:
        print("There is no trainings saved yet.")
        return
    else:    
        for index, run in enumerate(runs, start=1):
            print(f"\nRun {index:}")
            print(f"  Date:         {run["date"]}")
            print(f"  Distance:     {run["distance"]} km")
            print(f"  Time:         {run["time_min"]} min")
            print(f"  Pace          {run["pace"]} min/km\n")

def show_stats(): # Checking if the list isn't empty and sumarising stats
    if len (runs) == 0:
        print("There are no stats to show.")
    else:
        paces = []
        total_distance = 0
        total_time = 0
        fastest = float("inf")
        longest = 0
        for run in runs:
            
            paces.append(run["pace"])

            total_distance += run["distance"]

            total_time += run["time_min"]

            if run["distance"] > longest:
                longest = run["distance"]

            if run["pace"] < fastest:
                fastest = run["pace"]
        average_pace = sum(paces) / len(paces)

        print(f"Average pace: {average_pace} \nTotal distance: {total_distance} \nTotal time: {total_time} \nLongest run: {longest} \nFastest run: {fastest}")

def save_runs():
    with open("runs.json", "w", encoding="utf-8") as file:
        json.dump(runs, file, ensure_ascii=False, indent=2)
    print("Runs saved.")

def load_runs():
    try:
        with open("runs.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            runs.clear()
            runs.extend(data)
            print("Runs loaded")
    except FileNotFoundError:
        print("No saved runs found.")
        
load_runs()

while True:
    print("Menu: \n- Add run - choose 1 \n- Show all trainings - choose 2 \n- Show stats - choose 3 \n- save and leave - choose 4 " )
    option = int(input("\nChoose an option: "))

    if option == 1:
        add_run()
    elif option == 2:
        show_runs()
    elif option == 3:
        show_stats()
    elif option == 4:
        save_runs()
        break




