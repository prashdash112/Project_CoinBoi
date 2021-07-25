import hashlib

class neuralcoinblock:
    
    def __init__(self,previous_block_hash,transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        
        self.block_data = "/" + "/-&-/".join(transaction_list) + "/-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
# Sample transactions 
t1 = "Anna sends 20 NC to mike"
t2 = "bob sends 12.1 NC to mike"
t3 = "charlie sends 3.4 NC to Anna"
t4 = "prashdash sends 16.15 NC to drake"
t5 = "nick sends 5.342 NC to biky"
t6 = "krane sends 997.231 NC to shirley"

innitial_block = neuralcoinblock("Init_base",[t1,t2])
second_block = neuralcoinblock(innitial_block.block_hash,[t3,t4])
third_block = neuralcoinblock(second_block.block_hash,[t5,t6])
# Even changing a single value in transaction will result in a drastic change in all of the hashes of transactions & eventually 
# the later hashes will loose the base address & block chain got corrupted & the transaction will be lost forever. Because of 
# this, the blockchain hashes are permananet & untraceable

if __name__ == "__main__":
    
    print(innitial_block.block_data)
    print(innitial_block.block_hash)
    print('\n')
    print(second_block.block_data)
    print(second_block.block_hash)
    print('\n')
    print(third_block.block_data)
    print(third_block.block_hash)
    

        
