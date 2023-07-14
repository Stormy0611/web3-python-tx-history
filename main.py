from web3 import Web3
import csv
import glob
from datetime import datetime
import threading
import time

def scraper(from_block, to_block, id):

    # Define the CSV file path
    csv_file_path = f'transaction_data{id}_{from_block}_{to_block - 1}.csv'

    # Define the CSV field names
    field_names = ['Block Number', 'Timestamp', 'Transaction Hash', 'Nonce', 'Transaction Index', 'Sender', 'Receiver', 'Value', 'Gas Limit', 'Gas Price']
    
    # Open the CSV file in write mode
    with open(csv_file_path, mode='w+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)

        # Write the header row
        writer.writeheader()

        print(id, from_block, to_block + 1)
        # for block in range(from_block, to_block, -1):
        #     # Retrieve the block data using the `get_block()` method
        #     block_data = provider.eth.get_block(block)
        #     # Access the list of transactions from the block data
        #     transactions = block_data.transactions
        #     # Get Dai token's transactions
        #     dai_token_address = '0x6b175474e89094c44da98b954eedeac495271d0f'
        #     # Filter transactions by the token's address
        #     dai_transactions = [tx for tx in transactions if tx.to.lower() == dai_token_address.lower()]

        #     # Print each Dai token transaction hash
        #     for tx_hash in dai_transactions:
        #         print(f"Dai Transaction Hash: {tx_hash.hex()}")


        logs = provider.eth.get_logs({
            'fromBlock': to_block,
            'toBlock': from_block,
            'address': checksum_address
        })
        for log in logs:
            tx_hash = log['transactionHash'].hex()
            transaction = provider.eth.get_transaction(tx_hash)
            # Write the transaction details to the CSV file
            writer.writerow({
                'Block Number': transaction['blockNumber'],
                'Timestamp': datetime.fromtimestamp(provider.eth.get_block(transaction['blockNumber'])['timestamp']).isoformat(),
                'Transaction Hash': str(transaction['hash']),
                'Nonce': transaction['nonce'],
                'Transaction Index': transaction['transactionIndex'],
                'Sender': transaction['from'],
                'Receiver': transaction['to'],
                'Value': transaction['value'],
                'Gas Limit': transaction['gas'],
                'Gas Price': transaction['gasPrice']
            })

    print("Transaction data has been saved", id)


if __name__ == "__main__":

    global provider, checksum_address

    # Connect to the Ethereum mainnet using Infura
    provider = Web3(Web3.HTTPProvider('https://eth-mainnet.g.alchemy.com/v2/8x3VNb3cmLygheS2tLxDjp_HpSG9XDGh'))

    # Specify the contract address of the Dai token
    dai_contract_address = "0x6b175474e89094c44da98b954eedeac495271d0f"
    checksum_address = Web3.to_checksum_address(dai_contract_address)

    # Calculate the block number from 60 days ago
    block_number = provider.eth.block_number
    block_number_60_days_ago = block_number - 5760 * 60  # Assuming 15-second block time

    # Retrieve the transaction history using the `get_logs()` method
    # from_block = block_number
    from_block = 17691514
    threads = []
    idx = 1
    while from_block >= block_number_60_days_ago:
        if from_block == block_number_60_days_ago:
            break
        to_block = from_block - 2000
        if to_block < block_number_60_days_ago:
            to_block = block_number_60_days_ago
        # Create a thread passing parameters
        thread = threading.Thread(target=scraper, args=(from_block, to_block, idx))
        # Start the thread
        thread.start()
        threads.append(thread)
        thread.join()
        from_block = to_block
        idx = idx + 1

    # # Wait for the thread to finish
    # for thread in threads:
    #     thread.join()
    
    # Specify the path to the directory containing the CSV files
    csv_files_path = './*.csv'

    # Get a list of all CSV file paths in the directory
    csv_files = glob.glob(csv_files_path)

    # Specify the path and filename for the combined CSV file
    combined_csv_path = './combined_file.csv'

    # Open the combined CSV file in write mode
    with open(combined_csv_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        
        # Iterate over each CSV file
        for file in csv_files:
            # Open the CSV file
            with open(file, 'r') as infile:
                reader = csv.reader(infile)
                
                # Iterate over each row in the CSV file
                for row in reader:
                    # Write the row to the combined CSV file
                    writer.writerow(row)

    print("CSV files combined successfully!")
