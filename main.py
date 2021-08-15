#!/usr/bin/env python3
import csv
import random
import sys

with open(sys.argv[1]) as f:
    csv.register_dialect("my_dialect", skipinitialspace=True)
    reader = csv.DictReader(f, dialect="my_dialect")
    senders = list()
    receivers = list()
    emails = dict()
    for line in reader:
        senders.append(line["Name"])
        receivers.append(line["Name"])
        emails[line["Name"]] = line["Email"]


def create_file_of_presents(senders, receivers):
    HappyOfParticipants = len(senders)
    dict_of_participants = dict()
    for i, j in generate_random_lists(HappyOfParticipants):
        dict_of_participants[senders[i]] = receivers[j]
    return dict_of_participants


def generate_random_lists(length):
    first_list = list(range(length))
    second_list = list(range(length))
    while equality_of_elems(first_list, second_list):
        random.shuffle(first_list)
        random.shuffle(second_list)
    return zip(first_list, second_list)


def equality_of_elems(first_list, second_list):
    for i in range(len(first_list)):
        if first_list[i] == second_list[i]:
            return True
    return False


with open(sys.argv[2], "w", newline='') as f:
    keys = ["Sender", "Sender's e-mail", "Receiver"]
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    people = create_file_of_presents(senders, receivers)
    for i in range(len(senders)):
        writer.writerow({keys[0]: list(people)[i], keys[1]: emails[senders[i]], keys[2]: people[senders[i]]})
