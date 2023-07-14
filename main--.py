from web3 import Web3
import csv
from datetime import datetime

if __name__ == "__main__":

    # Define the CSV file path
    csv_file_path = 'transaction_data.csv'

    # Define the CSV field names
    field_names = ['Block Number', 'Timestamp', 'Transaction Hash', 'Nonce', 'Transaction Index', 'Sender', 'Receiver', 'Value', 'Gas Limit', 'Gas Price']
    
    # Open the CSV file in write mode
    with open(csv_file_path, mode='w+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)

        # Write the header row
        writer.writeheader()

        rpc_url = "https://eth-mainnet.g.alchemy.com/v2/w55KKVmfvP56Jz6ufadkT6UTJluYKalz"
        provider = Web3(Web3.HTTPProvider(rpc_url))
        contract_address = "0x6b175474e89094c44da98b954eedeac495271d0f"
        checksum_address = Web3.to_checksum_address(contract_address)
        contract_abi = [{"inputs":[{"internalType":"uint256","name":"chainId_","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"src","type":"address"},{"indexed":True,"internalType":"address","name":"guy","type":"address"},{"indexed":False,"internalType":"uint256","name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":True,"inputs":[{"indexed":True,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":True,"internalType":"address","name":"usr","type":"address"},{"indexed":True,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":True,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":False,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"src","type":"address"},{"indexed":True,"internalType":"address","name":"dst","type":"address"},{"indexed":False,"internalType":"uint256","name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":True,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"burn","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"guy","type":"address"}],"name":"deny","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"mint","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"move","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"holder","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"bool","name":"allowed","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"pull","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"push","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"guy","type":"address"}],"name":"rely","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]
        contract = provider.eth.contract(address=checksum_address, abi=contract_abi)
        # Calculate the block number for 60 days ago
        seconds_per_day = 24 * 60 * 60
        block_time = 15
        blocks_per_day = seconds_per_day // block_time
        current_block = provider.eth.block_number
        from_block = current_block - blocks_per_day * 60
        print(current_block, from_block)
        transactions = [] 
        i = 0
        while from_block <= current_block:
            to_block = from_block + 1900
            if to_block > current_block:
                to_block = current_block
            print(from_block, to_block)
            event_filter = contract.events.Transfer.create_filter(fromBlock=from_block, toBlock=to_block,  argument_filters={})
            events = provider.eth.get_filter_logs(event_filter.filter_id)
            tx_hashes = [event['transactionHash'].hex() for event in events]
            for tx_hash in tx_hashes:
                transaction = provider.eth.get_transaction(tx_hash)
                print(transaction['transactionIndex'])
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
            
            from_block = to_block + 1            

    print("Transaction data has been saved to", csv_file_path)    
