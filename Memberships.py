import csv
from queue import PriorityQueue

buddies = []
peers = []

class Member:

    def __init__(self, firstName, lastName, type, interestsString, interests, commTypesString, commTypes, daysAvailString, daysAvail):
        self.firstName = firstName
        self.lastName = lastName

        self.interestsString = interestsString
        self.interests = interests
        for i in range (18):
            interests.append(0)

        if "Activism and volunteering" in interestsString:
            interests[0] = 1
        if "Animals and pets" in interestsString:
            interests[1] = 1
        if "Arts and crafts" in interestsString:
            interests[2] = 1
        if "Books and reading" in interestsString:
            interests[3] = 1
        if "Comedy" in interestsString:
            interests[4] = 1
        if "Dance" in interestsString:
            interests[5] = 1
        if "Fitness" in interestsString:
            interests[6] = 1
        if "Food" in interestsString:
            interests[7] = 1
        if "Games" in interestsString:
            interests[8] = 1
        if "Movies and TV" in interestsString:
            interests[9] = 1
        if "Music" in interestsString:
            interests[10] = 1
        if "Outdoors" in interestsString:
            interests[11] = 1
        if "Religion" in interestsString:
            interests[12] = 1
        if "Shop" in interestsString:
            interests[13] = 1
        if "Sports" in interestsString:
            interests[14] = 1
        if "Theater" in interestsString:
            interests[15] = 1
        if "Travel" in interestsString:
            interests[16] = 1
        if "Video games" in interestsString:
            interests[17] = 1

        self.commTypesString = commTypesString
        self.commTypes = commTypes
        for i in range (8):
            commTypes.append(0)

        if "E-mail" in commTypesString:
            commTypes[0] = 1
        if "Hanging out together" in commTypesString:
            commTypes[1] = 1
        if "Instant Messenger" in commTypesString:
            commTypes[2] = 1
        if "Social Media" in commTypesString:
            commTypes[3] = 1
        if "Talking on the phone" in commTypesString:
            commTypes[4] = 1
        if "Texting" in commTypesString:
            commTypes[5] = 1
        if "Video chat" in commTypesString:
            commTypes[6] = 1
        if "Write Notes" in commTypesString:
            commTypes[7] = 1

        
        self.daysAvailString = daysAvailString
        self.daysAvail = daysAvail
        for i in range (8):
            daysAvail.append(0)

        if "Monday" in daysAvailString:
            daysAvail[0] = 1
        if "Tuesday" in daysAvailString:
            daysAvail[1] = 1
        if "Wednesday" in daysAvailString:
            daysAvail[2] = 1
        if "Thursday" in daysAvailString:
            daysAvail[3] = 1
        if "Friday" in daysAvailString:
            daysAvail[4] = 1
        if "Saturday" in daysAvailString:
            daysAvail[5] = 1
        if "Sunday" in daysAvailString:
            daysAvail[6] = 1

