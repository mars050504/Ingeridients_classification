class_mapping = ["Bean", "Bitter_Gourd", "Bottle_Gourd", "Brinjal", "Broccoli", "Cabbage", "Capsicum", "Carrot", "Cauliflower", "Cucumber", "Papaya", "Potato", "Pumpkin", "Radish", "Tomato"]

ingredients_mapping = {
    "Tomato": [
      {
        "recipe_name": "Tomato Soup",
        "ingredients": [
          "2 ripe tomatoes",
          "1 onion",
          "2 garlic cloves",
          "1 cup vegetable broth",
          "Salt and pepper to taste",
          "1 tablespoon olive oil"
        ],
        "instructions": [
          "Heat olive oil in a pot and sauté chopped onion and garlic until soft.",
          "Add chopped tomatoes and cook for 5 minutes.",
          "Add vegetable broth and bring to a boil.",
          "Simmer for 10 minutes and season with salt and pepper.",
          "Blend the soup until smooth and serve hot."
        ]
      },
      {
        "recipe_name": "Tomato Salad",
        "ingredients": [
          "3 tomatoes",
          "1 cucumber",
          "1 tablespoon olive oil",
          "1 teaspoon lemon juice",
          "Salt and pepper to taste",
          "Fresh basil leaves"
        ],
        "instructions": [
          "Chop tomatoes and cucumber into bite-sized pieces.",
          "Toss the vegetables with olive oil and lemon juice.",
          "Season with salt, pepper, and fresh basil leaves.",
          "Serve chilled as a refreshing salad."
        ]
      }
    ],
    "Radish": [
      {
        "recipe_name": "Radish Salad",
        "ingredients": [
          "1 bunch of radishes",
          "1 tablespoon olive oil",
          "1 teaspoon lemon juice",
          "Salt and pepper to taste",
          "Fresh parsley"
        ],
        "instructions": [
          "Slice radishes thinly and place them in a bowl.",
          "Toss with olive oil, lemon juice, salt, and pepper.",
          "Garnish with fresh parsley and serve chilled."
        ]
      },
      {
        "recipe_name": "Radish Stir Fry",
        "ingredients": [
          "5 radishes",
          "1 tablespoon vegetable oil",
          "1 teaspoon soy sauce",
          "1 garlic clove",
          "1/2 teaspoon chili flakes",
          "Salt to taste"
        ],
        "instructions": [
          "Slice radishes into thin rounds.",
          "Heat vegetable oil in a pan and sauté chopped garlic.",
          "Add radishes and stir-fry for 5-7 minutes.",
          "Season with soy sauce, chili flakes, and salt.",
          "Serve hot as a side dish."
        ]
      }
    ],
    "Pumpkin": [
      {
        "recipe_name": "Pumpkin Soup",
        "ingredients": [
          "1 small pumpkin",
          "1 onion",
          "2 garlic cloves",
          "2 cups vegetable broth",
          "Salt and pepper to taste",
          "1 tablespoon olive oil"
        ],
        "instructions": [
          "Peel and chop the pumpkin into cubes.",
          "Sauté chopped onion and garlic in olive oil.",
          "Add pumpkin cubes and vegetable broth, bring to a boil.",
          "Simmer for 15 minutes, then blend the mixture until smooth.",
          "Season with salt and pepper and serve hot."
        ]
      },
      {
        "recipe_name": "Pumpkin Curry",
        "ingredients": [
          "1 small pumpkin",
          "1 onion",
          "1 tablespoon curry powder",
          "1 can coconut milk",
          "1 tablespoon olive oil",
          "Salt to taste"
        ],
        "instructions": [
          "Chop the pumpkin and onion into chunks.",
          "Heat olive oil in a pot and sauté onion.",
          "Add pumpkin and curry powder, cook for 5 minutes.",
          "Add coconut milk and simmer for 20 minutes.",
          "Season with salt and serve hot."
        ]
      }
    ],
    "Potato": [
      {
        "recipe_name": "Mashed Potatoes",
        "ingredients": [
          "4 potatoes",
          "1/2 cup milk",
          "2 tablespoons butter",
          "Salt and pepper to taste"
        ],
        "instructions": [
          "Peel and boil the potatoes until tender.",
          "Mash the potatoes and add milk and butter.",
          "Season with salt and pepper and serve warm."
        ]
      },
      {
        "recipe_name": "Potato Fries",
        "ingredients": [
          "4 potatoes",
          "1 tablespoon olive oil",
          "1 teaspoon paprika",
          "Salt to taste"
        ],
        "instructions": [
          "Preheat the oven to 400°F (200°C).",
          "Cut potatoes into thin strips and toss with olive oil and paprika.",
          "Spread on a baking sheet and bake for 25-30 minutes.",
          "Season with salt and serve."
        ]
      }
    ],
    "Papaya": [
      {
        "recipe_name": "Papaya Smoothie",
        "ingredients": [
          "1 ripe papaya",
          "1/2 cup coconut milk",
          "1 tablespoon honey",
          "Ice cubes"
        ],
        "instructions": [
          "Peel and chop the papaya into chunks.",
          "Blend papaya with coconut milk, honey, and ice cubes.",
          "Serve chilled in glasses."
        ]
      },
      {
        "recipe_name": "Papaya Salad",
        "ingredients": [
          "1 small papaya",
          "1/2 cucumber",
          "1 tablespoon lime juice",
          "1 tablespoon fish sauce",
          "Fresh cilantro"
        ],
        "instructions": [
          "Peel and shred the papaya.",
          "Chop cucumber into thin slices.",
          "Toss papaya and cucumber with lime juice and fish sauce.",
          "Garnish with fresh cilantro and serve."
        ]
      }
    ],
    "Cucumber": [
      {
        "recipe_name": "Cucumber Salad",
        "ingredients": [
          "1 cucumber",
          "1 tablespoon olive oil",
          "1 teaspoon lemon juice",
          "Fresh dill",
          "Salt and pepper to taste"
        ],
        "instructions": [
          "Slice the cucumber thinly and place it in a bowl.",
          "Toss with olive oil, lemon juice, dill, salt, and pepper.",
          "Serve chilled."
        ]
      },
      {
        "recipe_name": "Cucumber Sandwiches",
        "ingredients": [
          "1 cucumber",
          "Bread slices",
          "Cream cheese",
          "Fresh dill",
          "Salt and pepper"
        ],
        "instructions": [
          "Slice cucumber thinly.",
          "Spread cream cheese on bread slices.",
          "Layer with cucumber slices, and sprinkle with fresh dill.",
          "Season with salt and pepper and serve as a sandwich."
        ]
      }
    ],
    "Cauliflower": [
      {
        "recipe_name": "Cauliflower Rice",
        "ingredients": [
          "1 cauliflower head",
          "1 tablespoon olive oil",
          "Salt and pepper to taste"
        ],
        "instructions": [
          "Grate cauliflower into rice-sized pieces.",
          "Heat olive oil in a pan and sauté cauliflower rice for 5-7 minutes.",
          "Season with salt and pepper and serve."
        ]
      },
      {
        "recipe_name": "Roasted Cauliflower",
        "ingredients": [
          "1 cauliflower head",
          "2 tablespoons olive oil",
          "1 teaspoon garlic powder",
          "Salt and pepper to taste"
        ],
        "instructions": [
          "Preheat the oven to 400°F (200°C).",
          "Cut cauliflower into florets and toss with olive oil, garlic powder, salt, and pepper.",
          "Spread on a baking sheet and roast for 25-30 minutes.",
          "Serve hot."
        ]
      }
    ],
    "Carrot": [
      {
        "recipe_name": "Carrot Soup",
        "ingredients": [
          "4 carrots",
          "1 onion",
          "2 garlic cloves",
          "2 cups vegetable broth",
          "Salt and pepper to taste"
        ],
        "instructions": [
          "Peel and chop the carrots.",
          "Sauté onion and garlic in a pot until soft.",
          "Add carrots and vegetable broth, bring to a boil.",
          "Simmer for 15-20 minutes, then blend until smooth.",
          "Season with salt and pepper and serve."
        ]
      },
      {
        "recipe_name": "Carrot Salad",
        "ingredients": [
          "2 carrots",
          "1 tablespoon olive oil",
          "1 teaspoon lemon juice",
          "Salt and pepper to taste",
          "Fresh parsley"
        ],
        "instructions": [
          "Grate the carrots.",
          "Toss with olive oil, lemon juice, salt, and pepper.",
          "Garnish with fresh parsley and serve."
        ]
      }
    ],
    "Capsicum": [
      {
        "recipe_name": "Stuffed Capsicum",
        "ingredients": [
          "4 capsicum peppers",
          "1 cup cooked rice",
          "1 onion",
          "1 can diced tomatoes",
          "1 teaspoon garlic powder",
          "Salt and pepper to taste"
        ],
        "instructions": [
          "Cut the tops off capsicum peppers and remove seeds.",
          "Mix cooked rice, diced tomatoes, onion, garlic powder, salt, and pepper.",
          "Stuff the peppers with the rice mixture.",
          "Bake at 350°F (175°C) for 20-25 minutes."
        ]
      },
      {
        "recipe_name": "Grilled Capsicum",
        "ingredients": [
          "4 capsicum peppers",
          "1 tablespoon olive oil",
          "Salt and pepper to taste"
        ],
        "instructions": [
          "Slice the capsicum peppers into strips.",
          "Toss with olive oil, salt, and pepper.",
          "Grill for 5-7 minutes until charred and tender."
        ]
      }
    ],
    "Cabbage": [
      {
        "recipe_name": "Cabbage Stir Fry",
        "ingredients": [
          "1/2 head of cabbage",
          "2 tablespoons soy sauce",
          "1 teaspoon sesame oil",
          "1 tablespoon olive oil",
          "Salt and pepper to taste"
        ],
        "instructions": [
          "Shred the cabbage.",
          "Heat olive oil in a pan and sauté cabbage for 5-7 minutes.",
          "Add soy sauce and sesame oil."
        ]
      }
    ],
    "Broccoli": [
      {
        "recipe_name": "Steamed Broccoli",
        "ingredients": [
          "1 head of broccoli",
          "Salt to taste",
          "1 tablespoon olive oil"
        ],
        "instructions": [
          "Cut broccoli into florets.",
          "Steam the florets for 5-7 minutes until tender.",
          "Toss with olive oil and season with salt."
        ]
      },
      {
        "recipe_name": "Broccoli Stir Fry",
        "ingredients": [
          "1 head of broccoli",
          "1 tablespoon soy sauce",
          "1 tablespoon sesame oil",
          "1 garlic clove",
          "1 teaspoon ginger"
        ],
        "instructions": [
          "Cut broccoli into florets.",
          "Heat sesame oil in a pan and sauté garlic and ginger.",
          "Add broccoli and stir-fry for 5-7 minutes.",
          "Season with soy sauce and serve."
        ]
      }
    ],
    "Brinjal": [
      {
        "recipe_name": "Brinjal Curry",
        "ingredients": [
          "2 brinjals",
          "1 onion",
          "1 can diced tomatoes",
          "1 tablespoon curry powder",
          "1/2 teaspoon turmeric",
          "1 tablespoon olive oil",
          "Salt to taste"
        ],
        "instructions": [
          "Cut brinjal into cubes.",
          "Heat olive oil in a pan and sauté chopped onion.",
          "Add brinjal, curry powder, turmeric, and diced tomatoes.",
          "Simmer for 15-20 minutes, season with salt, and serve."
        ]
      },
      {
        "recipe_name": "Grilled Brinjal",
        "ingredients": [
          "2 brinjals",
          "1 tablespoon olive oil",
          "Salt and pepper to taste"
        ],
        "instructions": [
          "Slice brinjal into thick rounds.",
          "Brush with olive oil and season with salt and pepper.",
          "Grill for 5-7 minutes on each side until soft."
        ]
      }
    ],
    "Bottle_Gourd": [
      {
        "recipe_name": "Bottle Gourd Curry",
        "ingredients": [
          "1 bottle gourd",
          "1 onion",
          "2 tomatoes",
          "1 tablespoon curry powder",
          "1 teaspoon cumin seeds",
          "1 tablespoon olive oil",
          "Salt to taste"
        ],
        "instructions": [
          "Peel and chop bottle gourd into cubes.",
          "Heat olive oil in a pan and sauté cumin seeds and chopped onion.",
          "Add tomatoes, curry powder, and bottle gourd.",
          "Simmer for 15-20 minutes, season with salt, and serve."
        ]
      },
      {
        "recipe_name": "Bottle Gourd Soup",
        "ingredients": [
          "1 bottle gourd",
          "1 onion",
          "2 garlic cloves",
          "1 teaspoon ginger",
          "2 cups vegetable broth",
          "Salt and pepper to taste"
        ],
        "instructions": [
          "Peel and chop bottle gourd into cubes.",
          "Sauté onion, garlic, and ginger in olive oil.",
          "Add bottle gourd and vegetable broth.",
          "Simmer for 15 minutes, blend until smooth, and season with salt and pepper."
        ]
      }
    ],
    "Bitter_Gourd": [
      {
        "recipe_name": "Bitter Gourd Stir Fry",
        "ingredients": [
          "2 bitter gourds",
          "1 onion",
          "1 teaspoon turmeric",
          "1 teaspoon chili powder",
          "1 tablespoon olive oil",
          "Salt to taste"
        ],
        "instructions": [
          "Slice bitter gourd and remove seeds.",
          "Sauté onion in olive oil, then add bitter gourd.",
          "Sprinkle turmeric, chili powder, and salt.",
          "Stir-fry for 10-15 minutes and serve."
        ]
      },
      {
        "recipe_name": "Bitter Gourd Chips",
        "ingredients": [
          "2 bitter gourds",
          "1 tablespoon olive oil",
          "Salt and pepper to taste"
        ],
        "instructions": [
          "Slice bitter gourd thinly and remove seeds.",
          "Toss with olive oil, salt, and pepper.",
          "Bake at 350°F (175°C) for 20-25 minutes until crispy."
        ]
      }
    ],
    "Bean": [
      {
        "recipe_name": "Baked Beans",
        "ingredients": [
          "2 cups kidney beans (or any type of beans)",
          "1 tablespoon olive oil",
          "1 onion, chopped",
          "2 cloves garlic, minced",
          "1 can diced tomatoes",
          "1 tablespoon brown sugar",
          "1 tablespoon molasses",
          "1 tablespoon mustard",
          "1 tablespoon Worcestershire sauce",
          "1 teaspoon paprika",
          "Salt and pepper to taste"
        ],
        "instructions": [
          "Soak the beans overnight, then cook them until tender (about 1-2 hours).",
          "Preheat the oven to 350°F (175°C).",
          "Heat olive oil in a pan, sauté onions and garlic until soft.",
          "Add diced tomatoes, brown sugar, molasses, mustard, Worcestershire sauce, paprika, and season with salt and pepper.",
          "Mix in the cooked beans, transfer to a baking dish, and bake for 30-40 minutes."
        ]
      },
      {
        "recipe_name": "Bean Salad",
        "ingredients": [
          "2 cups mixed beans (kidney beans, black beans, chickpeas)",
          "1 cucumber, diced",
          "1 bell pepper, diced",
          "1 small red onion, diced",
          "1 tablespoon olive oil",
          "1 tablespoon lemon juice",
          "1 teaspoon cumin",
          "Salt and pepper to taste",
          "Fresh cilantro for garnish"
        ],
        "instructions": [
          "Rinse and drain the beans.",
          "In a large bowl, mix the beans with cucumber, bell pepper, and red onion.",
          "In a separate small bowl, whisk together olive oil, lemon juice, cumin, salt, and pepper.",
          "Pour the dressing over the salad, toss gently, and garnish with fresh cilantro."
        ]
      }
    ]
  }