original_data = [
    {
        "name": "John Doe",
        "courses": [
            {
                "score": 76,
                "course": "Science"
            },
            {
                "score": 96,
                "course": "Maths"
            },
            {
                "score": 68,
                "course": "Nepali"
            }
        ]
    }
]

transformed_data = []

for person in original_data:
    name = person["name"]
    for course in person["courses"]:
        transformed_data.append({
            "name": name,
            "courses": [
                {
                    "score": course["score"],
                    "course": course["course"]
                }
            ]
        })

print(transformed_data)
