capitals = {
    "Francd": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris", "Dijon", "Bourdex"],
    "Russia": ["Moscow", "St Pitersburg", "Sochi"],
}

travle_log_expanded = {
    "France": { 
        "cities_visted": [
            {
                "Paris" : {
                    "vists": 4,
                    "amount_spent": 23.89
                }
            },
            { 
                "Dijon" : {
                    "vists": 4
                }
            },
            {
                "Bourdex": {
                    "vists": 12
                }
            }
        ],
    }
}

# Nesting dict in list

travle_log_expanded_expanded = [
    {
        "country": "France", 
        "cities_visted": ["Paris", "Dijon", "Bourdex"],
        "total_vists": 3,
    },
    {
        "country": "Russia", 
        "cities_visted": ["Moscow", "St Pitersburg", "Sochi"],
        "total_vists": 6,
    }
]