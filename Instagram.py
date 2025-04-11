import instaloader
from urllib.request import urlretrieve
import os

# Your WhatsApp Channel link
WHATSAPP_CHANNEL_LINK = "https://whatsapp.com/channel/0029VaeFfpxI1rcjigntom0h"

# Hacker-style banner for Ali_Hacker_95
print("\033[1;31m" + r"""
   _____ _    _ ______  _____ 
  / ____| |  | |  ____|/ ____|
 | |    | |__| | |__  | (___  
 | |    |  __  |  __|  \___ \ 
 | |____| |  | | |____ ____) |
  \_____|_|  |_|______|_____/ 
         Ali_Hacker_95
Tool Created by TRB
""" + "\033[0m")
print("\033[1;32m[*] Deployed - Ready to Infiltrate 🌚💗\033[0m")

# Redirect to WhatsApp Channel when the tool starts
print("\033[1;33m[*] Redirecting to Ali_Hacker_95's WhatsApp Channel...\033[0m")
os.system(f"termux-open-url {WHATSAPP_CHANNEL_LINK}")

# Expanded OSINT data for public accounts (placeholder values)
osint_data = {
    'nasa': {
        'Target IP': '192.168.1.1',
        'IP Location': 'USA',
        'Email': 'info@nasa.gov',
        'Account Creation Date': '2007-10-01',
        'Former Username': 'nasa_official',
        'Flagged Account': 'No'
    },
    'natgeo': {
        'Target IP': '192.168.1.2',
        'IP Location': 'USA',
        'Email': 'contact@natgeo.com',
        'Account Creation Date': '2012-03-15',
        'Former Username': 'nationalgeographic',
        'Flagged Account': 'No'
    },
    'bbcnews': {
        'Target IP': '192.168.1.3',
        'IP Location': 'UK',
        'Email': 'news@bbc.co.uk',
        'Account Creation Date': '2007-04-20',
        'Former Username': 'bbc_news',
        'Flagged Account': 'No'
    },
    'teslamotors': {
        'Target IP': '192.168.1.4',
        'IP Location': 'USA',
        'Email': 'info@tesla.com',
        'Account Creation Date': '2007-06-10',
        'Former Username': 'tesla_official',
        'Flagged Account': 'No'
    },
    'nike': {
        'Target IP': '192.168.1.5',
        'IP Location': 'USA',
        'Email': 'support@nike.com',
        'Account Creation Date': '2010-01-25',
        'Former Username': 'nikeofficial',
        'Flagged Account': 'No'
    },
    'trb_official': {
        'Target IP': '192.168.1.6',
        'IP Location': 'Unknown',
        'Email': 'contact@trbowner.com',
        'Account Creation Date': '2015-08-20',
        'Former Username': 'trb_hq',
        'Flagged Account': 'No'
    },
    'ali_hacker_95': {
        'Target IP': '192.168.1.7',
        'IP Location': 'Unknown',
        'Email': 'alihacker95@example.com',
        'Account Creation Date': '2018-04-11',
        'Former Username': 'ali_hacker_official',
        'Flagged Account': 'No'
    }
}

# Initialize instaloader
L = instaloader.Instaloader()