class Buddy:
    def __init__(self, firstName, lastName, type, interestsString, interests, commTypesString, commTypes, daysAvailString, daysAvail, peerPreferences):
        self.firstName = firstName
        self.lastName = lastName

        self.interestsString = interestsString
        self.interests = interests
        for i in range (18):
            interests.append(0)

        if "Activism and volunteering" in interestsString:
            interests[0] = 1
        if "Animals and pets" in interestsString:
            interests[1] = 1
        if "Arts and crafts" in interestsString:
            interests[2] = 1
        if "Books and reading" in interestsString:
            interests[3] = 1
        if "Comedy" in interestsString:
            interests[4] = 1
        if "Dance" in interestsString:
            interests[5] = 1
        if "Fitness" in interestsString:
            interests[6] = 1
        if "Food" in interestsString:
            interests[7] = 1
        if "Games" in interestsString:
            interests[8] = 1
        if "Movies and TV" in interestsString:
            interests[9] = 1
        if "Music" in interestsString:
            interests[10] = 1
        if "OutdoorFirs" in interestsString:
            interests[11] = 1
        if "Religion" in interestsString:
            interests[12] = 1
        if "Shop" in interestsString:
            interests[13] = 1
        if "Sports" in interestsString:
            interests[14] = 1
        if "Theater" in interestsString:
            interests[15] = 1
        if "Travel" in interestsString:
            interests[16] = 1
        if "Video games" in interestsString:
            interests[17] = 1

        self.commTypesString = commTypesString
        self.commTypes = commTypes
        for i in range (8):
            commTypes.append(0)

        if "E-mail" in commTypesString:
            commTypes[0] = 1
        if "Hanging out together" in commTypesString:
            commTypes[1] = 1
        if "Instant Messenger" in commTypesString:
            commTypes[2] = 1
        if "Social Media" in commTypesString:
            commTypes[3] = 1
        if "Talking on the phone" in commTypesString:
            commTypes[4] = 1
        if "Texting" in commTypesString:
            commTypes[5] = 1
        if "Video chat" in commTypesString:
            commTypes[6] = 1
        if "Write Notes" in commTypesString:
            commTypes[7] = 1

        
        self.daysAvailString = daysAvailString
        self.daysAvail = daysAvail
        for i in range (8):
            daysAvail.append(0)

        if "Monday" in daysAvailString:
            daysAvail[0] = 1
        if "Tuesday" in daysAvailString:
            daysAvail[1] = 1
        if "Wednesday" in daysAvailString:
            daysAvail[2] = 1
        if "Thursday" in daysAvailString:
            daysAvail[3] = 1
        if "Friday" in daysAvailString:
            daysAvail[4] = 1
        if "Saturday" in daysAvailString:
            daysAvail[5] = 1
        if "Sunday" in daysAvailString:
            daysAvail[6] = 1

        self.peerPreferences = peerPreferences



def PeerPreferences(buddies, peers):
    commonalities = 0
    for buddy in range(len(buddies)):
        for peer in range(len(peers)):
            for interest in buddies[buddy].interests:
                if buddies[buddy].interests[interest] == peers[peer].interests[interest]:
                    commonalities+=1
            buddies[buddy].peerPreferences.put((commonalities, peers[peer]))

PeerPreferences(buddies, peers)

while not buddies[0].peerPreferences.empty():
    next_item = buddies[0].peerPreferences.get()
    print(next_item)

# PeerPreferences(buddies, peers)
# for r in range(len(buddi es)+1):
#     print(r)
#     for c in range(len(peers)+1):
#         print(c)
#         print(preferences[r][c])


def Matching(buddies, peers):
    AvailableBuddies = []
    for buddy in buddies:
        AvailableBuddies.append(buddy)
    for peer in peers:
        peer.available = True
    while AvailableBuddies.length() > 0:
        for buddy in buddies:
            buddy.request = buddies[buddy].peerPreferences.get()
            if peer.available:
                buddy.match = buddies[buddy].peerPreferences.get()

# for b in buddies:
#     print(b.firstName + " " + str(b.interests) + " " + str(b.commTypes) + " " + str(b.daysAvail))

# for b in peers:
#     print(b.firstName + " " + str(b.interests) + " " + str(b.commTypes) + " " + str(b.daysAvail))

def main():
  
    with open('MatchingInfo.csv', 'rt', encoding="UTF-8", errors='ignore') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            if row["Interested in a Match"] == "Yes":
                if row["IDD?"] == "Yes":
                    buddies.append(Buddy(row["First Name"], row["Last Name"], "Buddy", row["Matching Survey Interests"], [], row["Matching Survey Communication Types"], [], row["Matching Survey Days Available"], [], PriorityQueue()))
                else:
                    peers.append(Member(row["First Name"], row["Last Name"], "Peer", row["Matching Survey Interests"], [], row["Matching Survey Communication Types"], [], row["Matching Survey Days Available"], []))


if __name__ == "__main__":
    main()    
