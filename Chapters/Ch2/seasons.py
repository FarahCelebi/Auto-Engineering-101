"""" Challenge 2

Write a program, with Scenarios and Tests, that does the following:

1. Ask the user to enter a Season
2. Using this input, create the logic to handle different Seasons:

* If the input is "winter", print "snow"
* If the input is "spring", print "flowers"
* If the input is "summer", print "beach"
* If the input is "fall" or "autumn", print "leaves"
* If the input is anything else, print "I don't know that season"
"""
def get_season_response(season):
    season = season.lower()
    if season == "winter":
        return "snow"
    elif season == "spring":
        return "flowers"
    elif season == "summer":
        return "beach"
    elif season in ["fall", "autumn"]:
        return "leaves"
    else:
        return "I don't know that season"

def main():
    season = input("Enter a season: ")
    response = get_season_response(season)
    print(response)

if __name__ == "__main__":
    main()