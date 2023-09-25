from cryptography.fernet import Fernet

# Generate a new key
key = Fernet.generate_key()

# Print the key
print(key.decode('utf-8'))