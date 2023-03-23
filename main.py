import importlib

scripts = [
    ["exit", "", ""],
    ["dummy", "dummy_job", "jobs"],
    ["fishing", "fishing_job", "jobs"],
    ["afk-bot", "afk-bot_job", "jobs"],
    ["stone-mining", "stone-mining_job", "jobs"],
    ["electric", "electric_job", "jobs"],
    ["oil-pump", "oil-pump_job", "jobs"],
    ["race-start", "race-start_action", "actions"],
    ["shortcut", "shortcut_action", "actions"]
]

while True:
    for index, each in enumerate(scripts):
        print("Select", index, "for", each[0])

    try:
        selection = input(">")
        to_number = int(selection)
        if to_number == 0:
            print("exit")
            exit(0)
        print("Start ", scripts[to_number][0])
        # https://docs.python.org/3/library/importlib.html#importlib.import_module
        job_module = scripts[to_number][2] + "." + scripts[to_number][1]
        importlib.__import__(job_module)
    except IndexError:
        print("Invalid input ")
        exit(0)
