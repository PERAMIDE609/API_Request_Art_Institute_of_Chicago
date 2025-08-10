import requests

def main():
    print("search the Art Institute of Chicago!")
    
    #Name of the specific artist you want to request for their artwork
    artist = input("Artist name: ")
    try:
        #Send a request to the Art Institute of Chichago
        response = requests.get("https://api.artic.edu/api/v1/artworks/search", {"q": artist})
        
        #check if the request works as intended
        response.raise_for_status()
    except request.HTTPError:
        print("Request could not be completed!")
        return
    
    content = response.json()

    for artwork in content["data"]:
        print(f"* {artwork['title']}")

if __name__ == "__main__":
    main()