# Function to process a single user's OSINT data
def process_user(username):
    print(f"\n\033[1;32m[*] Infiltrating @{username}...\033[0m")

    # Get OSINT data, default to Unknown
    custom_info = osint_data.get(username, {
        'Target IP': 'Unknown',
        'IP Location': 'Unknown',
        'Email': 'Unknown',
        'Account Creation Date': 'Unknown',
        'Former Username': 'Unknown',
        'Flagged Account': 'Unknown'
    })

    # Extract Account Create Year from Account Creation Date
    account_create_year = "Unknown"
    if custom_info['Account Creation Date'] != 'Unknown':
        try:
            account_create_year = custom_info['Account Creation Date'].split('-')[0]
        except:
            account_create_year = "Unknown"

    try:
        # Load profile data with instaloader
        profile = instaloader.Profile.from_username(L.context, username)

        # Display profile intel
        print(f"\n\033[1;32m[+] Extracting Intel for @{username}\033[0m")
        print(f"\033[1;36mUsername:\033[0m {profile.username}")
        print(f"\033[1;36mFull Name:\033[0m {profile.full_name}")
        print(f"\033[1;36mBio:\033[0m {profile.biography}")
        print(f"\033[1;36mStatus:\033[0m {'Private' if profile.is_private else 'Public'}")
        print(f"\033[1;36mFollowers:\033[0m {profile.followers}")
        print(f"\033[1;36mFollowing:\033[0m {profile.followees}")
        print(f"\033[1;36mPosts:\033[0m {profile.mediacount}")
        print(f"\033[1;36mIGTV:\033[0m {profile.igtvcount}")
        print(f"\033[1;36mAccount Create Year:\033[0m {account_create_year}")
        print(f"\033[1;36mProfile Pic URL:\033[0m {profile.profile_pic_url}")

        # OSINT Data
        print(f"\n\033[1;31m[#] OSINT Findings:\033[0m")
        print(f"\033[1;36mTarget IP:\033[0m {custom_info['Target IP']}")
        print(f"\033[1;36mIP Location:\033[0m {custom_info['IP Location']}")
        print(f"\033[1;36mEmail (OSINT):\033[0m {custom_info['Email']}")
        print(f"\033[1;36mCreation Date:\033[0m {custom_info['Account Creation Date']}")
        print(f"\033[1;36mFormer Username:\033[0m {custom_info['Former Username']}")
        print(f"\033[1;36mFlagged:\033[0m {custom_info['Flagged Account']}")

        return True

    except Exception as e:
        print(f"\033[1;31m[!] Mission Failed for @{username}: {e}\033[0m")
        print("\033[1;33m[Tip] Check if the username exists or is public.\033[0m")
        return False

# Function to search users by hashtag
def search_by_hashtag(hashtag, max_users=5):
    print(f"\n\033[1;32m[*] Searching for users associated with #{hashtag}...\033[0m")
    try:
        posts = instaloader.Hashtag.from_name(L.context, hashtag).get_posts()
        users = set()
        for post in posts:
            if len(users) >= max_users:
                break
            users.add(post.owner_username)
        return list(users)
    except Exception as e:
        print(f"\033[1;31m[!] Failed to search hashtag #{hashtag}: {e}\033[0m")
        return []

# Main menu
print("\n\033[1;33m[1] Process a List of Usernames\033[0m")
print("\033[1;33m[2] Search Users by Hashtag\033[0m")
print("\033[1;33m[3] Follow Ali_Hacker_95 on WhatsApp Channel\033[0m")
choice = input("\033[1;33m[>] Select Operation (1-3): \033[0m").strip()

if choice == "1":
    # Option 1: Process a list of usernames
    usernames_input = input("\033[1;33m[>] Enter Instagram Usernames (comma-separated, e.g., user1,user2,user3): \033[0m").strip()
    usernames = [u.strip() for u in usernames_input.split(",") if u.strip()]
    
    if not usernames:
        print("\033[1;31m[!] No usernames provided.\033[0m")
    else:
        print(f"\033[1;32m[*] Processing {len(usernames)} usernames...\033[0m")
        for username in usernames:
            process_user(username)

elif choice == "2":
    # Option 2: Search users by hashtag
    hashtag = input("\033[1;33m[>] Enter Hashtag (without #, e.g., cybersecurity): \033[0m").strip()
    if not hashtag:
        print("\033[1;31m[!] No hashtag provided.\033[0m")
    else:
        users = search_by_hashtag(hashtag, max_users=5)
        if users:
            print(f"\033[1;32m[+] Found {len(users)} users associated with #{hashtag}:\033[0m")
            for user in users:
                print(f"\033[1;36m- {user}\033[0m")
                process_user(user)
        else:
            print(f"\033[1;31m[!] No users found for #{hashtag}.\033[0m")

elif choice == "3":
    # Option 3: Follow WhatsApp Channel
    print("\033[1;33m[*] Opening Ali_Hacker_95's WhatsApp Channel...\033[0m")
    os.system(f"termux-open-url {WHATSAPP_CHANNEL_LINK}")

else:
    print("\033[1;31m[!] Invalid operation. Select 1-3.\033[0m")

print("\033[1;32m[*] Operation Complete by Ali_Hacker_95 🌚💗\033[0m")