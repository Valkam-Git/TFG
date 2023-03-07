import processing
import scraping


def main(location='Cáceres'):
    # delete the current data from MongoDB
    processing.delete_from_mongo()
    
    # Get the data from the web
    data = scraping.scrape(location)

    # Process the data
    data = processing.preprocess_data(data)

    # Save the data to a file
    processing.save_to_csv(data)
    processing.save_to_json(data)

    # Save the data to MongoDB
    processing.save_to_mongo(data)

if __name__ == '__main__':
    main()