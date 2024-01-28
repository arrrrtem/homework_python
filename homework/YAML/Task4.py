"""
Достаньте имя из словаря
"""

task = {
    "kluch1":[
        {"info1": "not name"},
        {
            "info2":{"still not name": "not name",
                     ("not name","oleg","another name"):"that what we need"
                     }
        }
    ]
}


# Достаем имя из словаря
name = task["kluch1"][1]["info2"][("not name","oleg","another name")]

# Вывод результата
print("Имя:", name)
