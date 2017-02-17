import time, lightspeed_client, db_client, logging

logging.basicConfig(filename='ls2sql.log', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

def main():
    logging.info('Application started.')

    # Retrieve store information
    stores = db_client.get_store_list()

    # Loop through stores to process
    #for store in stores:
        # lightspeed_client.proccess_store(store)

    logging.info('Application ended')

if __name__ == '__main__':
    main()
