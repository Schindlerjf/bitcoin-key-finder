import blocksmith
import secrets

for n in range(0,20000):
            bits = secrets.randbits(256)
            bits_hex = hex(bits)
            private_key = bits_hex[2:]
            key = private_key
            car_len =len(key)

            if car_len == 64:
                address = blocksmith.BitcoinWallet.generate_address(key)
                print(address)
                arquivo = open(r'list-keys.txt','a')
                arquivo.write(address + '\n')
                arquivo.close()
                arquivo = open(r'compilado-public-private.txt','a')
                arquivo.write(key + '\n')
                arquivo.write(address + '\n')
                arquivo.close()
